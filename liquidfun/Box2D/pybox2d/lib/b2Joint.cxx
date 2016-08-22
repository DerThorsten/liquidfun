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
        return b2Vec2();
    }

    /// Get the anchor point on bodyB in world coordinates.
    virtual b2Vec2 GetAnchorB() const {
        PYBIND11_OVERLOAD_PURE(
            b2Vec2,       // Return type 
            b2Joint,      // Parent class 
            GetAnchorB    // Name of function 
        );
        return b2Vec2();
    }

    /// Get the reaction force on bodyB at the joint anchor in Newtons.
    virtual b2Vec2 GetReactionForce(float32 inv_dt) const {
        PYBIND11_OVERLOAD_PURE(
            b2Vec2,       // Return type 
            b2Joint,      // Parent class 
            GetReactionForce,    // Name of function 
            inv_dt
        )
        return b2Vec2();
    }

    /// Get the reaction torque on bodyB in N*m.
    virtual float32 GetReactionTorque(float32 inv_dt) const {
        PYBIND11_OVERLOAD_PURE(
            float32,       // Return type 
            b2Joint,      // Parent class 
            GetReactionTorque,    // Name of function 
            inv_dt
        );
        return float32();
    }



    // They are protected
    virtual void InitVelocityConstraints(const b2SolverData& data){
        PYBIND11_OVERLOAD_PURE(
            void,       // Return type 
            b2Joint,      // Parent class 
            InitVelocityConstraints,    // Name of function 
            data
        );
    }
    virtual void SolveVelocityConstraints(const b2SolverData& data){
        PYBIND11_OVERLOAD_PURE(
            void,       // Return type 
            b2Joint,      // Parent class 
            SolveVelocityConstraints,    // Name of function 
            data
        );
    }
    virtual bool SolvePositionConstraints(const b2SolverData& data){
        PYBIND11_OVERLOAD_PURE(
            bool,       // Return type 
            b2Joint,      // Parent class 
            SolvePositionConstraints,    // Name of function 
            data
        );
        return false;
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

    auto jointCls = py::class_<b2Joint, std::unique_ptr<b2Joint>, PyB2Joint>(pybox2dModule,"b2Joint");
    
    jointCls
        //.alias<b2Joint>()
        .def(py::init<const b2JointDef* >())
        //
        .def_property_readonly("type",&b2Joint::GetType) 
        .def_property_readonly("bodyA",&b2Joint::GetBodyA)
        .def_property_readonly("bodyB",&b2Joint::GetBodyB)  
        .def_property_readonly("anchorA",&b2Joint::GetAnchorA)
        .def_property_readonly("anchorB",&b2Joint::GetAnchorB)     
        .def("getReactionForce",&b2Joint::GetReactionForce, py::arg("iv_dt"))
        .def("getReactionTorque",&b2Joint::GetReactionTorque, py::arg("iv_dt"))
        .def("_hasNext", [](b2Joint * j){ return j->GetNext()!=nullptr;})
        .def("_getNext", [](b2Joint * j){return j->GetNext();}, py::return_value_policy::reference_internal)


        .def("_hasUserData",[](const b2Joint * j){return j->GetUserData()!=nullptr;})
        .def("_setUserData",[](b2Joint * j, const py::object & ud){
            auto ptr = new py::object(ud);
            j->SetUserData(ptr);
        })
        .def("_getUserData",[](const b2Joint * j){
            auto vuserData = j->GetUserData();
            auto ud = static_cast<py::object *>(vuserData);
            auto ret = py::object(*ud);
            return ret;
        })
        .def("_deleteUserData",[](b2Joint * j){
            auto vuserData = j->GetUserData();
            auto ud = static_cast<py::object *>(vuserData);
            delete ud;
            j->SetUserData(nullptr);
        })

            // .def_dynamic_cast<b2Joint,b2DistanceJoint>("asDistanceJoint")
            // .def_dynamic_cast<b2Joint,b2FrictionJoint>("asFrictionJoint")
            // .def_dynamic_cast<b2Joint,b2GearJoint>("asGearJoint")
            // .def_dynamic_cast<b2Joint,b2PrismaticJoint>("asPrismaticJoint")
            // .def_dynamic_cast<b2Joint,b2PulleyJoint>("asPulleyJoint")
            // .def_dynamic_cast<b2Joint,b2RevoluteJoint>("asRevoluteJoint")
            // .def_dynamic_cast<b2Joint,b2RopeJoint>("asRopeJoint")
            // .def_dynamic_cast<b2Joint,b2WeldJoint>("asWeldJoint")
            // .def_dynamic_cast<b2Joint,b2WheelJoint>("asWheelJoint")
            // .def_dynamic_cast<b2Joint,b2MouseJoint>("asMouseJoint")

    ;
   
   
    py::class_<b2DistanceJoint>(pybox2dModule,"b2DistanceJoint",jointCls)
        .def_property("length",&b2DistanceJoint::GetLength, &b2DistanceJoint::SetLength)
        .def_property("frequency",&b2DistanceJoint::GetFrequency, &b2DistanceJoint::SetFrequency)
        .def_property("dampingRatio",&b2DistanceJoint::GetDampingRatio, &b2DistanceJoint::SetDampingRatio)
    ;  
    py::class_<b2FrictionJoint, std::unique_ptr<b2FrictionJoint>, PyB2Joint >(pybox2dModule,"b2FrictionJoint",jointCls)
    ;
    py::class_<b2GearJoint, std::unique_ptr<b2GearJoint>, PyB2Joint >(pybox2dModule,"b2GearJoint",jointCls)
    ;
    py::class_<b2PrismaticJoint, std::unique_ptr<b2PrismaticJoint>, PyB2Joint >(pybox2dModule,"b2PrismaticJoint",jointCls)
    ;
    py::class_<b2PulleyJoint, std::unique_ptr<b2PulleyJoint>, PyB2Joint >(pybox2dModule,"b2PulleyJoint",jointCls)
    ;
    py::class_<b2RevoluteJoint, std::unique_ptr<b2RevoluteJoint>, PyB2Joint >(pybox2dModule,"b2RevoluteJoint",jointCls)
    ;
    py::class_<b2RopeJoint, std::unique_ptr<b2RopeJoint>, PyB2Joint >(pybox2dModule,"b2RopeJoint",jointCls)
    ;
    py::class_<b2WeldJoint, std::unique_ptr<b2WeldJoint>, PyB2Joint >(pybox2dModule,"b2WeldJoint",jointCls)
    ;
    py::class_<b2WheelJoint, std::unique_ptr<b2WheelJoint>, PyB2Joint >(pybox2dModule,"b2WheelJoint",jointCls)
    ;
    py::class_<b2MouseJoint, std::unique_ptr<b2MouseJoint>, PyB2Joint >(pybox2dModule,"b2MouseJoint",jointCls)
        .def("SetTarget",&b2MouseJoint::SetTarget)
    ;
   

}

