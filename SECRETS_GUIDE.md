# GitHub Secrets Configuration Guide

This document explains all the secrets required for the multi-language release orchestrator pipeline.

## 🔐 Required Secrets for Auto-Publishing

### 1. **PYPI_API_TOKEN** - PyPI Publishing
- **Purpose**: Publish Python packages (mnpbem*, mnp-plasmon) to PyPI
- **Type**: API Token (Trusted Publisher via OIDC recommended)
- **How to set up**:
  ```
  1. Go to https://pypi.org/account/
  2. Create a new PyPI Account (if needed)
  3. Get API token from: https://pypi.org/manage/account/
  4. In GitHub:
     - Settings → Secrets and variables → Actions
     - New repository secret: PYPI_API_TOKEN
     - Paste the token starting with 'pypi-...'
  ```
- **Used by**: `.github/workflows/mnpbem.yml`, `publish-python` job in `release-master.yml`

### 2. **NPMJS_TOKEN** - npm Publishing
- **Purpose**: Publish JavaScript packages (mnp, mnp-material, mnp-mie) to npm
- **Type**: npm Access Token
- **How to set up**:
  ```
  1. Go to https://npmjs.com (login/signup)
  2. Account settings → Tokens/Auth Tokens → Create new token
     - Choose "Automation" type (recommended)
     - Scope: "Full access"
  3. Copy the token
  4. In GitHub:
     - Settings → Secrets and variables → Actions
     - New repository secret: NPMJS_TOKEN
     - Paste the token
  ```
- **Used by**: `.github/workflows/npm-publish.yml`, `publish-npm` job in `release-master.yml`

### 3. **NUGET_API_KEY** - NuGet Publishing
- **Purpose**: Publish C# packages (MnpPlasmon) to NuGet.org
- **Type**: NuGet API Key
- **How to set up**:
  ```
  1. Go to https://www.nuget.org/account/
  2. Login/register account
  3. Manage API Keys → Create new key
     - Glob Pattern: mnp*
     - Permissions: "Push new packages and package versions"
     - Expiration: 1 year or more
  4. Copy the API key
  5. In GitHub:
     - Settings → Secrets and variables → Actions
     - New repository secret: NUGET_API_KEY
     - Paste the key
  ```
- **Used by**: `.github/workflows/publish-csharp.yml`, `publish-nuget` job in `release-master.yml`

### 4. **CARGO_REGISTRY_TOKEN** - Crates.io Publishing
- **Purpose**: Publish Rust packages (mnp-plasmon) to crates.io
- **Type**: Crates.io API Token
- **How to set up**:
  ```
  1. Go to https://crates.io (login/signup)
  2. Account settings → API Tokens → New Token
  3. Copy the token
  4. In GitHub:
     - Settings → Secrets and variables → Actions
     - New repository secret: CARGO_REGISTRY_TOKEN
     - Paste the token
  ```
- **Used by**: `.github/workflows/publish-rust.yml`, `publish-rust` job in `release-master.yml`

### 5. **GITHUB_TOKEN** - Automatic (No Setup Needed)
- **Purpose**: Publish to GitHub Package Registry (npm, NuGet)
- **Type**: GitHub-provided token
- **Status**: ✅ **Automatically provided by GitHub Actions**
- **Permissions required** (already set in workflow file):
  ```yaml
  permissions:
    contents: read
    packages: write
    id-token: write
  ```
- **Used by**: All platform workflows for GitHub Package Registry

## 📋 Complete Secrets Checklist

Copy this checklist to your GitHub Issues/Projects to track setup:

```
Secrets Setup Checklist:
- [ ] PYPI_API_TOKEN - PyPI
- [ ] NPMJS_TOKEN - npm
- [ ] NUGET_API_KEY - NuGet.org
- [ ] CARGO_REGISTRY_TOKEN - Crates.io
- [ ] Verify GITHUB_TOKEN has packages:write permission
```

## 🛠️ How to Add Secrets to GitHub

### Method 1: GitHub Web UI (Recommended)

1. Go to repository: `https://github.com/YOUR_USERNAME/mnpbem`
2. Click **Settings** tab
3. **Secrets and variables** → **Actions**
4. Click **New repository secret**
5. Add each secret with the exact name and value
6. Save

### Method 2: GitHub CLI

```bash
# Install GitHub CLI: https://cli.github.com/

# Add PyPI token
gh secret set PYPI_API_TOKEN

# Add npm token
gh secret set NPMJS_TOKEN

# Add NuGet key
gh secret set NUGET_API_KEY

# Add Cargo token
gh secret set CARGO_REGISTRY_TOKEN

# List all secrets (doesn't show values)
gh secret list
```

## 🔄 Publishing Workflow

Once secrets are configured:

### Manual Release (Recommended)

```bash
# Create an annotated tag
git tag -a v1.0.0 -m "Release version 1.0.0"

# Push tag (triggers workflows)
git push origin v1.0.0

# GitHub Release is created automatically
# Master Orchestrator triggers all publish jobs
```

### All Platforms Publish Simultaneously

```
v1.0.0 tag pushed
         ↓
GitHub Release created (auto or manual)
         ↓
Master Release Orchestrator (release-master.yml) triggered
         ↓
Four parallel jobs start:
  ├─→ publish-npm (→ npmjs.com + GitHub npm registry)
  ├─→ publish-python (→ PyPI)
  ├─→ publish-nuget (→ NuGet.org + GitHub NuGet registry)
  └─→ publish-rust (→ crates.io)
         ↓
Summary job reports results
```

## ⚠️ Security Best Practices

1. **Use Automated Token Rotation**
   - Don't share tokens in code or documentation
   - Rotate tokens regularly (quarterly recommended)
   - Delete old tokens after creating new ones

2. **Token Expiration**
   - Set token expiration to 1-2 years
   - Crates.io: defaults to no expiration (set manually)
   - npm: can set in Account Settings
   - NuGet: can set in API Keys page
   - PyPI: set during creation

3. **Scope Limitations**
   ```
   PyPI:   Full access (limited by token scope)
   npm:    "Full access" token (use Automation type)
   NuGet:  Limited to package patterns (mnp*)
   Cargo:  Full access (crates.io doesn't offer scoping)
   ```

4. **Monitoring**
   - Check GitHub Actions logs for failed publishes
   - Monitor registry accounts for package versions
   - Set up notifications for new releases

5. **Emergency Access Revocation**
   If credentials are compromised:
   ```
   1. Delete the old token on registry
   2. Create new token on registry
   3. Update GitHub secret with new token
   4. All future publishes use new token
   ```

## 🧪 Testing the Pipeline

### Test Single Platform

```bash
# Test npm publishing
gh workflow run npm-publish.yml -f version=0.1.1 -f skip=false

# Test PyPI publishing
gh workflow run mnpbem.yml -f version=0.1.1

# Test NuGet publishing
gh workflow run publish-csharp.yml
```

### Test Full Orchestrator (Dry Run)

```bash
# Trigger master release with all tasks
git tag -a v0.1.0-test -m "Test release"
git push origin v0.1.0-test

# Check workflow runs: 
# https://github.com/YOUR_USERNAME/mnpbem/actions
```

## 📊 Registry Status Pages

Monitor your published packages:

- **PyPI**: https://pypi.org/user/galihru/
- **npm**: https://www.npmjs.com/~galihru?tab=packages
- **NuGet**: https://www.nuget.org/profiles/galihru
- **Crates.io**: https://crates.io/users/galihru

## 🐛 Troubleshooting

### "401 Unauthorized" on PyPI
- Check token is copied completely (includes `pypi-` prefix)
- Verify token hasn't expired
- Check token has upload permissions

### "403 Forbidden" on npm
- Verify NPMJS_TOKEN is set correctly
- Check npm account permissions
- Verify package name isn't taken/restricted

### "Invalid API Key" on NuGet
- Copy entire API key (including spaces if any)
- Check key hasn't expired
- Verify key has "Push new packages" permission

### "Unauthorized" on Crates.io
- Ensure CARGO_REGISTRY_TOKEN is the full token
- Check token not revoked on crates.io
- Try `cargo login` locally first to verify token

## 📞 Support

For issues:
1. Check workflow logs: `.github/workflows/` → Actions
2. Review registry documentation:
   - [PyPI Uploading](https://packaging.python.org/tutorials/packaging-projects/)
   - [npm Authentication](https://docs.npmjs.com/cli/v9/configuring-npm/npmrc)
   - [NuGet Publishing](https://learn.microsoft.com/en-us/nuget/nuget-org/publish-a-package)
   - [Cargo Publishing](https://doc.rust-lang.org/cargo/commands/cargo-publish.html)
