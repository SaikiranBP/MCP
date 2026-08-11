import asyncio
import sys
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def main():
    server_params = StdioServerParameters(command=sys.executable, args=["server.py"],)
    # starts the server process and connects to it through stdin/stdout
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            print("Connected to MCP server!")
            # LIST TOOLS
            tools = await session.list_tools()
            print("\nTOOLS:")
            for tool in tools.tools:
                print(f"\nName: {tool.name}")
                print(f"Description: {tool.description}")
                print(f"Input schema: {tool.input_schema}")
            # CALL TOOL
            result = await session.call_tool(
                "add",{
                    "a": 10,
                    "b": 20})
            print("\nTOOL RESULT:")
            print(result)

if __name__ == "__main__":
    asyncio.run(main())