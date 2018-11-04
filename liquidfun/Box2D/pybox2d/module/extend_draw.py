from . _pybox2d import b2DrawCaller
from . tools import _classExtender, GenericB2dIter

import numbers 

class DrawFlags(object):
    shape_bit              = 0x0001
    joint_bit              = 0x0002
    aabb_bit               = 0x0004
    pair_bit               = 0x0008
    center_of_mass_bit     = 0x0010
    particle_bit           = 0x0020

draw_flags_dict = {
    "shape"              : 0x0001,
    "joint"              : 0x0002,
    "aabb"               : 0x0004,
    "pair"               : 0x0008,
    "center_of_mass"     : 0x0010,
    "particle"           : 0x0020
}



def extendB2DrawCaller():
    
    def append_flags(self, flag_list):
        if isinstance(flag_list, str):
            flag_list = [flag_list]
        for flag in flag_list:
            self.append_flags(draw_flags_dict[flag])
    b2DrawCaller.append_flags =append_flags

    def clear_flags(self, flag_list):
        if isinstance(flag_list, str):
            flag_list = [flag_list]
        for flag in flag_list:
            self.clear_flags(draw_flags_dict[flag])
    b2DrawCaller.clear_flags = clear_flags



class _DrawCaller(b2DrawCaller):

    def append_flags(self, flag_list_or_int):
        if isinstance(flag_list_or_int, numbers.Number):
            self._append_flags_int(flag_list_or_int)
        else:
            flag_list = flag_list_or_int
            if isinstance(flag_list, str):
                flag_list = [flag_list]
            for flag in flag_list:
                self._append_flags_int(draw_flags_dict[flag])


    def clear_flags(self, flag_list_or_int):
        if isinstance(flag_list_or_int, numbers.Number):
            self._clear_flags_int(flag_list_or_int)
        else:
            flag_list = flag_list_or_int
            if isinstance(flag_list, str):
                flag_list = [flag_list]
            for flag in flag_list:
                self._clear_flags_int(draw_flags_dict[flag])

_classExtender(_DrawCaller,['append_flags','clear_flags'])


