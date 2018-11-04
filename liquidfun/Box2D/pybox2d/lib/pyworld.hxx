#pragma once
#include <Box2D/Box2D.h>
#include <pybind11/pybind11.h>
#include "vectorize.hxx"
#include "pyb2WorldCallbacks.hxx"
#include <memory>

#include "user_data.hxx"

class FindBodiesInRadiusQueryCallback : public b2QueryCallback
{
public:
    FindBodiesInRadiusQueryCallback(
        BodySet & bodySet,
        const b2Vec2 &  center, 
        const float32 radius_min,
        const float32 radius_max,
        const bool only_body_of_type,
        const b2BodyType selected_body_type
    )
    :   m_center(center),
        m_radius_min(radius_min),
        m_radius_max(radius_max),
        m_only_body_of_type(only_body_of_type),
        m_selected_body_type(),
        m_body_set_ref(bodySet)
    {
        m_body_set_ref.clear();
    }

    virtual ~FindBodiesInRadiusQueryCallback() {}

    /// Called for each fixture found in the query AABB.
    /// @return false to terminate the query.
    bool ReportFixture(b2Fixture* fixture) override
    {
        auto body  = fixture->GetBody();
        if(!m_only_body_of_type || body->GetType() == m_selected_body_type);
        auto center = body->GetWorldCenter();
        auto d = (m_center - m_center).Length();
        if( d >= m_radius_min && d < m_radius_max)
        {
            m_body_set_ref.insert(body);
        }
    }



    /// Cull an entire particle system from b2World::QueryAABB. Ignored for
    /// b2ParticleSystem::QueryAABB.
    /// @return true if you want to include particleSystem in the AABB query,
    /// or false to cull particleSystem from the AABB query.
    bool ShouldQueryParticleSystem(const b2ParticleSystem* particleSystem) override
    {
        B2_NOT_USED(particleSystem);
        return false;
    }
private:
    b2Vec2 m_center;
    float32 m_radius_min;
    float32 m_radius_max;
    bool m_only_body_of_type;
    b2BodyType m_selected_body_type;
    BodySet & m_body_set_ref;
};




class PyWorld : public b2World
{
public:
    PyWorld(const b2Vec2& gravity)
    :   b2World(gravity),
        m_destruction_listener(new PyWorldDestructionListenerCaller())
    {
        // install destruction listener
        this->SetDestructionListener(m_destruction_listener.get());
    }
    ~PyWorld(){
        for ( b2Body* b = this->GetBodyList(); b; b = b->GetNext())
        {
            delete_user_data_if_has_user_data(b);
        }
    }

    void set_py_destruction_listener(const py::object & object)
    {
        this->m_destruction_listener->set_py_destruction_listener(object);
    }

    BodySet findBodiesInRadius(
        const b2Vec2 &  center, 
        const float32 radius_min,
        const float32 radius_max,
        const bool only_body_of_type,
        const b2BodyType selected_body_type
    )
    {
        // the callback
        BodySet result;
        FindBodiesInRadiusQueryCallback callback(
            result, center, radius_min, radius_max,
            only_body_of_type, selected_body_type);

        // the aabb
        b2AABB aabb;
        aabb.lowerBound = center - radius_max;
        aabb.upperBound = center + radius_max;

        // do the query
        
        this->QueryAABB(&callback, aabb);
        return result;
    }

private:
    std::unique_ptr<PyWorldDestructionListenerCaller> m_destruction_listener;
};