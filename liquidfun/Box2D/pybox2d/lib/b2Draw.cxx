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
        .def(py::init<const py::object &,const float32, const b2Vec2 & , const bool>(),
            py::arg("debugDraw"),py::arg("scale")=5.0,py::arg("offset")=b2Vec2(0,0),py::arg("flipY")=false
        )
        .def("SetFlags",[](PyB2Draw * draw,const int flag){draw->SetFlags(flag);})
        .def("GetFlags",[](PyB2Draw * draw){return draw->GetFlags();})
        .def("AppendFlags",[](PyB2Draw * draw,const int flag){draw->AppendFlags(flag);})
        .def("ClearFlags",[](PyB2Draw * draw,const int flag){draw->ClearFlags(flag);})
        .def_readwrite("scale",&PyB2Draw::scale_)
    ;
}


