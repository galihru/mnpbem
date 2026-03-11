import numpy as np
from mnpbem_bem import LinearResponseSolver

A = np.array([[2 + 0j, 1 + 0j], [1 + 0j, 3 + 0j]])
b = np.array([1 + 0j, 0 + 0j])

solver = LinearResponseSolver(A)
x = solver.solve(b)
print("Solution:", x)
