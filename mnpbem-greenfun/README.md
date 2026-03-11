# mnpbem-greenfun

`mnpbem-greenfun` provides baseline free-space Green-function kernels for frequency-domain electrodynamics.

## Implemented Formulations
Scalar Green function:

```text
G(r,k)=\frac{e^{ikr}}{4\pi r}
```

Dyadic-related prefactor:

```text
k^2 G(r,k)
```

## Implementation
- Kernel functions: `src/mnpbem_greenfun/kernels.py`

## Dependencies
- `numpy>=1.24`

## Installation
```bash
pip install mnpbem-greenfun
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
