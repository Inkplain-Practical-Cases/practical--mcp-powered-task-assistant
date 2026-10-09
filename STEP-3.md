# Step 3 of 6 — Build MCP client and discover tools
## What you build in this step
A reusable MCPGateway that launches the server as a child process, negotiates ClientSession and calls tools/list.
## What you learn
- stdio transport and client session lifecycle
- capability negotiation and tool discovery through MCP
- tool input schemas and avoiding hard-coded capability registries
## What changed since step 2
MCPGateway, service_discover_tools and discover_cli are added.
## Run it
```bash
python -m pip install -r requirements.txt
python -m pytest -q
python -m app.client.discover_cli
```
## Verify it
Tests confirm all three tools exist and create_task has a JSON schema with title/due_date. Closing the context terminates the child process.
## Diagram
CRD STEP-3 describes discovery; Stage 3 later renders this as the STEP-3 tab.
## Next
Implement and validate client tool invocation and server errors.
