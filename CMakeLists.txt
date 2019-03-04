cmake_minimum_required(VERSION 2.8) 
                        
execute_process(COMMAND python3 preparing.py WORKING_DIRECTORY ${PROJECT_SOURCE_DIR}/A)

set(SOURCE_EXE C/main.cpp)

include_directories(B)

include_directories(.)

add_executable(main ${SOURCE_EXE})

add_subdirectory(B)

target_link_libraries(main lib)


