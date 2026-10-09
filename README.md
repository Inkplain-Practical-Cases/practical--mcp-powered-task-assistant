# MCP-Powered Task Assistant — Step 3
The MCP server provides real tools; now `MCPGateway` starts a child process, initializes `ClientSession` and discovers tool definitions dynamically.
```bash
python -m pip install -r requirements.txt
python -m pytest -q
python -m app.client.discover_cli
```
The CLI prints tool names and input schemas. The client does not hardcode registered tool names; it queries them using `tools/list`.
