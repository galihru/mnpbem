"""2D mesh geometry primitives for computational plasmonics meshes."""

from __future__ import annotations
from importlib.metadata import PackageNotFoundError, version

from .geometry import circumcircle, quality, triarea

__all__ = [
    "triarea",
    "circumcircle",
    "quality",
    "__version__",
    "module_status",
]

try:
    __version__ = version("mnpbem-mesh2d")
except PackageNotFoundError:
    __version__ = "0.0.0"

def module_status() -> str:
    """Return the package maturity level for this submodule."""
    return "alpha"






