"""Module registry — maps action names to modules."""

from __future__ import annotations

from hiring_manager_tools.modules.base import Module


class UnknownModuleError(Exception):
    """Raised when an unknown module is requested."""

    def __init__(self, action: str):
        self.action = action
        super().__init__(f"Unknown module: '{action}'")


class IncompatibleSpecError(Exception):
    """Raised when a module doesn't support the given spec kind."""

    def __init__(self, action: str, spec_kind: str, supported_kinds: list[str]):
        self.action = action
        self.spec_kind = spec_kind
        self.supported_kinds = supported_kinds
        super().__init__(
            f"Module '{action}' does not support spec kind '{spec_kind}'. "
            f"Supported kinds: {supported_kinds}"
        )


class ModuleRegistry:
    """Maps action names to modules. Validates spec kind compatibility."""

    def __init__(self):
        self._modules: dict[str, Module] = {}

    def register(self, module: Module):
        """Register a module."""
        self._modules[module.name] = module

    def resolve(self, action: str, spec_kind: str) -> Module:
        """Look up a module by action name.

        Raises IncompatibleSpecError if the module doesn't support
        this spec kind.
        """
        if action not in self._modules:
            raise UnknownModuleError(action)
        module = self._modules[action]
        if spec_kind not in module.supported_kinds:
            raise IncompatibleSpecError(action, spec_kind, module.supported_kinds)
        return module

    def list_modules(self, kind: str | None = None) -> list[Module]:
        """List all registered modules, optionally filtered by supported kind."""
        if kind is None:
            return list(self._modules.values())
        return [m for m in self._modules.values() if kind in m.supported_kinds]


def create_default_registry() -> ModuleRegistry:
    """Create a registry with all built-in modules."""
    from hiring_manager_tools.modules.interview_prep import InterviewPrepModule
    from hiring_manager_tools.modules.spec_lint import SpecLintModule

    registry = ModuleRegistry()
    registry.register(InterviewPrepModule())
    registry.register(SpecLintModule())
    return registry
