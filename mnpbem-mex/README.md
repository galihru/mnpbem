# mnpbem-mex

`mnpbem-mex` provides acceleration-backend discovery hooks for optional compiled modules.
Release metadata is generated from this README to keep technical notes synchronized with package artifacts.

## Scientific Context
Acceleration backends are used to reduce numerical runtime. A common indicator is speedup:

```text
S = \frac{T_{\mathrm{python}}}{T_{\mathrm{accelerated}}}
```

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
