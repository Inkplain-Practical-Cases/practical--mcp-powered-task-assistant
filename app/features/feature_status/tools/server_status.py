# Status MCP tool delegates its operation to the status service.
# This public schema has no arguments and does not modify business data.
from app.features.feature_status.services.service_read_status import service_read_status

async def server_status() -> dict[str, str]:
    # The MCP runtime serializes the returned typed dictionary.
    return service_read_status()
