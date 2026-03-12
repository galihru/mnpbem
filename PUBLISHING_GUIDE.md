# Publishing Guide for MNP Plasmon C Family Packages

This document provides instructions for publishing all three language implementations to their respective package registries.

## C Library - Publish to vcpkg

### Prerequisites
- Vcpkg installed and configured
- Git access to: https://github.com/microsoft/vcpkg

### Steps

1. **Fork vcpkg repository** at https://github.com/microsoft/vcpkg

2. **Create port directory**:
   ```powershell
   mkdir vcpkg/ports/mnp-plasmon
   ```

3. **Add port files**:
   - Copy `c-mnp-plasmon/` contents
   - Create `vcpkg/ports/mnp-plasmon/portfile.cmake`:
   
   ```cmake
   vcpkg_from_github(
       OUT_SOURCE_PATH SOURCE_PATH
       REPO galihru/mnpbem
       REF main
       SHA512 <hash>
       HEAD_REF main
   )
   
   vcpkg_cmake_configure(SOURCE_PATH "${SOURCE_PATH}/c-mnp-plasmon")
   vcpkg_cmake_install()
   vcpkg_copy_pdbs()
   
   file(INSTALL "${CURRENT_PORT_DIR}/usage" 
        DESTINATION "${CURRENT_PACKAGES_DIR}/share/${PORT}")
   ```

4. **Create usage file** `vcpkg/ports/mnp-plasmon/usage`:
   ```
   The package mnp-plasmon provides libraries and headers.
   
   CMake usage:
       find_package(mnp_plasmon CONFIG REQUIRED)
       target_link_libraries(your_app PRIVATE mnp_plasmon)
   ```

5. **Submit pull request** to vcpkg with the new port

## C++ Library - Publish to vcpkg

Similar process to C library:

1. **Create port directory**:
   ```powershell
   mkdir vcpkg/ports/mnp-plasmon-cxx
   ```

2. **Add port files** with modern C++ configuration

3. **Submit pull request**

## C# Library - Publish to NuGet

### Prerequisites
- NuGet CLI installed
- NuGet.org account with API key
- .NET SDK 6.0+

### Steps

1. **Build package**:
   ```powershell
   cd csharp-mnp-plasmon\MnpPlasmon
   dotnet pack -c Release
   ```

2. **Get NuGet API key**:
   - Go to https://www.nuget.org/account/apikeys
   - Create new API key with Push permission
   - Save securely

3. **Publish package**:
   ```powershell
   dotnet nuget push bin\Release\MnpPlasmon.0.1.0.nupkg `
       -k <YOUR_API_KEY> `
       -s https://api.nuget.org/v3/index.json
   ```

4. **Verify publication**:
   - Check https://www.nuget.org/packages/MnpPlasmon/
   - Verify version 0.1.0 is listed

## Publish to GitHub Packages

### C# to GitHub NuGet Registry

1. **Setup authentication**:
   ```powershell
   dotnet nuget add source `
       --username galihru `
       --password <GITHUB_TOKEN> `
       --store-password-in-clear-text `
       --name github "https://nuget.pkg.github.com/galihru/index.json"
   ```

2. **Publish**:
   ```powershell
   dotnet nuget push bin\Release\MnpPlasmon.0.1.0.nupkg `
       -s https://nuget.pkg.github.com/galihru/index.json `
       -k <GITHUB_TOKEN>
   ```

### C/C++ to GitHub Release

1. **Create GitHub release** with binaries
2. **Upload pre-built libraries**: `.lib`, `.dll`, `.a`, `.so`
3. **Include documentation** and header files

## Post-Publishing Verification

### Verify All Packages

- [ ] C package visible on vcpkg.io
- [ ] C++ package visible on vcpkg.io
- [ ] C# package visible on NuGet.org
- [ ] All packages show correct version 0.1.0
- [ ] Documentation links are accessible
- [ ] Repository links point to correct GitHub URLs
- [ ] License (GPL-3.0-only) is displayed correctly
- [ ] Package count visible on registries

### Consumer Testing

```bash
# C with vcpkg
vcpkg install mnp-plasmon

# C++ with vcpkg
vcpkg install mnp-plasmon-cxx

# C# with NuGet
dotnet add package MnpPlasmon
```

## Troubleshooting

**vcpkg port issues**: Check `vcpkg/docs/maintainers/ports.md`

**NuGet publish errors**: Run `dotnet nuget push --help` for options

**GPL-3.0-only license issues**: Ensure `-l GPL-3.0-only` is in commands or add to project file

## References

- vcpkg: https://github.com/microsoft/vcpkg
- NuGet: https://www.nuget.org/
- OpenVCM: https://opencv.io/
