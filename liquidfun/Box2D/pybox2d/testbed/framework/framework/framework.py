import pybox2d as b2d
from pybox2d import vec2
import time
import logging
# logging.warning('Watch out!')  # will print a message to the console
# logging.info('I told you so')  # will not print anything

from . framework_settings import *
from . framework_base     import *





class Framework(FrameworkBase):
    name = ""
    description = ""
    def __init__(self,gui,gravity=vec2(0,-9.81)):
        super(Framework, self).__init__(gui,gravity=gravity)
   



class Testbed(object):
    def __init__(self, guiType = "kivy"):
        self.guiType =guiType

        if guiType == "kivy":
            from . framework_impl.kivy_gui import KivyTestbedGui
            self.guiCls = KivyTestbedGui

        elif guiType == "pygame":
            from . pygame_gui import PyGameTestbedGui
            self.guiCls = PyGameTestbedGui
        elif guiType == "pg":
            from . pg_gui import PgTestbedGui
            self.guiCls = PgTestbedGui
        else:
            raise RuntimeError("'%s' is an unknown gui cls")

    def setExample(self, cls):
        self.exampleCls = cls

    def run(self):
        self.guiCls(testbed=self).run()
