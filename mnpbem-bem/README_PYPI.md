# mnpbem-bem

`mnpbem-bem` implements a minimal linear-response solve interface for complex frequency-domain systems.
Release metadata is generated from this README to keep publication notes aligned with the implemented solver model.

## Implemented Formulation
The solver computes:

![Equation](https://latex.codecogs.com/svg.image?%5Cdpi%7B150%7D%20%5Cmathbf%7BA%7D%5Cmathbf%7Bx%7D%3D%5Cmathbf%7Bb%7D)

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
