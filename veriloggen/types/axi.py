from __future__ import absolute_import
from __future__ import print_function

import veriloggen.core.vtypes as vtypes
from veriloggen.seq.seq import Seq
from veriloggen.fsm.fsm import FSM, TmpFSM
from veriloggen.dataflow.dataflow import DataflowManager
from veriloggen.dataflow.dtypes import make_condition
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


# master interface
class AxiMaster(object):
    burst_size_width = 8

    def __init__(self, m, name, clk, rst, datawidth=32, addrwidth=32,
                 nodataflow=False):

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

        self.write_counters = []
        self.read_counters = []

        if nodataflow:
            self.df = None
        else:
            self.df = DataflowManager(self.m, self.clk, self.rst)

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

        raw_data, raw_valid = data.read(cond=cond)

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

        done = last

        return done

    def read_request(self, addr, length, cond=None, counter=None):
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

        prev_subst = self.rdata.rready._get_subst()
        if not prev_subst:
            self.rdata.rready.assign(val)
        else:
            self.rdata.rready.subst[0].overwrite_right(
                vtypes.Ors(prev_subst[0].right, val))

        ack = vtypes.Ands(self.rdata.rready, self.rdata.rvalid)
        data = self.rdata.rdata
        valid = ack
        last = self.rdata.rlast

        self.seq.If(vtypes.Ands(ack, counter > 0))(
            counter.dec()
        )

        return data, valid, last

    def read_dataflow(self, counter=None, cond=None, point=0, signed=False):
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

        prev_subst = self.rdata.rready._get_subst()
        if not prev_subst:
            self.rdata.rready.assign(val)
        else:
            self.rdata.rready.subst[0].overwrite_right(
                vtypes.Ors(prev_subst[0].right, val))

        ack = vtypes.Ands(self.rdata.rready, self.rdata.rvalid)
        data = self.rdata.rdata
        valid = self.rdata.rvalid
        last = self.rdata.rlast

        self.seq.If(vtypes.Ands(ack, counter > 0))(
            counter.dec()
        )

        df = self.df if self.df is not None else dataflow

        df_data = df.Variable(data, valid, data_ready,
                              point=point, signed=signed)
        df_last = df.Variable(last, valid, last_ready, width=1)
        done = last

        return df_data, df_last, done

    def dma_read(self, ram, bus_addr, ram_addr, length, cond=None, ram_port=0):
        fsm = TmpFSM(self.m, self.clk, self.rst)

        if cond is not None:
            fsm.If(cond).goto_next()

        ack, counter = self.read_request(bus_addr, length, cond=fsm)
        fsm.If(ack).goto_next()

        data, last, done = self.read_dataflow()

        done = ram.write_dataflow(ram_port, ram_addr, data, length, cond=fsm)
        fsm.goto_next()
        fsm.If(done).goto_init()

        return done

    def dma_write(self, ram, bus_addr, ram_addr, length, cond=None, ram_port=0):
        fsm = TmpFSM(self.m, self.clk, self.rst)

        if cond is not None:
            fsm.If(cond).goto_next()

        ack, counter = self.write_request(bus_addr, length, cond=fsm)
        fsm.If(ack).goto_next()

        data, last, done = ram.read_dataflow(
            ram_port, ram_addr, length, cond=fsm)
        fsm.goto_next()

        done = self.write_dataflow(data, counter, cond=fsm)
        fsm.If(done).goto_init()

        return done


class AxiSlave(object):
    burst_size_width = 8

    def __init__(self, m, name, clk, rst, datawidth=32, addrwidth=32,
                 nodataflow=False):

        self.m = m
        self.name = name
        self.clk = clk
        self.rst = rst
        self.datawidth = datawidth
        self.addrwidth = addrwidth

        self.waddr = AxiSlaveWriteAddress(m, name, datawidth, addrwidth)
        self.wdata = AxiSlaveWriteData(m, name, datawidth, addrwidth)
        self.raddr = AxiSlaveReadAddress(m, name, datawidth, addrwidth)
        self.rdata = AxiSlaveReadData(m, name, datawidth, addrwidth)

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
        self.seq(
            self.rdata.rvalid(0),
            self.rdata.rlast(0)
        )
        self._read_disabled = True

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

        val = (vtypes.Not(valid) if ready is None else
               vtypes.Ands(ready, vtypes.Not(valid)))

        prev_subst = self.waddr.awready._get_subst()
        if not prev_subst:
            self.waddr.awready.assign(val)
        else:
            self.waddr.awready.subst[0].overwrite_right(
                vtypes.Ors(prev_subst[0].right, val))

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

        prev_subst = self.wdata.wready._get_subst()
        if not prev_subst:
            self.wdata.wready.assign(val)
        else:
            self.wdata.wready.subst[0].overwrite_right(
                vtypes.Ors(prev_subst[0].right, val))

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

        prev_subst = self.wdata.wready._get_subst()
        if not prev_subst:
            self.wdata.wready.assign(val)
        else:
            self.wdata.wready.subst[0].overwrite_right(
                vtypes.Ors(prev_subst[0].right, val))

        ack = vtypes.Ands(self.wdata.wready, self.wdata.wvalid)
        data = self.wdata.wdata
        mask = self.wdata.wstrb
        valid = self.wdata.wvalid
        last = self.wdata.wlast

        self.seq.If(vtypes.Ands(ack, counter > 0))(
            counter.dec()
        )

        df = self.df if self.df is not None else dataflow

        df_data = df.Variable(data, valid, data_ready)
        df_mask = df.Variable(mask, valid, mask_ready,
                              width=self.datawidth // 4)
        df_last = df.Variable(last, valid, last_ready, width=1)
        done = last

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

        val = (vtypes.Not(valid) if ready is None else
               vtypes.Ands(ready, vtypes.Not(valid)))

        prev_subst = self.raddr.arready._get_subst()
        if not prev_subst:
            self.raddr.arready.assign(val)
        else:
            self.raddr.arready.subst[0].overwrite_right(
                vtypes.Ors(prev_subst[0].right, val))

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

        done = last

        return done


class AxiMemoryModel(object):
    burst_size_width = 8

    def __init__(self, m, name, clk, rst,
                 datawidth=32, addrwidth=32, mem_addrwidth=20,
                 memimg=None, write_delay=10, read_delay=10, sleep=4):

        self.m = m
        self.name = name
        self.clk = clk
        self.rst = rst
        self.datawidth = datawidth
        self.addrwidth = addrwidth
        self.mem_addrwidth = mem_addrwidth

        self.waddr = AxiSlaveWriteAddress(
            m, name, datawidth, addrwidth, itype=util.t_Reg, otype=util.t_Wire)
        self.wdata = AxiSlaveWriteData(
            m, name, datawidth, addrwidth, itype=util.t_Reg, otype=util.t_Wire)
        self.raddr = AxiSlaveReadAddress(
            m, name, datawidth, addrwidth, itype=util.t_Reg, otype=util.t_Wire)
        self.rdata = AxiSlaveReadData(
            m, name, datawidth, addrwidth, itype=util.t_Reg, otype=util.t_Wire)

        self.mem = self.m.Reg(
            '_'.join(['', self.name, 'mem']), 8, vtypes.Int(2) ** self.mem_addrwidth)

        if memimg is None:
            filename = '_'.join(['', self.name, 'memimg', '.out'])
            size = 2 ** self.mem_addrwidth
            wordsize = 4
            self._make_img(filename, size, wordsize)
        else:
            filename = memimg

        self.m.Initial(
            vtypes.Systask('readmemh', filename, self.mem)
        )

        self.fsm = FSM(self.m, '_'.join(['', self.name, 'fsm']), clk, rst)

        self._make_fsm(write_delay, read_delay, sleep)

    @staticmethod
    def _make_img(filename, size, wordsize):
        with open(filename, 'w') as f:
            for i in range(int(size // wordsize)):
                s = '%08x' % i
                f.write('%s\n' % s[6:8])
                f.write('%s\n' % s[4:6])
                f.write('%s\n' % s[2:4])
                f.write('%s\n' % s[0:2])

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
            self.rdata.rdata(self.rdata.rdata),
            self.rdata.rlast(self.rdata.rlast)
        )

        # read complete
        self.fsm.If(self.rdata.rvalid, self.rdata.rready,
                    read_count == 0).goto_init()

    def connect(self, ports, name):
        awaddr = ports['_'.join([name, 'awaddr'])]
        awlen = ports['_'.join([name, 'awlen'])]
        awvalid = ports['_'.join([name, 'awvalid'])]
        awready = ports['_'.join([name, 'awready'])]

        self.waddr.awaddr.assign(awaddr)
        self.waddr.awlen.assign(awlen)
        self.waddr.awvalid.assign(awvalid)
        self.m.Always()(awready(self.waddr.awready))

        wdata = ports['_'.join([name, 'wdata'])]
        wstrb = ports['_'.join([name, 'wstrb'])]
        wlast = ports['_'.join([name, 'wlast'])]
        wvalid = ports['_'.join([name, 'wvalid'])]
        wready = ports['_'.join([name, 'wready'])]

        self.wdata.wdata.assign(wdata)
        self.wdata.wstrb.assign(wstrb)
        self.wdata.wlast.assign(wlast)
        self.wdata.wvalid.assign(wvalid)
        self.m.Always()(wready(self.wdata.wready))

        araddr = ports['_'.join([name, 'araddr'])]
        arlen = ports['_'.join([name, 'arlen'])]
        arvalid = ports['_'.join([name, 'arvalid'])]
        arready = ports['_'.join([name, 'arready'])]

        self.raddr.araddr.assign(araddr)
        self.raddr.arlen.assign(arlen)
        self.raddr.arvalid.assign(arvalid)
        self.m.Always()(arready(self.raddr.arready))

        rdata = ports['_'.join([name, 'rdata'])]
        rlast = ports['_'.join([name, 'rlast'])]
        rvalid = ports['_'.join([name, 'rvalid'])]
        rready = ports['_'.join([name, 'rready'])]

        self.m.Always()(rdata(self.rdata.rdata))
        self.m.Always()(rlast(self.rdata.rlast))
        self.m.Always()(rvalid(self.rdata.rvalid))
        self.rdata.rready.assign(rready)
