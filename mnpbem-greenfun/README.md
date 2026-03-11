# mnpbem-greenfun

[![PyPI version](https://img.shields.io/pypi/v/mnpbem-greenfun.svg)](https://pypi.org/project/mnpbem-greenfun/)
[![Python versions](https://img.shields.io/pypi/pyversions/mnpbem-greenfun.svg)](https://pypi.org/project/mnpbem-greenfun/)
[![Publish mnpbem-greenfun](https://github.com/galihru/mnpbem/actions/workflows/mnpbemgreenfun.yml/badge.svg)](https://github.com/galihru/mnpbem/actions/workflows/mnpbemgreenfun.yml)

`mnpbem-greenfun` provides baseline free-space Green-function kernels for frequency-domain electrodynamics.

## Implemented Formulations
Scalar Green function:

$$
G(r,k)=\frac{e^{ikr}}{4\pi r}
$$

Dyadic-related prefactor:

$$
k^2 G(r,k)
$$

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
