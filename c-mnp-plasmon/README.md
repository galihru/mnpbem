# MNP Plasmon - C Library

Efficient C library for calculating optical response of metallic nanoparticles using Drude model and Rayleigh approximation.

## Features

- **Drude model** for metallic dielectric function
- **Rayleigh polarizability** calculations
- **Optical cross-sections**: extinction, scattering, absorption
- **Material database**: Au, Ag, Al with realistic parameters
- **High-level API** for complete sphere response simulation
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
ctest
# or
./mnp_plasmon_tests
```

### Run demo

```bash
./demo
```

## Usage

```c
#include "mnp_plasmon.h"
#include <stdio.h>

int main(void) {
    // Simulate Au nanoparticle response
    sphere_response_t response = mnp_simulate_sphere_response(
        "Au",           // material
        550.0,          // wavelength (nm)
        20.0,           // radius (nm)
        1.33            // medium refractive index (water)
    );
    
    mnp_print_response(&response);
    
    printf("Extinction cross-section: %.6e nm²\n", response.c_ext);
    printf("Scattering cross-section: %.6e nm²\n", response.c_sca);
    printf("Absorption cross-section: %.6e nm²\n", response.c_abs);
    
    return 0;
}
```

## API Reference

### Material Functions

- `const char **mnp_material_list(int *count)` - List available materials
- `int mnp_material_exists(const char *name)` - Check if material exists
- `material_t mnp_material_get(const char *name)` - Get material parameters

### Dielectric Function

- `complex_t mnp_drude_epsilon(const char *material, double wavelength_nm)` - Calculate Drude permittivity
- `complex_t mnp_constant_epsilon(double n_squared)` - Constant permittivity

### Rayleigh Theory

- `complex_t mnp_rayleigh_polarizability(double radius_nm, complex_t eps_particle, complex_t eps_medium)` - Calculate polarizability
- `cross_sections_t mnp_rayleigh_cross_sections(double wavelength_nm, double radius_nm, complex_t eps_particle, complex_t eps_medium)` - Calculate cross-sections

### High-level API

- `sphere_response_t mnp_simulate_sphere_response(const char *material, double wavelength_nm, double radius_nm, double medium_refractive_index)` - Complete response calculation

### Utilities

- `void mnp_print_response(const sphere_response_t *response)` - Pretty-print response

## License

GPL-3.0-only - See LICENSE file for details

## Links

- [Erlang package](https://hex.pm/packages/mnp_plasmon)
- [Racket package](https://pkgs.racket-lang.org/package/mnp-plasmon)
- [npm packages](https://www.npmjs.com/org/galihru)
- [GitHub repository](https://github.com/galihru/mnpbem)
