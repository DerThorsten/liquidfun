import sys, os, math
from framework import Framework,Testbed
#from pybox2d import *
import pybox2d as b2d

print(b2d.__file__)

import networkx as nx



class GooDistanceJointDef():
    def __init__(self):
        self.max_add_dist = 10
    def make_jd(self, body_a, body_b, **kwargs):
        return b2d.distance_joint_def(body_a, body_b,length=5, frequency_hz=5, **kwargs)


class GooBallDef(object):
    def __init__(self):

        self.can_be_first = True
        self.add_reach_range = 10.0
        self.max_angle  = 120.0 * math.pi/180.0
        self.min_edge_angle  = 150.0 * math.pi/180.0


class GooGraph(nx.Graph):
    def __init__(self, world):
        super(GooGraph, self).__init__()
        self.world = world

        self.joints = set()
    @property
    def n_goo_balls(self):
        return self.number_of_nodes()
    

    def add_goo_body(self, pos, goo_ball_def):
        fixtureA = b2d.fixture_def(shape=b2d.circle_shape(0.5),density=2.2, friction=0.2)
        body = self.world.create_dynamic_body(
            #bodyDef = bodyDef(linearDamping=2.0,angularDamping=2.0),                                              
            position=pos,
            fixtures=fixtureA,
            angular_damping=30.0
        ) 
        body.int_user_data = self.number_of_nodes()
        self.add_node(body.int_user_data)
        return body

    def create_goo_joint(self, goo_body_a, goo_body_b, goo_ball_def):
        goo_jd = GooDistanceJointDef()
        j = self.world.create_joint(goo_jd.make_jd(goo_body_a, goo_body_b))
        self.add_edge(goo_body_a.int_user_data, goo_body_b.int_user_data)
        self.joints.add(j)

    def try_place_goo_as_edge(self, pos, goo_ball_def):
        if self.n_goo_balls <= 1:
            return False
        else:
            f = self.world.find_closest_n_bodies
            body_filter = lambda b:  b.has_int_user_data and b.int_user_data>= 0
            b_and_d = f(pos=pos, r=goo_ball_def.add_reach_range, n=2, body_filter=body_filter)
            if len(b_and_d) >= 2:
                existing_goo_body_a = b_and_d[0][0]
                existing_goo_body_b = b_and_d[1][0]
                if not self.has_edge(existing_goo_body_a.int_user_data, existing_goo_body_b.int_user_data):
                    if self.leg_angle(pos,b_and_d[0], b_and_d[1])  > goo_ball_def.min_edge_angle:
                        self.create_goo_joint(existing_goo_body_a, existing_goo_body_b, goo_ball_def)

                    return True
        return False

    def leg_angle(self, pos, bpa, bpb):
        #     pos
        #     / \
        #    /pc \
        #   /     \
        #  /pb   pb\
        # A --------B
        pa,pb,pc = b2d.triangel_angles(bpa[0].world_center, bpb[0].world_center, pos)
        #print(pa*180/math.pi, pb*180/math.pi, pc*180/math.pi)

        return pc
         

    def try_place_goo(self, pos, goo_ball_def):
        # try as edge
        added_as_edge = self.try_place_goo_as_edge(pos=pos, goo_ball_def=goo_ball_def)




        if not added_as_edge:
            if self.n_goo_balls == 0 and goo_ball_def.can_be_first:
                self.add_goo_body(pos=pos, goo_ball_def=goo_ball_def)
            else:
                f = self.world.find_closest_n_bodies
                body_filter = lambda b: b.has_int_user_data and b.int_user_data>=0
                b_and_d = f(pos=pos, r=10, n=3, body_filter=body_filter)
                
                if self.number_of_nodes()==1 and len(b_and_d) == 1:
                    existing_goo_body = b_and_d[0][0]
                    new_goo_body = self.add_goo_body(pos=pos, goo_ball_def=goo_ball_def)
                    self.create_goo_joint(existing_goo_body, new_goo_body, goo_ball_def)

                elif len(b_and_d) >= 2:
                    
                    if self.has_edge(b_and_d[0][0].int_user_data, b_and_d[1][0].int_user_data):
                        if self.leg_angle(pos,b_and_d[0], b_and_d[1])  < goo_ball_def.max_angle:

                            existing_goo_body_a = b_and_d[0][0]
                            existing_goo_body_b = b_and_d[1][0]

                            new_goo_body = self.add_goo_body(pos=pos, goo_ball_def=goo_ball_def)
               
                            self.create_goo_joint(existing_goo_body_a, new_goo_body, goo_ball_def)
                            self.create_goo_joint(existing_goo_body_b, new_goo_body, goo_ball_def)

    def destroy_joint(self, j):
        body_a = j.body_a
        body_b = j.body_b
        self.remove_edge(body_a.int_user_data, body_b.int_user_data)
        self.joints.remove(j)
        #print('destroy', j)
        self.world.destroy_joint(j)
        #print('destroyed')

class WogTribute(Framework):
    name = "WogTribute"
    description = "This demonstrates a soft distance joint. Press: (b) to delete a body, (j) to delete a joint"
 
    def __init__(self,gui):
        super(WogTribute, self).__init__(gui)

        verts=[
            b2d.vec2(-20, 0),
            b2d.vec2(20, 0)
        ]
        groundbody = self.world.create_static_body(
            shapes=b2d.chain_shape(vertices=verts, loop=False)
        )

        self.goo_jd = GooDistanceJointDef() 
        self.goo_graph =  GooGraph(self.world)

        self.c = 0

    def pre_step(self, dt):
        pass

    def post_step(self, dt):
        mx = -1.0 * float('inf')
        # special render for joints
        idt = 1.0 / dt
        to_del_j = []
        for j in self.goo_graph.joints:
            rf = j.get_reaction_force(idt).length
            mx = max(rf, mx)
            v = math.exp(-0.02*rf)
            c = (1.0-v)*255.0
            #print(v,c)
            self.gui.renderer.draw_segment(j.anchor_a, j.anchor_b, (c,255.0-c,0))
            #if rf > 200:
            #    to_del_j.append(j)
        #for j in to_del_j:
        #    self.goo_graph.destroy_joint(j)
        #if self.step_count % 10 == 0:
        #    print(mx)
    def on_mouse_down(self, p):

        goo_ball_def = GooBallDef()
        world = self.world
        goo_jd  = self.goo_jd 
        world = self.world
        graph = self.goo_graph

        n_nodes = graph.number_of_nodes()
        graph.try_place_goo(pos=p, goo_ball_def=goo_ball_def)




        return True





       

if __name__ == "__main__":

    testbed = Testbed(guiType='pg')
    testbed.setExample(WogTribute)
    testbed.run()

    #main(WogTribute)
