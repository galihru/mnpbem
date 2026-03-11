"""High-level simulation orchestration helpers for MNPBEM workflows."""

from __future__ import annotations
from importlib.metadata import PackageNotFoundError, version

from .spectra import sample_spectrum

__all__ = ["sample_spectrum", "__version__", "module_status"]

try:
    __version__ = version("mnpbem-simulation")
except PackageNotFoundError:
    __version__ = "0.0.0"

def module_status() -> str:
    return "alpha"






