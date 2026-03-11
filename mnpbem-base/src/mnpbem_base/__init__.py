"""Factory and registry primitives for selecting BEM solvers and excitation operators."""

from __future__ import annotations
from importlib.metadata import PackageNotFoundError, version

from .factory import bemsolver, dipole, electronbeam, greenfunction, planewave, spectrum
from .registry import BEMRegistry, default_registry, register

__all__ = [
    "BEMRegistry",
    "default_registry",
    "register",
    "bemsolver",
    "dipole",
    "electronbeam",
    "greenfunction",
    "planewave",
    "spectrum",
    "__version__",
    "module_status",
]

try:
    __version__ = version("mnpbem-base")
except PackageNotFoundError:
    __version__ = "0.0.0"

def module_status() -> str:
    """Return the package maturity level for this submodule."""
    return "alpha"






