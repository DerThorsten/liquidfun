from pybox2d import *
from tools import GenericB2dIter

from extend_fixture import fixtureDef
from extend_math import vec2
from extend_joints import *


def extendWorld():
    
    def _CreateBody(self,btype=None, bodyDef=None,position=None,angle=None, shape=None,fixtures=None, density = 1.0):
        if position is not None  and not isinstance(position,b2Vec2):
            position  = b2Vec2(position[0],position[1])

        if bodyDef is None:
            bodyDef = b2BodyDef()
        if btype  is not None:
            bodyDef.type = btype

        if position is not None:
            bodyDef.position = vec2(position)
        if angle is not None:
            bodyDef.angle = angle

        body =  self._CreateBodyCpp(bodyDef)

        if shape is not None:
            body.CreateFixture(shape, density)
        if fixtures is not None:
            body.CreateFixture(fixtures)

        return body
    b2World._CreateBody = _CreateBody

    def CreateStaticBody(self,bodyDef=None, position=None,angle=None, shape=None, density = 1.0):
        return self._CreateBody(btype= b2BodyType.b2_staticBody,bodyDef=bodyDef,position=position,
                                angle=angle, shape=shape,fixtures=fixtures, density=density)
    b2World.CreateStaticBody = CreateStaticBody

    def CreateDynamicBody(self,bodyDef=None, position=None,angle=None, shape=None,fixtures=None, density = 1.0):
        return self._CreateBody(btype= b2BodyType.b2_dynamicBody,bodyDef=bodyDef,position=position,
                                angle=angle, shape=shape,fixtures=fixtures, density=density)
    b2World.CreateDynamicBody = CreateDynamicBody

    def CreateBody(self,bodyDef=None,btype=None,position=None,shapes=None):
    
        if btype is None:
            btype = b2BodyType.b2_staticBody

        if bodyDef is None:
            bodyDef = b2BodyDef()
        if btype is not None:
            bodyDef.type = btype
        if position is not None:
            bodyDef.position = position

        body = self._CreateBodyCpp(bodyDef)
        if shapes is not None:
            if isinstance(shapes, b2Shape):
                fd = fixtureDef(shape=shapes)
                body.CreateFixture(fd)
            else:
                for s in shapes:
                    assert False

        return body
    b2World.CreateBody = CreateBody

    def GetBodyList(self):
        blist = None
        if self.GetBodyCount > 0:
            blist = self._GetBodyList()
        return GenericB2dIter(blist)
    b2World.GetBodyList = GetBodyList

    def GetJointList(self):
        blist = None
        if self.GetBodyCount > 0:
            blist = self._GetJointList()
        return GenericB2dIter(blist)
    b2World.GetJointList = GetJointList


    def CreateMouseJoint(self,bodyA,bodyB,collideConnected=False,target=vec2(0,0),
                     maxForce=0.0, frequencyHz=5.0,dampingRatio=0.7):

        d = mouseJointDef(bodyA=bodyA,bodyB=bodyB,collideConnected=collideConnected,target=target,
                     maxForce=maxForce, frequencyHz=frequencyHz,dampingRatio=dampingRatio)
        return self.CreateJoint(d)
    b2World.CreateMouseJoint = CreateMouseJoint

extendWorld()
del extendWorld
