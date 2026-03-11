import { add, complex, div, fromReal, mul, sqrtComplex, sub } from "./complex.js";

export const EV_TO_NM = 1.0 / 8.0655477e-4;
export const HARTREE_EV = 27.2116;

const MATERIAL_TABLE = {
  au: { rs: 3.0, eps0: 10.0, gammadAu: (0.66 / HARTREE_EV) / 10.0 },
  gold: { rs: 3.0, eps0: 10.0, gammadAu: (0.66 / HARTREE_EV) / 10.0 },
  ag: { rs: 3.0, eps0: 3.3, gammadAu: (0.66 / HARTREE_EV) / 30.0 },
  silver: { rs: 3.0, eps0: 3.3, gammadAu: (0.66 / HARTREE_EV) / 30.0 },
  al: { rs: 2.07, eps0: 1.0, gammadAu: 1.06 / HARTREE_EV },
  aluminum: { rs: 2.07, eps0: 1.0, gammadAu: 1.06 / HARTREE_EV }
};

function mapInput(values, fn) {
  if (Array.isArray(values)) {
    return values.map(fn);
  }
  return fn(values);
}

export function makeDrudeMaterial(name) {
  const key = String(name).toLowerCase();
  const row = MATERIAL_TABLE[key];
  if (!row) {
    throw new Error(`Unknown material '${name}'. Expected one of: Au, Ag, Al.`);
  }

  const density = 3.0 / (4.0 * Math.PI * row.rs ** 3);
  const wpAu = Math.sqrt(4.0 * Math.PI * density);

  return {
    name,
    eps0: row.eps0,
    gammad: row.gammadAu * HARTREE_EV,
    wp: wpAu * HARTREE_EV
  };
}

export function drudeEpsilon(materialName, wavelengthNm) {
  const m = makeDrudeMaterial(materialName);
  return mapInput(wavelengthNm, (wl) => {
    const w = EV_TO_NM / Number(wl);
    const numerator = fromReal(m.wp ** 2);
    const denom = mul(fromReal(w), add(fromReal(w), complex(0, m.gammad)));
    return sub(fromReal(m.eps0), div(numerator, denom));
  });
}

export function constantEpsilon(value, wavelengthNm) {
  return mapInput(wavelengthNm, () => complex(value, 0));
}

export function wavenumberInMedium(wavelengthNm, epsilonComplex) {
  const computeOne = (wl, eps) => {
    const factor = (2.0 * Math.PI) / Number(wl);
    return mul(fromReal(factor), sqrtComplex(eps));
  };

  if (Array.isArray(wavelengthNm)) {
    return wavelengthNm.map((wl, i) => computeOne(wl, epsilonComplex[i]));
  }
  return computeOne(wavelengthNm, epsilonComplex);
}
