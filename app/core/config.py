# Validates the maximum number of seconds to wait for each MCP tool call.
# Values are environment-backed and can be tuned for local demos.
import os

def get_tool_timeout_seconds() -> float:
    value = float(os.environ.get("MCP_TOOL_TIMEOUT_SECONDS", "8"))
    if not 0 < value <= 60:
        raise ValueError("MCP_TOOL_TIMEOUT_SECONDS must be > 0 and <= 60")
    return value
