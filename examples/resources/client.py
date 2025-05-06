#!/usr/bin/env python3
import asyncio
from fastmcp import Client
from fastmcp.client.transports import SSETransport

# Client configuration
url="http://localhost:5001/sse"
client = Client(url)

async def main():
    async with client:
        print(await client.list_resources())
        print(await client.list_resource_templates())
        # Construct full URI with default values
        #uri = f"s_server2+search://python" # BUG, doesnt allow underscore before the colon
        uri = f"server2+search://python"
        results = await client.read_resource(uri)
        print(results)

if __name__ == "__main__":
    asyncio.run(main())
