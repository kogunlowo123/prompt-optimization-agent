# Prompt Optimization Agent Architecture

Prompt engineering and optimization agent that designs, tests, and iterates on LLM prompts using systematic evaluation, A/B testing, chain-of-thought refinement, and automated prompt versioning with regression detection.

## Domain Tools

- **design_prompt**: Design an optimized prompt for a specific task using best practices
- **evaluate_prompt**: Evaluate a prompt against a test suite with scoring metrics
- **ab_test_prompts**: Run A/B test between two prompt variants
- **version_prompt**: Save a prompt version with metadata and evaluation results
- **detect_regression**: Check if a new prompt regresses on any test case category