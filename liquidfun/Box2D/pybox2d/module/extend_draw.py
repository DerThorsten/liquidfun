from pybox2d import b2DrawCaller

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
        for flag in flagList:
            self.AppendFlags(DrawFlagsDict[flag])
    b2DrawCaller.appendFlags =appendFlags
    
extendB2DrawCaller()
del extendB2DrawCaller
