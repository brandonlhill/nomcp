from fastmcp import FastMCP

mcp = FastMCP(name="MyServer")

@mcp.tool()
def add_numbers(a: int, b: int) -> int:
    """ adds two numbers via floating point addition."""
    return a + b

if __name__ == "__main__":
    mcp.run(transport="sse", host="0.0.0.0", port=5001, log_level="debug")