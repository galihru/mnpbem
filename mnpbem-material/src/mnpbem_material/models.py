"""Dielectric-function models for nanoscale electrodynamics.

Core relations used in this module:
1) k(lambda) = 2*pi/lambda * sqrt(epsilon)
2) Drude model:
   epsilon(w) = epsilon_inf - wp^2 / (w * (w + i*gamma))
3) Tabulated optical constants:
   epsilon = (n + i*kappa)^2
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Callable

import numpy as np

EV_TO_NM = 1.0 / 8.0655477e-4
HARTREE_EV = 27.2116


def _as_float_array(values: np.ndarray | float) -> np.ndarray:
    return np.asarray(values, dtype=float)


def wavenumber_in_medium(wavelength_nm: np.ndarray | float, epsilon: np.ndarray | complex) -> np.ndarray:
    """Return medium wavenumber k = 2*pi/lambda * sqrt(epsilon)."""
    wavelength = _as_float_array(wavelength_nm)
    eps = np.asarray(epsilon, dtype=complex)
    return 2.0 * np.pi / wavelength * np.sqrt(eps)


@dataclass(frozen=True)
class EpsConst:
    """Constant dielectric function model."""

    eps: complex | float

    def __call__(self, wavelength_nm: np.ndarray | float) -> tuple[np.ndarray, np.ndarray]:
        wavelength = _as_float_array(wavelength_nm)
        eps = np.full(wavelength.shape, complex(self.eps), dtype=complex)
        return eps, wavenumber_in_medium(wavelength, eps)

    def wavenumber(self, wavelength_nm: np.ndarray | float) -> np.ndarray:
        wavelength = _as_float_array(wavelength_nm)
        return wavenumber_in_medium(wavelength, complex(self.eps))


class EpsDrude:
    """Drude dielectric model for free-electron response in metals.

    epsilon(w) = epsilon_inf - wp^2 / (w * (w + i*gamma))
    """

    _TABLE = {
        "au": {"rs": 3.0, "eps0": 10.0, "gammad_au": (0.66 / HARTREE_EV) / 10.0},
        "gold": {"rs": 3.0, "eps0": 10.0, "gammad_au": (0.66 / HARTREE_EV) / 10.0},
        "ag": {"rs": 3.0, "eps0": 3.3, "gammad_au": (0.66 / HARTREE_EV) / 30.0},
        "silver": {"rs": 3.0, "eps0": 3.3, "gammad_au": (0.66 / HARTREE_EV) / 30.0},
        "al": {"rs": 2.07, "eps0": 1.0, "gammad_au": 1.06 / HARTREE_EV},
        "aluminum": {"rs": 2.07, "eps0": 1.0, "gammad_au": 1.06 / HARTREE_EV},
    }

    def __init__(self, name: str) -> None:
        key = name.lower()
        if key not in self._TABLE:
            raise ValueError("Material name unknown")

        row = self._TABLE[key]
        rs = row["rs"]
        density = 3.0 / (4.0 * np.pi * rs**3)
        wp_au = np.sqrt(4.0 * np.pi * density)

        self.name = name
        self.eps0 = float(row["eps0"])
        self.gammad = float(row["gammad_au"] * HARTREE_EV)
        self.wp = float(wp_au * HARTREE_EV)

    def __call__(self, wavelength_nm: np.ndarray | float) -> tuple[np.ndarray, np.ndarray]:
        wavelength = _as_float_array(wavelength_nm)
        w = EV_TO_NM / wavelength
        eps = self.eps0 - self.wp**2 / (w * (w + 1j * self.gammad))
        return eps, wavenumber_in_medium(wavelength, eps)


class EpsFunction:
    """Dielectric function from a user-provided callable."""

    def __init__(self, fun: Callable[[np.ndarray], np.ndarray], key: str = "nm") -> None:
        if key not in {"nm", "eV"}:
            raise ValueError("key must be 'nm' or 'eV'")
        self.fun = fun
        self.key = key

    def __call__(self, wavelength_nm: np.ndarray | float) -> tuple[np.ndarray, np.ndarray]:
        wavelength = _as_float_array(wavelength_nm)
        if self.key == "nm":
            eps = np.asarray(self.fun(wavelength), dtype=complex)
        else:
            eps = np.asarray(self.fun(EV_TO_NM / wavelength), dtype=complex)
        return eps, wavenumber_in_medium(wavelength, eps)


class EpsTable:
    """Interpolate dielectric function from tabulated (energy, n, k) data."""

    def __init__(self, file_path: str | Path) -> None:
        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError(path)

        table = np.loadtxt(path, comments=("%", "#"), dtype=float)
        if table.ndim != 2 or table.shape[1] < 3:
            raise ValueError("Table must have at least 3 columns: energy_eV, n, k")

        ene_ev = table[:, 0]
        n = table[:, 1]
        k = table[:, 2]

        wavelength_nm = EV_TO_NM / ene_ev
        order = np.argsort(wavelength_nm)

        self.wavelength_nm = wavelength_nm[order]
        self.n_real = n[order]
        self.k_imag = k[order]

    @classmethod
    def from_builtin(cls, filename: str) -> "EpsTable":
        data_path = Path(__file__).resolve().parent / "data" / filename
        return cls(data_path)

    def __call__(self, wavelength_nm: np.ndarray | float) -> tuple[np.ndarray, np.ndarray]:
        wavelength = _as_float_array(wavelength_nm)
        wmin = float(np.min(self.wavelength_nm))
        wmax = float(np.max(self.wavelength_nm))

        if np.min(wavelength) < wmin or np.max(wavelength) > wmax:
            raise ValueError(
                f"Requested wavelengths must lie within [{wmin:.6g}, {wmax:.6g}] nm"
            )

        n = np.interp(wavelength, self.wavelength_nm, self.n_real)
        k = np.interp(wavelength, self.wavelength_nm, self.k_imag)
        eps = (n + 1j * k) ** 2
        return eps, wavenumber_in_medium(wavelength, eps)
