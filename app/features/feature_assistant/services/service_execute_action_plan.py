# Execute approved MCP actions with bounded waiting per tool invocation.
# Only server-discovered tools can run and execution remains ordered.
import asyncio
from mcp import ClientSession
from app.features.feature_assistant.schemas.action_plan import ActionPlan
from app.features.feature_invocation.services.service_invoke_tool import service_invoke_tool
from app.core.config import get_tool_timeout_seconds
from app.core.observability import log_tool_event

async def service_execute_action_plan(session: ClientSession, plan: ActionPlan) -> list[dict]:
    results: list[dict] = []
    for action in plan.actions:
        try:
            result = await asyncio.wait_for(
                service_invoke_tool(session, action.name, action.arguments),
                timeout=get_tool_timeout_seconds(),
            )
        except asyncio.TimeoutError:
            log_tool_event("tool_timeout", action.name)
            raise
        except Exception:
            # Avoid leaking customer task names or raw MCP server text into logs.
            log_tool_event("tool_failed", action.name)
            raise
        else:
            log_tool_event("tool_completed", action.name)
            results.append({"tool": action.name, "result": result})
    return results
