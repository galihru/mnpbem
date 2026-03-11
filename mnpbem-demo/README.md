# mnpbem-demo

`mnpbem-demo` provides reproducible spectral grids for controlled numerical experiments.

## Implemented Formulation
For start wavelength `lambda_start`, stop wavelength `lambda_stop`, and sample count `N`:

```text
\lambda_i = \lambda_0 + i\,\Delta\lambda,\qquad \Delta\lambda=\frac{\lambda_1-\lambda_0}{N-1}
```

## Implementation
- Demo grid generator: `src/mnpbem_demo/cases.py`

## Dependencies
- `numpy>=1.24`

## Installation
```bash
pip install mnpbem-demo
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
