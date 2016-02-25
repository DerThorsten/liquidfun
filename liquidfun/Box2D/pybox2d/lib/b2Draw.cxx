#include <pybind11/pybind11.h>
#include <Box2D/Box2D.h>

#include "pyb2Draw.hxx"

#include <iostream>

namespace py = pybind11;



void exportB2Draw(py::module & pybox2dModule){


    py::class_<b2Color>(pybox2dModule, "b2Color")
        .def_readwrite("r",&b2Color::r)
        .def_readwrite("g",&b2Color::g)
        .def_readwrite("b",&b2Color::b)
    ;

    py::class_<PyB2Draw>(pybox2dModule,"b2DrawCaller")
        .def(py::init<const py::object &>())
    ;
}


