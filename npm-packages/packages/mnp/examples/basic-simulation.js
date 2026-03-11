import { simulateSphereResponse } from "../src/index.js";

const result = simulateSphereResponse({
  material: "Au",
  wavelengthNm: 548.1,
  radiusNm: 50,
  mediumRefractiveIndex: 1.33
});

console.log("MNP simulation snapshot");
console.log(JSON.stringify(result, null, 2));
