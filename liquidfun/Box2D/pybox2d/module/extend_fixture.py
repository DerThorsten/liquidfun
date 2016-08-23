from _pybox2d import *
from tools import _classExtender

FixtureDef = b2FixtureDef





def fixtureDef(shape=None,friction=None,restitution=None, density=None, isSensor=None, shapeFilter=None, userData=None):
    fd = b2FixtureDef()
    if shape is not None : 
        fd.shape = shape
    if friction is not None : 
        fd.friction = friction
    if restitution is not None : 
        fd.restitution = restitution
    if density is not None : 
        fd.density = density
    if isSensor is not None : 
        fd.isSensor = isSensor
    if shapeFilter is not None : 
        fd.filter = shapeFilter
    if userData is not None:
        fd.userData = userData
    return fd


class _FixtureDef(b2FixtureDef):

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
    def shape(self):
        return self._shape
    @shape.setter
    def shape(self, shape):
        self._setShape(shape)

_classExtender(_FixtureDef,['userData','shape'])


    
class _Fixture(b2Fixture):

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
    def next(self):
        if self._hasNext():
            return self._getNext()
        else:
            return None
    @property
    def shape(self):
        return self._getShape()
_classExtender(_Fixture,['userData','next','shape'])

