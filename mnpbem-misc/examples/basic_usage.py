"""Basic usage examples for mnpbem-misc."""

from __future__ import annotations

import numpy as np

from mnpbem_misc import ev_to_nm, inner, matcross, vecnorm, vecnormalize


def main() -> None:
    energies_ev = np.array([1.5, 2.0, 2.5], dtype=float)
    wavelengths_nm = ev_to_nm(energies_ev)
    print("wavelengths (nm):", wavelengths_nm)

    vectors = np.array([[1.0, 2.0, 2.0], [2.0, 0.0, 1.0]], dtype=float)
    print("vector norms:", vecnorm(vectors))
    print("normalized vectors:", vecnormalize(vectors))

    a = np.array([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0]])
    b = np.array([[0.0, 1.0, 0.0], [1.0, 0.0, 1.0]])
    print("cross products:", matcross(a, b))

    nvec = np.array([[1.0, 0.0, 0.0], [0.5, 0.5, 0.0]])
    val = np.array([[2.0, 3.0, 4.0], [1.0, 1.0, 1.0]])
    print("inner products:", inner(nvec, val))


if __name__ == "__main__":
    main()
