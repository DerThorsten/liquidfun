add_definitions(-DLIQUIDFUN_MULTI_GRAVITY=1)

#-------------------------------------------------------------------------------------------------------------------
# check for c++ 11 support
#-------------------------------------------------------------------------------------------------------------------
include(CheckCXXCompilerFlag)

if (CMAKE_CXX_COMPILER_ID MATCHES "Clang" OR CMAKE_CXX_COMPILER_ID MATCHES "GNU")
    CHECK_CXX_COMPILER_FLAG("-std=c++14" HAS_CPP14_FLAG)
    CHECK_CXX_COMPILER_FLAG("-std=c++11" HAS_CPP11_FLAG)
    if (HAS_CPP14_FLAG)
        set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++14")
    elseif (HAS_CPP11_FLAG)
        set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")
    else()
        message(FATAL_ERROR "Unsupported compiler -- nifty  requires C++11 support!")
    endif()
endif()



#FIND_PACKAGE(PYBIND_ELEVEN REQUIRED)
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/pybind11/include)
# Add a CMake parameter for choosing a desired Python version
set(PYTHON_VERSION "" CACHE STRING "Python version to use for compiling the example library")


# Try to autodetect Python (can be overridden manually if needed)
set(Python_ADDITIONAL_VERSIONS 3.4 3.5 3.6)
find_package(PythonLibs ${PYTHON_VERSION} REQUIRED)



if (CMAKE_CXX_COMPILER_ID MATCHES "Clang" OR CMAKE_CXX_COMPILER_ID MATCHES "GNU")
  # Enable C++11 mode on C++ / Clang
  set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

  # Enable link time optimization and set the default symbol
  # visibility to hidden (very important to obtain small binaries)
  if (NOT ${U_CMAKE_BUILD_TYPE} MATCHES DEBUG)
    # Default symbol visibility
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fvisibility=hidden")

    # Check for Link Time Optimization support
    #CHECK_CXX_COMPILER_FLAG("-flto" HAS_LTO_FLAG)
    #if (HAS_LTO_FLAG)
      set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -flto")
    #endif()
  endif()
endif()

# Include path for Python header files
include_directories(${PYTHON_INCLUDE_DIR})



# Create the binding library
add_library(pybox2d SHARED
  pybox2d.cxx
  b2Math.cxx
  b2World.cxx
  b2Body.cxx
  b2Fixture.cxx
  b2Shape.cxx
  b2Joint.cxx
  b2JointDef.cxx
  b2Particle.cxx
  b2ParticleSystem.cxx
  b2ParticleGroup.cxx
  b2WorldCallbacks.cxx
  b2Contact.cxx
  b2Collision.cxx
  b2Draw.cxx
  b2Vectorization.cxx
)
add_dependencies(pybox2d Box2D_shared)
#target_link_libraries(pybox2d ${Box2D})
# message(Box2D_shared)
# message(${Box2D})
# message("f")
target_link_libraries(pybox2d Box2D_shared)
# Don't add a 'lib' prefix to the shared library
set_target_properties(pybox2d PROPERTIES PREFIX "")

if (WIN32)
    if (MSVC)
        # Enforce size-based optimization and link time code generation
        # on MSVC (~30% smaller binaries in experiments). /bigobj is needed
        # for bigger binding projects due to the limit to 64k addressable sections
        # /MP enables multithreaded builds (relevant when there are many files).
        set_target_properties(pybox2d PROPERTIES COMPILE_FLAGS "/Os /GL /MP /bigobj")
        set_target_properties(pybox2d PROPERTIES LINK_FLAGS "/LTCG")
    endif()
    # .PYD file extension on Windows
    set_target_properties(pybox2d PROPERTIES SUFFIX ".pyd")
    # Link against the Python shared library
    target_link_libraries(pybox2d ${PYTHON_LIBRARY})
elseif (UNIX)
    # It's quite common to have multiple copies of the same Python version
    # installed on one's system. E.g.: one copy from the OS and another copy
    # that's statically linked into an application like Blender or Maya.
    # If we link our plugin library against the OS Python here and import it
    # into Blender or Maya later on, this will cause segfaults when multiple
    # conflicting Python instances are active at the same time.

    # Windows is not affected by this issue since it handles DLL imports
    # differently. The solution for Linux and Mac OS is simple: we just don't
    # link against the Python library. The resulting shared library will have
    # missing symbols, but that's perfectly fine -- they will be resolved at
    # import time.

    # .SO file extension on Linux/Mac OS
    set_target_properties(pybox2d PROPERTIES SUFFIX ".so")

    # Strip unnecessary sections of the binary on Linux/Mac OS
    if(APPLE)
        set_target_properties(pybox2d PROPERTIES MACOSX_RPATH ".")
        set_target_properties(pybox2d PROPERTIES LINK_FLAGS "-undefined dynamic_lookup -dead_strip")
        if (NOT ${U_CMAKE_BUILD_TYPE} MATCHES DEBUG)
            add_custom_command(TARGET pybox2d POST_BUILD COMMAND strip -u -r ${CMAKE_CURRENT_BINARY_DIR}/pybox2d.so)
        endif()
    else()
        if (NOT ${U_CMAKE_BUILD_TYPE} MATCHES DEBUG)
            add_custom_command(TARGET pybox2d POST_BUILD COMMAND strip ${CMAKE_CURRENT_BINARY_DIR}/pybox2d.so)
        endif()
    endif()
endif()

file(MAKE_DIRECTORY ${CMAKE_BINARY_DIR}/python/pybox2d)
file(MAKE_DIRECTORY ${CMAKE_BINARY_DIR}/test_python/)

ADD_CUSTOM_COMMAND(
        TARGET pybox2d
        POST_BUILD
        COMMAND ${CMAKE_COMMAND} ARGS -E copy_if_different $<TARGET_FILE:pybox2d> ${CMAKE_BINARY_DIR}/python/pybox2d/
        COMMENT "Copying target _graph to temporary module directory")



file(GLOB PYTHON_HEADERS
  ${CMAKE_SOURCE_DIR}/pybox2d/module/*.py
)

MATH(EXPR VAR "0")
FOREACH(file_path ${PYTHON_HEADERS})
    MATH(EXPR VAR "${VAR}+1")
    add_custom_target( copy_python_file_nr_${VAR} ALL#POST_BUILD
        COMMAND cmake -E copy_if_different 
        ${file_path}
        ${CMAKE_BINARY_DIR}/python/pybox2d/)
ENDFOREACH()






add_custom_target(copy_python_test ALL#POST_BUILD
    COMMAND cmake -E copy_if_different 
    ${CMAKE_SOURCE_DIR}/pybox2d/test/test.py 
    ${CMAKE_BINARY_DIR}/test_python/test.py)

