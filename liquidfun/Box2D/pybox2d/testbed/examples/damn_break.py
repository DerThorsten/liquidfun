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
from testbed.framework import main,Framework

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
        ground = self.world.CreateBody(
            shapes=chainShape(vertices=verts)
        )



        pdef = particleSystemDef()
        psystem = self.world.CreateParticleSystem(pdef)
        psystem.SetRadius(0.025)
        psystem.SetDamping(0.2)


        shape = polygonShape(box=(0.8,1.0),center=vec2(-1.2,1.01),angle=0)
        pgDef = particleGroupDef(shape=shape,flags=ParticleGroupFlag.solidParticleGroup)

        group = psystem.CreateParticleGroup(pgDef)

       

if __name__ == "__main__":
    main(DamnBreak)
