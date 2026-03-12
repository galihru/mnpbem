cmake_minimum_required(VERSION 3.15)
project(mnp_plasmon_cxx VERSION 0.1.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

include(GNUInstallDirs)
include(CMakePackageConfigHelpers)

# Options
option(BUILD_TESTING "Build test executables" OFF)
option(BUILD_EXAMPLES "Build example programs" OFF)

# Threads
find_package(Threads REQUIRED)

# Main library
add_library(mnp_plasmon_cxx src/mnp_plasmon.cpp)
add_library(mnp_plasmon_cxx::mnp_plasmon_cxx ALIAS mnp_plasmon_cxx)
target_include_directories(mnp_plasmon_cxx PUBLIC
    $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
    $<INSTALL_INTERFACE:${CMAKE_INSTALL_INCLUDEDIR}>
)
target_link_libraries(mnp_plasmon_cxx PUBLIC Threads::Threads)

# Demo executable (optional)
if(BUILD_EXAMPLES)
    add_executable(demo examples/demo.cpp)
    target_link_libraries(demo PRIVATE mnp_plasmon_cxx)
endif()

# Tests (optional, requires Google Test)
if(BUILD_TESTING)
    enable_testing()
    find_package(GTest QUIET)
    if(GTest_FOUND)
        add_executable(mnp_plasmon_test test/mnp_plasmon_test.cpp)
        target_link_libraries(mnp_plasmon_test PRIVATE mnp_plasmon_cxx GTest::GTest GTest::Main)
        add_test(NAME mnp_plasmon_test COMMAND mnp_plasmon_test)
    else()
        message(STATUS "GoogleTest not found - skipping tests")
    endif()
endif()

# Installation
install(
    TARGETS mnp_plasmon_cxx
    EXPORT mnp_plasmon_cxx_targets
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
    ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
    INCLUDES DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}
)
install(DIRECTORY include/ DESTINATION ${CMAKE_INSTALL_INCLUDEDIR})

# CMake package config files
install(
    EXPORT mnp_plasmon_cxx_targets
    FILE mnp_plasmon_cxxTargets.cmake
    NAMESPACE mnp_plasmon_cxx::
    DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/mnp_plasmon_cxx
)

configure_package_config_file(
    "${CMAKE_CURRENT_SOURCE_DIR}/cmake/mnp_plasmon_cxxConfig.cmake.in"
    "${CMAKE_CURRENT_BINARY_DIR}/mnp_plasmon_cxxConfig.cmake"
    INSTALL_DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/mnp_plasmon_cxx
)

write_basic_package_version_file(
    "${CMAKE_CURRENT_BINARY_DIR}/mnp_plasmon_cxxConfigVersion.cmake"
    VERSION ${PROJECT_VERSION}
    COMPATIBILITY AnyNewerVersion
)

install(
    FILES
        "${CMAKE_CURRENT_BINARY_DIR}/mnp_plasmon_cxxConfig.cmake"
        "${CMAKE_CURRENT_BINARY_DIR}/mnp_plasmon_cxxConfigVersion.cmake"
    DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/mnp_plasmon_cxx
)
