"""Green-function utilities and kernels for electrodynamics simulations."""

from __future__ import annotations
from importlib.metadata import PackageNotFoundError, version

from .kernels import dyadic_prefactor, scalar_green

__all__ = ["scalar_green", "dyadic_prefactor", "__version__", "module_status"]

try:
    __version__ = version("mnpbem-greenfun")
except PackageNotFoundError:
    __version__ = "0.0.0"

def module_status() -> str:
    return "alpha"






