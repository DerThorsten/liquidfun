import pybox2d as b2d


import pygame
from pygame.locals import (QUIT, KEYDOWN, K_ESCAPE)


# --- constants ---
# Box2D deals with meters, but we want to display pixels,
# so define a conversion factor:
PPM = 5.0  # pixels per meter
TARGET_FPS = 60
TIME_STEP = 1.0 / TARGET_FPS
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480

class Draw(object):

    def __init__(self, ppm, w,h):
        self.ppm = ppm
        self.w = w
        self.h = h

        # --- pygame setup ---
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
        pygame.display.set_caption('Simple pygame example')
        self.clock = pygame.time.Clock()

    def DrawPolygon(self, vertices, color):
        print "DrawPolygon"
    def DrawSolidPolygon(self, vertices, color):
        print "DrawSolidPolygon",vertices.shape
        c = color.r*255.0,color.g*255.0,color.b*255.0,255
        pygame.draw.polygon(self.screen, c, vertices)


    def DrawCircle(self, center, radius, color):
        print "DrawCircle"
    def DrawSolidCircle(self, center, radius, color):
        c = color.r*255,color.g*255,color.b*255,255
        pygame.draw.circle(self.screen, c, center, radius)
        
    def DrawParticles(self, centers, radius, colors, count):
        print "DrawParticles"
    def DrawSegment(self, p1, p2, color):
        print "DrawSegment"
    def DrawTransform(self, xf):
        print "DrawTransform"



debugDraw  = Draw(PPM,SCREEN_WIDTH, SCREEN_HEIGHT)
b2DrawCaller = b2d.b2DrawCaller(debugDraw)






gravity = b2d.b2Vec2(x=0,y=-9.81)
world = b2d.b2World(gravity=gravity)


world.SetDebugDraw(b2DrawCaller)


shape = b2d.b2PolygonShape()
print type(shape)
shape.SetAsBox(50,10)

ground_body = world.CreateStaticBody(
    position = b2d.b2Vec2(0,1),
    shape = shape
)



# polygon box
dynamic_body = world.CreateDynamicBody(position=b2d.b2Vec2(10, 20), angle=15)
box = dynamic_body.CreatePolygonFixture(box=(1.5, 2.5), density=1, friction=0.3)


dynamic_body2 = world.CreateDynamicBody(position=b2d.b2Vec2(20, 20), angle=15)
box = dynamic_body2.CreatePolygonFixture(box=(1.5, 2.5), density=1, friction=0.3)

# circle
body = world.CreateDynamicBody(position=b2d.b2Vec2(40, 100))
circle = body.CreateCircleFixture(radius=2.5, density=1, friction=0.3)


colors = {
    b2d.b2BodyType.b2_staticBody: (255, 255, 255, 255),
    b2d.b2BodyType.b2_dynamicBody: (127, 127, 127, 255),
}

bodies = [ground_body,dynamic_body,dynamic_body2, body]

def my_draw_polygon(polygon, body, fixture):
    #print "draw pol"
    mf = b2d.b2Mul
    vertices = [mf(body.GetTransform(),v) * PPM for v in polygon.Vertices()]
    vertices = [(v[0], SCREEN_HEIGHT - v[1]) for v in vertices]
    pygame.draw.polygon(screen, colors[body.GetType()], vertices)
b2d.b2PolygonShape.draw = my_draw_polygon


def my_draw_circle(circle, body, fixture):
    #print "draw", circle.radius,circle.pos.x,circle.pos.y
    mf = b2d.b2Mul
    position = mf(body.GetTransform() , circle.pos) * PPM
    position = (position[0], SCREEN_HEIGHT - position[1])
    pygame.draw.circle(screen, colors[body.GetType()], [int(
        x) for x in position], int(circle.radius * PPM))
    # Note: Python 3.x will enforce that pygame get the integers it requests,
    #       and it will not convert from float.
b2d.b2CircleShape.draw = my_draw_circle



# --- main game loop ---
running = True
while running:
    # Check the event queue
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            # The user closed the window or pressed escape
            running = False

    
    # Draw the world
    # 
    debugDraw.screen.fill((0, 0, 0, 0))
    world.DrawDebugData()

    for joints in world.GetJointList():
        joints

    for body in world.GetBodyList():  # or: world.bodies
        
        #print body.position.y
        # The body gives us the position and angle of its shapes
        for fixture in body.GetFixtureList():
            # The fixture holds information like density and friction,
            # and also the shape.
            shape  = fixture.GetShape().asMostDerived()
            #print type(shape)
            #shape.draw(body,fixture)
            
    # Make Box2D simulate the physics of our world for one step.
    # Instruct the world to perform a single step of simulation. It is
    # generally best to keep the time step and iterations fixed.
    # See the manual (Section "Simulating the World") for further discussion
    # on these parameters and their implications.
    world.Step(TIME_STEP, 10, 10)
    world.DrawDebugData()
    # Flip the screen and try to keep at the target FPS
    pygame.display.flip()
    debugDraw.clock.tick(TARGET_FPS)

pygame.quit()
print('Done!')
b2DrawCaller.foo()
