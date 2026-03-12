# MNPBEM — Multi-Language Plasmonics Simulation Ecosystem

[![License: GPL-3.0](https://img.shields.io/badge/license-GPL--3.0-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/galihru/mnpbem)](https://github.com/galihru/mnpbem/releases)
[![PyPI](https://img.shields.io/pypi/v/mnpbem.svg)](https://pypi.org/project/mnpbem/)
[![Crates.io](https://img.shields.io/crates/v/mnp-plasmon.svg)](https://crates.io/crates/mnp-plasmon)
[![npm](https://img.shields.io/npm/v/%40galihru%2Fmnp.svg)](https://www.npmjs.com/package/@galihru/mnp)
[![NuGet](https://img.shields.io/nuget/v/MnpPlasmon.svg)](https://www.nuget.org/packages/MnpPlasmon/)

Multi-language implementation of optical response calculations for metallic nanoparticles, based on the Drude dielectric model and the Rayleigh quasi-static approximation. Covers Python, JavaScript, C#, Rust, R, Julia, C/C++, and Conan.

## Contents

1. [Physical Model](#physical-model)
2. [Supported Platforms](#supported-platforms)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Package Index](#package-index)
6. [Release Pipeline](#release-pipeline)
7. [CI/CD and Security](#cicd-and-security)
8. [Author](#author)
9. [License](#license)

---

## Physical Model

### Drude Dielectric Function

The frequency-dependent permittivity of a dispersive metal is described by the Drude model:

$$\varepsilon(\omega) = \varepsilon_\infty - \frac{\omega_p^2}{\omega\,(\omega + i\gamma)}$$

| Symbol | Quantity | Unit |
|--------|----------|------|
| $\varepsilon_\infty$ | High-frequency dielectric constant | — |
| $\omega_p$ | Plasma frequency | eV |
| $\gamma$ | Damping (collision) rate | eV |
| $\omega$ | Angular frequency of incident light | eV |

### Rayleigh Polarizability

In the quasi-static (Rayleigh) limit, valid when the particle radius $a \ll \lambda$, the complex polarizability of a sphere is:

$$\alpha(\omega) = 4\pi a^3\,\frac{\varepsilon_p(\omega) - \varepsilon_m}{\varepsilon_p(\omega) + 2\,\varepsilon_m}$$

where $\varepsilon_p(\omega)$ is the particle permittivity and $\varepsilon_m$ is the real permittivity of the surrounding medium.

### Optical Cross-Sections

The three observable cross-sections follow directly from $\alpha(\omega)$:

$$\sigma_\text{ext} = \frac{4\pi}{k}\,\mathrm{Im}[\alpha(\omega)]$$

$$\sigma_\text{sca} = \frac{k^4}{6\pi}\,|\alpha(\omega)|^2$$

$$\sigma_\text{abs} = \sigma_\text{ext} - \sigma_\text{sca}$$

where $k = 2\pi n_m/\lambda$ is the wave vector magnitude in the medium.

### Built-in Material Parameters

| Material | $\omega_p$ (eV) | $\gamma$ (eV) | $\varepsilon_\infty$ |
|----------|----------------|---------------|----------------------|
| Au (Gold) | 3.106 | 0.0132 | 8.90 |
| Ag (Silver) | 3.810 | 0.0048 | 3.91 |
| Al (Aluminum) | 14.83 | 0.0980 | 1.24 |

---

## Supported Platforms

| Language | Package | Registry | Version |
|----------|---------|----------|---------|
| Python | `mnpbem`, `mnp-plasmon` | PyPI | [![PyPI](https://img.shields.io/pypi/v/mnpbem.svg)](https://pypi.org/project/mnpbem/) |
| JavaScript | `@galihru/mnp` | npm | [![npm](https://img.shields.io/npm/v/%40galihru%2Fmnp.svg)](https://www.npmjs.com/package/@galihru/mnp) |
| C# / .NET | `MnpPlasmon` | NuGet | [![NuGet](https://img.shields.io/nuget/v/MnpPlasmon.svg)](https://www.nuget.org/packages/MnpPlasmon/) |
| Rust | `mnp-plasmon` | Crates.io | [![Crates.io](https://img.shields.io/crates/v/mnp-plasmon.svg)](https://crates.io/crates/mnp-plasmon) |
| R | `mnpPlasmonR` | CRAN | [![CRAN](https://www.r-pkg.org/badges/version/mnpPlasmonR)](https://cran.r-project.org/package=mnpPlasmonR) |
| Julia | `MnpPlasmon.jl` | Julia General Registry | [![Julia](https://img.shields.io/badge/julia-MnpPlasmon.jl-9558B2.svg)](https://github.com/galihru/mnpbem/tree/main/julia-mnp-plasmon) |
| C / C++ | `mnp-plasmon` | vcpkg | — |
| C / C++ | `mnp-plasmon` | Conan Center | [![Conan](https://img.shields.io/badge/conan-mnp--plasmon-blue.svg)](https://conan.io/center) |

---

## Installation

**Python**

```bash
pip install mnpbem
# or individual submodules
pip install mnpbem-material mnpbem-mie
```

**JavaScript / TypeScript**

```bash
npm install @galihru/mnp @galihru/mnp-material @galihru/mnp-mie
```

**C# / .NET**

```bash
dotnet add package MnpPlasmon
```

**Rust**

```toml
[dependencies]
mnp-plasmon = "0.1"
```

**R**

```r
install.packages("mnpPlasmonR")
```

**Julia**

```julia
using Pkg
Pkg.add("MnpPlasmon")
```

**C / C++ via Conan**

```bash
conan install --requires="mnp-plasmon/0.1.0" --build=missing
```

---

## Usage

All implementations expose a `sphere_response` function that computes extinction, scattering, and absorption cross-sections for a spherical nanoparticle under the Rayleigh approximation.

**Python**

```python
from mnp_plasmon import sphere_response

result = sphere_response(wavelength_nm=550.0, radius_nm=25.0, material="Au")
print(result.c_ext, result.c_sca, result.c_abs)
```

**JavaScript**

```javascript
import { MnpPlasmon } from '@galihru/mnp';

const result = MnpPlasmon.sphereResponse({ wavelength: 550, radius: 25, material: 'Au' });
console.log(result.cExt, result.cSca, result.cAbs);
```

**C# (.NET)**

```csharp
using MnpPlasmon;

var r = MnpPlasmon.SphereResponse(wavelengthNm: 550.0, radiusNm: 25.0, material: "Au");
Console.WriteLine($"{r.CExt:F2} nm²");
```

**Rust**

```rust
use mnp_plasmon::sphere_response;

let r = sphere_response(550.0, 25.0, "Au", 1.0)?;
println!("{:.2} nm²", r.c_ext);
```

**R**

```r
library(mnpPlasmonR)

r <- sphere_response(wavelength_nm = 550, radius_nm = 25, material = "Au")
cat(r$c_ext, "nm²\n")
```

**C**

```c
#include "mnp_plasmon.h"

sphere_result_t r = mnp_sphere_response(550.0, 25.0, "Au", 1.0);
printf("%.2f nm²\n", r.c_ext);
```

**Julia**

```julia
using MnpPlasmon

r = sphere_response(550.0, 25.0, "Au")
println(r.c_ext, " nm²")
```

---

## Package Index

### Python — MNPBEM Ecosystem

| Package | Role | Link |
|---------|------|------|
| `mnpbem` | Umbrella — installs all core submodules | [PyPI](https://pypi.org/project/mnpbem/) |
| `mnpbem-base` | Registry and factory infrastructure for solver workflows | [PyPI](https://pypi.org/project/mnpbem-base/) |
| `mnpbem-bem` | Linear-response BEM solver kernels | [PyPI](https://pypi.org/project/mnpbem-bem/) |
| `mnpbem-greenfun` | Green-function kernels for wave propagation | [PyPI](https://pypi.org/project/mnpbem-greenfun/) |
| `mnpbem-material` | Dispersive dielectric models and tabulated optical data | [PyPI](https://pypi.org/project/mnpbem-material/) |
| `mnpbem-mesh2d` | Triangle-based geometry operators for 2D meshes | [PyPI](https://pypi.org/project/mnpbem-mesh2d/) |
| `mnpbem-mie` | Rayleigh and Mie approximation routines | [PyPI](https://pypi.org/project/mnpbem-mie/) |
| `mnpbem-misc` | Shared numerical utilities and unit conversion | [PyPI](https://pypi.org/project/mnpbem-misc/) |
| `mnpbem-particles` | Geometric primitives for nanoparticles | [PyPI](https://pypi.org/project/mnpbem-particles/) |
| `mnpbem-simulation` | Spectrum orchestration over wavelength grids | [PyPI](https://pypi.org/project/mnpbem-simulation/) |

### JavaScript — npm

| Package | Role |
|---------|------|
| [`@galihru/mnp`](https://www.npmjs.com/package/@galihru/mnp) | Core plasmon calculator |
| [`@galihru/mnp-material`](https://www.npmjs.com/package/@galihru/mnp-material) | Material parameter definitions |
| [`@galihru/mnp-mie`](https://www.npmjs.com/package/@galihru/mnp-mie) | Mie and Rayleigh approximations |

---

## Release Pipeline

A single git tag triggers simultaneous publication to all registries:

```
GitHub Release (vX.Y.Z)
    |
    +-- Publish Python      --> PyPI
    +-- Publish JavaScript  --> npm
    +-- Publish C# (.NET)   --> NuGet
    +-- Publish Rust        --> Crates.io
    +-- R CMD check         --> CRAN (manual upload to cran.r-project.org/submit.html)
    +-- Julia tests         --> Julia General Registry (trigger via @JuliaRegistrator)
    +-- Conan recipe check  --> Conan Center (manual PR to conan-center-index)
    +-- Publish C / C++     --> vcpkg
```

To create a release:

```bash
git tag v1.0.0
git push origin v1.0.0
```

See [`.github/workflows/release-master.yml`](.github/workflows/release-master.yml) for the full workflow definition.

---

## CI/CD and Security

All workflows run on GitHub Actions.

- Trusted publishing (OIDC) for PyPI — no long-lived token stored in secrets.
- `R CMD check --as-cran` runs before any CRAN upload.
- Build matrix covers Linux, macOS, and Windows for C/C++ targets.
- GPL-3.0 license verified across all packages.

**Required secrets for maintainers:**

| Secret | Purpose |
|--------|---------|
| `PYPI_API_TOKEN` | PyPI upload token |
| `NPMJS_API_TOKEN` | npm publish token |
| `NUGET_API_KEY` | NuGet.org API key |
| `CARGO_TOKEN` | Crates.io API key (mapped to `CARGO_REGISTRY_TOKEN` in workflow) |
| `GH_TOKEN` | GitHub Packages and release automation |

---

## Author

Galih Ridho Utomo  
g4lihru@students.unnes.ac.id  
[github.com/galihru](https://github.com/galihru) — [npm](https://www.npmjs.com/~galihru) — [PyPI](https://pypi.org/user/galihru/) — [NuGet](https://www.nuget.org/profiles/galihru) — [Crates.io](https://crates.io/users/galihru)

---

## License

GPL-3.0-only. See [LICENSE](LICENSE) for the full text.

All language implementations (Python, JavaScript, C#, Rust, R, C, C++) are subject to the same license.
