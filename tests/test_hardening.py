# Bounded MCP operation time and safe errors are tested without network calls.
import asyncio
import json
import pytest
from app.core.config import get_tool_timeout_seconds
from app.core.observability import log_tool_event
from app.features.feature_assistant.schemas.action_plan import Action, ActionPlan
from app.features.feature_assistant.services import service_execute_action_plan as execution
from app.features.feature_assistant.handlers import handle_assistant_request as handler

def test_timeout_configuration(monkeypatch) -> None:
    monkeypatch.setenv("MCP_TOOL_TIMEOUT_SECONDS", "0")
    with pytest.raises(ValueError):
        get_tool_timeout_seconds()
    monkeypatch.setenv("MCP_TOOL_TIMEOUT_SECONDS", "0.01")
    assert get_tool_timeout_seconds() == 0.01

def test_safe_structured_event(caplog) -> None:
    with caplog.at_level("INFO", logger="northstar.task_assistant"):
        log_tool_event("tool_completed", "create_task")
    parsed = json.loads(caplog.records[-1].message)
    assert parsed == {"event": "tool_completed", "tool": "create_task"}

def test_tool_timeout(monkeypatch) -> None:
    async def slow_call(*args, **kwargs):
        await asyncio.sleep(0.08)
        return {"id": 1}
    monkeypatch.setattr(execution, "service_invoke_tool", slow_call)
    monkeypatch.setenv("MCP_TOOL_TIMEOUT_SECONDS", "0.01")
    plan = ActionPlan(actions=[Action(name="create_task", arguments={})])
    with pytest.raises(asyncio.TimeoutError):
        asyncio.run(execution.service_execute_action_plan(None, plan))

def test_handler_rejects_unsupported_language_without_calls(monkeypatch) -> None:
    async def never_call(*args, **kwargs):
        raise AssertionError("MCP should not run an unsupported action")
    monkeypatch.setattr(handler, "service_execute_action_plan", never_call)
    with pytest.raises(ValueError):
        asyncio.run(handler.handle_assistant_request(None, "Delete every calendar event"))
