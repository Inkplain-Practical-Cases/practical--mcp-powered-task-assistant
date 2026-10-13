"""Durable local SQLite task adapter for the MCP create_task tool.

Each created task is stored with one immutable creation event; no secrets are logged.
"""
import asyncio
import os
import sqlite3
from pathlib import Path
from app.features.feature_tasks.schemas.task_schema import TaskCreate

class SQLiteTaskStore:
    """Injectable async adapter whose SQLite I/O runs outside the event loop."""
    def __init__(self, db_path: str | None = None) -> None:
        self.path = db_path or os.getenv("INKPLAIN_TASK_DB", "data/mcp_tasks.sqlite3")
        self._lock = asyncio.Lock()

    def _insert(self, payload: TaskCreate) -> dict:
        # Resolve the file only when an operation actually needs persistence.
        Path(self.path).parent.mkdir(parents=True, exist_ok=True)
        with sqlite3.connect(self.path) as connection:
            connection.execute("PRAGMA foreign_keys = ON")
            connection.execute("""CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                due_date TEXT NOT NULL,
                priority TEXT NOT NULL,
                status TEXT NOT NULL
            )""")
            connection.execute("""CREATE TABLE IF NOT EXISTS task_events (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                task_id INTEGER NOT NULL REFERENCES tasks(id),
                event_type TEXT NOT NULL,
                occurred_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            )""")
            # Parameterized inserts ensure task text cannot become SQL code.
            cursor = connection.execute(
                "INSERT INTO tasks (title, due_date, priority, status) VALUES (?, ?, ?, ?)",
                (payload.title, payload.due_date.isoformat(), payload.priority, "open"),
            )
            task_id = cursor.lastrowid
            connection.execute(
                "INSERT INTO task_events (task_id, event_type) VALUES (?, ?)",
                (task_id, "created"),
            )
        return {"id": task_id, **payload.model_dump(mode="json"), "status": "open"}

    async def create(self, payload: TaskCreate) -> dict:
        # The lock serializes operations in this MCP server session.
        async with self._lock:
            return await asyncio.to_thread(self._insert, payload)
