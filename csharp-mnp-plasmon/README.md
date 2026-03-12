# MNP Plasmon - C# NuGet Package

Modern .NET library for calculating optical response of metallic nanoparticles using Drude model and Rayleigh approximation.

## Features

- **.NET 6.0+** implementation with `System.Numerics.Complex`
- **Drude model** for metallic dielectric function
- **Rayleigh polarizability** calculations
- **Optical cross-sections**: extinction, scattering, absorption
- **Material database**: Au, Ag, Al with realistic parameters
- **High-level API** for complete sphere response simulation
- **Comprehensive unit tests** with xUnit
- **Nullable reference types** enabled for better type safety
- **XML documentation** for IntelliSense

## Installation

Install via NuGet Package Manager:

```bash
dotnet add package MnpPlasmon
```

Or in Visual Studio Package Manager Console:

```powershell
Install-Package MnpPlasmon
```

## Build from Source

```bash
dotnet build
dotnet test
dotnet run --project Demo
```

## Usage

```csharp
using MnpPlasmon;

// Simulate Au nanoparticle response
var response = MnpPlasmon.SimulateSphereResponse(
    "Au",           // material
    550.0,          // wavelength (nm)
    20.0,           // radius (nm)
    1.33            // medium refractive index (water)
);

MnpPlasmon.PrintResponse(response);

Console.WriteLine($"Extinction: {response.CExt:E6} nm²");
Console.WriteLine($"Scattering: {response.CSca:E6} nm²");
Console.WriteLine($"Absorption: {response.CAbs:E6} nm²");
```

## API Reference

### Material Functions

```csharp
IReadOnlyList<Material> MaterialList()
bool MaterialExists(string name)
Material GetMaterial(string name)
```

### Dielectric Functions

```csharp
Complex DrudeEpsilon(string material, double wavelengthNm)
Complex ConstantEpsilon(double nSquared)
```

### Rayleigh Theory

```csharp
Complex RayleighPolarizability(
    double radiusNm,
    Complex epsParticle,
    Complex epsMedium
)

CrossSections RayleighCrossSections(
    double wavelengthNm,
    double radiusNm,
    Complex epsParticle,
    Complex epsMedium
)
```

### High-level API

```csharp
SphereResponse SimulateSphereResponse(
    string material,
    double wavelengthNm,
    double radiusNm,
    double mediumRefractiveIndex
)
```

### Utilities

```csharp
void PrintResponse(SphereResponse response)
```

## Data Types

All types use C# records for immutability:

```csharp
record Material(
    string Name,
    double OmegaP,
    double Gamma,
    double EpsInf
);

record SphereResponse(
    double WavelengthNm,
    double RadiusNm,
    double MediumRefractiveIndex,
    Complex EpsParticle,
    Complex Polarizability,
    double CExt,
    double CSca,
    double CAbs
);

record CrossSections(
    double CExt,
    double CSca,
    double CAbs
);
```

## Requirements

- .NET 6.0 or higher
- No external dependencies for core library

## License

GPL-3.0-only - See LICENSE file for details

## Links

- [Erlang package](https://hex.pm/packages/mnp_plasmon)
- [Racket package](https://pkgs.racket-lang.org/package/mnp-plasmon)
- [npm packages](https://www.npmjs.com/org/galihru)
- [GitHub repository](https://github.com/galihru/mnpbem)
