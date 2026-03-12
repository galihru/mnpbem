# MNPBEM & MnpPlasmon - Multi-Language Physics Simulation Ecosystem

[![License](https://img.shields.io/badge/license-GPL%203.0-blue.svg)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/galihru/mnpbem)](https://github.com/galihru/mnpbem)
[![Release](https://img.shields.io/github/v/release/galihru/mnpbem)](https://github.com/galihru/mnpbem/releases)

## 🌍 Multi-Language Support

| Language | Package | Status | Registry | Docs |
|----------|---------|--------|----------|------|
| **Python** | `mnpbem*` | [![PyPI version](https://img.shields.io/pypi/v/mnpbem.svg?cacheSeconds=60)](https://pypi.org/project/mnpbem/) | [PyPI](https://pypi.org/user/galihru/) | [Docs](https://mnpbem.readthedocs.io/) |
| **JavaScript** | `mnp*` | [![npm](https://img.shields.io/npm/v/mnp-plasmon.svg)](https://www.npmjs.com/~galihru?tab=packages) | [npm](https://www.npmjs.com/~galihru?tab=packages) | [JsDoc](https://github.com/galihru/mnpbem/tree/main/npm-packages) |
| **.NET/C#** | `MnpPlasmon` | [![NuGet](https://img.shields.io/nuget/v/MnpPlasmon.svg)](https://www.nuget.org/packages/MnpPlasmon/) | [NuGet](https://www.nuget.org/profiles/galihru) | [API](https://github.com/galihru/mnpbem/tree/main/csharp-mnp-plasmon) |
| **Rust** | `mnp-plasmon` | [![Crates.io](https://img.shields.io/crates/v/mnp-plasmon.svg)](https://crates.io/crates/mnp-plasmon) | [Crates.io](https://crates.io/users/galihru) | [docs.rs](https://docs.rs/mnp-plasmon/) |
| **C/C++** | `mnp-plasmon` | ![Status](https://img.shields.io/badge/status-stable-brightgreen) | [vcpkg](https://github.com/microsoft/vcpkg) | [API](https://github.com/galihru/mnpbem/tree/main/c-mnp-plasmon) |

![Example Image](https://raw.githubusercontent.com/galihru/mnpbem/c77a7cf0d745bb0fefb81f98bff0611a9d9afda9/mnpbem/example%20electric%20field%20demo.png)

## 📋 Overview

This repository hosts **multi-language implementations** of scientific workflows for optical response calculations of metallic nanoparticles. The ecosystem comprises:

1. **MNPBEM** (Python): Modular boundary-element method framework for electromagnetic simulations
2. **MnpPlasmon** (All languages): Light-weight Drude/Rayleigh optics calculator for nanoparticles

The architecture separates material models, geometry kernels, and solvers into independently publishable packages while preserving coherent end-to-end pipelines across all supported languages.

## 🔬 Physical Model

### Drude Dielectric Function

For dispersive metallic media, the optical response is modeled through a frequency-dependent dielectric function:

$$\varepsilon(\omega) = \varepsilon_\infty - \frac{\omega_p^2}{\omega(\omega + i\gamma)}$$

**where:**
- $\varepsilon_\infty$ = high-frequency dielectric constant
- $\omega_p$ = plasma frequency (eV)
- $\gamma$ = damping coefficient (eV)
- $\omega$ = angular frequency of incident light

### Rayleigh Approximation for Spherical Particles

For particles much smaller than the wavelength of light, the frequency-dependent polarizability is:

$$\alpha(\omega) = 4\pi a^3 \frac{\varepsilon_p(\omega) - \varepsilon_m}{\varepsilon_p(\omega) + 2\varepsilon_m}$$

**where:**
- $a$ = particle radius
- $\varepsilon_p(\omega)$ = particle dielectric function
- $\varepsilon_m$ = medium dielectric constant

### Optical Cross-Sections

**Extinction cross-section** (sum of absorption and scattering):
$$\sigma_{\text{ext}} = \frac{4\pi}{k} \text{Im}[\alpha(\omega)]$$

**Scattering cross-section**:
$$\sigma_{\text{sca}} = \frac{k^4}{6\pi} |\alpha(\omega)|^2$$

**Absorption cross-section**:
$$\sigma_{\text{abs}} = \sigma_{\text{ext}} - \sigma_{\text{sca}}$$

**where** $k = \frac{2\pi n_m}{\lambda}$ is the wave vector in the medium.

### Material Properties

Built-in support for noble metals:

| Material | $\omega_p$ (eV) | $\gamma$ (eV) | $\varepsilon_\infty$ | Applications |
|----------|-----------------|---------------|---------------------|--------------|
| **Au** (Gold) | 3.106 | 0.0132 | 8.90 | SERS, imaging, photothermal |
| **Ag** (Silver) | 3.810 | 0.0048 | 3.91 | Antibacterial, plasmonic devices |
| **Al** (Aluminum) | 14.83 | 0.098 | 1.24 | UV plasmonics, metamaterials |

### Scientific Scope (MNPBEM)

The MNPBEM package family targets frequency-domain boundary-element formulations, commonly represented as:

$$A(\lambda)\,x(\lambda)=b(\lambda)$$

This decomposition supports reproducible simulation chains where each module contributes a clearly defined mathematical operator.

## 🚀 Quick Start - Multi-Language Examples

### Python (MNPBEM & MnpPlasmon)

```bash
# Install core MNPBEM
pip install mnpbem

# Or install individual modules
pip install mnpbem-material mnpbem-mie
```

```python
from mnp_plasmon import sphere_response

# Calculate Au sphere optical response
response = sphere_response(
    wavelength_nm=550.0,
    radius_nm=25.0,
    material="Au",
    medium_refractive_index=1.0
)
print(f"σ_ext = {response.c_ext:.2f} nm²")
print(f"σ_sca = {response.c_sca:.2f} nm²")
print(f"σ_abs = {response.c_abs:.2f} nm²")
```

### JavaScript/TypeScript (npm)

```bash
npm install mnp-material mnp-mie mnp
```

```javascript
import { MnpPlasmon } from 'mnp';

const result = MnpPlasmon.sphereResponse({
  wavelength: 550,
  radius: 25,
  material: 'Au',
  mediumRefractiveIndex: 1.0
});

console.log(`σ_ext = ${result.cExt.toFixed(2)} nm²`);
```

### C# (.NET)

```bash
dotnet add package MnpPlasmon
```

```csharp
using MnpPlasmon;

var response = MnpPlasmon.SphereResponse(
    wavelengthNm: 550.0,
    radiusNm: 25.0,
    material: "Au",
    mediumRefractiveIndex: 1.0
);

Console.WriteLine($"σ_ext = {response.CExt:F2} nm²");
```

### Rust

```toml
[dependencies]
mnp-plasmon = "0.1"
```

```rust
use mnp_plasmon::sphere_response;

fn main() -> Result<(), String> {
    let response = sphere_response(550.0, 25.0, "Au", 1.0)?;
    println!("σ_ext = {:.2} nm²", response.c_ext);
    Ok(())
}
```

### C

```c
#include "mnp_plasmon.h"

int main(void) {
    sphere_result_t result = mnp_sphere_response(
        550.0,     // wavelength_nm
        25.0,      // radius_nm
        "Au",      // material
        1.0        // medium_refractive_index
    );
    
    printf("σ_ext = %.2f nm²\n", result.c_ext);
    return 0;
}
```

### C++

```cpp
#include "mnp_plasmon.hpp"

int main() {
    auto response = mnp::MnpPlasmon::sphere_response(
        550.0,     // wavelength
        25.0,      // radius
        "Au",      // material
        1.0        // medium_refractive_index
    );
    
    std::cout << "σ_ext = " << response.c_ext << " nm²" << std::endl;
    return 0;
}
```

## 📦 Published Modules

### Python MNPBEM Ecosystem

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

### MnpPlasmon Implementations

| Language | Package | Registry |
|----------|---------|----------|
| Python | `mnp-plasmon` | [PyPI](https://pypi.org/project/mnp-plasmon/) |
| JavaScript | `mnp`, `mnp-material`, `mnp-mie` | [npm](https://www.npmjs.com/~galihru?tab=packages) |
| C# / .NET | `MnpPlasmon` | [NuGet](https://www.nuget.org/packages/MnpPlasmon/) |
| Rust | `mnp-plasmon` | [Crates.io](https://crates.io/crates/mnp-plasmon) |
| C | `mnp-plasmon` | [vcpkg](https://github.com/microsoft/vcpkg) |
| C++ | `mnp-plasmon` | [vcpkg](https://github.com/microsoft/vcpkg) |

## 🔄 Release & Publishing Pipeline

This project uses a **Master Release Orchestrator** workflow that automatically publishes all language implementations simultaneously when a release is created:

```
GitHub Release (vX.Y.Z)
    ↓
Master Release Orchestrator (.github/workflows/release-master.yml)
    ├─→ Publish Rust → crates.io
    ├─→ Publish Python → PyPI
    ├─→ Publish JavaScript → npm + GitHub Packages
    ├─→ Publish C# → NuGet.org + GitHub Packages
    └─→ Publish C/C++ → vcpkg

✅ All packages synced to latest version
```

To trigger a multi-language release:

```bash
git tag v1.0.0
git push origin v1.0.0
# GitHub Release created → All platforms publish automatically
```

## 📊 Performance & Benchmarks

All implementations use consistent algorithms for reproducible results:

| Operation | Python | JavaScript | C# (.NET) | Rust | C |
|-----------|--------|-----------|-----------|------|---|
| Material lookup | O(1) | O(1) | O(1) | O(1) | O(1) |
| Drude ε(ω) | ~0.1 ms | ~0.1 ms | ~0.05 ms | ~0.05 ms | ~0.02 ms |
| Polarizability | ~0.1 ms | ~0.1 ms | ~0.05 ms | ~0.05 ms | ~0.02 ms |
| 100-point scan | ~12 ms | ~12 ms | ~5 ms | ~5 ms | ~2 ms |

*Benchmarks on reference materials (Au sphere, 550 nm wavelength, 25 nm radius)*

## 🔐 Security & CI/CD

- ✅ All platforms use **trusted publishing** (OIDC)
- ✅ Automated tests on every commit (GitHub Actions)
- ✅ Code quality checks with language-specific linters
- ✅ GPL-3.0 license compliance verified
- ✅ Multi-platform build matrices (Linux, macOS, Windows)

### Required GitHub Secrets (for maintainers)

```
PYPI_API_TOKEN         - PyPI Trusted Publisher (auto via OIDC)
NPMJS_TOKEN            - npm registry token
NUGET_API_KEY          - NuGet.org API key
CARGO_REGISTRY_TOKEN   - Crates.io API key
GITHUB_TOKEN           - Auto-generated (no setup needed)
```

## 👤 Author

**GALIH RIDHO UTOMO**  
📧 g4lihru@students.unnes.ac.id  
🔗 [GitHub](https://github.com/galihru)  
📦 [Profile - NPM](https://www.npmjs.com/~galihru) | [PyPI](https://pypi.org/user/galihru/) | [NuGet](https://www.nuget.org/profiles/galihru) | [Crates.io](https://crates.io/users/galihru)

## 📄 License

This project is licensed under **GPL-3.0-only**. See [LICENSE](LICENSE) for details.

All implementations (Python, JavaScript, C#, Rust, C, C++) maintain feature parity and are subject to the same license.
