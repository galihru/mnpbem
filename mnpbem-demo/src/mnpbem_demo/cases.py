"""Demonstration case builders."""

from __future__ import annotations

import numpy as np


def demo_wavelength_grid(start_nm: float = 350.0, stop_nm: float = 900.0, count: int = 200) -> np.ndarray:
    """Return a default spectral grid for nanoparticle plasmonics demos."""
    if count <= 1:
        raise ValueError("count must be greater than 1")
    return np.linspace(start_nm, stop_nm, count)
