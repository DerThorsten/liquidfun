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
            b2Vec2(4, 0),
            b2Vec2(4, 8),
            b2Vec2(-2, 8)
        ]
        groundbody = self.world.createBody(
            shapes=chainShape(vertices=verts)
        )




        fixture = fixtureDef(shape=circleShape(0.5),density=2.2, friction=0.2)
        body = self.world.createDynamicBody(
            #bodyDef = bodyDef(linearDamping=2.0,angularDamping=2.0),                                              
            position=(1,2.5),
            fixtures=fixture
        ) 

        fixture = fixtureDef(shape=polygonShape(box=(1,1)),density=2.2, friction=0.2)
        body = self.world.createDynamicBody(
            #bodyDef = bodyDef(linearDamping=2.0,angularDamping=2.0),                                              
            position=(1,7.5),
            fixtures=fixture
        ) 



        pdef = particleSystemDef(viscousStrength=5.0,springStrength=0.0)
        psystem = self.world.createParticleSystem(pdef)
        psystem.radius = 0.045
        psystem.damping = 0.2


        shape = polygonShape(box=(2.0,2.0),center=vec2(0,2.01),angle=0)
        pgDef = particleGroupDef(flags=ParticleFlag.waterParticle, 
                                 groupFlags=ParticleGroupFlag.solidParticleGroup,
                                 shape=shape,strength=0.0
                                 )

        group = psystem.createParticleGroup(pgDef)




        pdef = particleSystemDef(viscousStrength=5.0,springStrength=0.0)
        psystem = self.world.createParticleSystem(pdef)
        psystem.radius = 0.045
        psystem.damping = 0.2


        shape = polygonShape(box=(1.0,1.0),center=vec2(1,3.01),angle=0)
        pgDef = particleGroupDef(flags=ParticleFlag.waterParticle, 
                                 groupFlags=ParticleGroupFlag.solidParticleGroup,
                                 shape=shape,strength=0.0
                                 )

        group = psystem.createParticleGroup(pgDef)



       

if __name__ == "__main__":

    testbed = Testbed(guiType='kivy')
    testbed.setExample(DamnBreak)
    testbed.run()

    #main(DamnBreak)
