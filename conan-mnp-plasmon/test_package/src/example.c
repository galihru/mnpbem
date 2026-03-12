#include "mnp_plasmon.h"
#include <stdio.h>

int main(void)
{
    sphere_response_t r = mnp_simulate_sphere_response("Au", 550.0, 25.0, 1.0);
    printf("sigma_ext = %.4f nm^2\n", r.c_ext);
    printf("sigma_sca = %.4f nm^2\n", r.c_sca);
    printf("sigma_abs = %.4f nm^2\n", r.c_abs);
    return 0;
}
