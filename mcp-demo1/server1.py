from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Simple Demo Server", json_response=True)

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers and return the sum."""
    return a + b

@mcp.tool()
def greet(name: str) -> str:
    """Return a greeting for the given name."""
    return f"Welcome to the MCP Demo Server , {name}!"


# if __name__ == "__main__":
#     mcp.run(transport = "streamable-http", host = "0.0.0.0", port = 9000)
    

import uvicorn

if __name__ == "__main__":
    uvicorn.run("server1:mcp", host="0.0.0.0", port=9000)