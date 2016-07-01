from __future__ import absolute_import
from __future__ import print_function

import veriloggen.core.vtypes as vtypes

t_Input = 'Input'
t_Output = 'Output'
t_Wire = 'Wire'
t_Reg = 'Reg'
t_OutputReg = 'OutputReg'

def swap_type(cls):
    return cls._O, cls._I

def make_port(m, _type, *args, **kwargs):
    if 'initval' in kwargs and 'Reg' not in _type:
        del kwargs['initval']
    return getattr(m, _type)(*args, **kwargs)

def connect_port(left, right):
    if isinstance(left, vtypes.Reg):
        left.module.Always()( left(right, blk=True) )
    else:
        left.assign(right)
