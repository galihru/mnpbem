#include "../src/mnp_plasmon.h"
#include <stdio.h>

int main(void) {
    FILE *fp = fopen("docs/example-data/c.csv", "w");
    if (!fp) {
        return 1;
    }

    fprintf(fp, "wavelength_nm,c_ext,c_sca,c_abs\n");
    for (int wl = 400; wl <= 700; wl += 5) {
        sphere_response_t r = mnp_simulate_sphere_response("Au", (double)wl, 25.0, 1.33);
        fprintf(fp, "%d,%.12g,%.12g,%.12g\n", wl, r.c_ext, r.c_sca, r.c_abs);
    }

    fclose(fp);
    return 0;
}
