cmake_minimum_required(VERSION 3.15)
project(test_package LANGUAGES C)

find_package(mnp-plasmon REQUIRED)

add_executable(example src/example.c)
target_link_libraries(example PRIVATE mnp_plasmon::mnp_plasmon)
