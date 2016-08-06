import inspect
import sys

from framework import Framework,Testbed

from examples import * 
import examples



exampleClassList = []


# get all the example classes
for name, obj in inspect.getmembers(examples):
    #print "Name",name
    if inspect.ismodule(obj):
        submod = obj

        for name, objCls in inspect.getmembers(submod):
            if inspect.isclass(objCls):
                if issubclass(objCls, Framework):
                    try:
                        print objCls.name
                    except:
                        pass
                    exampleClassList.append(objCls)


if __name__ == "__main__":

    testbed = Testbed(guiType='kivy')
    testbed.setExample(exampleClassList[0])
    testbed.run()
