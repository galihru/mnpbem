# MNPBEM Python Modules

[![Publish mnpbem](https://github.com/galihru/mnpbem/actions/workflows/mnpbem.yml/badge.svg)](https://github.com/galihru/mnpbem/actions/workflows/mnpbem.yml)
[![PyPI status mnpbem](https://img.shields.io/badge/PyPI-pending%20first%20release-orange)](https://github.com/galihru/mnpbem/actions/workflows/mnpbem.yml)
[![PyPI mnpbem-base](https://img.shields.io/pypi/v/mnpbem-base.svg)](https://pypi.org/project/mnpbem-base/)
[![PyPI mnpbem-material](https://img.shields.io/pypi/v/mnpbem-material.svg)](https://pypi.org/project/mnpbem-material/)
[![PyPI mnpbem-misc](https://img.shields.io/pypi/v/mnpbem-misc.svg)](https://pypi.org/project/mnpbem-misc/)

This repository hosts modular Python packages for scientific boundary-element workflows inspired by the MNPBEM ecosystem.

## Installation

Install published modules from PyPI:

```bash
pip install mnpbem-base mnpbem-material mnpbem-misc
```

The umbrella package `mnpbem` is currently pending first PyPI publication.
Track publication status in the workflow:
- https://github.com/galihru/mnpbem/actions/workflows/mnpbem.yml

Temporary installation for the umbrella package from repository source:

```bash
pip install git+https://github.com/galihru/mnpbem.git#subdirectory=mnpbem
```

## Package Layout

- [`mnpbem`](https://github.com/galihru/mnpbem/tree/main/mnpbem): umbrella package that installs all submodules.
- [`mnpbem-material`](https://pypi.org/project/mnpbem-material/): dielectric-function models and optical tables.
- [`mnpbem-misc`](https://pypi.org/project/mnpbem-misc/): shared linear algebra and unit conversion utilities.
- [`mnpbem-base`](https://pypi.org/project/mnpbem-base/): factory/registry primitives.
- [`mnpbem-demo`](https://pypi.org/project/mnpbem-demo/), [`mnpbem-demo-mnpbem`](https://pypi.org/project/mnpbem-demo-mnpbem/), [`mnpbem-help`](https://pypi.org/project/mnpbem-help/), [`mnpbem-mex`](https://pypi.org/project/mnpbem-mex/), [`mnpbem-particles`](https://pypi.org/project/mnpbem-particles/), [`mnpbem-simulation`](https://pypi.org/project/mnpbem-simulation/).
- Pending first PyPI publication:
  - `mnpbem-bem`: https://github.com/galihru/mnpbem/actions/workflows/mnpbembem.yml
  - `mnpbem-greenfun`: https://github.com/galihru/mnpbem/actions/workflows/mnpbemgreenfun.yml
  - `mnpbem-mesh2d`: https://github.com/galihru/mnpbem/actions/workflows/mnpbemmesh2d.yml
  - `mnpbem-mie`: https://github.com/galihru/mnpbem/actions/workflows/mnpbemmie.yml

## Author

- GALIH RIDHO UTOMO
- g4lihru@students.unnes.ac.id
