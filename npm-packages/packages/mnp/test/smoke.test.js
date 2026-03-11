import test from "node:test";
import assert from "node:assert/strict";

import { simulateSphereResponse } from "../src/index.js";

test("integrated mnp simulation returns coherent output object", () => {
  const out = simulateSphereResponse({
    material: "Au",
    wavelengthNm: 548.1,
    radiusNm: 50,
    mediumRefractiveIndex: 1.33
  });

  assert.equal(out.inputs.material, "Au");
  assert.equal(typeof out.epsParticle.re, "number");
  assert.equal(typeof out.crossSection.cExt, "number");
});
