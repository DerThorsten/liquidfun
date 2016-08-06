import sys # "hack"
sys.path.append('/home/tbeier/bld/liquidfun/liquidfun/Box2D/python/')
import pybox2d as b2

import unittest
import nose



def approxEqual(a, b, tol=0.001):
 return abs(a - b) < tol

def testBody():
    pass


class TestBody(unittest.TestCase):

    def test_extended(self):
        world = b2.World()
        fixture1=b2.fixtureDef(shape=b2.circleShape(radius=1), density=1, friction=0.3)
        fixture2=b2.fixtureDef(shape=b2.circleShape(radius=2), density=1, friction=0.3)
        shape1=b2.polygonShape(box=(5,1))
        shape2=b2.polygonShape(box=(5,1))
        shapefixture=b2.fixtureDef(density=2.0, friction=0.3)

        body = world.createStaticBody(fixtures=[fixture1, fixture2],
                shapes=[shape1, shape2], shapeFixture=shapefixture)

        # make sure that 4 bodies were created
        self.assertEqual( len(list(body.fixtures)), 4)

        body = world.createKinematicBody(fixtures=[fixture1, fixture2],
                shapes=[shape1, shape2], shapeFixture=shapefixture)
        self.assertEqual( len(list(body.fixtures)), 4)
        body = world.createDynamicBody(fixtures=[fixture1, fixture2],
                shapes=[shape1, shape2], shapeFixture=shapefixture)
        self.assertEqual( len(list(body.fixtures)), 4)

    def testBodyWorldRef(self):

        world1 = b2.b2World()
        body = world1.createDynamicBody()
        bw = body.world

        assert world1.bodyCount == 1
        assert bw.bodyCount == 1

        body2 = world1.createDynamicBody()
        assert world1.bodyCount == 2
        assert bw.bodyCount == 2



class TestWorld(object):

    def testWorldConstructors(self):

        world1 = b2.b2World()
        world2 = b2.b2World(gravity=(0,-9.81))
        world3 = b2.b2World(gravity=b2.b2Vec2(0,-9.81))
        world4 = b2.world()
        world5 = b2.world(gravity=(0,-9.81))
        world6 = b2.world(gravity=b2.b2Vec2(0,-9.81))

        for w in [world1,world2,world3]:
            assert isinstance(w,b2.b2World)
            assert isinstance(w,b2.World)  
            g = w.gravity
            assert approxEqual(g.x, 0)
            assert approxEqual(g.y, -9.81)
            assert approxEqual(g[0], 0)
            assert approxEqual(g[1], -9.81)

    # ported test from "old" box2d bindings
    def test_helloworld(self):
        gravity = b2.vec2(0, -10)
        world = b2.b2World(gravity)

        groundBodyDef = b2.b2BodyDef()
        groundBodyDef.position = b2.vec2(0, -10)
         
        groundBody = world.createBody(groundBodyDef)
         
        groundBox = b2.b2PolygonShape()
         
        groundBox.setAsBox(50, 10)
         
        groundBody.createFixturesFromShapes(groundBox)
         
        bodyDef = b2.b2BodyDef()
        bodyDef.btype = b2.b2_dynamicBody
        bodyDef.position = (0, 4)
        body = world.createBody(bodyDef)
         
        dynamicBox = b2.b2PolygonShape()
        dynamicBox.setAsBox(1, 1)

        fixtureDef = b2.b2FixtureDef()
        fixtureDef.shape = dynamicBox

        fixtureDef.density = 1
         
        fixtureDef.friction = 0.3
         
        body.createFixture(fixtureDef)
         
        timeStep = 1.0 / 60
        vel_iters, pos_iters = 6, 2

        for i in range(60):
            world.step(timeStep, vel_iters, pos_iters)
            world.clearForces()


    def test_helloworld_pythonic(self):

        world = b2.b2World((0, -10))
        assert world.bodyCount == 0

        # ground body
        groundBody = world.createBody(b2.bodyDef(position=(0, -10)))
        assert world.bodyCount == 1

        groundBody.createFixturesFromShapes(b2.polygonShape(box=(50, 10)))
         
        # body
        body = world.createBody(b2.bodyDef(btype=b2.b2_dynamicBody,
                                           position=(0,4)))
        assert world.bodyCount == 2

        # some fixture
        dynamicBox = b2.polygonShape(box=(1,1))
        fixtureDef = b2.fixtureDef(shape=dynamicBox,density=1,
                                   friction=0.3)         
        body.createFixture(fixtureDef)
         
        timeStep = 1.0 / 60
        vel_iters, pos_iters = 6, 2

        for i in range(60):
            world.step(timeStep, vel_iters, pos_iters)
            world.clearForces()


nose.main()
