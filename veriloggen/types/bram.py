from __future__ import absolute_import
from __future__ import print_function

import veriloggen.core.vtypes as vtypes
import veriloggen.core.module as module
import veriloggen.dataflow as dataflow
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
        # self.m.add_hook(self.seq.make_always)

        self.counters = []
        self.next_address = {}

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

    def write_request(self, addr, length=1, cond=None, counter=None):
        return self._request(addr, length, cond, counter)

    def write_dataflow(self, port, data, counter=None, cond=None):
        if self._write_disabled[port]:
            raise TypeError('Write disabled.')

        if self.seq.current_delay > 0:
            raise ValueError("Delayed control is not supported.")

        if counter is None:
            counter = self.counters[-1]

        naddr = self.next_address[counter]

        ack = counter > 0
        last = self.m.TmpReg(initval=0)

        if cond is None:
            cond = ack
        else:
            cond = (cond, ack)

        raw_data, raw_valid = data.read(cond=cond)

        # write condition
        self.seq.If(raw_valid)

        self.seq.If(ack)(
            self.interfaces[port].addr(naddr),
            self.interfaces[port].wdata(raw_data),
            self.interfaces[port].wenable(1),
            naddr.inc(),
            counter.dec()
        )
        self.seq.Then().If(counter == 1)(
            last(1)
        )

        # de-assert
        self.seq.Delay(1)(
            self.interfaces[port].wenable(0),
            last(0)
        )

        # no retry, because there is no stall by memory-side

        return ack, last

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

    def read_request(self, addr, length=1, cond=None, counter=None):
        return self._request(addr, length, cond, counter)

    def read_dataflow(self, port, counter=None, cond=None):
        if self.seq.current_delay > 0:
            raise ValueError("Delayed control is not supported.")

        if counter is None:
            counter = self.counters[-1]

        naddr = self.next_address[counter]

        data_ready = self.m.TmpWire()
        last_ready = self.m.TmpWire()
        data_ready.assign(1)
        last_ready.assign(1)

        if cond is None:
            cond = (data_ready, last_ready)
        elif isinstance(cond, (tuple, list)):
            cond = tuple(list(cond) + [data_ready, last_ready])
        else:
            cond = (cond, data_ready, last_ready)

        ready = self.seq._check_cond(cond)
        ack = counter > 0 if ready is None else vtypes.Ands(counter > 0, ready)
        data = self.interfaces[port].rdata
        valid = self.m.TmpReg(initval=0)
        last = self.m.TmpReg(initval=0)

        self.seq.If(ack)(
            self.interfaces[port].addr(naddr),
            counter.dec(),
            naddr.inc(),
        )
        self.seq.Then().Delay(1)(
            valid(1),
            last(0)
        )
        self.seq.Then().If(counter == 1).Delay(1)(
            last(1)
        )

        # de-assert
        self.seq.Delay(2)(
            valid(0),
            last(0)
        )

        # retry
        if ready is not None:
            self.seq.If(vtypes.Ands(counter > 0, vtypes.Not(ready)))(
                counter(counter),
                naddr(naddr),
                valid(valid)
            )

        df_data = dataflow.Variable(data, valid, data_ready)
        df_last = dataflow.Variable(last, valid, last_ready)

        return df_data, df_last

    def _request(self, addr, length=1, cond=None, counter=None):
        if self.seq.current_delay > 0:
            raise ValueError("Delayed control is not supported.")

        if isinstance(length, int) and length < 1:
            raise ValueError("length must be more than 0.")

        if counter is not None and not isinstance(counter, vtypes.Reg):
            raise TypeError("counter must be Reg or None.")

        if cond is not None:
            self.seq.If(cond)

        if counter is None:
            counter = self.m.TmpReg(length.bit_length() + 1, initval=0)
            naddr = self.m.TmpReg((addr + length).bit_length() + 1, initval=0)
            self.next_address[counter] = naddr
        else:
            naddr = self.next_address[counter]

        self.counters.append(counter)

        ack = counter == 0

        self.seq.If(ack)(
            counter(length),
            naddr(addr)
        )

        return ack, counter
