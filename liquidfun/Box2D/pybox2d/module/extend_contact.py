
from pybox2d import b2Contact,b2WorldManifold,b2ContactProxy
from tools import _classExtender
from extend_math import vec2

class _Contact(b2Contact):

    @property
    def fixtureA(self):
        return self._getFixtureA()

    @property
    def fixtureB(self):
        return self._getFixtureB()

    @property
    def worldManifold(self):
        wm = b2WorldManifold()
        self._getWorldManifold(wm)
        return wm



_classExtender(_Contact,['fixtureA','fixtureB','worldManifold'])





class _ContactProxy(b2ContactProxy):

    @property
    def fixtureA(self):
        return self._getFixtureA()

    @property
    def fixtureB(self):
        return self._getFixtureB()

    @property
    def worldManifold(self):
        wm = b2WorldManifold()
        self._getWorldManifold(wm)
        return wm



_classExtender(_ContactProxy,['fixtureA','fixtureB','worldManifold'])
