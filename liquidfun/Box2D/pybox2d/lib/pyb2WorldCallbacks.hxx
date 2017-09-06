#include <pybind11/pybind11.h>

#include <Box2D/Box2D.h>
#include <iostream>
#include "proxies.hxx"

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
        py::object f = object_.attr("sayGoodbyeJoint");
        f(joint);
    }
    virtual void SayGoodbye(b2Fixture * fixture)  {
        py::object f = object_.attr("sayGoodbyeFixture");
        f(fixture);
    }
    virtual void SayGoodbye(b2ParticleGroup* group){
        py::object f = object_.attr("sayGoodbyeParticleGroup");
        f(group);
    }

    virtual void SayGoodbye(b2ParticleSystem* particleSystem, int32 index){
        py::object f = object_.attr("sayGoodbyeParticleSystem");
        f(particleSystem, index);
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
        py::object f = object_.attr("shouldCollideFixtureFixture");
        bool ret = f(fixtureA, fixtureB).cast<bool>();
        return ret;
    }

    virtual bool ShouldCollide(b2Fixture* fixtureA, b2ParticleSystem* particleSystem, int32 particleIndex) {
        py::object f = object_.attr("shouldCollideFixtureParticle");
        bool ret = f(fixtureA, particleSystem, particleIndex).cast<bool>();
        return ret;
    }

    virtual bool ShouldCollide(b2ParticleSystem* particleSystem, int32 particleIndexA, int32 particleIndexB) {
        py::object f = object_.attr("shouldCollideParticleParticle");
        bool ret = f(particleSystem, particleIndexA, particleIndexB).cast<bool>();
        return ret;
    }
private:
    py::object object_;
};

class PyB2ContactListenerCaller : public b2ContactListener{
public:


    virtual ~PyB2ContactListenerCaller() {}
    PyB2ContactListenerCaller(const py::object & object)
    : object_(object){
    }


    virtual void BeginContact(b2Contact* contact) { 
        py::object f = object_.attr("beginContact");
        f(b2ContactProxy(contact));
    }

    virtual void EndContact(b2Contact* contact) { 
        py::object f = object_.attr("endContact");
        f(b2ContactProxy(contact));
    }


    virtual void BeginContact(b2ParticleSystem* particleSystem,
                              b2ParticleBodyContact* particleBodyContact){
        py::object f = object_.attr("beginContactParticleBody");
        f(particleSystem, particleBodyContact);
    }

    virtual void EndContact(b2Fixture* fixture,
                            b2ParticleSystem* particleSystem, int32 index){
        py::object f = object_.attr("endContactFixtureParticle");
        f(fixture, particleSystem, index);  
    }

    virtual void BeginContact(b2ParticleSystem* particleSystem,
                              b2ParticleContact* particleContact){
        py::object f = object_.attr("beginContactParticle");
        f(particleSystem,  particleContact);  
    }

    virtual void EndContact(b2ParticleSystem* particleSystem,
                            int32 indexA, int32 indexB){
        py::object f = object_.attr("endContactParticle");
        f(particleSystem,  indexA, indexB);  
    }

    virtual void PreSolve(b2Contact* contact, const b2Manifold* oldManifold){
        py::object f = object_.attr("preSolve");
        f(b2ContactProxy(contact),  b2ManifoldProxy(oldManifold)); 
    }

    virtual void PostSolve(b2Contact* contact, const b2ContactImpulse* impulse){
        py::object f = object_.attr("postSolve");
        f(b2ContactProxy(contact),  b2ContactImpulseProxy(impulse));  
    }
private:
    py::object object_;
};

class PyB2QueryCallbackCaller : public b2QueryCallback{
public:


    virtual ~PyB2QueryCallbackCaller() {}
    PyB2QueryCallbackCaller(const py::object & object)
    : object_(object){
    }

    virtual bool ReportFixture(b2Fixture* fixture){
        py::object f = object_.attr("ReportFixture");
        bool ret = f(fixture).cast<bool>();
        return ret;
    }

    /// Called for each particle found in the query AABB.
    /// @return false to terminate the query.
    virtual bool ReportParticle(const b2ParticleSystem* particleSystem,
                                int32 index)
    {

        py::object f = object_.attr("ReportParticle");
        bool ret = f(particleSystem, index).cast<bool>();
        return ret;
    }

    /// Cull an entire particle system from b2World::QueryAABB. Ignored for
    /// b2ParticleSystem::QueryAABB.
    /// @return true if you want to include particleSystem in the AABB query,
    /// or false to cull particleSystem from the AABB query.
    virtual bool ShouldQueryParticleSystem(
        const b2ParticleSystem* particleSystem)
    {
        
        py::object f = object_.attr("ShouldQueryParticleSystem");
        bool ret = f(particleSystem).cast<bool>();
        return ret;
    }
private:
    py::object object_;
};

class PyB2RayCastCallbackCaller : public b2RayCastCallback
{
public:
    virtual ~PyB2RayCastCallbackCaller() {}
    PyB2RayCastCallbackCaller(const py::object & object)
    : object_(object){
    }
    /// Called for each fixture found in the query. You control how the ray cast
    /// proceeds by returning a float:
    /// return -1: ignore this fixture and continue
    /// return 0: terminate the  cast
    /// return fraction: clip the ray to this point
    /// return 1: don't clip the ray and continue
    /// @param fixture the fixture hit by the ray
    /// @param point the point of initial intersection
    /// @param normal the normal vector at the point of intersection
    /// @return -1 to filter, 0 to terminate, fraction to clip the ray for
    /// closest hit, 1 to continue
    virtual float32 ReportFixture(  b2Fixture* fixture, const b2Vec2& point,
                                    const b2Vec2& normal, float32 fraction){

        py::object f = object_.attr("ReportFixture");
        float ret = f(fixture, point, normal, fraction).cast<float>();
        return ret;
    }

    /// Called for each particle found in the query. You control how the ray
    /// cast proceeds by returning a float:
    /// return <=0: ignore the remaining particles in this particle system
    /// return fraction: ignore particles that are 'fraction' percent farther
    ///   along the line from 'point1' to 'point2'. Note that 'point1' and
    ///   'point2' are parameters to b2World::RayCast.
    /// @param particleSystem the particle system containing the particle
    /// @param index the index of the particle in particleSystem
    /// @param point the point of intersection bt the ray and the particle
    /// @param normal the normal vector at the point of intersection
    /// @param fraction percent (0.0~1.0) from 'point0' to 'point1' along the
    ///   ray. Note that 'point1' and 'point2' are parameters to
    ///   b2World::RayCast.
    /// @return <=0 to ignore rest of particle system, fraction to ignore
    /// particles that are farther away.
    virtual float32 ReportParticle(const b2ParticleSystem* particleSystem,
                                   int32 index, const b2Vec2& point,
                                   const b2Vec2& normal, float32 fraction)
    {
        B2_NOT_USED(particleSystem);
        B2_NOT_USED(index);
        B2_NOT_USED(&point);
        B2_NOT_USED(&normal);
        B2_NOT_USED(fraction);
        return 0;
    }

    /// Cull an entire particle system from b2World::RayCast. Ignored in
    /// b2ParticleSystem::RayCast.
    /// @return true if you want to include particleSystem in the RayCast, or
    /// false to cull particleSystem from the RayCast.
    virtual bool ShouldQueryParticleSystem(
        const b2ParticleSystem* particleSystem)
    {
        B2_NOT_USED(particleSystem);
        return true;
    }
private:
    py::object object_;
};
