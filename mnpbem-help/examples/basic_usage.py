from mnpbem_help import list_reference_modules

print("Reference modules:")
for module_name in list_reference_modules():
    print(f"- {module_name}")
