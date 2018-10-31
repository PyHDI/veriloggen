from __future__ import absolute_import
from __future__ import print_function

import copy
import veriloggen.core.vtypes as vtypes
from veriloggen.core.module import Module
from . import util


def mkRAMDefinition(name, datawidth=32, addrwidth=10, numports=2,
                    initvals=None, sync=True, with_enable=False):
    m = Module(name)
    clk = m.Input('CLK')

    interfaces = []

    for i in range(numports):
        interface = RAMSlaveInterface(
            m, name + '_%d' % i, datawidth, addrwidth, with_enable=with_enable)
        if sync:
            interface.delay_addr = m.Reg(name + '_%d_daddr' % i, addrwidth)

        interfaces.append(interface)

    mem = m.Reg('mem', datawidth, length=2**addrwidth)

    if initvals is not None:
        if not isinstance(initvals, (tuple, list)):
            raise TypeError("initvals must be tuple or list, not '%s" %
                            str(type(initvals)))

        new_initvals = []
        base = 16
        for initval in initvals:
            if isinstance(initval, int):
                new_initvals.append(vtypes.Int(initval, datawidth, base=16))
            elif isinstance(initval, vtypes.Int) and isinstance(initval.value, int):
                v = copy.deepcopy(initval)
                v.width = datawidth
                v.base = base
                new_initvals.append(v)
            elif isinstance(initval, vtypes.Int) and isinstance(initval.value, str):
                v = copy.deepcopy(initval)
                v.width = datawidth
                if v.base != 2 and v.base != 16:
                    raise ValueError('base must be 2 or 16')
                base = v.base
                new_initvals.append(v)
            else:
                raise TypeError("values of initvals must be int, not '%s" %
                                str(type(initval)))

        initvals = new_initvals

        if 2 ** addrwidth > len(initvals):
            initvals.extend(
                [vtypes.Int(0, datawidth, base=base)
                 for _ in range(2 ** addrwidth - len(initvals))])

        m.Initial(
            *[mem[i](initval) for i, initval in enumerate(initvals)]
        )

    for interface in interfaces:
        body = [
            vtypes.If(interface.wenable)(
                mem[interface.addr](interface.wdata)
            )]

        if sync:
            body.append(interface.delay_addr(interface.addr))

        if with_enable:
            body = vtypes.If(interface.enable)(*body)

        m.Always(vtypes.Posedge(clk))(
            body
        )

        if sync:
            m.Assign(interface.rdata(mem[interface.delay_addr]))
        else:
            m.Assign(interface.rdata(mem[interface.addr]))

    return m


class RAMInterface(object):
    _I = 'Reg'
    _O = 'Wire'

    def __init__(self, m, name=None, datawidth=32, addrwidth=10,
                 itype=None, otype=None,
                 p_addr='addr', p_rdata='rdata',
                 p_wdata='wdata', p_wenable='wenable',
                 p_enable='enable',
                 with_enable=False, index=None):

        if itype is None:
            itype = self._I
        if otype is None:
            otype = self._O

        self.m = m

        name_addr = p_addr if name is None else '_'.join([name, p_addr])
        name_rdata = p_rdata if name is None else '_'.join([name, p_rdata])
        name_wdata = p_wdata if name is None else '_'.join([name, p_wdata])
        name_wenable = (
            p_wenable if name is None else '_'.join([name, p_wenable]))
        if with_enable:
            name_enable = (
                p_enable if name is None else '_'.join([name, p_enable]))

        if index is not None:
            name_addr = name_addr + str(index)
            name_rdata = name_rdata + str(index)
            name_wdata = name_wdata + str(index)
            name_wenable = name_wenable + str(index)
            if with_enable:
                name_enable = name_enable + str(index)

        self.addr = util.make_port(m, itype, name_addr, addrwidth, initval=0)
        self.rdata = util.make_port(m, otype, name_rdata, datawidth, initval=0)
        self.wdata = util.make_port(m, itype, name_wdata, datawidth, initval=0)
        self.wenable = util.make_port(m, itype, name_wenable, initval=0)
        if with_enable:
            self.enable = util.make_port(m, itype, name_enable, initval=0)

    def connect(self, targ):
        self.addr.connect(targ.addr)
        targ.rdata.connect(self.rdata)
        self.wdata.connect(targ.wdata)
        self.wenable.connect(targ.wenable)
        if hasattr(self, 'enable'):
            if hasattr(targ, 'enable'):
                self.enable.connect(targ.enable)
            else:
                self.enable.connect(1)
        else:
            if hasattr(targ, 'enable'):
                raise ValueError('no enable port')


class RAMSlaveInterface(RAMInterface):
    _I = 'Input'
    _O = 'Output'


class RAMMasterInterface(RAMInterface):
    _I = 'Output'
    _O = 'Input'


class _RAM_RTL(object):

    def __init__(self, m, name, clk,
                 datawidth=32, addrwidth=10, numports=1,
                 initvals=None, sync=True, with_enable=False):

        self.m = m
        self.name = name
        self.clk = clk
        self.with_enable = with_enable

        self.interfaces = [RAMInterface(m, name + '_%d' % i, datawidth, addrwidth,
                                        itype='Wire', otype='Wire', with_enable=with_enable)
                           for i in range(numports)]

        ram_def = mkRAMDefinition(name, datawidth, addrwidth, numports,
                                  initvals, sync, with_enable)

        self.m.Instance(ram_def, name,
                        params=(), ports=m.connect_ports(ram_def))

    def connect(self, port, addr, wdata, wenable, enable=None):
        self.m.Assign(self.interfaces[port].addr(addr))
        self.m.Assign(self.interfaces[port].wdata(wdata))
        self.m.Assign(self.interfaces[port].wenable(wenable))
        if self.with_enable:
            self.m.Assign(self.interfaces[port].enable(enable))

    def rdata(self, port):
        return self.interfaces[port].rdata


class SyncRAM(_RAM_RTL):

    def __init__(self, m, name, clk,
                 datawidth=32, addrwidth=10, numports=1,
                 initvals=None, with_enable=False):
        _RAM_RTL.__init__(self, m, name, clk,
                          datawidth, addrwidth, numports,
                          initvals, sync=True, with_enable=with_enable)


class AsyncRAM(_RAM_RTL):

    def __init__(self, m, name, clk,
                 datawidth=32, addrwidth=10, numports=1,
                 initvals=None, with_enable=False):
        _RAM_RTL.__init__(self, m, name, clk,
                          datawidth, addrwidth, numports,
                          initvals, sync=False)
