#include <pybind11/pybind11.h>

namespace py = pybind11;

void exportB2World(py::module & );
void exportB2Body(py::module & );
void exportB2Math(py::module & );
void exportB2Fixture(py::module & );
void exportB2Shape(py::module & );
void exportb2Joint(py::module & );
void exportB2WorldCallbacks(py::module & );
void exportContact(py::module & );
void exportB2Draw(py::module & );
void exportB2Particle(py::module & );

PYBIND11_PLUGIN(pybox2d) {
    py::module pybox2dModule("pybox2d", "pybox2d python bindings");

    exportB2World(pybox2dModule);
    exportB2Body(pybox2dModule);
    exportB2Math(pybox2dModule);
    exportB2Fixture(pybox2dModule);
    exportB2Shape(pybox2dModule);
    exportb2Joint(pybox2dModule);
    exportB2WorldCallbacks(pybox2dModule);
    exportContact(pybox2dModule);
    exportB2Draw(pybox2dModule);
    exportB2Particle(pybox2dModule);

    
    return pybox2dModule.ptr();
}
