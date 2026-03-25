"""
MCP Server implementation for Research Orchestrator
Provides tools for web search and report generation
"""

from mcp.server import Server
from mcp.types import Tool, TextContent
from duckduckgo_search import DDGS
import json
import os
from datetime import datetime


def create_mcp_server():
    """Create and configure MCP server with tools"""
    server = Server("research-orchestrator")

    @server.call_tool()
    def web_search(query: str, num_results: int = 5) -> str:
        """Search the web using DuckDuckGo"""
        try:
            results = []
            with DDGS() as ddgs:
                for r in ddgs.text(query, max_results=num_results):
                    results.append({
                        "title": r.get("title", ""),
                        "snippet": r.get("body", ""),
                        "url": r.get("href", "")
                    })
            return json.dumps({
                "query": query,
                "results": results
            })
        except Exception as e:
            return json.dumps({
                "query": query,
                "results": [],
                "error": str(e)
            })

    @server.call_tool()
    def save_report(title: str, content: str, filename: str = None) -> str:
        """Save a report to file"""
        try:
            if filename is None:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"report_{timestamp}.md"

            os.makedirs("reports", exist_ok=True)
            filepath = os.path.join("reports", filename)

            with open(filepath, "w", encoding="utf-8") as f:
                f.write(f"# {title}\n\n")
                f.write(f"*Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*\n\n")
                f.write(content)

            return json.dumps({
                "status": "success",
                "filename": filename,
                "filepath": filepath,
                "message": f"Report '{title}' saved successfully"
            })
        except Exception as e:
            return json.dumps({
                "status": "error",
                "error": str(e)
            })

    return server


if __name__ == "__main__":
    server = create_mcp_server()
    print("MCP Server created successfully")