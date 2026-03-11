# mnpbem-greenfun

`mnpbem-greenfun` provides baseline free-space Green-function kernels for frequency-domain electrodynamics.

## Implemented Formulations
Scalar Green function:

![Equation](https://latex.codecogs.com/svg.image?%5Cdpi%7B150%7D%20G%28r%2Ck%29%3D%5Cfrac%7Be%5E%7Bikr%7D%7D%7B4%5Cpi%20r%7D)

Dyadic-related prefactor:

```text
k^2 G(r,k)
```

## Implementation
- Kernel functions: `src/mnpbem_greenfun/kernels.py`

## Dependencies
- `numpy>=1.24`

## Installation
```bash
pip install mnpbem-greenfun
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
