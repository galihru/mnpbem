#include "mnp_plasmon.hpp"
#include <iostream>
#include <vector>
#include <iomanip>

using namespace mnp;

int main() {
    std::cout << "=== MNP Plasmon C++ Demo ===\n\n";
    
    // List available materials
    auto materials = MnpPlasmon::material_list();
    std::cout << "Available materials:\n";
    for (const auto& mat : materials) {
        std::cout << "  - " << mat.name << "\n";
    }
    std::cout << "\n";
    
    // Simulate Au nanoparticle response at different wavelengths
    double wavelengths[] = {400.0, 500.0, 550.0, 600.0, 700.0};
    
    std::cout << "Au nanoparticle (r=20nm) in water (n=1.33):\n";
    std::cout << std::left << std::setw(15) << "Wavelength(nm)"
              << std::setw(15) << "C_ext(nm²)"
              << std::setw(15) << "C_sca(nm²)"
              << std::setw(15) << "C_abs(nm²)\n";
    std::cout << std::string(60, '-') << "\n";
    
    std::cout << std::scientific << std::setprecision(4);
    for (double wl : wavelengths) {
        SphereResponse response = MnpPlasmon::simulate_sphere_response(
            "Au", wl, 20.0, 1.33
        );
        std::cout << std::left << std::fixed << std::setprecision(1) << std::setw(15) << wl
                  << std::scientific << std::setprecision(4)
                  << std::setw(15) << response.c_ext
                  << std::setw(15) << response.c_sca
                  << std::setw(15) << response.c_abs << "\n";
    }
    
    std::cout << "\n";
    
    // Detailed response at resonance
    SphereResponse response = MnpPlasmon::simulate_sphere_response("Au", 550.0, 20.0, 1.33);
    MnpPlasmon::print_response(response);
    
    return 0;
}
