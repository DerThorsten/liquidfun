#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include <Box2D/Box2D.h>

namespace py = pybind11;



class PyB2Shape : public b2Shape {
public:
    /* Inherit the constructors */
    using b2Shape::b2Shape;

    ///* Trampoline (need one for each virtual function) */
    //std::string go(int n_times) {
    //    PYBIND11_OVERLOAD_PURE(
    //        std::string, /* Return type */
    //        Animal,      /* Parent class */
    //        go,          /* Name of function */
    //        n_times      /* Argument(s) */
    //    );
    //}



    //~PyB2Shape() {}

    /// Clone the concrete shape using the provided allocator.
    b2Shape* Clone(b2BlockAllocator* allocator) const {
        PYBIND11_OVERLOAD_PURE(
            b2Shape*,     /* Return type */
            b2Shape,      /* Parent class */
            Clone,        /* Name of function */
            allocator     /* Argument(s) */
        );
        return NULL;
    }

    int32 GetChildCount() const {
        PYBIND11_OVERLOAD_PURE(
            int32,     /* Return type */
            b2Shape,      /* Parent class */
            GetChildCount        /* Name of function */
        )
        return 0;
    }

    bool TestPoint(const b2Transform& xf, const b2Vec2& p) const{
        PYBIND11_OVERLOAD_PURE(
            bool,     /* Return type */
            b2Shape,      /* Parent class */
            TestPoint, /* Name of function */
            xf,p        /* Name of function */
        );
        return false;
    }

    void ComputeDistance(const b2Transform& xf, const b2Vec2& p, float32* distance, b2Vec2* normal, int32 childIndex) const{
        PYBIND11_OVERLOAD_PURE(
            void,     /* Return type */
            b2Shape,      /* Parent class */
            ComputeDistance, /* Name of function */
            xf,p,distance,normal,childIndex      /* Name of function */
        );
    }

    bool RayCast(b2RayCastOutput* output, const b2RayCastInput& input,
                        const b2Transform& transform, int32 childIndex) const {

        PYBIND11_OVERLOAD_PURE(
            bool,     /* Return type */
            b2Shape,      /* Parent class */
            RayCast, /* Name of function */
            output,input,transform,childIndex      /* Name of function */
        );
        return false;

    }

    void ComputeAABB(b2AABB* aabb, const b2Transform& xf, int32 childIndex) const {
        PYBIND11_OVERLOAD_PURE(
            void,     /* Return type */
            b2Shape,      /* Parent class */
            ComputeAABB, /* Name of function */
            aabb,xf,childIndex      /* Name of function */
        );
    }

    void ComputeMass(b2MassData* massData, float32 density) const {
        PYBIND11_OVERLOAD_PURE(
            void,     /* Return type */
            b2Shape,      /* Parent class */
            ComputeMass, /* Name of function */
            massData,density    /* Name of function */
        );
    }
};


template<class DT>
bool isType(const b2Shape * shape){
    return bool(dynamic_cast<const DT *>(shape));
}

template<class DT>
DT * asType(b2Shape * shape){
    auto res =  dynamic_cast<DT *>(shape);
    if(res == nullptr){
        throw std::runtime_error("invalid b2Shape dynamic cast");
    }
    return res;
}

void exportB2Shape(py::module & pybox2dModule){



    auto shapeCls = py::class_< b2Shape, PyB2Shape>(pybox2dModule,"b2Shape");
    shapeCls
        //.alias<b2Shape>()
        .def(py::init<>())
        .def("getType",&b2Shape::GetType)
        .def("getChildCount",&b2Shape::GetChildCount)
        .def("testPoint",&b2Shape::TestPoint,py::arg("xf"),py::arg("p"))
        .def("computeDistance",&b2Shape::ComputeDistance)
        .def("isCircleShape",&isType<b2CircleShape>)
        .def("isChainShape",&isType<b2ChainShape>)
        .def("isEdgeShape",&isType<b2EdgeShape>)
        .def("isPolygonShape",&isType<b2PolygonShape>)
        .def_readwrite("radius", &b2Shape::m_radius)
            //.def_dynamic_cast<b2Shape,b2CircleShape>("asCircleShape")
            //.def_dynamic_cast<b2Shape,b2ChainShape>("asChainShape")
            //.def_dynamic_cast<b2Shape,b2EdgeShape>("asEdgeShape")
            //.def_dynamic_cast<b2Shape,b2PolygonShape>("asPolygonShape")
        //.defIseadwrite("categoryBits", &b2Shape::categoryBits)
        //.def_readwrite("maskBits", &b2Shape::maskBits)
        //.def_readwrite("groupIndex", &b2Shape::groupIndex)
    ;



    py::enum_<b2Shape::Type>(shapeCls, "ShapeType")
        .value("e_circle", b2Shape::Type::e_circle)
        .value("e_edge", b2Shape::Type::e_edge)
        .value("e_chain", b2Shape::Type::e_chain)
        .value("e_polygon", b2Shape::Type::e_polygon)
        .value("e_typeCount", b2Shape::Type::e_typeCount)
        //.exportValues()
    ;
    
    
    // derived shapes
    py::class_<b2CircleShape>(pybox2dModule,"b2CircleShape",shapeCls)
        .def(py::init<>())
        .def_readwrite("pos", &b2CircleShape::m_p)
    ;


    py::class_<b2EdgeShape>(pybox2dModule,"b2EdgeShape",shapeCls)
        .def(py::init<>())
        .def("set",[](b2EdgeShape * s,const b2Vec2 & v1,const b2Vec2 & v2)
             {s->Set(v1,v2);},py::arg("v1"),py::arg("v2"))
    ;


    py::class_<b2ChainShape>(pybox2dModule,"b2ChainShape",shapeCls)
        .def(py::init<>())
        .def("createLoop",[](b2ChainShape *s, const std::vector<b2Vec2> & verts ){
            s->CreateLoop(verts.data(), verts.size());
        })
        .def("createChain",[](b2ChainShape *s, const std::vector<b2Vec2> & verts ){
            s->CreateChain(verts.data(), verts.size());
        })
        .def_readonly("vertexCount", &b2ChainShape::m_count)
        .def_property_readonly("vertices",[](const b2ChainShape * shape){
            std::vector<b2Vec2> vec(shape->m_count);
            for(size_t i=0; i<vec.size(); ++i){
                vec[i]  = shape->m_vertices[i];
            }
            return vec;
        })
    ;

    py::class_<b2PolygonShape>(pybox2dModule,"b2PolygonShape",shapeCls)
        .def(py::init<>())
        .def("setAsBox",
            [&](
                b2PolygonShape & shape,
                float32 hx,float32 hy,
                float32 cx,float32 cy,
                float32 angle
            ){
                shape.SetAsBox(hx, hy, cx, cy, angle);
            },
            py::arg("hx"),
            py::arg("hy"),
            py::arg("centerX") = 0,
            py::arg("centerY") = 0,
            py::arg("angle") = 0
        )
        .def("set",[](b2PolygonShape *s, const std::vector<b2Vec2> & verts ){
            s->Set(verts.data(), verts.size());
        })
        .def_property_readonly("vertexCount", &b2PolygonShape::GetVertexCount)
        .def("getVertex", &b2PolygonShape::GetVertex,py::return_value_policy::reference_internal)
    ;

    //pybox2dModule.def("b2PolygonShapeCast", &asType<b2PolygonShape>,
    //    py::return_value_policy::dont_cache_cast,py::keep_alive<1,0>());



}

