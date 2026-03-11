"""Geometric particle primitives."""

from __future__ import annotations

from dataclasses import dataclass
import numpy as np


def sphere_volume(radius_nm: float) -> float:
    """Return volume of a sphere (nm^3)."""
    r = float(radius_nm)
    return 4.0 / 3.0 * np.pi * r**3


@dataclass(frozen=True)
class Sphere:
    """Spherical particle primitive."""

    radius_nm: float

    @property
    def volume_nm3(self) -> float:
        return sphere_volume(self.radius_nm)
