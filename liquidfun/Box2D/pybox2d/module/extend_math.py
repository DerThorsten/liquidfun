
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
