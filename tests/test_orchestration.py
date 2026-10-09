# Offline grammar and real two-tool invocation tests.
import asyncio
import pytest
from app.client.mcp_gateway import MCPGateway
from app.features.feature_assistant.services.service_interpret_request import service_interpret_request
from app.features.feature_assistant.handlers.handle_assistant_request import handle_assistant_request

EXAMPLE = "Create a task to review the customer report tomorrow and show my upcoming meetings"

def test_parser_plans_two_known_tools() -> None:
    plan = service_interpret_request(EXAMPLE)
    assert [action.name for action in plan.actions] == ["create_task", "list_calendar_events"]
    assert plan.actions[0].arguments["title"] == "review the customer report"

@pytest.mark.parametrize("text", ["Delete all my tasks", "Hello", "Create task x"])
def test_unsupported_or_ambiguous_request_is_rejected(text: str) -> None:
    with pytest.raises(ValueError):
        service_interpret_request(text)

async def verify_end_to_end() -> None:
    async with MCPGateway().connect() as session:
        outputs = await handle_assistant_request(session, EXAMPLE)
        assert [x["tool"] for x in outputs] == ["create_task", "list_calendar_events"]
        assert outputs[0]["result"]
        assert outputs[1]["result"]

def test_two_tool_mcp_plan() -> None:
    asyncio.run(verify_end_to_end())
