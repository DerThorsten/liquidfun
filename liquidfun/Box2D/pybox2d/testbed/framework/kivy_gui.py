import kivy
kivy.require('1.1.1')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import *
import numpy
from kivy.clock import Clock


from kivy.config import Config
Config.set('input', 'mouse', 'mouse,disable_multitouch')



from pybox2d import *


class DrawKivy(object):

    def __init__(self):
        pass

    def DrawSolidCircle(self, center, radius, axis, c):
        print "circle"
        center = (numpy.array(center)-radius)
        size = numpy.array([radius*2,radius*2])
        #print "color",color
        #with self.canvas:
        e = Ellipse(pos=center,size=size ,color=Color(c[0],c[1],c[2],1.0))

    def DrawCircle(self, center, radius, c):
        center = (numpy.array(center)-radius)
        size = numpy.array([radius*2,radius*2])
        e = Ellipse(pos=center,size=size ,color=Color(c[0],c[1],c[2],1.0))

    def DrawSegment(self,v1, v2, c):
        Line(points=[v1,v2], width=1,color=Color(c[0],c[1],c[2],1.0))
    def DrawPolygon(self,vertices, c):
        vertices = numpy.array(vertices)
        vertices[:,0] #+= self.offset[0]
        vertices[:,1] #+= self.offset[1]
        #vertices*=self.scale
        v = [] 
        indices = []
        for i in range(vertices.shape[0]):
            v.extend([vertices[i,0],vertices[i,1],0,0])
            indices.append(i)
        Mesh(vertices=v,indices=indices,mode='line_loop',color=Color(c[0],c[1],c[2],1.0))
    def DrawSolidPolygon(self,vertices, c):
        vertices = numpy.array(vertices)
        vertices[:,0] #+= self.offset[0]
        vertices[:,1] #+= self.offset[1]
        #vertices*=self.scale

        v = [] 
        indices = []
        for i in range(vertices.shape[0]):
            v.extend([vertices[i,0],vertices[i,1],0,0])
            indices.append(i)
        #with self.canvas:
        Mesh(vertices=v,indices=indices,mode='triangle_fan',color=Color(c[0],c[1],c[2],1.0))

        
    def DrawParticles(self, centers, radius, colors=None):
        nparticles = centers.shape[0]

        for p in range(nparticles):
            self.DrawSolidCircle(center=centers[p,:],radius=radius,axis=(1,0),c=(1,1,1))








    



class KivyTestbedWidget(Widget):
    def __init__(self,testbed, **kwargs):
        super(KivyTestbedWidget, self).__init__(**kwargs)
        
        # offsets and ppm
        self.ppm = 50.0
        self.offset = vec2(5.0,0.0)

        # start the example
        self.testbed = testbed
        self.example = self.testbed.exampleCls()

        # shortcut
        self.world = self.example.world

        # setup debug draw
        self.debugDraw = DrawKivy()
        self.debugDrawCaller =  b2DrawCaller(self.debugDraw,scale=self.ppm,
                                            offset=self.offset,flipY=False)

        self.debugDrawCaller.appendFlags(['shape','joint','centerOfMass','particle'])
        self.world.SetDebugDraw(self.debugDrawCaller)

        # callback to launch world step
        Clock.schedule_interval(self.step, 1.0 / 60.0)



    def step(self, dt):

        # render step
        self.canvas.clear()
        with self.canvas:
            self.world.DrawDebugData()

        # do a physical step
        self.example.step(dt)

    def on_touch_move(self, touch):
        if touch.is_mouse_scrolling:
            pass
        else:
            screenPos = touch.pos
            worldPos = self.screenToWorld(screenPos)

            with self.canvas:
                self.debugDraw.DrawSolidCircle(screenPos,2,vec2(0,1),(1,1,1,1))

            self.example.MouseMove(p=vec2(worldPos))

    def on_touch_down(self, touch):
        # will receive all motion events.
        if touch.is_mouse_scrolling:
            print touch.button
            if touch.button == 'scrolldown':
                self.zoomIn()
            else:
                self.zoomOut()
        else:
            screenPos = touch.pos
            worldPos = self.screenToWorld(screenPos)

            self.example.MouseDown(p=vec2(worldPos))

            #print "screenPos",screenPos,"worldPos",worldPos
            #aabbCallback = AABBCallback(worldPos)
            #aabbCaller = b2QueryCallbackCaller(aabbCallback)
            #box = self.aabbFromScreenPos(screenPos)
            #self.world.QueryAABB(aabbCallback, box)
            #if aabbCallback.body is not None:
            #    print "found body",aabbCallback.body


    def on_touch_up(self, touch):
        # will receive all motion events.
        if touch.is_mouse_scrolling:
            pass
        else:
            screenPos = touch.pos
            worldPos = self.screenToWorld(screenPos)
            self.example.MouseUp(p=vec2(worldPos))



    def screenToWorld(self, pos):
        pos = numpy.array(pos)
        pos /= self.ppm
        pos -= (self.offset.x,self.offset.y)
        return pos

    def zoomIn(self):
        self.ppm /= 1.2
        self.debugDrawCaller.scale = self.ppm
    def zoomOut(self):
        self.ppm *= 1.2
        self.debugDrawCaller.scale = self.ppm


class KivyTestbedGui(App):
    def __init__(self, testbed):
        super(KivyTestbedGui, self).__init__()
        self.testbed = testbed
    def build(self):
        w =  KivyTestbedWidget(testbed=self.testbed)
        #Clock.schedule_interval(w.update_world, 1.0 / 60.0)
        return w




if __name__ == '__main__':
    KivyTestbedGui().run()
