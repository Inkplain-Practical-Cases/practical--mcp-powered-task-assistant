# Converts an MCP result into application data, rejecting tool-side errors.
# The model/client cannot report a rejected operation as successful.
import json
from mcp.types import CallToolResult

def service_parse_tool_result(name: str, response: CallToolResult) -> dict:
    if response.isError:
        raise ValueError(f"MCP tool {name} reported an error")
    structured = getattr(response, "structuredContent", None)
    if isinstance(structured, dict):
        return structured
    text = "\n".join(getattr(block, "text", "") for block in response.content)
    try:
        value = json.loads(text)
    except json.JSONDecodeError:
        # Text-only tools can legitimately return text.
        value = {"text": text}
    return value if isinstance(value, dict) else {"result": value}
