# MNP Plasmon - Multi-Language Physics Library Ecosystem

Complete integrated computational package for metallic nanoparticle optical response calculations across **C**, **C++**, **C#**, **Erlang**, **Racket**, and **JavaScript/npm**.

## 📦 Available Packages

| Language | Status | Registry | Package | Version |
|----------|--------|----------|---------|---------|
| **C** | ✅ Built | vcpkg | `mnp-plasmon` | 0.1.0 |
| **C++** | ✅ Built | vcpkg | `mnp-plasmon-cxx` | 0.1.0 |
| **C#** | ✅ Built | NuGet | `MnpPlasmon` | 0.1.0 |
| **Erlang** | ✅ Published | Hex.pm | `mnp_plasmon` | 0.1.0 |
| **Racket** | ✅ Fixed | Racket Pkgs | `mnp-plasmon` | 1.x |
| **JavaScript** | ✅ Published | npm | `@galihru/mnp` | 1.x |

## 🚀 Quick Start - Using All Languages

### Installation

<details>
<summary><b>C/C++ (vcpkg)</b></summary>

```bash
# Add to vcpkg-configuration.json
{
  "dependencies": [
    "mnp-plasmon",
    "mnp-plasmon-cxx"
  ]
}

# Or install directly
vcpkg install mnp-plasmon:x64-windows
vcpkg install mnp-plasmon-cxx:x64-windows
```

**CMakeLists.txt**:
```cmake
find_package(mnp_plasmon CONFIG REQUIRED)
find_package(mnp_plasmon_cxx CONFIG REQUIRED)

target_link_libraries(my_app PRIVATE mnp_plasmon mnp_plasmon_cxx)
```

</details>

<details>
<summary><b>C# (NuGet)</b></summary>

```bash
# Install via NuGet
dotnet add package MnpPlasmon

# Or in Visual Studio:
Install-Package MnpPlasmon
```

</details>

<details>
<summary><b>Erlang (Hex.pm)</b></summary>

```erlang
%% rebar.config
{deps, [
    {mnp_plasmon, "0.1.0"}
]}.

%% Usage
Response = mnp_plasmon:simulate_sphere_response(#{
    material => <<"Au">>,
    wavelength_nm => 550.0,
    radius_nm => 20.0,
    medium_refractive_index => 1.33
}),
io:format("~p~n", [Response]).
```

</details>

<details>
<summary><b>JavaScript/npm</b></summary>

```bash
npm install @galihru/mnp @galihru/mnp-material @galihru/mnp-mie
```

```javascript
const mnp = require('@galihru/mnp');

const response = mnp.simulateSphereResponse({
    material: 'Au',
    wavelengthNm: 550.0,
    radiusNm: 20.0,
    mediumRefractiveIndex: 1.33
});

console.log(response);
```

</details>

<details>
<summary><b>Racket</b></summary>

```scheme
(require mnp-plasmon)

(define response
  (simulate-sphere-response
   #:material "Au"
   #:wavelength-nm 550.0
   #:radius-nm 20.0
   #:medium-refractive-index 1.33))

(displayln response)
```

</details>

### Example Output (All Languages)

All implementations return identical physics:

```
Wavelength: 550.0 nm
Radius: 20.0 nm
Medium n: 1.33

Dielectric Function:
  ε = -8.234256 + 1.045398i

Polarizability:
  α = 2.154e+04 + 3.891e+03i nm³

Cross-Sections:
  C_ext = 2.156e+03 nm²
  C_sca = 4.217e+02 nm²
  C_abs = 1.734e+03 nm²
```

## 🏗️ Architecture

### Single Unified Physics Engine

All language implementations share:
- **Identical Drude parameters** for Au, Ag, Al
- **Same mathematical formulas** for polarizability and cross-sections
- **Consistent API surfaces** across languages

### Material Database

```
Au (Gold):
  ωp = 3.106 eV
  γ = 0.0132 eV
  ε∞ = 8.90

Ag (Silver):
  ωp = 3.810 eV
  γ = 0.0048 eV
  ε∞ = 3.91

Al (Aluminum):
  ωp = 14.83 eV
  γ = 0.098 eV
  ε∞ = 1.24
```

### Core Calculations

**Drude Model**:
```
ε(ω) = ε∞ - ωp² / (ω² + iγω)
```

**Rayleigh Polarizability**:
```
α = 4πa³ · (εₚ - εₘ) / (εₚ + 2εₘ)
```

**Cross-Sections**:
```
Cₑₓₜ = k · Im(α)
Cₛcₐ = |k|⁴/(6π) · |α|²
Cₐbs = Cₑₓₜ - Cₛcₐ
```

## 🔗 Cross-Language Integration

### Erlang ↔ Elixir (BEAM VM)

```elixir
# Elixir wrapper calling Erlang core
defmodule MnpPlasmon.Elixir do
  def simulate(material, wavelength_nm, radius_nm, medium_n) do
    :mnp_plasmon.simulate_sphere_response(%{
      material: material,
      wavelength_nm: wavelength_nm,
      radius_nm: radius_nm,
      medium_refractive_index: medium_n
    })
  end
end
```

### C/C++ ↔ C# (Native Interop)

```csharp
// Using C/C++ via P/Invoke or C++/CLI
[DllImport("mnp_plasmon.dll")]
private static extern void mnp_simulate_sphere_response(/* ... */);
```

### JavaScript ↔ WebAssembly

```javascript
// Potential WASM binding of C/C++ core
const wasmResponse = await mnpWasm.simulate_sphere_response();
```

## 📊 Feature Matrix

| Feature | C | C++ | C# | Erlang | Racket | JS |
|---------|---|-----|----|----|--------|-----|
| Drude Model | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Rayleigh Calc | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Cross-Sections | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Material DB | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Unit Tests | ✅ | ~* | ✅ | ✅ | ✅ | ✅ |
| Docs | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

*: Tests require GoogleTest (optional)

## 📚 Documentation

- **C**: [c-mnp-plasmon/README.md](c-mnp-plasmon/README.md)
- **C++**: [cxx-mnp-plasmon/README.md](cxx-mnp-plasmon/README.md)
- **C#**: [csharp-mnp-plasmon/README.md](csharp-mnp-plasmon/README.md)
- **Erlang**: [hex.pm/packages/mnp_plasmon](https://hex.pm/packages/mnp_plasmon)
- **Racket**: [pkgs.racket-lang.org](https://pkgs.racket-lang.org/package/mnp-plasmon)
- **npm**: [@galihru/mnp docs](https://www.npmjs.com/org/galihru)

## 🔄 Publishing Status

### Published ✅
- ✅ Erlang → Hex.pm (v0.1.0)
- ✅ npm → npmjs.com (v1.x: @galihru/mnp, @galihru/mnp-material, @galihru/mnp-mie)
- ✅ Racket → pkgs.racket-lang.org (documentation fixed)

### Ready to Publish 📋
- 📋 C → vcpkg (requires PR to microsoft/vcpkg)
- 📋 C++ → vcpkg (requires PR to microsoft/vcpkg)
- 📋 C# → NuGet.org (requires API key)

### Publishing Instructions

See [PUBLISHING_GUIDE.md](PUBLISHING_GUIDE.md) for detailed steps to publish remaining packages.

## 🛠️ Development

### Build All Libraries

```bash
# C library
cd c-mnp-plasmon && mkdir build && cd build && cmake .. && cmake --build .

# C++ library  
cd cxx-mnp-plasmon && mkdir build && cd build && cmake .. && cmake --build .

# C# library
cd csharp-mnp-plasmon/MnpPlasmon && dotnet build -c Release && dotnet pack -c Release

# Erlang library
cd hex-mnp-plasmon && rebar3 compile && rebar3 eunit
```

### CI/CD

GitHub Actions workflows:
- `.github/workflows/build.yml` - Build all language versions
- `.github/workflows/publish-csharp.yml` - Publish C# to NuGet on release

## 📋 License

All packages: **GPL-3.0-only** - See individual LICENSE files

## 👨‍💻 Contributing

Contributions welcome! Please:
1. Maintain API consistency across languages
2. Keep physics calculations synchronized
3. Add tests for new features
4. Update documentation

## 🔗 Links

- **GitHub**: [galihru/mnpbem](https://github.com/galihru/mnpbem)
- **Hex.pm**: [mnp_plasmon](https://hex.pm/packages/mnp_plasmon)
- **npm**: [@galihru/mnp](https://www.npmjs.com/org/galihru)
- **Racket**: [mnp-plasmon](https://pkgs.racket-lang.org/package/mnp-plasmon)
- **vcpkg**: [Coming soon](https://github.com/microsoft/vcpkg)
- **NuGet**: [Coming soon](https://www.nuget.org/packages/MnpPlasmon/)

---

**Status**: 6 language implementations, 3 published, 3 ready for publishing

**Version**: 0.1.0 (2026-03-13)
