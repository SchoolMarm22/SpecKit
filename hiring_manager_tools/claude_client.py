"""Thin wrapper around the Anthropic SDK for structured output via tool_use."""

from __future__ import annotations

import os

import anthropic


class ClaudeClient:
    """Calls Claude with a tool definition for structured output."""

    def __init__(
        self,
        model: str = "claude-sonnet-4-20250514",
        api_key: str | None = None,
    ):
        self.model = model
        self.client = anthropic.Anthropic(
            api_key=api_key or os.environ.get("ANTHROPIC_API_KEY")
        )

    def invoke(
        self,
        system_prompt: str,
        messages: list[dict],
        tool_schema: dict,
    ) -> dict:
        """Call Claude with a tool definition for structured output.

        Returns the parsed tool call arguments (the structured JSON).
        """
        tool_definition = {
            "name": "structured_output",
            "description": "Return the structured output for this task.",
            "input_schema": tool_schema,
        }

        response = self.client.messages.create(
            model=self.model,
            max_tokens=4096,
            system=system_prompt,
            messages=messages,
            tools=[tool_definition],
            tool_choice={"type": "tool", "name": "structured_output"},
        )

        # Extract the tool use block
        for block in response.content:
            if block.type == "tool_use" and block.name == "structured_output":
                return block.input

        from hiring_manager_tools import EngineError
        raise EngineError("Claude did not return a structured output tool call")
