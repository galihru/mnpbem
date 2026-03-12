# mnp-plasmon (Rust)

[![Crates.io](https://img.shields.io/crates/v/mnp-plasmon)](https://crates.io/crates/mnp-plasmon)
[![Docs.rs](https://docs.rs/mnp-plasmon/badge.svg)](https://docs.rs/mnp-plasmon/)
[![License: GPL-3.0](https://img.shields.io/badge/license-GPL--3.0-blue)](LICENSE)

Efficient Rust library for calculating optical response of metallic nanoparticles using Drude model and Rayleigh approximation.

## Features

- Drude dielectric model for metallic response
- Rayleigh approximation for optical polarizability
- Cross-section calculations (extinction, scattering, absorption)
- Material database (Au, Ag, Al)
- Wavelength scanning capabilities
- Zero external dependencies (core functionality only)
- Optional serde serialization support

## Installation

Add to your `Cargo.toml`:

```toml
[dependencies]
mnp-plasmon = "0.1"
```

## Quick Start

```rust
use mnp_plasmon::*;

fn main() -> Result<(), String> {
    // Calculate optical response of 25 nm Au sphere at 550 nm
    let response = sphere_response(
        550.0,  // wavelength (nm)
        25.0,   // radius (nm)
        "Au",   // material
        1.0,    // medium refractive index
    )?;

    println!("Extinction: {:.2} nm²", response.c_ext);
    println!("Scattering: {:.2} nm²", response.c_sca);
    println!("Absorption: {:.2} nm²", response.c_abs);
    
    Ok(())
}
```

## Supported Materials

- **Au** (Gold): ωₚ = 3.106 eV, γ = 0.0132 eV
- **Ag** (Silver): ωₚ = 3.810 eV, γ = 0.0048 eV
- **Al** (Aluminum): ωₚ = 14.83 eV, γ = 0.098 eV

## Physical Model

The Drude dielectric function is given by:

```text
epsilon(omega) = epsilon_inf - (omega_p^2) / (omega * (omega + i*gamma))
```

where:
- `omega_p` is the plasma frequency
- `gamma` is the damping coefficient
- `omega` is the angular frequency

The Rayleigh approximation for spherical particles yields a frequency-dependent polarizability:

```text
alpha(omega) = 4*pi*a^3 * (epsilon_p(omega) - epsilon_m) / (epsilon_p(omega) + 2*epsilon_m)
```

Cross-sections are computed as:
- **Extinction**: `sigma_ext = (4*pi/k) * Im(alpha)`
- **Scattering**: `sigma_sca = (k^4/(6*pi)) * |alpha|^2`
- **Absorption**: `sigma_abs = sigma_ext - sigma_sca`

## Building from Source

```bash
cargo build --release
cargo test
cargo run --example basic_sphere --release
```

## License

GPL-3.0-only

See [LICENSE](../../LICENSE) for details.
