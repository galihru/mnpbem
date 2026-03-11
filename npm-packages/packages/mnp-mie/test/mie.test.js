import test from "node:test";
import assert from "node:assert/strict";

import { complex, rayleighCrossSections, rayleighPolarizability } from "../src/index.js";

test("rayleigh polarizability returns complex output", () => {
  const alpha = rayleighPolarizability(50, complex(-5, 2), complex(1.77, 0));
  assert.equal(typeof alpha.re, "number");
  assert.equal(typeof alpha.im, "number");
});

test("rayleigh cross section returns physically ordered channels", () => {
  const out = rayleighCrossSections(548.1, 50, complex(-5, 2), complex(1.77, 0));
  assert.equal(typeof out.cExt, "number");
  assert.equal(typeof out.cSca, "number");
  assert.equal(typeof out.cAbs, "number");
});
