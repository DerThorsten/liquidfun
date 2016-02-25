#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>
#include <Box2D/Box2D.h>
#include <iostream>

namespace py = pybind11;


class PyB2Draw : public b2Draw {
public:
    /* Inherit the constructors */
    //using b2Draw::b2Draw;

    virtual ~PyB2Draw() {}

    PyB2Draw(const py::object object)
    : object_(object){

    }


    virtual void DrawPolygon(const b2Vec2* vertices, int32 vertexCount, const b2Color& color) {
        
        //typedef long unsigned int ShapeType;

        auto npVertices = py::array(py::buffer_info(
            nullptr,            /* Pointer to data (nullptr -> ask NumPy to allocate!) */
            sizeof(float32),     /* Size of one item */
            py::format_descriptor<float32>::value(), /* Buffer format */
            2,          /* How many dimensions? */
            { size_t(vertexCount), size_t(2) },  /* Number of elements for each dimension */
            { 2*sizeof(float32),sizeof(float32)}  /* Strides for each dimension */
        ));

        float32 * ptr  = static_cast<float32* >(npVertices.request().ptr);        
        for(size_t i=0;  i<size_t(vertexCount); ++i){
            ptr[i*2 ]   = vertices[i].x;
            ptr[i*2 +1] = vertices[i].y;
        }
        py::object f = object_.attr("DrawPolygon");
        f.call(npVertices,color);
    }

    virtual void DrawSolidPolygon(const b2Vec2* vertices, int32 vertexCount, const b2Color& color) {
        auto npVertices = py::array(py::buffer_info(
            nullptr,            /* Pointer to data (nullptr -> ask NumPy to allocate!) */
            sizeof(float32),     /* Size of one item */
            py::format_descriptor<float32>::value(), /* Buffer format */
            2,          /* How many dimensions? */
            { size_t(vertexCount), size_t(2) },  /* Number of elements for each dimension */
            { 2*sizeof(float32),sizeof(float32)}  /* Strides for each dimension */
        ));

        float32 * ptr  = static_cast<float32* >(npVertices.request().ptr);        
        for(size_t i=0;  i<size_t(vertexCount); ++i){
            ptr[i*2 ]   = vertices[i].x;
            ptr[i*2 +1] = vertices[i].y;
        }
        py::object f = object_.attr("DrawSolidPolygon");
        f.call(npVertices,color);
    }

    virtual void DrawCircle(const b2Vec2& center, float32 radius, const b2Color& color) {
        py::object f = object_.attr("DrawCircle");
        f.call(center,radius,color);
    }

    virtual void DrawSolidCircle(const b2Vec2& center, float32 radius, const b2Vec2& axis, const b2Color& color) {
        py::object f = object_.attr("DrawSolidCircle");
        f.call(center,radius,color);
    }

    virtual void DrawParticles(const b2Vec2 *centers, float32 radius, const b2ParticleColor *colors, int32 count) {
        //std::cout<<"Draw\n";
    }

    virtual void DrawSegment(const b2Vec2& p1, const b2Vec2& p2, const b2Color& color) {
        py::object f = object_.attr("DrawSegment");
        f.call(p1,p2,color);
    }

    virtual void DrawTransform(const b2Transform& xf) {
       py::object f = object_.attr("DrawTransform");
       f.call(xf);
    }

    py::object object_;

};
