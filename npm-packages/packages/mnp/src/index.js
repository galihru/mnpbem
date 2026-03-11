import { constantEpsilon, drudeEpsilon } from "@galihru/mnp-material";
import { rayleighCrossSections, rayleighPolarizability } from "@galihru/mnp-mie";

export { EV_TO_NM, HARTREE_EV, constantEpsilon, drudeEpsilon, makeDrudeMaterial, wavenumberInMedium } from "@galihru/mnp-material";
export { complex, rayleighCrossSections, rayleighPolarizability } from "@galihru/mnp-mie";

export function simulateSphereResponse({
  material = "Au",
  wavelengthNm = 548.1,
  radiusNm = 50,
  mediumRefractiveIndex = 1.33
} = {}) {
  const epsParticle = drudeEpsilon(material, wavelengthNm);
  const epsMedium = constantEpsilon(mediumRefractiveIndex ** 2, wavelengthNm);
  const alpha = rayleighPolarizability(radiusNm, epsParticle, epsMedium);
  const crossSection = rayleighCrossSections(wavelengthNm, radiusNm, epsParticle, epsMedium);

  return {
    inputs: { material, wavelengthNm, radiusNm, mediumRefractiveIndex },
    epsParticle,
    epsMedium,
    alpha,
    crossSection
  };
}
