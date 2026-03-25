"""
Orchestrator Agent - main controller that routes between other agents
"""

from typing import Any, Dict
from agents.researcher import ResearchAgent
from agents.summarizer import SummarizerAgent


class OrchestratorAgent:
    """Main orchestrator that manages the workflow"""

    def __init__(self, tools: Dict[str, Any]):
        self.researcher = ResearchAgent(tools)
        self.summarizer = SummarizerAgent()
        self.name = "Orchestrator"

    async def run(self, user_query: str) -> Dict[str, Any]:
        """
        Main orchestration workflow:
        1. Pass query to researcher
        2. Summarize results
        3. Return final output
        """
        print(f"\n🎯 {self.name}: Starting workflow for '{user_query}'")

        # Step 1: Research
        research_output = await self.researcher.run(user_query)

        # Step 2: Summarize
        summary_output = await self.summarizer.run(research_output)

        # Step 3: Final output
        final_report = {
            "query": user_query,
            "research": research_output,
            "summary": summary_output,
            "status": "completed"
        }

        print(f"\n✅ {self.name}: Workflow completed")
        return final_report
