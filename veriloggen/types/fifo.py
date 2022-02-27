from __future__ import absolute_import
from __future__ import print_function

import veriloggen.core.vtypes as vtypes
import veriloggen.core.module as module
from veriloggen.seq.seq import Seq
from . import util


class FifoWriteInterface(object):
    _I = 'Wire'
    _O = 'Wire'

    def __init__(self, m, name=None, datawidth=32, itype=None, otype=None,
                 p_enq='enq', p_wdata='wdata', p_full='full', p_almost_full='almost_full'):

        if itype is None:
            itype = self._I
        if otype is None:
            otype = self._O

        self.m = m

        name_enq = p_enq if name is None else '_'.join([name, p_enq])
        name_wdata = p_wdata if name is None else '_'.join([name, p_wdata])
        name_full = p_full if name is None else '_'.join([name, p_full])
        name_almost_full = p_almost_full if name is None else '_'.join(
            [name, p_almost_full])

        self.enq = util.make_port(m, itype, name_enq, initval=0)
        self.wdata = util.make_port(m, itype, name_wdata, datawidth, initval=0)
        self.full = util.make_port(m, otype, name_full, initval=0)
        self.almost_full = util.make_port(
            m, otype, name_almost_full, initval=0)

    def connect(self, targ):
        self.enq.connect(targ.enq)
        self.wdata.connect(targ.wdata)
        targ.full.connect(self.full)
        targ.almost_full.connect(self.almost_full)


class FifoReadInterface(object):
    _I = 'Wire'
    _O = 'Wire'

    def __init__(self, m, name=None, datawidth=32, itype=None, otype=None,
                 p_deq='deq', p_rdata='rdata', p_empty='empty', p_almost_empty='almost_empty'):

        if itype is None:
            itype = self._I
        if otype is None:
            otype = self._O

        self.m = m

        name_deq = p_deq if name is None else '_'.join([name, p_deq])
        name_rdata = p_rdata if name is None else '_'.join([name, p_rdata])
        name_empty = p_empty if name is None else '_'.join([name, p_empty])
        name_almost_empty = p_almost_empty if name is None else '_'.join(
            [name, p_almost_empty])

        self.deq = util.make_port(m, itype, name_deq, initval=0)
        self.rdata = util.make_port(m, otype, name_rdata, datawidth, initval=0)
        self.empty = util.make_port(m, otype, name_empty, initval=0)
        self.almost_empty = util.make_port(
            m, otype, name_almost_empty, initval=0)

    def connect(self, targ):
        self.deq.connect(targ.deq)
        targ.rdata.connect(self.rdata)
        targ.empty.connect(self.empty)
        targ.almost_empty.connect(self.almost_empty)


class FifoWriteSlaveInterface(FifoWriteInterface):
    _I = 'Input'
    _O = 'Output'


class FifoWriteMasterInterface(FifoWriteInterface):
    _I = 'Output'
    _O = 'Input'


class FifoReadSlaveInterface(FifoReadInterface):
    _I = 'Input'
    _O = 'Output'


class FifoReadMasterInterface(FifoReadInterface):
    _I = 'Output'
    _O = 'Input'


# -------------------------------------------------------------------------
def mkFifoDefinition(name, datawidth=32, addrwidth=4,
                     sync=True):
    m = module.Module(name)
    clk = m.Input('CLK')
    rst = m.Input('RST')

    wif = FifoWriteSlaveInterface(m, name, datawidth)
    rif = FifoReadSlaveInterface(m, name, datawidth)

    mem = m.Reg('mem', datawidth, 2**addrwidth)
    head = m.Reg('head', addrwidth, initval=0)
    tail = m.Reg('tail', addrwidth, initval=0)

    is_empty = m.Wire('is_empty')
    is_almost_empty = m.Wire('is_almost_empty')
    is_full = m.Wire('is_full')
    is_almost_full = m.Wire('is_almost_full')

    mask = (2 ** addrwidth) - 1

    is_empty.assign(head == tail)
    is_almost_empty.assign(head == ((tail + 1) & mask))
    is_full.assign(((head + 1) & mask) == tail)
    is_almost_full.assign(((head + 2) & mask) == tail)

    if sync:
        rdata = m.Reg('rdata_reg', datawidth, initval=0)
    else:
        rdata = m.Wire('rdata', datawidth)

    wif.full.assign(is_full)
    wif.almost_full.assign(vtypes.Ors(is_almost_full, is_full))
    rif.empty.assign(is_empty)
    rif.almost_empty.assign(vtypes.Ors(is_almost_empty, is_empty))

    seq = Seq(m, '', clk, rst)

    seq.If(vtypes.Ands(wif.enq, vtypes.Not(is_full)))(
        mem[head](wif.wdata),
        head.inc()
    )

    if sync:
        seq.If(vtypes.Ands(rif.deq, vtypes.Not(is_empty)))(
            rdata(mem[tail]),
            tail.inc()
        )
    else:
        seq.If(vtypes.Ands(rif.deq, vtypes.Not(is_empty)))(
            tail.inc()
        )
        rdata.assign(mem[tail])

    rif.rdata.assign(rdata)

    seq.make_always()

    return m
