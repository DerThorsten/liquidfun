from pybox2d import *





def extendFixtureDef():
    
    def GetUserData(self):
        if self.HasUserData():
            return self._GetUserData()
        else:
            return None
    b2FixtureDef.GetUserData = GetUserData

    def SetUserData(self,data):
        if self.HasUserData():
            return self._DeleteUserData()
        self._SetUserData(data)
    b2FixtureDef.SetUserData = SetUserData 


extendFixtureDef()
del extendFixtureDef



def fixtureDef(shape=None,friction=None,restitution=None, density=None, isSensor=None, ffilter=None, userData=None):
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
    if userData is not None:
        fd.SetUserData(userData)
    return fd


    
def extendFixture():


    def GetNext(self):
        if self.HasNext():
            return self._GetNext()
        else:
            return None
    b2Fixture.GetNext = GetNext


    def GetUserData(self):
        if self.HasUserData():
            return self._GetUserData()
        else:
            return None
    b2Fixture.GetUserData = GetUserData

    def SetUserData(self,data):
        if self.HasUserData():
            return self._DeleteUserData()
        self._SetUserData(data)
    b2Fixture.SetUserData = SetUserData 

extendFixture()
del extendFixture
