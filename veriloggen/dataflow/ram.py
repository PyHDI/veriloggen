from __future__ import absolute_import
from __future__ import print_function

import math
import veriloggen.core.vtypes as vtypes
from veriloggen.core.module import Module


def make_port(m, _type, *args, **kwargs):
    if 'initval' in kwargs and 'Reg' not in _type:
        del kwargs['initval']
    return getattr(m, _type)(*args, **kwargs)


class RAMInterface(object):
    _I = 'Input'
    _O = 'Output'

    def __init__(self, m, name=None, datawidth=32, addrwidth=10, itype=None, otype=None,
                 p_addr='addr', p_rdata='rdata', p_wdata='wdata', p_wenable='wenable',
                 index=None):

        if itype is None:
            itype = self._I
        if otype is None:
            otype = self._O

        self.m = m

        name_addr = p_addr if name is None else '_'.join([name, p_addr])
        name_rdata = p_rdata if name is None else '_'.join([name, p_rdata])
        name_wdata = p_wdata if name is None else '_'.join([name, p_wdata])
        name_wenable = p_wenable if name is None else '_'.join(
            [name, p_wenable])

        if index is not None:
            name_addr = name_addr + str(index)
            name_rdata = name_rdata + str(index)
            name_wdata = name_wdata + str(index)
            name_wenable = name_wenable + str(index)

        self.addr = make_port(m, itype, name_addr, addrwidth, initval=0)
        self.rdata = make_port(m, otype, name_rdata, datawidth, initval=0)
        self.wdata = make_port(m, itype, name_wdata, datawidth, initval=0)
        self.wenable = make_port(m, itype, name_wenable, initval=0)


def mkRAMCore(name, datawidth=32, addrwidth=10, numports=2):
    m = Module(name)
    clk = m.Input('CLK')

    interfaces = []

    for i in range(numports):
        interface = RAMInterface(
            m, name + '_%d' % i, datawidth, addrwidth)
        interface.delay_addr = m.Reg(name + '_%d_daddr' % i, addrwidth)
        interfaces.append(interface)

    mem = m.Reg('mem', datawidth, length=2**addrwidth)

    for interface in interfaces:
        m.Always(vtypes.Posedge(clk))(
            vtypes.If(interface.wenable)(
                mem[interface.addr](interface.wdata)
            ),
            interface.delay_addr(interface.addr)
        )
        m.Assign(interface.rdata(mem[interface.delay_addr]))

    return m


def mkRAM(name, datawidth=32, addrwidth=10, numports=2):
    if numports < 1:
        raise ValueError("numports must be greater than 0.")

    name = 'dataflow_ram_%d' % index
    m = mkRAMCore(name, datawidth, addrwidth, numports)

    return m


# global multiplier count
index_count = 0


def get_RAM(datawidth=32, length=1024, numports=1):
    global index_count
    ram = mkRAM(index_count, datawidth, length, numports)
    index_count += 1
    return ram


def reset():
    global index_count
    index_count = 0
