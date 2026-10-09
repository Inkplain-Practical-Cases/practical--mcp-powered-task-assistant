# Public MCP tool: accept user fields, delegate business rules to service.
# No direct state changes or SDK client construction inside the tool door.
from app.core.dependencies import get_task_store
from app.features.feature_tasks.services.service_create_task import service_create_task

async def create_task(title: str, due_date: str, priority: str = "normal") -> dict:
    """Create a work task. due_date uses YYYY-MM-DD; priority is normal or urgent."""
    return await service_create_task(title, due_date, priority, get_task_store())
