from __future__ import absolute_import
from __future__ import print_function

import veriloggen.core.vtypes as vtypes
import veriloggen.types.fixed as fixed


def _intrinsic_FixedConst(fsm, value, point=0, signed=True, raw=False):
    point = vtypes.raw_value(point)
    return fixed.FixedConst(value, point, signed, raw)


def _intrinsic_to_fixed(fsm, value, point, signed=False):
    return fixed.to_fixed(value, point, signed)


def _intrinsic_fixed_to_int(fsm, value, point, signed=False):
    return fixed.fixed_to_int(value, point, signed)


def _intrinsic_fixed_to_int_low(fsm, value, point):
    return fixed.fixed_to_int_low(value, point)


def _intrinsic_fixed_to_real(fsm, value, point, signed=False):
    return fixed.fixed_to_real(value, point, signed)
