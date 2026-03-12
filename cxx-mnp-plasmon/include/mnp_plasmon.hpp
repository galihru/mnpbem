#pragma once

#include <complex>
#include <string>
#include <vector>
#include <stdexcept>
#include <cmath>

namespace mnp {

using complex = std::complex<double>;

/**
 * Material structure for Drude model parameters
 */
struct Material {
    std::string name;
    double omega_p;      // Plasma frequency (eV)
    double gamma;        // Damping coefficient (eV)
    double eps_inf;      // High-frequency dielectric constant
};

/**
 * Output structure for sphere response
 */
struct SphereResponse {
    double wavelength_nm;
    double radius_nm;
    double medium_refractive_index;
    complex epsilon_particle;
    complex polarizability;
    double c_ext;        // Extinction cross-section
    double c_sca;        // Scattering cross-section
    double c_abs;        // Absorption cross-section
};

/**
 * Cross-section result
 */
struct CrossSections {
    double c_ext;
    double c_sca;
    double c_abs;
};

/**
 * MnpPlasmon - C++ implementation
 */
class MnpPlasmon {
public:
    // Constants
    static constexpr double HC_EV_NM = 1239.84197;  // hc in eV·nm
    static constexpr double PI = 3.141592653589793;
    
    // Material database
    static std::vector<Material> material_list();
    static bool material_exists(const std::string& name);
    static Material material_get(const std::string& name);
    
    // Dielectric functions
    static complex drude_epsilon(const std::string& material, double wavelength_nm);
    static complex constant_epsilon(double n_squared);
    
    // Rayleigh theory
    static complex rayleigh_polarizability(
        double radius_nm,
        complex eps_particle,
        complex eps_medium
    );
    
    static CrossSections rayleigh_cross_sections(
        double wavelength_nm,
        double radius_nm,
        complex eps_particle,
        complex eps_medium
    );
    
    // High-level API
    static SphereResponse simulate_sphere_response(
        const std::string& material,
        double wavelength_nm,
        double radius_nm,
        double medium_refractive_index
    );
    
    // Utilities
    static void print_response(const SphereResponse& response);

private:
    static const std::vector<Material> MATERIALS;
    
    static double wavelength_to_energy(double wavelength_nm);
    static double complex_magnitude(complex c);
    static double complex_magnitude_sq(complex c);
    static double wave_vector(double wavelength_nm, double n_medium);
};

}  // namespace mnp
