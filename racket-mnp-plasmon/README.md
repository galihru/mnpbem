# MNP Plasmon

**Integrated computational package for single-nanoparticle electromagnetic response** in the Rayleigh quasi-static limit.

Composes Drude dielectric-function evaluation with Rayleigh polarizability and optical cross-section computation into a unified, self-consistent simulation API for plasmonic nanoparticles.

## Physical Scope

Given a metallic sphere of radius **a** < λ embedded in a dielectric host medium, compute as functions of illumination wavelength:

1. **Complex permittivity** via the Drude free-electron model:
   ```
   ε(ω) = ε_∞ - ω_p² / [ω(ω + iγ)]
   ```

2. **Rayleigh polarizability** via Clausius-Mossotti:
   ```
   α = 4πa³ (ε_p - ε_m) / (ε_p + 2ε_m)
   ```

3. **Optical cross-sections**:
   ```
   C_ext = k · Im(α)
   C_sca = |k|⁴|α|² / (6π)
   C_abs = C_ext - C_sca
   ```

## Installation

```bash
raco pkg install mnp-plasmon
```

Or install from source:

```bash
cd racket-mnp-plasmon
raco pkg install
```

## Quick Start

```racket
#lang racket

(require mnp-plasmon)

;; Gold nanoparticle: 20 nm radius, in water, 550 nm wavelength
(define result
  (simulate-sphere-response
    #:material "Au"
    #:wavelength-nm 550
    #:radius-nm 20
    #:medium-n 1.33))

;; Extinction cross-section in nm²
(displayln (cadr (assoc 'c-ext result)))
```

## Materials

Built-in Drude parameters for:
- **Au** (Gold): ωp = 3.106 eV, γ = 0.0132 eV
- **Ag** (Silver): ωp = 3.810 eV, γ = 0.0048 eV
- **Al** (Aluminum): ωp = 14.83 eV, γ = 0.098 eV

## API

### High-Level Interface

```racket
(simulate-sphere-response
  #:material "Au"           ; Material name
  #:wavelength-nm 550       ; Wavelength in nm
  #:radius-nm 20            ; Nanoparticle radius in nm
  #:medium-n 1.33)          ; Medium refractive index
```

Returns a property list with:
- Material, wavelength, radius, medium refractive index
- Complex permittivity `epsilon-particle`
- Complex polarizability `polarizability`
- Cross-sections: `c-ext`, `c-sca`, `c-abs` (in nm²)

### Core Functions

- `(drude-epsilon material wl_nm)` → (values real imag)
- `(rayleigh-polarizability radius eps_p eps_m)` → (values real imag)
- `(rayleigh-cross-sections wl radius eps_p eps_m)` → (values c_ext c_sca c_abs)
- `(material-list)` → list of available materials
- `(get-drude-params material)` → Drude parameters

## Examples

See [examples/basic.rkt](examples/basic.rkt) for a complete example.

## Testing

```bash
raco test tests/
```

## References

- Bohren, C. F., & Huffman, D. R. (1983). *Absorption and scattering of light by small particles*. Wiley.
- Eustis, S., & El-Sayed, M. A. (2006). Why gold nanoparticles are more precious than pretty gold. *Chemical Society Reviews*, 35(3), 209–217.

## Author

Galih Ridho Utomo <g4lihru@students.unnes.ac.id>

## License

GPL-3.0 license
