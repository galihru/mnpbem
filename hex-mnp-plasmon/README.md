# mnp_plasmon

`mnp_plasmon` is an Erlang Hex package for single-particle plasmonic response in the Rayleigh quasi-static limit. It mirrors the same physical model already published in JavaScript and Racket, so the codebase stays consistent across languages.

It integrates three layers:

- Drude dielectric function for Au, Ag, and Al
- Rayleigh polarizability of a metallic sphere in a dielectric medium
- Optical cross sections: extinction, scattering, and absorption

## Install

Add to `rebar.config`:

```erlang
{deps, [
    {mnp_plasmon, "0.1.0"}
]}. 
```

## High-level API

```erlang
1> mnp_plasmon:simulate_sphere_response(#{
       material => <<"Au">>,
       wavelength_nm => 550.0,
       radius_nm => 20.0,
       medium_refractive_index => 1.33
   }).
```

Return structure:

- `inputs`
- `eps_particle`
- `eps_medium`
- `alpha`
- `cross_section.c_ext`
- `cross_section.c_sca`
- `cross_section.c_abs`

## Low-level API

- `mnp_plasmon_material:material_list/0`
- `mnp_plasmon_material:get_drude_params/1`
- `mnp_plasmon_material:drude_epsilon/2`
- `mnp_plasmon_material:constant_epsilon/2`
- `mnp_plasmon_mie:rayleigh_polarizability/3`
- `mnp_plasmon_mie:rayleigh_cross_sections/4`

## Cross-language integration

This package is designed to match the same API concepts already implemented in:

- Python components in this repository
- npm packages under `npm-packages/`
- Racket package `mnp-plasmon`

There is also an Elixir example in `examples/elixir_demo.exs` showing how the Erlang package can be consumed from another BEAM language.

## License

GPL-3.0-only