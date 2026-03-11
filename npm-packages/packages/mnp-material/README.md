# @galihru/mnp-material

Analytical dielectric-function models for metallic nanoparticles in the
framework of plasmonic nanophotonics. Provides frequency-dependent complex
permittivity via the Drude free-electron model and constant dielectric
approximation, with complex wave-number computation, all operating natively
in the wavelength domain (wavelength in nm).

---

## Physical Background

The optical response of a metallic nanoparticle is governed by its
frequency-dependent complex dielectric function epsilon(omega). This package
implements two analytical models and the wave-number relation used in
electrodynamic simulations.

---

## Implemented Models

### 1. Energy-Wavelength Conversion

All models accept wavelength in nanometres. The photon energy is computed as:

![omega = C/lambda](https://latex.codecogs.com/svg.latex?\omega\,[\mathrm{eV}]=\frac{C}{\lambda\,[\mathrm{nm}]},\quad%20C=1239.841984\,\mathrm{eV\cdot%20nm})

---

### 2. Drude Free-Electron Model

Describes the dielectric response of free-electron metals:

![epsilon(omega)](https://latex.codecogs.com/svg.latex?\varepsilon(\omega)=\varepsilon_\infty-\frac{\omega_p^2}{\omega(\omega+i\gamma)})

**Parameters:**
- **eps_inf** -- high-frequency (interband) dielectric constant
- **omega_p** -- bulk plasma frequency, derived from electron density via the Wigner-Seitz radius *r_s*:

![omega_p from r_s](https://latex.codecogs.com/svg.latex?\rho_0=\frac{3}{4\pi%20r_s^3},\qquad\omega_p=\sqrt{4\pi\rho_0}\times%2027.2116\,\mathrm{eV})

- **gamma** -- phenomenological Drude damping rate (scattering)

**Built-in material table:**

| Material | r_s (a.u.) | eps_inf | gamma (eV) | omega_p (eV) |
|---|---|---|---|---|
| `Au` / `gold` | 3.00 | 10.0 | 0.066 | ~9.07 |
| `Ag` / `silver` | 3.00 | 3.3 | 0.022 | ~9.07 |
| `Al` / `aluminum` | 2.07 | 1.0 | 1.06 | ~15.8 |

---

### 3. Constant Dielectric Model

For non-dispersive homogeneous embedding media (glass, water, vacuum):

![epsilon constant](https://latex.codecogs.com/svg.latex?\varepsilon(\lambda)=\varepsilon_0,\quad\varepsilon_0\in\mathbb{C})

---

### 4. Wave Number in Medium

Complex wave number for light propagating through a dielectric:

![k(lambda)](https://latex.codecogs.com/svg.latex?k(\lambda)=\frac{2\pi}{\lambda}\sqrt{\varepsilon(\lambda)}\quad[\mathrm{nm}^{-1}])

---

## Install

```bash
npm install @galihru/mnp-material
```

---

## API Reference

### `drudeEpsilon(materialName, wavelengthNm)`

Returns the complex Drude permittivity for a built-in metal at one or multiple
wavelengths.

```js
import { drudeEpsilon } from "@galihru/mnp-material";

// Single wavelength -> { re, im }
const eps = drudeEpsilon("Au", 548.1);

// Wavelength array -> [{ re, im }, ...]
const spectra = drudeEpsilon("Ag", [400, 500, 600, 700]);
```

---

### `makeDrudeMaterial(name)`

Returns the raw Drude parameter object for a given metal name.

```js
import { makeDrudeMaterial } from "@galihru/mnp-material";

const au = makeDrudeMaterial("Au");
// -> { name: "Au", eps0: 10.0, gammad: 0.066, wp: 9.07 }
```

---

### `constantEpsilon(value, wavelengthNm)`

Returns a wavelength-independent complex permittivity.

```js
import { constantEpsilon } from "@galihru/mnp-material";

// Water: n = 1.33 -> eps = n^2 = 1.769
const epsWater = constantEpsilon(1.769, 548.1);
// -> { re: 1.769, im: 0 }
```

---

### `wavenumberInMedium(wavelengthNm, epsilonComplex)`

Computes the complex wave number k = (2*pi/lambda)*sqrt(epsilon).

```js
import { constantEpsilon, wavenumberInMedium } from "@galihru/mnp-material";

const eps = constantEpsilon(1.769, 548.1);
const k = wavenumberInMedium(548.1, eps);
// -> { re: ..., im: ... }   [nm^-1]
```

---

### Complex Arithmetic Utilities

```js
import { complex, add, sub, mul, div, sqrtComplex, fromReal } from "@galihru/mnp-material";

const z1 = complex(-5.2, 1.3);     // -5.2 + 1.3i
const z2 = fromReal(2.0);          //  2.0 + 0i
const prod = mul(z1, z2);          // -> { re: -10.4, im: 2.6 }
const root = sqrtComplex(z1);      // -> { re: ..., im: ... }
```

---

## Author

**GALIH RIDHO UTOMO** | g4lihru@students.unnes.ac.id
Universitas Negeri Semarang (UNNES)
License: GPL-2.0-only