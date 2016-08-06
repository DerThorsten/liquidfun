import sys, os
sys.path.append('../')
from framework import Framework,Testbed
from pybox2d import *


class Web(Framework):
    name = "Web"
    description = "This demonstrates a soft distance joint. Press: (b) to delete a body, (j) to delete a joint"
    bodies = []
    joints = []

    def __init__(self):
        super(Web, self).__init__()

        # The ground
        ground = self.world.createBody(
            shapes=edgeShape(vertices=[(-40, 0), (40, 0)])
        )
        fixture = fixtureDef(shape=polygonShape(box=(0.5, 0.5)),
                               density=5, friction=0.2)
        self.bodies = [self.world.createDynamicBody(                                              
            position=pos,
            fixtures=fixture
        ) for pos in ((20+-5, 5), (10+5, 5), (10+5, 15), (10+-5, 15))]

        bodies = self.bodies


        # Create the joints between each of the bodies and also the ground
        #         bodyA      bodyB   localAnchorA localAnchorB
        sets = [(ground,    bodies[0], (-10, 0),   (-0.5, -0.5)),
                (ground,    bodies[1], (10, 0),    (0.5, -0.5)),
                (ground,    bodies[2], (10, 20),   (0.5, 0.5)),
                (ground,    bodies[3], (-10, 20),  (-0.5, 0.5)),
                (bodies[0], bodies[1], (0.5, 0),   (-0.5, 0)),
                (bodies[1], bodies[2], (0, 0.5),   (0, -0.5)),
                (bodies[2], bodies[3], (-0.5, 0),  (0.5, 0)),
                (bodies[3], bodies[0], (0, -0.5),  (0, 0.5)),
                ]

        #for b in self.bodies:
        #    print b.GetUserData()

        # We will define the positions in the local body coordinates, the length
        # will automatically be set by the __init__ of the b2DistanceJointDef
        self.joints = []
        for bodyA, bodyB, localAnchorA, localAnchorB in sets:
            dfn = distanceJointDef(
                frequencyHz=1.0,
                dampingRatio=2.1,
                bodyA=bodyA,
                bodyB=bodyB,
                localAnchorA=localAnchorA,
                localAnchorB=localAnchorB
            )
            self.joints.append(self.world.createJoint(dfn))

    def Keyboard(self, key):
        if key == Keys.K_b:
            for body in self.bodies:
                # Gets both FixtureDestroyed and JointDestroyed callbacks.
                self.world.destroyBody(body)
                break

        elif key == Keys.K_j:
            for joint in self.joints:
                # Does not get a JointDestroyed callback!
                self.world.destroyJoint(joint)
                self.joints.remove(joint)
                break

    def FixtureDestroyed(self, fixture):
        super(Web, self).FixtureDestroyed(fixture)
        body = fixture.body
        if body in self.bodies:
            print(body)
            self.bodies.remove(body)
            print("Fixture destroyed, removing its body from the list. Bodies left: %d"
                  % len(self.bodies))

    def JointDestroyed(self, joint):
        if joint in self.joints:
            self.joints.remove(joint)
            print("Joint destroyed and removed from the list. Joints left: %d"
                  % len(self.joints))

if __name__ == "__main__":

    testbed = Testbed(guiType='kivy')
    testbed.setExample(Web)
    testbed.run()
