# Developer CLI shows all real tools exposed by an MCP subprocess.
# Run: python -m app.client.discover_cli
import asyncio
import json
from app.client.mcp_gateway import MCPGateway
from app.features.feature_discovery.services.service_discover_tools import service_discover_tools

async def main() -> None:
    gateway = MCPGateway()
    async with gateway.connect() as session:
        tools = await service_discover_tools(session)
        print(json.dumps(tools, indent=2))

if __name__ == "__main__":
    asyncio.run(main())
