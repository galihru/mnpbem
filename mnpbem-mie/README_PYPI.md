# mnpbem-mie

`mnpbem-mie` provides Rayleigh-limit scattering formulas for small spherical particles.

## Implemented Formulations
Polarizability:

![Equation](https://latex.codecogs.com/svg.image?%5Cdpi%7B150%7D%20%5Calpha%20%3D%204%5Cpi%20a%5E3%5Cfrac%7B%5Cvarepsilon_p-%5Cvarepsilon_m%7D%7B%5Cvarepsilon_p%2B2%5Cvarepsilon_m%7D)

Wave number in medium:

![Equation](https://latex.codecogs.com/svg.image?%5Cdpi%7B150%7D%20k%20%3D%20%5Cfrac%7B2%5Cpi%7D%7B%5Clambda%7D%5Csqrt%7B%5Cvarepsilon_m%7D)

Cross sections:

![Equation](https://latex.codecogs.com/svg.image?%5Cdpi%7B150%7D%20C_%7B%5Cmathrm%7Bext%7D%7D%20%3D%20k%5C%2C%5Cmathrm%7BIm%7D%28%5Calpha%29%2C%5Cquad%20C_%7B%5Cmathrm%7Bsca%7D%7D%20%3D%20%5Cfrac%7B%7Ck%7C%5E4%7D%7B6%5Cpi%7D%7C%5Calpha%7C%5E2%2C%5Cquad%20C_%7B%5Cmathrm%7Babs%7D%7D%20%3D%20C_%7B%5Cmathrm%7Bext%7D%7D-C_%7B%5Cmathrm%7Bsca%7D%7D)

## Implementation
- Rayleigh model: `src/mnpbem_mie/rayleigh.py`

## Dependencies
- `numpy>=1.24`

## Installation
```bash
pip install mnpbem-mie
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
