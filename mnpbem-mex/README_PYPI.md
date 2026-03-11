# mnpbem-mex

`mnpbem-mex` provides acceleration-backend discovery hooks for optional compiled modules.
Release metadata is generated from this README to keep technical notes synchronized with package artifacts.

## Scientific Context
Acceleration backends are used to reduce numerical runtime. A common indicator is speedup:

![Equation](https://latex.codecogs.com/svg.image?%5Cdpi%7B150%7D%20S%20%3D%20%5Cfrac%7BT_%7B%5Cmathrm%7Bpython%7D%7D%7D%7BT_%7B%5Cmathrm%7Baccelerated%7D%7D%7D)

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
