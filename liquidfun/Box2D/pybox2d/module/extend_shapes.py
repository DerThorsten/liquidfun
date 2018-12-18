from . _pybox2d import *
from . extend_math import vec2
from . tools import _classExtender



class ShapeType(object):
    circle = b2Shape.ShapeType.circle
    edge = b2Shape.ShapeType.edge
    chain = b2Shape.ShapeType.chain
    polygon = b2Shape.ShapeType.polygon

    # circle = b2Shape.ShapeType.circle
    # edge = b2Shape.ShapeType.edge
    # chain = b2Shape.ShapeType.chain
    # polygon = b2Shape.ShapeType.polygon


def shape_filter(category_bits=None, mask_bits=None, group_index=None):
    f = b2Filter()
    if category_bits is not None:
        f.category_bits = category_bits
    if mask_bits is not None:
        f.mask_bits = mask_bits
    if group_index is not None:
        f.group_index = group_index


# shape factories
def edge_shape(vertices):
    assert len(vertices) == 2
    s = b2EdgeShape()
    s.set(vec2(vertices[0]),vec2(vertices[1]))
    return s

def chain_shape(vertices,loop=True):
    s = b2ChainShape()
    v = [vec2(vert) for vert in vertices]
    if loop:
        s.create_loop(v)
    else:
        s.create_chain(v)
    return s

def box_loop_shape(w,h):
    verts = [
        vec2(0,0),vec2(0,w),vec2(h,w),vec2(h,0)
    ]
    return chain_shape(verts,True)

def circle_shape(radius, pos = (0,0)):
    s = b2CircleShape()
    s.radius = radius
    s.pos = vec2(pos)
    return s

def polygon_shape(box=None,center=(0,0),angle=0.0,vertices=None):
    s = b2PolygonShape()
    if vertices is None:
        s.set_as_box(box[0],box[1],center_x=center[0],center_y=center[1], angle=angle)
    else:
        verts = [ vec2(v) for v in vertices]
        s.set(verts)
    return s

def extend_shape():
    pass
    # def asMostDerived(self):
    #     if self.isCircleShape():
    #         return self.asCircleShape()
    #     elif self.isChainShape():
    #         return self.asChainShape()
    #     elif self.isEdgeShape():
    #         return self.asEdgeShape()
    #     elif self.isPolygonShape():
    #         return self.asPolygonShape()
    #     else:
    #         raise RuntimeError("cast error")
    # b2Shape.asMostDerived = asMostDerived

extend_shape()
del extend_shape

def extend_polygon_shape():
    

    def _vertices(self):
        return [self.get_vertex(i) for i in range(self.vertex_count)]


    b2PolygonShape._vertices = _vertices
    b2PolygonShape.vertices = property(lambda self: self._vertices())

    
    # b2PolygonShape.vertices_setter = vertices_setter

class _PolygonShape(b2PolygonShape):

    @property
    def vertices(self):
        return [self.getVertex(i) for i in range(self.vertexCount)]

    @vertices.setter
    def vertices(self, v):
        verts = [vec2(vert) for vert in  v]
        self.set(verts)
        

_classExtender(_PolygonShape, ['vertices'])






extend_polygon_shape()
del extend_polygon_shape
