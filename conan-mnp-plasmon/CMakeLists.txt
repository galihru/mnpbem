cmake_minimum_required(VERSION 3.15)
project(mnp_plasmon VERSION 0.1.0 LANGUAGES C)

set(CMAKE_C_STANDARD 99)
set(CMAKE_C_STANDARD_REQUIRED ON)

include(GNUInstallDirs)

option(BUILD_SHARED_LIBS "Build as shared library" OFF)

add_library(mnp_plasmon src/mnp_plasmon.c)
add_library(mnp_plasmon::mnp_plasmon ALIAS mnp_plasmon)

if(BUILD_SHARED_LIBS AND MSVC)
    set_target_properties(mnp_plasmon PROPERTIES WINDOWS_EXPORT_ALL_SYMBOLS ON)
endif()

target_include_directories(mnp_plasmon
    PUBLIC
        $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
        $<INSTALL_INTERFACE:${CMAKE_INSTALL_INCLUDEDIR}>
)

if(UNIX)
    target_link_libraries(mnp_plasmon PUBLIC m)
endif()

install(
    TARGETS mnp_plasmon
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
    ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
)
install(
    FILES include/mnp_plasmon.h
    DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}
)
