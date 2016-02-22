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

# --- pygame setup ---
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
pygame.display.set_caption('Simple pygame example')
clock = pygame.time.Clock()


gravity = b2d.b2Vec2(x=0,y=-9.81)
world = b2d.b2World(gravity=gravity)




shape = b2d.b2PolygonShape()
print type(shape)
shape.SetAsBox(50,10)

ground_body = world.CreateStaticBody(
    position = b2d.b2Vec2(0,1),
    shape = shape
)

dynamic_body = world.CreateDynamicBody(position=b2d.b2Vec2(10, 20), angle=15)


box = dynamic_body.CreatePolygonFixture(box=(1.5, 2.5), density=1, friction=0.3)





colors = {
    b2d.b2BodyType.b2_staticBody: (255, 255, 255, 255),
    b2d.b2BodyType.b2_dynamicBody: (127, 127, 127, 255),
}


# --- main game loop ---
running = True
while running:
    # Check the event queue
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            # The user closed the window or pressed escape
            running = False

    screen.fill((0, 0, 0, 0))
    # Draw the world
    for body in (ground_body, dynamic_body):  # or: world.bodies
        
        print body.position.y
        # The body gives us the position and angle of its shapes
        for fixture in body.Fixtures():
            # The fixture holds information like density and friction,
            # and also the shape.
            shape  = fixture.GetShape()
            pshape = shape.AsPolygonShape()
            assert pshape.IsPolygonShape()

            #print type(shape)
            #pshape = b2d.b2PolygonShapeCast(shape)
            #pshape.__class__ = b2d.b2PolygonShape
            #print type(pshape)
            #shape.__class__ = b2d.b2PolygonShape
            # Naively assume that this is a polygon shape. (not good normally!)
            # We take the body's transform and multiply it with each
            # vertex, and then convert from meters to pixels with the scale
            # factor.
            mf = b2d.b2Mul
            vertices = [(mf(body.GetTransform() , v)) * PPM for v in pshape.Vertices()]

            #for v in vertices:
            #    print v.x,v.y

            # But wait! It's upside-down! Pygame and Box2D orient their
            # axes in different ways. Box2D is just like how you learned
            # in high school, with positive x and y directions going
            # right and up. Pygame, on the other hand, increases in the
            # right and downward directions. This means we must flip
            # the y components.
            vertices = [(v.x, SCREEN_HEIGHT - v.y) for v in vertices]

            pygame.draw.polygon(screen, colors[body.GetType()], vertices)

    # Make Box2D simulate the physics of our world for one step.
    # Instruct the world to perform a single step of simulation. It is
    # generally best to keep the time step and iterations fixed.
    # See the manual (Section "Simulating the World") for further discussion
    # on these parameters and their implications.
    world.Step(TIME_STEP, 10, 10)

    # Flip the screen and try to keep at the target FPS
    pygame.display.flip()
    clock.tick(TARGET_FPS)

pygame.quit()
print('Done!')
