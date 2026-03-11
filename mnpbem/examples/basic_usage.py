from mnpbem import available_submodules

installed = available_submodules()
print("Installed mnpbem submodules:")
for name in installed:
    print(f"- {name}")
