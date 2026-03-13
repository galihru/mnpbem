from __future__ import annotations

import csv
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
for package_dir in ROOT.glob("mnpbem-*"):
    src_dir = package_dir / "src"
    if src_dir.is_dir():
        sys.path.insert(0, str(src_dir))

from mnpbem_material import EpsConst, EpsDrude  # noqa: E402
from mnpbem_mie import rayleigh_cross_sections  # noqa: E402


wavelengths = np.linspace(400.0, 700.0, 61)
eps_particle, _ = EpsDrude("Au")(wavelengths)
eps_medium, _ = EpsConst(1.33**2)(wavelengths)
c_ext, c_sca, c_abs = rayleigh_cross_sections(wavelengths, 25.0, eps_particle, eps_medium)

out_path = ROOT / "docs" / "example-data" / "python.csv"
out_path.parent.mkdir(parents=True, exist_ok=True)
with out_path.open("w", encoding="utf-8", newline="") as handle:
    writer = csv.writer(handle)
    writer.writerow(["wavelength_nm", "c_ext", "c_sca", "c_abs"])
    for wl, ext, sca, abs_ in zip(wavelengths, c_ext, c_sca, c_abs):
        writer.writerow([f"{wl:.6f}", f"{float(ext):.12g}", f"{float(sca):.12g}", f"{float(abs_):.12g}"])
