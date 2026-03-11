"""Free-space Green-function kernels used as baseline references."""

from __future__ import annotations

import numpy as np


def scalar_green(r_nm: np.ndarray | float, k_nm_inv: np.ndarray | complex) -> np.ndarray:
    """Compute scalar Green function G = exp(i k r) / (4 pi r)."""
    r = np.asarray(r_nm, dtype=float)
    k = np.asarray(k_nm_inv, dtype=complex)
    with np.errstate(divide="ignore", invalid="ignore"):
        g = np.exp(1j * k * r) / (4.0 * np.pi * r)
    return np.where(r == 0, 0.0 + 0.0j, g)


def dyadic_prefactor(r_nm: np.ndarray | float, k_nm_inv: np.ndarray | complex) -> np.ndarray:
    """Return k^2 * G(r,k), commonly appearing in dyadic formulations."""
    k = np.asarray(k_nm_inv, dtype=complex)
    return k**2 * scalar_green(r_nm, k)
