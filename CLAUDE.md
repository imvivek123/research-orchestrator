# Smart Research Orchestrator

## Project Overview
A multi-agent AI system built with LangGraph and MCP (Model Context Protocol) that orchestrates specialized Python agents to handle research workflows.

**Agents:**
- **Orchestrator Agent**: Decides workflows and routes tasks
- **Research Agent**: Performs web searches (via MCP tool)
- **Summarizer Agent**: Condenses research findings
- **Report Agent**: Generates final output

**Tech Stack:**
- Python 3.11+
- LangGraph (orchestration)
- MCP Python SDK (tool protocol)
- Anthropic API (Claude backend)

## Project Structure
```
research-orchestrator/
├── mcp_server/
│   ├── server.py          ← MCP server with tools
│   └── tools/
│       ├── search.py      ← Web search tool
│       └── reporter.py    ← Report generation tool
├── agents/
│   ├── orchestrator.py    ← Main controller/router
│   ├── researcher.py      ← Research agent logic
│   └── summarizer.py      ← Summarizer agent logic
├── graph/
│   └── workflow.py        ← LangGraph workflow definition
├── main.py                ← Entry point/CLI
├── requirements.txt
├── .gitignore
├── README.md
└── CLAUDE.md              ← This file
```

## Development Plan (2-3 Days)

### Day 1: Setup + Basic Agent
- [ ] Install dependencies (langgraph, langchain, anthropic, mcp)
- [ ] Create MCP server with web_search and save_report tools
- [ ] Single agent that uses MCP tools
- [ ] Basic testing

### Day 2: Multi-Agent Orchestration
- [ ] Research Agent implementation
- [ ] Summarizer Agent implementation
- [ ] Orchestrator Agent implementation (routes between agents)
- [ ] LangGraph workflow integration
- [ ] Error handling and retries

### Day 3: Polish + GitHub Ready
- [ ] README with architecture diagrams
- [ ] Performance logging
- [ ] Example outputs/screenshots
- [ ] GitHub push
- [ ] Demo GIF (optional)

## Key Features
- **MCP Protocol**: Standard tool interface for agents
- **Agentic AI**: LLM-powered decision making
- **Multi-Agent Orchestration**: Specialized agents for different tasks
- **Error Recovery**: Robust error handling and retries
- **Concurrent Task Handling**: Parallel agent execution
- **Workflow Automation**: LangGraph-based state machine

## Resume Keywords
✅ MCP (Model Context Protocol)
✅ Agentic AI / Multi-Agent Systems
✅ LangGraph Orchestration
✅ Specialized Agents
✅ Error Recovery & Resilience
✅ Automated Workflow Execution
✅ Python Backend Development
✅ Tool Interface Design

## Setup Instructions
1. Create virtual environment: `python -m venv venv`
2. Activate: `source venv/bin/activate` (or `venv\Scripts\activate` on Windows)
3. Install: `pip install -r requirements.txt`
4. Set API keys: `export ANTHROPIC_API_KEY=your_key`
5. Run: `python main.py "your research query"`

## Claude Code Instructions
- Always read existing code before making changes
- Follow the MCP protocol specification when adding tools
- Use LangGraph StateGraph for workflow definitions
- Test agents independently before integration
- Maintain error handling and logging throughout
- Document architectural decisions in code comments

## Important Notes
- MCP tools must be stateless where possible
- All agents should handle errors gracefully
- Log all API calls and agent decisions for debugging
- Use type hints throughout Python code
