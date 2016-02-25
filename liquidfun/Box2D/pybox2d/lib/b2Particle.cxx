#include <pybind11/pybind11.h>

#include <Box2D/Box2D.h>

namespace py = pybind11;






void exportB2Particle(py::module & pybox2dModule){


    py::class_<b2ParticleColor>(pybox2dModule, "b2ParticleColor")
    ;

}


