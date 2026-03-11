# mnpbem

[![Publish mnpbem](https://github.com/galihru/mnpbem/actions/workflows/mnpbem.yml/badge.svg)](https://github.com/galihru/mnpbem/actions/workflows/mnpbem.yml)
[![PyPI status](https://img.shields.io/badge/PyPI-pending%20first%20release-orange)](https://github.com/galihru/mnpbem/actions/workflows/mnpbem.yml)

`mnpbem` is the umbrella meta-package for the scientific Python conversion of the MNPBEM ecosystem.
Installing `mnpbem` installs all submodules required for boundary-element plasmonics workflows.

## Scientific Overview
The package family targets frequency-domain formulations of nanoplasmonic problems, typically represented as:

$$
\mathbf{A}(\lambda)\,\mathbf{x}(\lambda)=\mathbf{b}(\lambda)
$$

where geometry, material dispersion, kernels, and solvers are decomposed into dedicated submodules.

## Installation
PyPI publication for `mnpbem` is pending first release.

Track publication status:
- https://github.com/galihru/mnpbem/actions/workflows/mnpbem.yml

Install from repository source:

```bash
pip install git+https://github.com/galihru/mnpbem.git#subdirectory=mnpbem
```

## Submodule Map
| Submodule | Scientific role | PyPI |
| --- | --- | --- |
| `mnpbem-base` | Registry and factory for task-dependent solver selection | https://pypi.org/project/mnpbem-base/ |
| `mnpbem-bem` | Linear response solver kernels | Pending publication: https://github.com/galihru/mnpbem/actions/workflows/mnpbembem.yml |
| `mnpbem-demo` | Reproducible spectral-grid demos | https://pypi.org/project/mnpbem-demo/ |
| `mnpbem-demo-mnpbem` | Extended demo orchestration layer | https://pypi.org/project/mnpbem-demo-mnpbem/ |
| `mnpbem-greenfun` | Green-function kernels for wave propagation | Pending publication: https://github.com/galihru/mnpbem/actions/workflows/mnpbemgreenfun.yml |
| `mnpbem-help` | Documentation and reference module index | https://pypi.org/project/mnpbem-help/ |
| `mnpbem-material` | Dispersive dielectric models and tabulated optical data | https://pypi.org/project/mnpbem-material/ |
| `mnpbem-mesh2d` | Triangle geometry operators for 2D meshes | Pending publication: https://github.com/galihru/mnpbem/actions/workflows/mnpbemmesh2d.yml |
| `mnpbem-mex` | Optional acceleration backend probing interface | https://pypi.org/project/mnpbem-mex/ |
| `mnpbem-mie` | Rayleigh/Mie small-particle scattering approximations | Pending publication: https://github.com/galihru/mnpbem/actions/workflows/mnpbemmie.yml |
| `mnpbem-misc` | Core linear algebra and unit conversion utilities | https://pypi.org/project/mnpbem-misc/ |
| `mnpbem-particles` | Particle geometry primitives | https://pypi.org/project/mnpbem-particles/ |
| `mnpbem-simulation` | Spectrum orchestration over wavelength grids | https://pypi.org/project/mnpbem-simulation/ |

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
