#ifndef MNP_PLASMON_H
#define MNP_PLASMON_H

#include <stdint.h>
#include <math.h>

/**
 * MNP Plasmon - C Library for Metallic Nanoparticle Optical Response
 * Calculates Drude-model dielectric function and Rayleigh polarizability
 * for spherical metallic nanoparticles in arbitrary dielectric media.
 */

/* Complex number structure and operations */
typedef struct
{
    double real;
    double imag;
} complex_t;

/* Complex number operations */
static inline complex_t complex_new(double real, double imag)
{
    complex_t c;
    c.real = real;
    c.imag = imag;
    return c;
}

static inline complex_t complex_add(complex_t a, complex_t b)
{
    return complex_new(a.real + b.real, a.imag + b.imag);
}

static inline complex_t complex_sub(complex_t a, complex_t b)
{
    return complex_new(a.real - b.real, a.imag - b.imag);
}

static inline complex_t complex_mul(complex_t a, complex_t b)
{
    return complex_new(a.real * b.real - a.imag * b.imag,
                       a.real * b.imag + a.imag * b.real);
}

static inline complex_t complex_div(complex_t a, complex_t b)
{
    double denom = b.real * b.real + b.imag * b.imag;
    if (denom == 0.0)
        return complex_new(0.0, 0.0);
    return complex_new((a.real * b.real + a.imag * b.imag) / denom,
                       (a.imag * b.real - a.real * b.imag) / denom);
}

static inline double complex_abs(complex_t c)
{
    return sqrt(c.real * c.real + c.imag * c.imag);
}

static inline double complex_abs_sq(complex_t c)
{
    return c.real * c.real + c.imag * c.imag;
}

/* Output structure for sphere response */
typedef struct
{
    double wavelength_nm;
    double radius_nm;
    double medium_refractive_index;
    complex_t epsilon_particle;
    complex_t polarizability;
    double c_ext; /* Extinction cross-section (nm^2) */
    double c_sca; /* Scattering cross-section (nm^2) */
    double c_abs; /* Absorption cross-section (nm^2) */
} sphere_response_t;

/* Material structure for Drude model parameters */
typedef struct
{
    const char *name;
    double omega_p; /* Plasma frequency (eV) */
    double gamma;   /* Damping coefficient (eV) */
    double eps_inf; /* High-frequency dielectric constant */
} material_t;

/* Material database functions */
const char **mnp_material_list(int *count);
int mnp_material_exists(const char *name);
material_t mnp_material_get(const char *name);

/* Drude model */
complex_t mnp_drude_epsilon(const char *material, double wavelength_nm);
complex_t mnp_constant_epsilon(double n_squared);

/* Rayleigh polarizability */
complex_t mnp_rayleigh_polarizability(
    double radius_nm,
    complex_t eps_particle,
    complex_t eps_medium);

/* Cross-section calculations */
typedef struct
{
    double c_ext;
    double c_sca;
    double c_abs;
} cross_sections_t;

cross_sections_t mnp_rayleigh_cross_sections(
    double wavelength_nm,
    double radius_nm,
    complex_t eps_particle,
    complex_t eps_medium);

/* High-level API */
sphere_response_t mnp_simulate_sphere_response(
    const char *material,
    double wavelength_nm,
    double radius_nm,
    double medium_refractive_index);

/* Utility */
void mnp_print_response(const sphere_response_t *response);

#endif /* MNP_PLASMON_H */
