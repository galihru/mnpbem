cmake_minimum_required(VERSION 3.15)
project(mnp_plasmon VERSION 0.1.0 LANGUAGES C)

set(CMAKE_C_STANDARD 99)
set(CMAKE_C_STANDARD_REQUIRED ON)

include(GNUInstallDirs)
include(CMakePackageConfigHelpers)

# Options
option(BUILD_TESTING "Build test executables" OFF)
option(BUILD_EXAMPLES "Build example programs" OFF)

# Library target
add_library(mnp_plasmon src/mnp_plasmon.c)
add_library(mnp_plasmon::mnp_plasmon ALIAS mnp_plasmon)
set_target_properties(mnp_plasmon PROPERTIES WINDOWS_EXPORT_ALL_SYMBOLS ON)
target_include_directories(mnp_plasmon PUBLIC
    $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/src>
    $<INSTALL_INTERFACE:${CMAKE_INSTALL_INCLUDEDIR}>
)

# Link math library on Unix-like systems
if(UNIX)
    target_link_libraries(mnp_plasmon PUBLIC m)
endif()

# Test executable (optional)
if(BUILD_TESTING)
    enable_testing()
    add_executable(mnp_plasmon_tests test/mnp_plasmon_tests.c)
    target_link_libraries(mnp_plasmon_tests PRIVATE mnp_plasmon)
    add_test(NAME mnp_plasmon_tests COMMAND mnp_plasmon_tests)
endif()

# Demo executable (optional)
if(BUILD_EXAMPLES)
    add_executable(demo examples/demo.c)
    target_link_libraries(demo PRIVATE mnp_plasmon)
endif()

# Installation
install(
    TARGETS mnp_plasmon
    EXPORT mnp_plasmon_targets
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
    ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
    INCLUDES DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}
)
install(FILES src/mnp_plasmon.h DESTINATION ${CMAKE_INSTALL_INCLUDEDIR})

# CMake package config files
install(
    EXPORT mnp_plasmon_targets
    FILE mnp_plasmonTargets.cmake
    NAMESPACE mnp_plasmon::
    DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/mnp_plasmon
)

configure_package_config_file(
    "${CMAKE_CURRENT_SOURCE_DIR}/cmake/mnp_plasmonConfig.cmake.in"
    "${CMAKE_CURRENT_BINARY_DIR}/mnp_plasmonConfig.cmake"
    INSTALL_DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/mnp_plasmon
)

write_basic_package_version_file(
    "${CMAKE_CURRENT_BINARY_DIR}/mnp_plasmonConfigVersion.cmake"
    VERSION ${PROJECT_VERSION}
    COMPATIBILITY AnyNewerVersion
)

install(
    FILES
        "${CMAKE_CURRENT_BINARY_DIR}/mnp_plasmonConfig.cmake"
        "${CMAKE_CURRENT_BINARY_DIR}/mnp_plasmonConfigVersion.cmake"
    DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/mnp_plasmon
)
