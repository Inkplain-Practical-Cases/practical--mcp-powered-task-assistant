# MCP server assembly door: declares which public tools are exposed.
# Why: services stay independent of the MCP transport and protocol lifecycle.
from mcp.server.fastmcp import FastMCP
from app.features.feature_status.tools.server_status import server_status

server = FastMCP("Northstar Task Assistant")
# Only explicitly registered functions may be called by connected MCP clients.
server.tool(name="server_status", description="Return the task assistant server status")(server_status)
