"""Hiring Manager Tools — Spec files for AI-native people management."""

from __future__ import annotations

from hiring_manager_tools.spec import SpecFile, load_spec, parse_spec, list_specs
from hiring_manager_tools.validation import ValidationIssue, validate_spec_structure, VALID_KINDS
from hiring_manager_tools.run_record import RunRecord
from hiring_manager_tools.engine import Engine
from hiring_manager_tools.registry import ModuleRegistry, create_default_registry

__version__ = "0.1.0"


class HMTError(Exception):
    """Base exception for Hiring Manager Tools."""


class SpecValidationError(HMTError):
    """Raised when a spec file fails validation."""


class UnknownModuleError(HMTError):
    """Raised when an unknown module is requested."""

    def __init__(self, action: str):
        self.action = action
        super().__init__(f"Unknown module: '{action}'")


class IncompatibleSpecError(HMTError):
    """Raised when a module doesn't support the given spec kind."""

    def __init__(self, action: str, spec_kind: str, supported_kinds: list[str]):
        self.action = action
        self.spec_kind = spec_kind
        self.supported_kinds = supported_kinds
        super().__init__(
            f"Module '{action}' does not support spec kind '{spec_kind}'. "
            f"Supported kinds: {supported_kinds}"
        )


class EngineError(HMTError):
    """Raised when the engine encounters an error during execution."""
