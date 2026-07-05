# Prompt Optimization Agent

[![CI](https://github.com/kogunlowo123/prompt-optimization-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/prompt-optimization-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: AI Engineering | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

Prompt engineering and optimization agent that designs, tests, and iterates on LLM prompts using systematic evaluation, A/B testing, chain-of-thought refinement, and automated prompt versioning with regression detection.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `design_prompt` | Design an optimized prompt for a specific task using best practices |
| `evaluate_prompt` | Evaluate a prompt against a test suite with scoring metrics |
| `ab_test_prompts` | Run A/B test between two prompt variants |
| `version_prompt` | Save a prompt version with metadata and evaluation results |
| `detect_regression` | Check if a new prompt regresses on any test case category |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/prompts/design` | Design a prompt |
| `POST` | `/api/v1/prompts/evaluate` | Evaluate a prompt |
| `POST` | `/api/v1/prompts/ab-test` | A/B test prompts |
| `POST` | `/api/v1/prompts/version` | Version a prompt |
| `POST` | `/api/v1/prompts/regression` | Detect regression |

## Features

- Prompt Design
- Ab Testing
- Chain Of Thought
- Prompt Versioning
- Regression Detection

## Integrations

- Openai Api
- Anthropic Api
- Langsmith
- Promptfoo
- Humanloop

## Architecture

```
prompt-optimization-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── prompt_optimization_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 5 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 5 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**LLM APIs + Evaluation Frameworks + Prompt Management**

---

Built as part of the Enterprise AI Agent Platform.
