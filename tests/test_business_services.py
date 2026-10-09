# Fast offline tests exercise service-level validation without MCP transport.
import asyncio
from datetime import date, timedelta
import pytest
from pydantic import ValidationError
from app.providers.tasks.in_memory_task_store import InMemoryTaskStore
from app.providers.calendar.fake_calendar_provider import FakeCalendarProvider
from app.features.feature_tasks.services.service_create_task import service_create_task
from app.features.feature_calendar.services.service_list_calendar_events import service_list_calendar_events

def test_create_task_valid() -> None:
    store = InMemoryTaskStore()
    tomorrow = (date.today() + timedelta(days=1)).isoformat()
    result = asyncio.run(service_create_task("Review report", tomorrow, "urgent", store))
    assert result["id"] == 1 and result["priority"] == "urgent" and result["status"] == "open"

@pytest.mark.parametrize("title,days,priority", [
    ("", 1, "normal"), ("Valid title", -1, "normal"), ("Valid title", 1, "critical"),
])
def test_invalid_task(title: str, days: int, priority: str) -> None:
    store = InMemoryTaskStore()
    due = (date.today() + timedelta(days=days)).isoformat()
    with pytest.raises(ValidationError):
        asyncio.run(service_create_task(title, due, priority, store))

def test_calendar_limit_and_future_dates() -> None:
    entries = service_list_calendar_events(2, FakeCalendarProvider())
    assert len(entries) == 2
    assert entries[0]["date"] > date.today().isoformat()
    with pytest.raises(ValueError):
        service_list_calendar_events(0, FakeCalendarProvider())
