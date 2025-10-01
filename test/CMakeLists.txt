# Utiliser GTest installé sur le système
find_package(GTest REQUIRED)

add_executable(GreenMindTests test_main.cpp)

target_link_libraries(GreenMindTests
    PRIVATE
        GTest::GTest
        GTest::Main
        GreenMindLibShared
)

target_include_directories(GreenMindTests PRIVATE
    ${CMAKE_SOURCE_DIR}/lib/inc
)

include(GoogleTest)
gtest_discover_tests(GreenMindTests)
