# mnpbem-greenfun

[![Publish mnpbem-greenfun](https://github.com/galihru/mnpbem/actions/workflows/mnpbemgreenfun.yml/badge.svg)](https://github.com/galihru/mnpbem/actions/workflows/mnpbemgreenfun.yml)
[![PyPI status](https://img.shields.io/badge/PyPI-pending%20first%20release-orange)](https://github.com/galihru/mnpbem/actions/workflows/mnpbemgreenfun.yml)

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
PyPI publication for `mnpbem-greenfun` is pending first release.

Track publication status:
- https://github.com/galihru/mnpbem/actions/workflows/mnpbemgreenfun.yml

Install from repository source:

```bash
pip install git+https://github.com/galihru/mnpbem.git#subdirectory=mnpbem-greenfun
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
