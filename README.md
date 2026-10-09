# MCP-Powered Task Assistant

Practical Case **2/6** for beginner Forward Deployed Engineers at fictional Northstar Operations.

A working Python MCP client/server teaches tool registration, discovery and safe invocation. Users can request a mock task and upcoming calendar entries in one natural-language message. Real MCP protocol runs over **stdio**; calendar and tasks use **offline local adapters**. No hosted LLM or Google account is required. The interpreter is a deterministic teaching baseline, not a full general-purpose language model.

## Six cumulative teaching branches

| Step | Branch | New capability |
|---|---|---|
| 1 | step-01-create-basic-mcp-server | Local stdio MCP server, server_status tool |
| 2 | step-02-define-task-and-calendar-tools | create_task, list_calendar_events, validated fake services |
| 3 | step-03-build-mcp-client-and-discover-tools | Real MCP ClientSession and dynamic tools/list |
| 4 | step-04-invoke-tools-and-validate-results | JSON-Schema check, call_tool and error handling |
| 5 | step-05-orchestrate-natural-language-requests | Typed ActionPlan, deterministic two-tool workflow |
| 6 | step-06-harden-and-verify | Per-tool timeouts, safe logs and end-to-end pytest |

Each branch has its own `STEP-N.crd` and `STEP-N.md` at the root, describing only the complete state of that branch. The final `main` branch holds `FINAL.crd` and this README. The separate six-tab `.inkp` Simulator file is **Stage 3**, not created in this repository stage.

## Install & run (Python 3.12+)

```bash
git clone https://github.com/Inkplain-Practical-Cases/practical--mcp-powered-task-assistant.git
cd practical--mcp-powered-task-assistant
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
python -m pip install -r requirements.txt
python -m pytest -q
```

To start the server for an MCP client:
```bash
python -m app.main
```
The MCP server uses **stdio** rather than HTTP. It waits for MCP JSON-RPC messages on stdin; do not expect a web page or print logs to stdout. For a usable client demo, start a new terminal:
```bash
python -m app.client.discover_cli
python -m app.client.invoke_cli
python -m app.client.assistant_cli
```
Each client starts its own short-lived server child process, negotiates a session and closes it safely. The final CLI translates the following sample input into two typed MCP actions:

> Create a task to review the customer report tomorrow and show my upcoming meetings.

It creates a local task, then lists deterministic mock calendar events. Task data belongs only to that child server process: restarting the client resets the in-memory task list. It does not touch real calendars.

## Architecture (Inkplain Codebase Structure)

- `app/server.py` registers approved MCP tools; `app/main.py` starts stdio.
- `app/features/feature_tasks/tools/create_task.py` → `service_create_task.py` → `InMemoryTaskStore`.
- `app/features/feature_calendar/tools/list_calendar_events.py` → `service_list_calendar_events.py` → `FakeCalendarProvider`.
- `app/client/mcp_gateway.py` owns MCP client session initialization/cleanup.
- `service_discover_tools.py` calls `tools/list` and returns JSON input schemas.
- `service_invoke_tool.py` verifies allowed tool names, checks arguments against discovered JSON Schema, calls MCP and rejects `isError`.
- `service_interpret_request.py` produces a limited `ActionPlan`; the handler executes known actions sequentially, with bounded timeout and safe event logging.

## Security and validation

Tool names and schemas are obtained from the MCP server; unsupported tools and arguments are rejected. Task title, date and priority have separate Pydantic validation on the server. Dates must use YYYY-MM-DD and cannot be in the past. Calendar list limit is 1–20. Unknown natural-language intentions do not execute arbitrary operations. There is no production authentication or authorization in this teaching app; never expose these tools to untrusted network clients without adding them.

`MCP_TOOL_TIMEOUT_SECONDS` defaults to 8. Change it through the environment if needed (0 < timeout ≤ 60). Never commit keys; see `.env.example`.

## Tests and CI

```bash
python -m pytest -q
```

Pure unit tests cover provider behavior, task validation, intent parser, tool result handling, timeouts and logs. MCP integration tests spawn the real server via stdio, negotiate a session and invoke tools. GitHub Actions is configured to run pytest across **every step branch and main**, not only main.

## Case study and simulator

The canonical Component Relation Diagram is `FINAL.crd`, generated from the actual sources, and each teaching branch contains its matching `STEP-N.crd`. The six-tab Simulator `mcp-powered-task-assistant.inkp` is intentionally reserved for Stage 3 after the user's authorization.
