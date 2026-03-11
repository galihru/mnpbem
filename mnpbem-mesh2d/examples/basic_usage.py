import numpy as np
from mnpbem_mesh2d import triarea, quality, circumcircle

points = np.array([[0.0, 0.0], [1.0, 0.0], [0.0, 1.0]])
triangles = np.array([[0, 1, 2]])

print("Signed doubled area:", triarea(points, triangles))
print("Quality:", quality(points, triangles))
print("Circumcircle [cx, cy, r^2]:", circumcircle(points, triangles))
