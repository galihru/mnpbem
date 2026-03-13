using DelimitedFiles
using MnpPlasmon

wavelengths = 400.0:5.0:700.0
rows = Vector{NTuple{4,Float64}}()
for wl in wavelengths
    r = sphere_response(wl, 25.0, "Au", 1.33)
    push!(rows, (wl, r.c_ext, r.c_sca, r.c_abs))
end

mkpath("docs/example-data")
open("docs/example-data/julia.csv", "w") do io
    write(io, "wavelength_nm,c_ext,c_sca,c_abs\n")
    for row in rows
        write(io, string(row[1], ",", row[2], ",", row[3], ",", row[4], "\n"))
    end
end
