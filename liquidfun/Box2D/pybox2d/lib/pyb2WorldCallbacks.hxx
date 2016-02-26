#include <pybind11/pybind11.h>

#include <Box2D/Box2D.h>

namespace py = pybind11;



class PyB2DestructionListenerCaller : public b2DestructionListener {
public:
    /* Inherit the constructors */
    //using b2DestructionListener::b2DestructionListener;

    virtual ~PyB2DestructionListenerCaller() {}

    PyB2DestructionListenerCaller(const py::object & object)
    : object_(object){
    }
    virtual void SayGoodbye(b2Joint * joint)  {
        py::object f = object_.attr("SayGoodbyeJoint");
        f.call(joint);
    }
    virtual void SayGoodbye(b2Fixture * fixture)  {
        py::object f = object_.attr("SayGoodbyeFixture");
        f.call(fixture);
    }
    virtual void SayGoodbye(b2ParticleGroup* group){
        py::object f = object_.attr("SayGoodbyeParticleGroup");
        f.call(group);
    }

    virtual void SayGoodbye(b2ParticleSystem* particleSystem, int32 index){
        py::object f = object_.attr("SayGoodbyeParticleSystem");
        f.call(particleSystem, index);
    }
private:
    py::object object_;
};


class PyB2ContactFilterCaller : public b2ContactFilter {
public:
    /* Inherit the constructors */
    //using b2ContactFilter::b2ContactFilter;

    virtual ~PyB2ContactFilterCaller() {}

    PyB2ContactFilterCaller(const py::object & object)
    : object_(object){
    }

    virtual bool ShouldCollide(b2Fixture* fixtureA, b2Fixture* fixtureB) {
        py::object f = object_.attr("ShouldCollideFixtureFixture");
        bool ret = f.call(fixtureA, fixtureB);
    }

    virtual bool ShouldCollide(b2Fixture* fixtureA, b2ParticleSystem* particleSystem, int32 particleIndex) {
        py::object f = object_.attr("ShouldCollideFixtureParticle");
        bool ret = f.call(fixtureA, particleSystem, particleIndex);
    }

    virtual bool ShouldCollide(b2ParticleSystem* particleSystem, int32 particleIndexA, int32 particleIndexB) {
        py::object f = object_.attr("ShouldCollideParticleParticle");
        bool ret = f.call(particleSystem, particleIndexA, particleIndexB);
    }
private:
    py::object object_;
};

class PyB2ContactListenerCaller : b2ContactListener{
public:


    virtual ~PyB2ContactListenerCaller() {}
    PyB2ContactListenerCaller(const py::object & object)
    : object_(object){
    }


    virtual void BeginContact(b2Contact* contact) { 
        py::object f = object_.attr("BeginContact");
        f.call(contact);
    }

    virtual void EndContact(b2Contact* contact) { 
        py::object f = object_.attr("EndContact");
        f.call(contact);
    }


    virtual void BeginContact(b2ParticleSystem* particleSystem,
                              b2ParticleBodyContact* particleBodyContact){
        py::object f = object_.attr("BeginContactParticleBoddy");
        f.call(particleSystem, particleBodyContact);
    }

    virtual void EndContact(b2Fixture* fixture,
                            b2ParticleSystem* particleSystem, int32 index){
        py::object f = object_.attr("EndContactFixtureParticle");
        f.call(fixture, particleSystem, particleBodyContact);  
    }

    virtual void BeginContact(b2ParticleSystem* particleSystem,
                              b2ParticleContact* particleContact){
        py::object f = object_.attr("BeginContactParticle");
        f.call(particleSystem,  particleContact);  
    }

    virtual void EndContact(b2ParticleSystem* particleSystem,
                            int32 indexA, int32 indexB){
        py::object f = object_.attr("EndContactParticle");
        f.call(particleSystem,  indexA, indexB);  
    }

    virtual void PreSolve(b2Contact* contact, const b2Manifold* oldManifold){
        py::object f = object_.attr("PreSolve");
        f.call(contact,  oldManifold);  
    }

    virtual void PostSolve(b2Contact* contact, const b2ContactImpulse* impulse){
        py::object f = object_.attr("PostSolve");
        f.call(contact,  impulse);  
    }
private:
    py::object object_;
};




