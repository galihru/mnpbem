cmake_minimum_required(VERSION 3.15)
project(mnp_plasmon_cxx VERSION 0.1.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Threads
find_package(Threads REQUIRED)

# Main library
add_library(mnp_plasmon src/mnp_plasmon.cpp)
target_include_directories(mnp_plasmon PUBLIC
    $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
    $<INSTALL_INTERFACE:include>
)
target_link_libraries(mnp_plasmon PUBLIC Threads::Threads)

# Demo executable
add_executable(demo examples/demo.cpp)
target_link_libraries(demo PRIVATE mnp_plasmon)

# Tests
enable_testing()

# Google Test - Optional
find_package(GTest QUIET)
if(GTest_FOUND)
    add_executable(mnp_plasmon_test test/mnp_plasmon_test.cpp)
    target_link_libraries(mnp_plasmon_test PRIVATE mnp_plasmon GTest::GTest GTest::Main)
    add_test(NAME mnp_plasmon_test COMMAND mnp_plasmon_test)
else()
    message(STATUS "GoogleTest not found - skipping tests")
endif()

# Installation
install(TARGETS mnp_plasmon
    LIBRARY DESTINATION lib
    ARCHIVE DESTINATION lib
    RUNTIME DESTINATION bin
)
install(DIRECTORY include/ DESTINATION include)
