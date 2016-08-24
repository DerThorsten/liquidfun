
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/operators.h>
#include <Box2D/Box2D.h>

#include "proxies.hxx"

#include <vector>

namespace py = pybind11;




void exportb2Collision(py::module & pybox2dModule){



    py::class_<b2AABB>(pybox2dModule,"b2AABB")
        .def(py::init<>())
        .def_readwrite("lowerBound",&b2AABB::lowerBound)
        .def_readwrite("upperBound",&b2AABB::upperBound)
    ;

    py::class_<b2ManifoldPoint>(pybox2dModule,"b2ManifoldPoint")
        .def_readonly("localPoint",         &b2ManifoldPoint::localPoint)
        .def_readonly("normalImpulse",      &b2ManifoldPoint::normalImpulse)
        .def_readonly("tangentImpulse",     &b2ManifoldPoint::tangentImpulse)
        .def_readonly("id",                 &b2ManifoldPoint::id)
    ;
    


    auto b2ManifoldCls = py::class_<b2Manifold>(pybox2dModule,"b2Manifold");
    b2ManifoldCls
        .def(py::init<>())

        .def_property_readonly("points",[](const b2Manifold * self){
            std::vector<b2ManifoldPoint> p(self->pointCount);
            for(int i=0; i<self->pointCount; ++i)
                p[i] = self->points[i];
            return p;
        })
        .def_readonly("localNormal",   &b2Manifold::localNormal)
        .def_readonly("localPoint",    &b2Manifold::localPoint)
        .def_readonly("type",          &b2Manifold::type)
        .def_readonly("pointCount",    &b2Manifold::pointCount)

    ;


    py::enum_<b2Manifold::Type>(b2ManifoldCls, "b2ManifoldType")
        .value("e_circles", b2Manifold::Type::e_circles)
        .value("e_faceA",   b2Manifold::Type::e_faceA)
        .value("e_faceA",   b2Manifold::Type::e_faceB)
    ;

    py::class_<b2ManifoldProxy>(pybox2dModule,"b2ManifoldProxy")
        .def_property_readonly("points",[](const b2ManifoldProxy * self){
            std::vector<b2ManifoldPoint> p(self->manifold_->pointCount);
            for(int i=0; i<self->manifold_->pointCount; ++i)
                p[i] = self->manifold_->points[i];
            return p;
        })
        .def_property_readonly("localNormal", [](const b2ManifoldProxy * self){return self->manifold_->localNormal;})
        .def_property_readonly("localPoint",  [](const b2ManifoldProxy * self){return self->manifold_->localPoint;})
        .def_property_readonly("type",        [](const b2ManifoldProxy * self){return self->manifold_->type;})
        .def_property_readonly("pointCount",  [](const b2ManifoldProxy * self){return self->manifold_->pointCount;})



    ;


    py::class_<b2WorldManifold>(pybox2dModule,"b2WorldManifold")
        .def(py::init<>())
    ;
}
