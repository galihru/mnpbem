# mnpbem-base

`mnpbem-base` provides registry and factory primitives for selecting solver classes from option constraints.
The release notes are generated directly from this scientific README for traceable package documentation.

## Implemented Formulation
Given a requirement set for a candidate class, the selection score is:

![Equation](https://latex.codecogs.com/svg.image?%5Cdpi%7B150%7D%20%5Chat%7Bc%7D%3D%5Carg%5Cmax_c%5Csum_j%5Cmathbf%7B1%7D%5B%5Ctext%7Bneed%7D_%7Bc%2Cj%7D%5C%20%5Ctext%7Bis%20satisfied%7D%5D)

This mirrors rule-based class dispatch used in MNPBEM-style solver construction.

## Implementation
- Registry logic: `src/mnpbem_base/registry.py`
- Factory entry points: `src/mnpbem_base/factory.py`

## Dependencies
- `numpy>=1.24`

## Installation
```bash
pip install mnpbem-base
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
