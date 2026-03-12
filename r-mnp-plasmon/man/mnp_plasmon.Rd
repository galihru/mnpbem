\name{mnpPlasmonR}
\alias{material_list}
\alias{material_exists}
\alias{drude_epsilon}
\alias{rayleigh_polarizability}
\alias{sphere_response}
\title{MnpPlasmon R API}
\description{Functions for Drude dielectric model and Rayleigh optical response of metallic nanoparticles.}
\usage{
material_list()
material_exists(material)
drude_epsilon(material, wavelength_nm)
rayleigh_polarizability(radius_nm, eps_particle, medium_refractive_index = 1.0)
sphere_response(wavelength_nm, radius_nm, material, medium_refractive_index = 1.0)
}
\arguments{
  \item{material}{Material name, one of \code{"Au"}, \code{"Ag"}, \code{"Al"}.}
  \item{wavelength_nm}{Wavelength in nanometers.}
  \item{radius_nm}{Sphere radius in nanometers.}
  \item{eps_particle}{Complex dielectric value for particle.}
  \item{medium_refractive_index}{Refractive index of medium (default 1.0).}
}
\value{
\code{material_list()} returns character vector.\cr
\code{material_exists()} returns logical.\cr
\code{drude_epsilon()} and \code{rayleigh_polarizability()} return complex values.\cr
\code{sphere_response()} returns named list with \code{sigma_ext}, \code{sigma_sca}, \code{sigma_abs}.
}
\examples{
material_list()
material_exists("Au")

eps <- drude_epsilon("Au", 550)
resp <- sphere_response(550, 25, "Au", 1.0)
resp$sigma_ext
}
