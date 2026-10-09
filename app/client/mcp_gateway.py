# Client-side stdio session gateway; protocol lifecycle is handled here.
# Without this boundary each feature would need to spawn and initialize MCP itself.
import sys
from contextlib import asynccontextmanager
from collections.abc import AsyncIterator
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

class MCPGateway:
    def __init__(self, server_module: str = "app.main") -> None:
        self.server_module = server_module

    @asynccontextmanager
    async def connect(self) -> AsyncIterator[ClientSession]:
        # The subprocess is the exact server used by this practical case.
        params = StdioServerParameters(command=sys.executable, args=["-m", self.server_module])
        async with stdio_client(params) as (read_stream, write_stream):
            async with ClientSession(read_stream, write_stream) as session:
                # initialize() negotiates MCP capabilities before any tool call.
                await session.initialize()
                yield session
