# mnpbem-mesh2d

`mnpbem-mesh2d` provides triangle geometry operators used in mesh-quality and circumcircle computations.

## Implemented Formulations
Signed doubled triangle area:

![Equation](https://latex.codecogs.com/svg.image?%5Cdpi%7B150%7D%20A_2%20%3D%20%28d_%7B12%7D%29_x%28d_%7B13%7D%29_y-%28d_%7B12%7D%29_y%28d_%7B13%7D%29_x)

Circumcircle radius squared:

![Equation](https://latex.codecogs.com/svg.image?%5Cdpi%7B150%7D%20R%5E2%20%3D%20%5C%7Cp_1-c%5C%7C%5E2)

Mesh quality indicator:

![Equation](https://latex.codecogs.com/svg.image?%5Cdpi%7B150%7D%20q%20%3D%20%5Cfrac%7B2%5Csqrt%7B3%7D%7CA_2%7C%7D%7B%5C%7Cd_%7B12%7D%5C%7C%5E2%2B%5C%7Cd_%7B13%7D%5C%7C%5E2%2B%5C%7Cd_%7B23%7D%5C%7C%5E2%7D%2C%5Cquad%200%5Cle%20q%5Cle%201)

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
