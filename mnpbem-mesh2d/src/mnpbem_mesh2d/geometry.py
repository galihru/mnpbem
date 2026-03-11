"""Triangle geometry helpers aligned with MATLAB Mesh2d formulas."""

from __future__ import annotations

import numpy as np


def _to_zero_based_indices(points: np.ndarray, triangles: np.ndarray) -> np.ndarray:
    tri = np.asarray(triangles, dtype=int)
    if tri.ndim != 2 or tri.shape[1] != 3:
        raise ValueError("triangles must have shape (m, 3)")

    if tri.size == 0:
        return tri

    if np.min(tri) == 1 and np.max(tri) <= points.shape[0]:
        tri = tri - 1
    if np.min(tri) < 0 or np.max(tri) >= points.shape[0]:
        raise IndexError("triangle indices are out of bounds")
    return tri


def triarea(p: np.ndarray, t: np.ndarray) -> np.ndarray:
    """Return signed doubled area A = d12_x*d13_y - d12_y*d13_x for each triangle."""
    points = np.asarray(p, dtype=float)
    tri = _to_zero_based_indices(points, t)

    d12 = points[tri[:, 1], :] - points[tri[:, 0], :]
    d13 = points[tri[:, 2], :] - points[tri[:, 0], :]
    return d12[:, 0] * d13[:, 1] - d12[:, 1] * d13[:, 0]


def circumcircle(p: np.ndarray, t: np.ndarray) -> np.ndarray:
    """Return circumcircle centers and squared radii as array (m, 3)."""
    points = np.asarray(p, dtype=float)
    tri = _to_zero_based_indices(points, t)

    p1 = points[tri[:, 0], :]
    p2 = points[tri[:, 1], :]
    p3 = points[tri[:, 2], :]

    a1 = p2 - p1
    a2 = p3 - p1
    b1 = np.sum(a1 * (p2 + p1), axis=1)
    b2 = np.sum(a2 * (p3 + p1), axis=1)

    det = a1[:, 0] * a2[:, 1] - a2[:, 0] * a1[:, 1]
    if np.any(det == 0):
        raise ValueError("Degenerate triangle encountered while computing circumcircle")

    idet = 0.5 / det
    x = (a2[:, 1] * b1 - a1[:, 1] * b2) * idet
    y = (-a2[:, 0] * b1 + a1[:, 0] * b2) * idet

    center = np.column_stack((x, y))
    radius_sq = np.sum((p1 - center) ** 2, axis=1)
    return np.column_stack((center, radius_sq))


def quality(p: np.ndarray, t: np.ndarray) -> np.ndarray:
    """Return approximate triangle quality in [0, 1] using Mesh2d formula."""
    points = np.asarray(p, dtype=float)
    tri = _to_zero_based_indices(points, t)

    p1 = points[tri[:, 0], :]
    p2 = points[tri[:, 1], :]
    p3 = points[tri[:, 2], :]

    d12 = p2 - p1
    d13 = p3 - p1
    d23 = p3 - p2

    numer = 3.4641 * np.abs(d12[:, 0] * d13[:, 1] - d12[:, 1] * d13[:, 0])
    denom = np.sum(d12**2 + d13**2 + d23**2, axis=1)
    with np.errstate(divide="ignore", invalid="ignore"):
        q = np.divide(numer, denom, out=np.zeros_like(numer), where=denom != 0)
    return q
