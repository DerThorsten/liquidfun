from pybox2d import *
from extend_math import vec2



# shape factories
def edgeShape(vertices):
    assert len(vertices) == 2
    s = b2EdgeShape()
    s.Set(vec2(vertices[0]),vec2(vertices[1]))
    return s

def chainShape(vertices):
    s = b2ChainShape()
    s.CreateLoop(vertices)
    return s


def circleShape(r):
    s = b2CircleShape()
    s.radius = r
    return s

def polygonShape(box=None,center=None,angle=None):
    assert box is not None
    s = b2PolygonShape()
    if center is not None:
        s.SetAsBox(box[0],box[1],centerX=center[0],centerY=center[1],angle=angle)
    elif angle is None:
        s.SetAsBox(hx=box[0],hy=box[1])
    else:
        assert False
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

def extendPolygonShape():
    
    def Vertices(self):
        return [self.GetVertex(i) for i in range(self.GetVertexCount())]

    b2PolygonShape.Vertices = Vertices

extendPolygonShape()
del extendPolygonShape
