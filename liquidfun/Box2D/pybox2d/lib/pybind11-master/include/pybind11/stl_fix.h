#pragma once

#ifdef PYBIND11_HAS_NO_STD_TO_STRING


#include <string>
#include <sstream>

namespace std
{
   template < typename T > 
   inline std::string to_string( const T& n )
   {
       std::ostringstream stm ;
       stm << n ;
       return stm.str() ;
   }
}

#endif
