from __future__ import annotations

import numpy as np

from mnpbem_material import EpsConst, EpsDrude, EpsTable


def main() -> None:
    wavelengths_nm = np.array([500.0, 600.0, 700.0])

    # Model 1: medium with constant dielectric constant eps = n^2 (water-like).
    eps_const = EpsConst(1.33**2)
    eps_c, k_c = eps_const(wavelengths_nm)
    print("EpsConst eps:", eps_c)
    print("EpsConst k:", k_c)

    # Model 2: Drude metal model.
    # Formula:
    #   eps(w) = eps_inf - wp^2 / (w * (w + i*gamma))
    drude_au = EpsDrude("Au")
    eps_d, k_d = drude_au(wavelengths_nm)
    print("EpsDrude(Au) eps:", eps_d)
    print("EpsDrude(Au) k:", k_d)

    # Model 3: tabulated optical constants (E, n, k).
    table = EpsTable.from_builtin("gold.dat")
    eps_t, k_t = table(wavelengths_nm)
    print("EpsTable(gold) eps:", eps_t)
    print("EpsTable(gold) k:", k_t)


if __name__ == "__main__":
    main()
