/*
    example/example7.cpp -- supporting Pythons' buffer protocol

    Copyright (c) 2015 Wenzel Jakob <wenzel@inf.ethz.ch>

    All rights reserved. Use of this source code is governed by a
    BSD-style license that can be found in the LICENSE file.
*/

#include "example.h"
#include <pybind11/marray.hxx>
class Matrix {
public:
    Matrix(size_t rows, size_t cols) : m_rows(rows), m_cols(cols) {
        std::cout << "Value constructor: Creating a " << rows << "x" << cols << " matrix " << std::endl;
        m_data = new float[rows*cols];
        memset(m_data, 0, sizeof(float) * rows * cols);
    }

    Matrix(const Matrix &s) : m_rows(s.m_rows), m_cols(s.m_cols) {
        std::cout << "Copy constructor: Creating a " << m_rows << "x" << m_cols << " matrix " << std::endl;
        m_data = new float[m_rows * m_cols];
        memcpy(m_data, s.m_data, sizeof(float) * m_rows * m_cols);
    }

    Matrix(Matrix &&s) : m_rows(s.m_rows), m_cols(s.m_cols), m_data(s.m_data) {
        std::cout << "Move constructor: Creating a " << m_rows << "x" << m_cols << " matrix " << std::endl;
        s.m_rows = 0;
        s.m_cols = 0;
        s.m_data = nullptr;
    }

    ~Matrix() {
        std::cout << "Freeing a " << m_rows << "x" << m_cols << " matrix " << std::endl;
        delete[] m_data;
    }

    Matrix &operator=(const Matrix &s) {
        std::cout << "Assignment operator : Creating a " << s.m_rows << "x" << s.m_cols << " matrix " << std::endl;
        delete[] m_data;
        m_rows = s.m_rows;
        m_cols = s.m_cols;
        m_data = new float[m_rows * m_cols];
        memcpy(m_data, s.m_data, sizeof(float) * m_rows * m_cols);
        return *this;
    }

    Matrix &operator=(Matrix &&s) {
        std::cout << "Move assignment operator : Creating a " << s.m_rows << "x" << s.m_cols << " matrix " << std::endl;
        if (&s != this) {
            delete[] m_data;
            m_rows = s.m_rows; m_cols = s.m_cols; m_data = s.m_data;
            s.m_rows = 0; s.m_cols = 0; s.m_data = nullptr;
        }
        return *this;
    }

    float operator()(size_t i, size_t j) const {
        return m_data[i*m_cols + j];
    }

    float &operator()(size_t i, size_t j) {
        return m_data[i*m_cols + j];
    }

    float *data() { return m_data; }

    size_t rows() const { return m_rows; }
    size_t cols() const { return m_cols; }
private:
    size_t m_rows;
    size_t m_cols;
    float *m_data;
};




template<class T>
class NumpyMarry : public pybind11::marray::View<T>{

public:
    NumpyMarry(py::buffer buffer)
    : buffer_(buffer){
        py::buffer_info info = buffer.request();
        if (info.format != py::format_descriptor<float>::value())
            throw std::runtime_error("Incompatible buffer format!");
        auto shape = info.shape;
        auto strides = info.strides;

        for(auto &s : shape)
           std::cout<<"shape "<<s<<"\n";
        for(auto &s : strides)
           std::cout<<"stride "<<s<<"\n";

        for(auto &s : strides)
            s/=sizeof(float);
        this->assign(shape.begin(),shape.end(), strides.begin(),static_cast<float*>(info.ptr),pybind11::marray::FirstMajorOrder);
    }   
private:
    py::buffer  buffer_;
};




void init_ex14(py::module &m) {
    py::class_<Matrix> mtx(m, "Matrix");

    mtx.def(py::init<size_t, size_t>())
        /// Construct from a buffer
        .def("__init__", [](Matrix &v, py::buffer b) {
            py::buffer_info info = b.request();
            if (info.format != py::format_descriptor<float>::value() || info.ndim != 2)
                throw std::runtime_error("Incompatible buffer format!");
            new (&v) Matrix(info.shape[0], info.shape[1]);
            memcpy(v.data(), info.ptr, sizeof(float) * v.rows() * v.cols());
        })

       .def("rows", &Matrix::rows)
       .def("cols", &Matrix::cols)

        /// Bare bones interface
       .def("__getitem__", [](const Matrix &m, std::pair<size_t, size_t> i) {
            if (i.first >= m.rows() || i.second >= m.cols())
                throw py::index_error();
            return m(i.first, i.second);
        })
       .def("__setitem__", [](Matrix &m, std::pair<size_t, size_t> i, float v) {
            if (i.first >= m.rows() || i.second >= m.cols())
                throw py::index_error();
            m(i.first, i.second) = v;
        })
       /// Provide buffer access
       .def_buffer([](Matrix &m) -> py::buffer_info {
            return py::buffer_info(
                m.data(),                              /* Pointer to buffer */
                sizeof(float),                         /* Size of one scalar */
                py::format_descriptor<float>::value(), /* Python struct-style format descriptor */
                2,                                     /* Number of dimensions */
                { m.rows(), m.cols() },                /* Buffer dimensions */
                { sizeof(float) * m.rows(),            /* Strides (in bytes) for each index */
                  sizeof(float) }
            );
        });


    m.def("foo",
        [](py::buffer b){
            NumpyMarry<float> marray(b);

            for(auto d : marray)
                std::cout<<"d" <<d<<"\n";
        }
    );
}
