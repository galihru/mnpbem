require_relative "lib/mnp_plasmon/version"

Gem::Specification.new do |spec|
  spec.name = "mnp_plasmon"
  spec.version = MnpPlasmon::VERSION
  spec.authors = ["Galih Ridho Utomo"]
  spec.email = ["g4lihru@students.unnes.ac.id"]

  spec.summary = "Drude + Rayleigh plasmonics calculator for metallic nanoparticles"
  spec.description = "Cross-language MnpPlasmon Ruby implementation for optical response simulation of spherical metallic nanoparticles."
  spec.homepage = "https://github.com/galihru/mnpbem"
  spec.license = "GPL-3.0-only"
  spec.required_ruby_version = ">= 3.0"

  spec.metadata["homepage_uri"] = spec.homepage
  spec.metadata["source_code_uri"] = "https://github.com/galihru/mnpbem/tree/main/ruby-mnp-plasmon"
  spec.metadata["changelog_uri"] = "https://github.com/galihru/mnpbem/releases"

  spec.files = Dir.chdir(__dir__) do
    Dir["lib/**/*", "README.md", "LICENSE"]
  end

  spec.bindir = "exe"
  spec.executables = []
  spec.require_paths = ["lib"]
end
