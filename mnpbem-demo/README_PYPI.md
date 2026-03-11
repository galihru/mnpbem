# mnpbem-demo

`mnpbem-demo` provides reproducible spectral grids for controlled numerical experiments.

## Implemented Formulation
For start wavelength `lambda_start`, stop wavelength `lambda_stop`, and sample count `N`:

![Equation](https://latex.codecogs.com/svg.image?%5Cdpi%7B150%7D%20%5Clambda_i%20%3D%20%5Clambda_0%20%2B%20i%5C%2C%5CDelta%5Clambda%2C%5Cqquad%20%5CDelta%5Clambda%3D%5Cfrac%7B%5Clambda_1-%5Clambda_0%7D%7BN-1%7D)

## Implementation
- Demo grid generator: `src/mnpbem_demo/cases.py`

## Dependencies
- `numpy>=1.24`

## Installation
```bash
pip install mnpbem-demo
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
