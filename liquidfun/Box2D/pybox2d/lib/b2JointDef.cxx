#include <pybind11/pybind11.h>

#include <Box2D/Box2D.h>

namespace py = pybind11;


void exportb2JointDef(py::module & pybox2dModule){

    auto jdClass = py::class_<b2JointDef>(pybox2dModule, "b2JointDef");
    jdClass
        .def(py::init<>())
        .def_readwrite("jtype", &b2JointDef::type)
        .def_readwrite("collideConnected", &b2JointDef::collideConnected)
        .def_readwrite("bodyA", &b2JointDef::bodyA)
        .def_readwrite("bodyB", &b2JointDef::bodyB)
        .def("_hasUserData",[](const b2JointDef & b){return b.userData!=nullptr;})
        .def("_setUserData",[](b2JointDef & b, const py::object & ud){
            auto ptr = new py::object(ud);
            b.userData = ptr;
        })
        .def("_getUserData",[](const b2JointDef & b){
            auto vuserData = b.userData;
            auto ud = static_cast<py::object *>(vuserData);
            auto ret = py::object(*ud);
            return ret;
        })
        .def("_deleteUserData",[](b2JointDef & b){
            auto vuserData = b.userData;
            auto ud = static_cast<py::object *>(vuserData);
            delete ud;
            b.userData = nullptr;
        })
    ;
   

    py::class_<b2DistanceJointDef>(pybox2dModule,"b2DistanceJointDef",jdClass)
        .def(py::init<>())
        .def_readwrite("localAnchorA",&b2DistanceJointDef::localAnchorA)
        .def_readwrite("localAnchorB",&b2DistanceJointDef::localAnchorB)
        .def_readwrite("length", &b2DistanceJointDef::length)
        .def_readwrite("frequencyHz", &b2DistanceJointDef::frequencyHz)
        .def_readwrite("dampingRatio", &b2DistanceJointDef::dampingRatio)
    ;
    
    py::class_<b2FrictionJointDef>(pybox2dModule,"b2FrictionJointDef",jdClass)
        .def(py::init<>())
        .def_readwrite("localAnchorA",&b2FrictionJointDef::localAnchorA)
        .def_readwrite("localAnchorB",&b2FrictionJointDef::localAnchorB)
        .def_readwrite("maxForce", &b2FrictionJointDef::maxForce)
        .def_readwrite("maxTorque", &b2FrictionJointDef::maxTorque)
    ;

    py::class_<b2GearJointDef>(pybox2dModule,"b2GearJointDef",jdClass)
        .def(py::init<>())
        .def_readwrite("joint1",&b2GearJointDef::joint1)
        .def_readwrite("joint2",&b2GearJointDef::joint2)
        .def_readwrite("ratio", &b2GearJointDef::ratio)
    ;


    py::class_<b2PrismaticJointDef>(pybox2dModule,"b2PrismaticJointDef",jdClass)
        .def(py::init<>())
        .def_readwrite("localAnchorA",&b2PrismaticJointDef::localAnchorA)
        .def_readwrite("localAnchorB",&b2PrismaticJointDef::localAnchorB)
        .def_readwrite("localAxisA", &b2PrismaticJointDef::localAxisA)
        .def_readwrite("referenceAngle", &b2PrismaticJointDef::referenceAngle)
        .def_readwrite("enableLimit", &b2PrismaticJointDef::enableLimit)
        .def_readwrite("lowerTranslation", &b2PrismaticJointDef::lowerTranslation)
        .def_readwrite("upperTranslation", &b2PrismaticJointDef::upperTranslation)
        .def_readwrite("enableMotor", &b2PrismaticJointDef::enableMotor)
        .def_readwrite("maxMotorForce", &b2PrismaticJointDef::maxMotorForce)
        .def_readwrite("motorSpeed", &b2PrismaticJointDef::motorSpeed)
    ;


    py::class_<b2PulleyJointDef>(pybox2dModule,"b2PulleyJointDef",jdClass)
        .def(py::init<>())
        .def_readwrite("localAnchorA",&b2PulleyJointDef::localAnchorA)
        .def_readwrite("localAnchorB",&b2PulleyJointDef::localAnchorB)
        .def_readwrite("groundAnchorA", &b2PulleyJointDef::groundAnchorA)
        .def_readwrite("groundAnchorB", &b2PulleyJointDef::groundAnchorB)
        .def_readwrite("lengthA", &b2PulleyJointDef::lengthA)
        .def_readwrite("lengthB", &b2PulleyJointDef::lengthB)
        .def_readwrite("ratio", &b2PulleyJointDef::ratio)
        .def_readwrite("collideConnected", &b2PulleyJointDef::collideConnected)
    ;


    py::class_<b2RevoluteJointDef>(pybox2dModule,"b2RevoluteJointDef",jdClass)
        .def(py::init<>())
        .def_readwrite("localAnchorA",&b2RevoluteJointDef::localAnchorA)
        .def_readwrite("localAnchorB",&b2RevoluteJointDef::localAnchorB)
        .def_readwrite("referenceAngle", &b2RevoluteJointDef::referenceAngle)
        .def_readwrite("lowerAngle", &b2RevoluteJointDef::lowerAngle)
        .def_readwrite("upperAngle", &b2RevoluteJointDef::upperAngle)
        .def_readwrite("maxMotorTorque", &b2RevoluteJointDef::maxMotorTorque)
        .def_readwrite("motorSpeed", &b2RevoluteJointDef::motorSpeed)
        .def_readwrite("enableLimit", &b2RevoluteJointDef::enableLimit)
        .def_readwrite("enableMotor", &b2RevoluteJointDef::enableMotor)
        .def_readwrite("collideConnected", &b2RevoluteJointDef::collideConnected)
    ;


    py::class_<b2RopeJointDef>(pybox2dModule,"b2RopeJointDef",jdClass)
        .def(py::init<>())
        .def_readwrite("localAnchorA",&b2RopeJointDef::localAnchorA)
        .def_readwrite("localAnchorB",&b2RopeJointDef::localAnchorB)
        .def_readwrite("maxLength", &b2RopeJointDef::maxLength)
    ;


    py::class_<b2WeldJointDef>(pybox2dModule,"b2WeldJointDef",jdClass)
        .def(py::init<>())
        .def_readwrite("localAnchorA",&b2WeldJointDef::localAnchorA)
        .def_readwrite("localAnchorB",&b2WeldJointDef::localAnchorB)
        .def_readwrite("referenceAngle", &b2WeldJointDef::referenceAngle)
        .def_readwrite("frequencyHz", &b2WeldJointDef::frequencyHz)
        .def_readwrite("dampingRatio", &b2WeldJointDef::dampingRatio)
    ;


    py::class_<b2WheelJointDef>(pybox2dModule,"b2WheelJointDef",jdClass)
        .def(py::init<>())
        .def_readwrite("localAnchorA",&b2WheelJointDef::localAnchorA)
        .def_readwrite("localAnchorB",&b2WheelJointDef::localAnchorB)
        .def_readwrite("localAxisA", &b2WheelJointDef::localAxisA)
        .def_readwrite("enableMotor", &b2WheelJointDef::enableMotor)
        .def_readwrite("maxMotorTorque", &b2WheelJointDef::maxMotorTorque)
        .def_readwrite("motorSpeed", &b2WheelJointDef::motorSpeed)
        .def_readwrite("frequencyHz", &b2WheelJointDef::frequencyHz)
        .def_readwrite("dampingRatio", &b2WheelJointDef::dampingRatio)
    ;

    py::class_<b2MouseJointDef>(pybox2dModule,"b2MouseJointDef",jdClass)
        .def(py::init<>())
        .def_readwrite("target", &b2MouseJointDef::target)
        .def_readwrite("maxForce", &b2MouseJointDef::maxForce)
        .def_readwrite("frequencyHz", &b2MouseJointDef::frequencyHz)
        .def_readwrite("dampingRatio", &b2MouseJointDef::dampingRatio)
    ;

}

