import numpy as np
from mnpbem_mie import rayleigh_cross_sections

wavelength = np.linspace(450.0, 750.0, 5)
radius = 20.0
eps_particle = -10.0 + 1.0j
eps_medium = 1.77

c_ext, c_sca, c_abs = rayleigh_cross_sections(wavelength, radius, eps_particle, eps_medium)
print("C_ext:", c_ext)
print("C_sca:", c_sca)
print("C_abs:", c_abs)
