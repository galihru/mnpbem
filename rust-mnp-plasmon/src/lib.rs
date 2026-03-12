// MnpPlasmon - Rust implementation for optical response of metallic nanoparticles
// Based on Drude model and Rayleigh approximation
//
// Physical Constants:
// - hc = 1239.84197 eV·nm
// - k_B = 8.617333262 × 10^-5 eV/K
// - π = 3.141592653589793

use num_complex::Complex64;
use std::collections::HashMap;

/// Fundamental constants used in calculations
const HC_EV_NM: f64 = 1239.84197;      // hc in eV·nm
const PI: f64 = std::f64::consts::PI;
const K_B: f64 = 8.617333262e-5;       // Boltzmann constant in eV/K
const ABS_TOLERANCE: f64 = 1e-10;

/// Material properties for Drude model
#[derive(Clone, Debug)]
pub struct Material {
    pub name: String,
    pub omega_p: f64,  // Plasma frequency (eV)
    pub gamma: f64,    // Damping coefficient (eV)
    pub eps_inf: f64,  // High-frequency dielectric constant
}

impl Material {
    pub fn new(name: &str, omega_p: f64, gamma: f64, eps_inf: f64) -> Self {
        Material {
            name: name.to_string(),
            omega_p,
            gamma,
            eps_inf,
        }
    }
}

/// Optical response of a metal sphere
#[derive(Clone, Debug)]
pub struct SphereResponse {
    pub wavelength_nm: f64,
    pub radius_nm: f64,
    pub medium_refractive_index: f64,
    pub eps_particle: Complex64,
    pub polarizability: Complex64,
    pub c_ext: f64,    // Extinction cross-section (nm²)
    pub c_sca: f64,    // Scattering cross-section (nm²)
    pub c_abs: f64,    // Absorption cross-section (nm²)
}

/// Cross-section results
#[derive(Clone, Debug)]
pub struct CrossSections {
    pub c_ext: f64,
    pub c_sca: f64,
    pub c_abs: f64,
}

/// Material database
static MATERIALS_DB: &[(&str, f64, f64, f64)] = &[
    ("Au", 3.106, 0.0132, 8.90),
    ("Ag", 3.810, 0.0048, 3.91),
    ("Al", 14.83, 0.098, 1.24),
];

/// Get list of available materials
pub fn material_list() -> Vec<Material> {
    MATERIALS_DB
        .iter()
        .map(|(name, omega_p, gamma, eps_inf)| Material::new(name, *omega_p, *gamma, *eps_inf))
        .collect()
}

/// Check if material exists in database
pub fn material_exists(name: &str) -> bool {
    MATERIALS_DB.iter().any(|(mat_name, _, _, _)| *mat_name == name)
}

/// Get material from database
pub fn material_get(name: &str) -> Result<Material, String> {
    MATERIALS_DB
        .iter()
        .find(|(mat_name, _, _, _)| *mat_name == name)
        .map(|(n, op, g, e)| Material::new(n, *op, *g, *e))
        .ok_or_else(|| format!("Material not found: {}", name))
}

/// Convert wavelength to photon energy
///
/// # Formula
/// E (eV) = hc / λ (nm)
pub fn wavelength_to_energy(wavelength_nm: f64) -> f64 {
    HC_EV_NM / wavelength_nm
}

/// Convert photon energy to wavelength
///
/// # Formula
/// λ (nm) = hc / E (eV)
pub fn energy_to_wavelength(energy_ev: f64) -> f64 {
    HC_EV_NM / energy_ev
}

/// Calculate Drude dielectric function
///
/// # Formula
/// ε(ω) = ε∞ - ωₚ² / (ω(ω + iγ))
pub fn drude_epsilon(
    material: &str,
    wavelength_nm: f64,
) -> Result<Complex64, String> {
    let material_data = material_get(material)?;
    
    let energy_ev = wavelength_to_energy(wavelength_nm);
    let omega = energy_ev / HC_EV_NM;  // normalize to eV
    
    let numerator = material_data.omega_p.powi(2);
    let denominator = omega * (omega + Complex64::new(0.0, material_data.gamma));
    
    let epsilon = Complex64::new(material_data.eps_inf, 0.0) - numerator / denominator;
    Ok(epsilon)
}

/// Calculate polarizability using Rayleigh approximation
///
/// # Formula
/// α = 4π a³ · (ε_p - ε_m) / (ε_p + 2ε_m)
pub fn rayleigh_polarizability(
    radius_nm: f64,
    eps_particle: Complex64,
    medium_refractive_index: f64,
) -> Complex64 {
    let eps_medium = medium_refractive_index.powi(2);
    let numerator = eps_particle - Complex64::new(eps_medium, 0.0);
    let denominator = eps_particle + Complex64::new(2.0 * eps_medium, 0.0);
    
    let volume = 4.0 / 3.0 * PI * radius_nm.powi(3);
    volume * numerator / denominator
}

/// Calculate extinction cross-section
///
/// # Formula
/// σ_ext = (4π/k) · Im[α]
/// where k = 2π·n_m / λ
pub fn extinction_cross_section(
    wavelength_nm: f64,
    medium_refractive_index: f64,
    polarizability: Complex64,
) -> f64 {
    let k = 2.0 * PI * medium_refractive_index / wavelength_nm;
    (4.0 * PI / k) * polarizability.im.abs()
}

/// Calculate scattering cross-section
///
/// # Formula
/// σ_sca = (k⁴/6π) · |α|²
pub fn scattering_cross_section(
    wavelength_nm: f64,
    medium_refractive_index: f64,
    polarizability: Complex64,
) -> f64 {
    let k = 2.0 * PI * medium_refractive_index / wavelength_nm;
    let k4 = k.powi(4);
    (k4 / (6.0 * PI)) * polarizability.norm_sqr()
}

/// Calculate absorption cross-section
///
/// # Formula
/// σ_abs = σ_ext - σ_sca
pub fn absorption_cross_section(c_ext: f64, c_sca: f64) -> f64 {
    (c_ext - c_sca).max(0.0)
}

/// Calculate optical response of a metal sphere
pub fn sphere_response(
    wavelength_nm: f64,
    radius_nm: f64,
    material: &str,
    medium_refractive_index: f64,
) -> Result<SphereResponse, String> {
    let eps_particle = drude_epsilon(material, wavelength_nm)?;
    let polarizability = rayleigh_polarizability(radius_nm, eps_particle, medium_refractive_index);
    let c_ext = extinction_cross_section(wavelength_nm, medium_refractive_index, polarizability);
    let c_sca = scattering_cross_section(wavelength_nm, medium_refractive_index, polarizability);
    let c_abs = absorption_cross_section(c_ext, c_sca);

    Ok(SphereResponse {
        wavelength_nm,
        radius_nm,
        medium_refractive_index,
        eps_particle,
        polarizability,
        c_ext,
        c_sca,
        c_abs,
    })
}

/// Calculate cross-sections for a range of wavelengths
pub fn wavelength_scan(
    start_wavelength_nm: f64,
    end_wavelength_nm: f64,
    num_points: usize,
    radius_nm: f64,
    material: &str,
    medium_refractive_index: f64,
) -> Result<Vec<SphereResponse>, String> {
    if num_points < 2 {
        return Err("num_points must be >= 2".to_string());
    }

    let mut results = Vec::with_capacity(num_points);
    let step = (end_wavelength_nm - start_wavelength_nm) / (num_points - 1) as f64;

    for i in 0..num_points {
        let wavelength = start_wavelength_nm + step * i as f64;
        let response = sphere_response(wavelength, radius_nm, material, medium_refractive_index)?;
        results.push(response);
    }

    Ok(results)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_material_exists() {
        assert!(material_exists("Au"));
        assert!(material_exists("Ag"));
        assert!(material_exists("Al"));
        assert!(!material_exists("Cu"));
    }

    #[test]
    fn test_wavelength_energy_conversion() {
        let wavelength = 550.0; // nm
        let energy = wavelength_to_energy(wavelength);
        let wavelength_back = energy_to_wavelength(energy);
        
        assert!((wavelength - wavelength_back).abs() < 1e-6);
    }

    #[test]
    fn test_material_get() {
        let material = material_get("Au").unwrap();
        assert_eq!(material.name, "Au");
        assert!((material.omega_p - 3.106).abs() < 1e-3);
    }

    #[test]
    fn test_sphere_response_au() {
        let response = sphere_response(550.0, 25.0, "Au", 1.0).unwrap();
        assert!(response.c_ext > 0.0);
        assert!(response.c_sca > 0.0);
        assert!(response.c_abs > 0.0);
        assert!(response.c_abs < response.c_ext);
    }
}
