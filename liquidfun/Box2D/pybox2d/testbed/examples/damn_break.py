#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# C++ version Copyright (c) 2006-2007 Erin Catto http://www.box2d.org
# Python version Copyright (c) 2016 thorsten
#
# This software is provided 'as-is', without any express or implied
# warranty.  In no event will the authors be held liable for any damages
# arising from the use of this software.
# Permission is granted to anyone to use this software for any purpose,
# including commercial applications, and to alter it and redistribute it
# freely, subject to the following restrictions:
# 1. The origin of this software must not be misrepresented; you must not
# claim that you wrote the original software. If you use this software
# in a product, an acknowledgment in the product documentation would be
# appreciated but is not required.
# 2. Altered source versions must be plainly marked as such, and must not be
# misrepresented as being the original software.
# 3. This notice may not be removed or altered from any source distribution.

import sys, os
sys.path.append('../../')
print sys.path[0]
import testbed
import testbed.framework
from testbed.framework import Testbed,Framework

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
        groundbody = self.world.CreateBody(
            shapes=chainShape(vertices=verts)
        )




        fixture = fixtureDef(shape=circleShape(0.5),density=2.2, friction=0.2)
        body = self.world.CreateDynamicBody(
            #bodyDef = bodyDef(linearDamping=2.0,angularDamping=2.0),                                              
            position=(1,2.5),
            fixtures=fixture
        ) 

        fixture = fixtureDef(shape=polygonShape(box=(1,1)),density=2.2, friction=0.2)
        body = self.world.CreateDynamicBody(
            #bodyDef = bodyDef(linearDamping=2.0,angularDamping=2.0),                                              
            position=(1,7.5),
            fixtures=fixture
        ) 

        if True:

            pdef = particleSystemDef(viscousStrength=5.0,springStrength=0.0)
            psystem = self.world.CreateParticleSystem(pdef)
            psystem.SetRadius(0.025)
            psystem.SetDamping(0.2)


            shape = polygonShape(box=(0.4,1.0),center=vec2(0,2.01),angle=0)
            pgDef = particleGroupDef(flags=ParticleFlag.waterParticle, groupFlags=ParticleGroupFlag.solidParticleGroup,
                                     shape=shape,strength=0.0
                                     )

            group = psystem.CreateParticleGroup(pgDef)

       

if __name__ == "__main__":

    testbed = Testbed(guiType='kivy')
    testbed.setExample(DamnBreak)
    testbed.run()

    #main(DamnBreak)
