#include <pybind11/pybind11.h>

#include <Box2D/Box2D.h>

#include <vector>

#include "holder.hxx"
#include "user_data.hxx"

namespace py = pybind11;






void exportB2Particle(py::module & pybox2dModule){


    py::class_<b2ParticleColor>(pybox2dModule, "b2ParticleColor")
        .def(py::init<uint8,uint8,uint8,uint8>(),
            py::arg("r"),py::arg("g"),py::arg("b"),py::arg("a")
        );
    ;


    typedef PyDefExtender<b2ParticleDef> PyParticleDef;

    py::class_<PyParticleDef> py_particle_def(pybox2dModule, "ParticleDef");
    add_user_data_api<PyParticleDef>(py_particle_def);

    py_particle_def
        .def(py::init<>())
        .def_readwrite("flags",&PyParticleDef::flags)
        .def_readwrite("position",&PyParticleDef::position)
        .def_readwrite("velocity",&PyParticleDef::velocity)
        .def_readwrite("color",&PyParticleDef::color)
        .def_readwrite("lifetime",&PyParticleDef::lifetime)
        .def_readwrite("group",&PyParticleDef::group)
    ;
}


