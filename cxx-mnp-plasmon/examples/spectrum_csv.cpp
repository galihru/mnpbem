#include "../include/mnp_plasmon.hpp"
#include <filesystem>
#include <fstream>

int main() {
    std::filesystem::create_directories("docs/example-data");
    std::ofstream out("docs/example-data/cpp.csv");
    if (!out) {
        return 1;
    }

    out << "wavelength_nm,c_ext,c_sca,c_abs\n";
    for (int wl = 400; wl <= 700; wl += 5) {
        auto r = mnp::MnpPlasmon::simulate_sphere_response("Au", static_cast<double>(wl), 25.0, 1.33);
        out << wl << ',' << r.c_ext << ',' << r.c_sca << ',' << r.c_abs << "\n";
    }

    return 0;
}
