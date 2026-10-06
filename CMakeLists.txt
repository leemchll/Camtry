cmake_minimum_required(VERSION 3.20)

project(Camtry)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(OpenCV REQUIRED)

set(ONNXRUNTIME_ROOT "/opt/homebrew/opt/onnxruntime")

add_executable(camtry src/main.cpp)

target_include_directories(camtry PRIVATE
    ${OpenCV_INCLUDE_DIRS}
    ${ONNXRUNTIME_ROOT}/include
)

target_link_directories(camtry PRIVATE
    ${ONNXRUNTIME_ROOT}/lib
)

target_link_libraries(camtry PRIVATE
    ${OpenCV_LIBS}
    onnxruntime
)