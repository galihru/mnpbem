# @galihru/mnp-material

Scientific dielectric-response models for plasmonic simulations.

Implemented formulation (Drude model):

$$
\varepsilon(\omega)=\varepsilon_\infty-\frac{\omega_p^2}{\omega(\omega+i\gamma)}
$$

## Install

```bash
npm install @galihru/mnp-material
```

## Usage

```js
import { drudeEpsilon } from "@galihru/mnp-material";

const epsAu = drudeEpsilon("Au", 548.1);
console.log(epsAu);
```
