"""Spec lint eval — known-bad specs should produce correct flags."""

import os
import pytest

from speckit.spec import parse_spec, load_spec
from speckit.claude_client import ClaudeClient
from speckit.engine import Engine
from speckit.registry import create_default_registry


BIASED_SPEC_PATH = os.path.join("evals", "fixtures", "biased_spec.md")
GOOD_SPEC_PATH = os.path.join("specs", "hiring", "senior-frontend-platform.md")


def _run_lint(spec_text: str = None, spec_path: str = None) -> dict:
    """Run the spec lint module and return the output."""
    if spec_path:
        spec = load_spec(spec_path)
    else:
        spec = parse_spec(spec_text)

    registry = create_default_registry()
    module = registry.resolve("spec_lint", spec.kind)
    plan = module.plan(spec, {})

    client = ClaudeClient()
    engine = Engine(client)
    result = engine.execute(plan, spec, module.name)
    return result.output


@pytest.mark.slow
class TestSpecLint:
    """Validate that the lint module catches known issues."""

    def test_culture_fit_flagged(self):
        """'Culture fit' language should produce a bias_risk warning."""
        result = _run_lint(spec_path=BIASED_SPEC_PATH)

        categories = [issue["category"] for issue in result["issues"]]
        assert "bias_risk" in categories, (
            f"Expected bias_risk issue for 'culture fit' language. "
            f"Got categories: {categories}"
        )

    def test_native_speaker_flagged(self):
        """'Native English speaker' should produce a legal_risk error."""
        result = _run_lint(spec_path=BIASED_SPEC_PATH)

        # Should have either legal_risk or bias_risk for native speaker
        issue_texts = [
            issue["text"].lower() for issue in result["issues"]
        ]
        has_native_speaker_flag = any(
            "native" in text or "speaker" in text
            for text in issue_texts
        )
        assert has_native_speaker_flag, (
            f"Expected flag for 'native English speaker'. Issues: {issue_texts}"
        )

    def test_missing_anti_patterns_flagged(self):
        """A spec with no anti-patterns should get a missing_section suggestion."""
        spec_text = """---
kind: hiring
role: Engineer
team: Backend
level: L4
version: 1
---

# What We Want

A solid backend engineer with Python experience.

## Must-Haves
- 3+ years Python
- Experience with REST APIs
- Database design skills
"""
        result = _run_lint(spec_text=spec_text)

        categories = [issue["category"] for issue in result["issues"]]
        assert "missing_section" in categories, (
            f"Expected missing_section for spec without anti-patterns. "
            f"Got categories: {categories}"
        )

    def test_biased_spec_overall_quality(self):
        """The biased fixture spec should get 'needs_work' or 'problematic'."""
        result = _run_lint(spec_path=BIASED_SPEC_PATH)

        assert result["overall_quality"] in ("needs_work", "problematic"), (
            f"Expected poor quality rating for biased spec. "
            f"Got: {result['overall_quality']}"
        )

    def test_good_spec_no_errors(self):
        """The good fixture spec should have no errors."""
        result = _run_lint(spec_path=GOOD_SPEC_PATH)

        error_issues = [
            issue for issue in result["issues"]
            if issue["level"] == "error"
        ]
        assert len(error_issues) == 0, (
            f"Good spec should have no errors. Got: {error_issues}"
        )

    def test_good_spec_quality(self):
        """The good fixture spec should get 'strong' or 'adequate'."""
        result = _run_lint(spec_path=GOOD_SPEC_PATH)

        assert result["overall_quality"] in ("strong", "adequate"), (
            f"Expected good quality for clean spec. Got: {result['overall_quality']}"
        )

    def test_vagueness_flagged(self):
        """Vague criteria like 'team player' should be flagged."""
        result = _run_lint(spec_path=BIASED_SPEC_PATH)

        categories = [issue["category"] for issue in result["issues"]]
        assert "vagueness" in categories, (
            f"Expected vagueness flag for 'team player', 'self-starter'. "
            f"Got categories: {categories}"
        )
