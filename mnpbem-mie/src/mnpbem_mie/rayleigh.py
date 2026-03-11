"""Small-particle (Rayleigh) scattering formulas for quick spectral estimates."""

from __future__ import annotations

import numpy as np


def rayleigh_polarizability(
    radius_nm: float,
    eps_particle: np.ndarray | complex,
    eps_medium: np.ndarray | complex,
) -> np.ndarray:
    """Compute electrostatic polarizability alpha = 4*pi*a^3*(ep-em)/(ep+2*em)."""
    a = float(radius_nm)
    ep = np.asarray(eps_particle, dtype=complex)
    em = np.asarray(eps_medium, dtype=complex)
    return 4.0 * np.pi * a**3 * (ep - em) / (ep + 2.0 * em)


def rayleigh_cross_sections(
    wavelength_nm: np.ndarray | float,
    radius_nm: float,
    eps_particle: np.ndarray | complex,
    eps_medium: np.ndarray | complex,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Return (C_ext, C_sca, C_abs) using Rayleigh-limit closed forms."""
    wavelength = np.asarray(wavelength_nm, dtype=float)
    em = np.asarray(eps_medium, dtype=complex)
    k = 2.0 * np.pi * np.sqrt(em) / wavelength

    alpha = rayleigh_polarizability(radius_nm, eps_particle, eps_medium)

    c_ext = k * np.imag(alpha)
    c_sca = (np.abs(k) ** 4) * np.abs(alpha) ** 2 / (6.0 * np.pi)
    c_abs = c_ext - c_sca
    return c_ext.real, c_sca.real, c_abs.real
