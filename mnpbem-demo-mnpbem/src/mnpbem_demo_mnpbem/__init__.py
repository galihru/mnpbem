"""Extended demonstration layer corresponding to the MATLAB Demo MNPBEM folder."""

from __future__ import annotations
from importlib.metadata import PackageNotFoundError, version

from .runner import demo_summary

__all__ = ["demo_summary", "__version__", "module_status"]

try:
    __version__ = version("mnpbem-demo-mnpbem")
except PackageNotFoundError:
    __version__ = "0.0.0"

def module_status() -> str:
    return "alpha"






