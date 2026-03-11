# mnpbem

`mnpbem` is the umbrella meta-package for the modular Python implementation of MNPBEM-inspired workflows.
Installing this package installs the complete set of scientific submodules needed for boundary-element plasmonic simulations.

## Scientific Context

The full pipeline is organized around coupled operators in the frequency domain:

```text
A(lambda) x(lambda) = b(lambda)
```

where `A` combines geometric operators, Green kernels, and material dispersion terms defined by the submodule ecosystem.

## Installation

```bash
pip install mnpbem
```

## Submodule Topology

| Submodule | Scientific Role | PyPI |
| --- | --- | --- |
| `mnpbem-base` | Registry and factory primitives for modular solver composition | https://pypi.org/project/mnpbem-base/ |
| `mnpbem-bem` | Core linear-response solver kernels | https://pypi.org/project/mnpbem-bem/ |
| `mnpbem-greenfun` | Green-function kernel implementations | https://pypi.org/project/mnpbem-greenfun/ |
| `mnpbem-material` | Dispersive dielectric models and optical tables | https://pypi.org/project/mnpbem-material/ |
| `mnpbem-mesh2d` | 2D triangular mesh geometry operators | https://pypi.org/project/mnpbem-mesh2d/ |
| `mnpbem-mie` | Small-particle Mie/Rayleigh approximations | https://pypi.org/project/mnpbem-mie/ |
| `mnpbem-misc` | Shared linear algebra and unit conversion utilities | https://pypi.org/project/mnpbem-misc/ |
| `mnpbem-particles` | Particle geometry representations | https://pypi.org/project/mnpbem-particles/ |
| `mnpbem-simulation` | Spectral simulation orchestration | https://pypi.org/project/mnpbem-simulation/ |
| `mnpbem-demo` | Deterministic demo and benchmark cases | https://pypi.org/project/mnpbem-demo/ |
| `mnpbem-demo-mnpbem` | Extended demo orchestration layer | https://pypi.org/project/mnpbem-demo-mnpbem/ |
| `mnpbem-help` | Documentation-facing helper interfaces | https://pypi.org/project/mnpbem-help/ |
| `mnpbem-mex` | Optional acceleration backend probing interface | https://pypi.org/project/mnpbem-mex/ |

## Example

Runnable example:

- `examples/basic_usage.py`

Run:

```bash
python examples/basic_usage.py
```

## Author

GALIH RIDHO UTOMO  
g4lihru@students.unnes.ac.id
