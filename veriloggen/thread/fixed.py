from __future__ import absolute_import
from __future__ import print_function

import veriloggen.core.vtypes as vtypes
import veriloggen.types.fixed as fxd

__intrinsics__ = ('FixedConst',
                  'cast_to_fixed', 'reinterpret_cast_to_fixed',
                  'fixed_to_int', 'fixed_to_real')


def FixedConst(fsm, value, point=0, signed=True, raw=False):
    point = vtypes.raw_value(point)
    signed = vtypes.raw_value(signed)
    raw = vtypes.raw_value(raw)

    if (isinstance(value, fxd._FixedConstant) and
            value.orig_value is not None):
        value = value.orig_value
    elif isinstance(value, fxd._FixedBase):
        value = fxd.write_adjust(value, point)
        value = vtypes.raw_value(value)
        raw = True
    elif not raw:
        value = vtypes.raw_value(value)

    if not isinstance(value, (int, bool, float)):
        raise TypeError("value must be int, bool, or float")
    if not isinstance(point, int):
        raise TypeError("point must be int")

    return fxd.FixedConst(value, point, signed, raw)


def cast_to_fixed(fsm, value, point, signed=True):
    point = vtypes.raw_value(point)
    signed = vtypes.raw_value(signed)
    cv = fxd.write_adjust(value, point)
    return fxd.reinterpret_cast_to_fixed(cv, point, signed)


def reinterpret_cast_to_fixed(fsm, value, point, signed=True):
    point = vtypes.raw_value(point)
    signed = vtypes.raw_value(signed)
    return fxd.reinterpret_cast_to_fixed(value, point, signed)


def fixed_to_int(fsm, value, point):
    point = vtypes.raw_value(point)
    return fxd.fixed_to_int(value, point)


def fixed_to_real(fsm, value, point, signed=True):
    point = vtypes.raw_value(point)
    signed = vtypes.raw_value(signed)
    return fxd.fixed_to_real(value, point, signed)
