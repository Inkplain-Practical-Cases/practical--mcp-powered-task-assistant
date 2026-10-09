# Execute only typed, known actions through the already validated MCP client.
# Ordering is intentional: create the task first, then list events.
from mcp import ClientSession
from app.features.feature_assistant.schemas.action_plan import ActionPlan
from app.features.feature_invocation.services.service_invoke_tool import service_invoke_tool

async def service_execute_action_plan(session: ClientSession, plan: ActionPlan) -> list[dict]:
    outputs: list[dict] = []
    for action in plan.actions:
        result = await service_invoke_tool(session, action.name, action.arguments)
        outputs.append({"tool": action.name, "result": result})
    return outputs
