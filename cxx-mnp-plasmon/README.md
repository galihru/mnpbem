# MNP Plasmon - C++ Library

Modern C++17 library for calculating optical response of metallic nanoparticles using Drude model and Rayleigh approximation.

## Features

- **Modern C++17** design with STL containers and `std::complex`
- **Drude model** for metallic dielectric function
- **Rayleigh polarizability** calculations
- **Optical cross-sections**: extinction, scattering, absorption
- **Material database**: Au, Ag, Al with realistic parameters
- **High-level API** for complete sphere response simulation
- **Unit tests** with Google Test framework
- **Cross-platform** build with CMake

## Installation

### Build from source

```bash
mkdir build
cd build
cmake ..
cmake --build .
```

### Run tests

```bash
ctest --verbose
```

### Run demo

```bash
./demo
```

## Usage

```cpp
#include "mnp_plasmon.hpp"
#include <iostream>

using namespace mnp;

int main() {
    // Simulate Au nanoparticle response
    SphereResponse response = MnpPlasmon::simulate_sphere_response(
        "Au",           // material
        550.0,          // wavelength (nm)
        20.0,           // radius (nm)
        1.33            // medium refractive index (water)
    );
    
    MnpPlasmon::print_response(response);
    
    std::cout << "Extinction cross-section: " << response.c_ext << " nm²\n";
    std::cout << "Scattering cross-section: " << response.c_sca << " nm²\n";
    std::cout << "Absorption cross-section: " << response.c_abs << " nm²\n";
    
    return 0;
}
```

## API Reference

### Material Functions

```cpp
static std::vector<Material> material_list();
static bool material_exists(const std::string& name);
static Material material_get(const std::string& name);
```

### Dielectric Functions

```cpp
static complex drude_epsilon(const std::string& material, double wavelength_nm);
static complex constant_epsilon(double n_squared);
```

### Rayleigh Theory

```cpp
static complex rayleigh_polarizability(
    double radius_nm,
    complex eps_particle,
    complex eps_medium
);

static CrossSections rayleigh_cross_sections(
    double wavelength_nm,
    double radius_nm,
    complex eps_particle,
    complex eps_medium
);
```

### High-level API

```cpp
static SphereResponse simulate_sphere_response(
    const std::string& material,
    double wavelength_nm,
    double radius_nm,
    double medium_refractive_index
);
```

### Utilities

```cpp
static void print_response(const SphereResponse& response);
```

## Data Types

- `complex` = `std::complex<double>`
- `Material` - Contains name, omega_p, gamma, eps_inf
- `SphereResponse` - Complete response with epsilon, polarizability, and cross-sections
- `CrossSections` - Contains c_ext, c_sca, c_abs

## License

GPL-3.0-only - See LICENSE file for details

## Links

- [Erlang package](https://hex.pm/packages/mnp_plasmon)
- [Racket package](https://pkgs.racket-lang.org/package/mnp-plasmon)
- [npm packages](https://www.npmjs.com/org/galihru)
- [GitHub repository](https://github.com/galihru/mnpbem)
