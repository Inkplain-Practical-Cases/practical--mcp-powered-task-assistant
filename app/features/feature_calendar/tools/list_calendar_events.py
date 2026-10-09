# Public read-only MCP tool for upcoming mock calendar events.
from app.core.dependencies import get_calendar_provider
from app.features.feature_calendar.services.service_list_calendar_events import service_list_calendar_events

async def list_calendar_events(limit: int = 3) -> list[dict]:
    """List upcoming mock meetings; limit must be between 1 and 20."""
    return service_list_calendar_events(limit, get_calendar_provider())
