# Program entry point for local stdio transport.
# Why: a single door starts the MCP server without business logic.
from app.server import server

def main() -> None:
    # stdio is the standard local transport to an MCP client.
    server.run(transport="stdio")

if __name__ == "__main__":
    main()
