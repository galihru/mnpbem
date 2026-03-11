"""Meta-package that installs all MNPBEM Python submodules."""

from __future__ import annotations
from importlib.metadata import PackageNotFoundError, version

import importlib

SUBMODULES = (
    "mnpbem_base",
    "mnpbem_bem",
    "mnpbem_demo",
    "mnpbem_demo_mnpbem",
    "mnpbem_greenfun",
    "mnpbem_help",
    "mnpbem_material",
    "mnpbem_mesh2d",
    "mnpbem_mex",
    "mnpbem_mie",
    "mnpbem_misc",
    "mnpbem_particles",
    "mnpbem_simulation",
)

__all__ = ["SUBMODULES", "available_submodules", "__version__", "module_status"]

try:
    __version__ = version("mnpbem")
except PackageNotFoundError:
    __version__ = "0.0.0"

def available_submodules() -> list[str]:
    """Return installed MNPBEM submodules discoverable in current environment."""
    installed: list[str] = []
    for name in SUBMODULES:
        if importlib.util.find_spec(name) is not None:
            installed.append(name)
    return installed


def module_status() -> str:
    """Return the package maturity level for this submodule."""
    return "alpha"






