# mnpbem-misc

`mnpbem-misc` provides shared numerical utilities used across MNPBEM-Python submodules.

## Features
- Physical unit conversions between photon energy and wavelength.
- Vector norms and normalization utilities with MATLAB-compatible behavior.
- Tensor-aware linear algebra helpers (`matmul`, `matcross`, `inner`, `outer`, `spdiag`).

## Mathematical Formulations

### 1. Photon Energy-Wavelength Conversion
The conversion between photon energy and wavelength is:

$$
\lambda_{\mathrm{nm}} = \frac{C_{\mathrm{eV\cdot nm}}}{E_{\mathrm{eV}}},
\qquad C_{\mathrm{eV\cdot nm}} \approx 1239.841984
$$

### 2. Euclidean Vector Norm
For a vector $\mathbf{v}$:

$$
\|\mathbf{v}\|_2 = \sqrt{\sum_i |v_i|^2}
$$

### 3. Vector Normalization
Normalized vector:

$$
\tilde{\mathbf{v}} = \frac{\mathbf{v}}{\|\mathbf{v}_{\mathrm{ref}}\|_2}
$$

## Implementation
- Unit conversion utilities: `src/mnpbem_misc/units.py`
- Vector operations: `src/mnpbem_misc/vector.py`
- Linear algebra helpers: `src/mnpbem_misc/linalg.py`

## Dependencies
Runtime dependencies are installed automatically by `pip`:
- `numpy>=1.24`

## Installation
```bash
pip install mnpbem-misc
```

## Example Usage
Runnable example:
- `examples/basic_usage.py`

Run:
```bash
python examples/basic_usage.py
```

## Author
- GALIH RIDHO UTOMO
- g4lihru@students.unnes.ac.id
