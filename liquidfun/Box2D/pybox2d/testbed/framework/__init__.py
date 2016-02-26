import pybox2d as b2d
from pybox2d import vec2

class fwSettings(object):
    # The default backend to use in (can be: pyglet, pygame, etc.)
    backend = 'pygame'

    # Physics options
    hz = 60.0
    velocityIterations = 8
    positionIterations = 3
    # Makes physics results more accurate (see Box2D wiki)
    enableWarmStarting = True
    enableContinuous = True     # Calculate time of impact
    enableSubStepping = False

    # Drawing
    drawStats = True
    drawShapes = True
    drawJoints = True
    drawCoreShapes = False
    drawAABBs = False
    drawOBBs = False
    drawPairs = False
    drawContactPoints = False
    maxContactPoints = 100
    drawContactNormals = False
    drawFPS = True
    drawMenu = True             # toggle by pressing F1
    drawCOMs = False            # Centers of mass
    pointSize = 2.5             # pixel radius for drawing points

    # Miscellaneous testbed options
    pause = False
    singleStep = False
    # run the test's initialization without graphics, and then quit (for
    # testing)
    onlyInit = False



class AABBCallback(b2d.QueryCallback):
    def __init__(self, testPoint):
        super(AABBCallback,self).__init__()

        self.testPoint = vec2(testPoint)
        self.fixture  = None

    def ReportFixture(self, fixture):
        if fixture.TestPoint(self.testPoint):
            self.fixture  =fixture
            return False
        else:
            return True



class Framework(object):

    def __init__(self,gravity=vec2(0,-9.81)):
        self.__reset()
        self.canvas = None
        self.world = b2d.b2World(gravity)
        self.groundbody = self.world.CreateBody()
        print self.groundbody
    def __reset(self):
        """ Reset all of the variables to their starting values.
        Not to be called except at initialization."""
        # Box2D-related
        self.points = []
        self.world = None
        self.bomb = None
        self.mouseJoint = None
        self.settings = fwSettings
        self.bombSpawning = False
        self.bombSpawnPoint = None
        self.mouseWorld = None
        self.using_contacts = False
        self.stepCount = 0

        # Box2D-callbacks
    def step(self, dt):
        self.world.Step(dt, 10, 10, 10)


    def MouseMove(self, p):
        """
        Mouse moved to point p, in world coordinates.
        """
        print "mouse move",p
        self.mouseWorld = p
        if self.mouseJoint is not None:
            print "target",p
            self.mouseJoint.SetTarget(p)

    def MouseDown(self, p):
        """
        Indicates that there was a left click at point p (world coordinates)
        """
        print "mouse down",p
        if self.mouseJoint is not None:
            return

        # Create a mouse joint on the selected body (assuming it's dynamic)
        # Make a small box.
        box =  b2d.aabb(lowerBound=p - b2d.vec2(0.001, 0.001),
                      upperBound=p + b2d.vec2(0.001, 0.001))

        # Query the world for overlapping shapes.
        query = AABBCallback(p)
        self.world.QueryAABB(query, box)

        if query.fixture is not None:
            print "found body"
            body = query.fixture.GetBody()
            # A body was selected, create the mouse joint
            self.mouseJoint = self.world.CreateMouseJoint(
                bodyA=self.groundbody,
                bodyB=body,
                target=p,
                maxForce=10000.0 * body.GetMass()).AsMouseJoint()
            body.SetAwake(True)

    def MouseUp(self, p):
        """
        Left mouse button up.
        """
        print "mouse up",p
        if self.mouseJoint is not None:
            self.world.DestroyJoint(self.mouseJoint)
            self.mouseJoint = None





class Testbed(object):
    def __init__(self, guiType = "kivy"):
        self.guiType =guiType

        if guiType == "kivy":
            from kivy_gui import KivyTestbedGui
            self.guiCls = KivyTestbedGui
        if guiType == "pygame":
            from pygame_gui import PyGameTestbedGui
            self.guiCls = PyGameTestbedGui

    def setExample(self, cls):
        self.exampleCls = cls

    def run(self):
        self.guiCls(testbed=self).run()
