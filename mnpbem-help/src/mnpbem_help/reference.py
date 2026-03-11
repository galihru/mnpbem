"""Reference registry for package-level documentation discovery."""

from __future__ import annotations


def list_reference_modules() -> list[str]:
    """Return canonical submodule names for user documentation."""
    return [
        "mnpbem_base",
        "mnpbem_material",
        "mnpbem_mesh2d",
        "mnpbem_mie",
        "mnpbem_greenfun",
        "mnpbem_particles",
        "mnpbem_simulation",
    ]
