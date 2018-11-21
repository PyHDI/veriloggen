from __future__ import absolute_import
from __future__ import print_function

import veriloggen.core.vtypes as vtypes
import veriloggen.types.fixed as fxd

__intrinsics__ = ('FixedConst', 'as_fixed',
                  'to_fixed', 'fixed_to_int',
                  'fixed_to_int_low', 'fixed_to_real')


def FixedConst(fsm, value, point=0, signed=True, raw=False):
    point = vtypes.raw_value(point)
    return fxd.FixedConst(value, point, signed, raw)


def as_fixed(fsm, value, point, signed=True):
    return fxd.as_fixed(value, point, signed)


def to_fixed(fsm, value, point, signed=True):
    return fxd.to_fixed(value, point, signed)


def fixed_to_int(fsm, value, point, signed=True):
    return fxd.fixed_to_int(value, point, signed)


def fixed_to_int_low(fsm, value, point):
    return fxd.fixed_to_int_low(value, point)


def fixed_to_real(fsm, value, point, signed=True):
    return fxd.fixed_to_real(value, point, signed)
