# MNPBEM: Multi-Language Plasmonics Simulation Ecosystem

[![License: GPL-3.0](https://img.shields.io/badge/license-GPL--3.0-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/galihru/mnpbem)](https://github.com/galihru/mnpbem/releases)
[![PyPI](https://img.shields.io/pypi/v/mnpbem.svg)](https://pypi.org/project/mnpbem/)
[![npm](https://img.shields.io/npm/v/%40galihru%2Fmnp.svg)](https://www.npmjs.com/package/@galihru/mnp)
[![NuGet](https://img.shields.io/nuget/v/MnpPlasmon.svg)](https://www.nuget.org/packages/MnpPlasmon/)
[![Crates.io](https://img.shields.io/crates/v/mnp-plasmon.svg)](https://crates.io/crates/mnp-plasmon)

MNPBEM provides reproducible optical-response workflows for metallic nanoparticles, implemented across multiple programming languages.
The core physical model combines the Drude dielectric function with the Rayleigh quasi-static approximation for spherical particles.

## Scope

This repository contains two aligned tracks:

1. MNPBEM family (modular scientific workflow packages)
2. MnpPlasmon family (lightweight cross-language plasmonics calculator)

## Physical Model

### Drude dielectric function

For a dispersive metal:

$$
\varepsilon(\omega) = \varepsilon_\infty - \frac{\omega_p^2}{\omega(\omega + i\gamma)}
$$

Where:

- $\varepsilon_\infty$: high-frequency dielectric constant
- $\omega_p$: plasma frequency (eV)
- $\gamma$: damping rate (eV)
- $\omega$: angular frequency (eV)

### Rayleigh polarizability for a sphere

For $a \ll \lambda$:

$$
\alpha(\omega) = 4\pi a^3 \frac{\varepsilon_p(\omega) - \varepsilon_m}{\varepsilon_p(\omega) + 2\varepsilon_m}
$$

### Optical cross-sections

$$
\sigma_{ext} = \frac{4\pi}{k}\,\mathrm{Im}\left[\alpha(\omega)\right]
$$

$$
\sigma_{sca} = \frac{k^4}{6\pi}\,\left|\alpha(\omega)\right|^2
$$

$$
\sigma_{abs} = \sigma_{ext} - \sigma_{sca}
$$

with $k = \frac{2\pi n_m}{\lambda}$.

### Built-in material parameters

| Material | $\omega_p$ (eV) | $\gamma$ (eV) | $\varepsilon_\infty$ |
|---|---:|---:|---:|
| Au | 3.106 | 0.0132 | 8.90 |
| Ag | 3.810 | 0.0048 | 3.91 |
| Al | 14.83 | 0.0980 | 1.24 |

## Platform and Registry Status

| Language | Package | Registry | Status |
|---|---|---|---|
| Python | mnpbem, mnp-plasmon | PyPI | Published |
| JavaScript | @galihru/mnp, @galihru/mnp-material, @galihru/mnp-mie | npm | Published |
| C# / .NET | MnpPlasmon | NuGet | Published |
| Rust | mnp-plasmon | Crates.io | Published |
| R | mnpPlasmonR | CRAN | Submission workflow ready (manual CRAN upload) |
| Julia | MnpPlasmon | Julia General Registry | Registration in progress |
| C / C++ | mnp-plasmon | vcpkg | Published |
| C / C++ | mnp-plasmon | ConanCenter | Submission in review |

## Installation

### Python

```bash
pip install mnpbem
# optional modular install
pip install mnpbem-material mnpbem-mie
```

### JavaScript

```bash
npm install @galihru/mnp @galihru/mnp-material @galihru/mnp-mie
```

### C#

```bash
dotnet add package MnpPlasmon
```

### Rust

```toml
[dependencies]
mnp-plasmon = "0.1"
```

### R

```r
install.packages("mnpPlasmonR")
```

### Julia

```julia
using Pkg
Pkg.add("MnpPlasmon")
```

### Conan (C/C++)

```bash
conan install --requires="mnp-plasmon/0.1.0" --build=missing
```

## Minimal Usage

### Python

```python
from mnp_plasmon import sphere_response

r = sphere_response(wavelength_nm=550.0, radius_nm=25.0, material="Au")
print(r.c_ext, r.c_sca, r.c_abs)
```

### Julia

```julia
using MnpPlasmon

r = sphere_response(550.0, 25.0, "Au")
println(r.c_ext, " ", r.c_sca, " ", r.c_abs)
```

### C

```c
#include "mnp_plasmon.h"

sphere_response_t r = mnp_simulate_sphere_response("Au", 550.0, 25.0, 1.0);
```

## Release Pipeline

A release tag triggers the master orchestrator workflow for language-specific publish jobs.

```text
GitHub Release (vX.Y.Z)
  -> Python publish (PyPI)
  -> JavaScript publish (npm)
  -> C# publish (NuGet)
  -> Rust publish (Crates.io)
  -> R check and source artifact (manual CRAN upload)
  -> Julia test and registration trigger path
  -> Conan recipe validation path
  -> C/C++ publish path (vcpkg)
```

Release command:

```bash
git tag v1.0.0
git push origin v1.0.0
```

Workflow definition:

- [.github/workflows/release-master.yml](.github/workflows/release-master.yml)

## CI/CD and Security

All pipelines run on GitHub Actions.

- Trusted publishing (OIDC) is used where supported.
- R package path runs R CMD check before CRAN submission.
- Multi-platform build coverage is enforced for native targets.
- License policy is GPL-3.0-only across implementations.

Required repository secrets:

| Secret | Purpose |
|---|---|
| PYPI_API_TOKEN | PyPI publishing |
| NPMJS_API_TOKEN | npm publishing |
| NUGET_API_KEY | NuGet publishing |
| CARGO_TOKEN | Crates.io token mapped to CARGO_REGISTRY_TOKEN in workflow |
| GH_TOKEN | Release automation and related publishing tasks |

## Author

Galih Ridho Utomo  
g4lihru@students.unnes.ac.id  
[GitHub profile](https://github.com/galihru)

## License

GPL-3.0-only. See [LICENSE](LICENSE).
