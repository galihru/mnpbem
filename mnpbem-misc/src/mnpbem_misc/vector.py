"""Vector-norm and normalization helpers."""

from __future__ import annotations

import numpy as np


def vecnorm(v: np.ndarray, key: str | None = None) -> np.ndarray | float:
    """Return Euclidean norm along axis=1, following MATLAB vecnorm.m behavior."""
    arr = np.asarray(v)
    n = np.sqrt(np.sum(np.abs(arr) * np.abs(arr), axis=1))
    if key == "max":
        return float(np.max(n))
    return n


def vecnormalize(v: np.ndarray, v2: np.ndarray | None = None, key: str | None = None) -> np.ndarray:
    """Normalize vector/tensor arrays with MATLAB-compatible modes."""
    arr = np.asarray(v, dtype=complex)
    ref = arr if v2 is None else np.asarray(v2, dtype=complex)
    n = np.sqrt(np.sum(np.abs(ref) * np.abs(ref), axis=1, keepdims=True))

    if key == "max":
        scale = np.max(n)
        if scale == 0:
            return arr.copy()
        return arr / scale

    if key == "max2":
        # Per trailing-index normalization analogous to max(n, [], 1) in MATLAB.
        scale = np.max(n, axis=0, keepdims=True)
        scale = np.where(scale == 0, 1.0, scale)
        return arr / scale

    safe_n = np.where(n == 0, 1.0, n)
    return arr / safe_n
