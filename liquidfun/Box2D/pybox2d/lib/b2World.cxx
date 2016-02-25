#include <pybind11/pybind11.h>

#include <Box2D/Box2D.h>
#include "pyb2Draw.hxx"

namespace py = pybind11;




void exportB2World(py::module & pybox2dModule){

    py::class_<b2World>(pybox2dModule,"b2World")
        .def(py::init<const b2Vec2 & >(),py::arg("gravity"))
        .def("_CreateBodyCpp", &b2World::CreateBody, py::return_value_policy::reference_internal)
        .def("DestroyBody", &b2World::DestroyBody,py::arg("body"))
        .def("Step",[&]
            (b2World & self, float32 timeStep, 
            int32 velocityIterations, int32 positionIterations,
            int32 particleIterations){

                self.Step(timeStep, velocityIterations, positionIterations,particleIterations);
            },
            py::arg("timeStep"),
            py::arg("velocityIterations"),
            py::arg("positionIterations"),
            py::arg("particleIterations") = 1
        )
        .def("SetDestructionListener", &b2World::SetDestructionListener , py::arg("listener"))
        .def("SetContactFilter", &b2World::SetContactFilter , py::arg("filter"))
        .def("SetContactListener", &b2World::SetContactListener , py::arg("listener"))


        .def("SetDebugDraw", 
        [](b2World & w, PyB2Draw * d){
            w.SetDebugDraw(d);
        },
        py::arg("debugDraw"))
        .def("DrawDebugData",&b2World::DrawDebugData)

        .def("GetProxyCount",&b2World::GetProxyCount)
        .def("GetBodyCount",&b2World::GetBodyCount)
        .def("GetJointCount",&b2World::GetJointCount)
        .def("GetContactCount",&b2World::GetContactCount)
        .def("GetTreeHeight",&b2World::GetTreeHeight)
        .def("GetTreeBalance",&b2World::GetTreeBalance)
        .def("GetTreeQuality",&b2World::GetTreeQuality)

        .def("CreateJoint",&b2World::CreateJoint,py::return_value_policy::reference_internal)


        // lists
        .def("_GetBodyList", [](const b2World & w){
            return  w.GetBodyList();
        }, py::return_value_policy::reference_internal)
        .def("_GetBodyList", []( b2World & w){
            return  w.GetBodyList();
        }, py::return_value_policy::reference_internal)

        .def("_GetJointList", [](const b2World & w){
            return  w.GetJointList();
        }, py::return_value_policy::reference_internal)
        .def("_GetJointList", []( b2World & w){
            return  w.GetJointList();
        }, py::return_value_policy::reference_internal)


        // particles
        .def("CreateParticleSystem",&b2World::CreateParticleSystem, py::return_value_policy::reference_internal)
    ;

}

