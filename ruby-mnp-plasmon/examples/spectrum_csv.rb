require "csv"
require "fileutils"
require_relative "../lib/mnp_plasmon"

wavelengths = (400..700).step(5)
out_path = File.expand_path("../../docs/example-data/ruby.csv", __dir__)
FileUtils.mkdir_p(File.dirname(out_path))

CSV.open(out_path, "w") do |csv|
  csv << %w[wavelength_nm c_ext c_sca c_abs]
  wavelengths.each do |wl|
    result = MnpPlasmon.sphere_response(
      wavelength_nm: wl.to_f,
      radius_nm: 25.0,
      material: "Au",
      medium_refractive_index: 1.33
    )
    csv << [wl, result[:c_ext], result[:c_sca], result[:c_abs]]
  end
end
