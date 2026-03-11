# mnpbem-mesh2d

`mnpbem-mesh2d` provides triangle geometry operators used in mesh-quality and circumcircle computations.

## Implemented Formulations
Signed doubled triangle area:

```text
A_2 = (\mathbf{d}_{12})_x(\mathbf{d}_{13})_y-(\mathbf{d}_{12})_y(\mathbf{d}_{13})_x
```

Circumcircle radius squared:

```text
R^2=\|\mathbf{p}_1-\mathbf{c}\|^2
```

Mesh quality indicator:

```text
q = 3.4641\,\frac{|A_2|}{\|\mathbf{d}_{12}\|^2+\|\mathbf{d}_{13}\|^2+\|\mathbf{d}_{23}\|^2},\quad 0\le q\le 1
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
