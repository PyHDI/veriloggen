from __future__ import absolute_import
from __future__ import print_function

import veriloggen.core.vtypes as vtypes

def to_fixed(value, point):
    if isinstance(value, (int, float)):
        if not isinstance(point, int):
            raise TypeError('point field must be int')
        mag = 2 ** point
        return int(value * mag)
    return value << point

def fixed_to_int(value, point):
    if isinstance(value, (int, float)):
        if not isinstance(point, int):
            raise TypeError('point field must be int')
        mag = 2 ** point
        return float(value) / mag
    return value >> point

def fixed_to_int_low(value, point):
    if isinstance(value, (int, float)):
        if not isinstance(point, int):
            raise TypeError('point field must be int')
        mag = 2 ** point
        return (float(value) / mag) % 1.0
    return vtypes.And(value, vtypes.Repeat(vtypes.Int(1, 1), point))

def fixed_to_real(value, point):
    if not isinstance(value, vtypes._Variable):
        raise TypeError('fixed_to_real supports only _Variable .')
    
    msb = value[value.width - 1]
    
    v0 = (vtypes.SystemTask('itor', fixed_to_int(value, point)) +
          vtypes.SystemTask('itor', fixed_to_int_low(value, point)) / (2 ** point))
    
    nv = vtypes.Unot(value) + 1
    v1 = ((vtypes.SystemTask('itor', fixed_to_int(nv, point)) +
           vtypes.SystemTask('itor', fixed_to_int_low(nv, point)) / (2 ** point))) * -1
    
    return vtypes.Mux(msb == 0, v0, v1)

#-------------------------------------------------------------------------------
def adjust(left, right, lpoint, rpoint, lsigned=True, rsigned=True):
    diff_lpoint = rpoint - lpoint
    diff_rpoint = lpoint - rpoint
    if diff_lpoint < 0: diff_lpoint = 0
    if diff_rpoint < 0: diff_rpoint = 0
    ldata = left if diff_lpoint == 0 else shift_left(left, diff_lpoint, lsigned)
    rdata = right if diff_rpoint == 0 else shift_left(right, diff_rpoint, rsigned)
    return ldata, rdata
    
def shift_left(value, size, signed=True):
    if isinstance(value, vtypes.Int):
        v = value.value & 0x1
        ret = value
        for i in range(size):
            ret = (ret << 1) | v
        return ret
    
    if isinstance(value, int):
        v = value & 0x1
        ret = value
        for i in range(size):
            ret = (ret << 1) | v
        return ret
    
    if isinstance(value, bool):
        return value << size
    
    if not isinstance(value, vtypes._Variable):
        raise TypeError("shift_left not support type '%s'" % str(type(value)))
    
    if signed:
        return vtypes.Cat(value, vtypes.Repeat(value[0], size))
    
    return vtypes.Sll(value, size)

def shift_right(value, size, signed=True):
    if signed:
        return vtypes.Sra(value, size)
    
    return vtypes.Srl(value, size)
