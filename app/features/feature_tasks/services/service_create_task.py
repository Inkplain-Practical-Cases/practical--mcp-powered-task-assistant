"""Validate a typed MCP task and delegate creation to an injected provider."""
from typing import Protocol
from app.features.feature_tasks.schemas.task_schema import TaskCreate

class TaskStore(Protocol):
    async def create(self, payload: TaskCreate) -> dict: ...

async def service_create_task(title: str, due_date: str, priority: str, store: TaskStore) -> dict:
    task = TaskCreate.model_validate({"title": title, "due_date": due_date, "priority": priority})
    return await store.create(task)
