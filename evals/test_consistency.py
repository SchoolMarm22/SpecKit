"""Consistency eval — same input should produce stable output across runs."""

import os
import pytest
from collections import Counter

from hiring_manager_tools.spec import load_spec
from hiring_manager_tools.claude_client import ClaudeClient
from hiring_manager_tools.engine import Engine
from hiring_manager_tools.registry import create_default_registry


SPEC_PATH = os.path.join("specs", "hiring", "senior-frontend-platform.md")
RESUME_PATH = os.path.join("evals", "fixtures", "sample_resume.md")
NUM_RUNS = 3


@pytest.fixture(scope="module")
def results():
    """Run interview prep NUM_RUNS times and collect results."""
    spec = load_spec(SPEC_PATH)

    with open(RESUME_PATH, "r", encoding="utf-8") as f:
        resume_text = f.read()

    registry = create_default_registry()
    module = registry.resolve("interview_prep", spec.kind)

    client = ClaudeClient()
    engine = Engine(client)

    outputs = []
    for _ in range(NUM_RUNS):
        plan = module.plan(spec, {"resume_text": resume_text})
        result = engine.execute(plan, spec, module.name)
        outputs.append(result.output)

    return outputs


@pytest.mark.slow
class TestConsistency:
    """Verify that repeated runs produce structurally stable output."""

    def test_same_question_categories(self, results):
        """The same question category distribution should appear across runs."""
        category_sets = []
        for output in results:
            categories = Counter(
                q["category"] for q in output["recommended_questions"]
            )
            category_sets.append(set(categories.keys()))

        # All runs should have the same set of categories
        first = category_sets[0]
        for i, cats in enumerate(category_sets[1:], 1):
            assert cats == first, (
                f"Run {i} has different categories: {cats} vs {first}"
            )

    def test_spec_alignment_criteria_stable(self, results):
        """The same criteria should be identified across runs."""
        criteria_sets = []
        for output in results:
            criteria = set(
                item["criterion"].lower().strip()
                for item in output["spec_alignment"]
            )
            criteria_sets.append(criteria)

        # At least 70% overlap between any two runs
        for i in range(len(criteria_sets)):
            for j in range(i + 1, len(criteria_sets)):
                overlap = len(criteria_sets[i] & criteria_sets[j])
                total = max(len(criteria_sets[i]), len(criteria_sets[j]))
                ratio = overlap / total if total > 0 else 1.0
                assert ratio >= 0.7, (
                    f"Runs {i} and {j} have low criteria overlap: {ratio:.2f}"
                )

    def test_confidence_levels_consistent(self, results):
        """Confidence levels should not wildly vary across runs."""
        # Map criterion -> confidence across runs
        confidence_map = {}
        for run_idx, output in enumerate(results):
            for item in output["spec_alignment"]:
                key = item["criterion"].lower().strip()
                if key not in confidence_map:
                    confidence_map[key] = []
                confidence_map[key].append(item["confidence"])

        # For criteria that appear in all runs, confidence should be within 1 step
        confidence_order = ["strong", "moderate", "weak", "no_signal"]
        for criterion, levels in confidence_map.items():
            if len(levels) < NUM_RUNS:
                continue
            indices = [confidence_order.index(l) for l in levels if l in confidence_order]
            if indices:
                spread = max(indices) - min(indices)
                assert spread <= 1, (
                    f"Criterion '{criterion}' has confidence spread of {spread}: {levels}"
                )

    def test_question_count_stable(self, results):
        """Number of questions should be consistent (8-10 per spec)."""
        counts = [len(output["recommended_questions"]) for output in results]
        for count in counts:
            assert 6 <= count <= 12, f"Unexpected question count: {count}"
        # Counts shouldn't vary by more than 2
        assert max(counts) - min(counts) <= 2, (
            f"Question counts vary too much: {counts}"
        )

    def test_candidate_snapshot_present(self, results):
        """Every run should produce a non-empty candidate snapshot."""
        for i, output in enumerate(results):
            snapshot = output["candidate_snapshot"]
            assert isinstance(snapshot, str), f"Run {i}: snapshot is not a string"
            assert len(snapshot) > 50, f"Run {i}: snapshot too short ({len(snapshot)} chars)"

    def test_bias_check_present(self, results):
        """Every run should produce a bias check."""
        for i, output in enumerate(results):
            assert "bias_check" in output, f"Run {i}: missing bias_check"
            assert "note" in output["bias_check"], f"Run {i}: missing bias_check.note"
            assert isinstance(output["bias_check"]["flags"], list), (
                f"Run {i}: bias_check.flags is not a list"
            )
