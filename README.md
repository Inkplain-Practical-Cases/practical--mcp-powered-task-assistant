# MCP-Powered Task Assistant — Step 4
The client now performs live discovery, validates arguments with JSON Schema, calls tools over stdio and distinguishes success from MCP `isError`.
```bash
python -m pip install -r requirements.txt
python -m pytest -q
python -m app.client.invoke_cli
```
An unknown tool or bad schema is rejected before a call. A tool-side error cannot be claimed as a success.
