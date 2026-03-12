#lang scribble/manual

@require[scribble/example
         (for-label racket/base racket/contract)]

@title{MNP Plasmon: Nanoparticle Electromagnetic Response}

@author{@author+email["Galih Ridho Utomo" "g4lihru@students.unnes.ac.id"]}

@defmodule[mnp-plasmon]

This package provides integrated computational tools for single-nanoparticle
electromagnetic response in the Rayleigh quasi-static limit. It composes:

@itemlist[
  @item{Drude-model dielectric function for noble metals (Au, Ag, Al)}
  @item{Rayleigh polarizability calculation}
  @item{Optical cross-sections (extinction, scattering, absorption)}
]

@section{Physical Foundation}

For a metallic nanoparticle of radius @italic{a} in a dielectric medium:

@itemlist[
  @item{@bold{Drude permittivity}: 
        @math{ε(ω) = ε_∞ - ω_p² / [ω(ω + iγ)]}}
  @item{@bold{Rayleigh polarizability}:
        @math{α = 4πa³(ε_p - ε_m) / (ε_p + 2ε_m)}}
  @item{@bold{Cross-sections}:
        @math{C_ext = k Im(α)},
        @math{C_sca = |k|⁴|α|² / (6π)},
        @math{C_abs = C_ext - C_sca}}
]

@section{Material Database}

Available materials with Drude parameters:

@itemlist[
  @item{@bold{Au} (Gold): ωp = 3.106 eV, γ = 0.0132 eV}
  @item{@bold{Ag} (Silver): ωp = 3.810 eV, γ = 0.0048 eV}
  @item{@bold{Al} (Aluminum): ωp = 14.83 eV, γ = 0.098 eV}
]

@defproc[(material-list)
         (listof string?)]{
Return list of available material names: @racket{("Au" "Ag" "Al")}.
}

@defproc[(get-drude-params [material string?])
         (or/c (list string? real? real? real?) #f)]{
Retrieve Drude parameters @racket{(list name omega_p gamma eps_inf)} for a material.
Returns @racket{#f} if material not found.
}

@section{Core Functions}

@defproc[(drude-epsilon [material string?]
                        [wavelength-nm real?])
         (values real? real?)]{
Compute complex permittivity @math{ε(ω)} via the Drude free-electron model.

@itemlist[
  @item{@racket[material]: One of @racket["Au"], @racket["Ag"], @racket["Al"]}
  @item{@racket[wavelength-nm]: Wavelength in nanometers}
  @item{@bold{Returns}: @racket[(values real-part imag-part)]}
]

@examples[
  (drude-epsilon "Au" 550.0)
]
}

@defproc[(constant-epsilon [n-squared real?]
                           [wavelength-nm real?])
         real?]{
Return permittivity of a non-absorbing dielectric with refractive index @math{n}.
The wavelength argument is ignored (constant permittivity model).

@racket[n-squared] should be @racket[(* n n)] where @italic{n} is the refractive index.
}

@defproc[(rayleigh-polarizability [radius-nm real?]
                                   [eps-particle (list/c real? real?)]
                                   [eps-medium (list/c real? real?)])
         (values real? real?)]{
Compute the complex polarizability @math{α} in the Rayleigh quasi-static limit.

@itemlist[
  @item{@racket[radius-nm]: Particle radius in nanometers}
  @item{@racket[eps-particle]: Complex permittivity of particle as @racket[(list real imag)]}
  @item{@racket[eps-medium]: Complex permittivity of surrounding medium}
  @item{@bold{Returns}: @racket[(values real imag)] components of @math{α} in nm³}
]
}

@defproc[(rayleigh-cross-sections [wavelength-nm real?]
                                  [radius-nm real?]
                                  [eps-particle (list/c real? real?)]
                                  [eps-medium (list/c real? real?)])
         (values real? real? real?)]{
Compute extinction, scattering, and absorption cross-sections.

@itemlist[
  @item{@bold{Returns}: @racket[(values c_ext c_sca c_abs)]} in nm²}
]
}

@section{High-Level API}

@defproc[(simulate-sphere-response [#:material material string?]
                                   [#:wavelength-nm wl real?]
                                   [#:radius-nm radius real?]
                                   [#:medium-n n real?])
         (list/c symbol? any? ...)]{
Unified interface for complete nanoparticle simulation.
Computes Drude permittivity, polarizability, and cross-sections in one call.

@itemlist[
  @item{@racket[#:material]: Material name (@racket["Au"], @racket["Ag"], @racket["Al"])}
  @item{@racket[#:wavelength-nm]: Illumination wavelength in nm}
  @item{@racket[#:radius-nm]: Nanoparticle radius in nm}
  @item{@racket[#:medium-n]: Refractive index of surrounding medium (default water: 1.33)}
]

@bold{Returns:} Property list with keys:
@itemlist[
  @item{@racket['material], @racket['wavelength-nm], @racket['radius-nm], @racket['medium-n]}
  @item{@racket['epsilon-particle]: @racket[(list real imag)]}
  @item{@racket['polarizability]: @racket[(list real imag)]}
  @item{@racket['c-ext], @racket['c-sca], @racket['c-abs]: cross-sections in nm²}
]

@examples[
  (simulate-sphere-response
    #:material "Au"
    #:wavelength-nm 550
    #:radius-nm 20
    #:medium-n 1.33)
]
}

@section{Example}

@codeblock{
#lang racket
(require mnp-plasmon)

(define result
  (simulate-sphere-response
    #:material "Au"
    #:wavelength-nm 550
    #:radius-nm 20
    #:medium-n 1.33))

(displayln (cadr (assoc 'c-ext result)))  ; prints extinction cross-section
}

@section{References}

@itemlist[
  @item{Bohren, C. F., & Huffman, D. R. (1983). 
        @italic{Absorption and scattering of light by small particles}.
        Wiley.}
  @item{Eustis, S., & El-Sayed, M. A. (2006).
        Why gold nanoparticles are more precious than pretty gold.
        @italic{Chemical Society Reviews}, 35(3), 209–217.}
]
