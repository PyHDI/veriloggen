from __future__ import absolute_import
from __future__ import print_function

import veriloggen.core.vtypes as vtypes
import veriloggen.core.module as module


def mkMaddCore(index, awidth=32, bwidth=32, cwidth=32,
               asigned=True, bsigned=True, csigned=True, depth=6):

    retwidth = max(awidth + bwidth, cwidth)

    m = module.Module('madd_core_%d' % index)

    clk = m.Input('CLK')
    update = m.Input('update')

    a = m.Input('a', awidth)
    b = m.Input('b', bwidth)
    c = m.Input('c', cwidth)
    d = m.Output('d', retwidth)

    _a = m.Reg('_a', awidth, signed=asigned)
    _b = m.Reg('_b', bwidth, signed=bsigned)
    _c = m.Reg('_c', cwidth, signed=csigned)
    _mul = m.Wire('_mul', retwidth, signed=True)
    _madd = m.Wire('_madd', retwidth, signed=True)
    _pipe_madd = [m.Reg('_pipe_madd%d' % i, retwidth, signed=True)
                  for i in range(depth - 1)]

    __a = _a
    __b = _b
    __c = _c
    if not asigned:
        __a = vtypes.SystemTask(
            'signed', vtypes.Cat(vtypes.Int(0, width=1), _a))
    if not bsigned:
        __b = vtypes.SystemTask(
            'signed', vtypes.Cat(vtypes.Int(0, width=1), _b))
    if not csigned:
        __c = vtypes.SystemTask(
            'signed', vtypes.Cat(vtypes.Int(0, width=1), _c))

    m.Assign(_mul(__a * __b))
    m.Assign(_madd(_mul + __c))
    m.Assign(d(_pipe_madd[depth - 2]))

    m.Always(vtypes.Posedge(clk))(
        vtypes.If(update)(
            _a(a),
            _b(b),
            _c(c),
            _pipe_madd[0](_madd),
            [_pipe_madd[i](_pipe_madd[i - 1]) for i in range(1, depth - 1)]
        ))

    return m


def mkMadd(index, awidth=32, bwidth=32, cwidth=32,
           asigned=True, bsigned=True, csigned=True, depth=6):

    if awidth < 0:
        raise ValueError("data width must be greater than 0.")
    if bwidth < 0:
        raise ValueError("data width must be greater than 0.")
    if cwidth < 0:
        raise ValueError("data width must be greater than 0.")
    if depth < 2:
        raise ValueError("depth must be greater than 2.")

    retwidth = max(awidth + bwidth, cwidth)

    madd = mkMaddCore(index, awidth, bwidth, cwidth,
                      asigned, bsigned, csigned, depth)

    m = module.Module('madd_%d' % index)

    clk = m.Input('CLK')
    update = m.Input('update')
    a = m.Input('a', awidth)
    b = m.Input('b', bwidth)
    c = m.Input('c', cwidth)
    d = m.Output('d', retwidth)

    ports = [('CLK', clk), ('update', update),
             ('a', a), ('b', b), ('c', c), ('d', d)]
    m.Instance(madd, 'madd', ports=ports)

    return m


# global madd count
index_count = 0


def get_madd(awidth=32, bwidth=32, cwidth=32,
             asigned=True, bsigned=True, csigned=True, depth=6):

    global index_count
    madd = mkMadd(index_count, awidth, bwidth, cwidth,
                  asigned, bsigned, csigned, depth)
    index_count += 1
    return madd


def reset():
    global index_count
    index_count = 0
