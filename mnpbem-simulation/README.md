# mnpbem-simulation

`mnpbem-simulation` orchestrates vectorized spectrum evaluation over wavelength grids.
Release metadata is generated from this README so installation notes and mathematical context stay synchronized.

## Implemented Formulation
For a sampled wavelength grid, the response is evaluated as:

$$
S_i = f(\lambda_i)
$$

with strict shape-consistency between input grid and output spectrum.

## Implementation
- Spectrum sampling: `src/mnpbem_simulation/spectra.py`

## Dependencies
- `numpy>=1.24`

## Installation
```bash
pip install mnpbem-simulation
```

## Example
Runnable example:
- `examples/basic_usage.py`

Run:
```bash
python examples/basic_usage.py
```

## Author
- GALIH RIDHO UTOMO
- g4lihru@students.unnes.ac.id
