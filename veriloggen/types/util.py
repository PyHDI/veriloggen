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


def overwrite_assign(targ, value):
    prev_assign = targ._get_assign()
    if not prev_assign:
        targ.assign(value)
    else:
        prev_assign.overwrite_right(value)
        targ.module.remove(prev_assign)
        targ.module.append(prev_assign)


def add_mux(targ, cond, value):
    prev_assign = targ._get_assign()
    if not prev_assign:
        targ.assign(vtypes.Mux(cond, value, vtypes.IntX()))
    else:
        prev_value = prev_assign.statement.right
        prev_assign.overwrite_right(
            vtypes.Mux(cond, value, prev_value))
        targ.module.remove(prev_assign)
        targ.module.append(prev_assign)


def add_enable_cond(targ, cond, value):
    prev_assign = targ._get_assign()
    if not prev_assign:
        targ.assign(vtypes.Mux(cond, value, 0))
    else:
        prev_value = prev_assign.statement.right
        prev_assign.overwrite_right(
            vtypes.Mux(cond, value, prev_value))
        targ.module.remove(prev_assign)
        targ.module.append(prev_assign)


def add_disable_cond(targ, cond, value):
    prev_assign = targ._get_assign()
    if not prev_assign:
        targ.assign(vtypes.Mux(cond, value, 1))
    else:
        prev_value = prev_assign.statement.right
        prev_assign.overwrite_right(
            vtypes.Ands(vtypes.Mux(cond, value, 1), prev_value))
        targ.module.remove(prev_assign)
        targ.module.append(prev_assign)
