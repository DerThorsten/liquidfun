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
        .def_readwrite("type", &b2BodyDef::type)
        .def_readwrite("position", &b2BodyDef::position)
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
        .def("HasUserData",[](const b2BodyDef & b){return b.userData!=nullptr;})
        .def("_SetUserData",[](b2BodyDef & b, const py::object & ud){
            auto ptr = new py::object(ud);
            b.userData = ptr;
        })
        .def("_GetUserData",[](const b2BodyDef & b){
            auto vuserData = b.userData;
            auto ud = static_cast<py::object *>(vuserData);
            auto ret = py::object(*ud);
            return ret;
        })
        .def("_DeleteUserData",[](b2BodyDef & b){
            auto vuserData = b.userData;
            auto ud = static_cast<py::object *>(vuserData);
            delete ud;
            b.userData = nullptr;
        })
        .def_readwrite("gravityScale", &b2BodyDef::gravityScale)
    ;

    py::class_<b2Body>(pybox2dModule,"b2Body")
        //.def(py::init<>())
        .def("CreateFixture",
            [&](b2Body & body, b2Shape * shape, float32 density){
                return body.CreateFixture(shape, density);
            },
            py::arg("shape"),
            py::arg("density") = 1.0, py::return_value_policy::reference_internal
        )
        .def("CreateFixture",
            [&](b2Body & body, const b2FixtureDef * def){
                return body.CreateFixture(def);
            },
            py::arg("fixtureDef"), py::return_value_policy::reference_internal
        )
        .def("DestroyFixture",&b2Body::DestroyFixture,py::arg("fixture"))

        
        .def("SetTransform", 
            (void (b2Body::*)(const b2Vec2 &, float32)) &b2Body::SetTransform,
            py::arg("position"),py::arg("angle")
        )
        .def("SetTransform", 
            (void (b2Body::*)(float32, float32, float32)) &b2Body::SetTransform,
            py::arg("positionX"),py::arg("positionY"),py::arg("angle")
        )
        .def("GetTransform", &b2Body::GetTransform, py::return_value_policy::reference_internal)
        .def("GetPosition", &b2Body::GetPosition, py::return_value_policy::reference_internal)
        .def_property_readonly("position", &b2Body::GetPosition)
        .def("GetAngle", &b2Body::GetAngle)
        .def_property_readonly("angle", &b2Body::GetAngle)
        .def("GetWorldCenter", &b2Body::GetWorldCenter, py::return_value_policy::reference_internal)
        .def("GetLocalCenter", &b2Body::GetLocalCenter, py::return_value_policy::reference_internal)
        .def("SetLinearVelocity", &b2Body::SetLinearVelocity, py::arg("v"))
        .def("GetLinearVelocity", &b2Body::GetLinearVelocity, py::return_value_policy::reference_internal)
        .def("SetAngularVelocity", &b2Body::SetAngularVelocity, py::arg("omega"))
        .def("GetAngularVelocity", &b2Body::GetAngularVelocity)
        .def("ApplyForce", &b2Body::ApplyForce, py::arg("force"), py::arg("point"), py::arg("wake"))
        .def("ApplyForceToCenter", &b2Body::ApplyForceToCenter, py::arg("force"), py::arg("wake"))
        .def("ApplyTorque", &b2Body::ApplyTorque, py::arg("torque"), py::arg("wake"))
        .def("ApplyLinearImpulse", &b2Body::ApplyLinearImpulse, py::arg("impulse"), py::arg("point"), py::arg("wake"))
        .def("ApplyAngularImpulse", &b2Body::ApplyAngularImpulse, py::arg("impulse"), py::arg("wake"))
        .def("GetMass", &b2Body::GetMass)
        .def("GetInertia", &b2Body::GetInertia)
        .def("GetMassData", &b2Body::GetMassData, py::arg("data"))
        .def("SetMassData", &b2Body::SetMassData, py::arg("data"))
        .def("ResetMassData", &b2Body::ResetMassData)  
        .def("GetWorldPoint", &b2Body::GetWorldPoint, py::arg("localPoint"))
        .def("GetWorldVector", &b2Body::GetWorldVector, py::arg("localVector"))
        .def("GetLocalPoint", &b2Body::GetLocalPoint, py::arg("worldPoint"))
        .def("GetLocalVector", &b2Body::GetLocalVector, py::arg("worldVector"))
        .def("GetLinearVelocityFromWorldPoint", &b2Body::GetLinearVelocityFromWorldPoint, py::arg("worldPoint"))
        .def("GetLinearVelocityFromLocalPoint", &b2Body::GetLinearVelocityFromLocalPoint, py::arg("localPoint"))
        .def("GetLinearDamping", &b2Body::GetLinearDamping)
        .def("SetLinearDamping", &b2Body::SetLinearDamping, py::arg("linearDamping"))
        .def("GetAngularDamping", &b2Body::GetAngularDamping)
        .def("SetAngularDamping", &b2Body::SetAngularDamping, py::arg("angularDamping"))
        .def("GetGravityScale", &b2Body::GetGravityScale)
        .def("SetGravityScale", &b2Body::SetGravityScale, py::arg("scale"))
        .def("GetType", &b2Body::GetType)
        .def("SetType", &b2Body::SetType, py::arg("bodyType"))
        .def("SetBullet", &b2Body::SetBullet, py::arg("flag"))
        .def("IsBullet", &b2Body::IsBullet)
        .def("SetSleepingAllowed", &b2Body::SetSleepingAllowed, py::arg("flag"))
        .def("IsSleepingAllowed", &b2Body::IsSleepingAllowed)
        .def("SetAwake", &b2Body::SetAwake, py::arg("flag"))
        .def("IsAwake", &b2Body::IsAwake)
        .def("SetActive", &b2Body::SetActive, py::arg("flag"))
        .def("IsActive", &b2Body::IsActive)
        .def("SetFixedRotation", &b2Body::SetFixedRotation, py::arg("flag"))
        .def("IsFixedRotation", &b2Body::IsFixedRotation)
        .def("HasFixtureList",[]( b2Body & body){return body.GetFixtureList()!= nullptr;})
        .def("_GetFixtureList",[]( b2Body & body){return body.GetFixtureList();}, py::return_value_policy::reference_internal)
        .def("_GetFixtureList",[](const b2Body & body){return body.GetFixtureList();}, py::return_value_policy::reference_internal)
        .def("HasJointList",[]( b2Body & body){return body.GetJointList()!= nullptr;})
        .def("_GetJointList",[]( b2Body & body){return body.GetJointList();}, py::return_value_policy::reference_internal)
        .def("_GetJointList",[](const b2Body & body){return body.GetJointList();}, py::return_value_policy::reference_internal)
        .def("HasContactList",[]( b2Body & body){return body.GetContactList()!= nullptr;})
        .def("_GetContactList",[]( b2Body & body){return body.GetContactList();}, py::return_value_policy::reference_internal)
        .def("_GetContactList",[](const b2Body & body){return body.GetContactList();}, py::return_value_policy::reference_internal)
        .def("HasNext", [](b2Body &b){ return b.GetNext()!=nullptr;})
        .def("_GetNext", [](b2Body &b){return b.GetNext();}, py::return_value_policy::reference_internal)        
        .def("GetWorld",[]( b2Body & body){return body.GetWorld();}, py::return_value_policy::reference_internal)
        .def("GetWorld",[](const b2Body & body){return body.GetWorld();}, py::return_value_policy::reference_internal)


        .def("HasUserData",[](const b2Body & b){return b.GetUserData()!=nullptr;})
        .def("_SetUserData",[](b2Body & b, const py::object & ud){
            auto ptr = new py::object(ud);
            b.SetUserData(ptr);
        })
        .def("_GetUserData",[](const b2Body & b){
            auto vuserData = b.GetUserData();
            auto ud = static_cast<py::object *>(vuserData);
            auto ret = py::object(*ud);
            return ret;
        })
        .def("_DeleteUserData",[](b2Body & b){
            auto vuserData = b.GetUserData();
            auto ud = static_cast<py::object *>(vuserData);
            delete ud;
            b.SetUserData(nullptr);
        })

        // in order
        
    ;

}
