#include <pybind11/pybind11.h>

#include <Box2D/Box2D.h>

namespace py = pybind11;





void exportB2Body(py::module & pybox2dModule){



    py::enum_<b2BodyType>(pybox2dModule, "b2BodyType")
        .value("b2_staticBody", b2BodyType::b2_staticBody)
        .value("b2_kinematicBody", b2BodyType::b2_kinematicBody)
        .value("b2_dynamicBody", b2BodyType::b2_dynamicBody)
    ;
        //.export_values();


    py::class_<b2BodyDef>(pybox2dModule,"b2BodyDef")
        .def(py::init<>())
        .def_readwrite("btype", &b2BodyDef::type)
        .def_readwrite("_position", &b2BodyDef::position)
        .def_readwrite("angle", &b2BodyDef::angle)
        .def_readwrite("linearVelocity", &b2BodyDef::linearVelocity)
        .def_readwrite("angularVelocity", &b2BodyDef::angularVelocity)
        .def_readwrite("linearDamping", &b2BodyDef::linearDamping)
        .def_readwrite("angularDamping", &b2BodyDef::angularDamping)
        .def_readwrite("allowSleep", &b2BodyDef::allowSleep)
        .def_readwrite("awake", &b2BodyDef::awake)
        .def_readwrite("fixedRotation", &b2BodyDef::fixedRotation)
        .def_readwrite("bullet", &b2BodyDef::bullet)
        //.def_readwrite("userData", &b2BodyDef::userData)
        .def("_hasUserData",[](const b2BodyDef & b){return b.userData!=nullptr;})
        .def("_setUserData",[](b2BodyDef & b, const py::object & ud){
            auto ptr = new py::object(ud);
            b.userData = ptr;
        })
        .def("_getUserData",[](const b2BodyDef & b){
            auto vuserData = b.userData;
            auto ud = static_cast<py::object *>(vuserData);
            auto ret = py::object(*ud);
            return ret;
        })
        .def("_deleteUserData",[](b2BodyDef & b){
            auto vuserData = b.userData;
            auto ud = static_cast<py::object *>(vuserData);
            delete ud;
            b.userData = nullptr;
        })
        .def_readwrite("gravityScale", &b2BodyDef::gravityScale)
    ;

    py::class_<b2Body>(pybox2dModule,"b2Body")
        //.def(py::init<>())
        .def("createFixture",
            [&](b2Body & body, b2Shape * shape, float32 density){
                return body.CreateFixture(shape, density);
            },
            py::arg("shape"),
            py::arg("density") = 1.0, py::return_value_policy::reference_internal
        )
        .def("createFixture",
            [&](b2Body & body, const b2FixtureDef * def){
                return body.CreateFixture(def);
            },
            py::arg("fixtureDef"), py::return_value_policy::reference_internal
        )
        .def("_createFixtureFromFixtureDef",
            [&](b2Body & body, const b2FixtureDef * def){
                return body.CreateFixture(def);
            },
            py::arg("fixtureDef"), py::return_value_policy::reference_internal
        )
        .def("destroyFixture",&b2Body::DestroyFixture,py::arg("fixture"))

        
        .def("setTransform", 
            (void (b2Body::*)(const b2Vec2 &, float32)) &b2Body::SetTransform,
            py::arg("position"),py::arg("angle")
        )
        .def("setTransform", 
            (void (b2Body::*)(float32, float32, float32)) &b2Body::SetTransform,
            py::arg("positionX"),py::arg("positionY"),py::arg("angle")
        )


        .def_property_readonly("transform", &b2Body::GetTransform)
        .def_property_readonly("position", &b2Body::GetPosition)
        .def_property_readonly("angle", &b2Body::GetAngle)
        .def_property_readonly("worldCenter",&b2Body::GetWorldCenter)
        .def_property_readonly("getLocalCenter",&b2Body::GetLocalCenter)
        .def_property_readonly("mass",&b2Body::GetMass)
        .def_property_readonly("inertia",&b2Body::GetInertia)



        //.def_property_readonly("world",&b2Body::GetWorl)

        .def_property("linearVelocity",&b2Body::GetLinearVelocity,&b2Body::SetLinearVelocity)
        .def_property("angularVelocity",&b2Body::GetAngularVelocity,&b2Body::SetAngularVelocity)
        .def_property("massData",&b2Body::GetMassData,&b2Body::SetMassData)
        .def_property("bullet",&b2Body::IsBullet,&b2Body::SetBullet)
        .def_property("btype",&b2Body::GetType,&b2Body::SetType)
        .def_property("sleepingAllowed",&b2Body::IsSleepingAllowed,&b2Body::SetSleepingAllowed)
        .def_property("awake",&b2Body::IsAwake,&b2Body::SetAwake)
        .def_property("active",&b2Body::IsActive,&b2Body::SetActive)
        .def_property("fixedRotation",&b2Body::IsFixedRotation,&b2Body::SetFixedRotation)
        .def_property("gravityScale",&b2Body::GetGravityScale,&b2Body::SetGravityScale)
        .def_property("linearDamping",&b2Body::GetLinearDamping,&b2Body::SetLinearDamping)
        .def_property("angularDamping",&b2Body::GetAngularDamping,&b2Body::SetAngularDamping)


        .def("applyForce", &b2Body::ApplyForce, py::arg("force"), py::arg("point"), py::arg("wake"))
        .def("applyForceToCenter", &b2Body::ApplyForceToCenter, py::arg("force"), py::arg("wake"))
        .def("applyTorque", &b2Body::ApplyTorque, py::arg("torque"), py::arg("wake"))
        .def("applyLinearImpulse", &b2Body::ApplyLinearImpulse, py::arg("impulse"), py::arg("point"), py::arg("wake"))
        .def("applyAngularImpulse", &b2Body::ApplyAngularImpulse, py::arg("impulse"), py::arg("wake"))

        .def("resetMassData", &b2Body::ResetMassData)  
        .def("getWorldPoint", &b2Body::GetWorldPoint, py::arg("localPoint"))
        .def("getWorldVector", &b2Body::GetWorldVector, py::arg("localVector"))
        .def("getLocalPoint", &b2Body::GetLocalPoint, py::arg("worldPoint"))
        .def("getLocalVector", &b2Body::GetLocalVector, py::arg("worldVector"))
        .def("getLinearVelocityFromWorldPoint", &b2Body::GetLinearVelocityFromWorldPoint, py::arg("worldPoint"))
        .def("getLinearVelocityFromLocalPoint", &b2Body::GetLinearVelocityFromLocalPoint, py::arg("localPoint"))

     
        // will be extended on the python side
        .def("_hasFixtureList",[]( b2Body & body){return body.GetFixtureList()!= nullptr;})
        .def("_getFixtureList",[]( b2Body & body){return body.GetFixtureList();}, py::return_value_policy::reference_internal)
        .def("_getFixtureList",[](const b2Body & body){return body.GetFixtureList();}, py::return_value_policy::reference_internal)
        .def("_hasJointList",[]( b2Body & body){return body.GetJointList()!= nullptr;})
        .def("_GetJointList",[]( b2Body & body){return body.GetJointList();}, py::return_value_policy::reference_internal)
        .def("_GetJointList",[](const b2Body & body){return body.GetJointList();}, py::return_value_policy::reference_internal)
        .def("_hasContactList",[]( b2Body & body){return body.GetContactList()!= nullptr;})
        .def("_GetContactList",[]( b2Body & body){return body.GetContactList();}, py::return_value_policy::reference_internal)
        .def("_GetContactList",[](const b2Body & body){return body.GetContactList();}, py::return_value_policy::reference_internal)
        .def("_hasNext", [](b2Body &b){ return b.GetNext()!=nullptr;})
        .def("_getNext", [](b2Body &b){return b.GetNext();}, py::return_value_policy::reference_internal)        
        .def("_getWorld",[]( b2Body & body){return body.GetWorld();}, py::return_value_policy::reference_internal)
        .def("_getWorld",[](const b2Body & body){return body.GetWorld();}, py::return_value_policy::reference_internal)


        .def("_hasUserData",[](const b2Body & b){return b.GetUserData()!=nullptr;})
        .def("_setUserData",[](b2Body & b, const py::object & ud){
            auto ptr = new py::object(ud);
            b.SetUserData(ptr);
        })
        .def("_getUserData",[](const b2Body & b){
            auto vuserData = b.GetUserData();
            auto ud = static_cast<py::object *>(vuserData);
            auto ret = py::object(*ud);
            return ret;
        })
        .def("_deleteUserData",[](b2Body & b){
            auto vuserData = b.GetUserData();
            auto ud = static_cast<py::object *>(vuserData);
            delete ud;
            b.SetUserData(nullptr);
        })

        // in order
        
    ;

}
