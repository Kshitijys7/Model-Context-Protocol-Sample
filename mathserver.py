from mcp.server.fastmcp import FastMCP

mcp=FastMCP("Math")

@mcp.tool()
def add(x: int, y: int) -> int:
    """_summary_
    Add two numbers.
    """
    return x + y

@mcp.tool()
def multiply(x: int, y: int) -> int:
    """_summary_
    Multiply two numbers.
    """
    return x * y

if __name__ == "__main__":
    mcp.run(transport="stdio")