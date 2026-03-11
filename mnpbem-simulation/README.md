# mnpbem-simulation

[![PyPI version](https://img.shields.io/pypi/v/mnpbem-simulation.svg)](https://pypi.org/project/mnpbem-simulation/)
[![Python versions](https://img.shields.io/pypi/pyversions/mnpbem-simulation.svg)](https://pypi.org/project/mnpbem-simulation/)
[![Publish mnpbem-simulation](https://github.com/galihru/mnpbem/actions/workflows/mnpbemsimulation.yml/badge.svg)](https://github.com/galihru/mnpbem/actions/workflows/mnpbemsimulation.yml)

`mnpbem-simulation` orchestrates vectorized spectrum evaluation over wavelength grids.

## Implemented Formulation
For sampled wavelengths $\lambda_i$, the response is evaluated as:

$$
S_i = f(\lambda_i)
$$

with strict shape-consistency between input grid and output spectrum.

## Implementation
- Spectrum sampling: `src/mnpbem_simulation/spectra.py`

## Dependencies
- `numpy>=1.24`

## Installation
```bash
pip install mnpbem-simulation
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
