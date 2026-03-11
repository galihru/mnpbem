# mnpbem-material

`mnpbem-material` implements dielectric function models commonly used in plasmonic simulations.
The module provides simple analytical models and tabulated optical data for metallic materials such as Au, Ag, and Al.

---

# Implemented Formulations

## 1. Constant Dielectric Function

The simplest dielectric model assumes a wavelength-independent dielectric constant.

$$
[
\varepsilon(\lambda) = \varepsilon_0
]
$$

The corresponding wave number is

$$
[
k(\lambda) = \frac{2\pi}{\lambda}\sqrt{\varepsilon}
]
$$

where

$$v* ( \varepsilon_0 )$$ : constant dielectric permittivity
$$v* ( \lambda )$$ : wavelength

---

## 2. Drude Model

The Drude model describes the optical response of free-electron metals.

$$
[
\varepsilon(\omega) =
\varepsilon_\infty -
\frac{\omega_p^2}{\omega(\omega + i\gamma)}
]
$$

where

$$* ( \varepsilon_\infty )$$ : high-frequency dielectric constant
$$* ( \omega_p )$$ : plasma frequency
$$* ( \gamma )$$ : damping constant
$$* ( \omega )$$ : angular frequency

### Energy–Wavelength Conversion

The following relation is used to convert wavelength to photon energy:

$$
[
\omega_{eV} =
\frac{EV_TO_NM}{\lambda_{nm}}
]
$$

Material parameters for **Au**, **Ag**, and **Al** follow the formulation used in the MATLAB implementation:

```
Material/@epsdrude/init.m
```

from the original **MNPBEM toolbox**.

---

## 3. Tabulated Material Model

For tabulated optical data ( (E, n, k) ), the dielectric function is computed as

$$
[
\varepsilon = (n + i k)^2
]
$$

where

$$* ( n )$$ : refractive index
$$* ( k )v$$ : extinction coefficient

Interpolation is performed in the wavelength domain after converting tabulated energy values.

---

# Implementation

Core implementation:

```
src/mnpbem_material/models.py
```

Material datasets:

```
src/mnpbem_material/data/*.dat
```

---

# Dependencies

Runtime dependencies are installed automatically when the package is installed.

* numpy ≥ 1.24

---

# Example Usage

A runnable example is provided in:

```
examples/basic_usage.py
```

Run the example with:

```bash
python examples/basic_usage.py
```

---

# Author

GALIH RIDHO UTOMO
[g4lihru@students.unnes.ac.id](mailto:g4lihru@students.unnes.ac.id)
