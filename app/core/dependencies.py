"""Shared, cached adapters for the real local MCP tool server."""
from functools import lru_cache
from app.providers.tasks.sqlite_task_store import SQLiteTaskStore
from app.providers.calendar.fake_calendar_provider import FakeCalendarProvider

@lru_cache
def get_task_store() -> SQLiteTaskStore:
    """Return the same durable adapter throughout this MCP server process."""
    return SQLiteTaskStore()

@lru_cache
def get_calendar_provider() -> FakeCalendarProvider:
    """Keep calendar events deterministic for the educational fixture."""
    return FakeCalendarProvider()
