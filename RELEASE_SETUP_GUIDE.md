# Multi-Language Release Setup & Testing Guide

✅ **All implementations created and committed to GitHub!**

⚠️ **IMPORTANT**: Keep your API tokens/secrets secure! Never put them in public files. Only add them via GitHub's Secrets settings.

## 📦 What's Been Deployed

### 1. **New Rust Implementation** ✨
- **Location**: `rust-mnp-plasmon/`
- **Files**: 
  - `Cargo.toml` - Package metadata
  - `src/lib.rs` - Full implementation with tests
  - `examples/basic_sphere.rs` - Example usage
  - `README.md` - Rust-specific documentation
- **Registry**: Ready for crates.io publishing
- **Dependencies**: Only `num-complex` (no extra bloat)

### 2. **Master Release Orchestrator** 🎯
- **Workflow**: `.github/workflows/release-master.yml`
- **Trigger**: GitHub Releases or manual dispatch
- **Jobs**: Orchestrates 4 parallel publishing jobs
  - Python → PyPI
  - JavaScript → npm + GitHub npm registry
  - C# → NuGet.org + GitHub NuGet registry
  - Rust → crates.io

### 3. **Rust-Specific Publisher** 🚀
- **Workflow**: `.github/workflows/publish-rust.yml`
- **Trigger**: Tags matching `rust-v*` or manual dispatch
- **Actions**: Tests, builds, and publishes to crates.io

### 4. **Updated Documentation** 📚
- **Main README**: Comprehensive with:
  - Multi-language badges table
  - Physical formulas (KaTeX)
  - Quick start examples for each language
  - Performance benchmarks
  - Registry links
  - Material database table
  
- **SECRETS_GUIDE.md**: Complete setup instructions for:
  - PyPI_API_TOKEN
  - NPMJS_TOKEN
  - NUGET_API_KEY
  - CARGO_REGISTRY_TOKEN
  - Token rotation & security best practices

## 🔧 Setup Steps (NEXT - You Need to Do This)

### Step 1: Add GitHub Secrets

Go to: **Settings → Secrets and variables → Actions**

Add these secrets:

```
☐ PYPI_API_TOKEN         (from PyPI account)
☐ NPMJS_TOKEN            (from npm account)  
☐ NUGET_API_KEY          (from NuGet account)
☐ CARGO_REGISTRY_TOKEN   (from crates.io account)
```

**For CARGO_REGISTRY_TOKEN**, use the token you have from crates.io:

```bash
# Or use GitHub CLI:
gh secret set CARGO_REGISTRY_TOKEN
# Paste your crates.io token when prompted
```

### Step 2: Create a Test Release

```bash
# List current tags
git tag | tail -5

# Create test release (local branch, don't push yet)
git tag -a v0.2.0-test -m "Test all languages release"

# View release info
git show v0.2.0-test
```

### Step 3: Create GitHub Release (Web UI)

1. Go to: https://github.com/galihru/mnpbem/releases/new
2. **Tag version**: v0.2.0-test
3. **Title**: "v0.2.0-test - Multi-Language Release"
4. **Body**:
   ```
   ## Multi-Language Release 🚀
   
   This release includes implementations in:
   - Python (mnpbem ecosystem)
   - JavaScript/TypeScript (npm)
   - C# / .NET (NuGet)
   - Rust (crates.io)
   - C/C++ (vcpkg)
   
   ### What's New
   - Rust package full release
   - Master release orchestrator
   - Synchronized multi-platform publishing
   
   Packages go live across all registries automatically!
   ```
5. Check "This is a pre-release"
6. Click **Publish release**

### Step 4: Monitor the Workflow

**Watch it publish across all 4 platforms in parallel! 🎯**

```
https://github.com/galihru/mnpbem/actions
↓
Look for: "Master Release Orchestrator"
↓
Watch jobs:
  ✓ publish-npm     (npm + GitHub npm registry)
  ✓ publish-python  (PyPI)
  ✓ publish-nuget   (NuGet.org + GitHub NuGet)
  ✓ publish-rust    (crates.io)
  ✓ summary         (final report)
```

## 🧪 Verification Checklist

After release is published, verify each platform:

- [ ] **PyPI**: https://pypi.org/project/mnpbem/
  - Check version `0.2.0-test` in release history

- [ ] **npm**: https://www.npmjs.com/~galihru?tab=packages
  - Verify: `mnp`, `mnp-material`, `mnp-mie` all have new version

- [ ] **NuGet**: https://www.nuget.org/profiles/galihru
  - Check `MnpPlasmon` version history
  - Also visible on GitHub: https://github.com/galihru/mnpbem/packages

- [ ] **Crates.io**: https://crates.io/crates/mnp-plasmon
  - Check `mnp-plasmon` version history
  - Documentation at: https://docs.rs/mnp-plasmon/

## 📊 What Each Platform Gets

### Python (PyPI)
```
  Version: 0.2.0-test
  Packages: mnpbem, mnpbem-base, mnpbem-bem, ...
  URL: https://pypi.org/project/mnpbem/
```

### JavaScript (npm)
```
  Version: 0.2.0-test
  Packages: mnp, mnp-material, mnp-mie
  Registries: npmjs.com, GitHub npm registry (@galihru)
  URL: https://www.npmjs.com/~galihru?tab=packages
```

### C# (.NET - NuGet)
```
  Version: 0.2.0-test
  Package: MnpPlasmon
  Registries: NuGet.org, GitHub NuGet registry
  URL: https://www.nuget.org/packages/MnpPlasmon/
```

### Rust (Crates.io)
```
  Version: 0.2.0-test
  Package: mnp-plasmon
  Registries: crates.io, docs.rs
  URL: https://crates.io/crates/mnp-plasmon
```

## 🔄 Recommended Release Flow for Future

Once you verify v0.2.0-test works:

### For Production Releases

```bash
# Update versions in:
1. rust-mnp-plasmon/Cargo.toml → version = "X.Y.Z"
2. csharp-mnp-plasmon/MnpPlasmon/MnpPlasmon.csproj → <Version>X.Y.Z</Version>
3. npm-packages/package.json → "version": "X.Y.Z"
4. mnpbem/setup.py (or pyproject.toml) → version="X.Y.Z"

# Commit version bumps
git add -A
git commit -m "chore: Bump version to X.Y.Z"

# Create release tag
git tag -a vX.Y.Z -m "Release version X.Y.Z - [description]"

# Push (triggers master orchestrator automatically!)
git push origin main
git push origin vX.Y.Z

# GitHub Release created → All platforms publish in parallel
```

## 🛠️ Manual Testing (If Workflows Fail)

### Test Rust locally
```bash
cd rust-mnp-plasmon
cargo test
cargo build --release
cargo run --example basic_sphere
```

### Test Python locally
```bash
cd mnpbem/mnpbem-material  # or other module
python -m pip install -e .
python -m pytest
```

### Test JavaScript locally
```bash
cd npm-packages
npm install
npm run test --workspaces
```

### Test C# locally
```bash
cd csharp-mnp-plasmon
dotnet build
dotnet test
dotnet pack -c Release
```

## ⚠️ Troubleshooting

### Workflow fails with "401 Unauthorized"
- **Python**: Check PYPI_API_TOKEN (should start with `pypi-`)
- **npm**: Check NPMJS_TOKEN format
- **NuGet**: Check NUGET_API_KEY not expired
- **Rust**: Check CARGO_REGISTRY_TOKEN format

### Package not appearing on registry
- Wait 5-10 minutes (registries need time to sync)
- Check workflow logs: https://github.com/galihru/mnpbem/actions
- Verify secret values are correct (copy-paste with spaces)

### Need to delete a test release?
```bash
# Delete local tag
git tag -d v0.2.0-test

# Delete remote tag
git push origin --delete v0.2.0-test

# Delete GitHub Release (web UI):
# https://github.com/galihru/mnpbem/releases/tag/v0.2.0-test
# → Click "Delete"
```

## 📈 Next Steps (Advanced)

After v0.2.0-test verification:

1. **Delete test packages from registries** (optional)
   ```bash
   # Each registry has package delete/yank features
   ```

2. **Create production release v0.2.0**
   ```bash
   git tag -a v0.2.0 -m "Production release"
   git push origin v0.2.0
   ```

3. **Enable branch protection rules** (Settings → Branches)
   - Require releases for version bumps
   - Automatic semver version parsing

4. **Setup automatic version bumping**
   - Tools like `semantic-release` can auto-bump on commits
   - Triggers release automatically

5. **Monitor package statistics**
   - npm: `npm-stat` for download stats
   - PyPI: View via repository dashboard
   - NuGet: Built-in download counter
   - Crates.io: Built-in download stats

## 📞 Quick Reference

**Files Changed:**
```
README.md                           ✅ Updated with formulas, badges, examples
SECRETS_GUIDE.md                    ✅ Created - Setup instructions
.github/workflows/release-master.yml ✅ Created - 4 parallel jobs
.github/workflows/publish-rust.yml   ✅ Created - Rust-specific
rust-mnp-plasmon/                   ✅ Created - Full Rust implementation
```

**Secrets Needed:**
```
PYPI_API_TOKEN         = (from PyPI account)
NPMJS_TOKEN            = (from npm account)
NUGET_API_KEY          = (from NuGet.org account)
CARGO_REGISTRY_TOKEN   = (from your crates.io account)
```

**Registry Status URLs:**
```
PyPI:      https://pypi.org/project/mnpbem/
npm:       https://www.npmjs.com/~galihru?tab=packages
NuGet:     https://www.nuget.org/profiles/galihru
Crates.io: https://crates.io/users/galihru
```

**Workflow Status:**
```
https://github.com/galihru/mnpbem/actions
```

---

**Ready to release v0.2.0 across all platforms?** 🚀
