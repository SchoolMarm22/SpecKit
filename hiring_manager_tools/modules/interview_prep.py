"""Interview prep module — spec + resume → structured interview package."""

from __future__ import annotations

from hiring_manager_tools.modules.base import Module, InvocationPlan


class InterviewPrepModule(Module):
    """Produces a structured interview preparation package from a hiring spec and resume."""

    @property
    def name(self) -> str:
        return "interview_prep"

    @property
    def supported_kinds(self) -> list[str]:
        return ["hiring"]

    def input_schema(self) -> dict:
        return {
            "type": "object",
            "required": ["resume_text"],
            "properties": {
                "resume_text": {
                    "type": "string",
                    "description": "The candidate's resume as plain text",
                }
            },
        }

    def plan(self, spec, inputs: dict) -> InvocationPlan:
        system_prompt = self._load_prompt_template()
        user_message = self._build_user_message(spec, inputs["resume_text"])

        return InvocationPlan(
            system_prompt=system_prompt,
            messages=[{"role": "user", "content": user_message}],
            tool_schema=self.output_schema(),
            prompt_version=self._get_prompt_version(),
        )

    def _build_user_message(self, spec, resume_text: str) -> str:
        return f"""## Hiring Spec

**Role:** {spec.metadata.get('role', 'Not specified')}
**Team:** {spec.metadata.get('team', 'Not specified')}
**Level:** {spec.metadata.get('level', 'Not specified')}

{spec.body}

---

## Candidate Resume

{resume_text}

---

Produce a structured interview preparation package for the interviewer based on this spec and resume."""

    def output_schema(self) -> dict:
        """The JSON schema for the interview prep output."""
        return {
            "type": "object",
            "required": [
                "candidate_snapshot",
                "spec_alignment",
                "recommended_questions",
                "bias_check",
            ],
            "properties": {
                "candidate_snapshot": {
                    "type": "string",
                    "description": "3-4 sentence summary of who this candidate is and what to focus on in the interview",
                },
                "spec_alignment": {
                    "type": "array",
                    "description": "Item-by-item assessment of how the candidate maps to each criterion in the spec",
                    "items": {
                        "type": "object",
                        "required": [
                            "criterion",
                            "signal",
                            "confidence",
                            "follow_up",
                        ],
                        "properties": {
                            "criterion": {
                                "type": "string",
                                "description": "The spec criterion being evaluated",
                            },
                            "signal": {
                                "type": "string",
                                "description": "What in the resume supports or contradicts this criterion",
                            },
                            "confidence": {
                                "type": "string",
                                "enum": [
                                    "strong",
                                    "moderate",
                                    "weak",
                                    "no_signal",
                                ],
                                "description": "How confident the assessment is based on available evidence",
                            },
                            "follow_up": {
                                "type": "string",
                                "description": "A suggested question or probe to verify this in the interview",
                            },
                        },
                    },
                },
                "recommended_questions": {
                    "type": "array",
                    "description": "8-10 tailored interview questions",
                    "items": {
                        "type": "object",
                        "required": [
                            "question",
                            "category",
                            "seeks",
                            "good_answer_looks_like",
                            "red_flags",
                        ],
                        "properties": {
                            "question": {
                                "type": "string",
                                "description": "The interview question to ask",
                            },
                            "category": {
                                "type": "string",
                                "enum": [
                                    "technical_depth",
                                    "experience_verification",
                                    "culture_and_collaboration",
                                    "growth_areas",
                                ],
                                "description": "Question category",
                            },
                            "seeks": {
                                "type": "string",
                                "description": "What signal this question is designed to surface",
                            },
                            "good_answer_looks_like": {
                                "type": "string",
                                "description": "What a strong response would include",
                            },
                            "red_flags": {
                                "type": "string",
                                "description": "Warning signs in the candidate's response",
                            },
                        },
                    },
                },
                "bias_check": {
                    "type": "object",
                    "required": ["flags", "note"],
                    "properties": {
                        "flags": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Any non-job-relevant factors that may have influenced the assessment",
                        },
                        "note": {
                            "type": "string",
                            "description": "Summary of bias check findings",
                        },
                    },
                },
            },
        }
