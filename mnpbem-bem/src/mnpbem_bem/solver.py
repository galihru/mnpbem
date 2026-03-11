"""Minimal linear response solver protocol for BEM-style operators."""

from __future__ import annotations

from dataclasses import dataclass
import numpy as np


@dataclass
class LinearResponseSolver:
    """Solve A x = b for frequency-domain response."""

    matrix: np.ndarray

    def solve(self, rhs: np.ndarray) -> np.ndarray:
        a = np.asarray(self.matrix, dtype=complex)
        b = np.asarray(rhs, dtype=complex)
        return np.linalg.solve(a, b)
