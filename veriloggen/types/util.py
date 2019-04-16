from __future__ import absolute_import
from __future__ import print_function

import math

import veriloggen.core.vtypes as vtypes
import veriloggen.seq.seq as seq

t_Input = 'Input'
t_Output = 'Output'
t_Wire = 'Wire'
t_Reg = 'Reg'
t_OutputReg = 'OutputReg'


def swap_type(cls):
    return cls._O, cls._I


def make_port(m, _type, *args, **kwargs):
    if 'no_reg' in kwargs and kwargs['no_reg']:
        _type = _type.replace('Reg', '')
        if len(_type) == 0:
            _type = 'Wire'

    if 'no_reg' in kwargs:
        del kwargs['no_reg']

    if 'initval' in kwargs and 'Reg' not in _type:
        del kwargs['initval']

    return getattr(m, _type)(*args, **kwargs)


def connect_port(left, right):
    if isinstance(left, vtypes.Reg):
        wire_left = left.module.TmpWireLike(left)
        wire_left.assign(right)
        left.module.Always()(left(wire_left, blk=True))
    else:
        left.assign(right)


def log2(value, maxsize=32):
    if isinstance(value, (int, bool, float)):
        return int(math.ceil(math.log(value, 2)))

    patterns = []
    for i in range(1, maxsize):
        patterns.append((value < 2 ** i, i))
    return vtypes.PatternMux(patterns)
