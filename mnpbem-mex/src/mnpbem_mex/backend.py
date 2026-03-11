"""Optional acceleration backend probes."""

from __future__ import annotations

import importlib.util


def has_acceleration_backend(module_name: str = "mnpbem_accel") -> bool:
    """Return True when an optional compiled acceleration backend is importable."""
    return importlib.util.find_spec(module_name) is not None
