# Developer CLI for a two-operation request through one shared MCP session.
import asyncio
import json
from app.client.mcp_gateway import MCPGateway
from app.features.feature_assistant.handlers.handle_assistant_request import handle_assistant_request

async def main() -> None:
    request = "Create a task to review the customer report tomorrow and show my upcoming meetings"
    async with MCPGateway().connect() as session:
        result = await handle_assistant_request(session, request)
        print(json.dumps(result, indent=2))

if __name__ == "__main__":
    asyncio.run(main())
