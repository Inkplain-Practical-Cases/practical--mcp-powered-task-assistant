# Step 1 of 6 — Create basic MCP server
## What you build in this step
A runnable MCP Python SDK server on local stdio, with one discoverable `server_status` tool. An integration test is the first MCP client.
## What you learn
- Difference between server bootstrap, public tool and business service
- MCP initialization, `tools/list` discovery and `tools/call`
- Why stdout belongs to the MCP transport rather than application print statements
## What changed since step 0
Four CRD components are introduced; this is a functional vertical slice.
## Run it
```bash
python -m pip install -r requirements.txt
python -m pytest -q
python -m app.main
```
## Verify it
`test_real_mcp_status` launches a subprocess, negotiates a session, lists server_status, invokes it and checks the returned payload. The pure status test checks its business data without transport.
## Diagram
STEP-1 will be visualized in Stage 3 using STEP-1.crd.
## Next
Step 2 implements task and calendar tools and in-memory business services.
