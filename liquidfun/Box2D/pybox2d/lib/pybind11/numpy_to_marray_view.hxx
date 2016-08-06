



namespace pybind11{

    array_t<double> add_arrays(py::array_t<double> i, py::array_t<double> j)
    {
      py::buffer_info info_i = i.request();
      py::buffer_info info_j = j.request();
    }





    template<class T>
    marray::MultiArrayView<T> toMarray(array_t<T> & array){
        auto info = array.request();
        const auto  strides = array.strides();
        const auto  strides = array.strides();
        auto  data = 
    }

}
