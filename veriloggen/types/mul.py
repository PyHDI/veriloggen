from __future__ import absolute_import
from __future__ import print_function

import veriloggen.core.vtypes as vtypes
import veriloggen.core.module as module


def mkMultiplierCore(name, lsigned=True, rsigned=True, depth=6, with_update=True):

    m = module.Module(name + '_core')

    lwidth = m.Parameter('lwidth', 32)
    rwidth = m.Parameter('rwidth', 32)
    retwidth = lwidth + rwidth

    clk = m.Input('CLK')

    if with_update:
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

    body = (_a(a),
            _b(b),
            _pipe_mul[0](_mul),
            [_pipe_mul[i](_pipe_mul[i - 1]) for i in range(1, depth - 1)])

    if with_update:
        body = vtypes.If(update)(body)

    m.Always(vtypes.Posedge(clk))(body)

    return m


def mkMultiplier(name, lsigned=True, rsigned=True, depth=6,
                 with_update=True, with_enable=True):

    mult = mkMultiplierCore(name, lsigned, rsigned, depth, with_update)

    m = module.Module(name)

    lwidth = m.Parameter('lwidth', 32)
    rwidth = m.Parameter('rwidth', 32)
    retwidth = lwidth + rwidth

    clk = m.Input('CLK')
    rst = m.Input('RST')

    if with_update:
        update = m.Input('update')

    if with_enable:
        enable = m.Input('enable')
    else:
        enable = 1

    if with_enable:
        valid = m.Output('valid')

    a = m.Input('a', lwidth)
    b = m.Input('b', rwidth)
    c = m.Output('c', retwidth)

    if with_enable:
        valid_reg = [m.Reg('valid_reg%d' % i) for i in range(depth)]

        m.Assign(valid(valid_reg[depth - 1]))

        body = (valid_reg[0](enable),
                [valid_reg[i](valid_reg[i - 1]) for i in range(1, depth)])

        if with_update:
            body = vtypes.If(update)(body)

        m.Always(vtypes.Posedge(clk))(
            vtypes.If(rst)(
                [valid_reg[i](0) for i in range(depth)]
            ).Else(
                body
            ))

    params = [('lwidth', lwidth), ('rwidth', rwidth)]

    ports = [('CLK', clk)]
    if with_update:
        ports.append(('update', update))

    ports.extend([('a', a), ('b', b), ('c', c)])

    m.Instance(mult, 'mult', params=params, ports=ports)

    return m


class Multiplier(object):

    def __init__(self, m, name, clk, rst, left, right, enable=None, update=None,
                 lwidth=None, rwidth=None, lsigned=True, rsigned=True, depth=6):

        if lwidth is None:
            lwidth = vtypes.get_width(left)
        if lwidth is None:
            lwidth = 1

        if rwidth is None:
            rwidth = vtypes.get_width(right)
        if rwidth is None:
            rwidth = 1

        retwidth = lwidth + rwidth

        with_enable = True if enable is not None else False
        with_update = True if update is not None else False

        self.m = m
        self.name = name
        self.clk = clk
        self.rst = rst

        self.enable = enable
        self.update = update

        if with_enable:
            self.valid = self.m.Wire(name + '_valid')

        self.left = left
        self.right = right
        self.value = self.m.Wire(name + '_value', retwidth)

        mul_def = mkMultiplier(name, lsigned, rsigned, depth,
                               with_update, with_enable)

        params = [('lwidth', lwidth), ('rwidth', rwidth)]

        ports = []
        ports.append(self.clk)
        ports.append(self.rst)

        if with_update:
            ports.append(self.update)

        if with_enable:
            ports.append(self.enable)
            ports.append(self.valid)

        ports.append(self.left)
        ports.append(self.right)
        ports.append(self.value)

        self.m.Instance(mul_def, name, params=params, ports=ports)
