from _pybox2d import *
from tools import _classExtender, GenericB2dIter
from extend_math import vec2
from extend_shapes import *


BodyDef = b2BodyDef
Body = b2Body

b2_staticBody    = b2BodyType.b2_staticBody
b2_kinematicBody = b2BodyType.b2_kinematicBody
b2_dynamicBody   = b2BodyType.b2_dynamicBody

class BodyTypes(object):
    staticBody = b2_staticBody
    kinematicBody = b2_kinematicBody
    dynamicBody = b2_dynamicBody

def bodyDef(btype=None,position=None,angle=None,linearVelocity=None,
            angularVelocity=None,linearDamping=None,angularDamping=None,
            allowSleep=None, awake=None, fixedRotation=None, bullet=None,
            userData=None):
    d = b2BodyDef()
    if btype is not None:
        d.btype = btype
    if position is not None:
        d.position = vec2(position)
    if angle is not None:
        d.angle = angle
    if linearVelocity is not None:
        d.linearVelocity = vec2(linearVelocity)
    if angularVelocity is not None:
        d.angularVelocity = float(angularVelocity)
    if linearDamping is not None:
        d.linearDamping = linearDamping
    if angularDamping is not None:
        d.angularDamping = angularDamping
    if allowSleep is not None:
        d.allowSleep = allowSleep
    if awake is not None:
        d.awake = awake
    if fixedRotation is not None:
        d.fixedRotation = fixedRotation
    if bullet is not None:
        d.bullet = bullet
    if userData is not None:
        d.userData = userData
    return d


class _BodyDef(b2BodyDef):

    @property
    def position(self):
        return self._position
    @position.setter
    def position(self, pos):
        self._position = vec2(pos)


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



_classExtender(_BodyDef,['userData','position'])




class _Body(b2Body):

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
    @property
    def world(self):
        return self._getWorld()

    def createPolygonFixture(self, box=None,**kwargs):

        fixtureDef = b2FixtureDef()

        assert box is not None
        shape = b2PolygonShape()
        shape.setAsBox(box[0],box[1])

        fixtureDef.shape = shape 

        for kw in kwargs:
            setattr(fixtureDef,kw, kwargs[kw])

        return self.createFixture(fixtureDef)

    def createCircleFixture(self, radius, density=1, friction=0.2):
        fixtureDef = b2FixtureDef()

        shape = b2CircleShape()
        shape.radius = radius
        fixtureDef.friction = friction
        fixtureDef.density = density
        fixtureDef.shape = shape 
        return self.createFixture(fixtureDef)

    def createEdgeChainFixture(self, vertices, density=1, friction=0.2):
        fixtureDef = b2FixtureDef()
        shape = chainShape(vertices=vertices,loop=False)
        fixtureDef.shape = shape 
        return self.createFixture(fixtureDef)



    def createFixturesFromShapes(self, shapes, density=1.0):
        if isinstance(shapes, b2Shape):
            shapes = [shapes]
        fixtures = []
        for shape in shapes:
            fixtureDef = b2FixtureDef()
            fixtureDef.density = density
            fixtureDef.shape = shape 
            fixtures.append( self.createFixture(fixtureDef))
        return fixtures

    @property
    def type(self):
        return self.btype

    @property
    def next(self):
        if self._hasNext():
            return self._getNext()
        else:
            return None

    @property
    def fixtures(self):
        flist = None
        if self._hasFixtureList():
            flist = self._getFixtureList()
        return GenericB2dIter(flist)

    @property
    def joints(self):
        jlist = None
        if self._hasJointList():
            jlist = self._getJointList()
        return GenericB2dIter(jlist)

    @property
    def jointList(self):
        return list(self.joints)
        
    @property
    def jointList(self):
        return list(self.joints)


_classExtender(_Body,['userData','type','world','createPolygonFixture','createCircleFixture',
                      'createEdgeChainFixture',
                    'createFixturesFromShapes',
                     'next','fixtures','joints'])


