"""Pytest configuration for SpecKit evals."""


def pytest_configure(config):
    """Register custom markers."""
    config.addinivalue_line("markers", "slow: marks tests as slow (real API calls)")
    config.addinivalue_line("markers", "bias: marks tests as bias swap tests")
