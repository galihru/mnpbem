-module(mnp_plasmon_tests).

-include_lib("eunit/include/eunit.hrl").

material_list_test() ->
    ?assertEqual([<<"Au">>, <<"Ag">>, <<"Al">>], mnp_plasmon:material_list()).

drude_epsilon_test() ->
    #{re := Re, im := Im} = mnp_plasmon:drude_epsilon(<<"Au">>, 550.0),
    ?assert(is_float(Re)),
    ?assert(is_float(Im)),
    ?assert(Im > 0.0).

cross_sections_positive_test() ->
    EpsParticle = #{re => -7.5, im => 2.1},
    EpsMedium = #{re => 1.7689, im => 0.0},
    #{c_ext := CExt, c_sca := CSca, c_abs := CAbs} =
        mnp_plasmon:rayleigh_cross_sections(550.0, 20.0, EpsParticle, EpsMedium),
    ?assert(CExt > 0.0),
    ?assert(CSca > 0.0),
    ?assert(CAbs > 0.0).

simulate_response_test() ->
    Response = mnp_plasmon:simulate_sphere_response(#{material => <<"Au">>,
                                                     wavelength_nm => 550.0,
                                                     radius_nm => 20.0,
                                                     medium_refractive_index => 1.33}),
    ?assertMatch(#{inputs := _, eps_particle := _, eps_medium := _, alpha := _, cross_section := _}, Response).