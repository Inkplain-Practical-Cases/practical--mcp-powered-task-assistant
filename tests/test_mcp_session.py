# Real MCP stdio integration: discover and invoke server_status.
# A child process runs the exact same server that learners start in the CLI.
import asyncio
import json
import sys
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def check_server() -> None:
    parameters = StdioServerParameters(command=sys.executable, args=["-m", "app.main"])
    async with stdio_client(parameters) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            tools = await session.list_tools()
            names = [tool.name for tool in tools.tools]
            assert "server_status" in names
            response = await session.call_tool("server_status", arguments={})
            assert not response.isError
            assert response.content
            assert "ok" in " ".join(getattr(x, "text", "") for x in response.content)

def test_real_mcp_status() -> None:
    asyncio.run(check_server())
