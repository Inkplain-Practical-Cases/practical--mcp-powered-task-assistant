# Orchestrates a natural request with safe failure messages for external clients.
# The CLI may catch the exception without exposing a raw protocol traceback.
import asyncio
from mcp import ClientSession
from app.features.feature_assistant.services.service_interpret_request import service_interpret_request
from app.features.feature_assistant.services.service_execute_action_plan import service_execute_action_plan

async def handle_assistant_request(session: ClientSession, message: str) -> list[dict]:
    plan = service_interpret_request(message)
    try:
        return await service_execute_action_plan(session, plan)
    except asyncio.TimeoutError as exc:
        raise RuntimeError("Task service timed out") from exc
    except Exception as exc:
        raise RuntimeError("Task service temporarily unavailable") from exc
