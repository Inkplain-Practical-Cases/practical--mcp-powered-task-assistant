# Dynamically discover tools, validate arguments, call MCP and parse response.
# Never call a name that was not returned by the live server tools/list.
from mcp import ClientSession
from app.features.feature_discovery.services.service_discover_tools import service_discover_tools
from app.features.feature_invocation.services.service_validate_arguments import service_validate_arguments
from app.features.feature_invocation.services.service_parse_tool_result import service_parse_tool_result

async def service_invoke_tool(session: ClientSession, name: str, arguments: dict) -> dict:
    tools = await service_discover_tools(session)
    service_validate_arguments(name, arguments, tools)
    reply = await session.call_tool(name, arguments=arguments)
    return service_parse_tool_result(name, reply)
