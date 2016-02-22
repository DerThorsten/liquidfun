#include <pybind11/pybind11.h>

#include <Box2D/Box2D.h>

namespace py = pybind11;



void exportB2Fixture(py::module & pybox2dModule){


    py::class_<b2Filter>(pybox2dModule,"b2Filter")
        .def(py::init<>())
        .def_readwrite("categoryBits", &b2Filter::categoryBits)
        .def_readwrite("maskBits", &b2Filter::maskBits)
        .def_readwrite("groupIndex", &b2Filter::groupIndex)
    ;


    py::class_<b2FixtureDef>(pybox2dModule,"b2FixtureDef")
        .def(py::init<>())
        .def_readwrite("shape", &b2FixtureDef::shape)
        //.def_readwrite("userData", &b2FixtureDef::userData)
        .def_readwrite("friction", &b2FixtureDef::friction)
        .def_readwrite("restitution", &b2FixtureDef::restitution)
        .def_readwrite("density", &b2FixtureDef::density)
        .def_readwrite("isSensor", &b2FixtureDef::isSensor)
        .def_readwrite("filter", &b2FixtureDef::filter)
    ;

    py::class_<b2Fixture>(pybox2dModule,"b2Fixture")
        .def("GetType", &b2Fixture::GetType)
        .def("GetShape", [](b2Fixture & f) {return f.GetShape();}, py::return_value_policy::reference_internal)
        .def("SetSensor", &b2Fixture::SetSensor,py::arg("sensor`"))
        .def("IsSensor", &b2Fixture::IsSensor)
        .def("GetBody", [](b2Fixture & f) {return f.GetBody();}, py::return_value_policy::reference_internal)
        .def("HasNext", [](b2Fixture &f){
            auto next = f.GetNext();
            return next != nullptr;
        })
        .def("_GetNext", [](b2Fixture &f){
            auto next = f.GetNext();
            return next;
        }, py::return_value_policy::reference_internal)
    ;

}

