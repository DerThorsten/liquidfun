#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>

#include <Box2D/Box2D.h>
//#include <Box2D/extensions/multi_gravity_world.hxx>
#include "pyb2Draw.hxx"
#include "pyb2WorldCallbacks.hxx"


#include "holder.hxx"
#include "container.hxx"
#include "vectorize.hxx"
#include <vector>

namespace py = pybind11;


void check_sizes(const std::size_t cpp_size, const std::size_t array_size)
{
    if(cpp_size != array_size && array_size != 1)
    {
        throw std::runtime_error("shape mismatch :(");
    }

}


class Vec2RepeatingArray
{
public:
    Vec2RepeatingArray(py::array_t<float> array, const std::size_t desired_size)
    :   m_desired_size(desired_size),
        m_array(array),    
        m_unchecked_array(m_array.template unchecked<2>()),
        m_first(),
        m_only_one(false)
    {
        check_sizes(desired_size, array.shape(0));
        if(array.shape(0) == 1)
        {
            m_only_one = true;
            m_first.x = m_unchecked_array(0, 0);
            m_first.x = m_unchecked_array(0, 1);
        }
    }
    b2Vec2 operator[](const std::size_t index) const 
    {
        return m_only_one ? m_first : 
            b2Vec2(m_unchecked_array(index, 0),
                   m_unchecked_array(index, 1));
    }
private:
    std::size_t m_desired_size;
    py::array_t<float> m_array;
    py::detail::unchecked_reference<float, 2> m_unchecked_array;
    b2Vec2 m_first;
    bool m_only_one;
};

template<class T>
class RepeatingArray
{
public:
    RepeatingArray(py::array_t<T> array, const std::size_t desired_size)
    :   m_desired_size(desired_size),
        m_array(array),    
        m_unchecked_array(m_array. template unchecked<1>()),
        m_first(),
        m_only_one(false)
    {
        check_sizes(desired_size, array.shape(0));
        if(array.shape(0) == 1)
        {
            m_only_one = true;
            //m_first = m_unchecked_array(0);
        }
    }

    T operator[](const std::size_t index) const 
    {
        return m_only_one ? m_first : m_unchecked_array(index);
    }
private:
    std::size_t m_desired_size;
    py::array_t<T> m_array;
    py::detail::unchecked_reference<T, 1> m_unchecked_array;
    T m_first;
    bool m_only_one;
};


void exportb2Vectorization(py::module & pybox2dModule){

    ////////////////
    // BODY 
    ////////////////
    {   // vector
        auto pyCls = py::class_<  BodyVector >(pybox2dModule, "BodyVector");
        make_vector_cls(pyCls);
        pyCls

            //////////////////////////////////////////////////////////////
            .def("set_transform",[]
            (
                BodyVector & vec, 
                py::array_t<float> position,
                py::array_t<float> angle
            ){
                Vec2RepeatingArray rposition(position, vec.size());
                RepeatingArray<float> rangle(angle, vec.size());
                for(std::size_t bi=0; bi<vec.size(); ++bi)
                {
                    vec[bi]->SetTransform(rposition[bi], 
                                                rangle[bi]);
                }
            },py::arg("position"), py::arg("angle"))
            //////////////////////////////////////////////////////////////
            .def("apply_force",[]
            (
                BodyVector & vec, 
                py::array_t<float> force_array,
                py::array_t<float> point_array,
                const bool wake
            ){
                Vec2RepeatingArray forces(force_array, vec.size());
                Vec2RepeatingArray points(point_array, vec.size());
                for(std::size_t bi=0; bi<vec.size(); ++bi)
                {
                    vec[bi]->ApplyForce(forces[bi], points[bi], wake);
                }
            },py::arg("force"), py::arg("point"), py::arg("wake"))
            //////////////////////////////////////////////////////////////
            .def("apply_force_to_center",[]
            (
                BodyVector & vec, 
                py::array_t<float> force_array,
                const bool wake
            ){
                Vec2RepeatingArray forces(force_array, vec.size());
                for(std::size_t bi=0; bi<vec.size(); ++bi)
                {
                    vec[bi]->ApplyForceToCenter(forces[bi], wake);
                }
            },py::arg("force"), py::arg("wake"))
            //////////////////////////////////////////////////////////////
            .def("apply_torque",[]
            (
                BodyVector & vec, 
                py::array_t<float> array,
                const bool wake
            ){
                RepeatingArray<float> rarray(array, vec.size());
                for(std::size_t bi=0; bi<vec.size(); ++bi)
                {
                    vec[bi]->ApplyTorque(rarray[bi], wake);
                }
            },py::arg("torque"), py::arg("wake"))
            //////////////////////////////////////////////////////////////
            .def("apply_linear_impulse",[]
            (
                BodyVector & vec, 
                py::array_t<float> array,
                py::array_t<float> points,
                const bool wake
            ){
                Vec2RepeatingArray rarray(array, vec.size());
                Vec2RepeatingArray rpoints(points, vec.size());
                for(std::size_t bi=0; bi<vec.size(); ++bi)
                {
                    vec[bi]->ApplyLinearImpulse(rarray[bi], 
                                                rpoints[bi], 
                                                wake);
                }
            },py::arg("impulse"), py::arg("point"), py::arg("wake"))
            //////////////////////////////////////////////////////////////
            .def("apply_angular_impulse",[]
            (
                BodyVector & vec, 
                py::array_t<float> array,
                const bool wake
            ){
                RepeatingArray<float> rarray(array, vec.size());
                for(std::size_t bi=0; bi<vec.size(); ++bi)
                {
                    vec[bi]->ApplyAngularImpulse(rarray[bi], wake);
                }
            },py::arg("force"), py::arg("wake"))

        ;

    }
    {   // set
        auto pyCls = py::class_<  BodySet >(pybox2dModule, "BodySet");
        make_set_cls(pyCls);
    }

    ////////////////
    // FIXTURES 
    ////////////////
    {   // vector
        auto pyCls = py::class_<  FixtureVector >(pybox2dModule, "FixtureVector");
        make_vector_cls(pyCls);
    }
    {   // set
        auto pyCls = py::class_<  FixtureSet >(pybox2dModule, "FixtureSet");
        make_set_cls(pyCls);
    }
}

