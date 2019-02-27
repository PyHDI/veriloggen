from __future__ import absolute_import
from __future__ import print_function
from __future__ import division

import functools
import math

import veriloggen.core.vtypes as vtypes
from veriloggen.seq.seq import Seq
from veriloggen.fsm.fsm import FSM

import veriloggen.dataflow as _df
from veriloggen.dataflow.dataflow import DataflowManager
from veriloggen.dataflow.dtypes import make_condition, read_multi
from veriloggen.dataflow.dtypes import _Numeric as df_numeric
from . import util


BURST_FIXED = 0b0
BURST_INCR = 0b1
BURST_WRAP = 0b10

CACHE_HP = 0b0011
CACHE_ACP = 0b1111

USER_DEFAULT = 0b1


def _connect_ready(m, var, val):
    prev_assign = var._get_assign()

    if not prev_assign:
        var.assign(val)
    else:
        prev_assign.overwrite_right(
            vtypes.Ors(prev_assign.statement.right, val))
        m.remove(prev_assign)
        m.append(prev_assign)


class AxiInterfaceBase(object):
    _I = util.t_Input
    _O = util.t_OutputReg

    def __init__(self, m, name=None,
                 datawidth=32, addrwidth=32,
                 id_width=1, user_width=1,
                 itype=None, otype=None):

        if itype is None:
            itype = self._I
        if otype is None:
            otype = self._O

        self.m = m
        self.name = name

        self.datawidth = datawidth
        self.addrwidth = addrwidth

        self.id_width = id_width
        self.user_width = user_width

        self.itype = itype
        self.otype = otype


class AxiLiteInterfaceBase(AxiInterfaceBase):
    _I = util.t_Input
    _O = util.t_OutputReg

    def __init__(self, m, name=None,
                 datawidth=32, addrwidth=32,
                 itype=None, otype=None):

        AxiInterfaceBase.__init__(self, m, name, datawidth, addrwidth,
                                  None, None,
                                  itype, otype)


class AxiWriteAddress(AxiInterfaceBase):

    def __init__(self, m, name=None, datawidth=32, addrwidth=32,
                 id_width=1, user_width=1,
                 itype=None, otype=None):

        AxiInterfaceBase.__init__(self, m, name, datawidth, addrwidth,
                                  id_width, user_width, itype, otype)

        self.awid = util.make_port(
            m, self.otype, name + '_awid', self.id_width, initval=0)
        self.awaddr = util.make_port(
            m, self.otype, name + '_awaddr', self.addrwidth, initval=0)
        self.awlen = util.make_port(
            m, self.otype, name + '_awlen', 8, initval=0)
        self.awsize = util.make_port(
            m, self.otype, name + '_awsize', 3, initval=0, no_reg=True)
        self.awburst = util.make_port(
            m, self.otype, name + '_awburst', 2, initval=0, no_reg=True)
        self.awlock = util.make_port(
            m, self.otype, name + '_awlock', 2, initval=0, no_reg=True)
        self.awcache = util.make_port(
            m, self.otype, name + '_awcache', 4, initval=0, no_reg=True)
        self.awprot = util.make_port(
            m, self.otype, name + '_awprot', 3, initval=0, no_reg=True)
        self.awqos = util.make_port(
            m, self.otype, name + '_awqos', 4, initval=0, no_reg=True)
        self.awuser = util.make_port(
            m, self.otype, name + '_awuser', self.user_width, initval=0, no_reg=True)
        self.awvalid = util.make_port(
            m, self.otype, name + '_awvalid', None, initval=0)
        self.awready = util.make_port(
            m, self.itype, name + '_awready', None, initval=0)


class AxiLiteWriteAddress(AxiLiteInterfaceBase):

    def __init__(self, m, name=None, datawidth=32, addrwidth=32,
                 itype=None, otype=None):

        AxiLiteInterfaceBase.__init__(self, m, name, datawidth, addrwidth,
                                      itype, otype)

        self.awaddr = util.make_port(
            m, self.otype, name + '_awaddr', self.addrwidth, initval=0)
        self.awvalid = util.make_port(
            m, self.otype, name + '_awvalid', None, initval=0)
        self.awready = util.make_port(
            m, self.itype, name + '_awready', None, initval=0)


class AxiWriteData(AxiInterfaceBase):

    def __init__(self, m, name=None, datawidth=32, addrwidth=32,
                 id_width=1, user_width=1,
                 itype=None, otype=None):

        AxiInterfaceBase.__init__(self, m, name, datawidth, addrwidth,
                                  id_width, user_width, itype, otype)

        self.wdata = util.make_port(
            m, self.otype, name + '_wdata', self.datawidth, initval=0)
        self.wstrb = util.make_port(
            m, self.otype, name + '_wstrb', self.datawidth // 8, initval=0)
        self.wlast = util.make_port(
            m, self.otype, name + '_wlast', None, initval=0)
        self.wuser = util.make_port(
            m, self.otype, name + '_wuser', self.user_width, initval=0, no_reg=True)
        self.wvalid = util.make_port(
            m, self.otype, name + '_wvalid', None, initval=0)
        self.wready = util.make_port(
            m, self.itype, name + '_wready', None, initval=0)


class AxiLiteWriteData(AxiLiteInterfaceBase):

    def __init__(self, m, name=None, datawidth=32, addrwidth=32,
                 itype=None, otype=None):

        AxiLiteInterfaceBase.__init__(self, m, name, datawidth, addrwidth,
                                      itype, otype)

        self.wdata = util.make_port(
            m, self.otype, name + '_wdata', self.datawidth, initval=0)
        self.wstrb = util.make_port(
            m, self.otype, name + '_wstrb', self.datawidth // 8, initval=0)
        self.wvalid = util.make_port(
            m, self.otype, name + '_wvalid', None, initval=0)
        self.wready = util.make_port(
            m, self.itype, name + '_wready', None, initval=0)


class AxiWriteResponse(AxiInterfaceBase):

    def __init__(self, m, name=None, datawidth=32, addrwidth=32,
                 id_width=1, user_width=1,
                 itype=None, otype=None):

        AxiInterfaceBase.__init__(self, m, name, datawidth, addrwidth,
                                  id_width, user_width, itype, otype)

        self.bid = util.make_port(
            m, self.itype, name + '_bid', self.id_width, initval=0)
        self.bresp = util.make_port(
            m, self.itype, name + '_bresp', 2, initval=0, no_reg=True)
        self.buser = util.make_port(
            m, self.itype, name + '_buser', self.user_width, initval=0, no_reg=True)
        self.bvalid = util.make_port(
            m, self.itype, name + '_bvalid', None, initval=0)
        self.bready = util.make_port(
            m, self.otype, name + '_bready', None, initval=0, no_reg=True)


class AxiLiteWriteResponse(AxiLiteInterfaceBase):

    def __init__(self, m, name=None, datawidth=32, addrwidth=32,
                 itype=None, otype=None):

        AxiLiteInterfaceBase.__init__(self, m, name, datawidth, addrwidth,
                                      itype, otype)

        self.bresp = util.make_port(
            m, self.itype, name + '_bresp', 2, initval=0, no_reg=True)
        self.bvalid = util.make_port(
            m, self.itype, name + '_bvalid', None, initval=0)
        self.bready = util.make_port(
            m, self.otype, name + '_bready', None, initval=0, no_reg=True)


class AxiReadAddress(AxiInterfaceBase):

    def __init__(self, m, name=None, datawidth=32, addrwidth=32,
                 id_width=1, user_width=1,
                 itype=None, otype=None):

        AxiInterfaceBase.__init__(self, m, name, datawidth, addrwidth,
                                  id_width, user_width, itype, otype)

        self.arid = util.make_port(
            m, self.otype, name + '_arid', self.id_width, initval=0)
        self.araddr = util.make_port(
            m, self.otype, name + '_araddr', self.addrwidth, initval=0)
        self.arlen = util.make_port(
            m, self.otype, name + '_arlen', 8, initval=0)
        self.arsize = util.make_port(
            m, self.otype, name + '_arsize', 3, initval=0, no_reg=True)
        self.arburst = util.make_port(
            m, self.otype, name + '_arburst', 2, initval=0, no_reg=True)
        self.arlock = util.make_port(
            m, self.otype, name + '_arlock', 2, initval=0, no_reg=True)
        self.arcache = util.make_port(
            m, self.otype, name + '_arcache', 4, initval=0, no_reg=True)
        self.arprot = util.make_port(
            m, self.otype, name + '_arprot', 3, initval=0, no_reg=True)
        self.arqos = util.make_port(
            m, self.otype, name + '_arqos', 4, initval=0, no_reg=True)
        self.aruser = util.make_port(
            m, self.otype, name + '_aruser', self.user_width, initval=0, no_reg=True)
        self.arvalid = util.make_port(
            m, self.otype, name + '_arvalid', None, initval=0)
        self.arready = util.make_port(
            m, self.itype, name + '_arready', None, initval=0)


class AxiLiteReadAddress(AxiLiteInterfaceBase):

    def __init__(self, m, name=None, datawidth=32, addrwidth=32,
                 itype=None, otype=None):

        AxiLiteInterfaceBase.__init__(self, m, name, datawidth, addrwidth,
                                      itype, otype)

        self.araddr = util.make_port(
            m, self.otype, name + '_araddr', self.addrwidth, initval=0)
        self.arvalid = util.make_port(
            m, self.otype, name + '_arvalid', None, initval=0)
        self.arready = util.make_port(
            m, self.itype, name + '_arready', None, initval=0)


class AxiReadData(AxiInterfaceBase):
    _O = util.t_Output

    def __init__(self, m, name=None, datawidth=32, addrwidth=32,
                 id_width=1, user_width=1,
                 itype=None, otype=None):

        AxiInterfaceBase.__init__(self, m, name, datawidth, addrwidth,
                                  id_width, user_width, itype, otype)

        self.rid = util.make_port(
            m, self.itype, name + '_rid', self.id_width, initval=0)
        self.rdata = util.make_port(
            m, self.itype, name + '_rdata', self.datawidth, initval=0)
        self.rresp = util.make_port(
            m, self.itype, name + '_rresp', 2, initval=0, no_reg=True)
        self.rlast = util.make_port(
            m, self.itype, name + '_rlast', None, initval=0)
        self.ruser = util.make_port(
            m, self.itype, name + '_ruser', self.user_width, initval=0, no_reg=True)
        self.rvalid = util.make_port(
            m, self.itype, name + '_rvalid', None, initval=0)
        self.rready = util.make_port(
            m, self.otype, name + '_rready', None, initval=0)


class AxiLiteReadData(AxiLiteInterfaceBase):
    _O = util.t_Output

    def __init__(self, m, name=None, datawidth=32, addrwidth=32,
                 itype=None, otype=None):

        AxiLiteInterfaceBase.__init__(self, m, name, datawidth, addrwidth,
                                      itype, otype)

        self.rdata = util.make_port(
            m, self.itype, name + '_rdata', self.datawidth, initval=0)
        self.rresp = util.make_port(
            m, self.itype, name + '_rresp', 2, initval=0, no_reg=True)
        self.rvalid = util.make_port(
            m, self.itype, name + '_rvalid', None, initval=0)
        self.rready = util.make_port(
            m, self.otype, name + '_rready', None, initval=0)


# AXI-Full Master
class AxiMasterWriteAddress(AxiWriteAddress):
    pass


class AxiMasterWriteData(AxiWriteData):
    pass


class AxiMasterWriteResponse(AxiWriteResponse):
    pass


class AxiMasterReadAddress(AxiReadAddress):
    pass


class AxiMasterReadData(AxiReadData):
    pass


# AXI-Lite Master
class AxiLiteMasterWriteAddress(AxiLiteWriteAddress):
    pass


class AxiLiteMasterWriteData(AxiLiteWriteData):
    pass


class AxiLiteMasterWriteResponse(AxiLiteWriteResponse):
    pass


class AxiLiteMasterReadAddress(AxiLiteReadAddress):
    pass


class AxiLiteMasterReadData(AxiLiteReadData):
    pass


# AXI-Full Slave
class AxiSlaveWriteAddress(AxiWriteAddress):
    _I = util.t_Output
    _O = util.t_Input


class AxiSlaveWriteData(AxiWriteData):
    _I = util.t_Output
    _O = util.t_Input


class AxiSlaveWriteResponse(AxiWriteResponse):
    _I = util.t_OutputReg
    _O = util.t_Input


class AxiSlaveReadAddress(AxiReadAddress):
    _I = util.t_Output
    _O = util.t_Input


class AxiSlaveReadData(AxiReadData):
    _I = util.t_OutputReg
    _O = util.t_Input


# AXI-Lite Slave
class AxiLiteSlaveWriteAddress(AxiLiteWriteAddress):
    _I = util.t_Output
    _O = util.t_Input


class AxiLiteSlaveWriteData(AxiLiteWriteData):
    _I = util.t_Output
    _O = util.t_Input


class AxiLiteSlaveWriteResponse(AxiLiteWriteResponse):
    _I = util.t_OutputReg
    _O = util.t_Input


class AxiLiteSlaveReadAddress(AxiLiteReadAddress):
    _I = util.t_Output
    _O = util.t_Input


class AxiLiteSlaveReadData(AxiLiteReadData):
    _I = util.t_OutputReg
    _O = util.t_Input


# AXI-Full
class AxiMaster(object):
    burst_size_width = 8
    boundary_size = 4096

    def __init__(self, m, name, clk, rst, datawidth=32, addrwidth=32,
                 id_width=1, user_width=1,
                 burst_mode=BURST_INCR, cache_mode=CACHE_HP, user_value=USER_DEFAULT,
                 noio=False, nodataflow=False):

        self.m = m
        self.name = name

        self.clk = clk
        self.rst = rst

        self.datawidth = datawidth
        self.addrwidth = addrwidth
        self.id_width = id_width
        self.user_width = user_width

        self.noio = noio

        if not hasattr(self.m, 'masterbus'):
            self.m.masterbus = []

        self.m.masterbus.append(self)

        itype = util.t_Wire if noio else None
        otype = util.t_Reg if noio else None

        self.waddr = AxiMasterWriteAddress(m, name, datawidth, addrwidth,
                                           id_width, user_width, itype, otype)
        self.wdata = AxiMasterWriteData(m, name, datawidth, addrwidth,
                                        id_width, user_width, itype, otype)
        self.wresp = AxiMasterWriteResponse(m, name, datawidth, addrwidth,
                                            id_width, user_width, itype, otype)
        self.raddr = AxiMasterReadAddress(m, name, datawidth, addrwidth,
                                          id_width, user_width, itype, otype)

        otype = util.t_Wire if noio else None

        self.rdata = AxiMasterReadData(m, name, datawidth, addrwidth,
                                       id_width, user_width, itype, otype)

        self.seq = Seq(m, name, clk, rst)

        # default values
        self.waddr.awsize.assign(int(math.log(self.datawidth / 8, 2)))
        self.waddr.awburst.assign(burst_mode)
        self.waddr.awlock.assign(0)
        self.waddr.awcache.assign(cache_mode)
        self.waddr.awprot.assign(0)
        self.waddr.awqos.assign(0)
        self.waddr.awuser.assign(user_value)
        self.wdata.wuser.assign(user_value)
        self.wresp.bready.assign(1)
        self.raddr.arsize.assign(int(math.log(self.datawidth / 8, 2)))
        self.raddr.arburst.assign(burst_mode)
        self.raddr.arlock.assign(0)
        self.raddr.arcache.assign(cache_mode)
        self.raddr.arprot.assign(0)
        self.raddr.arqos.assign(0)
        self.raddr.aruser.assign(user_value)

        self.write_counters = []
        self.read_counters = []

        if nodataflow:
            self.df = None
        else:
            self.df = DataflowManager(self.m, self.clk, self.rst)

        self._write_disabled = False
        self._read_disabled = False

    def disable_write(self):
        ports = [self.waddr.awid(0),
                 self.waddr.awaddr(0),
                 self.waddr.awlen(0),
                 self.waddr.awvalid(0),
                 self.wdata.wdata(0),
                 self.wdata.wstrb(0),
                 self.wdata.wlast(0),
                 self.wdata.wvalid(0)]

        self.seq(
            *ports
        )

        self._write_disabled = True

    def disable_read(self):
        ports = [self.raddr.arid(0),
                 self.raddr.araddr(0),
                 self.raddr.arlen(0),
                 self.raddr.arvalid(0)]

        self.seq(
            *ports
        )

        self.rdata.rready.assign(0)

        self._read_disabled = True

    def mask_addr(self, addr):
        s = util.log2(self.datawidth // 8)
        return (addr >> s) << s

    def check_boundary(self, addr, length, datawidth=None, boundary_size=None):
        if datawidth is None:
            datawidth = self.datawidth
        if boundary_size is None:
            boundary_size = self.boundary_size
        mask = boundary_size - 1
        return ((addr & mask) + (length << util.log2(datawidth // 8))) >= boundary_size

    def rest_boundary(self, addr, datawidth=None, boundary_size=None):
        if datawidth is None:
            datawidth = self.datawidth
        if boundary_size is None:
            boundary_size = self.boundary_size
        mask = boundary_size - 1
        return (vtypes.Int(boundary_size) - (addr & mask)) >> util.log2(datawidth // 8)

    def write_request(self, addr, length=1, cond=None, counter=None):
        """
        @return ack, counter
        """
        if self._write_disabled:
            raise TypeError('Write disabled.')

        if isinstance(length, int) and length > 2 ** self.burst_size_width:
            raise ValueError("length must be less than 257.")

        if isinstance(length, int) and length < 1:
            raise ValueError("length must be more than 0.")

        if counter is not None and not isinstance(counter, vtypes.Reg):
            raise TypeError("counter must be Reg or None.")

        if cond is not None:
            self.seq.If(cond)

        ack = vtypes.Ors(self.waddr.awready, vtypes.Not(self.waddr.awvalid))

        if counter is None:
            counter = self.m.TmpReg(self.burst_size_width + 1, initval=0)

        self.write_counters.append(counter)

        self.seq.If(vtypes.Ands(ack, counter == 0))(
            self.waddr.awid(0),
            self.waddr.awaddr(addr),
            self.waddr.awlen(length - 1),
            self.waddr.awvalid(1),
            counter(length)
        )
        self.seq.Then().If(length == 0)(
            self.waddr.awvalid(0)
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
        """
        @return ack, last
        """
        if self._write_disabled:
            raise TypeError('Write disabled.')

        if counter is not None and not isinstance(counter, vtypes.Reg):
            raise TypeError("counter must be Reg or None.")

        if counter is None:
            counter = self.write_counters[-1]

        if cond is not None:
            self.seq.If(cond)

        ack = vtypes.Ands(counter > 0,
                          vtypes.Ors(self.wdata.wready, vtypes.Not(self.wdata.wvalid)))
        last = self.m.TmpReg(initval=0)

        self.seq.If(vtypes.Ands(ack, counter > 0))(
            self.wdata.wdata(data),
            self.wdata.wvalid(1),
            self.wdata.wlast(0),
            self.wdata.wstrb(vtypes.Repeat(
                vtypes.Int(1, 1), (self.wdata.datawidth // 8))),
            counter.dec()
        )
        self.seq.Then().If(counter == 1)(
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

    def write_dataflow(self, data, counter=None, cond=None, when=None):
        """
        @return done
        'data' and 'when' must be dataflow variables
        """
        if self._write_disabled:
            raise TypeError('Write disabled.')

        if counter is not None and not isinstance(counter, vtypes.Reg):
            raise TypeError("counter must be Reg or None.")

        if counter is None:
            counter = self.write_counters[-1]

        ack = vtypes.Ands(counter > 0,
                          vtypes.Ors(self.wdata.wready, vtypes.Not(self.wdata.wvalid)))
        last = self.m.TmpReg(initval=0)

        if cond is None:
            cond = ack
        else:
            cond = (cond, ack)

        if when is None or not isinstance(when, df_numeric):
            raw_data, raw_valid = data.read(cond=cond)
        else:
            data_list, raw_valid = read_multi(self.m, data, when, cond=cond)
            raw_data = data_list[0]
            when = data_list[1]

        when_cond = make_condition(when, ready=cond)
        if when_cond is not None:
            raw_valid = vtypes.Ands(when_cond, raw_valid)

        # write condition
        self.seq.If(raw_valid)

        self.seq.If(vtypes.Ands(ack, counter > 0))(
            self.wdata.wdata(raw_data),
            self.wdata.wvalid(1),
            self.wdata.wlast(0),
            self.wdata.wstrb(vtypes.Repeat(
                vtypes.Int(1, 1), (self.wdata.datawidth // 8))),
            counter.dec()
        )
        self.seq.Then().If(counter == 1)(
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

        done = vtypes.Ands(last, self.wdata.wvalid, self.wdata.wready)

        return done

    def read_request(self, addr, length=1, cond=None, counter=None):
        """
        @return ack, counter
        """
        if self._read_disabled:
            raise TypeError('Read disabled.')

        if isinstance(length, int) and length > 2 ** self.burst_size_width:
            raise ValueError("length must be less than 257.")

        if isinstance(length, int) and length < 1:
            raise ValueError("length must be more than 0.")

        if counter is not None and not isinstance(counter, vtypes.Reg):
            raise TypeError("counter must be Reg or None.")

        if cond is not None:
            self.seq.If(cond)

        ack = vtypes.Ors(self.raddr.arready, vtypes.Not(self.raddr.arvalid))

        if counter is None:
            counter = self.m.TmpReg(self.burst_size_width + 1, initval=0)

        self.read_counters.append(counter)

        self.seq.If(vtypes.Ands(ack, counter == 0))(
            self.raddr.arid(0),
            self.raddr.araddr(addr),
            self.raddr.arlen(length - 1),
            self.raddr.arvalid(1),
            counter(length)
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
        """
        @return data, valid, last
        """
        if self._read_disabled:
            raise TypeError('Read disabled.')

        if counter is not None and not isinstance(counter, vtypes.Reg):
            raise TypeError("counter must be Reg or None.")

        if counter is None:
            counter = self.read_counters[-1]

        ready = make_condition(cond)
        val = 1 if ready is None else ready

        _connect_ready(self.rdata.rready._get_module(), self.rdata.rready, val)

        ack = vtypes.Ands(self.rdata.rready, self.rdata.rvalid)
        data = self.rdata.rdata
        valid = ack
        last = self.rdata.rlast

        self.seq.If(vtypes.Ands(ack, counter > 0))(
            counter.dec()
        )

        return data, valid, last

    def read_dataflow(self, counter=None, cond=None, point=0, signed=True):
        """
        @return data, last, done
        """
        if self._read_disabled:
            raise TypeError('Read disabled.')

        if counter is not None and not isinstance(counter, vtypes.Reg):
            raise TypeError("counter must be Reg or None.")

        if counter is None:
            counter = self.read_counters[-1]

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

        ready = make_condition(*cond)
        val = 1 if ready is None else ready

        _connect_ready(self.rdata.rready._get_module(), self.rdata.rready, val)

        ack = vtypes.Ands(self.rdata.rready, self.rdata.rvalid)
        data = self.rdata.rdata
        valid = self.rdata.rvalid
        last = self.rdata.rlast

        self.seq.If(vtypes.Ands(ack, counter > 0))(
            counter.dec()
        )

        df = self.df if self.df is not None else _df

        df_data = df.Variable(data, valid, data_ready,
                              point=point, signed=signed)
        df_last = df.Variable(last, valid, last_ready, width=1, signed=False)
        done = vtypes.Ands(last, self.rdata.rvalid, self.rdata.rready)

        return df_data, df_last, done

    def connect(self, ports, name):
        if not self.noio:
            raise ValueError('I/O ports can not be connected to others.')

        awid = ports['_'.join([name, 'awid'])]
        awaddr = ports['_'.join([name, 'awaddr'])]
        awlen = ports['_'.join([name, 'awlen'])]
        awsize = ports['_'.join([name, 'awsize'])]
        awburst = ports['_'.join([name, 'awburst'])]
        awlock = ports['_'.join([name, 'awlock'])]
        awcache = ports['_'.join([name, 'awcache'])]
        awprot = ports['_'.join([name, 'awprot'])]
        awqos = ports['_'.join([name, 'awqos'])]
        awuser = ports['_'.join([name, 'awuser'])]
        awvalid = ports['_'.join([name, 'awvalid'])]
        awready = ports['_'.join([name, 'awready'])]

        awid.connect(self.waddr.awid)
        awaddr.connect(self.waddr.awaddr)
        awlen.connect(self.waddr.awlen)
        awsize.connect(self.waddr.awsize)
        awburst.connect(self.waddr.awburst)
        awlock.connect(self.waddr.awlock)
        awcache.connect(self.waddr.awcache)
        awprot.connect(self.waddr.awprot)
        awqos.connect(self.waddr.awqos)
        awuser.connect(self.waddr.awuser)
        awvalid.connect(self.waddr.awvalid)
        self.waddr.awready.connect(awready)

        wdata = ports['_'.join([name, 'wdata'])]
        wstrb = ports['_'.join([name, 'wstrb'])]
        wlast = ports['_'.join([name, 'wlast'])]
        wuser = ports['_'.join([name, 'wuser'])]
        wvalid = ports['_'.join([name, 'wvalid'])]
        wready = ports['_'.join([name, 'wready'])]

        wdata.connect(self.wdata.wdata)
        wstrb.connect(self.wdata.wstrb)
        wlast.connect(self.wdata.wlast)
        wuser.connect(self.wdata.wuser)
        wvalid.connect(self.wdata.wvalid)
        self.wdata.wready.connect(wready)

        bid = ports['_'.join([name, 'bid'])]
        bresp = ports['_'.join([name, 'bresp'])]
        buser = ports['_'.join([name, 'buser'])]
        bvalid = ports['_'.join([name, 'bvalid'])]
        bready = ports['_'.join([name, 'bready'])]

        self.wresp.bid.connect(bid)
        self.wresp.bresp.connect(bresp)
        self.wresp.buser.connect(buser)
        self.wresp.bvalid.connect(bvalid)
        bready.connect(self.wresp.bready)

        arid = ports['_'.join([name, 'arid'])]
        araddr = ports['_'.join([name, 'araddr'])]
        arlen = ports['_'.join([name, 'arlen'])]
        arsize = ports['_'.join([name, 'arsize'])]
        arburst = ports['_'.join([name, 'arburst'])]
        arlock = ports['_'.join([name, 'arlock'])]
        arcache = ports['_'.join([name, 'arcache'])]
        arprot = ports['_'.join([name, 'arprot'])]
        arqos = ports['_'.join([name, 'arqos'])]
        aruser = ports['_'.join([name, 'aruser'])]
        arvalid = ports['_'.join([name, 'arvalid'])]
        arready = ports['_'.join([name, 'arready'])]

        arid.connect(self.raddr.arid)
        araddr.connect(self.raddr.araddr)
        arlen.connect(self.raddr.arlen)
        arsize.connect(self.raddr.arsize)
        arburst.connect(self.raddr.arburst)
        arlock.connect(self.raddr.arlock)
        arcache.connect(self.raddr.arcache)
        arprot.connect(self.raddr.arprot)
        arqos.connect(self.raddr.arqos)
        aruser.connect(self.raddr.aruser)
        arvalid.connect(self.raddr.arvalid)
        self.raddr.arready.connect(arready)

        rid = ports['_'.join([name, 'rid'])]
        rdata = ports['_'.join([name, 'rdata'])]
        rresp = ports['_'.join([name, 'rresp'])]
        rlast = ports['_'.join([name, 'rlast'])]
        ruser = ports['_'.join([name, 'ruser'])]
        rvalid = ports['_'.join([name, 'rvalid'])]
        rready = ports['_'.join([name, 'rready'])]

        self.rdata.rid.connect(rid)
        self.rdata.rdata.connect(rdata)
        self.rdata.rresp.connect(rresp)
        self.rdata.rlast.connect(rlast)
        self.rdata.ruser.connect(ruser)
        self.rdata.rvalid.connect(rvalid)
        rready.connect(self.rdata.rready)


# AXI-Lite
class AxiLiteMaster(AxiMaster):

    def __init__(self, m, name, clk, rst, datawidth=32, addrwidth=32,
                 noio=False, nodataflow=False):

        self.m = m
        self.name = name

        self.clk = clk
        self.rst = rst

        self.datawidth = datawidth
        self.addrwidth = addrwidth

        self.noio = noio

        if not hasattr(self.m, 'masterbus'):
            self.m.masterbus = []

        self.m.masterbus.append(self)

        itype = util.t_Wire if noio else None
        otype = util.t_Reg if noio else None

        self.waddr = AxiLiteMasterWriteAddress(m, name, datawidth, addrwidth,
                                               itype, otype)
        self.wdata = AxiLiteMasterWriteData(m, name, datawidth, addrwidth,
                                            itype, otype)
        self.wresp = AxiLiteMasterWriteResponse(m, name, datawidth, addrwidth,
                                                itype, otype)
        self.raddr = AxiLiteMasterReadAddress(m, name, datawidth, addrwidth,
                                              itype, otype)

        otype = util.t_Wire if noio else None

        self.rdata = AxiLiteMasterReadData(m, name, datawidth, addrwidth,
                                           itype, otype)

        self.seq = Seq(m, name, clk, rst)

        # default values
        self.wresp.bready.assign(1)

        if nodataflow:
            self.df = None
        else:
            self.df = DataflowManager(self.m, self.clk, self.rst)

        self._write_disabled = False
        self._read_disabled = False

    def disable_write(self):
        ports = [self.waddr.awaddr(0),
                 self.waddr.awvalid(0),
                 self.wdata.wdata(0),
                 self.wdata.wstrb(0),
                 self.wdata.wvalid(0)]

        self.seq(
            *ports
        )

        self._write_disabled = True

    def disable_read(self):
        ports = [self.raddr.araddr(0),
                 self.raddr.arvalid(0)]

        self.seq(
            *ports
        )

        self.rdata.rready.assign(0)

        self._read_disabled = True

    def write_request(self, addr, length=1, cond=None):
        """
        @return ack
        """
        if self._write_disabled:
            raise TypeError('Write disabled.')

        if length != 1:
            raise ValueError('length must be 1 for lite-interface.')

        if cond is not None:
            self.seq.If(cond)

        ack = vtypes.Ors(self.waddr.awready, vtypes.Not(self.waddr.awvalid))

        self.seq.If(ack)(
            self.waddr.awaddr(addr),
            self.waddr.awvalid(1),
        )

        # de-assert
        self.seq.Delay(1)(
            self.waddr.awvalid(0)
        )

        # retry
        self.seq.If(vtypes.Ands(self.waddr.awvalid, vtypes.Not(self.waddr.awready)))(
            self.waddr.awvalid(self.waddr.awvalid)
        )

        return ack

    def write_data(self, data, cond=None):
        """
        @return ack
        """
        if self._write_disabled:
            raise TypeError('Write disabled.')

        if cond is not None:
            self.seq.If(cond)

        ack = vtypes.Ors(self.wdata.wready, vtypes.Not(self.wdata.wvalid))

        self.seq.If(ack)(
            self.wdata.wdata(data),
            self.wdata.wvalid(1),
            self.wdata.wstrb(vtypes.Repeat(
                vtypes.Int(1, 1), (self.wdata.datawidth // 8)))
        )

        # de-assert
        self.seq.Delay(1)(
            self.wdata.wvalid(0),
        )

        # retry
        self.seq.If(vtypes.Ands(self.wdata.wvalid, vtypes.Not(self.wdata.wready)))(
            self.wdata.wvalid(self.wdata.wvalid)
        )

        return ack

    def write_dataflow(self, data, counter=None, cond=None, when=None):
        """
        @return done
        'data' and 'when' must be dataflow variables
        """
        raise TypeError('lite interface support no dataflow operation.')

    def read_request(self, addr, length=1, cond=None):
        """
        @return ack
        """
        if self._read_disabled:
            raise TypeError('Read disabled.')

        if length != 1:
            raise ValueError('length must be 1 for lite-interface.')

        if cond is not None:
            self.seq.If(cond)

        ack = vtypes.Ors(self.raddr.arready, vtypes.Not(self.raddr.arvalid))

        self.seq.If(ack)(
            self.raddr.araddr(addr),
            self.raddr.arvalid(1)
        )

        # de-assert
        self.seq.Delay(1)(
            self.raddr.arvalid(0)
        )

        # retry
        self.seq.If(vtypes.Ands(self.raddr.arvalid, vtypes.Not(self.raddr.arready)))(
            self.raddr.arvalid(self.raddr.arvalid)
        )

        return ack

    def read_data(self, cond=None):
        """
        @return data, valid
        """
        if self._read_disabled:
            raise TypeError('Read disabled.')

        ready = make_condition(cond)
        val = 1 if ready is None else ready

        _connect_ready(self.rdata.rready._get_module(), self.rdata.rready, val)

        ack = vtypes.Ands(self.rdata.rready, self.rdata.rvalid)
        data = self.rdata.rdata
        valid = ack

        return data, valid

    def read_dataflow(self, counter=None, cond=None, point=0, signed=True):
        """
        @return data, last, done
        """
        raise TypeError('lite interface support no dataflow operation.')

    def connect(self, ports, name):
        if not self.noio:
            raise ValueError('I/O ports can not be connected to others.')

        awaddr = ports['_'.join([name, 'awaddr'])]
        awvalid = ports['_'.join([name, 'awvalid'])]
        awready = ports['_'.join([name, 'awready'])]

        awaddr.connect(self.waddr.awaddr)
        awvalid.connect(self.waddr.awvalid)
        self.waddr.awready.connect(awready)

        wdata = ports['_'.join([name, 'wdata'])]
        wstrb = ports['_'.join([name, 'wstrb'])]
        wvalid = ports['_'.join([name, 'wvalid'])]
        wready = ports['_'.join([name, 'wready'])]

        wdata.connect(self.wdata.wdata)
        wstrb.connect(self.wdata.wstrb)
        wvalid.connect(self.wdata.wvalid)
        self.wdata.wready.connect(wready)

        bresp = ports['_'.join([name, 'bresp'])]
        bvalid = ports['_'.join([name, 'bvalid'])]
        bready = ports['_'.join([name, 'bready'])]

        self.wresp.bresp.connect(bresp)
        self.wresp.bvalid.connect(bvalid)
        bready.connect(self.wresp.bready)

        araddr = ports['_'.join([name, 'araddr'])]
        arvalid = ports['_'.join([name, 'arvalid'])]
        arready = ports['_'.join([name, 'arready'])]

        araddr.connect(self.raddr.araddr)
        arvalid.connect(self.raddr.arvalid)
        self.raddr.arready.connect(arready)

        rdata = ports['_'.join([name, 'rdata'])]
        rresp = ports['_'.join([name, 'rresp'])]
        rvalid = ports['_'.join([name, 'rvalid'])]
        rready = ports['_'.join([name, 'rready'])]

        self.rdata.rdata.connect(rdata)
        self.rdata.rresp.connect(rresp)
        self.rdata.rvalid.connect(rvalid)
        rready.connect(self.rdata.rready)


class AxiSlave(object):
    burst_size_width = 8

    def __init__(self, m, name, clk, rst, datawidth=32, addrwidth=32,
                 id_width=1, user_width=1,
                 burst_mode=BURST_INCR, cache_mode=CACHE_HP, user_value=USER_DEFAULT,
                 noio=False, nodataflow=False):

        self.m = m
        self.name = name

        self.clk = clk
        self.rst = rst

        self.datawidth = datawidth
        self.addrwidth = addrwidth
        self.id_width = id_width
        self.user_width = user_width

        self.noio = noio

        if not hasattr(self.m, 'slavebus'):
            self.m.slavebus = []

        self.m.slavebus.append(self)

        itype = util.t_Wire if noio else None
        otype = util.t_Wire if noio else None

        self.waddr = AxiSlaveWriteAddress(m, name, datawidth, addrwidth,
                                          id_width, user_width, itype, otype)
        self.wdata = AxiSlaveWriteData(m, name, datawidth, addrwidth,
                                       id_width, user_width, itype, otype)
        self.wresp = AxiSlaveWriteResponse(m, name, datawidth, addrwidth,
                                           id_width, user_width, itype, otype)
        self.raddr = AxiSlaveReadAddress(m, name, datawidth, addrwidth,
                                         id_width, user_width, itype, otype)

        itype = util.t_Reg if noio else None

        self.rdata = AxiSlaveReadData(m, name, datawidth, addrwidth,
                                      id_width, user_width, itype, otype)

        self.seq = Seq(m, name, clk, rst)

        # default values
        self.wresp.bresp.assign(0)
        self.wresp.buser.assign(user_value)
        self.rdata.rresp.assign(0)
        self.rdata.ruser.assign(user_value)

        # write response
        self.seq.If(self.waddr.awvalid, self.waddr.awready)(
            self.wresp.bid(self.waddr.awid)
        )
        self.seq.If(self.raddr.arvalid, self.raddr.arready)(
            self.rdata.rid(self.raddr.arid)
        )
        self.seq.If(self.wresp.bvalid, self.wresp.bready)(
            self.wresp.bvalid(0)
        )
        self.seq.If(self.wdata.wvalid, self.wdata.wready, self.wdata.wlast)(
            self.wresp.bvalid(1)
        )

        self.write_counters = []
        self.read_counters = []

        if nodataflow:
            self.df = None
        else:
            self.df = DataflowManager(self.m, self.clk, self.rst)

        self._write_disabled = False
        self._read_disabled = False

    def disable_write(self):
        self.waddr.awready.assign(0)
        self.wdata.wready.assign(0)

        self._write_disabled = True

    def disable_read(self):
        self.raddr.arready.assign(0)

        ports = [self.rdata.rvalid(0),
                 self.rdata.rlast(0)]

        self.seq(
            *ports
        )

        self._read_disabled = True

    def pull_request(self, cond, counter=None):
        """
        @return addr, counter, readvalid, writevalid
        """
        if counter is not None and not isinstance(counter, vtypes.Reg):
            raise TypeError("counter must be Reg or None.")

        if counter is None:
            counter = self.m.TmpReg(self.burst_size_width + 1, initval=0)

        ready = make_condition(cond)

        write_ack = vtypes.Ands(self.waddr.awready, self.waddr.awvalid)
        read_ack = vtypes.Ands(self.raddr.arready, self.raddr.arvalid)
        addr = self.m.TmpReg(self.addrwidth, initval=0)
        writevalid = self.m.TmpReg(initval=0)
        readvalid = self.m.TmpReg(initval=0)

        prev_awvalid = self.m.TmpReg(initval=0)
        self.seq(
            prev_awvalid(self.waddr.awvalid)
        )
        prev_arvalid = self.m.TmpReg(initval=0)
        self.seq(
            prev_arvalid(self.raddr.arvalid)
        )

        writeval = (vtypes.Ands(vtypes.Not(writevalid), vtypes.Not(readvalid),
                                prev_awvalid) if ready is None else
                    vtypes.Ands(ready, vtypes.Not(writevalid), vtypes.Not(readvalid),
                                prev_awvalid))
        readval = (vtypes.Ands(vtypes.Not(readvalid), vtypes.Not(writevalid),
                               prev_arvalid) if ready is None else
                   vtypes.Ands(ready, vtypes.Not(readvalid), vtypes.Not(writevalid),
                               prev_arvalid))

        _connect_ready(self.waddr.awready._get_module(),
                       self.waddr.awready, writeval)
        _connect_ready(self.raddr.arready._get_module(),
                       self.raddr.arready, readval)

        self.seq(
            writevalid(0),
            readvalid(0)
        )
        self.seq.If(write_ack)(
            addr(self.waddr.awaddr),
            counter(self.waddr.awlen + 1),
            writevalid(1)
        ).Elif(read_ack)(
            addr(self.raddr.araddr),
            counter(self.raddr.arlen + 1),
            readvalid(1)
        )

        return addr, counter, readvalid, writevalid

    def pull_write_request(self, cond=None, counter=None):
        """
        @return addr, counter, valid
        """
        if self._write_disabled:
            raise TypeError('Write disabled.')

        if counter is not None and not isinstance(counter, vtypes.Reg):
            raise TypeError("counter must be Reg or None.")

        if counter is None:
            counter = self.m.TmpReg(self.burst_size_width + 1, initval=0)

        self.write_counters.append(counter)

        ready = make_condition(cond)

        ack = vtypes.Ands(self.waddr.awready, self.waddr.awvalid)
        addr = self.m.TmpReg(self.addrwidth, initval=0)
        valid = self.m.TmpReg(initval=0)

        prev_awvalid = self.m.TmpReg(initval=0)
        self.seq(
            prev_awvalid(self.waddr.awvalid)
        )

        val = (vtypes.Ands(vtypes.Not(valid), prev_awvalid) if ready is None else
               vtypes.Ands(ready, vtypes.Not(valid), prev_awvalid))

        _connect_ready(self.waddr.awready._get_module(),
                       self.waddr.awready, val)

        self.seq.If(ack)(
            addr(self.waddr.awaddr),
            counter(self.waddr.awlen + 1)
        )

        self.seq(
            valid(ack)
        )

        return addr, counter, valid

    def pull_write_data(self, counter=None, cond=None):
        """
        @return data, mask, valid, last
        """
        if self._write_disabled:
            raise TypeError('Write disabled.')

        if counter is not None and not isinstance(counter, vtypes.Reg):
            raise TypeError("counter must be Reg or None.")

        if counter is None:
            counter = self.write_counters[-1]

        ready = make_condition(cond)
        val = 1 if ready is None else ready

        _connect_ready(self.wdata.wready._get_module(), self.wdata.wready, val)

        ack = vtypes.Ands(self.wdata.wready, self.wdata.wvalid)
        data = self.wdata.wdata
        mask = self.wdata.wstrb
        valid = ack
        last = self.wdata.wlast

        self.seq.If(vtypes.Ands(ack, counter > 0))(
            counter.dec()
        )

        return data, mask, valid, last

    def pull_write_dataflow(self, counter=None, cond=None):
        """
        @return data, mask, last, done
        """

        if self._write_disabled:
            raise TypeError('Write disabled.')

        if counter is not None and not isinstance(counter, vtypes.Reg):
            raise TypeError("counter must be Reg or None.")

        if counter is None:
            counter = self.write_counters[-1]

        data_ready = self.m.TmpWire()
        mask_ready = self.m.TmpWire()
        last_ready = self.m.TmpWire()
        data_ready.assign(1)
        mask_ready.assign(1)
        last_ready.assign(1)

        if cond is None:
            cond = (data_ready, last_ready)
        elif isinstance(cond, (tuple, list)):
            cond = tuple(list(cond) + [data_ready, last_ready])
        else:
            cond = (cond, data_ready, last_ready)

        ready = make_condition(*cond)
        val = 1 if ready is None else ready

        _connect_ready(self.wdata.wready._get_module(), self.wdata.wready, val)

        ack = vtypes.Ands(self.wdata.wready, self.wdata.wvalid)
        data = self.wdata.wdata
        mask = self.wdata.wstrb
        valid = self.wdata.wvalid
        last = self.wdata.wlast

        self.seq.If(vtypes.Ands(ack, counter > 0))(
            counter.dec()
        )

        df_data = self.df.Variable(data, valid, data_ready, signed=False)
        df_mask = self.df.Variable(mask, valid, mask_ready,
                                   width=self.datawidth // 4, signed=False)
        df_last = self.df.Variable(
            last, valid, last_ready, width=1, signed=False)
        done = vtypes.Ands(last, self.wdata.wvalid, self.wdata.wready)

        return df_data, df_mask, df_last, done

    def pull_read_request(self, cond=None, counter=None):
        """
        @return addr, counter, valid
        """
        if self._read_disabled:
            raise TypeError('Read disabled.')

        if counter is not None and not isinstance(counter, vtypes.Reg):
            raise TypeError("counter must be Reg or None.")

        if counter is None:
            counter = self.m.TmpReg(self.burst_size_width + 1, initval=0)

        self.read_counters.append(counter)

        ready = make_condition(cond)

        ack = vtypes.Ands(self.raddr.arready, self.raddr.arvalid)
        addr = self.m.TmpReg(self.addrwidth, initval=0)
        valid = self.m.TmpReg(initval=0)

        prev_arvalid = self.m.TmpReg(initval=0)
        self.seq(
            prev_arvalid(self.raddr.arvalid)
        )

        val = (vtypes.Ands(vtypes.Not(valid), prev_arvalid) if ready is None else
               vtypes.Ands(ready, vtypes.Not(valid), prev_arvalid))

        _connect_ready(self.raddr.arready._get_module(),
                       self.raddr.arready, val)

        self.seq.If(ack)(
            addr(self.raddr.araddr),
            counter(self.raddr.arlen + 1)
        )

        self.seq(
            valid(ack)
        )

        return addr, counter, valid

    def push_read_data(self, data, counter=None, cond=None):
        """
        @return ack, last
        """
        if self._read_disabled:
            raise TypeError('Read disabled.')

        if counter is not None and not isinstance(counter, vtypes.Reg):
            raise TypeError("counter must be Reg or None.")

        if counter is None:
            counter = self.read_counters[-1]

        if cond is not None:
            self.seq.If(cond)

        ack = vtypes.Ands(counter > 0,
                          vtypes.Ors(self.rdata.rready, vtypes.Not(self.rdata.rvalid)))
        last = self.m.TmpReg(initval=0)

        self.seq.If(vtypes.Ands(ack, counter > 0))(
            self.rdata.rdata(data),
            self.rdata.rvalid(1),
            self.rdata.rlast(0),
            counter.dec()
        )
        self.seq.Then().If(counter == 1)(
            self.rdata.rlast(1),
            last(1)
        )

        # de-assert
        self.seq.Delay(1)(
            self.rdata.rvalid(0),
            self.rdata.rlast(0),
            last(0)
        )

        # retry
        self.seq.If(vtypes.Ands(self.rdata.rvalid, vtypes.Not(self.rdata.rready)))(
            self.rdata.rvalid(self.rdata.rvalid),
            self.rdata.rlast(self.rdata.rlast),
            last(last)
        )

        return ack, last

    def push_read_dataflow(self, data, counter=None, cond=None):
        """ 
        @return done
        """

        if self._read_disabled:
            raise TypeError('Read disabled.')

        if counter is not None and not isinstance(counter, vtypes.Reg):
            raise TypeError("counter must be Reg or None.")

        if counter is None:
            counter = self.read_counters[-1]

        ack = vtypes.Ands(counter > 0,
                          vtypes.Ors(self.rdata.rready, vtypes.Not(self.rdata.rvalid)))
        last = self.m.TmpReg(initval=0)

        if cond is None:
            cond = ack
        else:
            cond = (cond, ack)

        raw_data, raw_valid = data.read(cond=cond)

        # write condition
        self.seq.If(raw_valid)

        self.seq.If(vtypes.Ands(ack, counter > 0))(
            self.rdata.rdata(raw_data),
            self.rdata.rvalid(1),
            self.rdata.rlast(0),
            counter.dec()
        )
        self.seq.Then().If(counter == 1)(
            self.rdata.rlast(1),
            last(1)
        )

        # de-assert
        self.seq.Delay(1)(
            self.rdata.rvalid(0),
            self.rdata.rlast(0),
            last(0)
        )

        # retry
        self.seq.If(vtypes.Ands(self.rdata.rvalid, vtypes.Not(self.rdata.rready)))(
            self.rdata.rvalid(self.rdata.rvalid),
            self.rdata.rlast(self.rdata.rlast),
            last(last)
        )

        done = vtypes.Ands(last, self.rdata.rvalid, self.rdata.rready)

        return done

    def connect(self, ports, name):
        if not self.noio:
            raise ValueError('I/O ports can not be connected to others.')

        awid = ports['_'.join([name, 'awid'])]
        awaddr = ports['_'.join([name, 'awaddr'])]
        awlen = ports['_'.join([name, 'awlen'])]
        awsize = ports['_'.join([name, 'awsize'])]
        awburst = ports['_'.join([name, 'awburst'])]
        awlock = ports['_'.join([name, 'awlock'])]
        awcache = ports['_'.join([name, 'awcache'])]
        awprot = ports['_'.join([name, 'awprot'])]
        awqos = ports['_'.join([name, 'awqos'])]
        awuser = ports['_'.join([name, 'awuser'])]
        awvalid = ports['_'.join([name, 'awvalid'])]
        awready = ports['_'.join([name, 'awready'])]

        self.waddr.awid.connect(awid)
        self.waddr.awaddr.connect(awaddr)
        self.waddr.awlen.connect(awlen)
        self.waddr.awsize.connect(awsize)
        self.waddr.awburst.connect(awburst)
        self.waddr.awlock.connect(awlock)
        self.waddr.awcache.connect(awcache)
        self.waddr.awprot.connect(awprot)
        self.waddr.awqos.connect(awqos)
        self.waddr.awuser.connect(awuser)
        self.waddr.awvalid.connect(awvalid)
        awready.connect(self.waddr.awready)

        wdata = ports['_'.join([name, 'wdata'])]
        wstrb = ports['_'.join([name, 'wstrb'])]
        wlast = ports['_'.join([name, 'wlast'])]
        wuser = ports['_'.join([name, 'wuser'])]
        wvalid = ports['_'.join([name, 'wvalid'])]
        wready = ports['_'.join([name, 'wready'])]

        self.wdata.wdata.connect(wdata)
        self.wdata.wstrb.connect(wstrb)
        self.wdata.wlast.connect(wlast)
        self.wdata.wuser.connect(wuser)
        self.wdata.wvalid.connect(wvalid)
        wready.connect(self.wdata.wready)

        bid = ports['_'.join([name, 'bid'])]
        bresp = ports['_'.join([name, 'bresp'])]
        buser = ports['_'.join([name, 'buser'])]
        bvalid = ports['_'.join([name, 'bvalid'])]
        bready = ports['_'.join([name, 'bready'])]

        bid.connect(self.wresp.bid)
        bresp.connect(self.wresp.bresp)
        buser.connect(self.wresp.buser)
        bvalid.connect(self.wresp.bvalid)
        self.wresp.bready.connect(bready)

        arid = ports['_'.join([name, 'arid'])]
        araddr = ports['_'.join([name, 'araddr'])]
        arlen = ports['_'.join([name, 'arlen'])]
        arsize = ports['_'.join([name, 'arsize'])]
        arburst = ports['_'.join([name, 'arburst'])]
        arlock = ports['_'.join([name, 'arlock'])]
        arcache = ports['_'.join([name, 'arcache'])]
        arprot = ports['_'.join([name, 'arprot'])]
        arqos = ports['_'.join([name, 'arqos'])]
        aruser = ports['_'.join([name, 'aruser'])]
        arvalid = ports['_'.join([name, 'arvalid'])]
        arready = ports['_'.join([name, 'arready'])]

        self.raddr.arid.connect(arid)
        self.raddr.araddr.connect(araddr)
        self.raddr.arlen.connect(arlen)
        self.raddr.arsize.connect(arsize)
        self.raddr.arburst.connect(arburst)
        self.raddr.arlock.connect(arlock)
        self.raddr.arcache.connect(arcache)
        self.raddr.arprot.connect(arprot)
        self.raddr.arqos.connect(arqos)
        self.raddr.aruser.connect(aruser)
        self.raddr.arvalid.connect(arvalid)
        arready.connect(self.raddr.arready)

        rid = ports['_'.join([name, 'rid'])]
        rdata = ports['_'.join([name, 'rdata'])]
        rresp = ports['_'.join([name, 'rresp'])]
        rlast = ports['_'.join([name, 'rlast'])]
        ruser = ports['_'.join([name, 'ruser'])]
        rvalid = ports['_'.join([name, 'rvalid'])]
        rready = ports['_'.join([name, 'rready'])]

        rid.connect(self.rdata.rid)
        rdata.connect(self.rdata.rdata)
        rresp.connect(self.rdata.rresp)
        rlast.connect(self.rdata.rlast)
        ruser.connect(self.rdata.ruser)
        rvalid.connect(self.rdata.rvalid)
        self.rdata.rready.connect(rready)


class AxiLiteSlave(AxiSlave):

    def __init__(self, m, name, clk, rst, datawidth=32, addrwidth=32,
                 noio=False, nodataflow=False):

        self.m = m
        self.name = name

        self.clk = clk
        self.rst = rst

        self.datawidth = datawidth
        self.addrwidth = addrwidth

        self.noio = noio

        if not hasattr(self.m, 'slavebus'):
            self.m.slavebus = []

        self.m.slavebus.append(self)

        itype = util.t_Wire if noio else None
        otype = util.t_Wire if noio else None

        self.waddr = AxiLiteSlaveWriteAddress(m, name, datawidth, addrwidth,
                                              itype, otype)
        self.wdata = AxiLiteSlaveWriteData(m, name, datawidth, addrwidth,
                                           itype, otype)
        self.wresp = AxiLiteSlaveWriteResponse(m, name, datawidth, addrwidth,
                                               itype, otype)
        self.raddr = AxiLiteSlaveReadAddress(m, name, datawidth, addrwidth,
                                             itype, otype)

        itype = util.t_Reg if noio else None

        self.rdata = AxiLiteSlaveReadData(m, name, datawidth, addrwidth,
                                          itype, otype)

        self.seq = Seq(m, name, clk, rst)

        # default values
        self.wresp.bresp.assign(0)
        self.rdata.rresp.assign(0)

        # write response
        self.seq.If(self.wresp.bvalid, self.wresp.bready)(
            self.wresp.bvalid(0)
        )
        self.seq.If(self.wdata.wvalid, self.wdata.wready)(
            self.wresp.bvalid(1)
        )

        if nodataflow:
            self.df = None
        else:
            self.df = DataflowManager(self.m, self.clk, self.rst)

        self._write_disabled = False
        self._read_disabled = False

    def disable_write(self):
        self.waddr.awready.assign(0)
        self.wdata.wready.assign(0)

        self._write_disabled = True

    def disable_read(self):
        self.raddr.arready.assign(0)

        ports = [self.rdata.rvalid(0)]

        self.seq(
            *ports
        )

        self._read_disabled = True

    def pull_request(self, cond):
        """
        @return addr, readvalid, writevalid
        """

        ready = make_condition(cond)

        write_ack = vtypes.Ands(self.waddr.awready, self.waddr.awvalid)
        read_ack = vtypes.Ands(self.raddr.arready, self.raddr.arvalid)
        addr = self.m.TmpReg(self.addrwidth, initval=0)
        writevalid = self.m.TmpReg(initval=0)
        readvalid = self.m.TmpReg(initval=0)

        prev_awvalid = self.m.TmpReg(initval=0)
        self.seq(
            prev_awvalid(self.waddr.awvalid)
        )
        prev_arvalid = self.m.TmpReg(initval=0)
        self.seq(
            prev_arvalid(self.raddr.arvalid)
        )

        writeval = (vtypes.Ands(vtypes.Not(writevalid), vtypes.Not(readvalid),
                                prev_awvalid) if ready is None else
                    vtypes.Ands(ready, vtypes.Not(writevalid), vtypes.Not(readvalid),
                                prev_awvalid))
        readval = (vtypes.Ands(vtypes.Not(readvalid), vtypes.Not(writevalid),
                               prev_arvalid) if ready is None else
                   vtypes.Ands(ready, vtypes.Not(readvalid), vtypes.Not(writevalid),
                               prev_arvalid))

        _connect_ready(self.waddr.awready._get_module(),
                       self.waddr.awready, writeval)
        _connect_ready(self.raddr.arready._get_module(),
                       self.raddr.arready, readval)

        self.seq(
            writevalid(0),
            readvalid(0)
        )
        self.seq.If(write_ack)(
            addr(self.waddr.awaddr),
            writevalid(1)
        ).Elif(read_ack)(
            addr(self.raddr.araddr),
            readvalid(1)
        )

        return addr, readvalid, writevalid

    def pull_write_request(self, cond=None):
        """
        @return addr, valid
        """
        if self._write_disabled:
            raise TypeError('Write disabled.')

        ready = make_condition(cond)

        ack = vtypes.Ands(self.waddr.awready, self.waddr.awvalid)
        addr = self.m.TmpReg(self.addrwidth, initval=0)
        valid = self.m.TmpReg(initval=0)

        prev_awvalid = self.m.TmpReg(initval=0)
        self.seq(
            prev_awvalid(self.waddr.awvalid)
        )

        val = (vtypes.Ands(vtypes.Not(valid), prev_awvalid) if ready is None else
               vtypes.Ands(ready, vtypes.Not(valid), prev_awvalid))

        _connect_ready(self.waddr.awready._get_module(),
                       self.waddr.awready, val)

        self.seq.If(ack)(
            addr(self.waddr.awaddr),
        )

        self.seq(
            valid(ack)
        )

        return addr, valid

    def pull_write_data(self, cond=None):
        """
        @return data, mask, valid
        """
        if self._write_disabled:
            raise TypeError('Write disabled.')

        ready = make_condition(cond)
        val = 1 if ready is None else ready

        _connect_ready(self.wdata.wready._get_module(), self.wdata.wready, val)

        ack = vtypes.Ands(self.wdata.wready, self.wdata.wvalid)
        data = self.wdata.wdata
        mask = self.wdata.wstrb
        valid = ack

        return data, mask, valid

    def pull_write_dataflow(self, counter=None, cond=None):
        """
        @return data, mask, last, done
        """
        raise TypeError('lite interface support no dataflow operation.')

    def pull_read_request(self, cond=None):
        """
        @return addr, valid
        """
        if self._read_disabled:
            raise TypeError('Read disabled.')

        ready = make_condition(cond)

        ack = vtypes.Ands(self.raddr.arready, self.raddr.arvalid)
        addr = self.m.TmpReg(self.addrwidth, initval=0)
        valid = self.m.TmpReg(initval=0)

        prev_arvalid = self.m.TmpReg(initval=0)
        self.seq(
            prev_arvalid(self.raddr.arvalid)
        )

        val = (vtypes.Ands(vtypes.Not(valid), prev_arvalid) if ready is None else
               vtypes.Ands(ready, vtypes.Not(valid), prev_arvalid))

        _connect_ready(self.raddr.arready._get_module(),
                       self.raddr.arready, val)

        self.seq.If(ack)(
            addr(self.raddr.araddr)
        )

        self.seq(
            valid(ack)
        )

        return addr, valid

    def push_read_data(self, data, cond=None):
        """
        @return ack
        """
        if self._read_disabled:
            raise TypeError('Read disabled.')

        if cond is not None:
            self.seq.If(cond)

        ack = vtypes.Ors(self.rdata.rready, vtypes.Not(self.rdata.rvalid))

        self.seq.If(ack)(
            self.rdata.rdata(data),
            self.rdata.rvalid(1)
        )

        # de-assert
        self.seq.Delay(1)(
            self.rdata.rvalid(0)
        )

        # retry
        self.seq.If(vtypes.Ands(self.rdata.rvalid, vtypes.Not(self.rdata.rready)))(
            self.rdata.rvalid(self.rdata.rvalid)
        )

        return ack

    def push_read_dataflow(self, data, counter=None, cond=None):
        """ 
        @return done
        """
        raise TypeError('lite interface support no dataflow operation.')

    def connect(self, ports, name):
        if not self.noio:
            raise ValueError('I/O ports can not be connected to others.')

        awaddr = ports['_'.join([name, 'awaddr'])]
        awvalid = ports['_'.join([name, 'awvalid'])]
        awready = ports['_'.join([name, 'awready'])]

        self.waddr.awaddr.connect(awaddr)
        self.waddr.awvalid.connect(awvalid)
        awready.connect(self.waddr.awready)

        wdata = ports['_'.join([name, 'wdata'])]
        wstrb = ports['_'.join([name, 'wstrb'])]
        wvalid = ports['_'.join([name, 'wvalid'])]
        wready = ports['_'.join([name, 'wready'])]

        self.wdata.wdata.connect(wdata)
        self.wdata.wstrb.connect(wstrb)
        self.wdata.wvalid.connect(wvalid)
        wready.connect(self.wdata.wready)

        bresp = ports['_'.join([name, 'bresp'])]
        bvalid = ports['_'.join([name, 'bvalid'])]
        bready = ports['_'.join([name, 'bready'])]

        bresp.connect(self.wresp.bresp)
        bvalid.connect(self.wresp.bvalid)
        self.wresp.bready.connect(bready)

        araddr = ports['_'.join([name, 'araddr'])]
        arvalid = ports['_'.join([name, 'arvalid'])]
        arready = ports['_'.join([name, 'arready'])]

        self.raddr.araddr.connect(araddr)
        self.raddr.arvalid.connect(arvalid)
        arready.connect(self.raddr.arready)

        rdata = ports['_'.join([name, 'rdata'])]
        rresp = ports['_'.join([name, 'rresp'])]
        rvalid = ports['_'.join([name, 'rvalid'])]
        rready = ports['_'.join([name, 'rready'])]

        rdata.connect(self.rdata.rdata)
        rresp.connect(self.rdata.rresp)
        rvalid.connect(self.rdata.rvalid)
        self.rdata.rready.connect(rready)


class AxiMemoryModel(AxiSlave):
    __intrinsics__ = ('read', 'write',
                      'read_word', 'write_word')

    def __init__(self, m, name, clk, rst, datawidth=32, addrwidth=32,
                 mem_datawidth=32, mem_addrwidth=20,
                 memimg=None, memimg_name=None,
                 memimg_datawidth=None,
                 write_delay=10, read_delay=10, sleep=4,
                 id_width=1, user_width=1,
                 burst_mode=BURST_INCR, cache_mode=CACHE_HP, user_value=USER_DEFAULT):

        if mem_datawidth % 8 != 0:
            raise ValueError('mem_datawidth must be a multiple of 8')

        self.m = m
        self.name = name

        self.clk = clk
        self.rst = rst

        self.datawidth = datawidth
        self.addrwidth = addrwidth
        self.id_width = id_width
        self.user_width = user_width

        self.mem_datawidth = mem_datawidth
        self.mem_addrwidth = mem_addrwidth

        itype = util.t_Reg
        otype = util.t_Wire

        self.waddr = AxiSlaveWriteAddress(m, name, datawidth, addrwidth,
                                          id_width, user_width, itype, otype)
        self.wdata = AxiSlaveWriteData(m, name, datawidth, addrwidth,
                                       id_width, user_width, itype, otype)
        self.wresp = AxiSlaveWriteResponse(m, name, datawidth, addrwidth,
                                           id_width, user_width, itype, otype)
        self.raddr = AxiSlaveReadAddress(m, name, datawidth, addrwidth,
                                         id_width, user_width, itype, otype)
        self.rdata = AxiSlaveReadData(m, name, datawidth, addrwidth,
                                      id_width, user_width, itype, otype)

        # default values
        self.wresp.bresp.assign(0)
        self.wresp.buser.assign(user_value)
        self.rdata.rresp.assign(0)
        self.rdata.ruser.assign(user_value)

        self.fsm = FSM(self.m, '_'.join(['', self.name, 'fsm']), clk, rst)

        # write response
        self.fsm.seq.If(self.waddr.awvalid, self.waddr.awready)(
            self.wresp.bid(self.waddr.awid)
        )
        self.fsm.seq.If(self.raddr.arvalid, self.raddr.arready)(
            self.rdata.rid(self.raddr.arid)
        )
        self.fsm.seq.If(self.wresp.bvalid, self.wresp.bready)(
            self.wresp.bvalid(0)
        )
        self.fsm.seq.If(self.wdata.wvalid, self.wdata.wready, self.wdata.wlast)(
            self.wresp.bvalid(1)
        )

        self.mem = self.m.Reg(
            '_'.join(['', self.name, 'mem']), 8, vtypes.Int(2) ** self.mem_addrwidth)

        if memimg is None:
            if memimg_name is None:
                memimg_name = '_'.join(['', self.name, 'memimg', '.out'])
            size = 2 ** self.mem_addrwidth
            width = self.mem_datawidth
            self._make_img(memimg_name, size, width)

        elif isinstance(memimg, str):
            memimg_name = memimg

        else:
            if memimg_datawidth is None:
                memimg_datawidth = mem_datawidth
            if memimg_name is None:
                memimg_name = '_'.join(['', self.name, 'memimg', '.out'])
            to_memory_image(memimg_name, memimg, datawidth=memimg_datawidth)

        self.m.Initial(
            vtypes.Systask('readmemh', memimg_name, self.mem)
        )

        self._make_fsm(write_delay, read_delay, sleep)

    @staticmethod
    def _make_img(filename, size, width):
        with open(filename, 'w') as f:
            for i in range(size * 8 // width):
                s = (''.join(['%0', '%d' %
                              int(math.ceil(width / 4)), 'x'])) % i
                for w in range(int(math.ceil(width / 4)), 0, -2):
                    f.write('%s\n' % s[w - 2:w])

    def _make_fsm(self, write_delay=10, read_delay=10, sleep=4):
        write_mode = 100
        read_mode = 200

        self.fsm.If(self.waddr.awvalid).goto(write_mode)
        self.fsm.If(self.raddr.arvalid).goto(read_mode)

        write_count = self.m.Reg(
            '_'.join(['', 'write_count']), self.addrwidth + 1, initval=0)
        write_addr = self.m.Reg(
            '_'.join(['', 'write_addr']), self.addrwidth, initval=0)
        read_count = self.m.Reg(
            '_'.join(['', 'read_count']), self.addrwidth + 1, initval=0)
        read_addr = self.m.Reg(
            '_'.join(['', 'read_addr']), self.addrwidth, initval=0)

        if sleep > 0:
            sleep_count = self.m.Reg(
                '_'.join(['', 'sleep_count']), self.addrwidth + 1, initval=0)

            self.fsm.seq(
                sleep_count.inc()
            )
            self.fsm.seq.If(sleep_count == sleep - 1)(
                sleep_count(0)
            )

        # write mode
        self.fsm._set_index(write_mode)

        # awvalid and awready
        self.fsm.If(self.waddr.awvalid)(
            self.waddr.awready(1),
            write_addr(self.waddr.awaddr),
            write_count(self.waddr.awlen + 1)
        )
        self.fsm.Delay(1)(
            self.waddr.awready(0)
        )
        self.fsm.If(vtypes.Not(self.waddr.awvalid)).goto_init()
        self.fsm.If(self.waddr.awvalid).goto_next()

        # delay
        for _ in range(write_delay):
            self.fsm.goto_next()

        # wready
        self.fsm(
            self.wdata.wready(1)
        )
        self.fsm.goto_next()

        # wdata -> mem
        for i in range(int(self.datawidth / 8)):
            self.fsm.If(self.wdata.wvalid, self.wdata.wstrb[i])(
                self.mem[write_addr + i](self.wdata.wdata[i * 8:i * 8 + 8])
            )

        self.fsm.If(self.wdata.wvalid, self.wdata.wready)(
            write_addr.add(int(self.datawidth / 8)),
            write_count.dec()
        )

        # sleep
        if sleep > 0:
            self.fsm.If(sleep_count == sleep - 1)(
                self.wdata.wready(0)
            ).Else(
                self.wdata.wready(1)
            )

        # write complete
        self.fsm.If(self.wdata.wvalid, self.wdata.wready, write_count == 1)(
            self.wdata.wready(0)
        )
        self.fsm.Then().goto_init()

        # read mode
        self.fsm._set_index(read_mode)

        # arvalid and arready
        self.fsm.If(self.raddr.arvalid)(
            self.raddr.arready(1),
            read_addr(self.raddr.araddr),
            read_count(self.raddr.arlen + 1)
        )
        self.fsm.Delay(1)(
            self.raddr.arready(0)
        )
        self.fsm.If(vtypes.Not(self.raddr.arvalid)).goto_init()
        self.fsm.If(self.raddr.arvalid).goto_next()

        # delay
        for _ in range(read_delay):
            self.fsm.goto_next()

        # mem -> rdata
        for i in range(int(self.datawidth / 8)):
            self.fsm.If(vtypes.Or(self.rdata.rready, vtypes.Not(self.rdata.rvalid)))(
                self.rdata.rdata[i * 8:i * 8 + 8](self.mem[read_addr + i])
            )

        if sleep > 0:
            self.fsm.If(sleep_count < sleep - 1, read_count > 0,
                        vtypes.Or(self.rdata.rready, vtypes.Not(self.rdata.rvalid)))(
                self.rdata.rvalid(1),
                read_addr.add(int(self.datawidth / 8)),
                read_count.dec()
            )
            self.fsm.If(sleep_count < sleep - 1, read_count == 1,
                        vtypes.Or(self.rdata.rready, vtypes.Not(self.rdata.rvalid)))(
                self.rdata.rlast(1)
            )
        else:
            self.fsm.If(read_count > 0,
                        vtypes.Or(self.rdata.rready, vtypes.Not(self.rdata.rvalid)))(
                self.rdata.rvalid(1),
                read_addr.add(int(self.datawidth / 8)),
                read_count.dec()
            )
            self.fsm.If(read_count == 1,
                        vtypes.Or(self.rdata.rready, vtypes.Not(self.rdata.rvalid)))(
                self.rdata.rlast(1)
            )

        # de-assert
        self.fsm.Delay(1)(
            self.rdata.rvalid(0),
            self.rdata.rlast(0)
        )

        # retry
        self.fsm.If(self.rdata.rvalid, vtypes.Not(self.rdata.rready))(
            self.rdata.rvalid(self.rdata.rvalid),
            self.rdata.rdata(self.rdata.rdata),
            self.rdata.rlast(self.rdata.rlast)
        )

        # read complete
        self.fsm.If(self.rdata.rvalid, self.rdata.rready,
                    read_count == 0).goto_init()

    def connect(self, ports, name):
        awid = ports['_'.join([name, 'awid'])]
        awaddr = ports['_'.join([name, 'awaddr'])]
        awlen = ports['_'.join([name, 'awlen'])]
        awsize = ports['_'.join([name, 'awsize'])]
        awburst = ports['_'.join([name, 'awburst'])]
        awlock = ports['_'.join([name, 'awlock'])]
        awcache = ports['_'.join([name, 'awcache'])]
        awprot = ports['_'.join([name, 'awprot'])]
        awqos = ports['_'.join([name, 'awqos'])]
        awuser = ports['_'.join([name, 'awuser'])]
        awvalid = ports['_'.join([name, 'awvalid'])]
        awready = ports['_'.join([name, 'awready'])]

        self.waddr.awid.connect(awid)
        self.waddr.awaddr.connect(awaddr)
        self.waddr.awlen.connect(awlen)
        self.waddr.awsize.connect(awsize)
        self.waddr.awburst.connect(awburst)
        self.waddr.awlock.connect(awlock)
        self.waddr.awcache.connect(awcache)
        self.waddr.awprot.connect(awprot)
        self.waddr.awqos.connect(awqos)
        self.waddr.awuser.connect(awuser)
        self.waddr.awvalid.connect(awvalid)
        awready.connect(self.waddr.awready)

        wdata = ports['_'.join([name, 'wdata'])]
        wstrb = ports['_'.join([name, 'wstrb'])]
        wlast = ports['_'.join([name, 'wlast'])]
        wuser = ports['_'.join([name, 'wuser'])]
        wvalid = ports['_'.join([name, 'wvalid'])]
        wready = ports['_'.join([name, 'wready'])]

        self.wdata.wdata.connect(wdata)
        self.wdata.wstrb.connect(wstrb)
        self.wdata.wlast.connect(wlast)
        self.wdata.wuser.connect(wuser)
        self.wdata.wvalid.connect(wvalid)
        wready.connect(self.wdata.wready)

        bid = ports['_'.join([name, 'bid'])]
        bresp = ports['_'.join([name, 'bresp'])]
        buser = ports['_'.join([name, 'buser'])]
        bvalid = ports['_'.join([name, 'bvalid'])]
        bready = ports['_'.join([name, 'bready'])]

        bid.connect(self.wresp.bid)
        bresp.connect(self.wresp.bresp)
        buser.connect(self.wresp.buser)
        bvalid.connect(self.wresp.bvalid)
        self.wresp.bready.connect(bready)

        arid = ports['_'.join([name, 'arid'])]
        araddr = ports['_'.join([name, 'araddr'])]
        arlen = ports['_'.join([name, 'arlen'])]
        arsize = ports['_'.join([name, 'arsize'])]
        arburst = ports['_'.join([name, 'arburst'])]
        arlock = ports['_'.join([name, 'arlock'])]
        arcache = ports['_'.join([name, 'arcache'])]
        arprot = ports['_'.join([name, 'arprot'])]
        arqos = ports['_'.join([name, 'arqos'])]
        aruser = ports['_'.join([name, 'aruser'])]
        arvalid = ports['_'.join([name, 'arvalid'])]
        arready = ports['_'.join([name, 'arready'])]

        self.raddr.arid.connect(arid)
        self.raddr.araddr.connect(araddr)
        self.raddr.arlen.connect(arlen)
        self.raddr.arsize.connect(arsize)
        self.raddr.arburst.connect(arburst)
        self.raddr.arlock.connect(arlock)
        self.raddr.arcache.connect(arcache)
        self.raddr.arprot.connect(arprot)
        self.raddr.arqos.connect(arqos)
        self.raddr.aruser.connect(aruser)
        self.raddr.arvalid.connect(arvalid)
        arready.connect(self.raddr.arready)

        rid = ports['_'.join([name, 'rid'])]
        rdata = ports['_'.join([name, 'rdata'])]
        rresp = ports['_'.join([name, 'rresp'])]
        rlast = ports['_'.join([name, 'rlast'])]
        ruser = ports['_'.join([name, 'ruser'])]
        rvalid = ports['_'.join([name, 'rvalid'])]
        rready = ports['_'.join([name, 'rready'])]

        rid.connect(self.rdata.rid)
        rdata.connect(self.rdata.rdata)
        rresp.connect(self.rdata.rresp)
        rlast.connect(self.rdata.rlast)
        ruser.connect(self.rdata.ruser)
        rvalid.connect(self.rdata.rvalid)
        self.rdata.rready.connect(rready)

    def read(self, fsm, addr):
        """ intrinsic for thread """

        cond = fsm.state == fsm.current
        rdata = self.m.TmpReg(self.mem_datawidth, initval=0, signed=True)
        num_bytes = self.mem_datawidth // 8

        fsm.If(cond)(
            rdata(vtypes.Cat(*reversed([self.mem[addr + i]
                                        for i in range(num_bytes)])))
        )
        fsm.goto_next()

        return rdata

    def write(self, fsm, addr, wdata):
        """ intrinsic for thread """

        cond = fsm.state == fsm.current
        num_bytes = self.mem_datawidth // 8

        wdata_wire = self.m.TmpWire(self.mem_datawidth)
        wdata_wire.assign(wdata)

        for i in range(num_bytes):
            self.fsm.seq.If(cond)(
                self.mem[addr + i](wdata_wire[i * 8:i * 8 + 8])
            )

        fsm.goto_next()

        return 0

    def read_word(self, fsm, word_index, byte_offset, bits=8):
        """ intrinsic method word-indexed read """

        cond = fsm.state == fsm.current
        rdata = self.m.TmpReg(bits, initval=0, signed=True)
        num_bytes = int(math.ceil(bits / 8))
        addr = vtypes.Add(byte_offset,
                          vtypes.Div(vtypes.Mul(word_index, bits), 8))
        shift = word_index * bits % 8

        raw_data = vtypes.Cat(*reversed([self.mem[addr + i]
                                         for i in range(num_bytes)]))

        fsm.If(cond)(
            rdata(raw_data >> shift)
        )
        fsm.goto_next()

        return rdata

    def write_word(self, fsm, word_index, byte_offset, wdata, bits=8):
        """ intrinsic method word-indexed write """

        cond = fsm.state == fsm.current
        rdata = self.m.TmpReg(bits, initval=0, signed=True)
        num_bytes = int(math.ceil(bits / 8))
        addr = vtypes.Add(byte_offset,
                          vtypes.Div(vtypes.Mul(word_index, bits), 8))
        shift = word_index * bits % 8

        wdata_wire = self.m.TmpWire(bits)
        wdata_wire.assign(wdata)
        mem_data = vtypes.Cat(*reversed([self.mem[addr + i]
                                         for i in range(num_bytes)]))
        mem_data_wire = self.m.TmpWire(8 * num_bytes)
        mem_data_wire.assign(mem_data)

        inv_mask = self.m.TmpWire(8 * num_bytes)
        inv_mask.assign(vtypes.Repeat(vtypes.Int(1, 1), bits) << shift)
        mask = self.m.TmpWire(8 * num_bytes)
        mask.assign(vtypes.Unot(inv_mask))

        raw_data = vtypes.Or(wdata_wire << shift,
                             vtypes.And(mem_data_wire, mask))
        raw_data_wire = self.m.TmpWire(8 * num_bytes)
        raw_data_wire.assign(raw_data)

        for i in range(num_bytes):
            self.fsm.seq.If(cond)(
                self.mem[addr + i](raw_data_wire[i * 8:i * 8 + 8])
            )

        fsm.goto_next()

        return 0


def make_memory_image(filename, length, pattern='inc', dtype=None,
                      datawidth=32, wordwidth=8, endian='little'):

    import numpy as np

    if dtype is None:
        dtype = np.int64

    if pattern == 'inc':
        l = list(range(length))
        array = np.array(l, dtype=dtype)
    else:
        array = np.zeros([length], dtype=dtype)

    to_memory_image(filename, array,
                    datawidth=datawidth, wordwidth=wordwidth,
                    endian=endian)


def to_memory_image(filename, array, length=None,
                    datawidth=32, wordwidth=8, endian='little'):

    import numpy as np

    if not isinstance(array, np.ndarray):
        array = np.array(array)

    array = np.reshape(array, [-1])

    if not isinstance(array[0], (int, np.int64, np.int32)):
        raise TypeError("not supported type: '%s'" %
                        str(type(array[0])))

    if length is not None:
        if len(array) > length:
            array = array[:length]
        elif len(array) < length:
            np.append(array, np.zeros([length - len(array)],
                                      dtype=array.dtype))

    num_hex = int(math.ceil(wordwidth / 4))
    fmt = ''.join(['%0', str(num_hex), 'x\n'])

    if datawidth >= wordwidth:
        num = int(math.ceil(datawidth / wordwidth))
        mask = (2 ** wordwidth) - 1

        with open(filename, 'w') as f:
            for data in array:
                values = []
                for i in range(num):
                    values.append(data & mask)
                    data >>= wordwidth

                if endian == 'big':
                    values.reverse()

                for v in values:
                    f.write(fmt % v)

    else:
        num = int(math.ceil(wordwidth / datawidth))
        mask = (2 ** datawidth) - 1

        with open(filename, 'w') as f:
            values = []
            for data in array:
                values.append(data & mask)

                if len(values) == num:
                    if endian == 'big':
                        values.reverse()

                    cat = 0
                    for i, v in enumerate(values):
                        cat = cat | (v << (i * datawidth))

                    f.write(fmt % cat)
                    values = []


def aligned_shape(shape, datawidth, mem_datawidth):
    aligned_shape = list(shape[:])

    if datawidth == mem_datawidth or datawidth > mem_datawidth:
        return aligned_shape

    chunk = mem_datawidth // datawidth
    new_size = int(math.ceil(aligned_shape[-1] / chunk)) * chunk
    aligned_shape[-1] = new_size

    return aligned_shape


def shape_to_length(shape):
    return functools.reduce(lambda x, y: x * y, shape, 1)


def shape_to_memory_size(shape, datawidth, mem_datawidth=None, block_size=4096):
    if mem_datawidth is not None:
        shape = aligned_shape(shape, datawidth, mem_datawidth)

    bytes = int(math.ceil(datawidth / 8))
    length = shape_to_length(shape)
    return ((block_size // bytes) *
            int(math.ceil(length / (block_size // bytes))))


def set_memory(mem, src, mem_datawidth, src_datawidth, mem_offset,
               num_align_words=None):
    if mem_datawidth < src_datawidth:
        return _set_memory_narrow(mem, src, mem_datawidth, src_datawidth, mem_offset,
                                  num_align_words)

    return _set_memory_wide(mem, src, mem_datawidth, src_datawidth, mem_offset,
                            num_align_words)


def _set_memory_wide(mem, src, mem_datawidth, src_datawidth, mem_offset,
                     num_align_words=None):

    if mem_datawidth > 64:
        raise ValueError('not supported')

    import numpy as np

    if num_align_words is not None:
        src = align(src, num_align_words)

    src_aligned_shape = aligned_shape(src.shape, src_datawidth, mem_datawidth)
    num_pack = int(math.ceil(mem_datawidth / src_datawidth))

    src_mask = np.uint64(2 ** src_datawidth - 1)
    mem_mask = np.uint64(2 ** mem_datawidth - 1)
    offset = mem_offset // int(math.ceil(mem_datawidth / 8))
    pack = 0
    index = 0
    align_count = 0

    for data in src.reshape([-1]):
        v = np.uint64(data) & src_mask
        shift = np.uint64(src_datawidth * pack)
        v = v << shift
        if pack > 0:
            old = np.uint64(mem[offset]) & mem_mask
            v = v | old
        mem[offset] = v

        index += 1
        if pack == num_pack - 1:
            pack = 0
            offset += 1
            if index == src.shape[-1]:
                index = 0
        else:
            pack += 1
            if index == src.shape[-1]:
                index = 0
                pack = 0
                offset += 1


def _set_memory_narrow(mem, src, mem_datawidth, src_datawidth, mem_offset,
                       num_align_words=None):

    if mem_datawidth > 64:
        raise ValueError('not supported')

    import numpy as np

    if num_align_words is not None:
        src = align(src, num_align_words)

    src_aligned_shape = aligned_shape(src.shape, src_datawidth, mem_datawidth)
    num_pack = int(math.ceil(src_datawidth / mem_datawidth))

    src_mask = np.uint64(2 ** src_datawidth - 1)
    mem_mask = np.uint64(2 ** mem_datawidth - 1)
    offset = mem_offset // int(math.ceil(mem_datawidth / 8))

    for data in src.reshape([-1]):
        for pack in range(num_pack):
            v = np.uint64(data)
            shift = np.uint64(mem_datawidth * pack)
            v = v >> shift
            v = v & mem_mask
            mem[offset] = v
            offset += 1


def align(src, num_align_words):
    if num_align_words == 1:
        return src

    import numpy as np

    src_aligned_shape = aligned_shape(src.shape, 1, num_align_words)
    ret = np.zeros(src_aligned_shape, dtype=np.int64).reshape([-1])
    offset = 0
    index = 0
    res = num_align_words - src.shape[-1] % num_align_words

    for data in src.reshape([-1]):
        ret[offset] = data
        offset += 1
        index += 1
        if index == src.shape[-1]:
            index = 0
            if res < num_align_words:
                offset += res

    return ret
