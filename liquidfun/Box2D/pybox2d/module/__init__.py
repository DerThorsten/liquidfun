from pybox2d import *


Vec2  = b2Vec2
Vec3  = b2Vec3
Vec4  = b2Vec4
Mat22 = b2Mat22
Mat33 = b2Mat33



def vec2(*args):
    l = len(args)
    if l == 1:
        a = args[0]
        if isinstance(a,Vec2):
            return a
        else:
            return Vec2(float(a[0]),float(a[1]))
    elif l == 2:
        return Vec2(float(args[0]),float(args[1]))


class GenericB2dIter(object):
    def __init__(self, currentBody):
        self.currentBody = currentBody
    def __next__(self):
        return self.next()
    def __iter__(self):
        return self
    def next(self):
        if self.currentBody is None:
            raise StopIteration
        else:
            c = self.currentBody
            self.currentBody = c.GetNext()
            return c


def extendWorld():
    
    def _CreateBody(self,btype, position=None,angle=None, shape=None,fixtures=None, density = 1.0):
        if position is not None  and not isinstance(position,b2Vec2):
            position  = b2Vec2(position[0],position[1])
        bodyDef = b2BodyDef()
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


    def CreateStaticBody(self, position=None,angle=None, shape=None, density = 1.0):
        return self._CreateBody(btype= b2BodyType.b2_staticBody,position=position,
                                angle=angle, shape=shape,fixtures=fixtures, density=density)
    
    b2World.CreateStaticBody = CreateStaticBody

    def CreateDynamicBody(self, position=None,angle=None, shape=None,fixtures=None, density = 1.0):
        return self._CreateBody(btype= b2BodyType.b2_dynamicBody,position=position,
                                angle=angle, shape=shape,fixtures=fixtures, density=density)
    b2World.CreateDynamicBody = CreateDynamicBody


    def CreateBody(self,bodyDef=None,btype=None,position=None,shapes=None):
        if bodyDef is not None:
            if btype is not None:
                bodyDef.btype =  btype
            if position is not None:
                bodyDef.position = vec2(position)
            return self._CreateBodyCpp(bodyDef)
        else:
            if shapes is not None:
                if btype is None:
                    btype = b2BodyType.b2_staticBody

                bodyDef = b2BodyDef()
                bodyDef.type = btype
                if position is not None:
                    bodyDef.position = position

                body = self._CreateBodyCpp(bodyDef)
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





extendWorld()
del extendWorld


def extendB2Vec2():
    
    def __getitem__(self, key):
        if key == 0:
            return self.x
        elif key == 1:
            return self.y
        else:
            raise RuntimeError("wrong index")
    b2Vec2.__getitem__ = __getitem__


extendB2Vec2()
del extendB2Vec2




def extendBody():

    def CreatePolygonFixture(self, box=None, density=1.0, friction=0.2):

        fixtureDef = b2FixtureDef()

        assert box is not None
        shape = b2PolygonShape()
        shape.SetAsBox(box[0],box[1])

      
        fixtureDef.friction = friction
        fixtureDef.density = density
        fixtureDef.shape = shape 
        return self.CreateFixture(fixtureDef)

    b2Body.CreatePolygonFixture = CreatePolygonFixture  

    def CreateCircleFixture(self, radius, density=1, friction=0.2):
        fixtureDef = b2FixtureDef()

        shape = b2CircleShape()
        shape.radius = radius
        fixtureDef.friction = friction
        fixtureDef.density = density
        fixtureDef.shape = shape 
        return self.CreateFixture(fixtureDef)

    b2Body.CreateCircleFixture = CreateCircleFixture  

    def GetNext(self):
        if self.HasNext():
            return self._GetNext()
        else:
            return None
    b2Body.GetNext = GetNext


    def GetFixtureList(self):
        blist = None
        if self.HasFixtureList():
            blist = self._GetFixtureList()
        return GenericB2dIter(blist)
    b2Body.GetFixtureList = GetFixtureList

    def GetJointList(self):
        blist = None
        if self.HasFixtureList():
            blist = self._GetJointList()
        return GenericB2dIter(blist)
    b2Body.GetJointList = GetJointList


extendBody()
del extendBody


def jointDef(jtype,bodyA,bodyB,collideConnected=False):
    jd = b2JointDef()
    jd.jtype = jtype
    jd.bodyA = bodyA
    jd.bodyB = bodyB
    jd.collideConnected = collideConnected 
    return jd

def distanceJointDef(bodyA,bodyB,
                     localAnchorA,localAnchorB,
                     collideConnected=False,
                     length=1.0, frequencyHz=0.0,dampingRatio=0.0):

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


def extendJoint():
    def GetNext(self):
        if self.HasNext():
            return self._GetNext()
        else:
            return None
    b2Joint.GetNext = GetNext

extendJoint()
del extendJoint


def fixtureDef(shape=None,friction=None,restitution=None, density=None, isSensor=None, ffilter=None):
    fd = b2FixtureDef()
    if shape is not None : 
        fd.SetShape(shape)
    if friction is not None : 
        fd.friction = friction
    if restitution is not None : 
        fd.restitution = restitution
    if density is not None : 
        fd.density = density
    if isSensor is not None : 
        fd.isSensor = isSensor
    if ffilter is not None : 
        fd.filter = ffilter
    return fd

def extendFixture():


    def GetNext(self):
        if self.HasNext():
            return self._GetNext()
        else:
            return None
    b2Fixture.GetNext = GetNext


    

    
extendFixture()
del extendFixture





# shape factories
def edgeShape(vertices):
    assert len(vertices) == 2
    
    v1 = tuple(vertices[0])
    v2 = tuple(vertices[1])
    s = b2EdgeShape()
    s.Set(Vec2(*v1),Vec2(*v2))
    return s
def extendShape():

    def asMostDerived(self):
        if self.IsCircleShape():
            return self.AsCircleShape()
        elif self.IsChainShape():
            return self.AsChainShape()
        elif self.IsEdgeShape():
            return self.AsEdgeShape()
        elif self.IsPolygonShape():
            return self.AsPolygonShape()
        else:
            raise RuntimeError("cast error")
    b2Shape.asMostDerived = asMostDerived

extendShape()
del extendShape



def polygonShape(box=None):
    assert box is not None
    s = b2PolygonShape()
    s.SetAsBox(box[0],box[1])
    return s

def extendPolygonShape():
    
    def Vertices(self):
        return [self.GetVertex(i) for i in range(self.GetVertexCount())]

    b2PolygonShape.Vertices = Vertices

extendPolygonShape()
del extendPolygonShape
