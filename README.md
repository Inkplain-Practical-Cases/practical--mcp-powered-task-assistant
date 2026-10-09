# MCP-Powered Task Assistant — Step 1
This branch runs a minimal **real** MCP server and status tool, not a mocked protocol.
## Quick start
```bash
python -m pip install -r requirements.txt
python -m pytest -q
python -m app.main
```
Running `app.main` waits for the MCP client over stdio (no HTTP port or browser page). The integration test launches the server automatically, negotiates the MCP session, discovers `server_status` and invokes it.

See `STEP-1.md` for a conceptual walkthrough and tests.
