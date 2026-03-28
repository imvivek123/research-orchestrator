# Smart Research Orchestrator

A multi-agent AI system that orchestrates specialized Python agents to handle research workflows using LangGraph and MCP (Model Context Protocol).

## 🏗️ Architecture flow 

```
User Query
    ↓
Orchestrator Agent (routes workflow)
    ↓          ↓           ↓
Research    Summarizer   Report
Agent       Agent        Agent
(web search) (condense)  (format)
    ↓          ↓           ↓
         Final Report
```

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- pip package manager

### Setup

1. **Clone the repository**
   ```bash
   cd research-orchestrator
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set API keys**
   ```bash
   export ANTHROPIC_API_KEY=your_key_here
   # On Windows: set ANTHROPIC_API_KEY=your_key_here
   ```

5. **Run the orchestrator**
   ```bash
   python main.py "Your research query here"
   ```

## 📁 Project Structure

```
research-orchestrator/
├── mcp_server/
│   ├── server.py          # MCP server with tool definitions
│   └── tools/
│       ├── search.py      # Web search tool
│       └── reporter.py    # Report generation tool
├── agents/
│   ├── orchestrator.py    # Main controller/router
│   ├── researcher.py      # Research agent logic
│   └── summarizer.py      # Summarizer agent logic
├── graph/
│   └── workflow.py        # LangGraph workflow (coming soon)
├── main.py                # Entry point
├── requirements.txt       # Python dependencies
├── CLAUDE.md              # Project documentation
└── README.md              # This file
```

## 🤖 Components

### Orchestrator Agent
- Routes user queries to appropriate agents
- Manages workflow execution
- Handles inter-agent communication
- Returns final structured report

### Research Agent
- Executes web searches via MCP tools
- Processes search results
- Returns structured research data

### Summarizer Agent
- Condenses findings
- Extracts key insights
- Formats results for final report

## 🛠️ Development Roadmap

### Day 1: Setup + Basic Agent ✅
- ✅ Project structure
- ✅ MCP server scaffold
- ✅ Single agent implementation
- ⏳ Full MCP integration testing

### Day 2: Multi-Agent Orchestration
- ⏳ LangGraph workflow integration
- ⏳ Error handling & retries
- ⏳ Concurrent agent execution
- ⏳ Inter-agent communication

### Day 3: Polish + Production Ready
- ⏳ Architecture documentation
- ⏳ Performance logging
- ⏳ Example outputs
- ⏳ GitHub release

## 📝 Example Usage

```bash
# Run with custom query
python main.py "Latest developments in quantum computing"

# This will:
# 1. Send query to orchestrator
# 2. Researcher agent performs web search
# 3. Summarizer condenses findings
# 4. Final report is generated and displayed
```

## 🔑 Key Technologies

- **LangGraph**: Orchestration and workflow management
- **MCP Protocol**: Standardized tool interface
- **Anthropic Claude**: AI backbone
- **Python async/await**: Concurrent execution
- **Pydantic**: Type validation and serialization

## 📚 Architecture Patterns

- **Multi-Agent Pattern**: Specialized agents for different tasks
- **MCP Protocol**: Standard tool interface
- **State Machine**: LangGraph-based workflow
- **Error Recovery**: Graceful error handling and retries
- **Logging**: Comprehensive operation logging

## 🔐 Environment Variables

- `ANTHROPIC_API_KEY`: Your Anthropic API key (required)
- `LOG_LEVEL`: Logging level (default: INFO)

## 📝 Code Style

- Type hints throughout
- Async/await for concurrency
- Comprehensive error handling
- Clear logging statements
- Docstrings for all functions

## 🤝 Contributing

1. Read CLAUDE.md for architectural decisions
2. Follow existing code patterns
3. Test agents independently
4. Maintain type hints and error handling

## 📄 License

MIT

---

**Status**: Early development (Day 1)
**Last Updated**: 2026-03-25
