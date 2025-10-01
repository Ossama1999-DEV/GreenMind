# Bibliothèque statique (.a)
add_library(GreenMindLibStatic STATIC
    src/version.cpp
)

# Bibliothèque dynamique (.so)
add_library(GreenMindLibShared SHARED
    src/version.cpp
)

# Répertoires include
target_include_directories(GreenMindLibStatic PUBLIC
    ${CMAKE_CURRENT_SOURCE_DIR}/inc
)
target_include_directories(GreenMindLibShared PUBLIC
    ${CMAKE_CURRENT_SOURCE_DIR}/inc
)

# Pour que la lib .so ait un nom propre sans "libShared"
set_target_properties(GreenMindLibShared PROPERTIES OUTPUT_NAME "GreenMindLib")
set_target_properties(GreenMindLibStatic PROPERTIES OUTPUT_NAME "GreenMindLib")
