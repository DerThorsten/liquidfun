#include <pybind11/pybind11.h>
#include <pybind11/operators.h>
#include <Box2D/Box2D.h>
namespace py = pybind11;




void exportb2Collision(py::module & pybox2dModule){



    py::class_<b2AABB>(pybox2dModule,"b2AABB")
        .def(py::init<>())
        .def_readwrite("lowerBound",&b2AABB::lowerBound)
        .def_readwrite("upperBound",&b2AABB::upperBound)
    ;


    py::class_<b2Manifold>(pybox2dModule,"b2Manifold")
        .def(py::init<>())
    ;

    py::class_<b2WorldManifold>(pybox2dModule,"b2WorldManifold")
        .def(py::init<>())
    ;
}
