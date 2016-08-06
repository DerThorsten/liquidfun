#include <pybind11/pybind11.h>

#include <Box2D/Box2D.h>
#include "pyb2WorldCallbacks.hxx"
namespace py = pybind11;







void exportB2WorldCallbacks(py::module & pybox2dModule){


    py::class_<b2ContactImpulse>(pybox2dModule,"b2ContactImpulse")
        .def_readonly("normalImpulses",&b2ContactImpulse::normalImpulses)
        .def_readonly("tangentImpulses",&b2ContactImpulse::tangentImpulses)
        .def_readonly("count",&b2ContactImpulse::count)
    ;


    py::class_<PyB2QueryCallbackCaller>(pybox2dModule,"b2QueryCallbackCaller")
        .def(py::init<const py::object &>(),py::arg("queryCallback")
        )
    ;

    py::class_<PyB2RayCastCallbackCaller>(pybox2dModule,"b2RayCastCallbackCaller")
        .def(py::init<const py::object &>(),py::arg("rayCastCallback")
        )
    ;

    py::class_<PyB2DestructionListenerCaller>(pybox2dModule,"b2DestructionListenerCaller")
        .def(py::init<const py::object &>(),py::arg("destructionListener")
        )
    ;
  
    py::class_<PyB2ContactListenerCaller>(pybox2dModule,"b2ContactListenerCaller")
        .def(py::init<const py::object &>(),py::arg("contactListener")
        )
    ;
   

 


   

}


