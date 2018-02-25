from __future__ import absolute_import
from __future__ import print_function

import veriloggen.core.vtypes as vtypes
import veriloggen.types.fixed as fxd
from veriloggen.types.fifo import Fifo

from .ttypes import _MutexFunction


class FIFO(Fifo, _MutexFunction):
    __intrinsics__ = ('enq', 'deq', 'try_enq', 'try_deq',
                      'is_empty', 'is_almost_empty',
                      'is_full', 'is_almost_full') + _MutexFunction.__intrinsics__

    def __init__(self, m, name, clk, rst, datawidth=32, addrwidth=4):
        Fifo.__init__(self, m, name, clk, rst, datawidth, addrwidth)
        self.mutex = None

    def enq(self, fsm, wdata):
        cond = fsm.state == fsm.current

        ack, ready = Fifo.enq(self, wdata, cond=cond)
        fsm.If(ready).goto_next()

        return 0

    def deq(self, fsm):
        cond = fsm.state == fsm.current

        rdata, rvalid = Fifo.deq(self, cond=cond)
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

        ack, ready = Fifo.enq(self, wdata, cond=cond)
        fsm.goto_next()

        ack_reg = self.m.TmpReg(initval=0)
        fsm(
            ack_reg(ack)
        )
        fsm.goto_next()

        return ack_reg

    def try_deq(self, fsm):
        cond = fsm.state == fsm.current

        rdata, rvalid = Fifo.deq(self, cond=cond)
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

        return fxd.as_fixed(raw_value, self.point)

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
        return fxd.as_fixed(raw_data, self.point), raw_valid
