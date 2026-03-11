"""Material dielectric models for plasmonic electrodynamics."""

from __future__ import annotations
from importlib.metadata import PackageNotFoundError, version

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

try:
    __version__ = version("mnpbem-material")
except PackageNotFoundError:
    __version__ = "0.0.0"

def module_status() -> str:
    """Return the package maturity level for this submodule."""
    return "alpha"






