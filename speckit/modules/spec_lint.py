"""Spec lint module — analyzes specs for bias, vagueness, and quality."""

from speckit.modules.base import Module, InvocationPlan


class SpecLintModule(Module):
    """Analyzes a spec file for quality issues using Claude."""

    @property
    def name(self) -> str:
        return "spec_lint"

    @property
    def supported_kinds(self) -> list[str]:
        return ["hiring", "review", "team", "onboarding", "offboarding"]

    def input_schema(self) -> dict:
        return {"type": "object", "properties": {}}

    def plan(self, spec, inputs: dict) -> InvocationPlan:
        system_prompt = self._load_prompt_template()

        user_message = f"""## Spec to Analyze

Kind: {spec.kind}

{spec.body}

---

Analyze this spec file for quality, clarity, potential bias, and completeness."""

        return InvocationPlan(
            system_prompt=system_prompt,
            messages=[{"role": "user", "content": user_message}],
            tool_schema=self.output_schema(),
            prompt_version=self._get_prompt_version(),
        )

    def output_schema(self) -> dict:
        return {
            "type": "object",
            "required": ["issues", "summary", "overall_quality"],
            "properties": {
                "issues": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "required": ["level", "category", "text", "suggestion"],
                        "properties": {
                            "level": {
                                "type": "string",
                                "enum": ["error", "warning", "suggestion"],
                            },
                            "category": {
                                "type": "string",
                                "enum": [
                                    "bias_risk",
                                    "vagueness",
                                    "missing_section",
                                    "legal_risk",
                                    "clarity",
                                    "completeness",
                                ],
                            },
                            "text": {
                                "type": "string",
                                "description": "The problematic text or missing element",
                            },
                            "suggestion": {
                                "type": "string",
                                "description": "What to do about it",
                            },
                        },
                    },
                },
                "summary": {
                    "type": "string",
                    "description": "2-3 sentence overall assessment",
                },
                "overall_quality": {
                    "type": "string",
                    "enum": ["strong", "adequate", "needs_work", "problematic"],
                },
            },
        }
