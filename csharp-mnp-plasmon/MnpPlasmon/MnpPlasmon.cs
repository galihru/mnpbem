using System;
using System.Collections.Generic;
using System.Linq;
using System.Numerics;

namespace MnpPlasmon;

/// <summary>
/// Material structure for Drude model parameters
/// </summary>
public record Material(
    string Name,
    double OmegaP,      // Plasma frequency (eV)
    double Gamma,       // Damping coefficient (eV)
    double EpsInf       // High-frequency dielectric constant
);

/// <summary>
/// Output structure for sphere response
/// </summary>
public record SphereResponse(
    double WavelengthNm,
    double RadiusNm,
    double MediumRefractiveIndex,
    Complex EpsParticle,
    Complex Polarizability,
    double CExt,        // Extinction cross-section (nm²)
    double CSca,        // Scattering cross-section (nm²)
    double CAbs         // Absorption cross-section (nm²)
);

/// <summary>
/// Cross-section result
/// </summary>
public record CrossSections(
    double CExt,
    double CSca,
    double CAbs
);

/// <summary>
/// MnpPlasmon - C# implementation for optical response of metallic nanoparticles
/// </summary>
public static class MnpPlasmon
{
    // Constants
    private const double HcEvNm = 1239.84197;  // hc in eV·nm
    private const double PI = Math.PI;

    // Material database
    private static readonly Material[] Materials =
    {
        new("Au", 3.106, 0.0132, 8.90),
        new("Ag", 3.810, 0.0048, 3.91),
        new("Al", 14.83, 0.098, 1.24)
    };

    /// <summary>
    /// Get list of available materials
    /// </summary>
    public static IReadOnlyList<Material> MaterialList() => Array.AsReadOnly(Materials);

    /// <summary>
    /// Check if material exists in database
    /// </summary>
    public static bool MaterialExists(string name) =>
        Materials.Any(m => m.Name == name);

    /// <summary>
    /// Get material from database
    /// </summary>
    public static Material GetMaterial(string name) =>
        Materials.FirstOrDefault(m => m.Name == name)
            ?? throw new ArgumentException($"Material not found: {name}");

    /// <summary>
    /// Convert wavelength (nm) to energy (eV)
    /// </summary>
    private static double WavelengthToEnergy(double wavelengthNm) =>
        HcEvNm / wavelengthNm;

    /// <summary>
    /// Drude model: epsilon(omega) = eps_inf - omega_p^2 / (omega^2 + i*gamma*omega)
    /// </summary>
    public static Complex DrudeEpsilon(string material, double wavelengthNm)
    {
        var mat = GetMaterial(material);
        double omega = WavelengthToEnergy(wavelengthNm);

        // omega^2
        double omegaSq = omega * omega;

        // i*gamma*omega
        var damping = new Complex(0, omega * mat.Gamma);

        // omega_p^2 / (omega^2 + i*gamma*omega)
        var denominator = new Complex(omegaSq, 0) + damping;
        var druideTerm = (mat.OmegaP * mat.OmegaP) / denominator;

        return new Complex(mat.EpsInf, 0) - druideTerm;
    }

    /// <summary>
    /// Constant permittivity (non-absorbing dielectric)
    /// epsilon = n^2
    /// </summary>
    public static Complex ConstantEpsilon(double nSquared) =>
        new(nSquared, 0);

    /// <summary>
    /// Rayleigh polarizability
    /// alpha = 4*pi*a^3 * (eps_p - eps_m) / (eps_p + 2*eps_m)
    /// </summary>
    public static Complex RayleighPolarizability(
        double radiusNm,
        Complex epsParticle,
        Complex epsMedium)
    {
        // 4*pi*a^3
        double volumeFactor = 4.0 * PI * radiusNm * radiusNm * radiusNm;

        // (eps_p - eps_m) / (eps_p + 2*eps_m)
        var numerator = epsParticle - epsMedium;
        var denominator = epsParticle + 2.0 * epsMedium;

        if (denominator.Magnitude < 1e-10)
            return Complex.Zero;

        return volumeFactor * numerator / denominator;
    }

    /// <summary>
    /// Wave vector k = 2*pi*n_medium / wavelength_nm
    /// </summary>
    private static double WaveVector(double wavelengthNm, double nMedium) =>
        2.0 * PI * nMedium / wavelengthNm;

    /// <summary>
    /// Rayleigh cross-sections
    /// C_ext = k * Im(alpha)
    /// C_sca = |k|^4 / (6*pi) * |alpha|^2
    /// C_abs = C_ext - C_sca
    /// </summary>
    public static CrossSections RayleighCrossSections(
        double wavelengthNm,
        double radiusNm,
        Complex epsParticle,
        Complex epsMedium)
    {
        var alpha = RayleighPolarizability(radiusNm, epsParticle, epsMedium);
        double k = WaveVector(wavelengthNm, epsMedium.Real);

        double kPow4 = k * k * k * k;
        double alphaMagSq = alpha.Magnitude * alpha.Magnitude;
        double alphaIm = alpha.Imaginary;

        double cExt = k * alphaIm;
        double cSca = (kPow4 / (6.0 * PI)) * alphaMagSq;
        double cAbs = cExt - cSca;

        // Ensure non-negative absorption
        if (cAbs < 0.0)
            cAbs = 0.0;

        return new CrossSections(cExt, cSca, cAbs);
    }

    /// <summary>
    /// High-level API: simulate sphere optical response
    /// </summary>
    public static SphereResponse SimulateSphereResponse(
        string material,
        double wavelengthNm,
        double radiusNm,
        double mediumRefractiveIndex)
    {
        // Calculate permittivity
        var epsParticle = DrudeEpsilon(material, wavelengthNm);
        var epsMedium = ConstantEpsilon(mediumRefractiveIndex * mediumRefractiveIndex);

        // Calculate polarizability
        var polarizability = RayleighPolarizability(radiusNm, epsParticle, epsMedium);

        // Calculate cross-sections
        var cs = RayleighCrossSections(wavelengthNm, radiusNm, epsParticle, epsMedium);

        return new SphereResponse(
            wavelengthNm,
            radiusNm,
            mediumRefractiveIndex,
            epsParticle,
            polarizability,
            cs.CExt,
            cs.CSca,
            cs.CAbs
        );
    }

    /// <summary>
    /// Pretty-print response structure
    /// </summary>
    public static void PrintResponse(SphereResponse response)
    {
        Console.WriteLine("=== MNP Plasmon Response ===");
        Console.WriteLine($"Wavelength: {response.WavelengthNm:F2} nm");
        Console.WriteLine($"Radius: {response.RadiusNm:F2} nm");
        Console.WriteLine($"Medium n: {response.MediumRefractiveIndex:F4}");
        Console.WriteLine();
        Console.WriteLine("Dielectric Function:");
        Console.WriteLine($"  ε = {response.EpsParticle.Real:F6} + {response.EpsParticle.Imaginary:F6}i");
        Console.WriteLine();
        Console.WriteLine("Polarizability:");
        Console.WriteLine($"  α = {response.Polarizability.Real:E6} + {response.Polarizability.Imaginary:E6}i nm³");
        Console.WriteLine();
        Console.WriteLine("Cross-Sections:");
        Console.WriteLine($"  C_ext = {response.CExt:E6} nm²");
        Console.WriteLine($"  C_sca = {response.CSca:E6} nm²");
        Console.WriteLine($"  C_abs = {response.CAbs:E6} nm²");
        Console.WriteLine("=============================");
    }
}
