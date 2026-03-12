%% Compile inside the package with rebar3 shell or erl -pa _build/default/lib/mnp_plasmon/ebin

-module(erlang_demo).
-export([run/0]).

run() ->
    Result = mnp_plasmon:simulate_sphere_response(#{material => <<"Au">>,
                                                   wavelength_nm => 550.0,
                                                   radius_nm => 20.0,
                                                   medium_refractive_index => 1.33}),
    io:format("~p~n", [Result]).