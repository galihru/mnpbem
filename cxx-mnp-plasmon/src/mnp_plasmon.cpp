#include "mnp_plasmon.hpp"
#include <iostream>
#include <iomanip>
#include <algorithm>

namespace mnp {

// Material database definition
const std::vector<Material> MnpPlasmon::MATERIALS = {
    {"Au", 3.106, 0.0132, 8.90},
    {"Ag", 3.810, 0.0048, 3.91},
    {"Al", 14.83, 0.098, 1.24}
};

std::vector<Material> MnpPlasmon::material_list() {
    return MATERIALS;
}

bool MnpPlasmon::material_exists(const std::string& name) {
    return std::any_of(MATERIALS.begin(), MATERIALS.end(),
        [&name](const Material& m) { return m.name == name; });
}

Material MnpPlasmon::material_get(const std::string& name) {
    auto it = std::find_if(MATERIALS.begin(), MATERIALS.end(),
        [&name](const Material& m) { return m.name == name; });
    
    if (it != MATERIALS.end()) {
        return *it;
    }
    throw std::invalid_argument("Material not found: " + name);
}

double MnpPlasmon::wavelength_to_energy(double wavelength_nm) {
    return HC_EV_NM / wavelength_nm;
}

complex MnpPlasmon::drude_epsilon(const std::string& material, double wavelength_nm) {
    if (!material_exists(material)) {
        throw std::invalid_argument("Unknown material: " + material);
    }
    
    Material mat = material_get(material);
    double omega = wavelength_to_energy(wavelength_nm);
    
    // omega^2
    double omega_sq = omega * omega;
    
    // i*gamma*omega
    complex damping(0.0, omega * mat.gamma);
    
    // omega_p^2 / (omega^2 + i*gamma*omega)
    complex denominator = omega_sq + damping;
    complex drude_term = (mat.omega_p * mat.omega_p) / denominator;
    
    return complex(mat.eps_inf, 0.0) - drude_term;
}

complex MnpPlasmon::constant_epsilon(double n_squared) {
    return complex(n_squared, 0.0);
}

double MnpPlasmon::complex_magnitude(complex c) {
    return std::abs(c);
}

double MnpPlasmon::complex_magnitude_sq(complex c) {
    return std::norm(c);
}

complex MnpPlasmon::rayleigh_polarizability(
    double radius_nm,
    complex eps_particle,
    complex eps_medium
) {
    // 4*pi*a^3
    double volume_factor = 4.0 * PI * radius_nm * radius_nm * radius_nm;
    
    // (eps_p - eps_m) / (eps_p + 2*eps_m)
    complex numerator = eps_particle - eps_medium;
    complex denominator = eps_particle + 2.0 * eps_medium;
    
    if (complex_magnitude(denominator) < 1e-10) {
        return complex(0.0, 0.0);
    }
    
    return volume_factor * numerator / denominator;
}

double MnpPlasmon::wave_vector(double wavelength_nm, double n_medium) {
    return 2.0 * PI * n_medium / wavelength_nm;
}

CrossSections MnpPlasmon::rayleigh_cross_sections(
    double wavelength_nm,
    double radius_nm,
    complex eps_particle,
    complex eps_medium
) {
    CrossSections sections;
    
    complex alpha = rayleigh_polarizability(radius_nm, eps_particle, eps_medium);
    double k = wave_vector(wavelength_nm, eps_medium.real());
    
    double k_pow4 = k * k * k * k;
    double alpha_mag_sq = complex_magnitude_sq(alpha);
    double alpha_im = alpha.imag();
    
    sections.c_ext = k * alpha_im;
    sections.c_sca = (k_pow4 / (6.0 * PI)) * alpha_mag_sq;
    sections.c_abs = sections.c_ext - sections.c_sca;
    
    // Ensure non-negative absorption
    if (sections.c_abs < 0.0) {
        sections.c_abs = 0.0;
    }
    
    return sections;
}

SphereResponse MnpPlasmon::simulate_sphere_response(
    const std::string& material,
    double wavelength_nm,
    double radius_nm,
    double medium_refractive_index
) {
    SphereResponse response;
    
    response.wavelength_nm = wavelength_nm;
    response.radius_nm = radius_nm;
    response.medium_refractive_index = medium_refractive_index;
    
    // Calculate permittivity
    response.epsilon_particle = drude_epsilon(material, wavelength_nm);
    complex eps_medium = constant_epsilon(medium_refractive_index * medium_refractive_index);
    
    // Calculate polarizability
    response.polarizability = rayleigh_polarizability(
        radius_nm,
        response.epsilon_particle,
        eps_medium
    );
    
    // Calculate cross-sections
    CrossSections cs = rayleigh_cross_sections(
        wavelength_nm,
        radius_nm,
        response.epsilon_particle,
        eps_medium
    );
    
    response.c_ext = cs.c_ext;
    response.c_sca = cs.c_sca;
    response.c_abs = cs.c_abs;
    
    return response;
}

void MnpPlasmon::print_response(const SphereResponse& response) {
    std::cout << "=== MNP Plasmon Response ===\n";
    std::cout << std::fixed << std::setprecision(4);
    std::cout << "Wavelength: " << response.wavelength_nm << " nm\n";
    std::cout << "Radius: " << response.radius_nm << " nm\n";
    std::cout << "Medium n: " << response.medium_refractive_index << "\n";
    std::cout << "\nDielectric Function:\n";
    std::cout << "  ε = " << response.epsilon_particle.real() << " + " 
              << response.epsilon_particle.imag() << "i\n";
    std::cout << "\nPolarizability:\n";
    std::cout << std::scientific << std::setprecision(6);
    std::cout << "  α = " << response.polarizability.real() << " + " 
              << response.polarizability.imag() << "i nm³\n";
    std::cout << "\nCross-Sections:\n";
    std::cout << "  C_ext = " << response.c_ext << " nm²\n";
    std::cout << "  C_sca = " << response.c_sca << " nm²\n";
    std::cout << "  C_abs = " << response.c_abs << " nm²\n";
    std::cout << "=============================\n";
}

}  // namespace mnp
