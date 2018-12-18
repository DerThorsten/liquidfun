#pragma once


#include <pybind11/numpy.h>
#include <initializer_list>
#include <vector>


template<class T>
py::array_t<T> make_numpy_array(
    std::initializer_list<int> shape
)
{
    const std::size_t n_dim = shape.size();
    std::vector<int> shape_vec(shape);
    std::vector<int> stride_vec(n_dim);
    stride_vec.back() = sizeof(T);
    for(int i = n_dim - 2; i>=0; --i)
    {
        stride_vec[i] = shape_vec[i+1] * stride_vec[i+1];
    }

    return py::array(py::buffer_info(
        nullptr,         /* Pointer to data (nullptr -> ask NumPy to allocate!) */
        sizeof(T),     /* Size of one item */
        py::format_descriptor<T>::value, /* Buffer format */
        n_dim,          /* How many dimensions? */
        shape,  /* Number of elements for each dimension */
        stride_vec  /* Strides for each dimension */
    ));
}