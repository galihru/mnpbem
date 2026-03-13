# frozen_string_literal: true

require "minitest/autorun"
require_relative "../lib/mnp_plasmon"

class TestMnpPlasmon < Minitest::Test
  def test_material_lookup
    assert MnpPlasmon.material_exists?("Au")
    refute MnpPlasmon.material_exists?("Cu")
  end

  def test_drude_returns_complex
    eps = MnpPlasmon.drude_epsilon("Au", 550.0)
    assert_instance_of Complex, eps
    assert eps.real.finite?
  end

  def test_sphere_response_positive_sections
    r = MnpPlasmon.sphere_response(
      wavelength_nm: 550.0,
      radius_nm: 25.0,
      material: "Au"
    )

    assert r[:c_ext] > 0
    assert r[:c_sca] >= 0
    assert r[:c_abs] >= 0
  end
end
