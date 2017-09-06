import sys, os
sys.path.append('../')


from framework import Framework,Testbed
from pybox2d import *



class DamnBreak(Framework):
    name = "DamnBreak"
    description = "This demonstrates a soft distance joint. Press: (b) to delete a body, (j) to delete a joint"
    bodies = []
    joints = []

    def __init__(self):
        super(DamnBreak, self).__init__()

        verts=[
            b2Vec2(-2, 0),
            b2Vec2(2, 0),
            b2Vec2(2, 4),
            b2Vec2(-2, 4)
        ]
        ground = self.world.createStaticBody(
            shapes=chainShape(vertices=verts)
        )





    
        psystem = self.particle_system
        psystem.radius = 0.025
        psystem.damping = 0.99


        pflag = ParticleFlag.staticPressureParticle 

        shape = polygonShape(box=(0.8,1.0),center=vec2(-1.2,1.01),angle=0)
        pgDef = particleGroupDef(flags=pflag,
                                 groupFlags=0,#ParticleGroupFlag.rigidParticleGroup,
                                 shape=shape,strength=1.0)

        group = psystem.createParticleGroup(pgDef)






       

if __name__ == "__main__":

    testbed = Testbed(guiType='kivy')
    testbed.setExample(DamnBreak)
    testbed.run()

    #main(DamnBreak)
