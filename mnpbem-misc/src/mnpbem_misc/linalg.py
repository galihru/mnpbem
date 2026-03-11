"""Linear algebra helpers for tensor-aware operations."""

from __future__ import annotations

import numpy as np


def matmul(a: np.ndarray | float | complex, x: np.ndarray | float | complex) -> np.ndarray | float | complex:
    """Generalized matrix multiplication matching MATLAB matmul.m intent."""
    if np.isscalar(a):
        return 0 if a == 0 else a * x

    if np.isscalar(x):
        return 0 if x == 0 else np.asarray(a) * x

    a_arr = np.asarray(a)
    x_arr = np.asarray(x)

    if a_arr.ndim == 1:
        # Diagonal action in MATLAB branch: diag(a) * x
        diag = np.diag(a_arr)
        x2 = x_arr.reshape((x_arr.shape[0], -1))
        y = diag @ x2
        return y.reshape(x_arr.shape)

    siza = a_arr.shape
    sizx = x_arr.shape
    y = a_arr.reshape((-1, siza[-1])) @ x_arr.reshape((sizx[0], -1))
    out_shape = siza[:-1] + sizx[1:]
    return y.reshape(out_shape)


def matcross(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Generalized cross product where vectors are stored along axis=1."""
    a_arr = np.asarray(a)
    b_arr = np.asarray(b)
    if a_arr.shape[1] != 3 or b_arr.shape[1] != 3:
        raise ValueError("a and b must have size 3 along axis=1")

    extra_dims = (1,) * (b_arr.ndim - 2)
    a0 = a_arr[:, 0].reshape((a_arr.shape[0],) + extra_dims)
    a1 = a_arr[:, 1].reshape((a_arr.shape[0],) + extra_dims)
    a2 = a_arr[:, 2].reshape((a_arr.shape[0],) + extra_dims)

    c1 = a1 * b_arr[:, 2, ...] - a2 * b_arr[:, 1, ...]
    c2 = a2 * b_arr[:, 0, ...] - a0 * b_arr[:, 2, ...]
    c3 = a0 * b_arr[:, 1, ...] - a1 * b_arr[:, 0, ...]
    return np.stack((c1, c2, c3), axis=1)


def inner(nvec: np.ndarray, a: np.ndarray, mul: np.ndarray | float | None = None) -> np.ndarray | float:
    """Inner product between vector array and tensor with optional pre-multiplication."""
    n = np.asarray(nvec)
    arr = np.asarray(a)
    if n.shape[0] != arr.shape[0]:
        return 0

    if mul is not None:
        arr = np.asarray(matmul(mul, arr))

    if arr.ndim == 2:
        return np.sum(n * arr, axis=1)

    expanded = n.reshape(n.shape + (1,) * (arr.ndim - 2))
    return np.sum(expanded * arr, axis=1)


def outer(nvec: np.ndarray, val: np.ndarray, mul: np.ndarray | float | None = None) -> np.ndarray | float:
    """Outer product between vector and tensor with optional pre-multiplication."""
    n = np.asarray(nvec)
    v = np.asarray(val)
    if mul is not None:
        v = np.asarray(matmul(mul, v))

    if n.shape[0] != v.shape[0]:
        return 0

    expanded = np.expand_dims(n, axis=tuple(range(2, v.ndim + 1)))
    v_expanded = np.expand_dims(v, axis=1)
    out = expanded * v_expanded
    if np.all(out == 0):
        return 0
    return out


def spdiag(a: np.ndarray) -> np.ndarray:
    """Place values on a dense diagonal matrix (NumPy equivalent of spdiags usage)."""
    vec = np.asarray(a).reshape(-1)
    return np.diag(vec)
