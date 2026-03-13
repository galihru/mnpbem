# mnp_plasmon

Ruby implementation of the Drude + Rayleigh nanoparticle optical response model.

## Install

```bash
gem install mnp_plasmon
```

## Quick Start

```ruby
require "mnp_plasmon"

result = MnpPlasmon.sphere_response(
  wavelength_nm: 550.0,
  radius_nm: 25.0,
  material: "Au",
  medium_refractive_index: 1.0
)

puts result[:c_ext]
puts result[:c_sca]
puts result[:c_abs]
```
