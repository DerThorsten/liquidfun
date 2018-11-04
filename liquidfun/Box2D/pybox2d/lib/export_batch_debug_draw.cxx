#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>

#include <Box2D/Box2D.h>
//#include <Box2D/extensions/multi_gravity_world.hxx>
#include "pyb2Draw.hxx"
#include "pyb2WorldCallbacks.hxx"

#include "holder.hxx"
#include "batch_debug_draw.hxx"
// PYBIND11_DECLARE_HOLDER_TYPE(T, Holder<T>, true);

//#include "type_caster.hxx"

namespace py = pybind11;


template<uint8_t INDEX>
std::tuple<py::array, py::array > polygon_shape(const BatchDebugDrawCollector & self)
{
    const auto & polygon_shapes = std::get<INDEX>(self.m_polygon_shapes);
    const auto & verts          = polygon_shapes.m_points;
    const auto & connect        = polygon_shapes.m_connect;

    const auto n = verts.size();

    auto verts_array = py::array(py::buffer_info(
        nullptr,             /* Pointer to data (nullptr -> ask NumPy to allocate!) */
        sizeof(float32),     /* Size of one item */
        py::format_descriptor<float32>::value, /* Buffer format */
        2,          /* How many dimensions? */
        { n, size_t(2) },  /* Number of elements for each dimension */
        { 2*sizeof(float32),sizeof(float32)}  /* Strides for each dimension */
    ));

    auto connect_array = py::array(py::buffer_info(
        nullptr,             /* Pointer to data (nullptr -> ask NumPy to allocate!) */
        sizeof(uint8_t),     /* Size of one item */
        py::format_descriptor<uint8_t>::value, /* Buffer format */
        1,          /* How many dimensions? */
        { n},  /* Number of elements for each dimension */
        { sizeof(uint8_t)}  /* Strides for each dimension */
    ));

    float32 * verts_ptr    = static_cast<float32* >(verts_array.request().ptr);        
    uint8_t * connect_ptr  = static_cast<uint8_t* >(connect_array.request().ptr);        

    for(size_t i=0;  i<n; ++i)
    {
        connect_ptr[i] = connect[i];
        verts_ptr[i * 2]     = verts[i][0];
        verts_ptr[i * 2 + 1] = verts[i][1];
    }
    return std::make_tuple(verts_array, connect_array);
}

template<uint8_t INDEX>
std::tuple<py::array, py::array > chain_shape(const BatchDebugDrawCollector & self)
{
    const auto & polygon_shapes = std::get<INDEX>(self.m_chain_shapes);
    const auto & verts          = polygon_shapes.m_points;
    const auto & connect        = polygon_shapes.m_connect;

    const auto n = verts.size();

    auto verts_array = py::array(py::buffer_info(
        nullptr,             /* Pointer to data (nullptr -> ask NumPy to allocate!) */
        sizeof(float32),     /* Size of one item */
        py::format_descriptor<float32>::value, /* Buffer format */
        2,          /* How many dimensions? */
        { n, size_t(2) },  /* Number of elements for each dimension */
        { 2*sizeof(float32),sizeof(float32)}  /* Strides for each dimension */
    ));

    auto connect_array = py::array(py::buffer_info(
        nullptr,             /* Pointer to data (nullptr -> ask NumPy to allocate!) */
        sizeof(uint8_t),     /* Size of one item */
        py::format_descriptor<uint8_t>::value, /* Buffer format */
        1,          /* How many dimensions? */
        { n},  /* Number of elements for each dimension */
        { sizeof(uint8_t)}  /* Strides for each dimension */
    ));

    float32 * verts_ptr    = static_cast<float32* >(verts_array.request().ptr);        
    uint8_t * connect_ptr  = static_cast<uint8_t* >(connect_array.request().ptr);        

    for(size_t i=0;  i<n; ++i)
    {
        connect_ptr[i] = connect[i];
        verts_ptr[i * 2]     = verts[i][0];
        verts_ptr[i * 2 + 1] = verts[i][1];
    }
    return std::make_tuple(verts_array, connect_array);
}

template<uint8_t INDEX>
std::tuple<py::array, py::array > make_aabbs(const BatchDebugDrawCollector & self)
{
    const auto & bounding_boxes = self.m_bounding_boxes;
    const auto & verts          = bounding_boxes.m_points;
    const auto & connect        = bounding_boxes.m_connect;

    const auto n = verts.size();

    auto verts_array = py::array(py::buffer_info(
        nullptr,             /* Pointer to data (nullptr -> ask NumPy to allocate!) */
        sizeof(float32),     /* Size of one item */
        py::format_descriptor<float32>::value, /* Buffer format */
        2,          /* How many dimensions? */
        { n, size_t(2) },  /* Number of elements for each dimension */
        { 2*sizeof(float32),sizeof(float32)}  /* Strides for each dimension */
    ));

    auto connect_array = py::array(py::buffer_info(
        nullptr,             /* Pointer to data (nullptr -> ask NumPy to allocate!) */
        sizeof(uint8_t),     /* Size of one item */
        py::format_descriptor<uint8_t>::value, /* Buffer format */
        1,          /* How many dimensions? */
        { n},  /* Number of elements for each dimension */
        { sizeof(uint8_t)}  /* Strides for each dimension */
    ));

    float32 * verts_ptr    = static_cast<float32* >(verts_array.request().ptr);        
    uint8_t * connect_ptr  = static_cast<uint8_t* >(connect_array.request().ptr);        

    for(size_t i=0;  i<n; ++i)
    {
        connect_ptr[i] = connect[i];
        verts_ptr[i * 2]     = verts[i][0];
        verts_ptr[i * 2 + 1] = verts[i][1];
    }
    return std::make_tuple(verts_array, connect_array);
}

void exportExtendedDebugDraw(py::module & pybox2dModule){

    py::class_<BatchDebugDrawOptions>(pybox2dModule, "BatchDebugDrawOptions")
        .def(py::init<>())
        .def_readwrite("draw_shapes", & BatchDebugDrawOptions::draw_shapes)
        .def_readwrite("draw_aabbs",  & BatchDebugDrawOptions::draw_aabbs)
        .def_readwrite("draw_joints", & BatchDebugDrawOptions::draw_joints)
        .def_readwrite("draw_coms",   & BatchDebugDrawOptions::draw_coms)
    ;

    py::class_<BatchDebugDrawCollector>(pybox2dModule, "BatchDebugDrawCollector")
        .def(py::init<const BatchDebugDrawOptions &>())
        .def("collect", &BatchDebugDrawCollector::collect)
        .def("clear", &BatchDebugDrawCollector::clear)
        .def("change_options", &BatchDebugDrawCollector::change_options)

        .def_readonly("drawing_aabb", &BatchDebugDrawCollector::m_drawing_bounding_box)

        .def("inactive_body_polygon_shapes",      &polygon_shape<INACTIVE_BODY>)
        .def("static_body_polygon_shapes",        &polygon_shape<STATIC_BODY>)
        .def("kinematic_body_polygon_shapes",     &polygon_shape<KINEMATIC_BODY>)
        .def("sleeping_body_polygon_shapes",     &polygon_shape<SLEEPING_BODY>)
        .def("dynamic_body_polygon_shapes",          &polygon_shape<DYNAMIC_BODY>)

        .def("inactive_body_chain_shapes",      &chain_shape<INACTIVE_BODY>)
        .def("static_body_chain_shapes",        &chain_shape<STATIC_BODY>)
        .def("kinematic_body_chain_shapes",     &chain_shape<KINEMATIC_BODY>)
        .def("sleeping_body_chain_shapes",       &chain_shape<SLEEPING_BODY>)
        .def("dynamic_body_chain_shapes",        &chain_shape<DYNAMIC_BODY>)

        .def("circles_axis", [](const BatchDebugDrawCollector & self) -> py::array {

            const auto & m_circles_axis = self.m_circles_axis;
            const auto n = m_circles_axis.size();

            auto verts_array = py::array(py::buffer_info(
                nullptr,             /* Pointer to data (nullptr -> ask NumPy to allocate!) */
                sizeof(float32),     /* Size of one item */
                py::format_descriptor<float32>::value, /* Buffer format */
                2,          /* How many dimensions? */
                { n, size_t(2) },  /* Number of elements for each dimension */
                { 2*sizeof(float32),sizeof(float32)}  /* Strides for each dimension */
            ));

            float32 * verts_ptr    = static_cast<float32* >(verts_array.request().ptr); 

            for(std::size_t i=0; i< m_circles_axis.size(); ++i)
            {
                verts_ptr[i * 2]     = m_circles_axis[i].x;
                verts_ptr[i * 2 + 1] = m_circles_axis[i].y;

            }
            return verts_array;
        })
        .def("aabbs",                                    &make_aabbs<DYNAMIC_BODY>)
        .def("joint_segments", [](const BatchDebugDrawCollector & self) -> py::array {

            const auto & m_joint_segments = self.m_joint_segments;
            const auto n = m_joint_segments.size();

            auto verts_array = py::array(py::buffer_info(
                nullptr,             /* Pointer to data (nullptr -> ask NumPy to allocate!) */
                sizeof(float32),     /* Size of one item */
                py::format_descriptor<float32>::value, /* Buffer format */
                2,          /* How many dimensions? */
                { n*2, size_t(2) },  /* Number of elements for each dimension */
                { 2*sizeof(float32),sizeof(float32)}  /* Strides for each dimension */
            ));

            float32 * verts_ptr    = static_cast<float32* >(verts_array.request().ptr); 

            for(std::size_t i=0; i< m_joint_segments.size(); ++i)
            {
                verts_ptr[i * 4]     = m_joint_segments[i].first.x;
                verts_ptr[i * 4 + 1] = m_joint_segments[i].first.y;
                verts_ptr[i * 4 + 2] = m_joint_segments[i].second.x;
                verts_ptr[i * 4 + 3] = m_joint_segments[i].second.y;
            }
            return verts_array;
        })
    ;



}

