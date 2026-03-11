"""Acceleration-facing interfaces corresponding to MNPBEM mex integrations."""

from __future__ import annotations
from importlib.metadata import PackageNotFoundError, version

from .backend import has_acceleration_backend

__all__ = ["has_acceleration_backend", "__version__", "module_status"]

try:
    __version__ = version("mnpbem-mex")
except PackageNotFoundError:
    __version__ = "0.0.0"

def module_status() -> str:
    return "alpha"






