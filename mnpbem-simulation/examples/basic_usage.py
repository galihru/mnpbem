import numpy as np
from mnpbem_simulation import sample_spectrum

wavelengths = np.linspace(450.0, 750.0, 6)
response = sample_spectrum(wavelengths, lambda wl: 1.0 / wl + 0j)

print("Wavelength grid:", wavelengths)
print("Sampled response:", response)
