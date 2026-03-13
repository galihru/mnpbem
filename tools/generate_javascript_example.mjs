import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { drudeEpsilon, constantEpsilon } from "../npm-packages/packages/mnp-material/src/index.js";
import { rayleighCrossSections } from "../npm-packages/packages/mnp-mie/src/index.js";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const root = path.resolve(__dirname, "..");
const outPath = path.join(root, "docs", "example-data", "javascript.csv");

const wavelengths = Array.from({ length: 61 }, (_, index) => 400 + index * 5);
const epsParticle = drudeEpsilon("Au", wavelengths);
const epsMedium = constantEpsilon(1.33 ** 2, wavelengths);
const spectra = rayleighCrossSections(wavelengths, 25.0, epsParticle, epsMedium);

fs.mkdirSync(path.dirname(outPath), { recursive: true });
let csv = "wavelength_nm,c_ext,c_sca,c_abs\n";
for (let index = 0; index < wavelengths.length; index += 1) {
  const row = spectra[index];
  csv += `${wavelengths[index]},${row.cExt},${row.cSca},${row.cAbs}\n`;
}
fs.writeFileSync(outPath, csv, "utf8");
