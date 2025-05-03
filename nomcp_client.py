import asyncio
import logging

from fastmcp import Client
from fastmcp.client.transports import SSETransport
from typing import Any

log = logging.getLogger(__name__)

class MCPClientManager:
    def __init__(self, url: str):
        self.url = url
        self.transport = SSETransport(url=url)
        self.client = Client(self.transport)
        self._connected = False
        self._session = None

    async def connect(self):
        """Establish the connection to the MCP server."""
        if not self._connected:
            self._session = self.client.__aenter__()
            await self._session.__anext__()  # enters the async context manually
            self._connected = True
            log.info(f"Connected to {self.url}")

    async def list_tools(self):
        """List all available tools from the server."""
        await self._ensure_connected()
        return await self.client.list_tools()

    async def call_tool(self, name: str, args: dict[str, Any]):
        """Call a tool by name with arguments."""
        await self._ensure_connected()
        result = await self.client.call_tool(name, args)
        return result
    
    # TODO: add tool can and return none formatted value

    async def shutdown(self):
        """Close the connection cleanly."""
        if self._connected and self._session:
            await self._session.aclose()
            self._connected = False
            log.info(f"[MCPClientManager] Disconnected from {self.url}")

    async def _ensure_connected(self):
        if not self._connected:
            raise RuntimeError("Client is not connected. Call `connect()` first.")

    @property
    def is_connected(self):
        return self._connected