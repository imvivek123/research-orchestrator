"""
Main entry point for the Research Orchestrator
"""

import asyncio
import json
from agents.orchestrator import OrchestratorAgent
from mcp_server.server import create_mcp_server


async def main():
    """Main entry point"""

    # Initialize MCP server and tools
    mcp_server = create_mcp_server()

    # Create mock tools dict (TODO: replace with actual MCP tools)
    tools = {
        "web_search": lambda q: json.dumps({"query": q, "results": []}),
        "save_report": lambda t, c: json.dumps({"status": "success"})
    }

    # Initialize orchestrator
    orchestrator = OrchestratorAgent(tools)

    # Example query
    user_query = "What are the latest advances in AI?"

    # Run the workflow
    result = await orchestrator.run(user_query)

    print("\n" + "="*50)
    print("FINAL REPORT")
    print("="*50)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    import sys

    # Get query from command line or use default
    query = sys.argv[1] if len(sys.argv) > 1 else "What are the latest advances in AI?"

    # Run async main
    asyncio.run(main())
