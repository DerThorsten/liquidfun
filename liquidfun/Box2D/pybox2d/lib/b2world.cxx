#include <pybind11/pybind11.h>

#include <Box2D/Box2D.h>

namespace py = pybind11;




void exportB2World(py::module & pybox2dModule){

    py::class_<b2World>(pybox2dModule,"b2World")
        .def(py::init<const b2Vec2 & >(),py::arg("gravity"))
        .def("CreateBody", &b2World::CreateBody, py::return_value_policy::reference_internal)
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
    ;

}

