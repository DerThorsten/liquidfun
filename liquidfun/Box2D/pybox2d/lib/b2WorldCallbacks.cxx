#include <pybind11/pybind11.h>

#include <Box2D/Box2D.h>

namespace py = pybind11;



class PyB2DestructionListener : public b2DestructionListener {
public:
    /* Inherit the constructors */
    //using b2DestructionListener::b2DestructionListener;

    virtual ~PyB2DestructionListener() {}

    PyB2DestructionListener(){

    }

    virtual void SayGoodbye(b2Joint * joint)  {
        PYBIND11_OVERLOAD_PURE(
            void ,                      // Return type 
            b2DestructionListener,      // Parent class 
            SayGoodbye,                 // name
            joint                       // args
        );
    }

    virtual void SayGoodbye(b2Fixture * fixture)  {
        PYBIND11_OVERLOAD_PURE(
            void ,                      // Return type 
            b2DestructionListener,      // Parent class 
            SayGoodbye,                 // name
            fixture                       // args
        );
    }

    virtual void SayGoodbye(b2ParticleGroup* group){
        PYBIND11_OVERLOAD(
            void ,                      // Return type 
            b2DestructionListener,      // Parent class 
            SayGoodbye,                 // name
            group                       // args
        );
    }

    virtual void SayGoodbye(b2ParticleSystem* particleSystem, int32 index){
        PYBIND11_OVERLOAD(
            void ,                      // Return type 
            b2DestructionListener,      // Parent class 
            SayGoodbye,                 // name
            particleSystem,index        // args
        );
    }
};


class PyB2ContactFilter : public b2ContactFilter {
public:
    /* Inherit the constructors */
    //using b2ContactFilter::b2ContactFilter;

    virtual ~PyB2ContactFilter() {}

    PyB2ContactFilter(){

    }

    virtual bool ShouldCollide(b2Fixture* fixtureA, b2Fixture* fixtureB) {
        PYBIND11_OVERLOAD(
            bool ,             // Return type 
            b2ContactFilter,   // Parent class 
            ShouldCollide,     // name
            fixtureA,fixtureB  // args
        );
    }

    virtual bool ShouldCollide(b2Fixture* fixtureA, b2ParticleSystem* particleSystem, int32 particleIndex) {
        PYBIND11_OVERLOAD(
            bool ,             // Return type 
            b2ContactFilter,   // Parent class 
            ShouldCollide,     // name
            fixtureA, particleSystem, particleIndex  // args
        );
    }

    virtual bool ShouldCollide(b2ParticleSystem* particleSystem, int32 particleIndexA, int32 particleIndexB) {
        PYBIND11_OVERLOAD(
            bool ,             // Return type 
            b2ContactFilter,   // Parent class 
            ShouldCollide,     // name
            particleSystem, particleIndexA, particleIndexB  // args
        );
    }

};

class PyB2ContactListener : b2ContactListener{
public:
    virtual ~PyB2ContactListener() {}


    virtual void BeginContact(b2Contact* contact) { 
        PYBIND11_OVERLOAD(
            void ,             // Return type 
            b2ContactListener,   // Parent class 
            BeginContact,     // name
            contact  // args
        );
    }

    virtual void EndContact(b2Contact* contact) { 
        PYBIND11_OVERLOAD(
            void ,             // Return type 
            b2ContactListener,   // Parent class 
            EndContact,     // name
            contact  // args
        );
    }


    virtual void BeginContact(b2ParticleSystem* particleSystem,
                              b2ParticleBodyContact* particleBodyContact){
        PYBIND11_OVERLOAD(
            void ,             // Return type 
            b2ContactListener,   // Parent class 
            BeginContact,     // name
            particleSystem, particleBodyContact  // args
        );
    }

    virtual void EndContact(b2Fixture* fixture,
                            b2ParticleSystem* particleSystem, int32 index){
        PYBIND11_OVERLOAD(
            void ,             // Return type 
            b2ContactListener,   // Parent class 
            EndContact,     // name
            fixture, particleSystem, index  // args
        );
    }

    virtual void BeginContact(b2ParticleSystem* particleSystem,
                              b2ParticleContact* particleContact){
        PYBIND11_OVERLOAD(
            void ,             // Return type 
            b2ContactListener,   // Parent class 
            BeginContact,     // name
            particleSystem, particleContact  // args
        );
    }

    virtual void EndContact(b2ParticleSystem* particleSystem,
                            int32 indexA, int32 indexB){
        PYBIND11_OVERLOAD(
            void ,             // Return type 
            b2ContactListener,   // Parent class 
            EndContact,     // name
            particleSystem, indexA, indexB  // args
        );
    }

    virtual void PreSolve(b2Contact* contact, const b2Manifold* oldManifold){
        PYBIND11_OVERLOAD(
            void ,             // Return type 
            b2ContactListener,   // Parent class 
            PreSolve,     // name
            contact, oldManifold  // args
        );
    }

    virtual void PostSolve(b2Contact* contact, const b2ContactImpulse* impulse){
        PYBIND11_OVERLOAD(
            void ,             // Return type 
            b2ContactListener,   // Parent class 
            PostSolve,     // name
            contact, impulse  // args
        );
    }
};





void exportB2WorldCallbacks(py::module & pybox2dModule){


    py::class_<b2ContactImpulse>(pybox2dModule,"b2ContactImpulse")
        .def_readonly("normalImpulses",&b2ContactImpulse::normalImpulses)
        .def_readonly("tangentImpulses",&b2ContactImpulse::tangentImpulses)
        .def_readonly("count",&b2ContactImpulse::count)
    ;

    auto destListCls = py::class_<PyB2DestructionListener>(pybox2dModule,"b2DestructionListener");
    destListCls
        .alias<b2DestructionListener>()
        .def(py::init<>())

        .def("SayGoodbyeJoint",(void (b2DestructionListener::*)(b2Joint *)) &b2DestructionListener::SayGoodbye)
        .def("SayGoodbyeFixture",(void (b2DestructionListener::*)(b2Fixture *)) &b2DestructionListener::SayGoodbye)
        .def("SayGoodbyeParticleGroup",(void (b2DestructionListener::*)(b2ParticleGroup *)) &b2DestructionListener::SayGoodbye)
        .def("SayGoodbyeParticle",(void (b2DestructionListener::*)(b2ParticleSystem *, int32)) &b2DestructionListener::SayGoodbye)
    ;


    auto contactFilterCls = py::class_<PyB2ContactFilter>(pybox2dModule,"b2ContactFilter");
    contactFilterCls
        .alias<b2ContactFilter>()
        .def(py::init<>())
        .def("ShouldCollideFixtureFixture",(bool (b2ContactFilter::*)(b2Fixture *, b2Fixture *)) &b2ContactFilter::ShouldCollide)
        .def("ShouldCollideFixtureParticle",(bool (b2ContactFilter::*)(b2Fixture *, b2ParticleSystem *, int32)) &b2ContactFilter::ShouldCollide)
        .def("ShouldCollideParticleParticle",(bool (b2ContactFilter::*)(b2ParticleSystem *, int32,int32)) &b2ContactFilter::ShouldCollide)
    ;

    auto contactListenerCls = py::class_<PyB2ContactListener>(pybox2dModule,"b2ContactListener");
    contactListenerCls
        .alias<b2ContactListener>()
        .def(py::init<>())
    ;
}


