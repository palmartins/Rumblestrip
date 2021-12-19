cmake_minimum_required(VERSION 3.16.3)
project(Rumblestrip VERSION 0.1.0)

include(CTest)
enable_testing()

project(rumblestrip)

add_executable(${PROJECT_NAME} main.cpp src/lexer.cpp)
target_include_directories(${PROJECT_NAME} PUBLIC include)

set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)
