cmake_minimum_required(VERSION 3.16)
project(GreenMind VERSION 0.1.0 LANGUAGES CXX)

# Utiliser g++
set(CMAKE_CXX_COMPILER g++)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Inclure les sous-répertoires
add_subdirectory(lib)
add_subdirectory(main)

# test
enable_testing()
add_subdirectory(test)
