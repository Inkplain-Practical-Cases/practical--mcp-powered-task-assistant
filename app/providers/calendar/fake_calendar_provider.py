# Read-only local calendar fixture; this never calls Google Calendar.
from datetime import date, timedelta

class FakeCalendarProvider:
    def list_events(self, limit: int) -> list[dict]:
        today = date.today()
        events = [
            {"id": "evt-1", "title": "Support standup", "date": (today + timedelta(days=1)).isoformat()},
            {"id": "evt-2", "title": "Customer review", "date": (today + timedelta(days=2)).isoformat()},
            {"id": "evt-3", "title": "Engineering planning", "date": (today + timedelta(days=7)).isoformat()},
        ]
        return events[:limit]
