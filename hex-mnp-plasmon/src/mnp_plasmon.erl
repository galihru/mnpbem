-module(mnp_plasmon).

-export([
    material_list/0,
    get_drude_params/1,
    drude_epsilon/2,
    constant_epsilon/2,
    rayleigh_polarizability/3,
    rayleigh_cross_sections/4,
    simulate_sphere_response/1
]).

-type complex() :: #{re := float(), im := float()}.
-type response() :: #{inputs := map(), eps_particle := complex(), eps_medium := complex(), alpha := complex(), cross_section := map()}.

-spec material_list() -> [binary()].
material_list() ->
    mnp_plasmon_material:material_list().

-spec get_drude_params(binary() | string()) -> map().
get_drude_params(Material) ->
    mnp_plasmon_material:get_drude_params(Material).

-spec drude_epsilon(binary() | string(), number()) -> complex().
drude_epsilon(Material, WavelengthNm) ->
    mnp_plasmon_material:drude_epsilon(Material, WavelengthNm).

-spec constant_epsilon(number(), number()) -> complex().
constant_epsilon(NSquared, WavelengthNm) ->
    mnp_plasmon_material:constant_epsilon(NSquared, WavelengthNm).

-spec rayleigh_polarizability(number(), complex(), complex()) -> complex().
rayleigh_polarizability(RadiusNm, EpsParticle, EpsMedium) ->
    mnp_plasmon_mie:rayleigh_polarizability(RadiusNm, EpsParticle, EpsMedium).

-spec rayleigh_cross_sections(number(), number(), complex(), complex()) -> map().
rayleigh_cross_sections(WavelengthNm, RadiusNm, EpsParticle, EpsMedium) ->
    mnp_plasmon_mie:rayleigh_cross_sections(WavelengthNm, RadiusNm, EpsParticle, EpsMedium).

-spec simulate_sphere_response(map()) -> response().
simulate_sphere_response(#{material := Material,
                           wavelength_nm := WavelengthNm,
                           radius_nm := RadiusNm,
                           medium_refractive_index := MediumN}) ->
    EpsParticle = drude_epsilon(Material, WavelengthNm),
    EpsMedium = constant_epsilon(MediumN * MediumN, WavelengthNm),
    Alpha = rayleigh_polarizability(RadiusNm, EpsParticle, EpsMedium),
    CrossSection = rayleigh_cross_sections(WavelengthNm, RadiusNm, EpsParticle, EpsMedium),
    #{inputs => #{material => Material,
                  wavelength_nm => WavelengthNm,
                  radius_nm => RadiusNm,
                  medium_refractive_index => MediumN},
      eps_particle => EpsParticle,
      eps_medium => EpsMedium,
      alpha => Alpha,
      cross_section => CrossSection}.