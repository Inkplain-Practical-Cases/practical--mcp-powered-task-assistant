# Validates limits and calls the read-only calendar provider.
from app.providers.calendar.fake_calendar_provider import FakeCalendarProvider

def service_list_calendar_events(limit: int, provider: FakeCalendarProvider) -> list[dict]:
    if not 1 <= limit <= 20:
        raise ValueError("limit must be between 1 and 20")
    return provider.list_events(limit)
