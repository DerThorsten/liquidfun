#pragma once

#include <pybind11/pybind11.h>

#include <Box2D/Box2D.h>
#include <iostream>

#include "holder.hxx"
#include "user_data.hxx"

namespace py = pybind11;






class PyWorldDestructionListenerCaller : public b2DestructionListener {
public:

    virtual ~PyWorldDestructionListenerCaller() {}

    PyWorldDestructionListenerCaller()
    :   object_(),
        m_has_obj(false)
    {
    }
    PyWorldDestructionListenerCaller(const py::object & object)
    :   object_(object),
        m_has_obj(bool(object_))
    {
    }

    void set_py_destruction_listener(const py::object & object)
    {
        object_ = object;
        m_has_obj = true;
    }

    void SayGoodbye(b2Joint * joint) override {
        if(m_has_obj)
        {
            py::object f = object_.attr("say_goodbye_joint");
            f(JointHolder(joint));
        }
        delete_user_data_if_has_user_data(joint);
    }
    void SayGoodbye(b2Fixture * fixture) override {

        if(m_has_obj)
        {
            py::object f = object_.attr("say_goodbye_fixture");
            f(FixtureHolder(fixture));
        }
        delete_user_data_if_has_user_data(fixture);
    }
    void SayGoodbye(b2ParticleGroup* group) override {
        if(m_has_obj)
        {
            py::object f = object_.attr("say_goodbye_particle_group");
            f(ParticleGroupHolder(group));
        }
        delete_user_data_if_has_user_data(group);
    }

    void SayGoodbye(b2ParticleSystem* particleSystem, int32 index) override {
        if(m_has_obj)
        {
            py::object f = object_.attr("say_goodbye_particle_System");
            f(ParticleSystemHolder(particleSystem), index);
        }
        // check me....
        //delete_user_data_if_has_user_data(group);

    }
private:
    py::object object_;
    bool m_has_obj;
};




class PyB2DestructionListenerCaller : public b2DestructionListener {
public:
    /* Inherit the constructors */
    //using b2DestructionListener::b2DestructionListener;

    virtual ~PyB2DestructionListenerCaller() {}

    PyB2DestructionListenerCaller(const py::object & object)
    : object_(object){
    }
    virtual void SayGoodbye(b2Joint * joint)  {
        py::object f = object_.attr("say_goodbye_joint");
        f(JointHolder(joint));
    }
    virtual void SayGoodbye(b2Fixture * fixture)  {
        py::object f = object_.attr("say_goodbye_fixture");
        f(FixtureHolder(fixture));
    }
    virtual void SayGoodbye(b2ParticleGroup* group){
        py::object f = object_.attr("say_goodbye_particle_group");
        f(ParticleGroupHolder(group));
    }

    virtual void SayGoodbye(b2ParticleSystem* particleSystem, int32 index){
        py::object f = object_.attr("say_goodbye_particle_System");
        f(ParticleSystemHolder(particleSystem), index);
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
        py::object f = object_.attr("should_collide_fixture_fixture");
        bool ret = f(FixtureHolder(fixtureA), FixtureHolder(fixtureB)).cast<bool>();
        return ret;
    }

    virtual bool ShouldCollide(b2Fixture* fixtureA, b2ParticleSystem* particleSystem, int32 particleIndex) {
        py::object f = object_.attr("should_collide_fixture_particle");
        bool ret = f(FixtureHolder(fixtureA), ParticleSystemHolder(particleSystem), particleIndex).cast<bool>();
        return ret;
    }

    virtual bool ShouldCollide(b2ParticleSystem* particleSystem, int32 particleIndexA, int32 particleIndexB) {
        py::object f = object_.attr("should_collide_particle_particle");
        bool ret = f(ParticleSystemHolder(particleSystem), particleIndexA, particleIndexB).cast<bool>();
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
        py::object f = object_.attr("begin_contact");
        //std::cout<<"call begin_contact"<<std::endl;
        f(ContactHolder(contact));
        //std::cout<<"after call begin_contact"<<std::endl;
    }

    virtual void EndContact(b2Contact* contact) { 
        py::object f = object_.attr("end_contact");
        //std::cout<<"call end_contact"<<std::endl;
        f(ContactHolder(contact));
        //std::cout<<"after call end_contact"<<std::endl;

    }


    virtual void BeginContact(b2ParticleSystem* particleSystem,
                              b2ParticleBodyContact* particleBodyContact){
        py::object f = object_.attr("begin_contact_particle_body");
        f(ParticleSystemHolder(particleSystem), particleBodyContact);
        //std::cout<<"after call begin_contact_particle_body"<<std::endl;
    }

    virtual void EndContact(b2Fixture* fixture,
                            b2ParticleSystem* particleSystem, int32 index){
        py::object f = object_.attr("end_contact_fixture_particle");
        //std::cout<<"call end_contact_fixture_particle"<<std::endl;
        f(FixtureHolder(fixture), ParticleSystemHolder(particleSystem), index);  
        //std::cout<<"after call end_contact_fixture_particle"<<std::endl;
    }

    virtual void BeginContact(b2ParticleSystem* particleSystem,
                              b2ParticleContact* particleContact){
        py::object f = object_.attr("begin_contact_particle");
        //std::cout<<"call begin_contact_particle"<<std::endl;
        f(ParticleSystemHolder(particleSystem),  particleContact);  
        //std::cout<<"after call begin_contact_particle"<<std::endl;
    }

    virtual void EndContact(b2ParticleSystem* particleSystem,
                            int32 indexA, int32 indexB){
        py::object f = object_.attr("end_pontact_particle");
        //std::cout<<"call end_pontact_particle"<<std::endl;
        f(ParticleSystemHolder(particleSystem),  indexA, indexB);  
        //std::cout<<"after call end_pontact_particle"<<std::endl;
    }

    virtual void PreSolve(b2Contact* contact, const b2Manifold* oldManifold){
        py::object f = object_.attr("pre_solve");
        //std::cout<<"call pre_solve"<<std::endl;
        f(ContactHolder(contact),  ManifoldHolder(oldManifold)); 
        //std::cout<<"after call pre_solve"<<std::endl;
    }

    virtual void PostSolve(b2Contact* contact, const b2ContactImpulse* impulse){
        py::object f = object_.attr("post_solve");
        //std::cout<<"call post_solve"<<std::endl;
        f(ContactHolder(contact),  ContactImpulseHolder(impulse));  
        //std::cout<<"after call post_solve"<<std::endl;
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
        py::object f = object_.attr("report_fixture");
        bool ret = f(fixture).cast<bool>();;
        return ret;
    }

    /// Called for each particle found in the query AABB.
    /// @return false to terminate the query.
    virtual bool ReportParticle(const b2ParticleSystem* particleSystem,
                                int32 index)
    {

        py::object f = object_.attr("report_particle");
        bool ret = f(particleSystem, index).cast<bool>();;
        return ret;
    }

    /// Cull an entire particle system from b2World::QueryAABB. Ignored for
    /// b2ParticleSystem::QueryAABB.
    /// @return true if you want to include particleSystem in the AABB query,
    /// or false to cull particleSystem from the AABB query.
    virtual bool ShouldQueryParticleSystem(
        const b2ParticleSystem* particleSystem)
    {
        
        py::object f = object_.attr("should_query_particle_system");
        bool ret = f(particleSystem).cast<bool>();;
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

        py::object f = object_.attr("report_fixture");
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
