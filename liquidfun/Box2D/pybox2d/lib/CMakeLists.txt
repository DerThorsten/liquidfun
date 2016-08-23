add_definitions(-DLIQUIDFUN_MULTI_GRAVITY=1)


add_definitions(-DPYBIND11_HAS_NO_STD_TO_STRING=1)
add_definitions(-DPYBIND11_HAS_NO_STD_TO_STRING)

add_definitions(-DPYBIND11_NO_EXCEPTION_PTR=1)
add_definitions(-DPYBIND11_NO_EXCEPTION_PTR)

cmake_minimum_required(VERSION 2.8.12)
project(example)

add_subdirectory(pybind11-master)
pybind11_add_module(_pybox2d 
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




add_dependencies(_pybox2d Box2D_shared)
#target_link_libraries(pybox2d ${Box2D})
# message(Box2D_shared)
# message(${Box2D})
# message("f")
target_link_libraries(_pybox2d Box2D_shared)
# Don't add a 'lib' prefix to the shared library
set_target_properties(_pybox2d PROPERTIES PREFIX "")



file(MAKE_DIRECTORY ${CMAKE_BINARY_DIR}/python/pybox2d)
file(MAKE_DIRECTORY ${CMAKE_BINARY_DIR}/test_python/)

ADD_CUSTOM_COMMAND(
        TARGET _pybox2d
        POST_BUILD
        COMMAND ${CMAKE_COMMAND} ARGS -E copy_if_different $<TARGET_FILE:_pybox2d> ${CMAKE_BINARY_DIR}/python/pybox2d/
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

