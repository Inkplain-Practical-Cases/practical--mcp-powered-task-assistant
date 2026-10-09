# Step 2 of 6 — Define task and calendar tools
## What you build in this step
The real MCP server now exposes create_task and list_calendar_events, using validated local task and calendar providers.
## What you learn
Tool registration, Pydantic schema boundaries, async service→provider calls and fake calendar data.
## What changed since step 1
Nine added CRD components and the MCP server tool registry extended to three tools.
## Run it
```bash
python -m pip install -r requirements.txt
python -m pytest -q
python -m app.main
```
## Verify it
MCP subprocess integration discovers the tools and calls each. Pydantic rejects empty task titles, past dates and unknown priority values. Calendar limits must be 1–20.
## Diagram
Simulator tab STEP-2 is a separate Stage-3 deliverable.
## Next
Build a reusable MCP client for real server sessions and dynamic tool discovery.
