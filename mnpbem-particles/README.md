# mnpbem-particles

[![PyPI version](https://img.shields.io/pypi/v/mnpbem-particles.svg)](https://pypi.org/project/mnpbem-particles/)
[![Python versions](https://img.shields.io/pypi/pyversions/mnpbem-particles.svg)](https://pypi.org/project/mnpbem-particles/)
[![Publish mnpbem-particles](https://github.com/galihru/mnpbem/actions/workflows/mnpbemparticles.yml/badge.svg)](https://github.com/galihru/mnpbem/actions/workflows/mnpbemparticles.yml)

`mnpbem-particles` provides geometric particle primitives for nanostructure models.

## Implemented Formulation
Sphere volume:

$$
V = \frac{4}{3}\pi r^3
$$

## Implementation
- Particle primitives: `src/mnpbem_particles/primitives.py`

## Dependencies
- `numpy>=1.24`

## Installation
```bash
pip install mnpbem-particles
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
