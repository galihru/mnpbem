# mnpbem-bem

`mnpbem-bem` implements a minimal linear-response solve interface for complex frequency-domain systems.
Release metadata is generated from this README to keep publication notes aligned with the implemented solver model.

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
