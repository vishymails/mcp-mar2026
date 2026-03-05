import asyncio
from pathlib import Path
import sys

from pydantic import AnyUrl

from mcp import ClientSession, types
from mcp.client.stdio import StdioServerParameters, stdio_client

async def run_client() -> None:
    server_script = Path(__file__).resolve().parent / "server.py"

    server_params = StdioServerParameters(
        command = sys.executable,
        args = [str(server_script)],
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:

            # Step 1: Initialize the MCP connection
            await session.initialize()
            print("Connected to MCP server.\n")

            # Step 2: List tools
            tools_result = await session.list_tools()
            print("Tools:", [t.name for t in tools_result.tools])

            # Step 3: Call the "add" tool
            result = await session.call_tool("add", arguments={"a": 10, "b": 7})
            content = result.content[0]
            if isinstance(content, types.TextContent):
                print("add(10, 7) =", content.text)

            # Step 4: Call the "greet" tool
            result = await session.call_tool("greet", arguments={"name": "MCP"})
            content = result.content[0]
            if isinstance(content, types.TextContent):
                print("greet('MCP') =", content.text)


print("\nDone.")

def main() -> None:
    asyncio.run(run_client())

if __name__ == "__main__":
    main()
