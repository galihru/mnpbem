-module(mnp_plasmon_mie).

-export([
    rayleigh_polarizability/3,
    rayleigh_cross_sections/4
]).

-define(PI, 3.141592653589793).

-type complex() :: #{re := float(), im := float()}.

-spec rayleigh_polarizability(number(), complex(), complex()) -> complex().
rayleigh_polarizability(RadiusNm, EpsParticle, EpsMedium) when is_number(RadiusNm), RadiusNm > 0 ->
    Scale = 4.0 * ?PI * math:pow(float(RadiusNm), 3),
    Numerator = complex_sub(EpsParticle, EpsMedium),
    Denominator = complex_add(EpsParticle, complex_scale(EpsMedium, 2.0)),
    complex_scale(complex_div(Numerator, Denominator), Scale).

-spec rayleigh_cross_sections(number(), number(), complex(), complex()) -> #{c_ext := float(), c_sca := float(), c_abs := float()}. 
rayleigh_cross_sections(WavelengthNm, RadiusNm, EpsParticle, EpsMedium)
        when is_number(WavelengthNm), WavelengthNm > 0, is_number(RadiusNm), RadiusNm > 0 ->
    NMedium = math:sqrt(maps:get(re, EpsMedium)),
    K = 2.0 * ?PI * (NMedium / float(WavelengthNm)),
    Alpha = rayleigh_polarizability(RadiusNm, EpsParticle, EpsMedium),
    CExt = K * maps:get(im, Alpha),
    MagSq = complex_mag_sq(Alpha),
    CSca = (math:pow(K, 4) * MagSq) / (6.0 * ?PI),
    CAbs = CExt - CSca,
    #{c_ext => CExt, c_sca => CSca, c_abs => CAbs}.

complex_add(#{re := Ar, im := Ai}, #{re := Br, im := Bi}) ->
    #{re => Ar + Br, im => Ai + Bi}.

complex_sub(#{re := Ar, im := Ai}, #{re := Br, im := Bi}) ->
    #{re => Ar - Br, im => Ai - Bi}.

complex_scale(#{re := Re, im := Im}, Scale) ->
    #{re => Re * Scale, im => Im * Scale}.

complex_div(#{re := Ar, im := Ai}, #{re := Br, im := Bi}) ->
    Den = Br * Br + Bi * Bi,
    #{re => ((Ar * Br) + (Ai * Bi)) / Den,
      im => ((Ai * Br) - (Ar * Bi)) / Den}.

complex_mag_sq(#{re := Re, im := Im}) ->
    Re * Re + Im * Im.