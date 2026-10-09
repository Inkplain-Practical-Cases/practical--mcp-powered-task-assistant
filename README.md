# MCP-Powered Task Assistant — Step 5
A deterministic offline interpreter turns one natural-language request into an explicit ActionPlan. The handler executes `create_task` then `list_calendar_events` inside the same real MCP session. This is a teaching intent parser, not a claim of full LLM understanding.
```bash
python -m pip install -r requirements.txt
python -m pytest -q
python -m app.client.assistant_cli
```
Unsafe or unsupported requests fail before any tool call; MCP inputs and outputs are validated in Step 4's services.
