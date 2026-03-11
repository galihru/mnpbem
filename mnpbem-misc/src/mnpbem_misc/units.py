"""Physical unit conversion utilities."""

from __future__ import annotations

import numpy as np

# Conversion factor from the MATLAB implementation: eV2nm = 1 / 8.0655477e-4.
EV_TO_NM: float = 1.0 / 8.0655477e-4
NM_TO_EV: float = 1.0 / EV_TO_NM


def ev_to_nm(energy_ev: np.ndarray | float) -> np.ndarray:
    """Convert photon energy in eV to vacuum wavelength in nm."""
    energy = np.asarray(energy_ev, dtype=float)
    return EV_TO_NM / energy


def nm_to_ev(wavelength_nm: np.ndarray | float) -> np.ndarray:
    """Convert vacuum wavelength in nm to photon energy in eV."""
    wavelength = np.asarray(wavelength_nm, dtype=float)
    return EV_TO_NM / wavelength
