"""Exercise real durable task persistence with a linked creation event."""
import asyncio
import sqlite3
from datetime import date, timedelta
from app.providers.tasks.sqlite_task_store import SQLiteTaskStore
from app.features.feature_tasks.services.service_create_task import service_create_task

def test_task_and_event_survive_new_adapter(tmp_path):
    database = str(tmp_path / "tasks.sqlite3")
    due = (date.today() + timedelta(days=1)).isoformat()
    first = asyncio.run(service_create_task("Prepare release notes", due, "normal", SQLiteTaskStore(database)))
    second = asyncio.run(service_create_task("Review deployment plan", due, "urgent", SQLiteTaskStore(database)))
    assert (first["id"], second["id"]) == (1, 2)
    with sqlite3.connect(database) as connection:
        assert connection.execute("SELECT COUNT(*) FROM tasks").fetchone()[0] == 2
        assert connection.execute("SELECT COUNT(*) FROM task_events").fetchone()[0] == 2
        assert connection.execute("PRAGMA foreign_key_check").fetchall() == []
