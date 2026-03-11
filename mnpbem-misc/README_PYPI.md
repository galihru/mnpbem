# mnpbem-misc

`mnpbem-misc` provides shared numerical utilities used across MNPBEM-Python submodules.

## Features
- Physical unit conversions between photon energy and wavelength.
- Vector norms and normalization utilities with MATLAB-compatible behavior.
- Tensor-aware linear algebra helpers (`matmul`, `matcross`, `inner`, `outer`, `spdiag`).

## Mathematical Formulations
Photon energy-wavelength conversion:

![Equation](https://latex.codecogs.com/svg.image?%5Cdpi%7B150%7D%20%5Clambda_%7Bnm%7D%20%3D%20%5Cfrac%7BC_%7BeV%5Ccdot%20nm%7D%7D%7BE_%7BeV%7D%7D%2C%5Cquad%20C_%7BeV%5Ccdot%20nm%7D%3D1239.841984)

Euclidean vector norm:

![Equation](https://latex.codecogs.com/svg.image?%5Cdpi%7B150%7D%20%5C%7Cv%5C%7C_2%20%3D%20%5Csqrt%7B%5Csum_i%20%7Cv_i%7C%5E2%7D)

Normalization:

![Equation](https://latex.codecogs.com/svg.image?%5Cdpi%7B150%7D%20%5Ctilde%7Bv%7D%20%3D%20%5Cfrac%7Bv%7D%7B%5C%7Cv_%7Bref%7D%5C%7C_2%7D)

## Implementation
- Unit conversion utilities: `src/mnpbem_misc/units.py`
- Vector operations: `src/mnpbem_misc/vector.py`
- Linear algebra helpers: `src/mnpbem_misc/linalg.py`

## Dependencies
- `numpy>=1.24`

## Installation
```bash
pip install mnpbem-misc
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
