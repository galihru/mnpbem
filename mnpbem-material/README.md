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

where:
- $\varepsilon_0$ is the constant dielectric permittivity.
- $\lambda$ is the wavelength.

### 2. Drude Model
For free-electron metal response:

$$
\varepsilon(\omega) =
\varepsilon_\infty -
\frac{\omega_p^2}{\omega(\omega + i\gamma)}
$$

where:
- $\varepsilon_\infty$ is the high-frequency dielectric constant.
- $\omega_p$ is the plasma frequency.
- $\gamma$ is the damping constant.
- $\omega$ is the angular frequency.

Energy-wavelength conversion used in the implementation:

$$
\omega_{\mathrm{eV}} = \frac{C_{\mathrm{eV\cdot nm}}}{\lambda_{\mathrm{nm}}},
\qquad C_{\mathrm{eV\cdot nm}} \approx 1239.841984
$$

Material parameters for Au, Ag, and Al are aligned with the established MNPBEM Drude-style parameterization.

### 3. Tabulated Material Model
Given tabulated optical constants $(E, n, k)$, the dielectric function is:

$$
\varepsilon = (n + i k)^2
$$

Interpolation is performed in the wavelength domain after converting tabulated energy values.

## Implementation
- Core implementation: `src/mnpbem_material/models.py`
- Material datasets: `src/mnpbem_material/data/*.dat`

## Dependencies
Runtime dependencies are installed automatically by `pip`:
- `numpy>=1.24`

## Installation
```bash
pip install mnpbem-material
```

## Example Usage
Runnable example:
- `examples/basic_usage.py`

Run:
```bash
python examples/basic_usage.py
```

## Author
- GALIH RIDHO UTOMO
- g4lihru@students.unnes.ac.id
