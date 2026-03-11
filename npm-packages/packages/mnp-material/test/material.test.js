import test from "node:test";
import assert from "node:assert/strict";

import { drudeEpsilon, makeDrudeMaterial } from "../src/index.js";

test("material parameters are generated for Au", () => {
  const au = makeDrudeMaterial("Au");
  assert.equal(typeof au.wp, "number");
  assert.ok(au.wp > 0);
});

test("drude epsilon returns complex value", () => {
  const eps = drudeEpsilon("Au", 548.1);
  assert.equal(typeof eps.re, "number");
  assert.equal(typeof eps.im, "number");
});

test("drude epsilon supports vector wavelengths", () => {
  const eps = drudeEpsilon("Ag", [500, 550, 600]);
  assert.equal(eps.length, 3);
});
