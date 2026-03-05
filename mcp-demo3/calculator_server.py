"""
Calculator MCP Server.
Exposes all calculator operations as MCP tools for clients to consume.
Run with: python calculator_server.py
"""

import math
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Calculator Server", json_response=True)


@mcp.tool()
def add(a: float, b: float) -> float:
    """Add two numbers. Returns a + b."""
    return a + b


@mcp.tool()
def subtract(a: float, b: float) -> float:
    """Subtract b from a. Returns a - b."""
    return a - b


@mcp.tool()
def multiply(a: float, b: float) -> float:
    """Multiply two numbers. Returns a * b."""
    return a * b


@mcp.tool()
def divide(a: float, b: float) -> float:
    """Divide a by b. Returns a / b. Fails if b is zero."""
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b


@mcp.tool()
def power(base: float, exponent: float) -> float:
    """Raise base to the power of exponent. Returns base ** exponent."""
    return base**exponent


@mcp.tool()
def sqrt(x: float) -> float:
    """Square root of x. x must be non-negative."""
    if x < 0:
        raise ValueError("Square root is not defined for negative numbers.")
    return math.sqrt(x)


@mcp.tool()
def modulo(a: float, b: float) -> float:
    """Remainder when a is divided by b. Returns a % b. b must not be zero."""
    if b == 0:
        raise ValueError("Modulo by zero is not allowed.")
    return a % b


@mcp.tool()
def factorial(n: int) -> int:
    """Factorial of non-negative integer n. Returns n! (e.g. 5! = 120)."""
    if n < 0:
        raise ValueError("Factorial is only defined for non-negative integers.")
    return math.factorial(n)


@mcp.tool()
def negate(x: float) -> float:
    """Return the opposite of x. Returns -x."""
    return -x


@mcp.tool()
def percentage(value: float, percent: float) -> float:
    """Compute 'percent'% of 'value'. Returns value * percent / 100."""
    return value * percent / 100.0


@mcp.tool()
def round_number(x: float, decimals: int = 0) -> float:
    """Round x to the given number of decimal places. decimals defaults to 0."""
    return round(x, decimals)


@mcp.tool()
def absolute(x: float) -> float:
    """Return the absolute value of x."""
    return abs(x)


if __name__ == "__main__":
    mcp.run(transport="stdio")
