from fastmcp import FastMCP

server2 = FastMCP(name="MyServer2")

@server2.resource("search://{query}")
def search_resources(query: str) -> bytes:
    """Search for resources matching the query string."""
    # Only 'query' is required in the URI, the other parameters use their defaults
    return {
        "query": query
    }