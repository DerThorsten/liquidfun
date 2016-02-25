#include <pybind11/pybind11.h>

#include <Box2D/Box2D.h>

namespace py = pybind11;



class PyB2Joint : public b2Joint {
public:

    using b2Joint::b2Joint;

    virtual ~PyB2Joint() {}




    /// Get the anchor point on bodyA in world coordinates.
    virtual b2Vec2 GetAnchorA() const {
        PYBIND11_OVERLOAD_PURE(
            b2Vec2,       // Return type 
            b2Joint,      // Parent class 
            GetAnchorA    // Name of function 
        );
    }

    /// Get the anchor point on bodyB in world coordinates.
    virtual b2Vec2 GetAnchorB() const {
        PYBIND11_OVERLOAD_PURE(
            b2Vec2,       // Return type 
            b2Joint,      // Parent class 
            GetAnchorB    // Name of function 
        );
    }

    /// Get the reaction force on bodyB at the joint anchor in Newtons.
    virtual b2Vec2 GetReactionForce(float32 inv_dt) const {
        PYBIND11_OVERLOAD_PURE(
            b2Vec2,       // Return type 
            b2Joint,      // Parent class 
            GetReactionForce,    // Name of function 
            inv_dt
        );
    }

    /// Get the reaction torque on bodyB in N*m.
    virtual float32 GetReactionTorque(float32 inv_dt) const {
        PYBIND11_OVERLOAD_PURE(
            float32,       // Return type 
            b2Joint,      // Parent class 
            GetReactionTorque,    // Name of function 
            inv_dt
        );
    }



    // They are protected
    virtual void InitVelocityConstraints(const b2SolverData& data){

    }
    virtual void SolveVelocityConstraints(const b2SolverData& data){

    }
    virtual bool SolvePositionConstraints(const b2SolverData& data){

    }


};


template<class DT>
bool isType(const b2Joint * shape){
    return bool(dynamic_cast<const DT *>(shape));
}

template<class DT>
DT * asType(b2Joint * shape){
    auto res =  dynamic_cast<DT *>(shape);
    if(res == nullptr){
        throw std::runtime_error("invalid b2Joint dynamic cast");
    }
    return res;
}

class PyB2JointDef : public b2JointDef{
public:
    using b2JointDef::b2JointDef;
};

void exportb2Joint(py::module & pybox2dModule){


    py::enum_<b2JointType>(pybox2dModule, "b2JointType")
        .value("e_unknownJoint", b2JointType::e_unknownJoint)
        .value("e_revoluteJoint", b2JointType::e_revoluteJoint)
        .value("e_prismaticJoint", b2JointType::e_prismaticJoint)
        .value("e_distanceJoint", b2JointType::e_distanceJoint)
        .value("e_pulleyJoint", b2JointType::e_pulleyJoint)
        .value("e_mouseJoint", b2JointType::e_mouseJoint)
        .value("e_gearJoint", b2JointType::e_gearJoint)
        .value("e_wheelJoint", b2JointType::e_wheelJoint)
        .value("e_weldJoint", b2JointType::e_weldJoint)
        .value("e_frictionJoint", b2JointType::e_frictionJoint)
        .value("e_ropeJoint", b2JointType::e_ropeJoint)
        .value("e_motorJoint", b2JointType::e_motorJoint)
    ;

    py::enum_<b2LimitState>(pybox2dModule, "b2LimitState")
        .value("e_inactiveLimit", b2LimitState::e_inactiveLimit)
        .value("e_atLowerLimit", b2LimitState::e_atLowerLimit)
        .value("e_atUpperLimit", b2LimitState::e_atUpperLimit)
        .value("e_equalLimits", b2LimitState::e_equalLimits)
    ;



    py::class_<b2JointEdge>(pybox2dModule, "b2JointEdge")
        // A lot to do
    ;

    auto jdClass = py::class_<b2JointDef>(pybox2dModule, "b2JointDef");
    jdClass
        .def(py::init<>())
        .def_readwrite("jtype", &b2JointDef::type)
        .def_readwrite("collideConnected", &b2JointDef::collideConnected)
        .def_readwrite("bodyA", &b2JointDef::bodyA)
        .def_readwrite("bodyB", &b2JointDef::bodyB)
        // user data is still missing
    ;


    auto jointCls = py::class_<PyB2Joint>(pybox2dModule,"b2Joint");
    
    jointCls
        .alias<b2Joint>()
        .def(py::init<const b2JointDef* >())
        //
        .def("GetAnchorA",&b2Joint::GetAnchorA)
        .def("GetAnchorB",&b2Joint::GetAnchorB)
        .def("GetReactionForce",&b2Joint::GetReactionForce, py::arg("iv_dt"))
        .def("GetReactionTorque",&b2Joint::GetReactionTorque, py::arg("iv_dt"))
        .def("HasNext", [](b2Joint * j){ return j->GetNext()!=nullptr;})
        .def("_GetNext", [](b2Joint * j){return j->GetNext();}, py::return_value_policy::reference_internal)        
    ;
   
   
    py::class_<b2DistanceJoint>(pybox2dModule,"b2DistanceJoint",jointCls)
       // .def(py::init<const b2JointDef* >())
    ;
    py::class_<b2DistanceJointDef>(pybox2dModule,"b2DistanceJointDef",jdClass)
        .def(py::init<>())
        .def_readwrite("localAnchorA",&b2DistanceJointDef::localAnchorA)
        .def_readwrite("localAnchorB",&b2DistanceJointDef::localAnchorB)
        .def_readwrite("length", &b2DistanceJointDef::length)
        .def_readwrite("frequencyHz", &b2DistanceJointDef::frequencyHz)
        .def_readwrite("dampingRatio", &b2DistanceJointDef::dampingRatio)
    ;
    
    py::class_<b2FrictionJoint>(pybox2dModule,"b2FrictionJoint",jointCls)
       // .def(py::init<const b2JointDef* >())
    ;
    py::class_<b2FrictionJointDef>(pybox2dModule,"b2FrictionJointDef",jdClass)
        .def(py::init<>())
    ;

    py::class_<b2GearJoint>(pybox2dModule,"b2GearJoint",jointCls)
       // .def(py::init<const b2JointDef* >())
    ;
    py::class_<b2GearJointDef>(pybox2dModule,"b2GearJointDef",jdClass)
        .def(py::init<>())
    ;

    py::class_<b2PrismaticJoint>(pybox2dModule,"b2PrismaticJoint",jointCls)
       // .def(py::init<const b2JointDef* >())
    ;
    py::class_<b2PrismaticJointDef>(pybox2dModule,"b2PrismaticJointDef",jdClass)
        .def(py::init<>())
    ;

    py::class_<b2PulleyJoint>(pybox2dModule,"b2PulleyJoint",jointCls)
       // .def(py::init<const b2JointDef* >())
    ;
    py::class_<b2PulleyJointDef>(pybox2dModule,"b2PulleyJointDef",jdClass)
        .def(py::init<>())
    ;

    py::class_<b2RevoluteJoint>(pybox2dModule,"b2RevoluteJoint",jointCls)
       // .def(py::init<const b2JointDef* >())
    ;
    py::class_<b2RevoluteJointDef>(pybox2dModule,"b2RevoluteJointDef",jdClass)
        .def(py::init<>())
    ;

    py::class_<b2RopeJoint>(pybox2dModule,"b2RopeJoint",jointCls)
       // .def(py::init<const b2JointDef* >())
    ;
    py::class_<b2RopeJointDef>(pybox2dModule,"b2RopeJointDef",jdClass)
        .def(py::init<>())
    ;

    py::class_<b2WeldJoint>(pybox2dModule,"b2WeldJoint",jointCls)
       // .def(py::init<const b2JointDef* >())
    ;
    py::class_<b2WeldJointDef>(pybox2dModule,"b2WeldJointDef",jdClass)
        .def(py::init<>())
    ;

    py::class_<b2WheelJoint>(pybox2dModule,"b2WheelJoint",jointCls)
        .def(py::init<const b2JointDef* >())
    ;
    py::class_<b2WheelJointDef>(pybox2dModule,"b2WheelJointDef",jdClass)
        .def(py::init<>())
    ;


}

