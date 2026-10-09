# Covers a successful real MCP operation, schema errors and unknown tools.
import asyncio
from datetime import date, timedelta
import pytest
from app.client.mcp_gateway import MCPGateway
from app.features.feature_invocation.services.service_invoke_tool import service_invoke_tool
from app.features.feature_invocation.services.service_validate_arguments import service_validate_arguments

def test_schema_validation_before_call() -> None:
    tools = [{"name": "create_task", "input_schema": {
        "type": "object", "properties": {"title": {"type": "string"}},
        "required": ["title"], "additionalProperties": False
    }}]
    with pytest.raises(ValueError, match="Invalid"):
        service_validate_arguments("create_task", {}, tools)
    with pytest.raises(ValueError, match="Unknown"):
        service_validate_arguments("delete_everything", {}, tools)

async def check_real_invocation() -> None:
    async with MCPGateway().connect() as session:
        tomorrow = (date.today() + timedelta(days=1)).isoformat()
        task = await service_invoke_tool(session, "create_task", {
            "title": "Review customer report", "due_date": tomorrow, "priority": "urgent"
        })
        assert task
        event_list = await service_invoke_tool(session, "list_calendar_events", {"limit": 2})
        assert event_list
        with pytest.raises(ValueError, match="Unknown"):
            await service_invoke_tool(session, "unknown_tool", {})

def test_live_client_tool_invocation() -> None:
    asyncio.run(check_real_invocation())
