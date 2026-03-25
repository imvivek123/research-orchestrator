"""
Summarizer Agent - condenses information
"""

from typing import Any, Dict, List


class SummarizerAgent:
    """Agent that summarizes research findings"""

    def __init__(self):
        self.name = "Summarizer"

    async def run(self, research_results: Dict[str, Any]) -> Dict[str, Any]:
        """Summarize the research results"""
        print(f"📝 {self.name}: Condensing findings...")

        # Simple summarization logic
        results = research_results.get("results", {}).get("results", [])
        summary = f"Found {len(results)} relevant results for '{research_results.get('topic')}'"

        return {
            "agent": self.name,
            "task": "summarize",
            "summary": summary,
            "snippet_count": len(results)
        }
