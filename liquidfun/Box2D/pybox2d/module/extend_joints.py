from ._pybox2d import *
from .extend_math import vec2
from .tools import _classExtender, GenericB2dIter
from . extend_user_data import add_user_data_api
from . _make_local_anchor_ab import _make_local_anchor_ab
from enum import Enum

JointType = b2JointType

add_user_data_api(JointDef)
add_user_data_api(Joint)


def joint_def(jtype,body_a,body_b,collide_connected=False):
    jd = JointDef()
    jd.jtype = jtype
    jd.body_a = body_a
    jd.body_b = body_b
    jd.collide_connected = collide_connected 
    return jd

def distance_joint_def(body_a,body_b,
                    local_anchor_a = None,
                    local_anchor_b = None,
                    local_anchor= None,
                    anchor_a = None,
                    anchor_b = None,
                    anchor= None,
                    collide_connected=False,
                    length=None, 
                    frequency_hz=0.0,
                    damping_ratio=0.0,
                    user_data=None,
                    int_user_data=None,
                    joint_def=None):
    if joint_def is None:
        jd = DistanceJointDef()
    else:
        jd = joint_def
    jd.jtype = b2JointType.distance_joint
    jd.body_a = body_a
    jd.body_b = body_b
    local_anchor_a, local_anchor_b = _make_local_anchor_ab(body_a, body_b, 
            local_anchor_a, local_anchor_b, local_anchor,
            anchor_a, anchor_b, anchor)
    jd.local_anchor_a = local_anchor_a
    jd.local_anchor_b = local_anchor_b
    jd.collide_connected = collide_connected 
    if length is None:
        anchor_a = body_a.get_world_point(local_anchor_a)
        anchor_b = body_b.get_world_point(local_anchor_b)
        length = (anchor_a - anchor_b).length
    jd.length = length
    jd.frequency_hz = frequency_hz
    jd.damping_ratio = damping_ratio
    if user_data is not None:
        jd.user_data = user_data
    if int_user_data is not None:
        jd.int_user_data = int(int_user_data)
    return jd

def wheel_joint_def(body_a,body_b,
                    local_anchor_a = None,
                    local_anchor_b = None,
                    local_anchor= None,
                    anchor_a = None,
                    anchor_b = None,
                    anchor = None,
                    local_axis_a = None,
                    enable_motor = None,
                    max_motor_torque = None,
                    motor_speed=None,
                    frequency_hz=None,
                    damping_ratio=None,
                    user_data=None,
                    int_user_data=None,
                    joint_def=None):
    if joint_def is None:
        jd = WheelJointDef()
    else:
        jd = joint_def
    jd.jtype = b2JointType.wheel_joint
    jd.body_a = body_a
    jd.body_b = body_b
    local_anchor_a, local_anchor_b = _make_local_anchor_ab(body_a, body_b, 
            local_anchor_a, local_anchor_b, local_anchor,
            anchor_a, anchor_b, anchor)
    jd.local_anchor_a = local_anchor_a
    jd.local_anchor_b = local_anchor_b
 
    if local_axis_a is not None:
        jd.local_axis_a = vec2(local_axis_a)
    if enable_motor is not None:
        jd.enable_motor = enable_motor
    if max_motor_torque is not None:
        jd.max_motor_torque = max_motor_torque
    if motor_speed is not None:
        jd.motor_speed = motor_speed
    if frequency_hz is not None:
        jd.frequency_hz = frequency_hz
    if damping_ratio is not None:
        jd.damping_ratio = damping_ratio
    if joint_def is not None:
        jd.joint_def = joint_def


    if user_data is not None:
        jd.user_data = user_data
    if int_user_data is not None:
        jd.int_user_data = int(int_user_data)
    return jd


def mouse_joint_def(body_a,body_b,collide_connected=False,target=vec2(0,0),
                    max_force=0.0, frequency_hz=5.0,damping_ratio=0.7):
    jd = MouseJointDef()
    jd.jtype = b2JointType.mouse_joint
    jd.body_a = body_a
    jd.body_b = body_b
    jd.collide_connected = collide_connected 
    jd.target = target
    jd.max_force = max_force
    jd.frequency_hz = frequency_hz
    jd.damping_ratio = damping_ratio
    return jd

def rope_joint_def(body_a,body_b,
                 local_anchor_a = (0,0),
                 local_anchor_b = (0,0),
                 maxLength = 0.0,
                 collide_connected=False
):
    jd = RopeJointDef()
    #jd.jtype = b2JointType.mouseJoint
    jd.body_a = body_a
    jd.body_b = body_b
    jd.collide_connected = collide_connected 
    jd.local_anchor_a = vec2(local_anchor_a)
    jd.local_anchor_b = vec2(local_anchor_b)
    jd.maxLength = maxLength
    return jd

def revolute_joint_def(body_a,body_b,
                    local_anchor_a = None,
                    local_anchor_b = None,
                    local_anchor= None,
                    anchor_a = None,
                    anchor_b = None,
                    anchor= None,
                    reference_angle = 0.0,
                    lower_angle = 0.0,
                    upper_angle = 0.0,
                    max_motor_torque = 0.0,
                    motor_speed = 0.0,
                    enable_limit = False,
                    enable_motor = False,
                    collide_connected=False
):
    jd = RevoluteJointDef()
    #jd.jtype = b2JointType.mouseJoint
    jd.body_a = body_a
    jd.body_b = body_b
    jd.collide_connected = collide_connected 
    local_anchor_a, local_anchor_b = _make_local_anchor_ab(body_a, body_b, 
            local_anchor_a, local_anchor_b, local_anchor,
            anchor_a, anchor_b, anchor)
    jd.local_anchor_a = local_anchor_a
    jd.local_anchor_b = local_anchor_b
    jd.reference_angle = reference_angle
    jd.lower_angle = lower_angle
    jd.max_motor_torque = max_motor_torque
    jd.upper_angle = upper_angle
    jd.motor_speed = motor_speed
    jd.enable_limit = enable_limit
    jd.enable_motor = enable_motor
    return jd

def prismatic_joint_def(body_a,body_b,
                    local_anchor_a = (0,0),
                    local_anchor_b = (0,0),
                    local_axis_a = (1,0),
                    reference_angle = 0.0,
                    enable_limit = False,
                    lower_translation = 0.0,
                    upper_translation = 0.0,
                    enable_motor = False,
                    max_motor_force = 0.0,
                    motor_speed = 0.0,
                    collide_connected=False
):
    jd = PrismaticJointDef()
    #jd.jtype = b2JointType.mouseJoint
    jd.body_a = body_a
    jd.body_b = body_b
    jd.collide_connected = collide_connected 

    # 
    jd.local_anchor_a = vec2(local_anchor_a)
    jd.local_anchor_b = vec2(local_anchor_b)
    jd.local_axis_a = vec2(local_axis_a)
    jd.reference_angle = reference_angle
    jd.enable_limit = enable_limit
    jd.lower_translation = lower_translation
    jd.upper_translation = upper_translation
    jd.enable_motor = enable_motor
    jd.max_motor_force = max_motor_force
    jd.motor_speed = motor_speed
    return jd



# class _JointDef(b2JointDef):

#     @property
#     def user_data(self):
#         if self._has_user_data():
#             return self._get_user_data()
#         else:
#             return None
#     @user_data.setter
#     def user_data(self, ud):
#         if self._has_user_data():
#             return self._delete_user_data()
#         self._set_user_data(ud)

# _classExtender(_JointDef,['user_data'])




class _Joint(Joint):
    @property
    def next(self):
        if self._has_next():
            return self._get_next()
        else:
            return None

    # @property
    # def user_data(self):
    #     if self._has_user_data():
    #         return self._get_user_data()
    #     else:
    #         return None
    # @user_data.setter
    # def user_data(self, ud):
    #     if self._has_user_data():
    #         return self._delete_user_data()
    #     self._set_user_data(ud)


    # # this is most probably deprecated
    # def as_most_derived(self):
    #     jtype = self.type
    #     if jtype == b2JointType.revoluteJoint:
    #         return self.asRevoluteJoint()
    #     elif jtype == b2JointType.prismaticJoint:
    #         return self.asPrismaticJoint()
    #     elif jtype == b2JointType.distanceJoint:
    #         return self.asPrismaticJoint()
    #     elif jtype == b2JointType.pulleyJoint:
    #         return self.asPulleyJoint()
    #     elif jtype == b2JointType.mouseJoint:
    #         return self.asMouseJoint()
    #     elif jtype == b2JointType.gearJoint:
    #         return self.asGearJoint()
    #     elif jtype == b2JointType.wheelJoint:
    #         return self.asWheelJoint()
    #     elif jtype == b2JointType.weldJoint:
    #         return self.asPrismaticJoint()
    #     elif jtype == b2JointType.frictionJoint:
    #         return self.asFrictionJoint()
    #     elif jtype == b2JointType.ropeJoint:
    #         return self.asRopeJoint()
    #     elif jtype == b2JointType.motorJoint:
    #         return self.asMouseJoint()
    #     else:
    #         raise RuntimeError("unkown joint type")
     


_classExtender(_Joint,['next'])


