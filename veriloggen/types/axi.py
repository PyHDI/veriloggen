from __future__ import absolute_import
from __future__ import print_function

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


def _connect_ready(m, var, val):
    prev_assign = var._get_assign()

    if not prev_assign:
        var.assign(val)
    else:
        prev_assign.overwrite_right(
            vtypes.Ors(prev_assign.statement.right, val))
        m.remove(prev_assign)
        m.append(prev_assign)


class AxiBase(object):
    _I = util.t_Input
    _O = util.t_OutputReg

    def __init__(self, m, name=None, datawidth=32, addrwidth=32,
                 itype=None, otype=None, lite=False):
        if itype is None:
            itype = self._I
        if otype is None:
            otype = self._O
        self.m = m
        self.datawidth = datawidth
        self.addrwidth = addrwidth
        self.itype = itype
        self.otype = otype
        self.lite = lite


class AxiWriteAddress(AxiBase):

    def __init__(self, m, name=None, datawidth=32, addrwidth=32,
                 itype=None, otype=None, lite=False):
        AxiBase.__init__(self, m, name, datawidth,
                         addrwidth, itype, otype, lite)
        self.awaddr = util.make_port(
            m, self.otype, name + '_awaddr', self.addrwidth, initval=0)
        if not self.lite:
            self.awlen = util.make_port(
                m, self.otype, name + '_awlen', 8, initval=0)
        self.awvalid = util.make_port(
            m, self.otype, name + '_awvalid', None, initval=0)
        self.awready = util.make_port(
            m, self.itype, name + '_awready', None, initval=0)


class AxiWriteData(AxiBase):

    def __init__(self, m, name=None, datawidth=32, addrwidth=32,
                 itype=None, otype=None, lite=False):
        AxiBase.__init__(self, m, name, datawidth,
                         addrwidth, itype, otype, lite)
        self.wdata = util.make_port(
            m, self.otype, name + '_wdata', self.datawidth, initval=0)
        self.wstrb = util.make_port(
            m, self.otype, name + '_wstrb', self.datawidth // 8, initval=0)
        if not self.lite:
            self.wlast = util.make_port(
                m, self.otype, name + '_wlast', None, initval=0)
        self.wvalid = util.make_port(
            m, self.otype, name + '_wvalid', None, initval=0)
        self.wready = util.make_port(
            m, self.itype, name + '_wready', None, initval=0)


class AxiReadAddress(AxiBase):

    def __init__(self, m, name=None, datawidth=32, addrwidth=32,
                 itype=None, otype=None, lite=False):
        AxiBase.__init__(self, m, name, datawidth,
                         addrwidth, itype, otype, lite)
        self.araddr = util.make_port(
            m, self.otype, name + '_araddr', self.addrwidth, initval=0)
        if not self.lite:
            self.arlen = util.make_port(
                m, self.otype, name + '_arlen', 8, initval=0)
        self.arvalid = util.make_port(
            m, self.otype, name + '_arvalid', None, initval=0)
        self.arready = util.make_port(
            m, self.itype, name + '_arready', None, initval=0)


class AxiReadData(AxiBase):
    _O = util.t_Output

    def __init__(self, m, name=None, datawidth=32, addrwidth=32,
                 itype=None, otype=None, lite=False):
        AxiBase.__init__(self, m, name, datawidth,
                         addrwidth, itype, otype, lite)
        self.rdata = util.make_port(
            m, self.itype, name + '_rdata', self.datawidth, initval=0)
        if not self.lite:
            self.rlast = util.make_port(
                m, self.itype, name + '_rlast', None, initval=0)
        self.rvalid = util.make_port(
            m, self.itype, name + '_rvalid', None, initval=0)
        self.rready = util.make_port(
            m, self.otype, name + '_rready', None, initval=0)


class AxiMasterWriteAddress(AxiWriteAddress):
    pass


class AxiMasterWriteData(AxiWriteData):
    pass


class AxiMasterReadAddress(AxiReadAddress):
    pass


class AxiMasterReadData(AxiReadData):
    pass


class AxiSlaveWriteAddress(AxiWriteAddress):
    _I = util.t_Output
    _O = util.t_Input


class AxiSlaveWriteData(AxiWriteData):
    _I = util.t_Output
    _O = util.t_Input


class AxiSlaveReadAddress(AxiReadAddress):
    _I = util.t_Output
    _O = util.t_Input


class AxiSlaveReadData(AxiReadData):
    _I = util.t_OutputReg
    _O = util.t_Input


class AxiMaster(object):
    burst_size_width = 8
    boundary_size = 4096

    def __init__(self, m, name, clk, rst, datawidth=32, addrwidth=32,
                 lite=False, noio=False, nodataflow=False):

        self.m = m
        self.name = name
        self.clk = clk
        self.rst = rst
        self.datawidth = datawidth
        self.addrwidth = addrwidth
        self.lite = lite
        self.noio = noio

        if not hasattr(self.m, 'masterbus'):
            self.m.masterbus = []

        self.m.masterbus.append(self)

        itype = util.t_Wire if noio else None
        otype = util.t_Reg if noio else None

        self.waddr = AxiMasterWriteAddress(
            m, name, datawidth, addrwidth, itype=itype, otype=otype, lite=lite)
        self.wdata = AxiMasterWriteData(
            m, name, datawidth, addrwidth, itype=itype, otype=otype, lite=lite)
        self.raddr = AxiMasterReadAddress(
            m, name, datawidth, addrwidth, itype=itype, otype=otype, lite=lite)

        otype = util.t_Wire if noio else None

        self.rdata = AxiMasterReadData(
            m, name, datawidth, addrwidth, itype=itype, otype=otype, lite=lite)

        self.seq = Seq(m, name, clk, rst)

        self.write_counters = []
        self.read_counters = []

        if nodataflow:
            self.df = None
        else:
            self.df = DataflowManager(self.m, self.clk, self.rst)

        self._write_disabled = False
        self._read_disabled = False

    def disable_write(self):
        ports = [self.waddr.awaddr(0)]
        if not self.lite:
            ports.append(self.waddr.awlen(0))

        ports.extend([self.waddr.awvalid(0),
                      self.wdata.wdata(0),
                      self.wdata.wstrb(0),
                      self.wdata.wvalid(0)])

        if not self.lite:
            ports.append(self.wdata.wlast(0))

        self.seq(
            *ports
        )
        self._write_disabled = True

    def disable_read(self):
        ports = [self.raddr.araddr(0)]
        if not self.lite:
            ports.append(self.raddr.arlen(0))
        ports.append(self.raddr.arvalid(0))

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
        @return ack, (counter)
        """
        if self._write_disabled:
            raise TypeError('Write disabled.')

        if self.lite:
            if length != 1:
                raise ValueError('length must be 1 for lite-interface.')

            return self._write_request_lite(addr, cond)

        return self._write_request_full(addr, length, cond, counter)

    def _write_request_lite(self, addr, cond=None):
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

    def _write_request_full(self, addr, length=1, cond=None, counter=None):
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
        @return ack, (last)
        """
        if self._write_disabled:
            raise TypeError('Write disabled.')

        if self.lite:
            return self._write_data_lite(data, cond)

        return self._write_data_full(data, counter, cond)

    def _write_data_lite(self, data, cond=None):
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

    def _write_data_full(self, data, counter=None, cond=None):
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
        if self.lite:
            raise TypeError('lite interface support no dataflow operation.')

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
        @return ack, (counter)
        """
        if self._read_disabled:
            raise TypeError('Read disabled.')

        if self.lite:
            if length != 1:
                raise ValueError('length must be 1 for lite-interface.')

            return self._read_request_lite(addr, cond)

        return self._read_request_full(addr, length, cond, counter)

    def _read_request_lite(self, addr, cond=None):
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

    def _read_request_full(self, addr, length=1, cond=None, counter=None):

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
        @return data, valid, (last)
        """
        if self._read_disabled:
            raise TypeError('Read disabled.')

        if self.lite:
            return self._read_data_lite(cond)

        return self._read_data_full(counter, cond)

    def _read_data_lite(self, cond=None):
        ready = make_condition(cond)
        val = 1 if ready is None else ready

        _connect_ready(self.rdata.rready._get_module(), self.rdata.rready, val)

        ack = vtypes.Ands(self.rdata.rready, self.rdata.rvalid)
        data = self.rdata.rdata
        valid = ack

        return data, valid

    def _read_data_full(self, counter=None, cond=None):
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
        if self.lite:
            raise TypeError('lite interface support no dataflow operation.')

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

        awaddr = ports['_'.join([name, 'awaddr'])]
        if '_'.join([name, 'awlen']) in ports:
            awlen = ports['_'.join([name, 'awlen'])]
        else:
            awlen = vtypes.Int(0)
        awvalid = ports['_'.join([name, 'awvalid'])]
        awready = ports['_'.join([name, 'awready'])]

        awaddr.connect(self.waddr.awaddr)
        if '_'.join([name, 'awlen']) in ports:
            awlen.connect(self.waddr.awlen)
        awvalid.connect(self.waddr.awvalid)
        self.waddr.awready.connect(awready)

        wdata = ports['_'.join([name, 'wdata'])]
        wstrb = ports['_'.join([name, 'wstrb'])]
        if '_'.join([name, 'wlast']) in ports:
            wlast = ports['_'.join([name, 'wlast'])]
        else:
            wlast = vtypes.Int(1)
        wvalid = ports['_'.join([name, 'wvalid'])]
        wready = ports['_'.join([name, 'wready'])]

        wdata.connect(self.wdata.wdata)
        wstrb.connect(self.wdata.wstrb)
        if '_'.join([name, 'wlast']) in ports:
            wlast.connect(self.wdata.wlast)
        wvalid.connect(self.wdata.wvalid)
        self.wdata.wready.connect(wready)

        araddr = ports['_'.join([name, 'araddr'])]
        if '_'.join([name, 'arlen']) in ports:
            arlen = ports['_'.join([name, 'arlen'])]
        else:
            arlen = vtypes.Int(0)
        arvalid = ports['_'.join([name, 'arvalid'])]
        arready = ports['_'.join([name, 'arready'])]

        araddr.connect(self.raddr.araddr)
        if '_'.join([name, 'arlen']) in ports:
            arlen.connect(self.raddr.arlen)
        arvalid.connect(self.raddr.arvalid)
        self.raddr.arready.connect(arready)

        rdata = ports['_'.join([name, 'rdata'])]
        if '_'.join([name, 'rlast']) in ports:
            rlast = ports['_'.join([name, 'rlast'])]
        else:
            rlast = vtypes.Int(1)
        rvalid = ports['_'.join([name, 'rvalid'])]
        rready = ports['_'.join([name, 'rready'])]

        self.rdata.rdata.connect(rdata)
        if not self.lite:
            self.rdata.rlast.connect(rlast)
        self.rdata.rvalid.connect(rvalid)
        rready.connect(self.rdata.rready)


def AxiLiteMaster(m, name, clk, rst, datawidth=32, addrwidth=32,
                  noio=False, nodataflow=False):

    return AxiMaster(m, name, clk, rst, datawidth=datawidth, addrwidth=addrwidth,
                     lite=True, noio=noio, nodataflow=nodataflow)


class AxiSlave(object):
    burst_size_width = 8

    def __init__(self, m, name, clk, rst, datawidth=32, addrwidth=32,
                 lite=False, noio=False, nodataflow=False):

        self.m = m
        self.name = name
        self.clk = clk
        self.rst = rst
        self.datawidth = datawidth
        self.addrwidth = addrwidth
        self.lite = lite
        self.noio = noio

        if not hasattr(self.m, 'slavebus'):
            self.m.slavebus = []

        self.m.slavebus.append(self)

        itype = util.t_Wire if noio else None
        otype = util.t_Wire if noio else None

        self.waddr = AxiSlaveWriteAddress(
            m, name, datawidth, addrwidth, itype=itype, otype=otype, lite=lite)
        self.wdata = AxiSlaveWriteData(
            m, name, datawidth, addrwidth, itype=itype, otype=otype, lite=lite)
        self.raddr = AxiSlaveReadAddress(
            m, name, datawidth, addrwidth, itype=itype, otype=otype, lite=lite)

        itype = util.t_Reg if noio else None

        self.rdata = AxiSlaveReadData(
            m, name, datawidth, addrwidth, itype=itype, otype=otype, lite=lite)

        self.seq = Seq(m, name, clk, rst)

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

        ports = [self.rdata.rvalid(0)]
        if not self.lite:
            ports.append(self.rdata.rlast(0))

        self.seq(
            *ports
        )
        self._read_disabled = True

    def pull_request(self, cond, counter=None):
        """
        @return addr, (counter), readvalid, writevalid
        """
        if self.lite:
            return self._pull_request_lite(cond)

        return self._pull_request_full(cond, counter)

    def _pull_request_lite(self, cond=None):
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

    def _pull_request_full(self, cond=None, counter=None):
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
        @return addr, (counter), valid
        """
        if self._write_disabled:
            raise TypeError('Write disabled.')

        if self.lite:
            return self._pull_write_request_lite(cond)

        return self._pull_write_request_full(cond, counter)

    def _pull_write_request_lite(self, cond=None):
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

    def _pull_write_request_full(self, cond=None, counter=None):
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
        @return data, mask, valid, (last)
        """
        if self._write_disabled:
            raise TypeError('Write disabled.')

        if self.lite:
            return self._pull_write_data_lite(cond)

        return self._pull_write_data_full(counter, cond)

    def _pull_write_data_lite(self, cond=None):
        ready = make_condition(cond)
        val = 1 if ready is None else ready

        _connect_ready(self.wdata.wready._get_module(), self.wdata.wready, val)

        ack = vtypes.Ands(self.wdata.wready, self.wdata.wvalid)
        data = self.wdata.wdata
        mask = self.wdata.wstrb
        valid = ack

        return data, mask, valid

    def _pull_write_data_full(self, counter=None, cond=None):

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
        if self.lite:
            raise TypeError('lite interface support no dataflow operation.')

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
        @return addr, (counter), valid
        """
        if self._read_disabled:
            raise TypeError('Read disabled.')

        if self.lite:
            return self._pull_read_request_lite(cond)

        return self._pull_read_request_full(cond, counter)

    def _pull_read_request_lite(self, cond=None):
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

    def _pull_read_request_full(self, cond=None, counter=None):
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
        @return ack, (last)
        """
        if self._read_disabled:
            raise TypeError('Read disabled.')

        if self.lite:
            return self._push_read_data_lite(data, cond)

        return self._push_read_data_full(data, counter, cond)

    def _push_read_data_lite(self, data, cond=None):
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

    def _push_read_data_full(self, data, counter=None, cond=None):
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
        if self.lite:
            raise TypeError('lite interface support no dataflow operation.')

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

        awaddr = ports['_'.join([name, 'awaddr'])]
        if '_'.join([name, 'awlen']) in ports:
            awlen = ports['_'.join([name, 'awlen'])]
        else:
            awlen = vtypes.Int(0)
        awvalid = ports['_'.join([name, 'awvalid'])]
        awready = ports['_'.join([name, 'awready'])]

        self.waddr.awaddr.assign(awaddr)
        if not self.lite:
            self.waddr.awlen.assign(awlen)
        self.waddr.awvalid.assign(awvalid)
        awready.assign(self.waddr.awready)

        wdata = ports['_'.join([name, 'wdata'])]
        wstrb = ports['_'.join([name, 'wstrb'])]
        if '_'.join([name, 'wlast']) in ports:
            wlast = ports['_'.join([name, 'wlast'])]
        else:
            wlast = vtypes.Int(1)
        wvalid = ports['_'.join([name, 'wvalid'])]
        wready = ports['_'.join([name, 'wready'])]

        self.wdata.wdata.assign(wdata)
        self.wdata.wstrb.assign(wstrb)
        if not self.lite:
            self.wdata.wlast.assign(wlast)
        self.wdata.wvalid.assign(wvalid)
        wready.assign(self.wdata.wready)

        araddr = ports['_'.join([name, 'araddr'])]
        if '_'.join([name, 'arlen']) in ports:
            arlen = ports['_'.join([name, 'arlen'])]
        else:
            arlen = vtypes.Int(0)
        arvalid = ports['_'.join([name, 'arvalid'])]
        arready = ports['_'.join([name, 'arready'])]

        self.raddr.araddr.assign(araddr)
        if not self.lite:
            self.raddr.arlen.assign(arlen)
        self.raddr.arvalid.assign(arvalid)
        arready.assign(self.raddr.arready)

        rdata = ports['_'.join([name, 'rdata'])]
        if '_'.join([name, 'rlast']) in ports:
            rlast = ports['_'.join([name, 'rlast'])]
        rvalid = ports['_'.join([name, 'rvalid'])]
        rready = ports['_'.join([name, 'rready'])]

        rdata.assign(self.rdata.rdata)
        if not self.lite and '_'.join([name, 'rlast']) in ports:
            rlast.assign(self.rdata.rlast)
        rvalid.assign(self.rdata.rvalid)
        self.rdata.rready.assign(rready)


def AxiLiteSlave(m, name, clk, rst, datawidth=32, addrwidth=32,
                 noio=False, nodataflow=False):
    return AxiSlave(m, name, clk, rst, datawidth=datawidth, addrwidth=addrwidth,
                    lite=True, noio=noio, nodataflow=nodataflow)


class AxiMemoryModel(object):
    __intrinsics__ = ('read', 'write')

    burst_size_width = 8

    def __init__(self, m, name, clk, rst,
                 datawidth=32, addrwidth=32,
                 mem_datawidth=32, mem_addrwidth=20,
                 memimg=None, write_delay=10, read_delay=10, sleep=4):

        if mem_datawidth % 8 != 0:
            raise ValueError('mem_datawidth must be a multiple of 8')

        self.m = m
        self.name = name
        self.clk = clk
        self.rst = rst
        self.datawidth = datawidth
        self.addrwidth = addrwidth
        self.mem_datawidth = mem_datawidth
        self.mem_addrwidth = mem_addrwidth

        itype = util.t_Reg
        otype = util.t_Wire

        self.waddr = AxiSlaveWriteAddress(
            m, name, datawidth, addrwidth, itype=itype, otype=otype)
        self.wdata = AxiSlaveWriteData(
            m, name, datawidth, addrwidth, itype=itype, otype=otype)
        self.raddr = AxiSlaveReadAddress(
            m, name, datawidth, addrwidth, itype=itype, otype=otype)
        self.rdata = AxiSlaveReadData(
            m, name, datawidth, addrwidth, itype=itype, otype=otype)

        self.mem = self.m.Reg(
            '_'.join(['', self.name, 'mem']), 8, vtypes.Int(2) ** self.mem_addrwidth)

        if memimg is None:
            filename = '_'.join(['', self.name, 'memimg', '.out'])
            size = 2 ** self.mem_addrwidth
            wordsize = self.mem_datawidth // 8
            self._make_img(filename, size, wordsize)

        elif isinstance(memimg, str):
            filename = memimg

        else:
            filename = '_'.join(['', self.name, 'memimg', '.out'])
            to_memory_image(filename, memimg, datawidth=mem_datawidth)

        self.m.Initial(
            vtypes.Systask('readmemh', filename, self.mem)
        )

        self.fsm = FSM(self.m, '_'.join(['', self.name, 'fsm']), clk, rst)

        self._make_fsm(write_delay, read_delay, sleep)

    @staticmethod
    def _make_img(filename, size, wordsize):
        with open(filename, 'w') as f:
            for i in range(int(size // wordsize)):
                s = (''.join(['%0', '%d' % (wordsize * 2), 'x'])) % i
                for w in range(wordsize * 2, 0, -2):
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
        awaddr = ports['_'.join([name, 'awaddr'])]
        if '_'.join([name, 'awlen']) in ports:
            awlen = ports['_'.join([name, 'awlen'])]
        else:
            awlen = vtypes.Int(0)
        awvalid = ports['_'.join([name, 'awvalid'])]
        awready = ports['_'.join([name, 'awready'])]

        self.waddr.awaddr.connect(awaddr)
        self.waddr.awlen.connect(awlen)
        self.waddr.awvalid.connect(awvalid)
        awready.connect(self.waddr.awready)

        wdata = ports['_'.join([name, 'wdata'])]
        wstrb = ports['_'.join([name, 'wstrb'])]
        if '_'.join([name, 'wlast']) in ports:
            wlast = ports['_'.join([name, 'wlast'])]
        else:
            wlast = vtypes.Int(1)
        wvalid = ports['_'.join([name, 'wvalid'])]
        wready = ports['_'.join([name, 'wready'])]

        self.wdata.wdata.connect(wdata)
        self.wdata.wstrb.connect(wstrb)
        self.wdata.wlast.connect(wlast)
        self.wdata.wvalid.connect(wvalid)
        wready.connect(self.wdata.wready)

        araddr = ports['_'.join([name, 'araddr'])]
        if '_'.join([name, 'arlen']) in ports:
            arlen = ports['_'.join([name, 'arlen'])]
        else:
            arlen = vtypes.Int(0)
        arvalid = ports['_'.join([name, 'arvalid'])]
        arready = ports['_'.join([name, 'arready'])]

        self.raddr.araddr.connect(araddr)
        self.raddr.arlen.connect(arlen)
        self.raddr.arvalid.connect(arvalid)
        arready.connect(self.raddr.arready)

        rdata = ports['_'.join([name, 'rdata'])]
        if '_'.join([name, 'rlast']) in ports:
            rlast = ports['_'.join([name, 'rlast'])]
        rvalid = ports['_'.join([name, 'rvalid'])]
        rready = ports['_'.join([name, 'rready'])]

        self.m.Always()(rdata(self.rdata.rdata, blk=True))
        if '_'.join([name, 'rlast']) in ports:
            rlast.connect(self.rdata.rlast)
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


def make_memory_image(filename, length, pattern='inc', dtype=None,
                      datawidth=32, wordwidth=8, endian='little'):

    import numpy as np

    if dtype is None:
        dtype = np.int32

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


def aligned_shape(shape, wordsize, mem_wordsize):
    aligned_shape = shape[:]

    if wordsize == mem_wordsize or wordsize > mem_wordsize:
        return aligned_shape

    chunk = mem_wordsize // wordsize
    res = mem_wordsize - aligned_shape[-1] % chunk

    if res == mem_wordsize:
        return aligned_shape

    aligned_shape[-1] += res
    return aligned_shape


def shape_to_length(shape):
    return functools.reduce(lambda x, y: x * y, shape, 1)


def memory_word_length(shape, wordsize, block_size=4096):
    length = shape_to_length(shape)
    return ((block_size // wordsize) *
            int(math.ceil(length / (block_size // wordsize))))


def set_memory(mem, src, mem_wordsize, src_wordsize, mem_offset):
    if mem_wordsize < src_wordsize:
        return _set_memory_narrow(mem, src, mem_wordsize, src_wordsize, mem_offset)

    return _set_memory_wide(mem, src, mem_wordsize, src_wordsize, mem_offset)


def _set_memory_wide(mem, src, mem_wordsize, src_wordsize, mem_offset):

    if mem_wordsize > 8:
        raise ValueError('not supported')

    import numpy as np

    src_aligned_shape = aligned_shape(src.shape, src_wordsize, mem_wordsize)
    num_pack = int(math.ceil(mem_wordsize / src_wordsize))

    src_mask = np.uint64(2 ** (8 * src_wordsize) - 1)
    mem_mask = np.uint64(2 ** (8 * mem_wordsize) - 1)
    offset = mem_offset // mem_wordsize
    pack = 0
    index = 0

    for data in src.reshape([-1]):
        v = np.uint64(data) & src_mask
        shift = np.uint64(8 * src_wordsize * pack)
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


def _set_memory_narrow(mem, src, mem_wordsize, src_wordsize, mem_offset):

    if mem_wordsize > 8:
        raise ValueError('not supported')

    import numpy as np

    src_aligned_shape = aligned_shape(src.shape, src_wordsize, mem_wordsize)
    num_pack = int(math.ceil(src_wordsize / mem_wordsize))

    src_mask = np.uint64(2 ** (8 * src_wordsize) - 1)
    mem_mask = np.uint64(2 ** (8 * mem_wordsize) - 1)
    offset = mem_offset // mem_wordsize

    for data in src.reshape([-1]):
        for pack in range(num_pack):
            v = np.uint64(data)
            shift = np.uint64(8 * mem_wordsize * pack)
            v = v >> shift
            v = v & mem_mask
            mem[offset] = v
            offset += 1
