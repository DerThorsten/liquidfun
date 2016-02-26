from pybox2d import *
from tools import GenericB2dIter



def bodyDef(btype=None,position=None,angle=None,linearVelocity=None,
            angularVelocity=None,linearDamping=None,angularDamping=None,
            allowSleep=None, awake=None, fixedRotation=None, bullet=None,
            userData=None):
    d = b2BodyDef()
    if btype is not None:
        d.btype = btype
    if position is not None:
        d.position = position
    if angle is not None:
        d.angle = angle
    if linearVelocity is not None:
        d.linearVelocity = linearVelocity
    if angularVelocity is not None:
        d.angularVelocity = angularVelocity
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
        d.SetUserData(userData)
    return d



def extendBodyDef():
    
    def GetUserData(self):
        if self.HasUserData():
            return self._GetUserData()
        else:
            return None
    b2BodyDef.GetUserData = GetUserData

    def SetUserData(self,data):
        if self.HasUserData():
            return self._DeleteUserData()
        self._SetUserData(data)
    b2BodyDef.SetUserData = SetUserData 


extendBodyDef()
del extendBodyDef

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

    def GetUserData(self):
        if self.HasUserData():
            return self._GetUserData()
        else:
            return None
    b2Body.GetUserData = GetUserData

    def SetUserData(self,data):
        if self.HasUserData():
            return self._DeleteUserData()
        self._SetUserData(data)
    b2Body.SetUserData = SetUserData 

extendBody()
del extendBody



