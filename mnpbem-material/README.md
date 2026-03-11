# mnpbem-material

`mnpbem-material` implements dielectric-function models used in plasmonic electrodynamics.
The module provides analytical material models and tabulated optical constants for metals such as Au, Ag, and Al.

## Features
- Constant dielectric model for homogeneous media.
- Drude dielectric model for free-electron metals.
- Tabulated `(E, n, k)` optical constants with wavelength-domain interpolation.
- Ready-to-use datasets for common plasmonic materials.

## Implemented Formulations

### 1. Constant Dielectric Function
For wavelength-independent permittivity:

$$
\varepsilon(\lambda) = \varepsilon_0
$$

The wave number is:

$$
k(\lambda) = \frac{2\pi}{\lambda}\sqrt{\varepsilon}
$$

### 2. Drude Model
For free-electron metal response:

$$
\varepsilon(\omega) =
\varepsilon_\infty -
\frac{\omega_p^2}{\omega(\omega + i\gamma)}
$$

Energy-wavelength conversion used in the implementation:

$$
\omega_{\mathrm{eV}} = \frac{C_{\mathrm{eV\cdot nm}}}{\lambda_{\mathrm{nm}}},
\qquad C_{\mathrm{eV\cdot nm}} \approx 1239.841984
$$

### 3. Tabulated Material Model
Given tabulated optical constants (energy, refractive index, extinction), the dielectric function is:

$$
\varepsilon = (n + i k)^2
$$

## Implementation
- Core implementation: `src/mnpbem_material/models.py`
- Material datasets: `src/mnpbem_material/data/*.dat`

## Dependencies
- `numpy>=1.24`

## Installation
```bash
pip install mnpbem-material
```

## Example
Runnable example:
- `examples/basic_usage.py`

Run:
```bash
python examples/basic_usage.py
```

## Author
- GALIH RIDHO UTOMO
- g4lihru@students.unnes.ac.id
