# Developer CLI: invoke create_task then list_calendar_events through real MCP.
import asyncio
import json
from datetime import date, timedelta
from app.client.mcp_gateway import MCPGateway
from app.features.feature_invocation.services.service_invoke_tool import service_invoke_tool

async def main() -> None:
    tomorrow = (date.today() + timedelta(days=1)).isoformat()
    async with MCPGateway().connect() as session:
        task = await service_invoke_tool(session, "create_task", {
            "title": "Review report", "due_date": tomorrow, "priority": "normal"
        })
        events = await service_invoke_tool(session, "list_calendar_events", {"limit": 2})
        print(json.dumps({"task": task, "events": events}, indent=2))

if __name__ == "__main__":
    asyncio.run(main())
