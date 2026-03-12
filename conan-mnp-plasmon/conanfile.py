from conan import ConanFile
from conan.tools.cmake import CMake, CMakeToolchain, cmake_layout
from conan.tools.files import copy, get
import os


class MnpPlasmonConan(ConanFile):
    name = "mnp-plasmon"
    version = "0.1.0"
    description = (
        "Drude dielectric model and Rayleigh quasi-static approximation "
        "for computing optical cross-sections of metallic nanoparticles."
    )
    topics = ("plasmonics", "nanoparticles", "optics", "physics", "drude")
    url = "https://github.com/galihru/mnpbem"
    homepage = "https://github.com/galihru/mnpbem"
    license = "GPL-3.0-only"

    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}

    exports_sources = "CMakeLists.txt", "include/*", "src/*"

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def layout(self):
        cmake_layout(self)

    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        copy(
            self,
            "*.h",
            src=os.path.join(self.source_folder, "include"),
            dst=os.path.join(self.package_folder, "include"),
        )
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["mnp_plasmon"]
        if self.settings.os in ("Linux", "FreeBSD"):
            self.cpp_info.system_libs = ["m"]
