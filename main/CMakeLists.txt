# Exécutable principal
add_executable(GreenMindApp main.cpp)

# Link avec la lib (statique ou partagée)
target_link_libraries(GreenMindApp PRIVATE GreenMindLibShared)

# Très important : dire à CMake d’hériter aussi des includes publics de la lib
target_include_directories(GreenMindApp PRIVATE
    ${CMAKE_SOURCE_DIR}/lib/inc
)
