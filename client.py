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
            result = await session.call_tool("add", {"a": 10, "b": 20})
            print("\nTOOL RESULT:")
            print(result)
            # LIST RESOURCE TEMPLATES
            templates = await session.list_resource_templates()
            print("\nRESOURCE TEMPLATES:")
            for template in templates.resource_templates:
                print(f"- {template.uri_template}")
            # READ RESOURCE
            resource = await session.read_resource("queue://clinic/status")
            print("\nRESOURCE RESULT:")
            for content in resource.contents:
                print(content)
            prompts = await session.list_prompts()
            print("\nPROMPTS:") 
            for prompt in prompts.prompts:
                print(f"- {prompt.name}")
            print("\nPROMPT RESULT:")
            prompt = await session.get_prompt("analyze_queue", {"facility": "canteen"})
            for message in prompt.messages:
                print(message)
if __name__ == "__main__":
    asyncio.run(main())