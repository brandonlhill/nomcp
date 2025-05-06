
import asyncio
from fastmcp import FastMCP
from server2 import server2

mcp = FastMCP(name="MyServer1")
async def main():
    # Create a shutdown event
    shutdown_event = asyncio.Event()

    await mcp.import_server("s_server2", server2)
    await mcp.import_server("server2", server2)
    server_task = asyncio.create_task(mcp.run_async(transport="sse", host="0.0.0.0", port=5001, log_level="debug"))
    await shutdown_event.wait()
if __name__ == "__main__":
    asyncio.run(main())
