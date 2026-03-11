# @galihru/mnp

Integrated computational package for the single-nanoparticle electromagnetic
response in the Rayleigh quasi-static limit. Composes dielectric-function
evaluation with polarizability and optical cross-section computation into a
unified, self-consistent simulation API.

---

## Physical Scope

This package solves the **single-nanoparticle optical response problem**: given
a metallic sphere of radius a << lambda embedded in a dielectric host medium,
compute as functions of illumination wavelength:

1. Complex permittivity via the **Drude free-electron model**:

   ![epsilon Drude](https://latex.codecogs.com/svg.latex?\varepsilon(\omega)=\varepsilon_\infty-\frac{\omega_p^2}{\omega(\omega+i\gamma)})

2. Complex polarizability via the **Clausius-Mossotti relation**:

   ![alpha CM](https://latex.codecogs.com/svg.latex?\alpha=4\pi%20a^3\frac{\varepsilon_p-\varepsilon_m}{\varepsilon_p+2\varepsilon_m})

3. Electromagnetic **cross sections** from the optical theorem:

   ![cross sections](https://latex.codecogs.com/svg.latex?C_{\mathrm{ext}}=k\,\mathrm{Im}(\alpha),\quad%20C_{\mathrm{sca}}=\frac{|k|^4}{6\pi}|\alpha|^2,\quad%20C_{\mathrm{abs}}=C_{\mathrm{ext}}-C_{\mathrm{sca}})

---

## Composed Packages

| Package | Description |
|---|---|
| [`@galihru/mnp-material`](https://www.npmjs.com/package/@galihru/mnp-material) | Drude dielectric model for Au, Ag, Al; constant epsilon; complex wave number |
| [`@galihru/mnp-mie`](https://www.npmjs.com/package/@galihru/mnp-mie) | Rayleigh polarizability; extinction, scattering, and absorption cross sections |

---

## Install

```bash
npm install @galihru/mnp
```

---

## API Reference

### `simulateSphereResponse(options)` -- High-level

Computes the complete optical response of a metallic nanosphere in a single call.

```js
import { simulateSphereResponse } from "@galihru/mnp";

const result = simulateSphereResponse({
  material:              "Au",   // "Au" | "Ag" | "Al"
  wavelengthNm:          548.1,  // nm -- scalar or Array for spectral scan
  radiusNm:              50,     // nm
  mediumRefractiveIndex: 1.33    // dimensionless refractive index of host medium
});
```

**Return value:**

| Field | Unit | Description |
|---|---|---|
| `inputs` | -- | Echo of all input parameters |
| `epsParticle` | `{re, im}` | Complex permittivity of the metal particle |
| `epsMedium` | `{re, im}` | Permittivity of the embedding medium |
| `alpha` | `{re, im}` nm^3 | Quasi-static complex polarizability |
| `crossSection.cExt` | nm^2 | Extinction cross section |
| `crossSection.cSca` | nm^2 | Scattering cross section |
| `crossSection.cAbs` | nm^2 | Absorption cross section |

---

### Low-level Re-exports

All functions from sub-packages are re-exported directly:

```js
import {
  // Dielectric models
  drudeEpsilon, makeDrudeMaterial, constantEpsilon, wavenumberInMedium,
  // Scattering
  rayleighPolarizability, rayleighCrossSections,
  // Complex arithmetic
  complex, add, sub, mul, div, sqrtComplex, fromReal,
  // Constants
  EV_TO_NM, HARTREE_EV
} from "@galihru/mnp";
```

---

## Example -- Spectral Scan

```js
import { drudeEpsilon, constantEpsilon, rayleighCrossSections } from "@galihru/mnp";

const wavelengths = [400, 450, 500, 548, 600, 700];

// Au permittivity across wavelengths
const epsAu  = drudeEpsilon("Au", wavelengths);

// Host medium: water (n = 1.33, eps = n^2)
const epsH2O = wavelengths.map(w => constantEpsilon(1.769, w));

// Cross sections for a 50 nm radius Au sphere
const spectra = rayleighCrossSections(wavelengths, 50, epsAu, epsH2O);

spectra.forEach((cs, i) =>
  console.log(
    wavelengths[i] + " nm  Cext=" + cs.cExt.toFixed(1) + " nm^2" +
    "  Cabs=" + cs.cAbs.toFixed(1) + " nm^2"
  )
);
```

---

## Author

**GALIH RIDHO UTOMO** | g4lihru@students.unnes.ac.id
Universitas Negeri Semarang (UNNES)
License: GPL-2.0-only