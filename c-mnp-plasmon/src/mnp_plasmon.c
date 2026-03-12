#include "mnp_plasmon.h"
#include <stdio.h>
#include <string.h>

/* Material database */
static const material_t MATERIALS[] = {
    {"Au", 3.106, 0.0132, 8.90},
    {"Ag", 3.810, 0.0048, 3.91},
    {"Al", 14.83, 0.098, 1.24}
};
static const int MATERIAL_COUNT = 3;

/* Constants */
#define HC_EV_NM 1239.84197  /* hc in eV·nm */
#define PI 3.141592653589793
#define K_B 8.617333262e-5   /* Boltzmann constant in eV/K */
#define ABS_TOLERANCE 1e-10

/**
 * Get list of available materials
 */
const char **mnp_material_list(int *count) {
    static const char *names[] = {"Au", "Ag", "Al"};
    *count = MATERIAL_COUNT;
    return names;
}

/**
 * Check if material exists in database
 */
int mnp_material_exists(const char *name) {
    for (int i = 0; i < MATERIAL_COUNT; i++) {
        if (strcmp(MATERIALS[i].name, name) == 0) {
            return 1;
        }
    }
    return 0;
}

/**
 * Get material from database
 */
material_t mnp_material_get(const char *name) {
    for (int i = 0; i < MATERIAL_COUNT; i++) {
        if (strcmp(MATERIALS[i].name, name) == 0) {
            return MATERIALS[i];
        }
    }
    /* Return empty material if not found */
    material_t empty = {NULL, 0.0, 0.0, 0.0};
    return empty;
}

/**
 * Calculate omega from wavelength in nm
 * omega (eV) = hc(eV·nm) / wavelength(nm)
 */
static double wavelength_to_energy(double wavelength_nm) {
    return HC_EV_NM / wavelength_nm;
}

/**
 * Drude model: epsilon(omega) = eps_inf - omega_p^2 / (omega^2 + i*gamma*omega)
 */
complex_t mnp_drude_epsilon(const char *material, double wavelength_nm) {
    if (!mnp_material_exists(material)) {
        return complex_new(0.0, 0.0);
    }
    
    material_t mat = mnp_material_get(material);
    double omega = wavelength_to_energy(wavelength_nm);
    
    /* omega^2 */
    double omega_sq = omega * omega;
    
    /* i*gamma*omega */
    complex_t damping = complex_new(0.0, omega * mat.gamma);
    
    /* omega^2 + i*gamma*omega */
    complex_t denominator = complex_new(omega_sq, 0.0);
    denominator = complex_add(denominator, damping);
    
    /* omega_p^2 */
    double omega_p_sq = mat.omega_p * mat.omega_p;
    
    /* omega_p^2 / (omega^2 + i*gamma*omega) */
    complex_t drude_term = complex_div(complex_new(omega_p_sq, 0.0), denominator);
    
    /* eps_inf - drude_term */
    return complex_sub(complex_new(mat.eps_inf, 0.0), drude_term);
}

/**
 * Constant permittivity (non-absorbing dielectric)
 * epsilon = n^2
 */
complex_t mnp_constant_epsilon(double n_squared) {
    return complex_new(n_squared, 0.0);
}

/**
 * Complex magnitude
 */
static double complex_magnitude(complex_t c) {
    return complex_abs(c);
}

/**
 * Complex magnitude squared
 */
static double complex_magnitude_sq(complex_t c) {
    return complex_abs_sq(c);
}

/**
 * Rayleigh polarizability
 * alpha = 4*pi*a^3 * (eps_p - eps_m) / (eps_p + 2*eps_m)
 * where a is radius in nm
 */
complex_t mnp_rayleigh_polarizability(
    double radius_nm,
    complex_t eps_particle,
    complex_t eps_medium
) {
    /* 4*pi*a^3 */
    double volume_factor = 4.0 * PI * radius_nm * radius_nm * radius_nm;
    
    /* (eps_p - eps_m) / (eps_p + 2*eps_m) */
    complex_t numerator = complex_sub(eps_particle, eps_medium);
    
    /* eps_p + 2*eps_m */
    complex_t two_eps_m = complex_new(2.0 * eps_medium.real, 2.0 * eps_medium.imag);
    complex_t denominator = complex_add(eps_particle, two_eps_m);
    
    if (complex_abs(denominator) < ABS_TOLERANCE) {
        return complex_new(0.0, 0.0);
    }
    
    complex_t result = complex_div(numerator, denominator);
    return complex_new(volume_factor * result.real, volume_factor * result.imag);
}

/**
 * Wave vector k = 2*pi*n_medium / wavelength_nm
 */
static double wave_vector(double wavelength_nm, double n_medium) {
    return 2.0 * PI * n_medium / wavelength_nm;
}

/**
 * Rayleigh cross-sections
 * C_ext = k * Im(alpha)
 * C_sca = |k|^4 / (6*pi) * |alpha|^2
 * C_abs = C_ext - C_sca
 */
cross_sections_t mnp_rayleigh_cross_sections(
    double wavelength_nm,
    double radius_nm,
    complex_t eps_particle,
    complex_t eps_medium
) {
    cross_sections_t sections;
    
    complex_t alpha = mnp_rayleigh_polarizability(radius_nm, eps_particle, eps_medium);
    double k = wave_vector(wavelength_nm, eps_medium.real);
    
    double k_pow4 = k * k * k * k;
    double alpha_mag_sq = complex_abs_sq(alpha);
    double alpha_im = alpha.imag;
    
    sections.c_ext = k * alpha_im;
    sections.c_sca = (k_pow4 / (6.0 * PI)) * alpha_mag_sq;
    sections.c_abs = sections.c_ext - sections.c_sca;
    
    /* Ensure non-negative absorption */
    if (sections.c_abs < 0.0) {
        sections.c_abs = 0.0;
    }
    
    return sections;
}

/**
 * High-level API: simulate sphere optical response
 */
sphere_response_t mnp_simulate_sphere_response(
    const char *material,
    double wavelength_nm,
    double radius_nm,
    double medium_refractive_index
) {
    sphere_response_t response = {0};
    
    response.wavelength_nm = wavelength_nm;
    response.radius_nm = radius_nm;
    response.medium_refractive_index = medium_refractive_index;
    
    /* Calculate permittivity */
    response.epsilon_particle = mnp_drude_epsilon(material, wavelength_nm);
    complex_t eps_medium = mnp_constant_epsilon(medium_refractive_index * medium_refractive_index);
    
    /* Calculate polarizability */
    response.polarizability = mnp_rayleigh_polarizability(
        radius_nm,
        response.epsilon_particle,
        eps_medium
    );
    
    /* Calculate cross-sections */
    cross_sections_t cs = mnp_rayleigh_cross_sections(
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

/**
 * Pretty-print response structure
 */
void mnp_print_response(const sphere_response_t *response) {
    if (!response) return;
    
    printf("=== MNP Plasmon Response ===\n");
    printf("Wavelength: %.2f nm\n", response->wavelength_nm);
    printf("Radius: %.2f nm\n", response->radius_nm);
    printf("Medium n: %.4f\n", response->medium_refractive_index);
    printf("\nDielectric Function:\n");
    printf("  epsilon = %.6f + %.6fi\n", 
        response->epsilon_particle.real, 
        response->epsilon_particle.imag);
    printf("\nPolarizability:\n");
    printf("  alpha = %.6e + %.6ei nm^3\n", 
        response->polarizability.real, 
        response->polarizability.imag);
    printf("\nCross-Sections:\n");
    printf("  C_ext = %.6e nm^2\n", response->c_ext);
    printf("  C_sca = %.6e nm^2\n", response->c_sca);
    printf("  C_abs = %.6e nm^2\n", response->c_abs);
    printf("=============================\n");
}
