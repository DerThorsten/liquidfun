import pybox2d as b2d
from pybox2d import Vec2

import pygame
from pygame.locals import (QUIT, KEYDOWN, K_ESCAPE)



class Framework(object):

    def __init__(self,gravity=Vec2(0,9.81)):
        self.world = b2d.b2World(gravity)
        self.gui = GuiPyGame(w=640,h=480,ppm=5.0)
        self.world.SetDebugDraw(self.gui.debugDrawCaller)
    def run(self):
        tfps = 60
        dt = 1.0 / tfps
        
        running = True
        while running:
            if self.gui.exit():
                break
            self.gui.drawDebugData(self.world)
            self.world.Step(dt, 10, 10)

class DrawPyGame(object):

    def __init__(self, screen, ppm, w,h):
        self.screen = screen
        self.ppm = ppm
        self.w = w
        self.h = h


    def DrawPolygon(self, vertices, color):
        print "DrawPolygon"
    def DrawSolidPolygon(self, vertices, color):
        print "DrawSolidPolygon",vertices.shape
        c = color.r*255.0,color.g*255.0,color.b*255.0,255
        print c
        vertices *=self.ppm 
        vertices[:,1] = self.h - vertices[:,1]
        pygame.draw.polygon(self.screen, c, vertices)


    def DrawCircle(self, center, radius, color):
        print "DrawCircle"
    def DrawSolidCircle(self, center, radius, color):
        center = int(center.x*self.ppm) ,self.h-int(center.y*self.ppm)
        r = int(radius*self.ppm+0.5)
        c = color.r*255,color.g*255,color.b*255,255
        pygame.draw.circle(self.screen, c, center, r)
        
    def DrawParticles(self, centers, radius, colors, count):
        print "DrawParticles"
    def DrawSegment(self, p1, p2, color):
        print "DrawSegment"
    def DrawTransform(self, xf):
        print "DrawTransform"


class GuiPyGame(object):
    def __init__(self,w,h, ppm):
        self.w = w
        self.h = h
        self.ppm = ppm
        self.screen = pygame.display.set_mode((w, h), 0, 32)
        self.debugDraw = DrawPyGame(screen=self.screen,w=w,h=h,ppm=ppm)
        self.debugDrawCaller = b2DrawCaller = b2d.b2DrawCaller(self.debugDraw)
        pygame.display.set_caption('Simple pygame example')
        self.clock = pygame.time.Clock()

    def exit(self):
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                # The user closed the window or pressed escape
                return True

    def drawDebugData(self, world):
        self.screen.fill((0, 0, 0, 0))
        world.DrawDebugData()
        pygame.display.flip()
        self.clock.tick(60)
def main(exampleCls):
    example = exampleCls()
    example.run()

