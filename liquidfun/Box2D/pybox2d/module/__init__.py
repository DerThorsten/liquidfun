

from pybox2d import *

from tools import GenericB2dIter
from extend_math import *
from extend_draw import *
from extend_world import *
from extend_body import *
from extend_fixture import *
from extend_shapes import *
from extend_joints import *
from extend_particles import *
from extend_collision import *
from extend_contact import *





class RayCastCallback(b2RayCastCallbackCaller):

    def __init__(self):
        super(RayCastCallback,self).__init__(self)

    def ReportFixture(self, fixture, point1, point2):
        raise NotImplementedError 
    #def ReportParticle(self, particleSystem, index):
    #    return False
    #def ShouldQueryParticleSystem(self, particleSystem):
    #    return False



class DestructionListener(b2DestructionListenerCaller):

    def __init__(self):
        super(DestructionListener,self).__init__(self)

    def sayGoodbyeJoint(self, joint):
        pass
    def sayGoodbyeFixture(self, fixture):
        pass
    def sayGoodbyeParticleGroup(self, particleGroup):
        pass
    def sayGoodbyeParticleSystem(self, particleSystem,index):
        pass



class ContactListener(b2ContactListenerCaller):

    def __init__(self):
        super(ContactListener,self).__init__(self)

    def beginContact(self, contact):
        pass

    def endContact(self, contact):
        pass

    def beginContactParticleBody(self, particleSystem, particleBodyContact):
        pass

    def beginContactParticle(self, particleSystem, indexA, indexB):
        pass

    def endContactParticle(self, particleSystem, indexA, indexB):
        pass

    def preSolve(self, contact, oldManifold):
        pass

    def preSolve(self, contact, impulse):
        pass

class QueryCallback(b2QueryCallbackCaller):

    def __init__(self):
        super(QueryCallback,self).__init__(self)

    def ReportFixture(self, fixture):
        raise NotImplementedError 
    def ReportParticle(self, particleSystem, index):
        return False
    def ShouldQueryParticleSystem(self, particleSystem):
        return False


class DebugDraw(b2DrawCaller):
    def __init__(self):
        super(DebugDraw,self).__init__(self)

    def DrawSolidCircle(self, center, radius, axis, c):
        raise NotImplementedError 

    def DrawCircle(self, center, radius, c):
        raise NotImplementedError 

    def DrawSegment(self,v1, v2, c):
        raise NotImplementedError 

    def DrawPolygon(self,vertices, c):
        raise NotImplementedError 

    def DrawSolidPolygon(self,vertices, c):
        raise NotImplementedError 

    def DrawParticles(self, centers, radius,  c=None):
        raise NotImplementedError 

