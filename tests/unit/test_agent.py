"""Prompt Optimization Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_design_prompt():
    """Test Design an optimized prompt for a specific task using best practices."""
    tools = AgentTools()
    result = await tools.design_prompt(task_description="test", model="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_evaluate_prompt():
    """Test Evaluate a prompt against a test suite with scoring metrics."""
    tools = AgentTools()
    result = await tools.evaluate_prompt(prompt="test", test_cases="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_ab_test_prompts():
    """Test Run A/B test between two prompt variants."""
    tools = AgentTools()
    result = await tools.ab_test_prompts(prompt_a="test", prompt_b="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_version_prompt():
    """Test Save a prompt version with metadata and evaluation results."""
    tools = AgentTools()
    result = await tools.version_prompt(prompt="test", version_tag="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.prompt_optimization_agent_agent import PromptOptimizationAgentAgent
    agent = PromptOptimizationAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
