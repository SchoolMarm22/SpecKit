"""Spec file validation — structural checks, no API calls."""

from __future__ import annotations

from dataclasses import dataclass

VALID_KINDS = {"hiring", "review", "team", "onboarding", "offboarding"}


@dataclass
class ValidationIssue:
    """A single validation finding."""

    level: str       # "error" | "warning" | "suggestion"
    field: str       # What field/section this relates to
    message: str     # Human-readable explanation


def validate_spec_structure(spec) -> list[ValidationIssue]:
    """Validate structural issues — missing required fields,
    unknown kinds, etc. This is NOT the AI-powered lint.
    This is fast, deterministic, no API call."""
    issues = []

    if not spec.kind:
        issues.append(
            ValidationIssue("error", "kind", "Spec file is missing the 'kind' field")
        )

    if spec.kind and spec.kind not in VALID_KINDS:
        issues.append(
            ValidationIssue("error", "kind", f"Unknown spec kind: '{spec.kind}'")
        )

    if spec.kind == "hiring":
        for field_name in ["role", "team", "level"]:
            if field_name not in spec.metadata:
                issues.append(
                    ValidationIssue(
                        "error",
                        field_name,
                        f"Hiring specs require '{field_name}' in frontmatter",
                    )
                )

    if "version" not in spec.metadata:
        issues.append(
            ValidationIssue(
                "warning", "version", "No version specified. Defaults to 1."
            )
        )

    # Section suggestions for hiring specs
    if spec.kind == "hiring":
        if "must_haves" not in spec.sections:
            issues.append(
                ValidationIssue(
                    "suggestion",
                    "sections",
                    "Consider adding a '## Must-Haves' section",
                )
            )
        if "anti_patterns" not in spec.sections:
            issues.append(
                ValidationIssue(
                    "suggestion",
                    "sections",
                    "Consider adding an '## Anti-Patterns' section",
                )
            )

    return issues
