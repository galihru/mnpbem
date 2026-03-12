#include <stdio.h>
#include "../src/mnp_plasmon.h"

int main(void) {
    printf("=== MNP Plasmon C Demo ===\n\n");
    
    /* List available materials */
    int count;
    const char **materials = mnp_material_list(&count);
    printf("Available materials:\n");
    for (int i = 0; i < count; i++) {
        printf("  - %s\n", materials[i]);
    }
    printf("\n");
    
    /* Simulate Au nanoparticle response at different wavelengths */
    double wavelengths[] = {400.0, 500.0, 550.0, 600.0, 700.0};
    
    printf("Au nanoparticle (r=20nm) in water (n=1.33):\n");
    printf("Wavelength(nm)  C_ext(nm²)   C_sca(nm²)   C_abs(nm²)\n");
    printf("%-15s  %-12s  %-12s  %-12s\n", "---", "---", "---", "---");
    
    for (int i = 0; i < 5; i++) {
        sphere_response_t response = mnp_simulate_sphere_response(
            "Au", wavelengths[i], 20.0, 1.33
        );
        printf("%-15.1f  %-12.4e  %-12.4e  %-12.4e\n",
            response.wavelength_nm,
            response.c_ext,
            response.c_sca,
            response.c_abs
        );
    }
    
    printf("\n");
    
    /* Detailed response at resonance */
    sphere_response_t response = mnp_simulate_sphere_response("Au", 550.0, 20.0, 1.33);
    mnp_print_response(&response);
    
    return 0;
}
