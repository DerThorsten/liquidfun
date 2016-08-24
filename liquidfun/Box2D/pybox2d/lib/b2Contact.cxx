#include <pybind11/pybind11.h>
#include <pybind11/operators.h>
#include <Box2D/Box2D.h>

#include "proxies.hxx"
namespace py = pybind11;





void exportContact(py::module & pybox2dModule){



    py::class_<b2ContactEdge>(pybox2dModule,"b2ContactEdge")
    ;


    py::class_<b2ContactImpulseProxy>(pybox2dModule,"b2ContactImpulseProxy")
    ;


    py::class_<b2ContactProxy>(pybox2dModule,"b2ContactProxy")
        .def_property_readonly("fixtureA",[](      b2ContactProxy & c){return c.GetFixtureA();},py::return_value_policy::reference_internal)
        .def_property_readonly("fixtureB",[](      b2ContactProxy & c){return c.GetFixtureB();},py::return_value_policy::reference_internal)
        .def_property_readonly("worldManifold",&b2ContactProxy::GetWorldManifold)
    ;

    py::class_<b2Contact>(pybox2dModule,"b2Contact")
        .def_property_readonly("fixtureA",[](const b2Contact & c){return c.GetFixtureA();},py::return_value_policy::reference_internal)
        .def_property_readonly("fixtureA",[](      b2Contact & c){return c.GetFixtureA();},py::return_value_policy::reference_internal)
        .def_property_readonly("fixtureB",[](const b2Contact & c){return c.GetFixtureB();},py::return_value_policy::reference_internal)
        .def_property_readonly("fixtureB",[](      b2Contact & c){return c.GetFixtureB();},py::return_value_policy::reference_internal)
        .def_property_readonly("getWorldManifold",&b2Contact::GetWorldManifold)

    ;



}
