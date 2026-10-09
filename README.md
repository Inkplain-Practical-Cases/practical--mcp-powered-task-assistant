# MCP-Powered Task Assistant — Step 6
This branch contains a complete **offline, real MCP task assistant**: client session, live tool discovery, schema-safe invocation, typed offline action plan, task/calendar tools, bounded timeouts and error/event logging.
```bash
python -m pip install -r requirements.txt
python -m pytest -q
python -m app.client.assistant_cli
```
No external account or API key is used. Task data is memory-only, so restarting the stdio server resets it.
