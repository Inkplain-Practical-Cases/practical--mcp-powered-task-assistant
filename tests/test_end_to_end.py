# Final happy path and server error checks over a real MCP stdio session.
import asyncio
from datetime import date, timedelta
from app.client.mcp_gateway import MCPGateway
from app.features.feature_assistant.handlers.handle_assistant_request import handle_assistant_request
from app.features.feature_invocation.services.service_invoke_tool import service_invoke_tool

REQUEST = "Create a task to review the customer report tomorrow and show my upcoming meetings"

async def verify_final() -> None:
    async with MCPGateway().connect() as session:
        reply = await handle_assistant_request(session, REQUEST)
        assert len(reply) == 2
        assert reply[0]["tool"] == "create_task"
        assert reply[1]["tool"] == "list_calendar_events"
        events = await service_invoke_tool(session, "list_calendar_events", {"limit": 2})
        assert events

def test_end_to_end_offline_mcp() -> None:
    asyncio.run(verify_final())
