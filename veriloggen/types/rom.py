from __future__ import absolute_import
from __future__ import print_function

import math

import veriloggen.core.vtypes as vtypes
from veriloggen.core.module import Module
from veriloggen.seq.seq import Seq
from veriloggen.dataflow.dtypes import make_condition
from . import util


def mkROMDefinition(name, values, size, datawidth, sync=False):
    m = Module(name)

    clk = m.Input('CLK') if sync else None
    sel = m.Input('sel', size)
    val = m.OutputReg('val', datawidth)

    if clk is not None:
        alw = m.Always(vtypes.Posedge(clk))
    else:
        alw = m.Always()

    patterns = [vtypes.When(i)(val(v, blk=not sync)) for i, v in enumerate(values)]

    alw(
        vtypes.Case(sel)(*patterns)
    )

    return m


class _ROM(object):

    def __init__(self, m, name, clk, sel, values, datawidth=None):

        self.m = m
        self.name = name
        self.clk = clk

        size = int(math.ceil(math.log(len(values), 2)))
        self.sel = self.m.Wire(name + '_sel', size)
        self.m.Assign(self.sel(sel))

        if datawidth is None:
            datawidth = 1
            for v in values:
                w = v.bit_length()
                if w is not None and w > datawidth:
                    datawidth = w

        self.val = self.m.Wire(name + '_val', datawidth)
        sync = True if clk is not None else False
        rom_def = mkROMDefinition(name, values, size, datawidth, sync)

        ports = []
        if clk is not None:
            ports.append(self.clk)

        ports.append(self.sel)
        ports.append(self.val)

        self.m.Instance(rom_def, name, params=(), ports=ports)


class SyncROM(_ROM):

    def __init__(self, m, name, clk, sel, values, datawidth=None):
        _ROM.__init__(self, m, name, clk, sel, values, datawidth=datawidth)


class AsyncROM(_ROM):

    def __init__(self, m, name, sel, values, datawidth=None):
        _ROM.__init__(self, m, name, None, sel, values, datawidth=datawidth)
