add_definitions(-DLIQUIDFUN_MULTI_GRAVITY=1)


add_definitions(-DPYBIND11_HAS_NO_STD_TO_STRING=1)
add_definitions(-DPYBIND11_HAS_NO_STD_TO_STRING)

add_definitions(-DPYBIND11_NO_EXCEPTION_PTR=1)
add_definitions(-DPYBIND11_NO_EXCEPTION_PTR)

cmake_minimum_required(VERSION 2.8.12)
project(example)



set(BOX2D_Collision_SRCS
  ${CMAKE_SOURCE_DIR}/Box2D/Collision/b2BroadPhase.cpp
  ${CMAKE_SOURCE_DIR}/Box2D/Collision/b2CollideCircle.cpp
  ${CMAKE_SOURCE_DIR}/Box2D/Collision/b2CollideEdge.cpp
  ${CMAKE_SOURCE_DIR}/Box2D/Collision/b2CollidePolygon.cpp
  ${CMAKE_SOURCE_DIR}/Box2D/Collision/b2Collision.cpp
  ${CMAKE_SOURCE_DIR}/Box2D/Collision/b2Distance.cpp
  ${CMAKE_SOURCE_DIR}/Box2D/Collision/b2DynamicTree.cpp
  ${CMAKE_SOURCE_DIR}/Box2D/Collision/b2TimeOfImpact.cpp
)
set(BOX2D_Collision_HDRS
  ${CMAKE_SOURCE_DIR}/Box2D/Collision/b2BroadPhase.h
  ${CMAKE_SOURCE_DIR}/Box2D/Collision/b2Collision.h
  ${CMAKE_SOURCE_DIR}/Box2D/Collision/b2Distance.h
  ${CMAKE_SOURCE_DIR}/Box2D/Collision/b2DynamicTree.h
  ${CMAKE_SOURCE_DIR}/Box2D/Collision/b2TimeOfImpact.h
)
set(BOX2D_Shapes_SRCS
  ${CMAKE_SOURCE_DIR}/Box2D/Collision/Shapes/b2CircleShape.cpp
  ${CMAKE_SOURCE_DIR}/Box2D/Collision/Shapes/b2EdgeShape.cpp
  ${CMAKE_SOURCE_DIR}/Box2D/Collision/Shapes/b2ChainShape.cpp
  ${CMAKE_SOURCE_DIR}/Box2D/Collision/Shapes/b2PolygonShape.cpp
)
set(BOX2D_Shapes_HDRS
  ${CMAKE_SOURCE_DIR}/Box2D/Collision/Shapes/b2CircleShape.h
  ${CMAKE_SOURCE_DIR}/Box2D/Collision/Shapes/b2EdgeShape.h
  ${CMAKE_SOURCE_DIR}/Box2D/Collision/Shapes/b2ChainShape.h
  ${CMAKE_SOURCE_DIR}/Box2D/Collision/Shapes/b2PolygonShape.h
  ${CMAKE_SOURCE_DIR}/Box2D/Collision/Shapes/b2Shape.h
)
set(BOX2D_Common_SRCS
  ${CMAKE_SOURCE_DIR}/Box2D/Common/b2BlockAllocator.cpp
  ${CMAKE_SOURCE_DIR}/Box2D/Common/b2Draw.cpp
  ${CMAKE_SOURCE_DIR}/Box2D/Common/b2FreeList.cpp
  ${CMAKE_SOURCE_DIR}/Box2D/Common/b2Math.cpp
  ${CMAKE_SOURCE_DIR}/Box2D/Common/b2Settings.cpp
  ${CMAKE_SOURCE_DIR}/Box2D/Common/b2StackAllocator.cpp
  ${CMAKE_SOURCE_DIR}/Box2D/Common/b2Stat.cpp
  ${CMAKE_SOURCE_DIR}/Box2D/Common/b2Timer.cpp
  ${CMAKE_SOURCE_DIR}/Box2D/Common/b2TrackedBlock.cpp
)
set(BOX2D_Common_HDRS
  ${CMAKE_SOURCE_DIR}/Box2D/Common/b2BlockAllocator.h
  ${CMAKE_SOURCE_DIR}/Box2D/Common/b2Draw.h
  ${CMAKE_SOURCE_DIR}/Box2D/Common/b2FreeList.h
  ${CMAKE_SOURCE_DIR}/Box2D/Common/b2GrowableStack.h
  ${CMAKE_SOURCE_DIR}/Box2D/Common/b2IntrusiveList.h
  ${CMAKE_SOURCE_DIR}/Box2D/Common/b2Math.h
  ${CMAKE_SOURCE_DIR}/Box2D/Common/b2Settings.h
  ${CMAKE_SOURCE_DIR}/Box2D/Common/b2SlabAllocator.h
  ${CMAKE_SOURCE_DIR}/Box2D/Common/b2StackAllocator.h
  ${CMAKE_SOURCE_DIR}/Box2D/Common/b2Stat.h
  ${CMAKE_SOURCE_DIR}/Box2D/Common/b2Timer.h
  ${CMAKE_SOURCE_DIR}/Box2D/Common/b2TrackedBlock.h
)
set(BOX2D_Dynamics_SRCS
  ${CMAKE_SOURCE_DIR}/Box2D/Dynamics/b2Body.cpp
  ${CMAKE_SOURCE_DIR}/Box2D/Dynamics/b2ContactManager.cpp
  ${CMAKE_SOURCE_DIR}/Box2D/Dynamics/b2Fixture.cpp
  ${CMAKE_SOURCE_DIR}/Box2D/Dynamics/b2Island.cpp
  ${CMAKE_SOURCE_DIR}/Box2D/Dynamics/b2World.cpp
  ${CMAKE_SOURCE_DIR}/Box2D/Dynamics/b2WorldCallbacks.cpp
)
set(BOX2D_Dynamics_HDRS
  ${CMAKE_SOURCE_DIR}/Box2D/Dynamics/b2Body.h
  ${CMAKE_SOURCE_DIR}/Box2D/Dynamics/b2ContactManager.h
  ${CMAKE_SOURCE_DIR}/Box2D/Dynamics/b2Fixture.h
  ${CMAKE_SOURCE_DIR}/Box2D/Dynamics/b2Island.h
  ${CMAKE_SOURCE_DIR}/Box2D/Dynamics/b2TimeStep.h
  ${CMAKE_SOURCE_DIR}/Box2D/Dynamics/b2World.h
  ${CMAKE_SOURCE_DIR}/Box2D/Dynamics/b2WorldCallbacks.h
)
set(BOX2D_Contacts_SRCS
  ${CMAKE_SOURCE_DIR}/Box2D/Dynamics/Contacts/b2CircleContact.cpp
  ${CMAKE_SOURCE_DIR}/Box2D/Dynamics/Contacts/b2Contact.cpp
  ${CMAKE_SOURCE_DIR}/Box2D/Dynamics/Contacts/b2ContactSolver.cpp
  ${CMAKE_SOURCE_DIR}/Box2D/Dynamics/Contacts/b2PolygonAndCircleContact.cpp
  ${CMAKE_SOURCE_DIR}/Box2D/Dynamics/Contacts/b2EdgeAndCircleContact.cpp
  ${CMAKE_SOURCE_DIR}/Box2D/Dynamics/Contacts/b2EdgeAndPolygonContact.cpp
  ${CMAKE_SOURCE_DIR}/Box2D/Dynamics/Contacts/b2ChainAndCircleContact.cpp
  ${CMAKE_SOURCE_DIR}/Box2D/Dynamics/Contacts/b2ChainAndPolygonContact.cpp
  ${CMAKE_SOURCE_DIR}/Box2D/Dynamics/Contacts/b2PolygonContact.cpp
)
set(BOX2D_Contacts_HDRS
  ${CMAKE_SOURCE_DIR}/Box2D/Dynamics/Contacts/b2CircleContact.h
  ${CMAKE_SOURCE_DIR}/Box2D/Dynamics/Contacts/b2Contact.h
  ${CMAKE_SOURCE_DIR}/Box2D/Dynamics/Contacts/b2ContactSolver.h
  ${CMAKE_SOURCE_DIR}/Box2D/Dynamics/Contacts/b2PolygonAndCircleContact.h
  ${CMAKE_SOURCE_DIR}/Box2D/Dynamics/Contacts/b2EdgeAndCircleContact.h
  ${CMAKE_SOURCE_DIR}/Box2D/Dynamics/Contacts/b2EdgeAndPolygonContact.h
  ${CMAKE_SOURCE_DIR}/Box2D/Dynamics/Contacts/b2ChainAndCircleContact.h
  ${CMAKE_SOURCE_DIR}/Box2D/Dynamics/Contacts/b2ChainAndPolygonContact.h
  ${CMAKE_SOURCE_DIR}/Box2D/Dynamics/Contacts/b2PolygonContact.h
)
set(BOX2D_Joints_SRCS
  ${CMAKE_SOURCE_DIR}/Box2D/Dynamics/Joints/b2DistanceJoint.cpp
  ${CMAKE_SOURCE_DIR}/Box2D/Dynamics/Joints/b2FrictionJoint.cpp
  ${CMAKE_SOURCE_DIR}/Box2D/Dynamics/Joints/b2GearJoint.cpp
  ${CMAKE_SOURCE_DIR}/Box2D/Dynamics/Joints/b2Joint.cpp
  ${CMAKE_SOURCE_DIR}/Box2D/Dynamics/Joints/b2MotorJoint.cpp
  ${CMAKE_SOURCE_DIR}/Box2D/Dynamics/Joints/b2MouseJoint.cpp
  ${CMAKE_SOURCE_DIR}/Box2D/Dynamics/Joints/b2MotorJoint.cpp
  ${CMAKE_SOURCE_DIR}/Box2D/Dynamics/Joints/b2PrismaticJoint.cpp
  ${CMAKE_SOURCE_DIR}/Box2D/Dynamics/Joints/b2PulleyJoint.cpp
  ${CMAKE_SOURCE_DIR}/Box2D/Dynamics/Joints/b2RevoluteJoint.cpp
  ${CMAKE_SOURCE_DIR}/Box2D/Dynamics/Joints/b2RopeJoint.cpp
  ${CMAKE_SOURCE_DIR}/Box2D/Dynamics/Joints/b2WeldJoint.cpp
  ${CMAKE_SOURCE_DIR}/Box2D/Dynamics/Joints/b2WheelJoint.cpp
)
set(BOX2D_Joints_HDRS
  ${CMAKE_SOURCE_DIR}/Box2D/Dynamics/Joints/b2DistanceJoint.h
  ${CMAKE_SOURCE_DIR}/Box2D/Dynamics/Joints/b2FrictionJoint.h
  ${CMAKE_SOURCE_DIR}/Box2D/Dynamics/Joints/b2GearJoint.h
  ${CMAKE_SOURCE_DIR}/Box2D/Dynamics/Joints/b2Joint.h
  ${CMAKE_SOURCE_DIR}/Box2D/Dynamics/Joints/b2MotorJoint.h
  ${CMAKE_SOURCE_DIR}/Box2D/Dynamics/Joints/b2MouseJoint.h
  ${CMAKE_SOURCE_DIR}/Box2D/Dynamics/Joints/b2PrismaticJoint.h
  ${CMAKE_SOURCE_DIR}/Box2D/Dynamics/Joints/b2PulleyJoint.h
  ${CMAKE_SOURCE_DIR}/Box2D/Dynamics/Joints/b2RevoluteJoint.h
  ${CMAKE_SOURCE_DIR}/Box2D/Dynamics/Joints/b2RopeJoint.h
  ${CMAKE_SOURCE_DIR}/Box2D/Dynamics/Joints/b2WeldJoint.h
  ${CMAKE_SOURCE_DIR}/Box2D/Dynamics/Joints/b2WheelJoint.h
)
set(BOX2D_Particle_SRCS
  ${CMAKE_SOURCE_DIR}/Box2D/Particle/b2Particle.cpp
  ${CMAKE_SOURCE_DIR}/Box2D/Particle/b2ParticleGroup.cpp
  ${CMAKE_SOURCE_DIR}/Box2D/Particle/b2ParticleSystem.cpp
  ${CMAKE_SOURCE_DIR}/Box2D/Particle/b2VoronoiDiagram.cpp
)
set(BOX2D_Particle_HDRS
  ${CMAKE_SOURCE_DIR}/Box2D/Particle/b2Particle.h
  ${CMAKE_SOURCE_DIR}/Box2D/Particle/b2ParticleGroup.h
  ${CMAKE_SOURCE_DIR}/Box2D/Particle/b2ParticleSystem.h
  ${CMAKE_SOURCE_DIR}/Box2D/Particle/b2StackQueue.h
  ${CMAKE_SOURCE_DIR}/Box2D/Particle/b2VoronoiDiagram.h
)
set(BOX2D_Rope_SRCS
  ${CMAKE_SOURCE_DIR}/Box2D/Rope/b2Rope.cpp
)
set(BOX2D_Rope_HDRS
  ${CMAKE_SOURCE_DIR}/Box2D/Rope/b2Rope.h
)
set(BOX2D_General_HDRS
  ${CMAKE_SOURCE_DIR}/Box2D/Box2D.h
)



















add_subdirectory(pybind11-2.2.0)
pybind11_add_module(_pybox2d 

  ${BOX2D_General_HDRS}
  ${BOX2D_Joints_SRCS}
  ${BOX2D_Joints_HDRS}
  ${BOX2D_Contacts_SRCS}
  ${BOX2D_Contacts_HDRS}
  ${BOX2D_Dynamics_SRCS}
  ${BOX2D_Dynamics_HDRS}
  ${BOX2D_Common_SRCS}
  ${BOX2D_Common_HDRS}
  ${BOX2D_Shapes_SRCS}
  ${BOX2D_Shapes_HDRS}
  ${BOX2D_Collision_SRCS}
  ${BOX2D_Collision_HDRS}
  ${BOX2D_Particle_SRCS}
  ${BOX2D_Particle_HDRS}
  ${BOX2D_Rope_SRCS}
  ${BOX2D_Rope_HDRS}

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




#add_dependencies(_pybox2d Box2D_shared)
#target_link_libraries(pybox2d ${Box2D})
# message(Box2D_shared)
# message(${Box2D})
# message("f")
#target_link_libraries(_pybox2d Box2D_shared)
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

