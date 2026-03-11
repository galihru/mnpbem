"""Reference and educational helper interfaces for MNPBEM Python users."""

from __future__ import annotations
from importlib.metadata import PackageNotFoundError, version

from .reference import list_reference_modules

__all__ = ["list_reference_modules", "__version__", "module_status"]

try:
    __version__ = version("mnpbem-help")
except PackageNotFoundError:
    __version__ = "0.0.0"

def module_status() -> str:
    return "alpha"






