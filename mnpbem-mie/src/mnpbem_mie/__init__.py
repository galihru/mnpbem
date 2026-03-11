"""Mie and Rayleigh scattering approximations for spherical particles."""

from __future__ import annotations
from importlib.metadata import PackageNotFoundError, version

from .rayleigh import rayleigh_cross_sections, rayleigh_polarizability

__all__ = [
    "rayleigh_polarizability",
    "rayleigh_cross_sections",
    "__version__",
    "module_status",
]

try:
    __version__ = version("mnpbem-mie")
except PackageNotFoundError:
    __version__ = "0.0.0"

def module_status() -> str:
    """Return the package maturity level for this submodule."""
    return "alpha"






