"""Reproducible demonstration scaffolding for MNPBEM Python modules."""

from __future__ import annotations
from importlib.metadata import PackageNotFoundError, version

from .cases import demo_wavelength_grid

__all__ = ["demo_wavelength_grid", "__version__", "module_status"]

try:
    __version__ = version("mnpbem-demo")
except PackageNotFoundError:
    __version__ = "0.0.0"

def module_status() -> str:
    return "alpha"






