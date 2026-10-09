# One job: validate a requested task, then store it using an injected adapter.
# A real task service can replace the in-memory adapter without changing the tool.
from app.features.feature_tasks.schemas.task_schema import TaskCreate
from app.providers.tasks.in_memory_task_store import InMemoryTaskStore

async def service_create_task(title: str, due_date: str, priority: str, store: InMemoryTaskStore) -> dict:
    task = TaskCreate.model_validate({"title": title, "due_date": due_date, "priority": priority})
    return await store.create(task)
