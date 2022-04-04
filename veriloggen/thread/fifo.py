from __future__ import absolute_import
from __future__ import print_function

import collections

import veriloggen.core.vtypes as vtypes
import veriloggen.types.util as util
import veriloggen.types.fixed as fxd

from veriloggen.seq.seq import Seq, make_condition
from veriloggen.types.fifo import FifoReadInterface, FifoWriteInterface, mkFifoDefinition

from .ttypes import _MutexFunction


class FIFO(_MutexFunction):
    __intrinsics__ = ('enq', 'deq', 'try_enq', 'try_deq',
                      'is_empty', 'is_almost_empty',
                      'is_full', 'is_almost_full') + _MutexFunction.__intrinsics__

    def __init__(self, m, name, clk, rst, datawidth=32, addrwidth=4, sync=True):

        self.m = m
        self.name = name
        self.clk = clk
        self.rst = rst

        self.datawidth = datawidth
        self.addrwidth = addrwidth
        self.sync = sync

        self.wif = FifoWriteInterface(self.m, name, datawidth, itype='Wire', otype='Wire')
        self.rif = FifoReadInterface(self.m, name, datawidth, itype='Wire', otype='Wire')

        # default values
        self.wif.enq.assign(0)
        self.wif.wdata.assign(vtypes.IntX())
        self.rif.deq.assign(0)

        self.definition = mkFifoDefinition(name, datawidth, addrwidth, sync=sync)

        ports = collections.OrderedDict()
        ports['CLK'] = self.clk
        ports['RST'] = self.rst
        ports.update(m.connect_ports(self.definition))
        self.inst = self.m.Instance(self.definition, 'inst_' + name,
                                    ports=ports)

        self.seq = Seq(m, name, clk, rst)

        # entry counter
        self._max_size = (2 ** self.addrwidth - 1 if isinstance(self.addrwidth, int) else
                          vtypes.Int(2) ** self.addrwidth - 1)

        self._count = self.m.Reg(
            'count_' + name, self.addrwidth + 1, initval=0)

        self.seq.If(
            vtypes.Ands(vtypes.Ands(self.wif.enq, vtypes.Not(self.wif.full)),
                        vtypes.Ands(self.rif.deq, vtypes.Not(self.rif.empty))))(
            self._count(self._count)
        ).Elif(vtypes.Ands(self.wif.enq, vtypes.Not(self.wif.full)))(
            self._count.inc()
        ).Elif(vtypes.Ands(self.rif.deq, vtypes.Not(self.rif.empty)))(
            self._count.dec()
        )

        self.mutex = None

    def _id(self):
        return id(self)

    def enq_rtl(self, wdata, cond=None):
        """ Enque """

        cond = make_condition(cond)
        ready = vtypes.Not(self.wif.almost_full)

        if cond is not None:
            enq_cond = vtypes.Ands(cond, ready)
            enable = cond
        else:
            enq_cond = ready
            enable = vtypes.Int(1, 1)

        util.add_mux(self.wif.wdata, enable, wdata)
        util.add_enable_cond(self.wif.enq, enable, enq_cond)

        ack = self.seq.Prev(ready, 1)

        return ack, ready

    def deq_rtl(self, cond=None):
        """ Deque """

        cond = make_condition(cond)
        ready = vtypes.Not(self.rif.empty)

        if cond is not None:
            deq_cond = vtypes.Ands(cond, ready)
        else:
            deq_cond = ready

        util.add_enable_cond(self.rif.deq, deq_cond, 1)

        data = self.rif.rdata

        if self.sync:
            valid = self.seq.Prev(deq_cond, 1)
        else:
            valid = deq_cond

        return data, valid, ready

    @property
    def wdata(self):
        return self.wif.wdata

    @property
    def empty(self):
        return self.rif.empty

    @property
    def almost_empty(self):
        return self.rif.almost_empty

    @property
    def rdata(self):
        return self.rif.rdata

    @property
    def full(self):
        return self.wif.full

    @property
    def almost_full(self):
        return self.wif.almost_full

    @property
    def count(self):
        return self._count

    @property
    def space(self):
        if isinstance(self._max_size, int):
            return vtypes.Int(self._max_size) - self.count
        return self._max_size - self.count

    def has_space(self, num=1):
        if num < 1:
            return True
        return (self._count + num < self._max_size)

    def enq(self, fsm, wdata):
        cond = fsm.state == fsm.current

        ack, ready = self.enq_rtl(wdata, cond=cond)
        fsm.If(ready).goto_next()

        return 0

    def deq(self, fsm):
        cond = fsm.state == fsm.current

        rdata, rvalid, rready = self.deq_rtl(cond=cond)

        rdata_reg = self.m.TmpReg(self.datawidth, initval=0, signed=True)

        if self.sync:
            fsm.If(rready).goto_next()

        fsm.If(rvalid)(
            rdata_reg(rdata)
        )
        fsm.If(rvalid).goto_next()

        return rdata_reg

    def try_enq(self, fsm, wdata):
        cond = fsm.state == fsm.current

        ack, ready = self.enq_rtl(wdata, cond=cond)
        fsm.goto_next()

        ack_reg = self.m.TmpReg(initval=0)
        fsm(
            ack_reg(ack)
        )
        fsm.goto_next()

        return ack_reg

    def try_deq(self, fsm):
        cond = fsm.state == fsm.current

        rdata, rvalid, rready = self.deq_rtl(cond=cond)

        if self.sync:
            fsm.goto_next()

        rdata_reg = self.m.TmpReg(self.datawidth, initval=0, signed=True)
        rvalid_reg = self.m.TmpReg(initval=0)

        fsm(
            rdata_reg(rdata),
            rvalid_reg(rvalid)
        )
        fsm.goto_next()

        return rdata_reg, rvalid_reg

    def is_almost_empty(self, fsm):
        fsm.goto_next()
        return self.almost_empty

    def is_empty(self, fsm):
        fsm.goto_next()
        return self.empty

    def is_almost_full(self, fsm):
        fsm.goto_next()
        return self.almost_full

    def is_full(self, fsm):
        fsm.goto_next()
        return self.full


class FixedFIFO(FIFO):

    def __init__(self, m, name, clk, rst,
                 datawidth=32, addrwidth=4, point=0):

        FIFO.__init__(self, m, name, clk, rst,
                      datawidth, addrwidth)

        self.point = point

    def enq(self, fsm, wdata, raw=False):
        if raw:
            fixed_wdata = wdata
        else:
            fixed_wdata = fxd.write_adjust(wdata, self.point)

        return FIFO.enq(self, fsm, fixed_wdata)

    def deq(self, fsm, raw=False):
        raw_value = FIFO.deq(self, fsm)
        if raw:
            return raw_value

        return fxd.reinterpret_cast_to_fixed(raw_value, self.point)

    def try_enq(self, fsm, wdata, raw=False):
        if raw:
            fixed_wdata = wdata
        else:
            fixed_wdata = fxd.write_adjust(wdata, self.point)

        return FIFO.try_enq(self, fsm, fixed_wdata)

    def try_deq(self, fsm, raw=False):
        raw_data, raw_valid = FIFO.try_deq(self, fsm)
        if raw:
            return raw_data, raw_valid
        return fxd.reinterpret_cast_to_fixed(raw_data, self.point), raw_valid
