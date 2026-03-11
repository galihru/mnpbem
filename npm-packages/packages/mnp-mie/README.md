# @galihru/mnp-mie

Rayleigh-limit scattering formulas for small spherical particles.

Implemented formulations:

$$
\alpha = 4\pi a^3\frac{\varepsilon_p-\varepsilon_m}{\varepsilon_p+2\varepsilon_m}
$$

$$
C_{\mathrm{ext}} = k\,\mathrm{Im}(\alpha),\quad
C_{\mathrm{sca}} = \frac{|k|^4}{6\pi}|\alpha|^2,\quad
C_{\mathrm{abs}} = C_{\mathrm{ext}}-C_{\mathrm{sca}}
$$

## Install

```bash
npm install @galihru/mnp-mie
```

## Usage

```js
import { complex, rayleighCrossSections } from "@galihru/mnp-mie";

const epsParticle = complex(-5.2, 2.1);
const epsMedium = complex(1.77, 0.0);
console.log(rayleighCrossSections(548.1, 50, epsParticle, epsMedium));
```
