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
def queue_status(facility: str) -> str:
    data = {
        "canteen": {
            "waiting": 17,
            "counters": 3,
            "wait": 12
        },
        "admin": {
            "waiting": 5,
            "counters": 2,
            "wait": 8
        },
        "clinic": {
            "waiting": 9,
            "counters": 1,
            "wait": 25
        }
    }
    queue = data.get(facility)
    if queue is None:
        return f"No queue found for {facility}"
    return f"""
    Queue Status
    Facility: {facility}
    Students waiting: {queue["waiting"]}
    Counters active: {queue["counters"]}
    Estimated wait: {queue["wait"]} minutes
    """

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