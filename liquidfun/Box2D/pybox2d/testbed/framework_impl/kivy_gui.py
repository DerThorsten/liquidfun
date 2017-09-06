import kivy
kivy.require('1.1.1')

from kivy.config import Config
Config.set('input', 'mouse', 'mouse,disable_multitouch')
Config.set('kivy', 'keyboard_mode', 'system')


from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.graphics import *
import numpy
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.properties import *

from pybox2d import *


class DrawKivy(DebugDraw):

    def __init__(self, scale = 5.0, offset = vec2(0,0), flipY=False):
        self.scale = scale
        self.offset = offset
        super(DrawKivy,self).__init__()


        
    def DrawSolidCircle(self, center, radius, axis, c):
        #print "circle"
        _center = (numpy.array(center)-radius)
        size = numpy.array([radius*2,radius*2])
        #print "color",color
        #with self.canvas:
        print("axis",axis)
        a = numpy.array(axis)
        a /= numpy.linalg.norm(a)
        a *= radius
        #a /= 2.0

        p0 = _center - a + radius
        p1 = _center + a + radius

        print(p0,p1,_center+radius)
        e = Ellipse(pos=_center,size=size ,color=Color(c[0],c[1],c[2],1.0))

        Line(points=[tuple(p0),tuple(p1)], width=1,color=Color(0.75*c[0],0.75*c[1],0.75*c[2],1))
        Line(circle=(center[0], center[1], radius),color=Color(0.75*c[0],0.75*c[1],0.75*c[2],1))

    def DrawCircle(self, center, radius, c):
        #e = Ellipse(pos=_center,size=size ,color=Color(c[0],c[1],c[2],1.0))
        Line(circle=(center[0], center[1], radius),color=Color(c[0],c[1],c[2],1))



    def DrawSegment(self,v1, v2, c):
        Line(points=[v1,v2], width=1,color=Color(c[0],c[1],c[2],1.0))


    def DrawPolygon(self,vertices, c):
        vertices = numpy.array(vertices)
        line = []
        for i in range(vertices.shape[0]):
            line.extend([vertices[i,0],vertices[i,1]])
        Line(points=line,width=1,color=Color(c[0],c[1],c[2],1), close=True)
        


    def DrawSolidPolygon(self,vertices, c):
        vertices = numpy.array(vertices)
        vertices[:,0] #+= self.offset[0]
        vertices[:,1] #+= self.offset[1]
        #vertices*=self.scale

        v = [] 
        indices = []
        line = []
        for i in range(vertices.shape[0]):
            v.extend([vertices[i,0],vertices[i,1],0,0])
            indices.append(i)
            line.extend([vertices[i,0],vertices[i,1]])
        Mesh(vertices=v,indices=indices,mode='triangle_fan',color=Color(c[0],c[1],c[2],1.0))
        Line(points=line,color=Color(0.75*c[0],0.75*c[1],0.75*c[2],1), close=True)
        
    def DrawParticles(self, centers, radius, colors=None):
        #nparticles = centers.shape[0]
        #pl = []
        #for i in range(nparticles):
        #    pl.append(float(centers[i,0]))
        #    pl.append(float(centers[i,1]))
        Point(points=centers.reshape(-1), pointsize=radius,color=Color(0,0,1,0.3))

        #for p in range(nparticles):
        #    self.DrawSolidCircle(center=centers[p,:],radius=radius,axis=(1,0),c=(1,1,1))








    


kv_string  = """
<KivyTestbedDrawWidget>: 
             
"""
Builder.load_string(kv_string)
class KivyTestbedDrawWidget(BoxLayout):
    ctrlWidget = ObjectProperty(None)
    def __init__(self, **kwargs):
        super(KivyTestbedDrawWidget, self).__init__(**kwargs)
        # offsets and ppm
        self.ppm = 50.0
        self.offset = vec2(5.0,0.0)
        self.targetFps = 30.0
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)

    def setTestbed(self,testbed, isPaused=False):

        # key
        #self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        #self._keyboard.bind(on_key_down=self._on_keyboard_down)

        # start the example
        self.testbed = testbed
        self.example = self.testbed.exampleCls()

        # shortcut
        self.world = self.example.world

        # setup debug draw
        self.debugDraw = DrawKivy(scale=self.ppm,offset=self.offset,flipY=False)
        self.debugDraw.appendFlags(['shape','joint','aabb','pair','centerOfMass','particle'])
        self.world.setDebugDraw(self.debugDraw)

        self.example.isPaused = isPaused
        if not isPaused:
            Clock.schedule_interval(self.step, 1.0 / self.targetFps)
        else:
            self.step(1.0/self.targetFps)
            self.step(1.0/self.targetFps)

    def unscheduleSepCallback(self):
        Clock.unschedule(self.step, all=True)
    def changeFps(self,val):
        self.targetFps = val
        if not self.example.isPaused:
            Clock.unschedule(self.step, all=True)
            Clock.schedule_interval(self.step, 1.0/float( self.targetFps))



    def playExample(self):
        if self.example.isPaused:
            self.example.isPaused = False
            self.changeFps(self.targetFps)

    def pauseExample(self):
        if not self.example.isPaused:
            self.example.isPaused = True
            self.unscheduleSepCallback()

    def stepExample(self):
        if self.example.isPaused:
            self.step(1.0/float( self.targetFps))




    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None
    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        print(keycode,text,modifiers)

        if 'ctrl' in modifiers:
            n = keycode[1]
            o = None
            if n == 'left':
                o = vec2(-0.025*self.ppm,0)
            if n == 'right':
                o = vec2(0.025*self.ppm,0)
            if n == 'up':
                o = vec2(0,0.025*self.ppm)
            if n == 'down':
                o = vec2(0,-0.025*self.ppm)
            if o is not None:
                self.offset = self.offset + o
                self.debugDraw.offset = self.offset
    def step(self, dt):
        self.ctrlWidget.efps = 1.0/dt
        # render step
        self.canvas.clear()
        with self.canvas:
            PushMatrix()
            Translate(self.offset[0], self.offset[1])
            Scale(self.ppm)
            self.world.drawDebugData()
            PopMatrix()
        # do a physical step
        self.example.step(dt)



    def on_touch_move(self, touch):
        if touch.is_mouse_scrolling:
            pass
        else:
            screenPos = touch.pos
            if self.example.mouseJoint is not None:
                worldPos = self.screenToWorld(screenPos)
                self.example.MouseMove(p=vec2(worldPos))
            else:
                offset = touch.dpos
                if offset is not None:
                    self.offset  = self.offset + vec2(offset)
    def on_touch_down(self, touch):
        # will receive all motion events.
        if touch.is_mouse_scrolling:
            print(touch.button)
            if touch.button == 'scrolldown':
                self.zoomIn()
            else:
                self.zoomOut()
        else:
            screenPos = touch.pos
            worldPos = self.screenToWorld(screenPos)

            self.example.MouseDown(p=vec2(worldPos))


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
        pos -= (self.offset.x,self.offset.y)
        pos /= self.ppm
        
        return pos

    def zoomIn(self):
        self.ppm /= 1.2
        self.debugDraw.scale = self.ppm
    def zoomOut(self):
        self.ppm *= 1.2
        self.debugDraw.scale = self.ppm



kv_string  = """<KivyTestbedCtrlWidget>:
    spacing: 30
    orientation: 'vertical'
    fpsLabel: fpsLabel
    fpsSlider: fpsSlider
    buttonPlay: buttonPlay
    buttonStep: buttonStep
    buttonPause: buttonPause
    BoxLayout:
        size_hint: 1,0.6
        orientation: 'vertical'
        
             
        
        BoxLayout:
            orientation: 'horizontal'
            Label: 
                size_hint: 0.15,1
                text: 'FPS'
            Label: 
                size_hint: 0.15,1
                text: str(int(root.efps+0.5))
            Label:
                size_hint: 0.15,1
                text: str(int(fpsSlider.value))
                id: fpsLabel
            Slider:
                size_hint: 0.5,1
                range: 1,100
                value: 30
                id: fpsSlider
                on_value: root.testbedWidget.changeFps(fpsSlider.value)
        
        BoxLayout:
            orientation: 'horizontal'
            Label: 
                text: 'DrawShapes'
            CheckBox:
                active: True
                on_state: root.testbedWidget.changeDrawBit('shape', self.state)
        BoxLayout:
            orientation: 'horizontal'
            Label:
                text: 'DrawJoint'
            CheckBox:
                active: True
                on_state: root.testbedWidget.changeDrawBit('joint', self.state)
        BoxLayout:
            orientation: 'horizontal'
            Label: 
                text: 'DrawAABB'
            CheckBox:
                active: True
                on_state: root.testbedWidget.changeDrawBit('aabb', self.state)
        BoxLayout:
            orientation: 'horizontal'
            Label: 
                text: 'DrawPair'
            CheckBox:
                active: True
                on_state: root.testbedWidget.changeDrawBit('pair', self.state)
        BoxLayout:
            orientation: 'horizontal'
            Label: 
                text: 'DrawCenterOfMass'
            CheckBox:
                active: True
                on_state: root.testbedWidget.changeDrawBit('centerOfMass', self.state)
        BoxLayout:
            orientation: 'horizontal'
            Label: 
                text: 'DrawParticles'
            CheckBox:
                active: True
                on_state: root.testbedWidget.changeDrawBit('particle', self.state)
    
    BoxLayout:
        orientation: 'vertical'
    
        BoxLayout:
            size_hint: 1,0.8
            orientation: 'horizontal'
            Button:
                text: "Play"
                id: buttonPlay
                disabled: True
                on_press: root.testbedWidget.playExample()
            Button:
                text: "Pause"   
                id: buttonPause
                disabled: False
                on_press: root.testbedWidget.pauseExample()
            Button:
                text: "Step"
                id: buttonStep
                disabled: True
                on_press: root.testbedWidget.stepExample()
        Button:
            size_hint: 1,0.2
            text: "Reset"
            on_press: root.testbedWidget.resetExample()
"""

Builder.load_string(kv_string)
class KivyTestbedCtrlWidget(BoxLayout):
    testbedWidget = ObjectProperty(None)
    drawWidget = ObjectProperty(None)

    buttonPlay = ObjectProperty(None)
    buttonPause = ObjectProperty(None)
    buttonStep = ObjectProperty(None)

    efps = NumericProperty(30)

kv_string  = """<KivyTestbedWidget>:
    ctrlWidget: ctrlWidget.__self__
    drawWidget: drawWidget.__self__
    KivyTestbedCtrlWidget:
        id: ctrlWidget
        size_hint: 0.3,1
        testbedWidget: root
        drawWidget: drawWidget
    StencilView:
        KivyTestbedDrawWidget:
            id: drawWidget
            ctrlWidget:ctrlWidget
            
"""
Builder.load_string(kv_string)
class KivyTestbedWidget(BoxLayout):

    ctrlWidget = ObjectProperty(None)
    drawWidget = ObjectProperty(None)
    testbed = ObjectProperty(None)

    def __init__(self, testbed, **kwargs):
        super(KivyTestbedWidget, self).__init__(**kwargs)
        self.testbed = testbed
        self.isPaused = False
    def setTestbed(self, testbed):
        self.drawWidget.setTestbed(testbed)

    def resetExample(self):
        self.drawWidget.unscheduleSepCallback()
        self.drawWidget.example
        self.drawWidget.setTestbed(self.testbed, isPaused=self.isPaused)

    def changeFps(self,val):
        self.drawWidget.changeFps(val)
    
    def changeDrawBit(self, name, value):
        print(name,value)
        if value == 'down':
            self.drawWidget.debugDraw.appendFlags(name)
        else:
            self.drawWidget.debugDraw.clearFlags(name)

    def playExample(self):
        assert self.isPaused
        self.isPaused = False
        self.ctrlWidget.buttonPause.disabled = False
        self.ctrlWidget.buttonPlay.disabled = True
        self.ctrlWidget.buttonStep.disabled = True
        self.drawWidget.playExample()
    def pauseExample(self):
        assert not self.isPaused 
        self.isPaused = True
        self.ctrlWidget.buttonPause.disabled = True
        self.ctrlWidget.buttonPlay.disabled = False
        self.ctrlWidget.buttonStep.disabled = False
        self.drawWidget.pauseExample()
    def stepExample(self):
        assert self.isPaused
        self.drawWidget.stepExample()

class KivyTestbedGui(App):
    def __init__(self, testbed):
        super(KivyTestbedGui, self).__init__()
        self.testbed = testbed
    def build(self):
        w =  KivyTestbedWidget(testbed=self.testbed)#testbed=self.testbed)
        w.setTestbed(self.testbed)
        #Clock.scedule_interval(w.update_world, 1.0 / 60.0)
        return w

    # def run(self):
    #     self.w.setTestbed(self.testbed)
    #     super(KivyTestbedGui,self).run()




if __name__ == '__main__':
    pass
