#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include "mnp_plasmon.h"

void test_material_list(void) {
    printf("Test: material_list\n");
    int count;
    const char **materials = mnp_material_list(&count);
    assert(count == 3);
    assert(strcmp(materials[0], "Au") == 0);
    assert(strcmp(materials[1], "Ag") == 0);
    assert(strcmp(materials[2], "Al") == 0);
    printf("  PASS\n");
}

void test_material_exists(void) {
    printf("Test: material_exists\n");
    assert(mnp_material_exists("Au") == 1);
    assert(mnp_material_exists("Ag") == 1);
    assert(mnp_material_exists("Al") == 1);
    assert(mnp_material_exists("Cu") == 0);
    printf("  PASS\n");
}

void test_drude_epsilon(void) {
    printf("Test: drude_epsilon\n");
    complex_t eps = mnp_drude_epsilon("Au", 550.0);
    double re = creal(eps);
    double im = cimag(eps);
    /* Au at 550nm should have real part near -5 to -10 and positive Im */
    assert(re < 0.0);
    assert(im > 0.0);
    printf("  Au@550nm: ε = %.4f + %.4fi\n", re, im);
    printf("  PASS\n");
}

void test_cross_sections_positive(void) {
    printf("Test: cross_sections_positive\n");
    sphere_response_t response = mnp_simulate_sphere_response(
        "Au", 550.0, 20.0, 1.33
    );
    assert(response.c_ext >= 0.0);
    assert(response.c_sca >= 0.0);
    assert(response.c_abs >= 0.0);
    assert(response.c_ext >= response.c_sca);  /* C_ext >= C_sca */
    printf("  PASS\n");
}

void test_simulate_response(void) {
    printf("Test: simulate_response\n");
    sphere_response_t response = mnp_simulate_sphere_response(
        "Au", 550.0, 20.0, 1.33
    );
    assert(response.wavelength_nm == 550.0);
    assert(response.radius_nm == 20.0);
    assert(response.medium_refractive_index == 1.33);
    assert(cabs(response.epsilon_particle) > 0.0);
    assert(cabs(response.polarizability) > 0.0);
    printf("  PASS\n");
}

int main(void) {
    printf("=== MNP Plasmon C Tests ===\n\n");
    
    test_material_list();
    test_material_exists();
    test_drude_epsilon();
    test_cross_sections_positive();
    test_simulate_response();
    
    printf("\n=== All tests passed! ===\n");
    return 0;
}
