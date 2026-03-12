-module(mnp_plasmon_material).

-export([
    material_list/0,
    get_drude_params/1,
    drude_epsilon/2,
    constant_epsilon/2
]).

-type complex() :: #{re := float(), im := float()}.
-type drude_params() :: #{name := binary(), omega_p := float(), gamma := float(), eps_inf := float()}.

-spec material_list() -> [binary()].
material_list() ->
    [<<"Au">>, <<"Ag">>, <<"Al">>].

-spec get_drude_params(binary() | string()) -> drude_params().
get_drude_params(Material0) ->
    Material = normalize_material(Material0),
    case Material of
        <<"Au">> -> #{name => <<"Au">>, omega_p => 3.106, gamma => 0.0132, eps_inf => 8.90};
        <<"Ag">> -> #{name => <<"Ag">>, omega_p => 3.810, gamma => 0.0048, eps_inf => 3.91};
        <<"Al">> -> #{name => <<"Al">>, omega_p => 14.83, gamma => 0.098, eps_inf => 1.24};
        _ -> erlang:error({unknown_material, Material0})
    end.

-spec drude_epsilon(binary() | string(), number()) -> complex().
drude_epsilon(Material, WavelengthNm) when is_number(WavelengthNm), WavelengthNm > 0 ->
    #{omega_p := OmegaP, gamma := Gamma, eps_inf := EpsInf} = get_drude_params(Material),
    OmegaEv = wavelength_to_energy(float(WavelengthNm)),
    OmegaSq = OmegaEv * OmegaEv,
    OmegaPSq = OmegaP * OmegaP,
    DenomSq = OmegaSq + Gamma * Gamma,
    Real = EpsInf - ((OmegaPSq * OmegaEv) / DenomSq),
    Imag = (OmegaPSq * Gamma) / (OmegaEv * DenomSq),
    #{re => Real, im => Imag}.

-spec constant_epsilon(number(), number()) -> complex().
constant_epsilon(NSquared, _WavelengthNm) when is_number(NSquared) ->
    #{re => float(NSquared), im => 0.0}.

normalize_material(Material) when is_binary(Material) ->
    Material;
normalize_material(Material) when is_list(Material) ->
    unicode:characters_to_binary(Material).

wavelength_to_energy(WavelengthNm) ->
    1240.0 / WavelengthNm.