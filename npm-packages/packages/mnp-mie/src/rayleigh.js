import { abs, add, complex, div, fromReal, imag, mul, sub } from "./complex.js";

function mapInput(values, fn) {
  if (Array.isArray(values)) {
    return values.map(fn);
  }
  return fn(values);
}

export function rayleighPolarizability(radiusNm, epsParticle, epsMedium) {
  const a = Number(radiusNm);
  const top = sub(epsParticle, epsMedium);
  const bottom = add(epsParticle, mul(fromReal(2), epsMedium));
  return mul(fromReal(4 * Math.PI * a ** 3), div(top, bottom));
}

export function rayleighCrossSections(wavelengthNm, radiusNm, epsParticle, epsMedium) {
  const solveOne = (wl, ep, em) => {
    const kFactor = (2 * Math.PI * Math.sqrt(em.re)) / Number(wl);
    const k = fromReal(kFactor);
    const alpha = rayleighPolarizability(radiusNm, ep, em);
    const cExt = k.re * imag(alpha);
    const cSca = (Math.abs(k.re) ** 4 * abs(alpha) ** 2) / (6 * Math.PI);
    const cAbs = cExt - cSca;
    return { cExt, cSca, cAbs };
  };

  if (Array.isArray(wavelengthNm)) {
    return wavelengthNm.map((wl, i) => solveOne(wl, epsParticle[i], epsMedium[i]));
  }
  return solveOne(wavelengthNm, epsParticle, epsMedium);
}

export { complex };
