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

![Equation](https://latex.codecogs.com/svg.image?%5Cdpi%7B150%7D%20%5Cvarepsilon%28%5Clambda%29%20%3D%20%5Cvarepsilon_0)

The wave number is:

![Equation](https://latex.codecogs.com/svg.image?%5Cdpi%7B150%7D%20k%28%5Clambda%29%20%3D%20%5Cfrac%7B2%5Cpi%7D%7B%5Clambda%7D%5Csqrt%7B%5Cvarepsilon%7D)

### 2. Drude Model
For free-electron metal response:

![Equation](https://latex.codecogs.com/svg.image?%5Cdpi%7B150%7D%20%5Cvarepsilon%28%5Comega%29%20%3D%20%5Cvarepsilon_%5Cinfty%20-%20%5Cfrac%7B%5Comega_p%5E2%7D%7B%5Comega%28%5Comega%20%2B%20i%5Cgamma%29%7D)

Energy-wavelength conversion used in the implementation:

![Equation](https://latex.codecogs.com/svg.image?%5Cdpi%7B150%7D%20%5Comega_%7B%5Cmathrm%7BeV%7D%7D%20%3D%20%5Cfrac%7BC_%7B%5Cmathrm%7BeV%5Ccdot%20nm%7D%7D%7D%7B%5Clambda_%7B%5Cmathrm%7Bnm%7D%7D%7D%2C%20%5Cqquad%20C_%7B%5Cmathrm%7BeV%5Ccdot%20nm%7D%7D%20%5Capprox%201239.841984)

### 3. Tabulated Material Model
Given tabulated optical constants (energy, refractive index, extinction), the dielectric function is:

![Equation](https://latex.codecogs.com/svg.image?%5Cdpi%7B150%7D%20%5Cvarepsilon%20%3D%20%28n%20%2B%20i%20k%29%5E2)

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
