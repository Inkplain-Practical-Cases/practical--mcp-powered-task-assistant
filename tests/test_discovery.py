# Exercises real MCP negotiation and tool discovery via the shared gateway.
import asyncio
from app.client.mcp_gateway import MCPGateway
from app.features.feature_discovery.services.service_discover_tools import service_discover_tools

async def verify() -> None:
    async with MCPGateway().connect() as session:
        tools = await service_discover_tools(session)
        found = {t["name"] for t in tools}
        assert {"server_status", "create_task", "list_calendar_events"} <= found
        for tool in tools:
            assert isinstance(tool["input_schema"], dict)
        task = next(t for t in tools if t["name"] == "create_task")
        assert "title" in task["input_schema"]["properties"]
        assert "due_date" in task["input_schema"]["properties"]

def test_tool_discovery() -> None:
    asyncio.run(verify())
