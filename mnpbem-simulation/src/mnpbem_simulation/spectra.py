"""Spectrum orchestration helpers."""

from __future__ import annotations

from typing import Callable
import numpy as np


def sample_spectrum(
    wavelengths_nm: np.ndarray,
    response_fn: Callable[[np.ndarray], np.ndarray],
) -> np.ndarray:
    """Evaluate a vectorized response function over wavelength grid."""
    wavelengths = np.asarray(wavelengths_nm, dtype=float)
    response = np.asarray(response_fn(wavelengths), dtype=complex)
    if response.shape != wavelengths.shape:
        raise ValueError("response_fn must return an array with same shape as wavelengths")
    return response
