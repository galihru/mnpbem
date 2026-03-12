cmake_minimum_required(VERSION 3.15)
project(mnp_plasmon VERSION 0.1.0 LANGUAGES C)

set(CMAKE_C_STANDARD 99)
set(CMAKE_C_STANDARD_REQUIRED ON)

# Library target
add_library(mnp_plasmon src/mnp_plasmon.c)
target_include_directories(mnp_plasmon PUBLIC
    $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/src>
    $<INSTALL_INTERFACE:include>
)

# Link math library on Unix-like systems
if(UNIX)
    target_link_libraries(mnp_plasmon PUBLIC m)
endif()

# Test executable
enable_testing()
add_executable(mnp_plasmon_tests test/mnp_plasmon_tests.c)
target_link_libraries(mnp_plasmon_tests PRIVATE mnp_plasmon)
add_test(NAME mnp_plasmon_tests COMMAND mnp_plasmon_tests)

# Demo executable
add_executable(demo examples/demo.c)
target_link_libraries(demo PRIVATE mnp_plasmon)

# Installation
install(TARGETS mnp_plasmon
    LIBRARY DESTINATION lib
    ARCHIVE DESTINATION lib
    RUNTIME DESTINATION bin
)
install(FILES src/mnp_plasmon.h DESTINATION include)
