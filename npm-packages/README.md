# MNP JavaScript Packages

This folder contains three publishable npm packages:

- `@galihru/mnp-material`: Drude dielectric formulations.
- `@galihru/mnp-mie`: Rayleigh-limit scattering formulations.
- `@galihru/mnp`: umbrella package re-exporting the two scientific components.

No external runtime dependencies are used.

## Install From npm

```bash
npm install @galihru/mnp
```

Or install sub-packages directly:

```bash
npm install @galihru/mnp-material @galihru/mnp-mie
```

## Basic Usage

```js
import { sphereResponse } from "@galihru/mnp";

const r = sphereResponse({
	wavelengthNm: 550,
	radiusNm: 25,
	material: "Au",
	mediumRefractiveIndex: 1.0
});

console.log(r.cExt, r.cSca, r.cAbs);
```

## Install From GitHub Packages (Alternative)

Create a project-level `.npmrc`:

```ini
@galihru:registry=https://npm.pkg.github.com/
//npm.pkg.github.com/:_authToken=YOUR_GITHUB_TOKEN
```

Then install as usual:

```bash
npm install @galihru/mnp
```

## Why "Used by" May Not Show Yet

GitHub "Used by" for repositories is generated automatically from dependency graph data in public repositories that depend on your package/repo.
It cannot be enabled manually by a single setting.

To increase the chance it appears:

1. Keep package metadata complete (`repository`, `homepage`, `bugs`).
2. Publish packages as public.
3. Ensure other public repositories declare dependency on `@galihru/mnp`.
