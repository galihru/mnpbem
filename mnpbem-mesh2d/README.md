# mnpbem-mesh2d

`mnpbem-mesh2d` provides triangle geometry operators used in mesh-quality and circumcircle computations.

## Implemented Formulations
Signed doubled triangle area:

$$
A_2=(d_{12})_x(d_{13})_y-(d_{12})_y(d_{13})_x
$$

Circumcircle radius squared:

$$
R^2=\|p_1-c\|^2
$$

Mesh quality indicator:

$$
q=\frac{2\sqrt{3}|A_2|}{\|d_{12}\|^2+\|d_{13}\|^2+\|d_{23}\|^2},
\quad 0 \le q \le 1
$$

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
