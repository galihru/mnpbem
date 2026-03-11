# mnpbem-mie

[![PyPI version](https://img.shields.io/pypi/v/mnpbem-mie.svg)](https://pypi.org/project/mnpbem-mie/)
[![Python versions](https://img.shields.io/pypi/pyversions/mnpbem-mie.svg)](https://pypi.org/project/mnpbem-mie/)
[![Publish mnpbem-mie](https://github.com/galihru/mnpbem/actions/workflows/mnpbemmie.yml/badge.svg)](https://github.com/galihru/mnpbem/actions/workflows/mnpbemmie.yml)

`mnpbem-mie` provides Rayleigh-limit scattering formulas for small spherical particles.

## Implemented Formulations
Polarizability:

$$
\alpha = 4\pi a^3\frac{\varepsilon_p-\varepsilon_m}{\varepsilon_p+2\varepsilon_m}
$$

Wave number in medium:

$$
k = \frac{2\pi}{\lambda}\sqrt{\varepsilon_m}
$$

Cross sections:

$$
C_{\mathrm{ext}} = k\,\mathrm{Im}(\alpha),\quad
C_{\mathrm{sca}} = \frac{|k|^4}{6\pi}|\alpha|^2,\quad
C_{\mathrm{abs}} = C_{\mathrm{ext}}-C_{\mathrm{sca}}
$$

## Implementation
- Rayleigh model: `src/mnpbem_mie/rayleigh.py`

## Dependencies
- `numpy>=1.24`

## Installation
```bash
pip install mnpbem-mie
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
