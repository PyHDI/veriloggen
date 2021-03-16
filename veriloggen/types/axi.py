from __future__ import absolute_import
from __future__ import print_function
from __future__ import division

import functools
import math
from collections import defaultdict

import veriloggen.core.vtypes as vtypes
from veriloggen.seq.seq import Seq
from veriloggen.fsm.fsm import FSM

import veriloggen.dataflow as _df
from veriloggen.dataflow.dataflow import DataflowManager
from veriloggen.dataflow.dtypes import make_condition, read_multi
from veriloggen.dataflow.dtypes import _Numeric as df_numeric
from . import util


BURST_FIXED = 0b00
BURST_INCR = 0b01
BURST_WRAP = 0b10

AxCACHE_NONCOHERENT = 0b0011
AxCACHE_COHERENT = 0b1111

AxPROT_NONCOHERENT = 0b000
AxPROT_COHERENT = 0b010

AxUSER_NONCOHERENT = 0b00
AxUSER_COHERENT = 0b01
xUSER_DEFAULT = 0b00


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
                 id_width=0, user_width=0,
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


class AxiStreamInterfaceBase(AxiInterfaceBase):
    _I = util.t_Input
    _O = util.t_OutputReg

    def __init__(self, m, name=None,
                 datawidth=32,
                 id_width=0, user_width=0, dest_width=0,
                 itype=None, otype=None):

        AxiInterfaceBase.__init__(self, m, name, datawidth, None,
                                  id_width, user_width,
                                  itype, otype)
        self.dest_width = dest_width


class AxiWriteAddress(AxiInterfaceBase):

    def __init__(self, m, name=None, datawidth=32, addrwidth=32,
                 id_width=0, user_width=2,
                 itype=None, otype=None):

        AxiInterfaceBase.__init__(self, m, name, datawidth, addrwidth,
                                  id_width, user_width, itype, otype)

        if isinstance(id_width, int) and id_width == 0:
            self.awid = None
        else:
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
            m, self.otype, name + '_awlock', 1, initval=0, no_reg=True)
        self.awcache = util.make_port(
            m, self.otype, name + '_awcache', 4, initval=0, no_reg=True)
        self.awprot = util.make_port(
            m, self.otype, name + '_awprot', 3, initval=0, no_reg=True)
        self.awqos = util.make_port(
            m, self.otype, name + '_awqos', 4, initval=0, no_reg=True)

        if isinstance(user_width, int) and user_width == 0:
            self.awuser = None
        else:
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
        self.awcache = util.make_port(
            m, self.otype, name + '_awcache', 4, initval=0, no_reg=True)
        self.awprot = util.make_port(
            m, self.otype, name + '_awprot', 3, initval=0, no_reg=True)
        self.awvalid = util.make_port(
            m, self.otype, name + '_awvalid', None, initval=0)
        self.awready = util.make_port(
            m, self.itype, name + '_awready', None, initval=0)


class AxiWriteData(AxiInterfaceBase):

    def __init__(self, m, name=None, datawidth=32, addrwidth=32,
                 id_width=0, user_width=0,
                 itype=None, otype=None):

        AxiInterfaceBase.__init__(self, m, name, datawidth, addrwidth,
                                  id_width, user_width, itype, otype)

        self.wdata = util.make_port(
            m, self.otype, name + '_wdata', self.datawidth, initval=0)
        self.wstrb = util.make_port(
            m, self.otype, name + '_wstrb', self.datawidth // 8, initval=0)
        self.wlast = util.make_port(
            m, self.otype, name + '_wlast', None, initval=0)

        if isinstance(user_width, int) and user_width == 0:
            self.wuser = None
        else:
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
                 id_width=0, user_width=0,
                 itype=None, otype=None):

        AxiInterfaceBase.__init__(self, m, name, datawidth, addrwidth,
                                  id_width, user_width, itype, otype)

        if isinstance(id_width, int) and id_width == 0:
            self.bid = None
        else:
            self.bid = util.make_port(
                m, self.itype, name + '_bid', self.id_width, initval=0)

        self.bresp = util.make_port(
            m, self.itype, name + '_bresp', 2, initval=0, no_reg=True)

        if isinstance(user_width, int) and user_width == 0:
            self.buser = None
        else:
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
                 id_width=0, user_width=2,
                 itype=None, otype=None):

        AxiInterfaceBase.__init__(self, m, name, datawidth, addrwidth,
                                  id_width, user_width, itype, otype)

        if isinstance(id_width, int) and id_width == 0:
            self.arid = None
        else:
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
            m, self.otype, name + '_arlock', 1, initval=0, no_reg=True)
        self.arcache = util.make_port(
            m, self.otype, name + '_arcache', 4, initval=0, no_reg=True)
        self.arprot = util.make_port(
            m, self.otype, name + '_arprot', 3, initval=0, no_reg=True)
        self.arqos = util.make_port(
            m, self.otype, name + '_arqos', 4, initval=0, no_reg=True)

        if isinstance(user_width, int) and user_width == 0:
            self.aruser = None
        else:
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
        self.arcache = util.make_port(
            m, self.otype, name + '_arcache', 4, initval=0, no_reg=True)
        self.arprot = util.make_port(
            m, self.otype, name + '_arprot', 3, initval=0, no_reg=True)
        self.arvalid = util.make_port(
            m, self.otype, name + '_arvalid', None, initval=0)
        self.arready = util.make_port(
            m, self.itype, name + '_arready', None, initval=0)


class AxiReadData(AxiInterfaceBase):
    _O = util.t_Output

    def __init__(self, m, name=None, datawidth=32, addrwidth=32,
                 id_width=0, user_width=0,
                 itype=None, otype=None):

        AxiInterfaceBase.__init__(self, m, name, datawidth, addrwidth,
                                  id_width, user_width, itype, otype)

        if isinstance(id_width, int) and id_width == 0:
            self.rid = None
        else:
            self.rid = util.make_port(
                m, self.itype, name + '_rid', self.id_width, initval=0)

        self.rdata = util.make_port(
            m, self.itype, name + '_rdata', self.datawidth, initval=0)
        self.rresp = util.make_port(
            m, self.itype, name + '_rresp', 2, initval=0, no_reg=True)
        self.rlast = util.make_port(
            m, self.itype, name + '_rlast', None, initval=0)

        if isinstance(user_width, int) and user_width == 0:
            self.ruser = None
        else:
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


class AxiStreamInData(AxiStreamInterfaceBase):
    _O = util.t_Output

    def __init__(self, m, name=None, datawidth=32,
                 with_last=True, with_strb=False,
                 id_width=0, user_width=0, dest_width=0,
                 itype=None, otype=None):

        AxiStreamInterfaceBase.__init__(self, m, name, datawidth,
                                        id_width, user_width, dest_width,
                                        itype, otype)

        self.tdata = util.make_port(
            m, self.itype, name + '_tdata', self.datawidth, initval=0)
        self.tvalid = util.make_port(
            m, self.itype, name + '_tvalid', None, initval=0)
        self.tready = util.make_port(
            m, self.otype, name + '_tready', None, initval=0)

        if not with_last:
            self.tlast = None
        else:
            self.tlast = util.make_port(
                m, self.itype, name + '_tlast', initval=0)

        if not with_strb:
            self.tstrb = None
        else:
            self.tstrb = util.make_port(
                m, self.itype, name + '_tstrb', self.datawidth // 8, initval=0)

        if isinstance(user_width, int) and user_width == 0:
            self.tuser = None
        else:
            self.tuser = util.make_port(
                m, self.itype, name + '_tuser', self.user_width, initval=0)

        if isinstance(id_width, int) and id_width == 0:
            self.tid = None
        else:
            self.tid = util.make_port(
                m, self.itype, name + '_tid', self.id_width, initval=0)

        if isinstance(dest_width, int) and dest_width == 0:
            self.tdest = None
        else:
            self.tdest = util.make_port(
                m, self.itype, name + '_tdest', self.dest_width, initval=0)


class AxiStreamOutData(AxiStreamInData):
    _I = util.t_OutputReg
    _O = util.t_Input


# AXI-Full
class AxiMaster(object):
    burst_size_width = 8
    boundary_size = 4096

    def __init__(self, m, name, clk, rst, datawidth=32, addrwidth=32,
                 waddr_id_width=0, wdata_id_width=0, wresp_id_width=0,
                 raddr_id_width=0, rdata_id_width=0,
                 waddr_user_width=2, wdata_user_width=0, wresp_user_width=0,
                 raddr_user_width=2, rdata_user_width=0,
                 waddr_burst_mode=BURST_INCR, raddr_burst_mode=BURST_INCR,
                 waddr_cache_mode=AxCACHE_NONCOHERENT, raddr_cache_mode=AxCACHE_NONCOHERENT,
                 waddr_prot_mode=AxPROT_NONCOHERENT, raddr_prot_mode=AxPROT_NONCOHERENT,
                 waddr_user_mode=AxUSER_NONCOHERENT, wdata_user_mode=xUSER_DEFAULT,
                 raddr_user_mode=AxUSER_NONCOHERENT,
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

        self.waddr = AxiMasterWriteAddress(m, name, datawidth, addrwidth,
                                           waddr_id_width, waddr_user_width, itype, otype)
        self.wdata = AxiMasterWriteData(m, name, datawidth, addrwidth,
                                        wdata_id_width, wdata_user_width, itype, otype)
        self.wresp = AxiMasterWriteResponse(m, name, datawidth, addrwidth,
                                            wresp_id_width, wresp_user_width, itype, otype)
        self.raddr = AxiMasterReadAddress(m, name, datawidth, addrwidth,
                                          raddr_id_width, raddr_user_width, itype, otype)

        otype = util.t_Wire if noio else None

        self.rdata = AxiMasterReadData(m, name, datawidth, addrwidth,
                                       rdata_id_width, rdata_user_width, itype, otype)

        self.seq = Seq(m, name, clk, rst)

        # default values
        self.waddr.awsize.assign(int(math.log(self.datawidth / 8, 2)))
        self.waddr.awburst.assign(waddr_burst_mode)
        self.waddr.awlock.assign(0)
        self.waddr.awcache.assign(waddr_cache_mode)
        self.waddr.awprot.assign(waddr_prot_mode)
        self.waddr.awqos.assign(0)
        if self.waddr.awuser is not None:
            self.waddr.awuser.assign(waddr_user_mode)
        if self.wdata.wuser is not None:
            self.wdata.wuser.assign(wdata_user_mode)
        self.wresp.bready.assign(1)
        self.raddr.arsize.assign(int(math.log(self.datawidth / 8, 2)))
        self.raddr.arburst.assign(raddr_burst_mode)
        self.raddr.arlock.assign(0)
        self.raddr.arcache.assign(raddr_cache_mode)
        self.raddr.arprot.assign(raddr_prot_mode)
        self.raddr.arqos.assign(0)
        if self.raddr.aruser is not None:
            self.raddr.aruser.assign(raddr_user_mode)

        self.write_counters = []
        self.read_counters = []

        if nodataflow:
            self.df = None
        else:
            self.df = DataflowManager(self.m, self.clk, self.rst)

        self._write_disabled = False
        self._read_disabled = False

    def disable_write(self):
        ports = [self.waddr.awaddr(0),
                 self.waddr.awlen(0),
                 self.waddr.awvalid(0),
                 self.wdata.wdata(0),
                 self.wdata.wstrb(0),
                 self.wdata.wlast(0),
                 self.wdata.wvalid(0)]

        if self.waddr.awid is not None:
            ports.insert(0, self.waddr.awid(0))

        self.seq(
            *ports
        )

        self._write_disabled = True

    def disable_read(self):
        ports = [self.raddr.araddr(0),
                 self.raddr.arlen(0),
                 self.raddr.arvalid(0)]

        if self.raddr.arid is not None:
            ports.insert(0, self.raddr.arid(0))

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

    def write_request(self, addr, length=1, cond=None):
        """
        @return ack
        """
        if self._write_disabled:
            raise TypeError('Write disabled.')

        if isinstance(length, int) and length > 2 ** self.burst_size_width:
            raise ValueError("length must be less than 257.")

        if isinstance(length, int) and length < 1:
            raise ValueError("length must be more than 0.")

        if cond is not None:
            self.seq.If(cond)

        ack = vtypes.Ors(self.waddr.awready, vtypes.Not(self.waddr.awvalid))

        self.seq.If(ack)(
            self.waddr.awid(0) if self.waddr.awid is not None else (),
            self.waddr.awaddr(addr),
            self.waddr.awlen(length - 1),
            self.waddr.awvalid(1)
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

        return ack

    def write_request_counter(self, addr, length=1, cond=None, counter=None):
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
            self.waddr.awid(0) if self.waddr.awid is not None else (),
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

    def read_request(self, addr, length=1, cond=None):
        """
        @return ack
        """
        if self._read_disabled:
            raise TypeError('Read disabled.')

        if isinstance(length, int) and length > 2 ** self.burst_size_width:
            raise ValueError("length must be less than 257.")

        if isinstance(length, int) and length < 1:
            raise ValueError("length must be more than 0.")

        if cond is not None:
            self.seq.If(cond)

        ack = vtypes.Ors(self.raddr.arready, vtypes.Not(self.raddr.arvalid))

        self.seq.If(ack)(
            self.raddr.arid(0) if self.raddr.arid is not None else (),
            self.raddr.araddr(addr),
            self.raddr.arlen(length - 1),
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

    def read_request_counter(self, addr, length=1, cond=None, counter=None):
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
            self.raddr.arid(0) if self.raddr.arid is not None else (),
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
                              width=self.datawidth, point=point, signed=signed)
        df_last = df.Variable(last, valid, last_ready, width=1, signed=False)
        done = vtypes.Ands(last, self.rdata.rvalid, self.rdata.rready)

        return df_data, df_last, done

    def connect(self, ports, name):
        if not self.noio:
            raise ValueError('I/O ports can not be connected to others.')

        if '_'.join([name, 'awid']) in ports:
            awid = ports['_'.join([name, 'awid'])]
        else:
            awid = None
        awaddr = ports['_'.join([name, 'awaddr'])]
        awlen = ports['_'.join([name, 'awlen'])]
        awsize = ports['_'.join([name, 'awsize'])]
        awburst = ports['_'.join([name, 'awburst'])]
        awlock = ports['_'.join([name, 'awlock'])]
        awcache = ports['_'.join([name, 'awcache'])]
        awprot = ports['_'.join([name, 'awprot'])]
        awqos = ports['_'.join([name, 'awqos'])]
        if '_'.join([name, 'awuser']) in ports:
            awuser = ports['_'.join([name, 'awuser'])]
        else:
            awuser = None
        awvalid = ports['_'.join([name, 'awvalid'])]
        awready = ports['_'.join([name, 'awready'])]

        if awid is not None:
            awid.connect(self.waddr.awid if self.waddr.awid is not None else 0)
        awaddr.connect(self.waddr.awaddr)
        awlen.connect(self.waddr.awlen)
        awsize.connect(self.waddr.awsize)
        awburst.connect(self.waddr.awburst)
        awlock.connect(self.waddr.awlock)
        awcache.connect(self.waddr.awcache)
        awprot.connect(self.waddr.awprot)
        awqos.connect(self.waddr.awqos)
        if awuser is not None:
            awuser.connect(self.waddr.awuser if self.waddr.awuser is not None else 0)
        awvalid.connect(self.waddr.awvalid)
        self.waddr.awready.connect(awready)

        wdata = ports['_'.join([name, 'wdata'])]
        wstrb = ports['_'.join([name, 'wstrb'])]
        wlast = ports['_'.join([name, 'wlast'])]
        if '_'.join([name, 'wuser']) in ports:
            wuser = ports['_'.join([name, 'wuser'])]
        else:
            wuser = None
        wvalid = ports['_'.join([name, 'wvalid'])]
        wready = ports['_'.join([name, 'wready'])]

        wdata.connect(self.wdata.wdata)
        wstrb.connect(self.wdata.wstrb)
        wlast.connect(self.wdata.wlast)
        if wuser is not None:
            wuser.connect(self.wdata.wuser if self.wdata.wuser is not None else 0)
        wvalid.connect(self.wdata.wvalid)
        self.wdata.wready.connect(wready)

        if '_'.join([name, 'bid']) in ports:
            bid = ports['_'.join([name, 'bid'])]
        else:
            bid = None
        bresp = ports['_'.join([name, 'bresp'])]
        if '_'.join([name, 'buser']) in ports:
            buser = ports['_'.join([name, 'buser'])]
        else:
            buser = None
        bvalid = ports['_'.join([name, 'bvalid'])]
        bready = ports['_'.join([name, 'bready'])]

        if self.wresp.bid is not None:
            self.wresp.bid.connect(bid if bid is not None else 0)
        self.wresp.bresp.connect(bresp)
        if self.wresp.buser is not None:
            self.wresp.buser.connect(buser if buser is not None else 0)
        self.wresp.bvalid.connect(bvalid)
        bready.connect(self.wresp.bready)

        if '_'.join([name, 'arid']) in ports:
            arid = ports['_'.join([name, 'arid'])]
        else:
            arid = None
        araddr = ports['_'.join([name, 'araddr'])]
        arlen = ports['_'.join([name, 'arlen'])]
        arsize = ports['_'.join([name, 'arsize'])]
        arburst = ports['_'.join([name, 'arburst'])]
        arlock = ports['_'.join([name, 'arlock'])]
        arcache = ports['_'.join([name, 'arcache'])]
        arprot = ports['_'.join([name, 'arprot'])]
        arqos = ports['_'.join([name, 'arqos'])]
        if '_'.join([name, 'aruser']) in ports:
            aruser = ports['_'.join([name, 'aruser'])]
        else:
            aruser = None
        arvalid = ports['_'.join([name, 'arvalid'])]
        arready = ports['_'.join([name, 'arready'])]

        if arid is not None:
            arid.connect(self.raddr.arid if self.raddr.arid is not None else 0)
        araddr.connect(self.raddr.araddr)
        arlen.connect(self.raddr.arlen)
        arsize.connect(self.raddr.arsize)
        arburst.connect(self.raddr.arburst)
        arlock.connect(self.raddr.arlock)
        arcache.connect(self.raddr.arcache)
        arprot.connect(self.raddr.arprot)
        arqos.connect(self.raddr.arqos)
        if aruser is not None:
            aruser.connect(self.raddr.aruser if self.raddr.aruser is not None else 0)
        arvalid.connect(self.raddr.arvalid)
        self.raddr.arready.connect(arready)

        if '_'.join([name, 'rid']) in ports:
            rid = ports['_'.join([name, 'rid'])]
        else:
            rid = None
        rdata = ports['_'.join([name, 'rdata'])]
        rresp = ports['_'.join([name, 'rresp'])]
        rlast = ports['_'.join([name, 'rlast'])]
        if '_'.join([name, 'ruser']) in ports:
            ruser = ports['_'.join([name, 'ruser'])]
        else:
            ruser = None
        rvalid = ports['_'.join([name, 'rvalid'])]
        rready = ports['_'.join([name, 'rready'])]

        if self.rdata.rid is not None:
            self.rdata.rid.connect(rid if rid is not None else 0)
        self.rdata.rdata.connect(rdata)
        self.rdata.rresp.connect(rresp)
        self.rdata.rlast.connect(rlast)
        if self.rdata.ruser is not None:
            self.rdata.ruser.connect(ruser if ruser is not None else 0)
        self.rdata.rvalid.connect(rvalid)
        rready.connect(self.rdata.rready)


# AXI-Lite
class AxiLiteMaster(AxiMaster):

    def __init__(self, m, name, clk, rst, datawidth=32, addrwidth=32,
                 waddr_cache_mode=AxCACHE_NONCOHERENT, raddr_cache_mode=AxCACHE_NONCOHERENT,
                 waddr_prot_mode=AxPROT_NONCOHERENT, raddr_prot_mode=AxPROT_NONCOHERENT,
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
        self.waddr.awcache.assign(waddr_cache_mode)
        self.waddr.awprot.assign(waddr_prot_mode)
        self.wresp.bready.assign(1)
        self.raddr.arcache.assign(raddr_cache_mode)
        self.raddr.arprot.assign(raddr_prot_mode)

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
        awcache = ports['_'.join([name, 'awcache'])]
        awprot = ports['_'.join([name, 'awprot'])]
        awvalid = ports['_'.join([name, 'awvalid'])]
        awready = ports['_'.join([name, 'awready'])]

        awaddr.connect(self.waddr.awaddr)
        awcache.connect(self.waddr.awcache)
        awprot.connect(self.waddr.awprot)
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
        arcache = ports['_'.join([name, 'arcache'])]
        arprot = ports['_'.join([name, 'arprot'])]
        arvalid = ports['_'.join([name, 'arvalid'])]
        arready = ports['_'.join([name, 'arready'])]

        araddr.connect(self.raddr.araddr)
        arcache.connect(self.raddr.arcache)
        arprot.connect(self.raddr.arprot)
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
                 waddr_id_width=0, wdata_id_width=0, wresp_id_width=0,
                 raddr_id_width=0, rdata_id_width=0,
                 waddr_user_width=2, wdata_user_width=0, wresp_user_width=0,
                 raddr_user_width=2, rdata_user_width=0,
                 wresp_user_mode=xUSER_DEFAULT,
                 rdata_user_mode=xUSER_DEFAULT,
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

        self.waddr = AxiSlaveWriteAddress(m, name, datawidth, addrwidth,
                                          waddr_id_width, waddr_user_width, itype, otype)
        self.wdata = AxiSlaveWriteData(m, name, datawidth, addrwidth,
                                       wdata_id_width, wdata_user_width, itype, otype)
        self.wresp = AxiSlaveWriteResponse(m, name, datawidth, addrwidth,
                                           wresp_id_width, wresp_user_width, itype, otype)
        self.raddr = AxiSlaveReadAddress(m, name, datawidth, addrwidth,
                                         raddr_id_width, raddr_user_width, itype, otype)

        itype = util.t_Reg if noio else None

        self.rdata = AxiSlaveReadData(m, name, datawidth, addrwidth,
                                      rdata_id_width, rdata_user_width, itype, otype)

        self.seq = Seq(m, name, clk, rst)

        # default values
        self.wresp.bresp.assign(0)
        if self.wresp.buser is not None:
            self.wresp.buser.assign(wresp_user_mode)
        self.rdata.rresp.assign(0)
        if self.rdata.ruser is not None:
            self.rdata.ruser.assign(rdata_user_mode)

        # write response
        if self.wresp.bid is not None:
            self.seq.If(self.waddr.awvalid, self.waddr.awready, vtypes.Not(self.wresp.bvalid))(
                self.wresp.bid(self.waddr.awid if self.waddr.awid is not None else 0)
            )

        if self.rdata.rid is not None:
            self.seq.If(self.raddr.arvalid, self.raddr.arready)(
                self.rdata.rid(self.raddr.arid if self.raddr.arid is not None else 0)
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

    def pull_request_counter(self, cond, counter=None):
        """
        @return addr, counter, readvalid, writevalid
        """
        if counter is not None and not isinstance(counter, vtypes.Reg):
            raise TypeError("counter must be Reg or None.")

        if counter is None:
            counter = self.m.TmpReg(self.burst_size_width + 1, initval=0)

        ready = make_condition(cond)

        write_ack = vtypes.Ands(self.waddr.awready, self.waddr.awvalid,
                                vtypes.Not(self.wresp.bvalid))
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

        writeval = vtypes.Ands(vtypes.Not(writevalid), vtypes.Not(readvalid),
                               vtypes.Not(self.wresp.bvalid),
                               prev_awvalid)
        if ready is not None:
            writeval = vtypes.Ands(ready, writeval)

        readval = vtypes.Ands(vtypes.Not(readvalid), vtypes.Not(writevalid),
                              prev_arvalid, vtypes.Not(prev_awvalid))

        if ready is not None:
            readval = vtypes.Ands(ready, readval)

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

    def pull_write_request_counter(self, cond=None, counter=None):
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

        ack = vtypes.Ands(self.waddr.awready, self.waddr.awvalid,
                          vtypes.Not(self.wresp.bvalid))
        addr = self.m.TmpReg(self.addrwidth, initval=0)
        valid = self.m.TmpReg(initval=0)

        prev_awvalid = self.m.TmpReg(initval=0)
        self.seq(
            prev_awvalid(self.waddr.awvalid)
        )

        val = (vtypes.Ands(vtypes.Not(valid),
                           vtypes.Not(self.wresp.bvalid),
                           prev_awvalid) if ready is None else
               vtypes.Ands(ready, vtypes.Not(valid),
                           vtypes.Not(self.wresp.bvalid),
                           prev_awvalid))

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

        df_data = self.df.Variable(data, valid, data_ready,
                                   width=self.datawidth, signed=False)
        df_mask = self.df.Variable(mask, valid, mask_ready,
                                   width=self.datawidth // 4, signed=False)
        df_last = self.df.Variable(last, valid, last_ready,
                                   width=1, signed=False)
        done = vtypes.Ands(last, self.wdata.wvalid, self.wdata.wready)

        return df_data, df_mask, df_last, done

    def pull_read_request_counter(self, cond=None, counter=None):
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
        @return ack, valid, last
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
        valid = vtypes.Ands(self.rdata.rready, self.rdata.rvalid)
        last = self.rdata.rlast

        self.seq.If(vtypes.Ands(ack, counter > 0))(
            self.rdata.rdata(data),
            self.rdata.rvalid(1),
            self.rdata.rlast(0),
            counter.dec()
        )
        self.seq.Then().If(counter == 1)(
            self.rdata.rlast(1)
        )

        # de-assert
        self.seq.Delay(1)(
            self.rdata.rvalid(0),
            self.rdata.rlast(0)
        )

        # retry
        self.seq.If(vtypes.Ands(self.rdata.rvalid, vtypes.Not(self.rdata.rready)))(
            self.rdata.rvalid(self.rdata.rvalid),
            self.rdata.rlast(self.rdata.rlast)
        )

        return ack, valid, last

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
            self.rdata.rlast(1)
        )

        # de-assert
        self.seq.Delay(1)(
            self.rdata.rvalid(0),
            self.rdata.rlast(0)
        )

        # retry
        self.seq.If(vtypes.Ands(self.rdata.rvalid, vtypes.Not(self.rdata.rready)))(
            self.rdata.rvalid(self.rdata.rvalid),
            self.rdata.rlast(self.rdata.rlast)
        )

        done = vtypes.Ands(self.rdata.rlast, self.rdata.rvalid, self.rdata.rready)

        return done

    def connect(self, ports, name):
        if not self.noio:
            raise ValueError('I/O ports can not be connected to others.')

        ports = defaultdict(lambda: None, ports)

        if '_'.join([name, 'awid']) in ports:
            awid = ports['_'.join([name, 'awid'])]
        else:
            awid = None
        awaddr = ports['_'.join([name, 'awaddr'])]
        awlen = ports['_'.join([name, 'awlen'])]
        awsize = ports['_'.join([name, 'awsize'])]
        awburst = ports['_'.join([name, 'awburst'])]
        awlock = ports['_'.join([name, 'awlock'])]
        awcache = ports['_'.join([name, 'awcache'])]
        awprot = ports['_'.join([name, 'awprot'])]
        awqos = ports['_'.join([name, 'awqos'])]
        if '_'.join([name, 'awuser']) in ports:
            awuser = ports['_'.join([name, 'awuser'])]
        else:
            awuser = None
        awvalid = ports['_'.join([name, 'awvalid'])]
        awready = ports['_'.join([name, 'awready'])]

        if self.waddr.awid is not None:
            self.waddr.awid.connect(awid if awid is not None else 0)
        self.waddr.awaddr.connect(awaddr)
        self.waddr.awlen.connect(awlen if awlen is not None else 0)
        self.waddr.awsize.connect(awsize if awsize is not None else
                                  int(math.log(self.datawidth // 8)))
        self.waddr.awburst.connect(awburst if awburst is not None else BURST_INCR)
        self.waddr.awlock.connect(awlock if awlock is not None else 0)
        self.waddr.awcache.connect(awcache)
        self.waddr.awprot.connect(awprot)
        self.waddr.awqos.connect(awqos if awqos is not None else 0)
        if self.waddr.awuser is not None:
            self.waddr.awuser.connect(awuser if awuser is not None else 0)
        self.waddr.awvalid.connect(awvalid)
        awready.connect(self.waddr.awready)

        wdata = ports['_'.join([name, 'wdata'])]
        wstrb = ports['_'.join([name, 'wstrb'])]
        wlast = ports['_'.join([name, 'wlast'])]
        if '_'.join([name, 'wuser']) in ports:
            wuser = ports['_'.join([name, 'wuser'])]
        else:
            wuser = None
        wvalid = ports['_'.join([name, 'wvalid'])]
        wready = ports['_'.join([name, 'wready'])]

        self.wdata.wdata.connect(wdata)
        self.wdata.wstrb.connect(wstrb)
        self.wdata.wlast.connect(wlast if wlast is not None else 1)
        if self.wdata.wuser is not None:
            self.wdata.wuser.connect(wuser if wuser is not None else 0)
        self.wdata.wvalid.connect(wvalid)
        wready.connect(self.wdata.wready)

        if '_'.join([name, 'bid']) in ports:
            bid = ports['_'.join([name, 'bid'])]
        else:
            bid = None
        bresp = ports['_'.join([name, 'bresp'])]
        if '_'.join([name, 'buser']) in ports:
            buser = ports['_'.join([name, 'buser'])]
        else:
            buser = None
        bvalid = ports['_'.join([name, 'bvalid'])]
        bready = ports['_'.join([name, 'bready'])]

        if bid is not None:
            bid.connect(self.wresp.bid if self.wresp.bid is not None else 0)
        bresp.connect(self.wresp.bresp)
        if buser is not None:
            buser.connect(self.wresp.buser if self.wresp.buser is not None else 0)
        bvalid.connect(self.wresp.bvalid)
        self.wresp.bready.connect(bready)

        if '_'.join([name, 'arid']) in ports:
            arid = ports['_'.join([name, 'arid'])]
        else:
            arid = None
        araddr = ports['_'.join([name, 'araddr'])]
        arlen = ports['_'.join([name, 'arlen'])]
        arsize = ports['_'.join([name, 'arsize'])]
        arburst = ports['_'.join([name, 'arburst'])]
        arlock = ports['_'.join([name, 'arlock'])]
        arcache = ports['_'.join([name, 'arcache'])]
        arprot = ports['_'.join([name, 'arprot'])]
        arqos = ports['_'.join([name, 'arqos'])]
        if '_'.join([name, 'aruser']) in ports:
            aruser = ports['_'.join([name, 'aruser'])]
        else:
            aruser = None
        arvalid = ports['_'.join([name, 'arvalid'])]
        arready = ports['_'.join([name, 'arready'])]

        if self.raddr.arid is not None:
            self.raddr.arid.connect(arid if arid is not None else 0)
        self.raddr.araddr.connect(araddr)
        self.raddr.arlen.connect(arlen if arlen is not None else 0)
        self.raddr.arsize.connect(arsize if arsize is not None else
                                  int(math.log(self.datawidth // 8)))
        self.raddr.arburst.connect(arburst if arburst is not None else BURST_INCR)
        self.raddr.arlock.connect(arlock if arlock is not None else 0)
        self.raddr.arcache.connect(arcache)
        self.raddr.arprot.connect(arprot)
        self.raddr.arqos.connect(arqos if arqos is not None else 0)
        if self.raddr.aruser is not None:
            self.raddr.aruser.connect(aruser if aruser is not None else 0)
        self.raddr.arvalid.connect(arvalid)
        arready.connect(self.raddr.arready)

        if '_'.join([name, 'rid']) in ports:
            rid = ports['_'.join([name, 'rid'])]
        else:
            rid = None
        rdata = ports['_'.join([name, 'rdata'])]
        rresp = ports['_'.join([name, 'rresp'])]
        rlast = ports['_'.join([name, 'rlast'])]
        if '_'.join([name, 'ruser']) in ports:
            ruser = ports['_'.join([name, 'ruser'])]
        else:
            ruser = None
        rvalid = ports['_'.join([name, 'rvalid'])]
        rready = ports['_'.join([name, 'rready'])]

        if rid is not None:
            rid.connect(self.rdata.rid if self.rdata.rid is not None else 0)
        rdata.connect(self.rdata.rdata)
        rresp.connect(self.rdata.rresp)
        if rlast is not None:
            rlast.connect(self.rdata.rlast)
        if ruser is not None:
            ruser.connect(self.rdata.ruser if self.rdata.ruser is not None else 0)
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

        write_ack = vtypes.Ands(self.waddr.awready, self.waddr.awvalid,
                                vtypes.Not(self.wresp.bvalid))
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

        writeval = vtypes.Ands(vtypes.Not(writevalid), vtypes.Not(readvalid),
                               vtypes.Not(self.wresp.bvalid),
                               prev_awvalid)
        if ready is not None:
            writeval = vtypes.Ands(ready, writeval)

        readval = vtypes.Ands(vtypes.Not(readvalid), vtypes.Not(writevalid),
                              prev_arvalid, vtypes.Not(prev_awvalid))

        if ready is not None:
            readval = vtypes.Ands(ready, readval)

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

        ack = vtypes.Ands(self.waddr.awready, self.waddr.awvalid,
                          vtypes.Not(self.wresp.bvalid))
        addr = self.m.TmpReg(self.addrwidth, initval=0)
        valid = self.m.TmpReg(initval=0)

        prev_awvalid = self.m.TmpReg(initval=0)
        self.seq(
            prev_awvalid(self.waddr.awvalid)
        )

        val = (vtypes.Ands(vtypes.Not(valid),
                           vtypes.Not(self.wresp.bvalid),
                           prev_awvalid) if ready is None else
               vtypes.Ands(ready, vtypes.Not(valid),
                           vtypes.Not(self.wresp.bvalid),
                           prev_awvalid))

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
        @return ack, valid
        """
        if self._read_disabled:
            raise TypeError('Read disabled.')

        if cond is not None:
            self.seq.If(cond)

        ack = vtypes.Ors(self.rdata.rready, vtypes.Not(self.rdata.rvalid))
        valid = vtypes.Ands(self.rdata.rready, self.rdata.rvalid)

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

        return ack, valid

    def push_read_dataflow(self, data, counter=None, cond=None):
        """ 
        @return done
        """
        raise TypeError('lite interface support no dataflow operation.')

    def connect(self, ports, name):
        if not self.noio:
            raise ValueError('I/O ports can not be connected to others.')

        awaddr = ports['_'.join([name, 'awaddr'])]
        awcache = ports['_'.join([name, 'awcache'])]
        awprot = ports['_'.join([name, 'awprot'])]
        awvalid = ports['_'.join([name, 'awvalid'])]
        awready = ports['_'.join([name, 'awready'])]

        self.waddr.awaddr.connect(awaddr)
        self.waddr.awcache.connect(awcache)
        self.waddr.awprot.connect(awprot)
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
        arcache = ports['_'.join([name, 'arcache'])]
        arprot = ports['_'.join([name, 'arprot'])]
        arvalid = ports['_'.join([name, 'arvalid'])]
        arready = ports['_'.join([name, 'arready'])]

        self.raddr.araddr.connect(araddr)
        self.raddr.arcache.connect(arcache)
        self.raddr.arprot.connect(arprot)
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


class AxiStreamIn(object):

    def __init__(self, m, name, clk, rst, datawidth=32,
                 with_last=True, with_strb=False,
                 id_width=0, user_width=0, dest_width=0,
                 noio=False, nodataflow=False):

        self.m = m
        self.name = name

        self.clk = clk
        self.rst = rst

        self.datawidth = datawidth

        self.noio = noio

        if not hasattr(self.m, 'streaminbus'):
            self.m.streaminbus = []

        self.m.streaminbus.append(self)

        itype = util.t_Wire if noio else None
        otype = util.t_Wire if noio else None

        self.tdata = AxiStreamInData(m, name, datawidth,
                                     with_last, with_strb,
                                     id_width, user_width, dest_width,
                                     itype, otype)

        self.seq = Seq(m, name, clk, rst)

        if nodataflow:
            self.df = None
        else:
            self.df = DataflowManager(self.m, self.clk, self.rst)

    def read_data(self, cond=None):
        """
        @return data, last, _id, user, dest, valid
        """
        ready = make_condition(cond)
        val = 1 if ready is None else ready

        _connect_ready(self.tdata.tready._get_module(), self.tdata.tready, val)

        ack = vtypes.Ands(self.tdata.tready, self.tdata.tvalid)
        data = self.tdata.tdata
        valid = ack
        last = self.tdata.tlast
        _id = self.tdata.tid
        user = self.tdata.tuser
        dest = self.tdata.tdest

        return data, last, _id, user, dest, valid

    def read_dataflow(self, cond=None, point=0, signed=True):
        """
        @return data, last, _id, user, dest, done
        """
        data_ready = self.m.TmpWire()
        last_ready = self.m.TmpWire()
        id_ready = self.m.TmpWire()
        user_ready = self.m.TmpWire()
        dest_ready = self.m.TmpWire()
        data_ready.assign(1)
        id_ready.assign(1)
        last_ready.assign(1)
        user_ready.assign(1)
        dest_ready.assign(1)

        if cond is None:
            cond = (data_ready, last_ready, id_ready, user_ready, dest_ready)
        elif isinstance(cond, (tuple, list)):
            cond = tuple(list(cond) + [data_ready, last_ready, id_ready, user_ready, dest_ready])
        else:
            cond = (cond, data_ready, last_ready, id_ready, user_ready, dest_ready)

        ready = make_condition(*cond)
        val = 1 if ready is None else ready

        _connect_ready(self.tdata.tready._get_module(), self.tdata.tready, val)

        ack = vtypes.Ands(self.tdata.tready, self.tdata.tvalid)
        data = self.tdata.tdata
        valid = self.tdata.tvalid
        _id = self.tdata.tid
        last = self.tdata.tlast
        user = self.tdata.tuser
        dest = self.tdata.tdest

        df = self.df if self.df is not None else _df

        df_data = df.Variable(data, valid, data_ready,
                              width=self.datawidth, point=point, signed=signed)
        if last is not None:
            df_last = df.Variable(last, valid, last_ready, width=1, signed=False)
            done = vtypes.Ands(last, self.tdata.tvalid, self.tdata.tready)
        else:
            df_last = None
            done = vtypes.Ands(self.tdata.tvalid, self.tdata.tready)

        if _id is not None:
            df_id = df.Variable(_id, valid, id_ready, width=_id.width, signed=False)
        else:
            df_id = None

        if user is not None:
            df_user = df.Variable(user, valid, user_ready, width=user.width, signed=False)
        else:
            df_user = None

        if dest is not None:
            df_dest = df.Variable(dest, valid, dest_ready, width=dest.width, signed=False)
        else:
            df_dest = None

        return df_data, df_last, df_id, df_user, df_dest, done

    def connect(self, ports, name):
        if not self.noio:
            raise ValueError('I/O ports can not be connected to others.')

        tdata = ports['_'.join([name, 'tdata'])]
        tvalid = ports['_'.join([name, 'tvalid'])]
        tready = ports['_'.join([name, 'tready'])]

        if '_'.join([name, 'tlast']) in ports:
            tlast = ports['_'.join([name, 'tlast'])]
        else:
            tlast = None

        if '_'.join([name, 'tid']) in ports:
            tid = ports['_'.join([name, 'tid'])]
        else:
            tid = None

        if '_'.join([name, 'tuser']) in ports:
            tuser = ports['_'.join([name, 'tuser'])]
        else:
            tuser = None

        if '_'.join([name, 'tdest']) in ports:
            tdest = ports['_'.join([name, 'tdest'])]
        else:
            tdest = None

        self.tdata.tdata.connect(tdata)
        self.tdata.tvalid.connect(tvalid)
        tready.connect(self.tdata.tready)

        if self.tdata.tlast is not None:
            self.tdata.tlast.connect(tlast if tlast is not None else 1)
        if self.tdata.tid is not None:
            self.tdata.tid.connect(tid if tid is not None else 0)
        if self.tdata.tuser is not None:
            self.tdata.tuser.connect(tuser if tuser is not None else 0)
        if self.tdata.tdest is not None:
            self.tdata.tdest.connect(tdest if tdest is not None else 0)

    def connect_stream(self, stream):
        if not isinstance(stream, AxiStreamOut):
            raise TypeError('stream must be an instance of AxiStreamOut.')

        if not self.noio:
            raise ValueError('I/O ports can not be connected to others.')

        tdata = stream.tdata.tdata
        tvalid = stream.tdata.tvalid
        tready = stream.tdata.tready

        if stream.tdata.tlast is not None:
            tlast = stream.tdata.tlast
        else:
            tlast = None

        if stream.tdata.tid is not None:
            tid = stream.tdata.tid
        else:
            tid = None

        if stream.tdata.tuser is not None:
            tuser = stream.tdata.tuser
        else:
            tuser = None

        if stream.tdata.tdest is not None:
            tdest = stream.tdata.tdest
        else:
            tdest = None

        self.tdata.tdata.connect(tdata)
        self.tdata.tvalid.connect(tvalid)
        tready.connect(self.tdata.tready)

        if self.tdata.tlast is not None:
            self.tdata.tlast.connect(tlast if tlast is not None else 1)
        if self.tdata.tid is not None:
            self.tdata.tid.connect(tid if tid is not None else 0)
        if self.tdata.tuser is not None:
            self.tdata.tuser.connect(tuser if tuser is not None else 0)
        if self.tdata.tdest is not None:
            self.tdata.tdest.connect(tdest if tdest is not None else 0)

    def connect_master_rdata(self, master):
        if not isinstance(master, AxiMaster):
            raise TypeError('master must be an instance of AxiMaster.')

        if not self.noio:
            raise ValueError('I/O ports can not be connected to others.')

        tdata = master.rdata.rdata
        tvalid = master.rdata.rvalid
        tready = master.rdata.rready

        tlast = 0

        if master.rdata.rid is not None:
            tid = master.rdata.rid
        else:
            tid = None

        if master.rdata.ruser is not None:
            tuser = master.rdata.ruser
        else:
            tuser = None

        tdest = None

        self.tdata.tdata.connect(tdata)
        self.tdata.tvalid.connect(tvalid)
        tready.connect(self.tdata.tready)

        if self.tdata.tlast is not None:
            self.tdata.tlast.connect(tlast if tlast is not None else 1)
        if self.tdata.tid is not None:
            self.tdata.tid.connect(tid if tid is not None else 0)
        if self.tdata.tuser is not None:
            self.tdata.tuser.connect(tuser if tuser is not None else 0)
        if self.tdata.tdest is not None:
            self.tdata.tdest.connect(tdest if tdest is not None else 0)


class AxiStreamOut(object):

    def __init__(self, m, name, clk, rst, datawidth=32,
                 with_last=True, with_strb=False,
                 id_width=0, user_width=0, dest_width=0,
                 noio=False, nodataflow=False):

        self.m = m
        self.name = name

        self.clk = clk
        self.rst = rst

        self.datawidth = datawidth

        self.noio = noio

        if not hasattr(self.m, 'streamoutbus'):
            self.m.streamoutbus = []

        self.m.streamoutbus.append(self)

        itype = util.t_Reg if noio else None
        otype = util.t_Wire if noio else None

        self.tdata = AxiStreamOutData(m, name, datawidth,
                                      with_last, with_strb,
                                      id_width, user_width, dest_width,
                                      itype, otype)

        self.seq = Seq(m, name, clk, rst)

        # default values
        if self.tdata.tuser is not None:
            self.tdata.tuser.assign(0)

        if self.tdata.tid is not None:
            self.tdata.tid.assign(0)

        if nodataflow:
            self.df = None
        else:
            self.df = DataflowManager(self.m, self.clk, self.rst)

    def write_data(self, data, last=None, _id=None, user=None, dest=None, cond=None):
        """
        @return ack
        """
        if cond is not None:
            self.seq.If(cond)

        ack = vtypes.Ors(self.tdata.tready, vtypes.Not(self.tdata.tvalid))

        self.seq.If(ack)(
            self.tdata.tdata(data),
            self.tdata.tvalid(1),
            self.tdata.tlast(last) if self.tdata.tlast is not None else (),
            self.tdata.tid(_id) if self.tdata.tid is not None else (),
            self.tdata.tuser(user) if self.tdata.tuser is not None else (),
            self.tdata.tdest(dest) if self.tdata.tdest is not None else (),
        )

        # de-assert
        self.seq.Delay(1)(
            self.tdata.tvalid(0),
            self.tdata.tlast(0) if self.tdata.tlast is not None else ()
        )

        # retry
        self.seq.If(vtypes.Ands(self.tdata.tvalid, vtypes.Not(self.tdata.tready)))(
            self.tdata.tvalid(self.tdata.tvalid),
            self.tdata.tlast(self.tdata.tlast) if self.tdata.tlast is not None else ()
        )

        return ack

    def write_dataflow(self, data, last=None, _id=None, user=None, dest=None, cond=None, when=None):
        """
        @return ack
        'data', 'last', '_id', 'user', 'dest', and 'when' must be dataflow variables
        """
        ack = vtypes.Ors(self.tdata.tready, vtypes.Not(self.tdata.tvalid))

        if cond is None:
            cond = ack
        else:
            cond = (cond, ack)

        args = [data]
        last_index = 0
        id_index = 0
        user_index = 0
        dest_index = 0
        when_index = 0
        if last is not None:
            args.append(last)
            last_index = len(args) - 1
        if _id is not None:
            args.append(_id)
            id_index = len(args) - 1
        if user is not None:
            args.append(user)
            user_index = len(args) - 1
        if dest is not None:
            args.append(dest)
            dest_index = len(args) - 1
        if when is not None:
            args.append(when)
            when_index = len(args) - 1

        data_list, raw_valid = read_multi(self.m, *args, cond=cond)
        raw_data = data_list[0]
        raw_last = data_list[last_index] if last_index > 0 else None
        raw_id = data_list[id_index] if id_index > 0 else None
        raw_user = data_list[user_index] if user_index > 0 else None
        raw_dest = data_list[dest_index] if dest_index > 0 else None
        raw_when = data_list[when_index] if when_index > 0 else None

        when_cond = make_condition(raw_when, ready=cond)
        if when_cond is not None:
            raw_valid = vtypes.Ands(when_cond, raw_valid)

        # write condition
        self.seq.If(raw_valid)

        self.seq.If(ack)(
            self.tdata.tdata(raw_data),
            self.tdata.tvalid(1),
            self.tdata.tlast(raw_last) if self.tdata.tlast is not None else (),
            self.tdata.tid(raw_id) if self.tdata.tid is not None else (),
            self.tdata.tuser(raw_user) if self.tdata.tuser is not None else (),
            self.tdata.tdest(raw_dest) if self.tdata.tdest is not None else (),
        )

        # de-assert
        self.seq.Delay(1)(
            self.tdata.tvalid(0),
            self.tdata.tlast(0)
        )

        # retry
        self.seq.If(vtypes.Ands(self.tdata.tvalid, vtypes.Not(self.tdata.tready)))(
            self.tdata.tvalid(self.tdata.tvalid),
            self.tdata.tlast(self.tdata.tlast) if self.tdata.tlast is not None else ()
        )

        ack = vtypes.Ands(self.tdata.tvalid, self.tdata.tready)

        return ack

    def connect(self, ports, name):
        if not self.noio:
            raise ValueError('I/O ports can not be connected to others.')

        tdata = ports['_'.join([name, 'tdata'])]
        tvalid = ports['_'.join([name, 'tvalid'])]
        tready = ports['_'.join([name, 'tready'])]

        if '_'.join([name, 'tlast']) in ports:
            tlast = ports['_'.join([name, 'tlast'])]
        else:
            tlast = None

        if '_'.join([name, 'tid']) in ports:
            tid = ports['_'.join([name, 'tid'])]
        else:
            tid = None

        if '_'.join([name, 'tuser']) in ports:
            tuser = ports['_'.join([name, 'tuser'])]
        else:
            tuser = None

        if '_'.join([name, 'tdest']) in ports:
            tdest = ports['_'.join([name, 'tdest'])]
        else:
            tdest = None

        tdata.connect(self.tdata.tdata)
        tvalid.connect(self.tdata.tvalid)
        self.tdata.tready.connect(tready)

        if tlast is not None:
            tlast.connect(self.tdata.tlast if self.tdata.tlast is not None else 1)

        if tuser is not None:
            tuser.connect(self.tdata.tuser if self.tdata.tuser is not None else 0)

        if tid is not None:
            tid.connect(self.tdata.tid if self.tdata.tid is not None else 0)

        if tdest is not None:
            tdest.connect(self.tdata.tdest if self.tdata.tdest is not None else 0)

    def connect_stream(self, stream):
        if not isinstance(stream, AxiStreamIn):
            raise TypeError('stream must be an instance of AxiStreamIn.')

        if not self.noio:
            raise ValueError('I/O ports can not be connected to others.')

        tdata = stream.tdata.tdata
        tvalid = stream.tdata.tvalid
        tready = stream.tdata.tready

        if stream.tdata.tlast is not None:
            tlast = stream.tdata.tlast
        else:
            tlast = None

        if stream.tdata.tid is not None:
            tid = stream.tdata.tid
        else:
            tid = None

        if stream.tdata.tuser is not None:
            tuser = stream.tdata.tuser
        else:
            tuser = None

        if stream.tdata.tdest is not None:
            tdest = stream.tdata.tdest
        else:
            tdest = None

        tdata.connect(self.tdata.tdata)
        tvalid.connect(self.tdata.tvalid)
        self.tdata.tready.connect(tready)

        if tlast is not None:
            tlast.connect(self.tdata.tlast if self.tdata.tlast is not None else 1)
        if tuser is not None:
            tuser.connect(self.tdata.tuser if self.tdata.tuser is not None else 0)
        if tid is not None:
            tid.connect(self.tdata.tid if self.tdata.tid is not None else 0)
        if tdest is not None:
            tdest.connect(self.tdata.tdest if self.tdata.tdest is not None else 0)


class AxiMemoryModel(AxiSlave):
    __intrinsics__ = ('read', 'write',
                      'read_word', 'write_word')

    def __init__(self, m, name, clk, rst, datawidth=32, addrwidth=32,
                 mem_datawidth=32, mem_addrwidth=20,
                 memimg=None, memimg_name=None,
                 memimg_datawidth=None,
                 write_delay=10, read_delay=10, sleep=4, sub_sleep=4,
                 waddr_id_width=0, wdata_id_width=0, wresp_id_width=0,
                 raddr_id_width=0, rdata_id_width=0,
                 waddr_user_width=2, wdata_user_width=0, wresp_user_width=0,
                 raddr_user_width=2, rdata_user_width=0,
                 wresp_user_mode=xUSER_DEFAULT,
                 rdata_user_mode=xUSER_DEFAULT):

        if mem_datawidth % 8 != 0:
            raise ValueError('mem_datawidth must be a multiple of 8')

        self.m = m
        self.name = name

        self.clk = clk
        self.rst = rst

        self.datawidth = datawidth
        self.addrwidth = addrwidth

        self.noio = True

        self.mem_datawidth = mem_datawidth
        self.mem_addrwidth = mem_addrwidth

        itype = util.t_Reg
        otype = util.t_Wire

        self.waddr = AxiSlaveWriteAddress(m, name, datawidth, addrwidth,
                                          waddr_id_width, waddr_user_width, itype, otype)
        self.wdata = AxiSlaveWriteData(m, name, datawidth, addrwidth,
                                       wdata_id_width, wdata_user_width, itype, otype)
        self.wresp = AxiSlaveWriteResponse(m, name, datawidth, addrwidth,
                                           wresp_id_width, wresp_user_width, itype, otype)
        self.raddr = AxiSlaveReadAddress(m, name, datawidth, addrwidth,
                                         raddr_id_width, raddr_user_width, itype, otype)
        self.rdata = AxiSlaveReadData(m, name, datawidth, addrwidth,
                                      rdata_id_width, rdata_user_width, itype, otype)

        # default values
        self.wresp.bresp.assign(0)
        if self.wresp.buser is not None:
            self.wresp.buser.assign(wresp_user_mode)
        self.rdata.rresp.assign(0)
        if self.rdata.ruser is not None:
            self.rdata.ruser.assign(rdata_user_mode)

        self.fsm = FSM(self.m, '_'.join(['', self.name, 'fsm']), clk, rst)

        # write response
        if self.wresp.bid is not None:
            self.fsm.seq.If(self.waddr.awvalid, self.waddr.awready,
                            vtypes.Not(self.wresp.bvalid))(
                self.wresp.bid(self.waddr.awid if self.waddr.awid is not None else 0)
            )

        if self.rdata.rid is not None:
            self.fsm.seq.If(self.raddr.arvalid, self.raddr.arready)(
                self.rdata.rid(self.raddr.arid if self.raddr.arid is not None else 0)
            )

        self.fsm.seq.If(self.wresp.bvalid, self.wresp.bready)(
            self.wresp.bvalid(0)
        )
        self.fsm.seq.If(self.wdata.wvalid, self.wdata.wready, self.wdata.wlast)(
            self.wresp.bvalid(1)
        )

        if memimg is None:
            if memimg_name is None:
                memimg_name = '_'.join(['', self.name, 'memimg', '.out'])
            size = 2 ** self.mem_addrwidth
            width = self.mem_datawidth
            self._make_img(memimg_name, size, width)

        elif isinstance(memimg, str):
            memimg_name = memimg

            num_words = sum(1 for line in open(memimg, 'r'))
            # resize mem_addrwidth according to the memimg size
            self.mem_addrwidth = max(self.mem_addrwidth,
                                     int(math.ceil(math.log(num_words, 2))))

        else:
            if memimg_datawidth is None:
                memimg_datawidth = mem_datawidth
            if memimg_name is None:
                memimg_name = '_'.join(['', self.name, 'memimg', '.out'])

            num_words = to_memory_image(memimg_name, memimg, datawidth=memimg_datawidth)
            # resize mem_addrwidth according to the memimg size
            self.mem_addrwidth = max(self.mem_addrwidth,
                                     int(math.ceil(math.log(num_words, 2))))

        self.mem = self.m.Reg(
            '_'.join(['', self.name, 'mem']), 8, vtypes.Int(2) ** self.mem_addrwidth)

        self.m.Initial(
            vtypes.Systask('readmemh', memimg_name, self.mem)
        )

        self._make_fsm(write_delay, read_delay, sleep, sub_sleep)

    @staticmethod
    def _make_img(filename, size, width, blksize=4096):
        import numpy as np

        wordsize = width // 8
        zero = np.zeros([size // wordsize, wordsize], dtype=np.int64)
        base = np.arange(size // wordsize, dtype=np.int64).reshape([-1, 1])
        shamt = np.arange(wordsize, dtype=np.int64) * [8]
        mask = np.full([1], 2 ** 8 - 1, dtype=np.int64)
        data = (((zero + base) >> shamt) & mask).reshape([-1])
        fmt = '%02x\n'

        with open(filename, 'w') as f:
            for i in range(0, len(data), blksize):
                blk = data[i:i + blksize]
                s = ''.join([fmt % d for d in blk])
                f.write(s)

    def _make_fsm(self, write_delay=10, read_delay=10, sleep=4, sub_sleep=4):
        write_mode = 100
        read_mode = 200
        while read_mode <= write_mode + write_delay + 10:
            read_mode += 100

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

            if sub_sleep > 0:
                sub_sleep_count = self.m.Reg(
                    '_'.join(['', 'sub_sleep_count']), self.addrwidth + 1, initval=0)

                self.fsm.seq.If(sleep_count == sleep - 1)(
                    sub_sleep_count.inc()
                )
                self.fsm.seq.If(sleep_count == sleep - 1,
                                sub_sleep_count == sub_sleep - 1)(
                    sub_sleep_count(0)
                )
                cond = sub_sleep_count == sub_sleep - 1
            else:
                cond = None

            self.fsm.seq.If(sleep_count < sleep - 1)(
                sleep_count.inc()
            )
            self.fsm.seq.If(cond, sleep_count == sleep - 1)(
                sleep_count(0)
            )

        # write mode
        self.fsm._set_index(write_mode)

        # awvalid and awready
        self.fsm.If(self.waddr.awvalid, vtypes.Not(self.wresp.bvalid))(
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


class AxiMultiportMemoryModel(AxiMemoryModel):
    __intrinsics__ = ('read', 'write',
                      'read_word', 'write_word')

    def __init__(self, m, name, clk, rst, datawidth=32, addrwidth=32, numports=2,
                 mem_datawidth=32, mem_addrwidth=20,
                 memimg=None, memimg_name=None,
                 memimg_datawidth=None,
                 write_delay=10, read_delay=10, sleep=4, sub_sleep=4,
                 waddr_id_width=0, wdata_id_width=0, wresp_id_width=0,
                 raddr_id_width=0, rdata_id_width=0,
                 waddr_user_width=2, wdata_user_width=0, wresp_user_width=0,
                 raddr_user_width=2, rdata_user_width=0,
                 wresp_user_mode=xUSER_DEFAULT,
                 rdata_user_mode=xUSER_DEFAULT):

        if mem_datawidth % 8 != 0:
            raise ValueError('mem_datawidth must be a multiple of 8')

        self.m = m
        self.name = name

        self.clk = clk
        self.rst = rst

        self.datawidth = datawidth
        self.addrwidth = addrwidth

        self.numports = numports

        self.noio = True

        self.mem_datawidth = mem_datawidth
        self.mem_addrwidth = mem_addrwidth

        itype = util.t_Reg
        otype = util.t_Wire

        self.waddrs = [AxiSlaveWriteAddress(m, name + '_%d' % i, datawidth, addrwidth,
                                            waddr_id_width, waddr_user_width, itype, otype)
                       for i in range(numports)]
        self.wdatas = [AxiSlaveWriteData(m, name + '_%d' % i, datawidth, addrwidth,
                                         wdata_id_width, wdata_user_width, itype, otype)
                       for i in range(numports)]
        self.wresps = [AxiSlaveWriteResponse(m, name + '%d' % i, datawidth, addrwidth,
                                             wresp_id_width, wresp_user_width, itype, otype)
                       for i in range(numports)]
        self.raddrs = [AxiSlaveReadAddress(m, name + '_%d' % i, datawidth, addrwidth,
                                           raddr_id_width, raddr_user_width, itype, otype)
                       for i in range(numports)]
        self.rdatas = [AxiSlaveReadData(m, name + '_%d' % i, datawidth, addrwidth,
                                        rdata_id_width, rdata_user_width, itype, otype)
                       for i in range(numports)]

        # default values
        for wresp in self.wresps:
            wresp.bresp.assign(0)
            if wresp.buser is not None:
                wresp.buser.assign(wresp_user_mode)

        for rdata in self.rdatas:
            rdata.rresp.assign(0)
            if rdata.ruser is not None:
                rdata.ruser.assign(rdata_user_mode)

        self.seq = Seq(self.m, '_'.join(['', self.name, 'seq']), clk, rst)
        self.fsms = [FSM(self.m, '_'.join(['', self.name, 'fsm_%d' % i]), clk, rst)
                     for i in range(numports)]

        # all FSM shares an indentical Seq
        for fsm in self.fsms:
            fsm.seq = self.seq

        # write response
        for wresp, waddr in zip(self.wresps, self.waddrs):
            if wresp.bid is not None:
                self.seq.If(waddr.awvalid, waddr.awready,
                            vtypes.Not(wresp.bvalid))(
                    wresp.bid(waddr.awid if waddr.awid is not None else 0)
                )

        for rdata, raddr in zip(self.rdatas, self.raddrs):
            if rdata.rid is not None:
                self.seq.If(raddr.arvalid, raddr.arready)(
                    rdata.rid(raddr.arid if raddr.arid is not None else 0)
                )

        for wresp, wdata in zip(self.wresps, self.wdatas):
            self.seq.If(wresp.bvalid, wresp.bready)(
                wresp.bvalid(0)
            )
            self.seq.If(wdata.wvalid, wdata.wready, wdata.wlast)(
                wresp.bvalid(1)
            )

        if memimg is None:
            if memimg_name is None:
                memimg_name = '_'.join(['', self.name, 'memimg', '.out'])
            size = 2 ** self.mem_addrwidth
            width = self.mem_datawidth
            self._make_img(memimg_name, size, width)

        elif isinstance(memimg, str):
            memimg_name = memimg

            num_words = sum(1 for line in open(memimg, 'r'))
            # resize mem_addrwidth according to the memimg size
            self.mem_addrwidth = max(self.mem_addrwidth,
                                     int(math.ceil(math.log(num_words, 2))))

        else:
            if memimg_datawidth is None:
                memimg_datawidth = mem_datawidth
            if memimg_name is None:
                memimg_name = '_'.join(['', self.name, 'memimg', '.out'])

            num_words = to_memory_image(memimg_name, memimg, datawidth=memimg_datawidth)
            # resize mem_addrwidth according to the memimg size
            self.mem_addrwidth = max(self.mem_addrwidth,
                                     int(math.ceil(math.log(num_words, 2))))

        self.mem = self.m.Reg(
            '_'.join(['', self.name, 'mem']), 8, vtypes.Int(2) ** self.mem_addrwidth)

        self.m.Initial(
            vtypes.Systask('readmemh', memimg_name, self.mem)
        )

        self._make_fsms(write_delay, read_delay, sleep, sub_sleep)

    def _make_fsms(self, write_delay=10, read_delay=10, sleep=4, sub_sleep=4):
        write_mode = 0
        read_mode = 0

        for i, (fsm, waddr, wdata, wresp, raddr, rdata) in enumerate(
                zip(self.fsms, self.waddrs, self.wdatas, self.wresps, self.raddrs, self.rdatas)):

            write_count = self.m.Reg(
                '_'.join(['', 'write_count_%d' % i]), self.addrwidth + 1, initval=0)
            write_addr = self.m.Reg(
                '_'.join(['', 'write_addr_%d' % i]), self.addrwidth, initval=0)
            read_count = self.m.Reg(
                '_'.join(['', 'read_count_%d' % i]), self.addrwidth + 1, initval=0)
            read_addr = self.m.Reg(
                '_'.join(['', 'read_addr_%d' % i]), self.addrwidth, initval=0)

            if sleep > 0:
                sleep_count = self.m.Reg(
                    '_'.join(['', 'sleep_count_%d' % i]), self.addrwidth + 1, initval=0)

                if sub_sleep > 0:
                    sub_sleep_count = self.m.Reg(
                        '_'.join(['', 'sub_sleep_count_%d' % i]), self.addrwidth + 1, initval=0)

                    fsm.seq.If(sleep_count == sleep - 1)(
                        sub_sleep_count.inc()
                    )
                    fsm.seq.If(sleep_count == sleep - 1,
                               sub_sleep_count == sub_sleep - 1)(
                        sub_sleep_count(0)
                    )
                    cond = sub_sleep_count == sub_sleep - 1
                else:
                    cond = None

                fsm.seq.If(sleep_count < sleep - 1)(
                    sleep_count.inc()
                )
                fsm.seq.If(cond, sleep_count == sleep - 1)(
                    sleep_count(0)
                )

            offset = 100 * i
            while offset <= read_mode + read_delay + 10:
                offset += 100

            write_mode = offset + 100
            read_mode = offset + 200
            while read_mode <= write_mode + write_delay + 10:
                read_mode += 100

            fsm.If(waddr.awvalid).goto(write_mode)
            fsm.If(raddr.arvalid).goto(read_mode)

            # write mode
            fsm._set_index(write_mode)

            # awvalid and awready
            fsm.If(waddr.awvalid, vtypes.Not(wresp.bvalid))(
                waddr.awready(1),
                write_addr(waddr.awaddr),
                write_count(waddr.awlen + 1)
            )
            fsm.Delay(1)(
                waddr.awready(0)
            )
            fsm.If(vtypes.Not(waddr.awvalid)).goto_init()
            fsm.If(waddr.awvalid).goto_next()

            # delay
            for _ in range(write_delay):
                fsm.goto_next()

            # wready
            fsm(
                wdata.wready(1)
            )
            fsm.goto_next()

            # wdata -> mem
            for i in range(int(self.datawidth / 8)):
                fsm.If(wdata.wvalid, wdata.wstrb[i])(
                    self.mem[write_addr + i](wdata.wdata[i * 8:i * 8 + 8])
                )

            fsm.If(wdata.wvalid, wdata.wready)(
                write_addr.add(int(self.datawidth / 8)),
                write_count.dec()
            )

            # sleep
            if sleep > 0:
                fsm.If(sleep_count == sleep - 1)(
                    wdata.wready(0)
                ).Else(
                    wdata.wready(1)
                )

            # write complete
            fsm.If(wdata.wvalid, wdata.wready, write_count == 1)(
                wdata.wready(0)
            )
            fsm.Then().goto_init()

            # read mode
            fsm._set_index(read_mode)

            # arvalid and arready
            fsm.If(raddr.arvalid)(
                raddr.arready(1),
                read_addr(raddr.araddr),
                read_count(raddr.arlen + 1)
            )
            fsm.Delay(1)(
                raddr.arready(0)
            )
            fsm.If(vtypes.Not(raddr.arvalid)).goto_init()
            fsm.If(raddr.arvalid).goto_next()

            # delay
            for _ in range(read_delay):
                fsm.goto_next()

            # mem -> rdata
            for i in range(int(self.datawidth / 8)):
                fsm.If(vtypes.Or(rdata.rready, vtypes.Not(rdata.rvalid)))(
                    rdata.rdata[i * 8:i * 8 + 8](self.mem[read_addr + i])
                )

            if sleep > 0:
                fsm.If(sleep_count < sleep - 1, read_count > 0,
                       vtypes.Or(rdata.rready, vtypes.Not(rdata.rvalid)))(
                    rdata.rvalid(1),
                    read_addr.add(int(self.datawidth / 8)),
                    read_count.dec()
                )
                fsm.If(sleep_count < sleep - 1, read_count == 1,
                       vtypes.Or(rdata.rready, vtypes.Not(rdata.rvalid)))(
                    rdata.rlast(1)
                )
            else:
                fsm.If(read_count > 0,
                       vtypes.Or(rdata.rready, vtypes.Not(rdata.rvalid)))(
                    rdata.rvalid(1),
                    read_addr.add(int(self.datawidth / 8)),
                    read_count.dec()
                )
                fsm.If(read_count == 1,
                       vtypes.Or(rdata.rready, vtypes.Not(rdata.rvalid)))(
                    rdata.rlast(1)
                )

            # de-assert
            fsm.Delay(1)(
                rdata.rvalid(0),
                rdata.rlast(0)
            )

            # retry
            fsm.If(rdata.rvalid, vtypes.Not(rdata.rready))(
                rdata.rvalid(rdata.rvalid),
                rdata.rdata(rdata.rdata),
                rdata.rlast(rdata.rlast)
            )

            # read complete
            fsm.If(rdata.rvalid, rdata.rready,
                   read_count == 0).goto_init()

    def connect(self, index, ports, name):
        if not self.noio:
            raise ValueError('I/O ports can not be connected to others.')

        ports = defaultdict(lambda: None, ports)

        if '_'.join([name, 'awid']) in ports:
            awid = ports['_'.join([name, 'awid'])]
        else:
            awid = None
        awaddr = ports['_'.join([name, 'awaddr'])]
        awlen = ports['_'.join([name, 'awlen'])]
        awsize = ports['_'.join([name, 'awsize'])]
        awburst = ports['_'.join([name, 'awburst'])]
        awlock = ports['_'.join([name, 'awlock'])]
        awcache = ports['_'.join([name, 'awcache'])]
        awprot = ports['_'.join([name, 'awprot'])]
        awqos = ports['_'.join([name, 'awqos'])]
        if '_'.join([name, 'awuser']) in ports:
            awuser = ports['_'.join([name, 'awuser'])]
        else:
            awuser = None
        awvalid = ports['_'.join([name, 'awvalid'])]
        awready = ports['_'.join([name, 'awready'])]

        if self.waddrs[index].awid is not None:
            self.waddrs[index].awid.connect(awid if awid is not None else 0)
        self.waddrs[index].awaddr.connect(awaddr)
        self.waddrs[index].awlen.connect(awlen if awlen is not None else 0)
        self.waddrs[index].awsize.connect(awsize if awsize is not None else
                                          int(math.log(self.datawidth // 8)))
        self.waddrs[index].awburst.connect(awburst if awburst is not None else BURST_INCR)
        self.waddrs[index].awlock.connect(awlock if awlock is not None else 0)
        self.waddrs[index].awcache.connect(awcache)
        self.waddrs[index].awprot.connect(awprot)
        self.waddrs[index].awqos.connect(awqos if awqos is not None else 0)
        if self.waddrs[index].awuser is not None:
            self.waddrs[index].awuser.connect(awuser if awuser is not None else 0)
        self.waddrs[index].awvalid.connect(awvalid)
        awready.connect(self.waddrs[index].awready)

        wdata = ports['_'.join([name, 'wdata'])]
        wstrb = ports['_'.join([name, 'wstrb'])]
        wlast = ports['_'.join([name, 'wlast'])]
        if '_'.join([name, 'wuser']) in ports:
            wuser = ports['_'.join([name, 'wuser'])]
        else:
            wuser = None
        wvalid = ports['_'.join([name, 'wvalid'])]
        wready = ports['_'.join([name, 'wready'])]

        self.wdatas[index].wdata.connect(wdata)
        self.wdatas[index].wstrb.connect(wstrb)
        self.wdatas[index].wlast.connect(wlast if wlast is not None else 1)
        if self.wdatas[index].wuser is not None:
            self.wdatas[index].wuser.connect(wuser if wuser is not None else 0)
        self.wdatas[index].wvalid.connect(wvalid)
        wready.connect(self.wdatas[index].wready)

        if '_'.join([name, 'bid']) in ports:
            bid = ports['_'.join([name, 'bid'])]
        else:
            bid = None
        bresp = ports['_'.join([name, 'bresp'])]
        if '_'.join([name, 'buser']) in ports:
            buser = ports['_'.join([name, 'buser'])]
        else:
            buser = None
        bvalid = ports['_'.join([name, 'bvalid'])]
        bready = ports['_'.join([name, 'bready'])]

        if bid is not None:
            bid.connect(self.wresps[index].bid if self.wresps[index].bid is not None else 0)
        bresp.connect(self.wresps[index].bresp)
        if buser is not None:
            buser.connect(self.wresps[index].buser if self.wresps[index].buser is not None else 0)
        bvalid.connect(self.wresps[index].bvalid)
        self.wresps[index].bready.connect(bready)

        if '_'.join([name, 'arid']) in ports:
            arid = ports['_'.join([name, 'arid'])]
        else:
            arid = None
        araddr = ports['_'.join([name, 'araddr'])]
        arlen = ports['_'.join([name, 'arlen'])]
        arsize = ports['_'.join([name, 'arsize'])]
        arburst = ports['_'.join([name, 'arburst'])]
        arlock = ports['_'.join([name, 'arlock'])]
        arcache = ports['_'.join([name, 'arcache'])]
        arprot = ports['_'.join([name, 'arprot'])]
        arqos = ports['_'.join([name, 'arqos'])]
        if '_'.join([name, 'aruser']) in ports:
            aruser = ports['_'.join([name, 'aruser'])]
        else:
            aruser = None
        arvalid = ports['_'.join([name, 'arvalid'])]
        arready = ports['_'.join([name, 'arready'])]

        if self.raddrs[index].arid is not None:
            self.raddrs[index].arid.connect(arid if arid is not None else 0)
        self.raddrs[index].araddr.connect(araddr)
        self.raddrs[index].arlen.connect(arlen if arlen is not None else 0)
        self.raddrs[index].arsize.connect(arsize if arsize is not None else
                                          int(math.log(self.datawidth // 8)))
        self.raddrs[index].arburst.connect(arburst if arburst is not None else BURST_INCR)
        self.raddrs[index].arlock.connect(arlock if arlock is not None else 0)
        self.raddrs[index].arcache.connect(arcache)
        self.raddrs[index].arprot.connect(arprot)
        self.raddrs[index].arqos.connect(arqos if arqos is not None else 0)
        if self.raddrs[index].aruser is not None:
            self.raddrs[index].aruser.connect(aruser if aruser is not None else 0)
        self.raddrs[index].arvalid.connect(arvalid)
        arready.connect(self.raddrs[index].arready)

        if '_'.join([name, 'rid']) in ports:
            rid = ports['_'.join([name, 'rid'])]
        else:
            rid = None
        rdata = ports['_'.join([name, 'rdata'])]
        rresp = ports['_'.join([name, 'rresp'])]
        rlast = ports['_'.join([name, 'rlast'])]
        if '_'.join([name, 'ruser']) in ports:
            ruser = ports['_'.join([name, 'ruser'])]
        else:
            ruser = None
        rvalid = ports['_'.join([name, 'rvalid'])]
        rready = ports['_'.join([name, 'rready'])]

        if rid is not None:
            rid.connect(self.rdatas[index].rid if self.rdatas[index].rid is not None else 0)
        rdata.connect(self.rdatas[index].rdata)
        rresp.connect(self.rdatas[index].rresp)
        if rlast is not None:
            rlast.connect(self.rdatas[index].rlast)
        if ruser is not None:
            ruser.connect(self.rdatas[index].ruser if self.rdatas[index].ruser is not None else 0)
        rvalid.connect(self.rdatas[index].rvalid)
        self.rdatas[index].rready.connect(rready)


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
                    datawidth=32, wordwidth=8, endian='little', blksize=4096):

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

        zero = np.zeros(list(array.shape) + [num], dtype=np.int64)
        base = array.reshape([-1, 1])
        shamt = np.arange(num, dtype=np.int64) * [wordwidth]
        if endian == 'big':
            shamt.reverse()

        mask = np.full([1], 2 ** wordwidth - 1, dtype=np.int64)
        data = (((zero + base) >> shamt) & mask).reshape([-1])

        with open(filename, 'w') as f:
            for i in range(0, len(data), blksize):
                blk = data[i:i + blksize]
                s = ''.join([fmt % d for d in blk])
                f.write(s)

        return len(data)

    else:
        num = int(math.ceil(wordwidth / datawidth))

        base = array.reshape([-1, num])
        shamt = np.arange(num, dtype=np.int64) * [datawidth]
        if endian == 'big':
            shamt.reverse()

        mask = np.full([1], 2 ** datawidth - 1, dtype=np.int64)
        data = (base.reshape([-1, num]) & mask) << shamt
        data = np.bitwise_or.reduce(data, -1).reshape([-1])

        with open(filename, 'w') as f:
            for i in range(0, len(data), blksize):
                blk = data[i:i + blksize]
                s = ''.join([fmt % d for d in blk])
                f.write(s)

        return len(data)


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

    num_pack = int(math.ceil(mem_datawidth / src_datawidth))
    src_mask = np.full([1], 2 ** src_datawidth - 1, dtype=np.int64)
    mem_mask = np.full([1], 2 ** mem_datawidth - 1, dtype=np.int64)
    offset = mem_offset // int(math.ceil(mem_datawidth / 8))

    if src.shape[-1] % num_pack != 0:
        pads = []
        for s in src.shape[:-1]:
            pads.append((0, 0))
        pads.append((0, num_pack - src.shape[-1]))

        src = np.pad(src, pads, 'constant')

    masked_data = src.astype(np.int64) & src_mask
    pack = np.arange(src.shape[-1], dtype=np.int64) % [num_pack]
    shift = [src_datawidth] * pack
    v = (masked_data << shift) & mem_mask
    v = np.reshape(v, [-1, num_pack])
    v = np.bitwise_or.reduce(v, -1)

    dst_size = mem[offset:offset + v.shape[-1]].size
    if v.size > dst_size:
        raise ValueError("""too large source data: """
                         """destination size (%d) < source size (%d)""" %
                         (dst_size, v.size))
    mem[offset:offset + v.shape[-1]] = v


def _set_memory_narrow(mem, src, mem_datawidth, src_datawidth, mem_offset,
                       num_align_words=None):

    if mem_datawidth > 64:
        raise ValueError('not supported')

    import numpy as np

    if num_align_words is not None:
        src = align(src, num_align_words)

    num_pack = int(math.ceil(src_datawidth / mem_datawidth))
    src_mask = np.full([1], 2 ** src_datawidth - 1, dtype=np.int64)
    mem_mask = np.full([1], 2 ** mem_datawidth - 1, dtype=np.int64)
    offset = mem_offset // int(math.ceil(mem_datawidth / 8))

    pack = np.arange(num_pack, dtype=np.int64)
    shift = [mem_datawidth] * pack
    dup_src_based = np.zeros(list(src.shape) + [num_pack], dtype=np.int64)
    dup_src = dup_src_based + np.reshape(src, list(src.shape) + [1])
    v = dup_src >> shift
    v = np.reshape(v, [-1])
    v = v & mem_mask

    dst_size = mem[offset:offset + v.shape[-1]].size
    if v.size > dst_size:
        raise ValueError("""too large source data: """
                         """destination size (%d) < source size (%d)""" %
                         (dst_size, v.size))
    mem[offset:offset + v.shape[-1]] = v


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
