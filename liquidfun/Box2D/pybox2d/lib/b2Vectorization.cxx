#include <pybind11/pybind11.h>

#include <Box2D/Box2D.h>
//#include <Box2D/extensions/multi_gravity_world.hxx>
#include "pyb2Draw.hxx"
#include "pyb2WorldCallbacks.hxx"
//#include "type_caster.hxx"

#include <vector>

namespace py = pybind11;




class BodyVector : public std::vector<b2Body * >
{

};

// NewtonianGravity
void applyNewtonianPointSourceGravity(
    const BodyVector & bodies,
    py::array_t<float32> sourcePositions,
    py::array_t<float32> sourceMasses
){

}


void exportb2Vectorization(py::module & pybox2dModule){

    py::class_<BodyVector>(pybox2dModule,"BodyVector")
        .def(py::init<>())
    ;
}

