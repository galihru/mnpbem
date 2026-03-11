"""Particle abstractions for compositional nanostructure modeling."""

from __future__ import annotations
from importlib.metadata import PackageNotFoundError, version

from .primitives import Sphere, sphere_volume

__all__ = ["Sphere", "sphere_volume", "__version__", "module_status"]

try:
    __version__ = version("mnpbem-particles")
except PackageNotFoundError:
    __version__ = "0.0.0"

def module_status() -> str:
    return "alpha"






