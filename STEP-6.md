# Step 6 of 6 — Harden and verify
## What you build in this step
A complete offline MCP task assistant with timeout, safe structured events and end-to-end tests.
## What you learn
- asyncio.wait_for for bounded tool execution
- safe error mapping, configuration limits and non-sensitive logging
- verifying real stdio client/server interactions
## What changed since step 5
Two core components introduced; assistant handler and tool executor changed.
## Run it
```bash
python -m pip install -r requirements.txt
python -m pytest -q
python -m app.client.assistant_cli
```
## Verify it
test_end_to_end checks one two-action request over a real session; hardening tests check tool timeout, safe event logs and unsupported-language denial.
## Diagram
Stage 3 will create Simulator STEP-6; do not create an .inkp in Stage 2.
## Next
Main is the final version. Stage 3 can begin only when the user asks.
