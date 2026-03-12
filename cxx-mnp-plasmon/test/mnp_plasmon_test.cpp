#include <gtest/gtest.h>
#include "mnp_plasmon.hpp"

using namespace mnp;

TEST(MaterialTest, MaterialList) {
    auto materials = MnpPlasmon::material_list();
    EXPECT_EQ(materials.size(), 3);
    EXPECT_EQ(materials[0].name, "Au");
    EXPECT_EQ(materials[1].name, "Ag");
    EXPECT_EQ(materials[2].name, "Al");
}

TEST(MaterialTest, MaterialExists) {
    EXPECT_TRUE(MnpPlasmon::material_exists("Au"));
    EXPECT_TRUE(MnpPlasmon::material_exists("Ag"));
    EXPECT_TRUE(MnpPlasmon::material_exists("Al"));
    EXPECT_FALSE(MnpPlasmon::material_exists("Cu"));
}

TEST(MaterialTest, MaterialGet) {
    Material au = MnpPlasmon::material_get("Au");
    EXPECT_EQ(au.name, "Au");
    EXPECT_DOUBLE_EQ(au.omega_p, 3.106);
    EXPECT_DOUBLE_EQ(au.gamma, 0.0132);
    EXPECT_DOUBLE_EQ(au.eps_inf, 8.90);
}

TEST(DielectricTest, DrudeEpsilon) {
    complex eps = MnpPlasmon::drude_epsilon("Au", 550.0);
    // Au at 550nm should have negative real part and positive imaginary part
    EXPECT_LT(eps.real(), 0.0);
    EXPECT_GT(eps.imag(), 0.0);
}

TEST(DielectricTest, ConstantEpsilon) {
    complex eps = MnpPlasmon::constant_epsilon(1.77);  // water at 550nm
    EXPECT_DOUBLE_EQ(eps.real(), 1.77);
    EXPECT_DOUBLE_EQ(eps.imag(), 0.0);
}

TEST(CrossSectionTest, PositiveValues) {
    SphereResponse response = MnpPlasmon::simulate_sphere_response(
        "Au", 550.0, 20.0, 1.33
    );
    EXPECT_GE(response.c_ext, 0.0);
    EXPECT_GE(response.c_sca, 0.0);
    EXPECT_GE(response.c_abs, 0.0);
    EXPECT_GE(response.c_ext, response.c_sca);  // C_ext >= C_sca
}

TEST(SimulationTest, CompleteResponse) {
    SphereResponse response = MnpPlasmon::simulate_sphere_response(
        "Au", 550.0, 20.0, 1.33
    );
    EXPECT_DOUBLE_EQ(response.wavelength_nm, 550.0);
    EXPECT_DOUBLE_EQ(response.radius_nm, 20.0);
    EXPECT_DOUBLE_EQ(response.medium_refractive_index, 1.33);
    EXPECT_NE(std::abs(response.epsilon_particle), 0.0);
    EXPECT_NE(std::abs(response.polarizability), 0.0);
}

TEST(SimulationTest, InvalidMaterial) {
    EXPECT_THROW(
        MnpPlasmon::simulate_sphere_response("Cu", 550.0, 20.0, 1.33),
        std::invalid_argument
    );
}
