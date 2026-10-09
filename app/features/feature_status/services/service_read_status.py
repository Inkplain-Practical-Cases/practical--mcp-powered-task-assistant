# Pure status service; usable without an MCP runtime.
# Without this boundary the protocol-facing tool would own business rules.
def service_read_status() -> dict[str, str]:
    # Deterministic output allows offline smoke testing.
    return {"service": "northstar-task-assistant", "status": "ok"}
