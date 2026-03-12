"""
    MnpPlasmon

Julia implementation of the Drude dielectric model and Rayleigh quasi-static
approximation for computing optical cross-sections of metallic nanoparticles.

Physical model
--------------
Drude permittivity:
    ε(ω) = ε∞ - ωₚ² / [ω(ω + iγ)]

Rayleigh polarizability (a ≪ λ):
    α(ω) = 4πa³ · (εₚ - εₘ) / (εₚ + 2εₘ)

Optical cross-sections:
    σ_ext = (4π/k) · Im[α(ω)]
    σ_sca = (k⁴/6π) · |α(ω)|²
    σ_abs = σ_ext - σ_sca

where k = 2πnₘ/λ.
"""
module MnpPlasmon

# ---------------------------------------------------------------------------
# Material database  (omega_p [eV], gamma [eV], eps_inf)
# ---------------------------------------------------------------------------
const MATERIALS = Dict{String,Tuple{Float64,Float64,Float64}}(
    "Au" => (3.106,  0.0132, 8.90),
    "Ag" => (3.810,  0.0048, 3.91),
    "Al" => (14.83,  0.0980, 1.24),
)

# ---------------------------------------------------------------------------
# Result type
# ---------------------------------------------------------------------------
struct SphereResponse
    c_ext::Float64   # extinction cross-section  [nm²]
    c_sca::Float64   # scattering cross-section  [nm²]
    c_abs::Float64   # absorption cross-section  [nm²]
end

# ---------------------------------------------------------------------------
# Core functions
# ---------------------------------------------------------------------------

"""
    drude_epsilon(omega, material) -> Complex{Float64}

Compute the Drude dielectric function at angular frequency `omega` (eV).
"""
function drude_epsilon(omega::Float64, material::String)::Complex{Float64}
    haskey(MATERIALS, material) || throw(ArgumentError("Unknown material: $material"))
    omega_p, gamma, eps_inf = MATERIALS[material]
    return Complex{Float64}(eps_inf) - omega_p^2 / (omega * (omega + im * gamma))
end

"""
    sphere_response(wavelength_nm, radius_nm, material[, medium_n]) -> SphereResponse

Compute extinction, scattering, and absorption cross-sections (nm²) for a
spherical nanoparticle using the Rayleigh quasi-static approximation.

# Arguments
- `wavelength_nm`: Incident wavelength in nanometres.
- `radius_nm`:     Sphere radius in nanometres (must satisfy radius ≪ wavelength).
- `material`:      Material key — `"Au"`, `"Ag"`, or `"Al"`.
- `medium_n`:      Real refractive index of the surrounding medium (default 1.0).

# Returns
A `SphereResponse` with fields `c_ext`, `c_sca`, `c_abs` in nm².
"""
function sphere_response(
    wavelength_nm::Float64,
    radius_nm::Float64,
    material::String,
    medium_n::Float64 = 1.0,
)::SphereResponse
    # Photon energy from wavelength: E = hc/λ  (eV·nm / nm)
    omega = 1239.84197 / wavelength_nm

    eps_m = Complex{Float64}(medium_n^2)
    eps_p = drude_epsilon(omega, material)

    # Rayleigh polarizability
    alpha = 4π * radius_nm^3 * (eps_p - eps_m) / (eps_p + 2 * eps_m)

    # Wave vector magnitude in medium
    k = 2π * medium_n / wavelength_nm

    c_ext = (4π / k) * imag(alpha)
    c_sca = (k^4 / (6π)) * abs2(alpha)
    c_abs = c_ext - c_sca

    return SphereResponse(c_ext, c_sca, c_abs)
end

export MATERIALS, SphereResponse, drude_epsilon, sphere_response

end  # module MnpPlasmon
