# mnpbem-mex

[![PyPI version](https://img.shields.io/pypi/v/mnpbem-mex.svg)](https://pypi.org/project/mnpbem-mex/)
[![Python versions](https://img.shields.io/pypi/pyversions/mnpbem-mex.svg)](https://pypi.org/project/mnpbem-mex/)
[![Publish mnpbem-mex](https://github.com/galihru/mnpbem/actions/workflows/mnpbemmex.yml/badge.svg)](https://github.com/galihru/mnpbem/actions/workflows/mnpbemmex.yml)

`mnpbem-mex` provides acceleration-backend discovery hooks for optional compiled modules.

## Scientific Context
Acceleration backends are used to reduce numerical runtime. A common indicator is speedup:

$$
S = \frac{T_{\mathrm{python}}}{T_{\mathrm{accelerated}}}
$$

This package provides capability detection needed before using accelerated kernels.

## Implementation
- Backend probe: `src/mnpbem_mex/backend.py`

## Dependencies
- `numpy>=1.24`

## Installation
```bash
pip install mnpbem-mex
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
