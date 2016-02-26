

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










class QueryCallback(b2QueryCallbackCaller):

    def __init__(self):
        super(QueryCallback,self).__init__(self)

    def ReportFixture(self, fixture):
        raise NotImplementedError 
    def ReportParticle(self, particleSystem, index):
        return False
    def ShouldQueryParticleSystem(self, particleSystem):
        return False
