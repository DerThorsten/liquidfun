from _pybox2d import *
from extend_math import vec2
from tools import _classExtender



class ShapeType(object):
    e_circle = b2Shape.ShapeType.e_circle
    e_edge = b2Shape.ShapeType.e_edge
    e_chain = b2Shape.ShapeType.e_chain
    e_polygon = b2Shape.ShapeType.e_polygon

    circle = b2Shape.ShapeType.e_circle
    edge = b2Shape.ShapeType.e_edge
    chain = b2Shape.ShapeType.e_chain
    polygon = b2Shape.ShapeType.e_polygon

def shapeFilter(categoryBits=None, maskBits=None, groupIndex=None):
    f = b2Filter()
    if categoryBits is not None:
        f.categoryBits = categoryBits
    if maskBits is not None:
        f.maskBits = maskBits
    if groupIndex is not None:
        f.groupIndex = groupIndex


# shape factories
def edgeShape(vertices):
    assert len(vertices) == 2
    s = b2EdgeShape()
    s.set(vec2(vertices[0]),vec2(vertices[1]))
    return s

def chainShape(vertices,loop=True):
    s = b2ChainShape()
    v = [vec2(vert) for vert in vertices]
    if loop:
        s.createLoop(v)
    else:
        s.createChain(v)
    return s

def boxLoopShape(w,h):
    verts = [
        vec2(0,0),vec2(0,w),vec2(h,w),vec2(h,0)
    ]
    return chainShape(verts,True)

def circleShape(radius, pos = (0,0)):
    s = b2CircleShape()
    s.radius = radius
    s.pos = vec2(pos)
    return s

def polygonShape(box=None,center=(0,0),angle=0.0,vertices=None):
    s = b2PolygonShape()
    if vertices is None:
        s.setAsBox(box[0],box[1],centerX=center[0],centerY=center[1],angle=angle)
    else:
        verts = [ vec2(v) for v in vertices]
        s.set(verts)
    return s

def extendShape():

    def asMostDerived(self):
        if self.isCircleShape():
            return self.asCircleShape()
        elif self.isChainShape():
            return self.asChainShape()
        elif self.isEdgeShape():
            return self.asEdgeShape()
        elif self.isPolygonShape():
            return self.asPolygonShape()
        else:
            raise RuntimeError("cast error")
    b2Shape.asMostDerived = asMostDerived

extendShape()
del extendShape

def extendPolygonShape():
    
    def Vertices(self):
        return [self.GetVertex(i) for i in range(self.GetVertexCount())]

    b2PolygonShape.Vertices = Vertices


class _PolygonShape(b2PolygonShape):

    @property
    def vertices(self):
        return [self.getVertex(i) for i in range(self.vertexCount)]

    @vertices.setter
    def vertices(self, v):
        verts = [vec2(vert) for vert in  v]
        self.set(verts)
        

_classExtender(_PolygonShape, ['vertices'])






extendPolygonShape()
del extendPolygonShape
