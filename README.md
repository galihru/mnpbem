# MNPBEM Python Modules

[![PyPI version](https://img.shields.io/pypi/v/mnpbem.svg?cacheSeconds=60)](https://pypi.org/project/mnpbem/)
[![Python versions](https://img.shields.io/pypi/pyversions/mnpbem.svg)](https://pypi.org/project/mnpbem/)
[![Publish mnpbem](https://github.com/galihru/mnpbem/actions/workflows/mnpbem.yml/badge.svg?branch=main)](https://github.com/galihru/mnpbem/actions/workflows/mnpbem.yml)

This repository hosts a modular Python implementation of scientific workflows inspired by the MNPBEM ecosystem.
The architecture separates material models, geometry, kernels, and solvers into independently publishable packages while preserving a coherent end-to-end pipeline.

## Scientific Scope

The package family targets frequency-domain boundary-element formulations, commonly represented as:

```text
A(lambda) x(lambda) = b(lambda)
```

For dispersive media, the optical response is modeled through a complex dielectric function:

```text
epsilon(omega) = epsilon_inf - omega_p^2 / (omega (omega + i gamma))
```

This decomposition supports reproducible simulation chains where each module contributes a clearly defined mathematical operator.

## Installation

Install the umbrella package:

```bash
pip install mnpbem
```

Install a specific module:

```bash
pip install mnpbem-material
```

## Published Modules

| Module | Scientific Role | PyPI |
| --- | --- | --- |
| `mnpbem` | Umbrella package that installs all core submodules | https://pypi.org/project/mnpbem/ |
| `mnpbem-base` | Registry/factory infrastructure for solver workflows | https://pypi.org/project/mnpbem-base/ |
| `mnpbem-bem` | Linear-response BEM solver kernels | https://pypi.org/project/mnpbem-bem/ |
| `mnpbem-greenfun` | Green-function kernels for wave propagation | https://pypi.org/project/mnpbem-greenfun/ |
| `mnpbem-material` | Dispersive dielectric models and tabulated optical data | https://pypi.org/project/mnpbem-material/ |
| `mnpbem-mesh2d` | Triangle-based geometry operators for 2D meshes | https://pypi.org/project/mnpbem-mesh2d/ |
| `mnpbem-mie` | Small-particle Rayleigh/Mie approximations | https://pypi.org/project/mnpbem-mie/ |
| `mnpbem-misc` | Shared numerical utilities and unit conversion | https://pypi.org/project/mnpbem-misc/ |
| `mnpbem-particles` | Particle-level geometric primitives | https://pypi.org/project/mnpbem-particles/ |
| `mnpbem-simulation` | Spectrum orchestration over wavelength grids | https://pypi.org/project/mnpbem-simulation/ |
| `mnpbem-demo` | Reproducible benchmark/demo cases | https://pypi.org/project/mnpbem-demo/ |
| `mnpbem-demo-mnpbem` | Extended orchestration for demo pipelines | https://pypi.org/project/mnpbem-demo-mnpbem/ |
| `mnpbem-help` | Auxiliary references and helper interfaces | https://pypi.org/project/mnpbem-help/ |
| `mnpbem-mex` | Optional acceleration backend probing layer | https://pypi.org/project/mnpbem-mex/ |

## Author

GALIH RIDHO UTOMO  
g4lihru@students.unnes.ac.id
