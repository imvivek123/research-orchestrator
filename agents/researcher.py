"""
Research Agent - fetches and processes information
"""

from typing import Any, Dict
import json


class ResearchAgent:
    """Agent that performs research using web search"""

    def __init__(self, tools: Dict[str, Any]):
        self.tools = tools
        self.name = "Researcher"

    async def search(self, query: str) -> Dict[str, Any]:
        """Perform a web search"""
        result = self.tools.get("web_search", lambda x: "{}")(query)
        return json.loads(result)

    async def run(self, topic: str) -> Dict[str, Any]:
        """Run the research workflow"""
        print(f"🔍 {self.name}: Researching '{topic}'...")

        search_results = await self.search(topic)

        return {
            "agent": self.name,
            "task": "research",
            "topic": topic,
            "results": search_results
        }
