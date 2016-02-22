from pybox2d import *


Vec2  = b2Vec2
Vec3  = b2Vec3
Vec4  = b2Vec4
Mat22 = b2Mat22
Mat33 = b2Mat33



def extendWorld():
    
    def _CreateBody(self,btype, position=None,angle=None, shape=None, density = 1.0):
        bodyDef = b2BodyDef()
        bodyDef.type = btype

        if position is not None:
            bodyDef.position = position
        if angle is not None:
            bodyDef.angle = angle

        body =  self.CreateBody(bodyDef)

        if shape is not None:
            body.CreateFixture(shape, density)

        return body
    b2World._CreateBody = _CreateBody

    @property
    def active(self):
        return self.IsActive
    
    b2World.active = active

    def CreateStaticBody(self, position=None,angle=None, shape=None, density = 1.0):
        return self._CreateBody(btype= b2BodyType.b2_staticBody,position=position,
                                angle=angle, shape=shape, density=density)
    
    b2World.CreateStaticBody = CreateStaticBody

    def CreateDynamicBody(self, position=None,angle=None, shape=None, density = 1.0):
        return self._CreateBody(btype= b2BodyType.b2_dynamicBody,position=position,
                                angle=angle, shape=shape, density=density)

    b2World.CreateDynamicBody = CreateDynamicBody



extendWorld()
del extendWorld



def extendBody():

    def CreatePolygonFixture(self, box=None, density=1.0, friction=0.2):

        fixtureDef = b2FixtureDef()

        assert box is not None
        shape = b2PolygonShape()
        shape.SetAsBox(box[0],box[1])

      
        fixtureDef.friction = friction
        fixtureDef.density = density
        fixtureDef.shape = shape 
        self.CreateFixture(fixtureDef)


    b2Body.CreatePolygonFixture = CreatePolygonFixture  

    def GetNext(self):
        if self.HasNext():
            return self._GetNext()
        else:
            return None
    b2Body.GetNext = GetNext


    def GetFixtureList(self):
        if self.HasFixtureList():
            return self._GetFixtureList()
        else:
            return None
    b2Body.GetFixtureList = GetFixtureList


    def Fixtures(self):
        res = []
        fl = self.GetFixtureList()
        if fl is not None:
            while fl is not None:
                res.append(fl)
                fl = fl.GetNext()
        return res
    b2Body.Fixtures = Fixtures

extendBody()
del extendBody


def extendFixture():


    def GetNext(self):
        if self.HasNext():
            return self._GetNext()
        else:
            return None
    b2Fixture.GetNext = GetNext


    

    
extendFixture()
del extendFixture





def extendShape():
    def Vertices(self):
       return [self.GetVertex(i) for i in range(self.GetVertexCount())]
    b2Shape.Vertices = Vertices

extendShape()
del extendShape



def extendPolygonShape():
    
    def Vertices(self):
        return [self.GetVertex(i) for i in range(self.GetVertexCount())]

    b2PolygonShape.Vertices = Vertices

extendPolygonShape()
del extendPolygonShape
