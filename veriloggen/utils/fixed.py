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
        raise TypeError('fixed_to_real supports only pure signal instances.')
    
    msb = value[value.width - 1]
    
    v0 = (vtypes.SystemTask('itor', fixed_to_int(value, point)) +
          vtypes.SystemTask('itor', fixed_to_int_low(value, point)) / (2 ** point))
    
    nv = vtypes.Unot(value) + 1
    v1 = ((vtypes.SystemTask('itor', fixed_to_int(nv, point)) +
           vtypes.SystemTask('itor', fixed_to_int_low(nv, point)) / (2 ** point))) * -1
    
    return vtypes.Mux(msb == 0, v0, v1)
