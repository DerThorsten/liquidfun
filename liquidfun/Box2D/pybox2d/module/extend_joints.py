from pybox2d import *
from extend_math import vec2
from tools import _classExtender, GenericB2dIter








def jointDef(jtype,bodyA,bodyB,collideConnected=False):
    jd = b2JointDef()
    jd.jtype = jtype
    jd.bodyA = bodyA
    jd.bodyB = bodyB
    jd.collideConnected = collideConnected 
    return jd

def distanceJointDef(bodyA,bodyB,localAnchorA,localAnchorB,collideConnected=False,length=1.0, frequencyHz=0.0,dampingRatio=0.0,_jd=None):
    if _jd is None:
        jd = b2DistanceJointDef()
    jd.jtype = b2JointType.e_distanceJoint
    jd.bodyA = bodyA
    jd.bodyB = bodyB
    jd.localAnchorA = vec2(localAnchorA)
    jd.localAnchorB = vec2(localAnchorB)
    jd.collideConnected = collideConnected 
    jd.length = length
    jd.frequencyHz = frequencyHz
    jd.dampingRatio = dampingRatio
    return jd




class DistanceJointDef(b2DistanceJoint):
    def __init__(self,*args,**kwargs):
        distanceJointDef(*args,_jd=self,**kwargs)


def mouseJointDef(bodyA,bodyB,collideConnected=False,target=vec2(0,0),
                     maxForce=0.0, frequencyHz=5.0,dampingRatio=0.7):
    jd = b2MouseJointDef()
    jd.jtype = b2JointType.e_mouseJoint
    jd.bodyA = bodyA
    jd.bodyB = bodyB
    jd.collideConnected = collideConnected 
    jd.target = target
    jd.maxForce = maxForce
    jd.frequencyHz = frequencyHz
    jd.dampingRatio = dampingRatio
    return jd

def ropeJointDef(bodyA,bodyB,
                    localAnchorA = (0,0),
                    localAnchorB = (0,0),
                    maxLength = 0.0,
                    collideConnected=False
):
    jd = b2RopeJointDef()
    #jd.jtype = b2JointType.e_mouseJoint
    jd.bodyA = bodyA
    jd.bodyB = bodyB
    jd.collideConnected = collideConnected 
    jd.localAnchorA = vec2(localAnchorA)
    jd.localAnchorB = vec2(localAnchorB)
    jd.maxLength = maxLength
    return jd

def revoluteJointDef(bodyA,bodyB,
                    localAnchorA = (0,0),
                    localAnchorB = (0,0),
                    lowerAngle = 0.0,
                    upperAngle = 0.0,
                    maxMotorTorque = 0.0,
                    motorSpeed = 0.0,
                    enableLimit = False,
                    enableMotor = False,
                    collideConnected=False
):
    jd = b2RevoluteJointDef()
    #jd.jtype = b2JointType.e_mouseJoint
    jd.bodyA = bodyA
    jd.bodyB = bodyB
    jd.collideConnected = collideConnected 
    jd.localAnchorA = vec2(localAnchorA)
    jd.localAnchorB = vec2(localAnchorB)
    jd.maxMotorTorque = maxMotorTorque
    jd.motorSpeed = motorSpeed
    jd.enableLimit = enableLimit
    jd.enableMotor = enableMotor
    return jd

def prismaticJointDef(bodyA,bodyB,
                    localAnchorA = (0,0),
                    localAnchorB = (0,0),
                    localAxisA = (1,0),
                    referenceAngle = 0.0,
                    enableLimit = False,
                    lowerTranslation = 0.0,
                    upperTranslation = 0.0,
                    enableMotor = False,
                    maxMotorForce = 0.0,
                    motorSpeed = 0.0,
                    collideConnected=False
):
    jd = b2PrismaticJointDef()
    #jd.jtype = b2JointType.e_mouseJoint
    jd.bodyA = bodyA
    jd.bodyB = bodyB
    jd.collideConnected = collideConnected 

    # 
    jd.localAnchorA = vec2(localAnchorA)
    jd.localAnchorB = vec2(localAnchorB)
    jd.localAxisA = vec2(localAxisA)
    jd.referenceAngle = referenceAngle
    jd.enableLimit = enableLimit
    jd.lowerTranslation = lowerTranslation
    jd.upperTranslation = upperTranslation
    jd.enableMotor = enableMotor
    jd.maxMotorForce = maxMotorForce
    jd.motorSpeed = motorSpeed
    return jd



class _JointDef(b2JointDef):

    @property
    def userData(self):
        if self._hasUserData():
            return self._getUserData()
        else:
            return None
    @userData.setter
    def userData(self, ud):
        if self._hasUserData():
            return self._deleteUserData()
        self._setUserData(ud)

_classExtender(_JointDef,['userData'])




class _Joint(b2Joint):
    @property
    def next(self):
        if self._hasNext():
            return self._getNext()
        else:
            return None

    @property
    def userData(self):
        if self._hasUserData():
            return self._getUserData()
        else:
            return None
    @userData.setter
    def userData(self, ud):
        if self._hasUserData():
            return self._deleteUserData()
        self._setUserData(ud)



    def asMostDerived(self):
        jtype = self.type
        if jtype == b2JointType.e_revoluteJoint:
            return self.asRevoluteJoint()
        elif jtype == b2JointType.e_prismaticJoint:
            return self.asPrismaticJoint()
        elif jtype == b2JointType.e_distanceJoint:
            return self.asPrismaticJoint()
        elif jtype == b2JointType.e_pulleyJoint:
            return self.asPulleyJoint()
        elif jtype == b2JointType.e_mouseJoint:
            return self.asMouseJoint()
        elif jtype == b2JointType.e_gearJoint:
            return self.asGearJoint()
        elif jtype == b2JointType.e_wheelJoint:
            return self.asWheelJoint()
        elif jtype == b2JointType.e_weldJoint:
            return self.asPrismaticJoint()
        elif jtype == b2JointType.e_frictionJoint:
            return self.asFrictionJoint()
        elif jtype == b2JointType.e_ropeJoint:
            return self.asRopeJoint()
        elif jtype == b2JointType.e_motorJoint:
            return self.asMouseJoint()
        else:
            raise RuntimeError("unkown joint type")
     


_classExtender(_Joint,['next','userData','asMostDerived'])


