using System;
using System.Numerics;
using Xunit;

namespace MnpPlasmon.Tests;

public class MaterialTests
{
    [Fact]
    public void MaterialList_ReturnsThreeMaterials()
    {
        var materials = MnpPlasmon.MaterialList();
        Assert.Equal(3, materials.Count);
        Assert.Equal("Au", materials[0].Name);
        Assert.Equal("Ag", materials[1].Name);
        Assert.Equal("Al", materials[2].Name);
    }

    [Theory]
    [InlineData("Au")]
    [InlineData("Ag")]
    [InlineData("Al")]
    public void MaterialExists_WithValidMaterial_ReturnsTrue(string name)
    {
        Assert.True(MnpPlasmon.MaterialExists(name));
    }

    [Fact]
    public void MaterialExists_WithInvalidMaterial_ReturnsFalse()
    {
        Assert.False(MnpPlasmon.MaterialExists("Cu"));
    }

    [Fact]
    public void GetMaterial_WithValidMaterial_ReturnsCorrectParameters()
    {
        var au = MnpPlasmon.GetMaterial("Au");
        Assert.Equal("Au", au.Name);
        Assert.Equal(3.106, au.OmegaP);
        Assert.Equal(0.0132, au.Gamma);
        Assert.Equal(8.90, au.EpsInf);
    }

    [Fact]
    public void GetMaterial_WithInvalidMaterial_ThrowsException()
    {
        Assert.Throws<ArgumentException>(() => MnpPlasmon.GetMaterial("Cu"));
    }
}

public class DielectricTests
{
    [Fact]
    public void DrudeEpsilon_Au550nm_HasNegativeRealAndPositiveImaginary()
    {
        var eps = MnpPlasmon.DrudeEpsilon("Au", 550.0);
        Assert.True(eps.Real < 0.0, $"Expected negative real part, got {eps.Real}");
        Assert.True(eps.Imaginary > 0.0, $"Expected positive imaginary part, got {eps.Imaginary}");
    }

    [Fact]
    public void ConstantEpsilon_ReturnsComplexWithCorrectValues()
    {
        var eps = MnpPlasmon.ConstantEpsilon(1.77);
        Assert.Equal(1.77, eps.Real);
        Assert.Equal(0.0, eps.Imaginary);
    }
}

public class CrossSectionTests
{
    [Fact]
    public void RayleighCrossSections_Au550nm20nm_AllPositive()
    {
        var response = MnpPlasmon.SimulateSphereResponse("Au", 550.0, 20.0, 1.33);
        Assert.True(response.CExt >= 0.0, $"C_ext should be non-negative, got {response.CExt}");
        Assert.True(response.CSca >= 0.0, $"C_sca should be non-negative, got {response.CSca}");
        Assert.True(response.CAbs >= 0.0, $"C_abs should be non-negative, got {response.CAbs}");
        Assert.True(response.CExt >= response.CSca, "C_ext should be >= C_sca");
    }
}

public class SimulationTests
{
    [Fact]
    public void SimulateSphereResponse_StoresAllInputParameters()
    {
        var response = MnpPlasmon.SimulateSphereResponse("Au", 550.0, 20.0, 1.33);
        Assert.Equal(550.0, response.WavelengthNm);
        Assert.Equal(20.0, response.RadiusNm);
        Assert.Equal(1.33, response.MediumRefractiveIndex);
    }

    [Fact]
    public void SimulateSphereResponse_CalculatesNonZeroPermittivity()
    {
        var response = MnpPlasmon.SimulateSphereResponse("Au", 550.0, 20.0, 1.33);
        Assert.NotEqual(0.0, response.EpsParticle.Magnitude);
    }

    [Fact]
    public void SimulateSphereResponse_CalculatesNonZeroPolarizability()
    {
        var response = MnpPlasmon.SimulateSphereResponse("Au", 550.0, 20.0, 1.33);
        Assert.NotEqual(0.0, response.Polarizability.Magnitude);
    }

    [Fact]
    public void SimulateSphereResponse_InvalidMaterial_ThrowsException()
    {
        Assert.Throws<ArgumentException>(
            () => MnpPlasmon.SimulateSphereResponse("Cu", 550.0, 20.0, 1.33)
        );
    }
}
