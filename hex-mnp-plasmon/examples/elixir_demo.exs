result = :mnp_plasmon.simulate_sphere_response(%{
  material: "Au",
  wavelength_nm: 550.0,
  radius_nm: 20.0,
  medium_refractive_index: 1.33
})

IO.inspect(result, label: "mnp_plasmon from Elixir")