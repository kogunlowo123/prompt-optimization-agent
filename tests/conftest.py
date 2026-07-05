"""Test configuration for Prompt Optimization Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "prompt-optimization-agent", "category": "AI Engineering"}
