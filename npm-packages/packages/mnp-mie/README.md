# @galihru/mnp-mie

Rayleigh quasi-static scattering formulas for spherical metallic nanoparticles
in a homogeneous dielectric medium. Computes complex polarizability and
electromagnetic cross sections -- extinction, scattering, and absorption --
within the electric-dipole approximation, valid for particle radius a << lambda.

---

## Physical Background

In the Rayleigh (quasi-static) limit, the electromagnetic response of a small
sphere is fully characterised by its induced electric dipole moment. The key
quantity is the complex polarizability alpha, which encodes both radiative
(scattering) and non-radiative (absorption) optical losses. This framework
underpins localized surface plasmon resonance (LSPR) spectroscopy, photothermal
therapy, and surface-enhanced sensing.

---

## Implemented Formulations

### 1. Quasi-static Polarizability (Clausius-Mossotti)

For a sphere of radius *a* with permittivity eps_p in an embedding medium with
permittivity eps_m:

![alpha](https://latex.codecogs.com/svg.latex?\alpha=4\pi%20a^3\frac{\varepsilon_p-\varepsilon_m}{\varepsilon_p+2\varepsilon_m}\quad[\mathrm{nm}^3])

The **Frohlich resonance** (LSPR condition) occurs when:

![Frohlich](https://latex.codecogs.com/svg.latex?\mathrm{Re}(\varepsilon_p+2\varepsilon_m)=0)

---

### 2. Wave Number in the Embedding Medium

![k in medium](https://latex.codecogs.com/svg.latex?k=\frac{2\pi}{\lambda}\sqrt{\varepsilon_m}\quad[\mathrm{nm}^{-1}])

where lambda is the free-space wavelength in nanometres.

---

### 3. Electromagnetic Cross Sections

**Extinction cross section** -- total power removed from the incident beam:

![C_ext](https://latex.codecogs.com/svg.latex?C_{\mathrm{ext}}=k\,\mathrm{Im}(\alpha)\quad[\mathrm{nm}^2])

**Scattering cross section** -- power re-radiated as scattered light:

![C_sca](https://latex.codecogs.com/svg.latex?C_{\mathrm{sca}}=\frac{|k|^4}{6\pi}|\alpha|^2\quad[\mathrm{nm}^2])

**Absorption cross section** -- power dissipated as Ohmic heat:

![C_abs](https://latex.codecogs.com/svg.latex?C_{\mathrm{abs}}=C_{\mathrm{ext}}-C_{\mathrm{sca}}\quad[\mathrm{nm}^2])

---

## Install

```bash
npm install @galihru/mnp-mie
```

---

## API Reference

### `rayleighPolarizability(radiusNm, epsParticle, epsMedium)`

Returns the complex polarizability alpha of a sphere.

```js
import { complex, rayleighPolarizability } from "@galihru/mnp-mie";

const epsParticle = complex(-7.45, 1.23);  // Au at 548 nm
const epsMedium   = complex(1.769, 0.0);   // water

const alpha = rayleighPolarizability(50, epsParticle, epsMedium);
// -> { re: ..., im: ... }   [nm^3]
```

---

### `rayleighCrossSections(wavelengthNm, radiusNm, epsParticle, epsMedium)`

Returns extinction, scattering, and absorption cross sections in nm^2.

```js
import { complex, rayleighCrossSections } from "@galihru/mnp-mie";

const epsParticle = complex(-7.45, 1.23);
const epsMedium   = complex(1.769, 0.0);

// Single wavelength
const cs = rayleighCrossSections(548.1, 50, epsParticle, epsMedium);
// -> { cExt: ..., cSca: ..., cAbs: ... }   [nm^2]

// Spectral scan (array input)
const scan = rayleighCrossSections(
  [400, 450, 500, 548, 600, 700],
  50,
  [eps400, eps450, eps500, eps548, eps600, eps700],
  [em400,  em450,  em500,  em548,  em600,  em700]
);
// -> [{ cExt, cSca, cAbs }, ...]
```

---

### `complex(re, im)`

Constructs a complex number `{ re, im }`.

```js
import { complex } from "@galihru/mnp-mie";

const z = complex(-5.2, 2.1);
// -> { re: -5.2, im: 2.1 }
```

---

## Author

**GALIH RIDHO UTOMO** | g4lihru@students.unnes.ac.id
Universitas Negeri Semarang (UNNES)
License: GPL-2.0-only