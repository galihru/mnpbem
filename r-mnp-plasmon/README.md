# mnpPlasmonR

R package for optical response of metallic nanoparticles using Drude dielectric model and Rayleigh approximation.

## Install from source

```r
install.packages("mnpPlasmonR_0.1.0.tar.gz", repos = NULL, type = "source")
```

## Example

```r
library(mnpPlasmonR)

resp <- sphere_response(
  wavelength_nm = 550,
  radius_nm = 25,
  material = "Au",
  medium_refractive_index = 1.0
)

resp$sigma_ext
resp$sigma_sca
resp$sigma_abs
```

## Physical model (plain text)

Drude dielectric function:

epsilon(omega) = epsilon_inf - (omega_p^2) / (omega * (omega + i*gamma))

Rayleigh polarizability:

alpha(omega) = 4*pi*a^3 * (epsilon_p(omega) - epsilon_m) / (epsilon_p(omega) + 2*epsilon_m)

Cross-sections:

sigma_ext = (4*pi/k) * Im(alpha)
sigma_sca = (k^4/(6*pi)) * |alpha|^2
sigma_abs = sigma_ext - sigma_sca

## CRAN submission

This repository provides CI checks and source tarball generation.
CRAN upload is done manually via:

https://cran.r-project.org/submit.html
