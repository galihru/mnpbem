source("r-mnp-plasmon/R/mnp_plasmon.R")

wavelengths <- seq(400, 700, by = 5)
rows <- lapply(wavelengths, function(wl) {
  result <- sphere_response(
    wavelength_nm = wl,
    radius_nm = 25,
    material = "Au",
    medium_refractive_index = 1.33
  )
  data.frame(
    wavelength_nm = wl,
    c_ext = result$sigma_ext,
    c_sca = result$sigma_sca,
    c_abs = result$sigma_abs
  )
})

output <- do.call(rbind, rows)
dir.create("docs/example-data", recursive = TRUE, showWarnings = FALSE)
write.csv(output, file = "docs/example-data/r.csv", row.names = FALSE)
