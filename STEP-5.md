# Step 5 of 6 — Orchestrate natural language requests
## What you build in this step
A deterministic offline intent parser converts a two-part natural-language request to typed MCP actions. The handler executes both tools through one MCP client session.
## What you learn
- Natural language to typed action plans, validation and safe execution
- Why a model suggestion is not authority to call arbitrary tools
- Sequential orchestration of a task create and calendar read
## What changed since step 4
Six new CRD components handle parsing, typed planning, execution and a CLI.
## Run it
```bash
python -m pip install -r requirements.txt
python -m pytest -q
python -m app.client.assistant_cli
```
## Verify it
The parser creates two actions for the case example; unknown or ambiguous phrases are rejected. An end-to-end test checks both MCP tool results through one connected session.
## Diagram
Stage 3 will visualize STEP-5.crd.
## Next
Add bounded waits, structured logs and final end-to-end failure tests.
