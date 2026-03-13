using MnpPlasmon
using Test

@testset "MnpPlasmon.jl" begin

    @testset "Material database" begin
        @test haskey(MATERIALS, "Au")
        @test haskey(MATERIALS, "Ag")
        @test haskey(MATERIALS, "Al")
        @test_throws ArgumentError drude_epsilon(2.0, "Unknown")
    end

    @testset "Drude permittivity" begin
        eps = drude_epsilon(2.25, "Au")   # ~550 nm in eV
        @test isfinite(real(eps))
        @test imag(eps) > 0               # positive imaginary part (loss)
    end

    @testset "Sphere response — Au" begin
        r = sphere_response(550.0, 25.0, "Au")
        @test r.c_ext > 0
        @test r.c_sca >= 0
        @test r.c_abs >= 0
        @test isapprox(r.c_ext, r.c_sca + r.c_abs, atol=1e-10)
    end

    @testset "Sphere response — Ag" begin
        r = sphere_response(400.0, 20.0, "Ag")
        @test r.c_ext > 0
    end

    @testset "Medium refractive index" begin
        r_vac  = sphere_response(550.0, 25.0, "Au", 1.0)
        r_med  = sphere_response(550.0, 25.0, "Au", 1.5)
        @test r_med.c_ext != r_vac.c_ext
    end

end
