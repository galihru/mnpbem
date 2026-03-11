# mnpbem-mesh2d

`mnpbem-mesh2d` provides triangle geometry operators used in mesh-quality and circumcircle computations.

## Implemented Formulations
Signed doubled triangle area:

```text
A2 = d12_x * d13_y - d12_y * d13_x
```

Circumcircle radius squared:

```text
R2 = ||p1 - c||^2
```

Mesh quality indicator:

```text
q = (2 * sqrt(3) * |A2|) / (||d12||^2 + ||d13||^2 + ||d23||^2), 0 <= q <= 1
```

## Implementation
- Geometry operators: `src/mnpbem_mesh2d/geometry.py`

## Dependencies
- `numpy>=1.24`

## Installation
```bash
pip install mnpbem-mesh2d
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
