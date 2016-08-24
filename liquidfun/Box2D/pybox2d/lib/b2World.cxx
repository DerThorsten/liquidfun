#include <pybind11/pybind11.h>

#include <Box2D/Box2D.h>
//#include <Box2D/extensions/multi_gravity_world.hxx>
#include "pyb2Draw.hxx"
#include "pyb2WorldCallbacks.hxx"
//#include "type_caster.hxx"

namespace py = pybind11;




void exportB2World(py::module & pybox2dModule){

    py::class_<b2World>(pybox2dModule,"b2World")
        .def(py::init<const b2Vec2 & >(),py::arg("gravity"))
        .def("__init__",[](b2World & instance,  std::pair<float,float>  arg){
            new(&instance) b2World(b2Vec2(arg.first,arg.second));
        }, py::arg("gravity") = std::pair<float,float>(0,-9.81))

        .def("setContactListener", [](b2World & w, PyB2ContactListenerCaller * listener){
            w.SetContactListener(listener);
        },py::arg("listener")) 

        .def("setDestructionListener", [](b2World & w, PyB2DestructionListenerCaller * listener){
            w.SetDestructionListener(listener);
        },py::arg("listener"))

        .def("setContactFilter", [](b2World & w, PyB2ContactFilterCaller * listener){
            w.SetContactFilter(listener);
        },py::arg("listener")) 
        .def("setDebugDraw", [](b2World & w, PyB2Draw * d){w.SetDebugDraw(d);},py::arg("debugDraw"))
        .def("_createBodyCpp", &b2World::CreateBody, py::return_value_policy::reference_internal)
        .def("destroyBody", 
            [](b2World & world, b2Body *  body){
                auto vud = body->GetUserData();
                if(vud!=nullptr){
                    auto ud = static_cast<py::object *>(vud);
                    delete ud;
                    body->SetUserData(nullptr);
                }
                world.DestroyBody(body);
            }
            ,py::arg("body")
        )
        .def("createJoint",&b2World::CreateJoint,py::return_value_policy::reference_internal)
        .def("destroyJoint", 
            [](b2World & world, b2Joint *  joint){
                auto vud = joint->GetUserData();
                if(vud!=nullptr){
                    auto ud = static_cast<py::object *>(vud);
                    delete ud;
                    joint->SetUserData(nullptr);
                }
                world.DestroyJoint(joint);
            }
            ,py::arg("body")
        )
        .def("createParticleSystem",&b2World::CreateParticleSystem, py::return_value_policy::reference_internal)
        .def("destroyParticleSystem",&b2World::DestroyParticleSystem)
        .def("step",[&]
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
        .def("calculateReasonableParticleIterations",&b2World::CalculateReasonableParticleIterations)
        .def("clearForces",&b2World::ClearForces)
        .def("drawDebugData",&b2World::DrawDebugData)
        .def("queryAABB", 
            [](const b2World & world, PyB2QueryCallbackCaller * cb, const b2AABB & aabb ){
                return world.QueryAABB(cb, aabb);
        })
        .def("rayCast", 
            [](const b2World & world, PyB2RayCastCallbackCaller * cb, const b2Vec2 & pa,const b2Vec2 & pb ){
                return world.RayCast(cb, pa, pb);
        })
        
        .def("shiftOrigin",&b2World::ShiftOrigin)


        // py extended properties
        .def("_getBodyList", [](const b2World & w){
            return  w.GetBodyList();
        }, py::return_value_policy::reference_internal)
        .def("_getBodyList", []( b2World & w){
            return  w.GetBodyList();
        }, py::return_value_policy::reference_internal)

        .def("_getJointList", [](const b2World & w){
            return  w.GetJointList();
        }, py::return_value_policy::reference_internal)
        .def("_getJointList", []( b2World & w){
            return  w.GetJointList();
        }, py::return_value_policy::reference_internal)

        .def("_getContactList", [](const b2World & w){
            return  w.GetContactList();
        }, py::return_value_policy::reference_internal)
        .def("_getContactList", []( b2World & w){
            return  w.GetContactList();
        }, py::return_value_policy::reference_internal)


        .def("_getParticleSystemList", [](const b2World & w){
            return  w.GetParticleSystemList();
        }, py::return_value_policy::reference_internal)
        .def("_getParticleSystemList", []( b2World & w){
            return  w.GetParticleSystemList();
        }, py::return_value_policy::reference_internal)

        // properties
        .def_property("allowSleeping",&b2World::GetAllowSleeping,&b2World::SetAllowSleeping)
        .def_property("warmStarting",&b2World::GetWarmStarting,&b2World::SetWarmStarting)
        .def_property("continuousPhysics",&b2World::GetContinuousPhysics,&b2World::SetContinuousPhysics)
        .def_property("subStepping",&b2World::GetSubStepping,&b2World::SetSubStepping)
        .def_property("warmStarting",&b2World::GetWarmStarting,&b2World::SetWarmStarting)
        .def_property("gravity",&b2World::GetGravity, [](b2World & w,const b2Vec2 & g){w.SetGravity(g);})
        .def_property_readonly("locked",&b2World::IsLocked)
        .def_property("autoClearForces",&b2World::GetAutoClearForces,&b2World::SetAutoClearForces)


        .def_property_readonly("proxyCount",&b2World::GetProxyCount)
        .def_property_readonly("bodyCount",&b2World::GetBodyCount)
        .def_property_readonly("jointCount",&b2World::GetJointCount)
        .def_property_readonly("contactCount",&b2World::GetContactCount)
        .def_property_readonly("treeHeight",&b2World::GetTreeHeight)
        .def_property_readonly("treeBalance",&b2World::GetTreeBalance)
        .def_property_readonly("treeQuality",&b2World::GetTreeQuality)
        .def_property_readonly("contactManager",&b2World::GetContactManager)
        .def_property_readonly("profile",&b2World::GetProfile)

        
      
    ;

}

