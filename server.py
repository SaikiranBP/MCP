from mcp.server import MCPServer
mcp = MCPServer("My First MCP Server")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b

@mcp.tool()
def greet(name: str) -> str:
    """Greet a person."""
    return f"Hello, {name}!"

@mcp.resource("queue://{facility}/status")
def canteen_queue(facility: str) -> str:
    """Get the queu status of a facility."""
    return f"Canteen Queue Status of {facility}"\

@mcp.prompt()
def analyze_queue(facility: str) -> str:
    """Generate the prompt to analyze the facility queue"""
    return f"""Analyze the queue for {facility}

    Consider:
    1. Number of people waiting
    2. Number of active counters
    3. Estimated waiting time
    4. Possible bottlenecks
    5. Recommended action"""

if __name__ == "__main__":
    mcp.run()