import sys, os
sys.path.append('../')
from framework import Framework,Testbed
import pybox2d as b2



class CollisionFiltering(Framework):
    name = "CollisionFiltering"
    description = "This demonstrates a soft distance joint. Press: (b) to delete a body, (j) to delete a joint"
    bodies = []
    joints = []

    def __init__(self):
        super(CollisionFiltering, self).__init__()

        # Ground body
        world = self.world
        ground = world.createBody(
            shapes=b2.edgeShape(vertices=[(-40, 0), (40, 0)])
        )

        # Define the groups that fixtures can fall into
        # Note that negative groups never collide with other negative ones.
        smallGroup = 1
        largeGroup = -1

        # And the categories
        # Note that these are bit-locations, and as such are written in
        # hexadecimal.
        # defaultCategory = 0x0001
        triangleCategory = 0x0002
        boxCategory = 0x0004
        circleCategory = 0x0008

        # And the masks that define which can hit one another
        # A mask of 0xFFFF means that it will collide with everything else in
        # its group. The box mask below uses an exclusive OR (XOR) which in
        # effect toggles the triangleCategory bit, making boxMask = 0xFFFD.
        # Such a mask means that boxes never collide with triangles.  (if
        # you're still confused, see the implementation details below)

        triangleMask = 0xFFFF
        boxMask = 0xFFFF ^ triangleCategory
        circleMask = 0xFFFF

        # The actual implementation determining whether or not two objects
        # collide is defined in the C++ source code, but it can be overridden
        # in Python (with b2ContactFilter).
        # The default behavior goes like this:
        #   if (filterA.groupIndex == filterB.groupIndex and filterA.groupIndex != 0):
        #       collide if filterA.groupIndex is greater than zero (negative groups never collide)
        #   else:
        #       collide if (filterA.maskBits & filterB.categoryBits) != 0 and (filterA.categoryBits & filterB.maskBits) != 0
        #
        # So, if they have the same group index (and that index isn't the
        # default 0), then they collide if the group index is > 0 (since
        # negative groups never collide)
        # (Note that a body with the default filter settings will always
        # collide with everything else.)
        # If their group indices differ, then only if their bitwise-ANDed
        # category and mask bits match up do they collide.
        #
        # For more help, some basics of bit masks might help:
        # -> http://en.wikipedia.org/wiki/Mask_%28computing%29

        # Small triangle
        triangle = b2.fixtureDef(
            shape=b2.polygonShape(vertices=[(-1, 0), (1, 0), (0, 2)]),
            density=1,
            shapeFilter=b2.shapeFilter(
                groupIndex=smallGroup,
                categoryBits=triangleCategory,
                maskBits=triangleMask,
            )
        )
        world.createDynamicBody(
            position=(-5, 2),
            fixtures=triangle,
        )

        triangle.shape.vertices = [
            b2.vec2(v) *2.0 for v in triangle.shape.vertices]
        triangle.filter.groupIndex = largeGroup

        trianglebody = world.createDynamicBody(
            position=(-5, 6),
            fixtures=triangle,
            fixedRotation=True,  # <--
        )
        # note that the large triangle will not rotate
        
        # Small box
        box = b2.fixtureDef(
            shape=b2.polygonShape(box=(1, 0.5)),
            density=1,
            restitution=0.1,
            shapeFilter = b2.shapeFilter(
                groupIndex=smallGroup,
                categoryBits=boxCategory,
                maskBits=boxMask,
            )
        )

        world.createDynamicBody(
            position=(0, 2),
            fixtures=box,
        )

        # Large box
        box.shape  = b2.polygonShape(box=(1, 0.5))
        box.filter.groupIndex = largeGroup
        world.createDynamicBody(
            position=(0, 6),
            fixtures=box,
        )

        # Small circle
        circle = b2.fixtureDef(
            shape=b2.circleShape(radius=1),
            density=1,
            shapeFilter=b2.shapeFilter(
                groupIndex=smallGroup,
                categoryBits=circleCategory,
                maskBits=circleMask,
            )
        )

        world.createDynamicBody(
            position=(5, 2),
            fixtures=circle,
        )

        # Large circle
        circle.shape.radius *= 2
        circle.filter.groupIndex = largeGroup
        world.createDynamicBody(
            position=(5, 6),
            fixtures=circle,
        )

        # Create a joint for fun on the big triangle
        # Note that it does not inherit or have anything to do with the
        # filter settings of the attached triangle.
        box = b2.fixtureDef(shape=b2.polygonShape(box=(0.5, 1)), density=1)

        testbody = world.createDynamicBody(
            position=(-5, 10),
            fixtures=box,
        )
        world.createPrismaticJoint(
            bodyA=trianglebody,
            bodyB=testbody,
            enableLimit=True,
            localAnchorA=(0, 4),
            localAnchorB=(0, 0),
            localAxisA=(0, 1),
            lowerTranslation=-1,
            upperTranslation=1,
        )

if __name__ == "__main__":

    testbed = Testbed(guiType='kivy')
    testbed.setExample(CollisionFiltering)
    testbed.run()
