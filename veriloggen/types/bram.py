from __future__ import absolute_import
from __future__ import print_function

import veriloggen.core.vtypes as vtypes
import veriloggen.core.module as module
from veriloggen.seq.seq import Seq
from . import util


class BramInterface(object):
    _I = 'Reg'
    _O = 'Wire'

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

        self.addr = util.make_port(m, itype, name_addr, addrwidth, initval=0)
        self.rdata = util.make_port(m, otype, name_rdata, datawidth, initval=0)
        self.wdata = util.make_port(m, itype, name_wdata, datawidth, initval=0)
        self.wenable = util.make_port(m, itype, name_wenable, initval=0)

    def connect(self, targ):
        util.connect_port(self.addr, targ.addr)
        util.connect_port(targ.rdata, self.rdata)
        util.connect_port(self.wdata, targ.wdata)
        util.connect_port(self.wenable, targ.wenable)


class BramSlaveInterface(BramInterface):
    _I = 'Input'
    _O = 'Output'


class BramMasterInterface(BramInterface):
    _I = 'Output'
    _O = 'Input'


#-------------------------------------------------------------------------
def mkBramDefinition(name, datawidth=32, addrwidth=10, numports=2):
    m = module.Module(name)
    clk = m.Input('CLK')

    interfaces = []

    for i in range(numports):
        interface = BramSlaveInterface(
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


#-------------------------------------------------------------------------
class Bram(object):

    def __init__(self, m, name, clk, rst, datawidth=32, addrwidth=10, numports=2):
        self.m = m
        self.name = name
        self.clk = clk
        self.rst = rst
        self.datawidth = datawidth
        self.addrwidth = addrwidth
        self.interfaces = [BramInterface(m, name + '_%d' % i, datawidth, addrwidth)
                           for i in range(numports)]

        self.definition = mkBramDefinition(
            name, datawidth, addrwidth, numports)
        self.inst = self.m.Instance(self.definition, 'inst_' + name,
                                    ports=m.connect_ports(self.definition))

        self.seq = Seq(m, name, clk, rst)
        #self.m.add_hook(self.seq.make_always)

        self._write_disabled = [False for i in range(numports)]

    def __getitem__(self, index):
        return self.interfaces[index]

    def disable_write(self, port):
        self.seq(
            self.interfaces[port].wdata(0),
            self.interfaces[port].wenable(0)
        )
        self._write_disabled[port] = True

    def write(self, port, addr, wdata, cond=None, delay=0):
        """ Write operation """
        if self._write_disabled[port]:
            raise TypeError('Write disabled.')

        if cond is not None:
            self.seq.If(cond)

        current_delay = self.seq.current_delay

        self.seq.Delay(current_delay + delay).EagerVal()(
            self.interfaces[port].addr(addr),
            self.interfaces[port].wdata(wdata),
            self.interfaces[port].wenable(1)
        )

        self.seq.Then().Delay(current_delay + delay + 1)(
            self.interfaces[port].wenable(0)
        )

    def read(self, port, addr, cond=None, delay=0):
        """ Read operation """
        if cond is not None:
            self.seq.If(cond)

        current_delay = self.seq.current_delay

        self.seq.Delay(current_delay + delay).EagerVal()(
            self.interfaces[port].addr(addr)
        )

        rdata = self.interfaces[port].rdata
        rvalid = self.m.TmpReg(initval=0)
        self.seq.Then().Delay(current_delay + delay + 1)(
            rvalid(1)
        )
        self.seq.Then().Delay(current_delay + delay + 2)(
            rvalid(0)
        )

        return rdata, rvalid
