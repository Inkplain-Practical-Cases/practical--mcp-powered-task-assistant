# MCP-Powered Task Assistant — Step 2
Three MCP tools are now exposed: server_status, create_task, list_calendar_events.
## Run
```bash
python -m pip install -r requirements.txt
python -m pytest -q
python -m app.main
```
The stdio server intentionally waits for MCP messages and must not write arbitrary text to stdout. The integration tests create the MCP client subprocess themselves. Task dates are `YYYY-MM-DD` today or later, and the calendar is a local fixture; no real accounts are changed.
