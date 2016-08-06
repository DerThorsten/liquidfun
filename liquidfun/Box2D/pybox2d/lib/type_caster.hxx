#include <pybind11/pybind11.h>
#include <Box2D/Box2D.h>

namespace pybind11{
namespace detail{


template < > class type_caster< b2Vec2 > {
    typedef float32 T1;
    typedef float32 T2;
    typedef b2Vec2 type;
public:
    bool load(handle src, bool convert) {
        if (!PyTuple_Check(src.ptr()) || PyTuple_Size(src.ptr()) != 2)
            return false;
        return  first.load(PyTuple_GET_ITEM(src.ptr(), 0), convert) &&
               second.load(PyTuple_GET_ITEM(src.ptr(), 1), convert);
    }

    static handle cast(const type &src, return_value_policy policy, handle parent) {
        object o1 = object(type_caster<typename intrinsic_type<T1>::type>::cast(src.x, policy, parent), false);
        object o2 = object(type_caster<typename intrinsic_type<T2>::type>::cast(src.y, policy, parent), false);
        if (!o1 || !o2)
            return handle();
        tuple result(2);
        PyTuple_SET_ITEM(result.ptr(), 0, o1.release().ptr());
        PyTuple_SET_ITEM(result.ptr(), 1, o2.release().ptr());
        return result.release();
    }

    static PYBIND11_DESCR name() {
        return type_descr(
            _("(") + type_caster<typename intrinsic_type<T1>::type>::name() +
            _(", ") + type_caster<typename intrinsic_type<T2>::type>::name() + _(")"));
    }

    operator type() {
        return b2Vec2(first, second);
    }
protected:
    type_caster<typename intrinsic_type<T1>::type> first;
    type_caster<typename intrinsic_type<T2>::type> second;
};

}
}
