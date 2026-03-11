"""Material dielectric models for plasmonic electrodynamics."""

from __future__ import annotations

from .models import EpsConst, EpsDrude, EpsFunction, EpsTable, wavenumber_in_medium

__all__ = [
    "EpsConst",
    "EpsDrude",
    "EpsFunction",
    "EpsTable",
    "wavenumber_in_medium",
    "__version__",
    "module_status",
]

__version__ = "0.1.0"


def module_status() -> str:
    """Return the package maturity level for this submodule."""
    return "alpha"
