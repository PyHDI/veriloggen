from __future__ import absolute_import
from __future__ import print_function

import veriloggen.types.fixed as fixed


def _intrinsic_FixedInput(fsm, m, name, width=32, point=0, signed=True):
    return fixed.FixedInput(m, name, width=width, point=point, signed=signed)


def _intrinsic_FixedOutput(fsm, m, name, width=32, point=0, signed=True):
    return fixed.FixedOutput(m, name, width=width, point=point, signed=signed)


def _intrinsic_FixedOutputReg(fsm, m, name, width=32, point=0, signed=True):
    return fixed.FixedOutputReg(m, name, width=width, point=point, signed=signed)


def _intrinsic_FixedReg(fsm, m, name, width=32, point=0, signed=True):
    return fixed.FixedReg(m, name, width=width, point=point, signed=signed)


def _intrinsic_FixedWire(fsm, m, name, width=32, point=0, signed=True):
    return fixed.FixedWire(m, name, width=width, point=point, signed=signed)


def _intrinsic_to_fixed(fsm, value, point, signed=False):
    return fixed.to_fixed(value, point, signed)


def _intrinsic_fixed_to_int(fsm, value, point, signed=False):
    return fixed.fixed_to_int(value, point, signed)


def _intrinsic_fixed_to_int_low(fsm, value, point):
    return fixed.fixed_to_int_low(value, point)


def _intrinsic_fixed_to_real(fsm, value, point, signed=False):
    return fixed.fixed_to_real(value, point, signed)
