# Agentic Framework

A lightweight framework for building AI Agent systems, inspired by AWS Strands and similar agentic platforms.

## Overview

Agentic Framework provides essential abstractions that allow developers to focus on agent business logic rather than infrastructure concerns. It offers:

- **Agent Orchestration**: Manage multiple agents with automatic coordination
- **Tool Integration**: Standardized interfaces for external services and APIs
- **Context Management**: Built-in conversation history and memory management
- **LLM Abstraction**: Flexible provider switching without code changes
- **Workflow Engine**: Declarative multi-step process definition
- **Monitoring**: Built-in observability and debugging support

## Quick Start

### Installation

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install the framework
pip install -e .

# Install development dependencies
pip install -e ".[dev]"
```

### Basic Usage

```python
from agentic_framework import Agent, ToolManager, ContextManager

# Create a simple agent
agent = Agent(name="assistant")

# Add tools
tool_manager = ToolManager()
agent.add_tool_manager(tool_manager)

# Run the agent
result = agent.run("Hello, how can you help me?")
print(result)
```

## Development

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src/agentic_framework

# Run specific test categories
pytest -m unit
pytest -m integration
```

### Code Quality

```bash
# Format code
black src/ tests/ examples/

# Sort imports
isort src/ tests/ examples/

# Lint code
flake8 src/ tests/ examples/

# Type checking
mypy src/
```

## Project Structure

```
agentic-framework/
├── src/agentic_framework/    # Main framework code
├── tests/                    # Test files
├── examples/                 # Example applications
├── docs/                     # Documentation
├── pyproject.toml           # Project configuration
├── requirements.txt         # Core dependencies
└── requirements-dev.txt     # Development dependencies
```

## License

MIT License - see LICENSE file for details.
