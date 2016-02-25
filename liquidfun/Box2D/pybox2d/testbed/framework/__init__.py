import pybox2d as b2d
from pybox2d import Vec2

import pygame
from pygame.locals import (QUIT, KEYDOWN, K_ESCAPE)



class Framework(object):

    def __init__(self,gravity=Vec2(0,9.81)):
        self.world = b2d.b2World(gravity)
        self.gui = GuiPyGame(w=640,h=480,ppm=80.0)
        self.world.SetDebugDraw(self.gui.debugDrawCaller)
    def run(self):
        tfps = 120.0
        dt = 1.0 / tfps
        
        running = True
        while running:
            if self.gui.exit():
                break
            self.gui.drawDebugData(self.world)
            self.world.Step(dt, 30, 30)

class DrawPyGame(object):

    def __init__(self, screen, ppm, w,h):
        self.screen = screen
        self.ppm = ppm
        self.w = w
        self.h = h

    def DrawPolygon(self, vertices, color):
        c = color.r*255.0,color.g*255.0,color.b*255.0,255
        pygame.draw.polygon(self.screen, c, vertices,1)

    def DrawSolidPolygon(self, vertices, color):
        c = color.r*255.0,color.g*255.0,color.b*255.0,255
        pygame.draw.polygon(self.screen, c, vertices)


    def DrawCircle(self, center, radius, color):
        c = color.r*255,color.g*255,color.b*255,255
        cent = (int(center.x),int(center.y))
        pygame.draw.circle(self.screen, c, cent, int(radius+0.5),1)
    def DrawSolidCircle(self, center, radius, color):        
        c = color.r*255,color.g*255,color.b*255,255
        pygame.draw.circle(self.screen, c, center, radius)
        
    def DrawParticles(self, centers, radius, colors):
        np = centers.shape[0]
        for p in range(np):
            pygame.draw.circle(self.screen, (100,)*4, centers[p,:], int(radius+0.5))
        
    def DrawSegment(self, p1, p2, color):
        c = color.r*255,color.g*255,color.b*255,255
        pygame.draw.aaline(self.screen, c, (p1.x,p1.y), (p2.x,p2.y), 1)
    #def DrawTransform(self, xf):
    #    print "DrawTransform"


class GuiPyGame(object):
    def __init__(self,w,h, ppm, offset = Vec2(5,1)):
        self.w = w
        self.h = h
        self.ppm = ppm
        self.offset = offset
        self.screen = pygame.display.set_mode((w, h), 0, 32)
        self.debugDraw = DrawPyGame(screen=self.screen,w=w,h=h,ppm=ppm)


        self.debugDrawCaller = b2DrawCaller = b2d.b2DrawCaller(self.debugDraw,
                                                               scale=self.ppm,offset=self.offset,
                                                               flipY=False)
        self.debugDrawCaller.AppendFlags(int(b2d.DrawFlags.shapeBit))
        self.debugDrawCaller.AppendFlags(int(b2d.DrawFlags.jointBit))
        #self.debugDrawCaller.AppendFlags(int(b2d.DrawFlags.aabbBit))
        self.debugDrawCaller.AppendFlags(int(b2d.DrawFlags.centerOfMassBit))
        self.debugDrawCaller.AppendFlags(int(b2d.DrawFlags.particleBit))

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
        self.clock.tick(120.0)
def main(exampleCls):
    example = exampleCls()
    example.run()

