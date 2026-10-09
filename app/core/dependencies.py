# Cached local data adapters shared by MCP tools in one server process.
# In step 2 no external task or calendar accounts are required.
from functools import lru_cache
from app.providers.tasks.in_memory_task_store import InMemoryTaskStore
from app.providers.calendar.fake_calendar_provider import FakeCalendarProvider

@lru_cache
def get_task_store() -> InMemoryTaskStore:
    # Share task IDs across calls in the same long-running stdio session.
    return InMemoryTaskStore()

@lru_cache
def get_calendar_provider() -> FakeCalendarProvider:
    # Calendar entries are deterministic, generated relative to today's date.
    return FakeCalendarProvider()
