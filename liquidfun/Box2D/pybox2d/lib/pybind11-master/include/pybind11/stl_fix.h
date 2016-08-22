#ifndef  PYBIND11_STL_FIX


#include <string>
#include <sstream>

namespace std
{
    template < typename T > 
    std::string to_string( const T& n )
    {
        std::ostringstream stm ;
        stm << n ;
        return stm.str() ;
    }
}


#endif