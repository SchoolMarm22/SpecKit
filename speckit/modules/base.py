"""Abstract Module base class and shared types."""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field


@dataclass
class InvocationPlan:
    """What the module wants Claude to do."""

    system_prompt: str
    messages: list[dict] = field(default_factory=list)
    tool_schema: dict = field(default_factory=dict)
    prompt_version: str = "unknown"


@dataclass
class ModuleResult:
    """What came back from Claude, validated and annotated."""

    output: dict = field(default_factory=dict)
    meta: dict = field(default_factory=dict)


class Module(ABC):
    """Base class for all SpecKit modules."""

    @property
    @abstractmethod
    def name(self) -> str:
        """Module identifier. E.g., 'interview_prep', 'spec_lint'."""

    @property
    @abstractmethod
    def supported_kinds(self) -> list[str]:
        """Which spec kinds this module can operate on."""

    @abstractmethod
    def input_schema(self) -> dict:
        """Describes what inputs this module needs beyond the spec."""

    @abstractmethod
    def plan(self, spec, inputs: dict) -> InvocationPlan:
        """Build the full invocation plan."""

    @abstractmethod
    def output_schema(self) -> dict:
        """JSON schema defining the structured output shape."""

    def _load_prompt_template(self) -> str:
        """Load prompt template from prompts/{name}.md, return body (no frontmatter)."""
        import os
        import yaml

        # Resolve relative to project root (where prompts/ lives)
        # Try multiple locations: cwd, package parent dir
        for base in [os.getcwd(), os.path.dirname(os.path.dirname(os.path.dirname(__file__)))]:
            path = os.path.join(base, "prompts", f"{self.name}.md")
            if os.path.exists(path):
                with open(path, "r", encoding="utf-8") as f:
                    raw = f.read()
                # Split frontmatter
                raw = raw.strip()
                if raw.startswith("---"):
                    end = raw.find("---", 3)
                    if end != -1:
                        return raw[end + 3:].strip()
                return raw

        raise FileNotFoundError(f"Prompt template not found: prompts/{self.name}.md")

    def _get_prompt_version(self) -> str:
        """Extract prompt_version from the prompt template frontmatter."""
        import os
        import yaml

        for base in [os.getcwd(), os.path.dirname(os.path.dirname(os.path.dirname(__file__)))]:
            path = os.path.join(base, "prompts", f"{self.name}.md")
            if os.path.exists(path):
                with open(path, "r", encoding="utf-8") as f:
                    raw = f.read()
                raw = raw.strip()
                if raw.startswith("---"):
                    end = raw.find("---", 3)
                    if end != -1:
                        frontmatter = yaml.safe_load(raw[3:end])
                        if frontmatter and "prompt_version" in frontmatter:
                            return frontmatter["prompt_version"]
                return "unknown"

        return "unknown"
