from __future__ import absolute_import
from __future__ import print_function

import math

import veriloggen.core.vtypes as vtypes
from veriloggen.core.module import Module
from veriloggen.seq.seq import Seq
from . import util


def mkROMDefinition(name, values, size, datawidth, sync=False, with_enable=False):
    m = Module(name)

    clk = m.Input('CLK') if sync else None
    addr = m.Input('addr', size)
    if with_enable:
        enable = m.Input('enable')
    val = m.OutputReg('val', datawidth)

    if clk is not None:
        alw = m.Always(vtypes.Posedge(clk))
    else:
        alw = m.Always()

    patterns = [vtypes.When(i)(val(v, blk=not sync))
                for i, v in enumerate(values)]

    body = vtypes.Case(addr)(*patterns)

    if with_enable:
        body = vtypes.If(enable)(body)
    
    alw(
       body
    )

    return m


class _ROM(object):

    def __init__(self, m, name, clk, addr, values, enable=None, datawidth=None):

        self.m = m
        self.name = name
        self.clk = clk

        size = int(math.ceil(math.log(len(values), 2)))
        self.addr = self.m.Wire(name + '_addr', size)
        self.m.Assign(self.addr(addr))

        if datawidth is None:
            datawidth = 1
            for v in values:
                w = v.bit_length()
                if w is not None and w > datawidth:
                    datawidth = w

        with_enable = enable is not None
        if enable is not None:
            self.enable = self.m.Wire(name + '_enable')
            self.m.Assign(self.enable(enable))

        self.rdata = self.m.Wire(name + '_val', datawidth)
        sync = True if clk is not None else False
        rom_def = mkROMDefinition(name, values, size, datawidth, sync, with_enable)

        ports = []
        if clk is not None:
            ports.append(self.clk)

        ports.append(self.addr)

        if enable is not None:
            ports.append(self.enable)
        
        ports.append(self.rdata)

        self.m.Instance(rom_def, name, params=(), ports=ports)


class SyncROM(_ROM):

    def __init__(self, m, name, clk, addr, values, enable=None, datawidth=None):
        _ROM.__init__(self, m, name, clk, addr, values, enable=enable, datawidth=datawidth)


class AsyncROM(_ROM):

    def __init__(self, m, name, addr, values, enable=None, datawidth=None):
        _ROM.__init__(self, m, name, None, addr, values, enable=enable, datawidth=datawidth)
