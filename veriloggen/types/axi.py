from __future__ import absolute_import
from __future__ import print_function

import veriloggen.core.vtypes as vtypes
import veriloggen.core.module as module
from veriloggen.seq.seq import Seq
from . import util


class AxiBase(object):
    _I = util.t_Input
    _O = util.t_OutputReg

    def __init__(self, m, name=None, datawidth=32, addrwidth=32, itype=None, otype=None):
        if itype is None:
            itype = self._I
        if otype is None:
            otype = self._O
        self.m = m
        self.datawidth = datawidth
        self.addrwidth = addrwidth
        self.itype = itype
        self.otype = otype


class AxiWriteAddress(AxiBase):

    def __init__(self, m, name=None, datawidth=32, addrwidth=32, itype=None, otype=None):
        AxiBase.__init__(self, m, name, datawidth, addrwidth, itype, otype)
        self.awaddr = util.make_port(
            m, self.otype, name + '_awaddr', self.addrwidth, initval=0)
        self.awlen = util.make_port(
            m, self.otype, name + '_awlen', 8, initval=0)
        self.awvalid = util.make_port(
            m, self.otype, name + '_awvalid', None, initval=0)
        self.awready = util.make_port(
            m, self.itype, name + '_awready', None, initval=0)


class AxiWriteData(AxiBase):

    def __init__(self, m, name=None, datawidth=32, addrwidth=32, itype=None, otype=None):
        AxiBase.__init__(self, m, name, datawidth, addrwidth, itype, otype)
        self.wdata = util.make_port(
            m, self.otype, name + '_wdata', self.datawidth, initval=0)
        self.wstrb = util.make_port(
            m, self.otype, name + '_wstrb', self.datawidth // 8, initval=0)
        self.wlast = util.make_port(
            m, self.otype, name + '_wlast', None, initval=0)
        self.wvalid = util.make_port(
            m, self.otype, name + '_wvalid', None, initval=0)
        self.wready = util.make_port(
            m, self.itype, name + '_wready', None, initval=0)


class AxiReadAddress(AxiBase):

    def __init__(self, m, name=None, datawidth=32, addrwidth=32, itype=None, otype=None):
        AxiBase.__init__(self, m, name, datawidth, addrwidth, itype, otype)
        self.araddr = util.make_port(
            m, self.otype, name + '_araddr', self.addrwidth, initval=0)
        self.arlen = util.make_port(
            m, self.otype, name + '_arlen', 8, initval=0)
        self.arvalid = util.make_port(
            m, self.otype, name + '_arvalid', None, initval=0)
        self.arready = util.make_port(
            m, self.itype, name + '_arready', None, initval=0)


class AxiReadData(AxiBase):
    _O = util.t_Output

    def __init__(self, m, name=None, datawidth=32, addrwidth=32, itype=None, otype=None):
        AxiBase.__init__(self, m, name, datawidth, addrwidth, itype, otype)
        self.rdata = util.make_port(
            m, self.itype, name + '_rdata', self.datawidth, initval=0)
        self.rlast = util.make_port(
            m, self.itype, name + '_rlast', None, initval=0)
        self.rvalid = util.make_port(
            m, self.itype, name + '_rvalid', None, initval=0)
        self.rready = util.make_port(
            m, self.otype, name + '_rready', None, initval=0)

        
# master port
class AxiMasterWriteAddress(AxiWriteAddress):
    pass


class AxiMasterWriteData(AxiWriteData):
    pass


class AxiMasterReadAddress(AxiReadAddress):
    pass


class AxiMasterReadData(AxiReadData):
    pass


# slave port
class AxiSlaveWriteAddress(AxiWriteAddress):
    _I, _O = util.swap_type(AxiWriteAddress)


class AxiSlaveWriteData(AxiWriteData):
    _I, _O = util.swap_type(AxiWriteData)


class AxiSlaveReadAddress(AxiReadAddress):
    _I, _O = util.swap_type(AxiReadAddress)


class AxiSlaveReadData(AxiReadData):
    _I, _O = util.swap_type(AxiReadData)

    
# master interface
class AxiMaster(object):
    burst_size_width = 8

    def __init__(self, m, name, clk, rst, datawidth=32, addrwidth=32):
        self.m = m
        self.name = name
        self.clk = clk
        self.rst = rst
        self.datawidth = datawidth
        self.addrwidth = addrwidth

        self.waddr = AxiMasterWriteAddress(m, name, datawidth, addrwidth)
        self.wdata = AxiMasterWriteData(m, name, datawidth, addrwidth)
        self.raddr = AxiMasterReadAddress(m, name, datawidth, addrwidth)
        self.rdata = AxiMasterReadData(m, name, datawidth, addrwidth)

        self.seq = Seq(m, name, clk, rst)
        #self.m.add_hook(self.seq.make_always)

        self.write_counters = []
        self.read_counters = []

        self._write_disabled = False
        self._read_disabled = False

    def disable_write(self):
        self.seq(
            self.waddr.awaddr(0),
            self.waddr.awlen(0),
            self.waddr.awvalid(0),
            self.wdata.wdata(0),
            self.wdata.wstrb(0),
            self.wdata.wvalid(0),
            self.wdata.wlast(0)
        )
        self._write_disabled = True

    def disable_read(self):
        self.seq(
            self.raddr.araddr(0),
            self.raddr.arlen(0),
            self.raddr.arvalid(0)
        )
        self.rdata.rready.assign(0)
        self._read_disabled = True

    def write_request(self, addr, length=1, cond=None):
        if self._write_disabled:
            raise TypeError('Write disabled.')
        
        if self.seq.current_delay > 0:
            raise ValueError("Delayed control is not supported.")

        if isinstance(length, int) and length > 2 ** self.burst_size_width:
            raise ValueError("length must be less than 257.")

        if isinstance(length, int) and length < 1:
            raise ValueError("length must be more than 0.")

        if cond is not None:
            self.seq.If(cond)

        ack = vtypes.Ors(self.waddr.awready,
                         vtypes.Not(self.waddr.awvalid))

        counter = self.m.TmpReg(self.burst_size_width, initval=0)
        self.write_counters.append(counter)

        self.seq.If(ack)(
            self.waddr.awaddr(addr),
            self.waddr.awlen(length - 1),
            self.waddr.awvalid(1),
            counter(length - 1)
        )
        
        # de-assert
        self.seq.Delay(1)(
            self.waddr.awvalid(0)
        )

        # retry
        self.seq.If(vtypes.Ands(self.waddr.awvalid, vtypes.Not(self.waddr.awready)))(
            self.waddr.awvalid(self.waddr.awvalid)
        )

        return ack, counter

    def write_data(self, data, counter=None, cond=None):
        if self._write_disabled:
            raise TypeError('Write disabled.')

        if self.seq.current_delay > 0:
            raise ValueError("Delayed control is not supported.")

        if counter is None:
            counter = self.write_counters[-1]
        
        if cond is not None:
            self.seq.If(cond)

        ack = vtypes.Ors(self.wdata.wready,
                         vtypes.Not(self.wdata.wvalid))
        last = self.m.TmpReg(initval=0)

        self.seq.If(vtypes.Ands(ack, vtypes.Not(last)))(
            self.wdata.wdata(data),
            self.wdata.wvalid(1),
            self.wdata.wlast(0),
            self.wdata.wstrb(vtypes.Repeat(vtypes.Int(1, 1), (self.wdata.datawidth // 8))),
            counter.dec()
        )
        self.seq.Then().If(counter == 0)(
            self.wdata.wlast(1),
            last(1)
        )

        # de-assert
        self.seq.Delay(1)(
            self.wdata.wvalid(0),
            self.wdata.wlast(0),
            last(0)
        )
        
        # retry
        self.seq.If(vtypes.Ands(self.wdata.wvalid, vtypes.Not(self.wdata.wready)))(
            self.wdata.wvalid(self.wdata.wvalid),
            self.wdata.wlast(self.wdata.wlast),
            last(last)
        )

        return ack, last

    def read_request(self, addr, length, cond=None):
        if self._read_disabled:
            raise TypeError('Read disabled.')
        
        if self.seq.current_delay > 0:
            raise ValueError("Delayed control is not supported.")

        if isinstance(length, int) and length > 2 ** self.burst_size_width:
            raise ValueError("length must be less than 257.")

        if isinstance(length, int) and length < 1:
            raise ValueError("length must be more than 0.")

        if cond is not None:
            self.seq.If(cond)

        ack = vtypes.Ors(self.raddr.arready,
                         vtypes.Not(self.raddr.arvalid))

        counter = self.m.TmpReg(self.burst_size_width, initval=0)
        self.read_counters.append(counter)

        self.seq.If(ack)(
            self.raddr.araddr(addr),
            self.raddr.arlen(length - 1),
            self.raddr.arvalid(1),
            counter(length - 1)
        )

        # de-assert
        self.seq.Delay(1)(
            self.raddr.arvalid(0)
        )

        # retry
        self.seq.If(vtypes.Ands(self.raddr.arvalid, vtypes.Not(self.raddr.arready)))(
            self.raddr.arvalid(self.raddr.arvalid)
        )

        return ack, counter

    def read_data(self, counter=None, cond=None):
        if self._read_disabled:
            raise TypeError('Read disabled.')
        
        if self.seq.current_delay > 0:
            raise ValueError("Delayed control is not supported.")
        
        if counter is None:
            counter = self.read_counters[-1]
        
        ready = self.seq._check_cond(cond)
        val = 1 if ready is None else ready
        
        prev_subst = self.rdata.rready._get_subst()
        if not prev_subst:
            self.rdata.rready.assign(val)
        else:
            self.rdata.rready.subst[0].overwrite_right(vtypes.Ors(prev_subst[0].right, val))

        ack = vtypes.Ands(self.rdata.rready, self.rdata.rvalid)
        data = self.rdata.rdata
        valid = ack
        last = self.rdata.rlast

        self.seq.If(ack)(
            counter.dec()
        )
        
        return data, valid, last
