"""SpecKit — Spec files for AI-native people management."""

from speckit.spec import SpecFile, load_spec, parse_spec, list_specs
from speckit.validation import ValidationIssue, validate_spec_structure, VALID_KINDS
from speckit.run_record import RunRecord
from speckit.engine import Engine
from speckit.registry import ModuleRegistry, create_default_registry

__version__ = "0.1.0"


class SpecKitError(Exception):
    """Base exception for SpecKit."""


class SpecValidationError(SpecKitError):
    """Raised when a spec file fails validation."""


class UnknownModuleError(SpecKitError):
    """Raised when an unknown module is requested."""

    def __init__(self, action: str):
        self.action = action
        super().__init__(f"Unknown module: '{action}'")


class IncompatibleSpecError(SpecKitError):
    """Raised when a module doesn't support the given spec kind."""

    def __init__(self, action: str, spec_kind: str, supported_kinds: list[str]):
        self.action = action
        self.spec_kind = spec_kind
        self.supported_kinds = supported_kinds
        super().__init__(
            f"Module '{action}' does not support spec kind '{spec_kind}'. "
            f"Supported kinds: {supported_kinds}"
        )


class EngineError(SpecKitError):
    """Raised when the engine encounters an error during execution."""
