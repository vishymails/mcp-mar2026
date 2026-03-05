"""
Calculator MCP Client.
Connects to the calculator server and consumes all calculator tools.
Run with: python calculator_client.py
"""

import asyncio
import sys
from pathlib import Path

from mcp import ClientSession, types
from mcp.client.stdio import StdioServerParameters, stdio_client


def get_text_result(result) -> str:
    """Extract text from first content block of a tool result."""
    if not result.content:
        return ""
    content = result.content[0]
    if isinstance(content, types.TextContent):
        return content.text
    return str(content)


async def run_calculator_client() -> None:
    server_script = Path(__file__).resolve().parent / "calculator_server.py"
    server_params = StdioServerParameters(
        command=sys.executable,
        args=[str(server_script)],
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Step 1: Initialize connection
            await session.initialize()
            print("=== Calculator MCP Client ===\n")
            print("Step 1: Connected to Calculator Server.\n")

            # Step 2: List all tools
            tools_result = await session.list_tools()
            tool_names = [t.name for t in tools_result.tools]
            print("Step 2: Available tools:", tool_names, "\n")

            # Step 3: Call each calculator tool with examples
            print("Step 3: Calling calculator tools:\n")

            # add
            r = await session.call_tool("add", arguments={"a": 10, "b": 7})
            print(f"  add(10, 7) = {get_text_result(r)}")

            # subtract
            r = await session.call_tool("subtract", arguments={"a": 20, "b": 8})
            print(f"  subtract(20, 8) = {get_text_result(r)}")

            # multiply
            r = await session.call_tool("multiply", arguments={"a": 6, "b": 7})
            print(f"  multiply(6, 7) = {get_text_result(r)}")

            # divide
            r = await session.call_tool("divide", arguments={"a": 100, "b": 4})
            print(f"  divide(100, 4) = {get_text_result(r)}")

            # power
            r = await session.call_tool("power", arguments={"base": 2, "exponent": 10})
            print(f"  power(2, 10) = {get_text_result(r)}")

            # sqrt
            r = await session.call_tool("sqrt", arguments={"x": 144})
            print(f"  sqrt(144) = {get_text_result(r)}")

            # modulo
            r = await session.call_tool("modulo", arguments={"a": 17, "b": 5})
            print(f"  modulo(17, 5) = {get_text_result(r)}")

            # factorial
            r = await session.call_tool("factorial", arguments={"n": 5})
            print(f"  factorial(5) = {get_text_result(r)}")

            # negate
            r = await session.call_tool("negate", arguments={"x": -42})
            print(f"  negate(-42) = {get_text_result(r)}")

            # percentage
            r = await session.call_tool("percentage", arguments={"value": 200, "percent": 15})
            print(f"  percentage(200, 15) = {get_text_result(r)}")

            # round_number
            r = await session.call_tool("round_number", arguments={"x": 3.14159, "decimals": 2})
            print(f"  round_number(3.14159, 2) = {get_text_result(r)}")

            # absolute
            r = await session.call_tool("absolute", arguments={"x": -7.5})
            print(f"  absolute(-7.5) = {get_text_result(r)}")

    print("\nStep 4: All calculator tools consumed. Done.")


def main() -> None:
    asyncio.run(run_calculator_client())


if __name__ == "__main__":
    main()
