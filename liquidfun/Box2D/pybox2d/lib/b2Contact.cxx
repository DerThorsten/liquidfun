#include <pybind11/pybind11.h>
#include <pybind11/operators.h>
#include <Box2D/Box2D.h>
namespace py = pybind11;




void exportContact(py::module & pybox2dModule){



    py::class_<b2ContactEdge>(pybox2dModule,"b2ContactEdge")

    ;

    py::class_<b2Contact>(pybox2dModule,"b2Contact")

    ;



}
