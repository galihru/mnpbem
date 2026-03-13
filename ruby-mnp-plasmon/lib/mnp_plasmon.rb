require "complex"
require_relative "mnp_plasmon/version"

module MnpPlasmon
  HC_EV_NM = 1239.84197
  PI = Math::PI

  MATERIALS = {
    "Au" => { omega_p: 3.106, gamma: 0.0132, eps_inf: 8.90 },
    "Ag" => { omega_p: 3.810, gamma: 0.0048, eps_inf: 3.91 },
    "Al" => { omega_p: 14.83, gamma: 0.0980, eps_inf: 1.24 }
  }.freeze

  module_function

  def material_list
    MATERIALS.keys
  end

  def material_exists?(material)
    MATERIALS.key?(material)
  end

  def wavelength_to_energy(wavelength_nm)
    validate_positive!(wavelength_nm, "wavelength_nm")
    HC_EV_NM / wavelength_nm.to_f
  end

  def drude_epsilon(material, wavelength_nm)
    validate_material!(material)
    validate_positive!(wavelength_nm, "wavelength_nm")

    props = MATERIALS.fetch(material)
    omega = wavelength_to_energy(wavelength_nm)

    denominator = Complex(omega, 0.0) * Complex(omega, props[:gamma])
    Complex(props[:eps_inf], 0.0) - (props[:omega_p]**2 / denominator)
  end

  def rayleigh_polarizability(radius_nm, eps_particle, medium_refractive_index = 1.0)
    validate_positive!(radius_nm, "radius_nm")
    validate_positive!(medium_refractive_index, "medium_refractive_index")

    eps_m = medium_refractive_index**2
    volume = (4.0 / 3.0) * PI * (radius_nm**3)
    volume * (eps_particle - Complex(eps_m, 0.0)) / (eps_particle + Complex(2.0 * eps_m, 0.0))
  end

  def sphere_response(wavelength_nm:, radius_nm:, material:, medium_refractive_index: 1.0)
    eps_particle = drude_epsilon(material, wavelength_nm)
    alpha = rayleigh_polarizability(radius_nm, eps_particle, medium_refractive_index)

    k = 2.0 * PI * medium_refractive_index / wavelength_nm
    c_ext = (4.0 * PI / k) * alpha.imag.abs
    c_sca = ((k**4) / (6.0 * PI)) * (alpha.abs**2)
    c_abs = [c_ext - c_sca, 0.0].max

    {
      wavelength_nm: wavelength_nm,
      radius_nm: radius_nm,
      material: material,
      medium_refractive_index: medium_refractive_index,
      eps_particle: eps_particle,
      polarizability: alpha,
      c_ext: c_ext,
      c_sca: c_sca,
      c_abs: c_abs
    }
  end

  def validate_positive!(value, name)
    raise ArgumentError, "#{name} must be > 0" unless value.is_a?(Numeric) && value.positive?
  end
  private_class_method :validate_positive!

  def validate_material!(material)
    return if material_exists?(material)

    raise ArgumentError, "Unknown material: #{material}"
  end
  private_class_method :validate_material!
end
