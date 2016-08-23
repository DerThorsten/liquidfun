
from _pybox2d import b2AABB
from extend_math import vec2


Aabb = b2AABB

def aabb(lowerBound, upperBound):
    lb = vec2(lowerBound)
    ub = vec2(upperBound)

    r = b2AABB()
    r.lowerBound = lb
    r.upperBound = ub

    return r
