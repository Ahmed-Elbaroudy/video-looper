cmake_minimum_required(VERSION 3.10)
project(VideoLooper)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(OpenCV REQUIRED)

add_executable(VideoLooper main.cpp)
target_link_libraries(VideoLooper PRIVATE ${OpenCV_LIBS})
