from __future__ import absolute_import
from __future__ import print_function

import veriloggen.core.vtypes as vtypes
import copy


def add(left, right, width=8, max=None, min=None):
    raw_val = left + right
    return _add(raw_val, left, right, width, max, min)


def sub(left, right, width=8, max=None, min=None):
    raw_val = left - right
    return _sub(raw_val, left, right, width, max, min)


def to_saturate(value, width=8, max=None, min=None, signed=False):
    value = _saturate_op(value, width, max, min, signed)
    return _saturate_single(value, width, max, min, signed)


def _saturate_op(value, width=8, max=None, min=None, signed=False):
    if hasattr(value, 'saturated') and value.saturated:
        return value

    if isinstance(value, vtypes.Plus):
        new_val = copy.deepcopy(value)
        new_val.left = _saturate_op(value.left, width=width, max=max, min=min)
        new_val.right = _saturate_op(value.right,
                                     width=width, max=max, min=min)
        ret = _add(new_val, new_val.left, new_val.right,
                   width=width, max=max, min=min)
        ret.saturated = True
        return ret

    if isinstance(value, vtypes.Minus):
        new_val = copy.deepcopy(value)
        new_val.left = _saturate_op(value.left, width, max)
        new_val.right = _saturate_op(value.right, width, max)
        ret = _sub(new_val, new_val.left, new_val.right,
                   width=width, max=max, min=min)
        ret.saturated = True
        return ret

    return value


def _saturate_single(value, width=8, max=None, min=None, signed=False):
    if hasattr(value, 'saturated') and value.saturated:
        return value

    if (signed or
            (isinstance(value, (int, float, bool)) and value < 0)):

        if not isinstance(value, int) and isinstance(min, int):
            min = vtypes.Int(min, signed=True)

        cond = value < min
        sat_val = _saturate_both(value, cond,
                                 width=width, max=max, min=min, signed=signed)
    else:
        sat_val = _saturate_overflow(value,
                                     width=width, max=max, signed=signed)

    try:
        sat_val.saturated = True
    except:
        pass

    return sat_val


def write(dst, value, blk=False, ldelay=None, rdelay=None, method='write'):
    width = vtypes.get_width(dst)
    signed = vtypes.get_signed(dst)

    if signed:
        max = _pow2(width - 1) - 1
        min = _pow2(width - 1) * (-1)
    else:
        max = _pow2(width) - 1
        min = 0

    sat_val = to_saturate(value, width=width, max=max, min=min, signed=signed)

    return getattr(dst, method)(sat_val, blk=blk, ldelay=ldelay, rdelay=rdelay)


def _add(raw_val, left, right, width=8, max=None, min=None):
    signed = vtypes.get_signed(raw_val)
    if min is None:
        min = _min(width, signed)

    if signed:
        cond = left < - right + min
        return _saturate_both(raw_val, cond,
                              width=width, max=max, min=min, signed=signed)

    return _saturate_overflow(raw_val, width=width, max=max, signed=signed)


def _sub(raw_val, left, right, width=8, max=None, min=None):
    signed = vtypes.get_signed(raw_val)
    if min is None:
        min = _min(width, signed)

    cond = left < right + min
    if signed:
        return _saturate_both(raw_val, cond,
                              width=width, max=max, min=min, signed=signed)

    return _saturate_underflow(raw_val, cond,
                               width=width, min=min, signed=signed)


def _saturate_overflow(raw_val, width=8, max=None, signed=False):
    if max is None:
        max = _max(width, signed)

    if (isinstance(max, int) and
            not isinstance(raw_val, int) and vtypes.get_signed(raw_val)):
        max = vtypes.Int(max, signed=True)

    return vtypes.Mux(raw_val > max, max, raw_val)


def _saturate_underflow(raw_val, cond, width=8, min=None, signed=False):
    if min is None:
        min = _min(width, signed)

    return vtypes.Mux(cond, min, raw_val)


def _saturate_both(raw_val, cond, width=8, max=None, min=None, signed=False):
    if max is None:
        max = _max(width, signed)

    if min is None:
        min = _min(width, signed)

    if (isinstance(max, int) and
            not isinstance(raw_val, int) and vtypes.get_signed(raw_val)):
        max = vtypes.Int(max, signed=True)

    return vtypes.Mux(cond, min, vtypes.Mux(raw_val > max, max, raw_val))


def _pow2(p):
    if isinstance(p, int):
        return 2 ** p

    return vtypes.Int(2, signed=True) ** p


def _max(width, signed=False):
    if signed:
        return _pow2(width - 1) - 1
    return _pow2(width) - 1


def _min(width, signed=False):
    if signed:
        return _pow2(width - 1) * (-1)
    return 0
