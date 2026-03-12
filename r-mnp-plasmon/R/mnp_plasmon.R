# Material database
.materials <- data.frame(
  name = c("Au", "Ag", "Al"),
  omega_p = c(3.106, 3.810, 14.83),
  gamma = c(0.0132, 0.0048, 0.098),
  eps_inf = c(8.90, 3.91, 1.24),
  stringsAsFactors = FALSE
)

#' List supported materials
#' @return Character vector of supported material names.
material_list <- function() {
  .materials$name
}

#' Check if material exists
#' @param material Material name.
#' @return Logical.
material_exists <- function(material) {
  material %in% .materials$name
}

#' Compute Drude dielectric function
#' @param material Material name (Au, Ag, Al).
#' @param wavelength_nm Wavelength in nm.
#' @return Complex dielectric value.
drude_epsilon <- function(material, wavelength_nm) {
  if (!material_exists(material)) {
    stop(sprintf("Unknown material: %s", material))
  }
  if (!is.numeric(wavelength_nm) || wavelength_nm <= 0) {
    stop("wavelength_nm must be positive")
  }

  hc_ev_nm <- 1239.84197
  row <- .materials[.materials$name == material, ]

  omega <- hc_ev_nm / wavelength_nm
  eps_inf <- row$eps_inf
  omega_p <- row$omega_p
  gamma <- row$gamma

  eps_inf - (omega_p^2) / (omega * (omega + 1i * gamma))
}

#' Rayleigh polarizability for a sphere
#' @param radius_nm Sphere radius in nm.
#' @param eps_particle Complex particle dielectric function.
#' @param medium_refractive_index Medium refractive index.
#' @return Complex polarizability.
rayleigh_polarizability <- function(radius_nm, eps_particle, medium_refractive_index = 1.0) {
  if (!is.numeric(radius_nm) || radius_nm <= 0) {
    stop("radius_nm must be positive")
  }

  eps_m <- medium_refractive_index^2
  volume <- (4.0 / 3.0) * pi * radius_nm^3
  volume * (eps_particle - eps_m) / (eps_particle + 2 * eps_m)
}

#' Optical response of a spherical nanoparticle
#' @param wavelength_nm Wavelength in nm.
#' @param radius_nm Sphere radius in nm.
#' @param material Material name (Au, Ag, Al).
#' @param medium_refractive_index Medium refractive index.
#' @return Named list with epsilon, polarizability, and cross-sections.
sphere_response <- function(wavelength_nm, radius_nm, material, medium_refractive_index = 1.0) {
  eps_particle <- drude_epsilon(material, wavelength_nm)
  alpha <- rayleigh_polarizability(radius_nm, eps_particle, medium_refractive_index)

  k <- 2 * pi * medium_refractive_index / wavelength_nm
  sigma_ext <- (4 * pi / k) * Im(alpha)
  sigma_sca <- (k^4 / (6 * pi)) * Mod(alpha)^2
  sigma_abs <- max(0, sigma_ext - sigma_sca)

  list(
    wavelength_nm = wavelength_nm,
    radius_nm = radius_nm,
    material = material,
    epsilon = eps_particle,
    polarizability = alpha,
    sigma_ext = sigma_ext,
    sigma_sca = sigma_sca,
    sigma_abs = sigma_abs
  )
}
