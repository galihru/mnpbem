import numpy as np
from mnpbem_greenfun import scalar_green, dyadic_prefactor

r = np.array([5.0, 10.0, 20.0])
k = 2 * np.pi / 500.0

G = scalar_green(r, k)
K2G = dyadic_prefactor(r, k)

print("G(r,k):", G)
print("k^2 G(r,k):", K2G)
