"""Shared numerical and vector algebra toolkit for MNPBEM-Python."""

from __future__ import annotations
from importlib.metadata import PackageNotFoundError, version

from .linalg import inner, matcross, matmul, outer, spdiag
from .units import EV_TO_NM, NM_TO_EV, ev_to_nm, nm_to_ev
from .vector import vecnorm, vecnormalize

__all__ = [
    "EV_TO_NM",
    "NM_TO_EV",
    "ev_to_nm",
    "nm_to_ev",
    "vecnorm",
    "vecnormalize",
    "matmul",
    "matcross",
    "inner",
    "outer",
    "spdiag",
    "__version__",
    "module_status",
]

try:
    __version__ = version("mnpbem-misc")
except PackageNotFoundError:
    __version__ = "0.0.0"


def module_status() -> str:
    """Return the package maturity level for this submodule."""
    return "alpha"






