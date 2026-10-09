# Offline task repository with sequential IDs and concurrency protection.
# No task state survives restart or spans independent MCP processes.
import asyncio
from app.features.feature_tasks.schemas.task_schema import TaskCreate

class InMemoryTaskStore:
    def __init__(self) -> None:
        self._lock = asyncio.Lock()
        self._items: list[dict] = []

    async def create(self, payload: TaskCreate) -> dict:
        async with self._lock:
            # Increment while locked: concurrent tasks never share the same ID.
            record = {"id": len(self._items) + 1, **payload.model_dump(mode="json"), "status": "open"}
            self._items.append(record)
            return record.copy()
