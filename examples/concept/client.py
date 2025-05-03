import asyncio
from fastmcp import Client
from fastmcp.client.transports import SSETransport

url="http://localhost:5001/sse"
client = Client(url)

async def main():
    # Connection is established here
    async with client:
        print(f"Client connected: {client.is_connected()}")
        tools = await client.list_tools()
        print(f"Available tools: {tools}")

        result = await client.call_tool("add_numbers", {"a": 15, "b": 25})
        print("Result:", result[0].text if result else "No result")


if __name__ == "__main__":
    asyncio.run(main())
