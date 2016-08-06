from pybox2d import *
from tools import _classExtender, GenericB2dIter

from extend_fixture import fixtureDef
from extend_math import vec2
from extend_joints import *

def world(gravity = (0,-9.81)):
    return b2World(vec2(gravity))

World = b2World

class _World(b2World):
    def __init__(self, gravity = (0,-9.81)):
        super(World, self).__init__(vec2(gravity))
    

    @property
    def bodyList(self):
        blist = None
        if self.bodyCount > 0:
            blist = self._getBodyList()
        return GenericB2dIter(blist)

    @property
    def jointList(self):
        blist = None
        if self.jointCount > 0:
            blist = self._getJointList()
        return GenericB2dIter(blist)

    # functions
    def _createBody(self,btype=None, bodyDef=None,position=None,angle=None, shape=None, shapes=None,fixtures=None,shapeFixture=None, density = 1.0,
                    fixedRotation=None):
        if position is not None  and not isinstance(position,b2Vec2):
            position  = b2Vec2(position[0],position[1])

        if bodyDef is None:
            bodyDef = b2BodyDef()
        if btype  is not None:
            bodyDef.btype = btype
        
        if position is not None:
            bodyDef.position = vec2(position)
        if angle is not None:
            bodyDef.angle = angle

        if fixedRotation is not None:
            bodyDef.fixedRotation = fixedRotation

        body =  self._createBodyCpp(bodyDef)

        _shapes = []
        if shape is not None:
            _shapes.append(shape)
        if shapes is not None:
            if isinstance(shapes, b2Shape):
                shapes = [shapes]
            _shapes = _shapes + shapes


        for shape in _shapes:
            if shapeFixture is None:
                shapeFixture =fixtureDef()
                if density is not None:
                    shapeFixture.density = density
            shapeFixture.shape = shape

            body.createFixture(shapeFixture)


        if fixtures is not None:
            if isinstance(fixtures,b2FixtureDef):
                fixtures = [fixtures]
            for fixture in fixtures:
                body.createFixture(fixture)

        return body

    def createStaticBody(self,bodyDef=None, position=None,angle=None, shape=None, shapes=None,fixtures=None, shapeFixture=None, density = 1.0, fixedRotation=None):
        return self._createBody(btype= b2BodyType.b2_staticBody,bodyDef=bodyDef,position=position,
                                angle=angle, shape=shape,shapes=shapes,fixtures=fixtures, shapeFixture=shapeFixture, density=density,fixedRotation=fixedRotation)

    def createDynamicBody(self,bodyDef=None, position=None,angle=None, shape=None, shapes=None,fixtures=None, shapeFixture=None, density = 1.0, fixedRotation=None):
        return self._createBody(btype= b2BodyType.b2_dynamicBody,bodyDef=bodyDef,position=position,
                                angle=angle, shape=shape,shapes=shapes,fixtures=fixtures,  shapeFixture=shapeFixture, density=density,fixedRotation=fixedRotation)
  
    def createKinematicBody(self,bodyDef=None, position=None,angle=None, shape=None, shapes=None,fixtures=None, shapeFixture=None, density = 1.0, fixedRotation=None):
        return self._createBody(btype= b2BodyType.b2_kinematicBody,bodyDef=bodyDef,position=position,
                                angle=angle, shape=shape,shapes=shapes,fixtures=fixtures,  shapeFixture=shapeFixture, density=density,fixedRotation=fixedRotation)
    

    def createBody(self,bodyDef=None,btype=b2BodyType.b2_dynamicBody, position=None,angle=None, shape=None, shapes=None,fixtures=None, shapeFixture=None, density = 1.0, fixedRotation=None):
        return self._createBody(btype= btype ,bodyDef=bodyDef,position=position,
                                angle=angle, shape=shape,shapes=shapes,fixtures=fixtures,  shapeFixture=shapeFixture, density=density,fixedRotation=fixedRotation)
  


    def createMouseJoint(self,bodyA,bodyB,collideConnected=False,target=vec2(0,0),maxForce=0.0, frequencyHz=5.0,dampingRatio=0.7):

        d = mouseJointDef(bodyA=bodyA,bodyB=bodyB,collideConnected=collideConnected,target=target,
                     maxForce=maxForce, frequencyHz=frequencyHz,dampingRatio=dampingRatio)
        return self.createJoint(d)




    def createPrismaticJoint(self,*args,**kwargs):
        d = prismaticJointDef(*args,**kwargs)
        return self.createJoint(d)

_classExtender(_World,
    [
        'bodyList', 'jointList',
        '_createBody', 'createStaticBody',
        'createDynamicBody','createKinematicBody',
        'createBody', 'createMouseJoint','createPrismaticJoint'
    ]
)
