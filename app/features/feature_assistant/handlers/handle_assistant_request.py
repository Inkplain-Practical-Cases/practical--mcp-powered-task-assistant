# One orchestrator joins deterministic intent interpretation with live MCP calls.
# Future hosted LLM planners must produce the same typed ActionPlan contract.
from mcp import ClientSession
from app.features.feature_assistant.services.service_interpret_request import service_interpret_request
from app.features.feature_assistant.services.service_execute_action_plan import service_execute_action_plan

async def handle_assistant_request(session: ClientSession, message: str) -> list[dict]:
    plan = service_interpret_request(message)
    return await service_execute_action_plan(session, plan)
