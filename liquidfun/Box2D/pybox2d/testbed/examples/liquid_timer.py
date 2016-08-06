import sys, os
sys.path.append('../')
from framework import Framework,Testbed
from pybox2d import *

import pybox2d as b2


class LiquidTimer(Framework):
    name = "LiquidTimer"
    description = "This demonstrates a soft distance joint. Press: (b) to delete a body, (j) to delete a joint"
    bodies = []
    joints = []

    def __init__(self):
        super(LiquidTimer, self).__init__()


        world = self.world

        #pdef = b2.particleSystemDef(viscousStrength=5.0,springStrength=0.0)
        pdef = b2.particleSystemDef()
        psystem = world.createParticleSystem(pdef)


        # ground body
        groud = world.createStaticBody(shape=b2.chainShape(
            vertices=[(-2, 0), (2, 0), (2, 4), (-2, 4)],
            loop=True
        ))


        psystem.radius = 0.025
        shape = b2.polygonShape(box=(2,0.4),center=(0,3.6))
        pgd = b2.particleGroupDef(shape=shape,
                                  flags=self.getParticleParameterValue())
        psystem.createParticleGroup(pgd)


        # edge shaped bodies
        edgeShapesVerts = [
            [(-2, 3.2), (-1.2, 3.2) ],
            [(-1.1, 3.2), (2, 3.2)],
            [(-1.2, 3.2), (-1.2, 2.8)],
            [(-1.1, 3.2), (-1.1, 2.8)],
            [(-1.6, 2.4), (0.8, 2)],
            [(1.6, 1.6), (-0.8, 1.2)],
            [(-1.2, 0.8), (-1.2, 0)],
            [(-0.4, 0.8), (-0.4, 0)],
            [(0.4, 0.8), (0.4, 0)],
            [(1.2, 0.8), (1.2, 0)]
        ]
        for verts in edgeShapesVerts:
            body = world.createStaticBody(shape=b2.edgeShape(
                vertices=verts
            ))


if __name__ == "__main__":

    testbed = Testbed(guiType='kivy')
    testbed.setExample(LiquidTimer)
    testbed.run()
