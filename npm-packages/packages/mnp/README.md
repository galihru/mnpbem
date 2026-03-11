# @galihru/mnp

Main integrated package that composes:

- `@galihru/mnp-material`
- `@galihru/mnp-mie`

This package provides a unified scientific API for fast nanoparticle-response estimates.

## Install

```bash
npm install @galihru/mnp
```

## Usage

```js
import { simulateSphereResponse } from "@galihru/mnp";

const result = simulateSphereResponse({
  material: "Au",
  wavelengthNm: 548.1,
  radiusNm: 50,
  mediumRefractiveIndex: 1.33
});

console.log(result.crossSection);
```
