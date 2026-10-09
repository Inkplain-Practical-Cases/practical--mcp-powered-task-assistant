# Discover both new MCP tools through actual stdio session and invoke each.
import asyncio
from datetime import date, timedelta
import json
import sys
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def integration() -> None:
    cfg = StdioServerParameters(command=sys.executable, args=["-m", "app.main"])
    async with stdio_client(cfg) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            names = [tool.name for tool in (await session.list_tools()).tools]
            assert {"server_status", "create_task", "list_calendar_events"} <= set(names)
            date_str = (date.today() + timedelta(days=1)).isoformat()
            created = await session.call_tool("create_task", {
                "title": "Review customer report", "due_date": date_str, "priority": "urgent"
            })
            assert not created.isError, created
            assert "Review customer report" in " ".join(getattr(x,"text","") for x in created.content)
            events = await session.call_tool("list_calendar_events", {"limit": 2})
            assert not events.isError
            assert "Customer review" in " ".join(getattr(x,"text","") for x in events.content)

def test_mcp_business_tools() -> None:
    asyncio.run(integration())
