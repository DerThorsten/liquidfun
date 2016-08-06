
from pybox2d import *
import numpy 

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




class Vec2Iter(object):
    def __init__(self,vector, currentIndex=0):
        self.vector = vector
        self.currentIndex = currentIndex
    def __next__(self):
        return self.next()
    def __iter__(self):
        return self
    def next(self):
        if self.currentIndex==2:
            raise StopIteration
        else:
            c = self.vector[self.currentIndex]
            self.currentIndex +=1
            return c



def extendB2Vec2():
    

    def __setitem__(self, key, val):

        if int(key) == 0:
            self.x = val
        elif int(key) == 1:
            self.y = val
        else:
            raise RuntimeError("wrong index %s"%str(key))
    b2Vec2.__setitem__ = __setitem__


    def __getitem__(self, key):

        if int(key) == 0:
            return self.x
        elif int(key) == 1:
            return self.y
        else:
            raise RuntimeError("wrong index %s"%str(key))
    b2Vec2.__getitem__ = __getitem__

    def isfinite(self):
        return numpy.isfinite(self.x) and numpy.isfinite(self.y)
    b2Vec2.isfinite = isfinite
  

    def __iter__(self):
        return Vec2Iter(self)
    b2Vec2.__iter__ = __iter__

  
    def asTuple(self):
        return (self.x,self.y)
    b2Vec2.asTuple = asTuple

    def __repr__(self):
        return "(%f,%f)"%(self.x,self.y)
    b2Vec2.__repr__ = __repr__

    def __str__(self):
        return "(%f,%f)"%(self.x,self.y)
    b2Vec2.__str__ = __str__
extendB2Vec2()
del extendB2Vec2
