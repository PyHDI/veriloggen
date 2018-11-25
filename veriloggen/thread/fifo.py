from __future__ import absolute_import
from __future__ import print_function

import veriloggen.core.vtypes as vtypes
import veriloggen.types.fixed as fxd

from veriloggen.seq.seq import Seq
from veriloggen.types.fifo import FifoReadInterface, FifoWriteInterface, mkFifoDefinition

from .ttypes import _MutexFunction


class FIFO(_MutexFunction):
    __intrinsics__ = ('enq', 'deq', 'try_enq', 'try_deq',
                      'is_empty', 'is_almost_empty',
                      'is_full', 'is_almost_full') + _MutexFunction.__intrinsics__

    def __init__(self, m, name, clk, rst, datawidth=32, addrwidth=4):

        self.m = m
        self.name = name
        self.clk = clk
        self.rst = rst

        self.datawidth = datawidth
        self.addrwidth = addrwidth

        self.wif = FifoWriteInterface(self.m, name, datawidth)
        self.rif = FifoReadInterface(self.m, name, datawidth)

        self.definition = mkFifoDefinition(name, datawidth, addrwidth)

        self.inst = self.m.Instance(self.definition, 'inst_' + name,
                                    ports=m.connect_ports(self.definition))

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

        self._enq_disabled = False
        self._deq_disabled = False

        self.mutex = None

    def disable_enq(self):
        self.seq(
            self.wif.enq(0)
        )
        self._enq_disabled = True

    def disable_deq(self):
        self.seq(
            self.rif.deq(0)
        )
        self._deq_disabled = True

    def enq_rtl(self, wdata, cond=None, delay=0):
        """ Enque """

        if self._enq_disabled:
            raise TypeError('Enq disabled.')

        if cond is not None:
            self.seq.If(cond)

        current_delay = self.seq.current_delay

        not_full = vtypes.Not(self.wif.full)
        ack = vtypes.Ands(not_full, self.wif.enq)
        if current_delay + delay == 0:
            ready = vtypes.Not(self.wif.almost_full)
        else:
            ready = self._count + (current_delay + delay + 1) < self._max_size

        self.seq.Delay(current_delay + delay).EagerVal().If(not_full)(
            self.wif.wdata(wdata)
        )
        self.seq.Then().Delay(current_delay + delay)(
            self.wif.enq(1)
        )

        # de-assert
        self.seq.Delay(current_delay + delay + 1)(
            self.wif.enq(0)
        )

        return ack, ready

    def deq_rtl(self, cond=None, delay=0):
        """ Deque """

        if self._deq_disabled:
            raise TypeError('Deq disabled.')

        if cond is not None:
            self.seq.If(cond)

        not_empty = vtypes.Not(self.rif.empty)

        current_delay = self.seq.current_delay

        self.seq.Delay(current_delay + delay)(
            self.rif.deq(1)
        )

        rdata = self.rif.rdata
        rvalid = self.m.TmpReg(initval=0)

        self.seq.Then().Delay(current_delay + delay + 1)(
            rvalid(vtypes.Ands(not_empty, self.rif.deq))
        )

        # de-assert
        self.seq.Delay(current_delay + delay + 1)(
            self.rif.deq(0)
        )
        self.seq.Delay(current_delay + delay + 2)(
            rvalid(0)
        )

        return rdata, rvalid

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

        rdata, rvalid = self.deq_rtl(cond=cond)
        fsm.If(vtypes.Not(self.empty)).goto_next()
        fsm.goto_next()

        rdata_reg = self.m.TmpReg(self.datawidth, initval=0, signed=True)

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

        rdata, rvalid = self.deq_rtl(cond=cond)
        fsm.goto_next()
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
