# DESIGN_SPEC.md

## Overview
This project serves as a learning playground for Google ADK (Agent Development Kit) in Python. We will iteratively build and explore different types of agents, starting with basic conversational agents and progressively moving to more complex workflow orchestrations (Sequential, Parallel, Loop) and multi-agent systems as outlined in the ADK documentation.

## Example Use Cases
1.  **Basic Agent**: A simple agent (e.g., a "Weather Assistant" or "Math Tutor") that demonstrates core features like state management and basic tool calling.
2.  **Sequential Agent Pipeline**: Passing information deliberately from one agent to another (e.g., a Summarizer passing data to a Question Generator).
3.  **Parallel Agent Execution**: Running multiple distinct tasks concurrently and merging their outputs.

## Tools Required
- Initial phases will use simple Python function tools (e.g., `get_weather`, `calculate`) to demonstrate the `FunctionTool` primitive.
- Later phases may explore built-in tools like `google_search` or `load_web_page`.

## Constraints & Safety Rules
- The code must remain highly educational, with comments explaining ADK-specific concepts (e.g., `include_contents`, `output_key`, decorators vs. tool lists).
- Implementations must adhere strictly to ADK code preservation principles.

## Success Criteria
- The playground structure allows easy execution of different agent lessons.
- The user can successfully run the basic agent via the ADK playground UI or CLI.
- The `.env` template is properly set up for the user to securely add their Gemini API key.

## Edge Cases to Handle
- Provide clear error messages if the Google Gemini API key is missing.
- Handle unexpected inputs gracefully during text generation limits or tool parsing fallback.
