from __future__ import absolute_import
from __future__ import print_function

import veriloggen.core.vtypes as vtypes
import veriloggen.core.module as module


def mkMultiplierCore(index, lwidth=32, rwidth=32, lsigned=True, rsigned=True, depth=6):
    retwidth = lwidth + rwidth

    m = module.Module('multiplier_core_%d' % index)

    clk = m.Input('CLK')
    update = m.Input('update')

    a = m.Input('a', lwidth)
    b = m.Input('b', rwidth)
    c = m.Output('c', retwidth)

    _a = m.Reg('_a', lwidth, signed=lsigned)
    _b = m.Reg('_b', rwidth, signed=rsigned)
    _mul = m.Wire('_mul', retwidth, signed=True)
    _pipe_mul = [m.Reg('_pipe_mul%d' % i, retwidth, signed=True)
                 for i in range(depth - 1)]

    __a = _a
    __b = _b
    if not lsigned:
        __a = vtypes.SystemTask(
            'signed', vtypes.Cat(vtypes.Int(0, width=1), _a))
    if not rsigned:
        __b = vtypes.SystemTask(
            'signed', vtypes.Cat(vtypes.Int(0, width=1), _b))

    m.Assign(_mul(__a * __b))
    m.Assign(c(_pipe_mul[depth - 2]))

    m.Always(vtypes.Posedge(clk))(
        vtypes.If(update)(
            _a(a),
            _b(b),
            _pipe_mul[0](_mul),
            [_pipe_mul[i](_pipe_mul[i - 1]) for i in range(1, depth - 1)]
        ))

    return m


def mkMultiplier(index, lwidth=32, rwidth=32, lsigned=True, rsigned=True, depth=6):
    if lwidth < 0:
        raise ValueError("data width must be greater than 0.")
    if rwidth < 0:
        raise ValueError("data width must be greater than 0.")
    if depth < 2:
        raise ValueError("depth must be greater than 2.")

    retwidth = lwidth + rwidth

    mult = mkMultiplierCore(index, lwidth, rwidth, lsigned, rsigned, depth)

    m = module.Module('multiplier_%d' % index)

    clk = m.Input('CLK')
    update = m.Input('update')
    a = m.Input('a', lwidth)
    b = m.Input('b', rwidth)
    c = m.Output('c', retwidth)

    ports = [('CLK', clk), ('update', update), ('a', a), ('b', b), ('c', c)]
    m.Instance(mult, 'mult', ports=ports)

    return m


# global multiplier count
index_count = 0


def get_mul(lwidth=32, rwidth=32, lsigned=True, rsigned=True, depth=6):
    global index_count
    mul = mkMultiplier(index_count, lwidth, rwidth, lsigned, rsigned, depth)
    index_count += 1
    return mul


def reset():
    global index_count
    index_count = 0
