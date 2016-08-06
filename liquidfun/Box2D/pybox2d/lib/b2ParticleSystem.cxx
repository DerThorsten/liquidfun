#include <pybind11/pybind11.h>

#include <Box2D/Box2D.h>

namespace py = pybind11;






void exportB2ParticleSystem(py::module & pybox2dModule){



    py::class_<b2ParticleSystemDef>(pybox2dModule, "b2ParticleSystemDef")
        .def(py::init<>())
        .def_readwrite("pressureStrength", &b2ParticleSystemDef::pressureStrength)
        .def_readwrite("dampingStrength", &b2ParticleSystemDef::dampingStrength)
        .def_readwrite("elasticStrength", &b2ParticleSystemDef::elasticStrength)
        .def_readwrite("springStrength", &b2ParticleSystemDef::springStrength)
        .def_readwrite("viscousStrength", &b2ParticleSystemDef::viscousStrength)
        .def_readwrite("surfaceTensionPressureStrength", &b2ParticleSystemDef::surfaceTensionPressureStrength)
        .def_readwrite("surfaceTensionNormalStrength", &b2ParticleSystemDef::surfaceTensionNormalStrength)
        .def_readwrite("repulsiveStrength", &b2ParticleSystemDef::repulsiveStrength)
        .def_readwrite("powderStrength", &b2ParticleSystemDef::powderStrength)
        .def_readwrite("ejectionStrength", &b2ParticleSystemDef::ejectionStrength)
        .def_readwrite("staticPressureStrength", &b2ParticleSystemDef::staticPressureStrength)
        .def_readwrite("staticPressureRelaxation", &b2ParticleSystemDef::staticPressureRelaxation)
        .def_readwrite("staticPressureIterations", &b2ParticleSystemDef::staticPressureIterations)
        .def_readwrite("colorMixingStrength", &b2ParticleSystemDef::colorMixingStrength)
        .def_readwrite("destroyByAge", &b2ParticleSystemDef::destroyByAge)
        .def_readwrite("lifetimeGranularity", &b2ParticleSystemDef::lifetimeGranularity)
    ;

    py::class_<b2ParticleSystem>(pybox2dModule, "b2ParticleSystem")
        .def_property("radius", &b2ParticleSystem::GetRadius, &b2ParticleSystem::SetRadius)
        .def_property("damping", &b2ParticleSystem::GetDamping, &b2ParticleSystem::SetDamping)
        .def("createParticleGroup",&b2ParticleSystem::CreateParticleGroup,py::return_value_policy::reference_internal)
    ;

}


