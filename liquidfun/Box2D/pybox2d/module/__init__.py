

from . _pybox2d import *

from . tools import *
from . extend_math import *
from . extend_draw import *
from . extend_world import *
from . extend_body import *
from . extend_fixture import *
from . extend_shapes import *
from . extend_joints import *
from . extend_particles import *
from . extend_collision import *
from . extend_contact import *
from . query_callback import *

from . destruction_listener import DestructionListener

class RayCastCallback(b2RayCastCallbackCaller):

    def __init__(self):
        super(RayCastCallback,self).__init__(self)

    def report_fixture(self, fixture, point1, point2):
        raise NotImplementedError 
    #def report_particle(self, particleSystem, index):
    #    return False
    #def should_query_particle_system(self, particleSystem):
    #    return False


class ContactListener(b2ContactListenerCaller):

    def __init__(self):
        super(ContactListener,self).__init__(self)

    def begin_contact(self, contact):
        pass

    def end_contact(self, contact):
        pass

    def begin_contact_particle_body(self, particleSystem, particleBodyContact):
        pass

    def begin_contact_particle(self, particleSystem, indexA, indexB):
        pass

    def end_contact_particle(self, particleSystem, indexA, indexB):
        pass

    def pre_solve(self, contact, oldManifold):
        pass

    def post_solve(self, contact, impulse):
        pass


class DebugDraw(b2DrawCaller):
    def __init__(self, float_colors=True):
        self.float_colors = float_colors
        super(DebugDraw, self).__init__(self, bool(float_colors))

    def draw_solid_circle(self, center, radius, axis, c):
        raise NotImplementedError 

    def draw_circle(self, center, radius, c):
        raise NotImplementedError 

    def draw_segment(self,v1, v2, c):
        raise NotImplementedError 

    def draw_polygon(self,vertices, c):
        raise NotImplementedError 

    def draw_solid_polygon(self,vertices, c):
        raise NotImplementedError 

    def draw_particles(self, centers, radius,  c=None):
        raise NotImplementedError 
    


class BatchDebugDraw(DebugDraw):

    def __init__(self, options = None, float_colors=True):
        super(BatchDebugDraw, self).__init__(float_colors=float_colors)
        if options is None:
            options = BatchDebugDrawOptions()

        self.options = options

    def drawing_aabb(self, aabb):
        pass

    def draw_solid_polygons(self, points, connect, color):
        pass

    def draw_polygons(self, points, connect, color):
        pass

    def draw_segments(self, points, connect, color):
        pass

    def draw_circles(self, centers, radii, color):
        pass

    def draw_particles(self, centers, radius, colors):
        pass




class ContactFilter(b2ContactFilterCaller):

    def __init__(self):
        super(ContactFilter,self).__init__(self)


    def should_collide_fixture_fixture(self, fixtureA, fixtureB):
        pass

    def should_collide_fixture_particle(self, fixture, particleSystem, particleIndex):
        pass

    def should_collide_particle_particle(self, particleSystem, particleIndexA, particleIndexB):
        pass   


    




# class BatchDebugDraw(object):
#     def __init__(self, world):
#         opts = ExtendedDebugDrawOptions()
#         self.edd = ExtendedDebugDraw(opts)
#         self.world = world
    

#         self.inactive_body_color  = (0.5, 0.5, 0.3)
#         self.static_body_color    = (0.5, 0.9, 0.5)
#         self.kinematic_body_color = (0.5, 0.5, 0.9)
#         self.sleeping_body_color  = (0.6, 0.6, 0.6)
#         self.dynamic_body_color   = (0.9, 0.7, 0.7)

#     def get_polygon_shapes(self):
#         names = [
#             "inactive_body",
#             "static_body",
#             "kinematic_body",
#             "sleeping_body",
#             "dynamic_body",
#         ]
#         ret = dict()
#         for name in names:
#             sub_dict = dict()
            
#             f = getattr(self.edd,"%s_polygon_shapes"%name)
#             verts,connect = f()

#             sub_dict['color'] = getattr(self, "%s_color"%name)
#             sub_dict['vertices'] = verts.copy()
#             sub_dict['connect'] = connect.copy()
#             ret[name] = sub_dict
#         return ret

#     def fill(self):
#         self.edd.fill(self.world)

#     def clear(self):
#         self.edd.clear()