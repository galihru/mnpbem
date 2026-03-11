"""Core BEM namespace package and solver-facing compatibility helpers."""

from __future__ import annotations
from importlib.metadata import PackageNotFoundError, version

from .solver import LinearResponseSolver

__all__ = ["LinearResponseSolver", "__version__", "module_status"]

try:
    __version__ = version("mnpbem-bem")
except PackageNotFoundError:
    __version__ = "0.0.0"

def module_status() -> str:
    return "alpha"






