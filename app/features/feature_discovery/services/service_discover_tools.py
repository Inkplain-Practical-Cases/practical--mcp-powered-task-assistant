# Reads registered server tools via MCP instead of hardcoding a tool list.
# Result contains names and JSON input schemas for subsequent safe invocation.
from mcp import ClientSession

async def service_discover_tools(session: ClientSession) -> list[dict]:
    response = await session.list_tools()
    return [{"name": t.name, "description": t.description or "",
             "input_schema": t.inputSchema} for t in response.tools]
