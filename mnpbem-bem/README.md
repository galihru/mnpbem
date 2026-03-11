# mnpbem-bem

[![PyPI version](https://img.shields.io/pypi/v/mnpbem-bem.svg)](https://pypi.org/project/mnpbem-bem/)
[![Python versions](https://img.shields.io/pypi/pyversions/mnpbem-bem.svg)](https://pypi.org/project/mnpbem-bem/)
[![Publish mnpbem-bem](https://github.com/galihru/mnpbem/actions/workflows/mnpbembem.yml/badge.svg)](https://github.com/galihru/mnpbem/actions/workflows/mnpbembem.yml)

`mnpbem-bem` implements a minimal linear-response solve interface for complex frequency-domain systems.

## Implemented Formulation
The solver computes:

$$
\mathbf{A}\mathbf{x}=\mathbf{b}
$$

using complex-valued linear algebra (`numpy.linalg.solve`).

## Implementation
- Solver: `src/mnpbem_bem/solver.py`

## Dependencies
- `numpy>=1.24`

## Installation
```bash
pip install mnpbem-bem
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
