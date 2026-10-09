# Logs events with no task title, calendar details, token or customer text.
# In production use a structured log shipper and a correlation ID.
import json
import logging

logger = logging.getLogger("northstar.task_assistant")

def log_tool_event(event: str, tool_name: str | None = None) -> None:
    logger.info(json.dumps({"event": event, "tool": tool_name}))
