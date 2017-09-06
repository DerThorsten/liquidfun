from ._pybox2d import b2DrawCaller
from .tools import _classExtender, GenericB2dIter

class DrawFlags(object):
    shapeBit              = 0x0001
    jointBit              = 0x0002
    aabbBit               = 0x0004
    pairBit               = 0x0008
    centerOfMassBit       = 0x0010
    particleBit           = 0x0020

DrawFlagsDict = {
    "shape"              : 0x0001,
    "joint"              : 0x0002,
    "aabb"               : 0x0004,
    "pair"               : 0x0008,
    "centerOfMass"       : 0x0010,
    "particle"           : 0x0020
}



def extendB2DrawCaller():
    
    def appendFlags(self, flagList):
        if isinstance(flagList, str):
            flagList = [flagList]
        for flag in flagList:
            self.AppendFlags(DrawFlagsDict[flag])
    b2DrawCaller.appendFlags =appendFlags

    def clearFlags(self, flagList):
        if isinstance(flagList, str):
            flagList = [flagList]
        for flag in flagList:
            self.ClearFlags(DrawFlagsDict[flag])
    b2DrawCaller.clearFlags =clearFlags



class _DrawCaller(b2DrawCaller):
    def appendFlags(self, flagList):
        if isinstance(flagList, str):
            flagList = [flagList]
        for flag in flagList:
            self.AppendFlags(DrawFlagsDict[flag])


    def clearFlags(self, flagList):
        if isinstance(flagList, str):
            flagList = [flagList]
        for flag in flagList:
            self.ClearFlags(DrawFlagsDict[flag])

_classExtender(_DrawCaller,['appendFlags','clearFlags'])


