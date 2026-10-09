# MCP assembly door registers the complete explicit tool allowlist.
# Tool business logic belongs to dedicated feature services and providers.
from mcp.server.fastmcp import FastMCP
from app.features.feature_status.tools.server_status import server_status
from app.features.feature_tasks.tools.create_task import create_task
from app.features.feature_calendar.tools.list_calendar_events import list_calendar_events

server = FastMCP("Northstar Task Assistant")
server.tool(name="server_status", description="Return MCP server status")(server_status)
server.tool(name="create_task", description="Create a mock work task with validated fields")(create_task)
server.tool(name="list_calendar_events", description="List upcoming local calendar events")(list_calendar_events)
