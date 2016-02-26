from pybox2d import *
from extend_math import vec2




def jointDef(jtype,bodyA,bodyB,collideConnected=False):
    jd = b2JointDef()
    jd.jtype = jtype
    jd.bodyA = bodyA
    jd.bodyB = bodyB
    jd.collideConnected = collideConnected 
    return jd

def distanceJointDef(bodyA,bodyB,localAnchorA,localAnchorB,collideConnected=False,length=1.0, frequencyHz=0.0,dampingRatio=0.0):
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


def extendJoint():
    def GetNext(self):
        if self.HasNext():
            return self._GetNext()
        else:
            return None
    b2Joint.GetNext = GetNext

extendJoint()
del extendJoint

