#include <pybind11/pybind11.h>

#include <Box2D/Box2D.h>
#include "pyb2Draw.hxx"
#include "pyb2WorldCallbacks.hxx"

namespace py = pybind11;




void exportB2World(py::module & pybox2dModule){

    py::class_<b2World>(pybox2dModule,"b2World")
        .def(py::init<const b2Vec2 & >(),py::arg("gravity"))
        .def("SetDestructionListener", &b2World::SetDestructionListener , py::arg("listener"))
        .def("SetContactFilter", &b2World::SetContactFilter , py::arg("filter"))
        .def("SetContactListener", &b2World::SetContactListener , py::arg("listener"))
        .def("SetDebugDraw", [](b2World & w, PyB2Draw * d){w.SetDebugDraw(d);},py::arg("debugDraw"))
        .def("_CreateBodyCpp", &b2World::CreateBody, py::return_value_policy::reference_internal)
        .def("DestroyBody", 
         [](b2World & world, b2Body *  body){
            auto vud = body->GetUserData();
            if(vud!=nullptr){
                auto ud = static_cast<py::object *>(vud);
                delete ud;
                body->SetUserData(nullptr);
            }
            world.DestroyBody(body);
         }
        ,py::arg("body"))
        .def("CreateJoint",&b2World::CreateJoint,py::return_value_policy::reference_internal)
        .def("DestroyJoint", &b2World::DestroyJoint,py::arg("joint"))
        .def("CreateParticleSystem",&b2World::CreateParticleSystem, py::return_value_policy::reference_internal)
        .def("DestroyParticleSystem",&b2World::DestroyParticleSystem)
        .def("Step",[&]
            (b2World & self, float32 timeStep, 
            int32 velocityIterations, int32 positionIterations,
            int32 particleIterations){

                self.Step(timeStep, velocityIterations, positionIterations,particleIterations);
            },
            py::arg("timeStep"),
            py::arg("velocityIterations"),
            py::arg("positionIterations"),
            py::arg("particleIterations") = 1
        )
        .def("CalculateReasonableParticleIterations",&b2World::CalculateReasonableParticleIterations)
        .def("ClearForces",&b2World::ClearForces)
        .def("DrawDebugData",&b2World::DrawDebugData)
        .def("QueryAABB", 
            [](const b2World & world, PyB2QueryCallbackCaller * cb, const b2AABB & aabb ){
                return world.QueryAABB(cb, aabb);
        })
            //.def("RayCast",&b2World::QueryAABB)
                // lists
        .def("_GetBodyList", [](const b2World & w){
            return  w.GetBodyList();
        }, py::return_value_policy::reference_internal)
        .def("_GetBodyList", []( b2World & w){
            return  w.GetBodyList();
        }, py::return_value_policy::reference_internal)

        .def("_GetJointList", [](const b2World & w){
            return  w.GetJointList();
        }, py::return_value_policy::reference_internal)
        .def("_GetJointList", []( b2World & w){
            return  w.GetJointList();
        }, py::return_value_policy::reference_internal)

        .def("_GetContactList", [](const b2World & w){
            return  w.GetContactList();
        }, py::return_value_policy::reference_internal)
        .def("_GetContactList", []( b2World & w){
            return  w.GetContactList();
        }, py::return_value_policy::reference_internal)

        .def("SetAllowSleeping",&b2World::SetAllowSleeping)
        .def("GetAllowSleeping",&b2World::GetAllowSleeping)
        .def("SetWarmStarting",&b2World::SetWarmStarting)
        .def("GetWarmStarting",&b2World::GetWarmStarting)
        .def("SetContinuousPhysics",&b2World::SetContinuousPhysics)
        .def("GetContinuousPhysics",&b2World::GetContinuousPhysics)
        .def("SetSubStepping",&b2World::SetSubStepping)
        .def("GetSubStepping",&b2World::GetSubStepping)
        .def("GetProxyCount",&b2World::GetProxyCount)
        .def("GetBodyCount",&b2World::GetBodyCount)
        .def("GetJointCount",&b2World::GetJointCount)
        .def("GetContactCount",&b2World::GetContactCount)
        .def("GetTreeHeight",&b2World::GetTreeHeight)
        .def("GetTreeBalance",&b2World::GetTreeBalance)
        .def("GetTreeQuality",&b2World::GetTreeQuality)
        .def("SetGravity",[](b2World & w,const b2Vec2 & g){w.SetGravity(g);})
        .def("GetGravity",&b2World::GetGravity)
        .def("IsLocked",&b2World::IsLocked)
        .def("SetAutoClearForces",&b2World::SetAutoClearForces)
        .def("GetAutoClearForces",&b2World::GetAutoClearForces)
        .def("ShiftOrigin",&b2World::ShiftOrigin)
        .def("GetContactManager",&b2World::GetContactManager, py::return_value_policy::reference_internal)
        .def("GetProfile",&b2World::GetProfile, py::return_value_policy::reference_internal)

        
      
    ;

}

