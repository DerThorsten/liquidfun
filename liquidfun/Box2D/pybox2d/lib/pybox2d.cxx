#include <pybind11/pybind11.h>

namespace py = pybind11;

void exportB2World(py::module & pybox2dModule);
void exportB2Body(py::module & pybox2dModule);
void exportB2Math(py::module & pybox2dModule);
void exportB2Fixture(py::module & pybox2dModule);
void exportB2Shape(py::module & pybox2dModule);
void exportb2Joint(py::module & pybox2dModule);

PYBIND11_PLUGIN(pybox2d) {
    py::module pybox2dModule("pybox2d", "pybox2d python bindings");

    exportB2World(pybox2dModule);
    exportB2Body(pybox2dModule);
    exportB2Math(pybox2dModule);
    exportB2Fixture(pybox2dModule);
    exportB2Shape(pybox2dModule);
    exportb2Joint(pybox2dModule);

    return pybox2dModule.ptr();
}
