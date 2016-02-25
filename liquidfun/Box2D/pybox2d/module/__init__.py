from pybox2d import *

Vec2  = b2Vec2
Vec3  = b2Vec3
Vec4  = b2Vec4
Mat22 = b2Mat22
Mat33 = b2Mat33

class DrawFlags(object):
    shapeBit              = 0x0001
    jointBit              = 0x0002
    aabbBit               = 0x0004
    pairBit               = 0x0008
    centerOfMassBit       = 0x0010
    particleBit           = 0x0020



class ParticleGroupFlag(object):
    # prevents overlapping or leaking.
    solidParticleGroup = 1 << 0
    # Keeps its shape.
    rigidParticleGroup = 1 << 1
    # Won't be destroyed if it gets empty.
    particleGroupCanBeEmpty = 1 << 2
    # Will be destroyed on next simulation step.
    particleGroupWillBeDestroyed = 1 << 3
    # Updates depth data on next simulation step.
    particleGroupNeedsUpdateDepth = 1 << 4
    particleGroupInternalMask = particleGroupWillBeDestroyed | particleGroupNeedsUpdateDepth


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
    
    def _CreateBody(self,btype=None, bodyDef=None,position=None,angle=None, shape=None,fixtures=None, density = 1.0):
        if position is not None  and not isinstance(position,b2Vec2):
            position  = b2Vec2(position[0],position[1])

        if bodyDef is not None:
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
        if shapes is not None:
            if btype is None:
                btype = b2BodyType.b2_staticBody

            if bodyDef is None:
                bodyDef = b2BodyDef()
            if btype is not None:
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

def chainShape(vertices):
    s = b2ChainShape()
    s.CreateLoop(vertices)
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

def polygonShape(box=None,center=None,angle=None):
    assert box is not None
    s = b2PolygonShape()
    s.SetAsBox(box[0],box[1],centerX=center[0],centerY=center[1],angle=angle)
    return s

def extendPolygonShape():
    
    def Vertices(self):
        return [self.GetVertex(i) for i in range(self.GetVertexCount())]

    b2PolygonShape.Vertices = Vertices

extendPolygonShape()
del extendPolygonShape



def particleSystemDef(
    strictContactCheck = False,
    density = 1.0,
    gravityScale = 1.0,
    radius = 1.0,
    maxCount = 0,
    pressureStrength = 0.05,
    dampingStrength = 1.0,
    elasticStrength = 0.25,
    springStrength = 0.25,
    viscousStrength = 0.25,
    surfaceTensionPressureStrength = 0.2,
    surfaceTensionNormalStrength = 0.2,
    repulsiveStrength = 1.0,
    powderStrength = 0.5,
    ejectionStrength = 0.5,
    staticPressureStrength = 0.2,
    staticPressureRelaxation = 0.2,
    staticPressureIterations = 8,
    colorMixingStrength = 0.5,
    destroyByAge = True,
    lifetimeGranularity = 1.0 / 60.0
):
    d = b2ParticleSystemDef()
    d.pressureStrength = pressureStrength
    d.dampingStrength = dampingStrength
    d.elasticStrength = elasticStrength
    d.springStrength = springStrength
    d.viscousStrength = viscousStrength
    d.surfaceTensionPressureStrength = surfaceTensionPressureStrength
    d.surfaceTensionNormalStrength = surfaceTensionNormalStrength
    d.repulsiveStrength = repulsiveStrength
    d.powderStrength = powderStrength
    d.ejectionStrength = ejectionStrength
    d.staticPressureStrength = staticPressureStrength
    d.staticPressureRelaxation = staticPressureRelaxation
    d.staticPressureIterations = staticPressureIterations
    d.colorMixingStrength = colorMixingStrength
    d.destroyByAge = destroyByAge
    d.lifetimeGranularity = lifetimeGranularity

    return d


def particleGroupDef(flags=None,groupFlags=None,position=None,
                     angle=None,linearVelocity=None,angularVelocity=None,
                     color=None,strength=None,shape=None,stride=None,
                     particleCount=None,group=None):
    
    d = b2ParticleGroupDef()

    if flags is not None:
        d.flags = flags
    if groupFlags is not None:
        d.groupFlags = groupFlags
    if position is not None:
        d.position = position
    if angle is not None:
        d.angle = angle
    if linearVelocity is not None:
        d.linearVelocity = linearVelocity
    if angularVelocity is not None:
        d.angularVelocity = angularVelocity
    if color is not None:
        d.color = color
    if linearVelocity is not None:
        d.linearVelocity = linearVelocity
    if angularVelocity is not None:
        d.angularVelocity = angularVelocity
    if color is not None:
        d.color = color
    if strength is not None:
        d.strength = strength
    if shape is not None:
        d.SetShape(shape)
    if stride is not None:
        d.stride = stride
    if particleCount is not None:
        d.particleCount = particleCount
    if group is not None:
        d.SetGroupr(shape)
    
    return d
