from __future__ import absolute_import
from __future__ import print_function

import veriloggen.core.vtypes as vtypes
import veriloggen.core.module as module
from veriloggen.seq.seq import Seq

class FifoWriteInterface(object):
    _I = 'Reg'
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
        name_almost_full = p_almost_full if name is None else '_'.join([name, p_almost_full])
    
        if itype == 'Reg' or itype == 'OutputReg':
            self.enq = getattr(m, itype)(name_enq, initval=0)
            self.wdata = getattr(m, itype)(name_wdata, datawidth, initval=0)
        else:
            self.enq = getattr(m, itype)(name_enq)
            self.wdata = getattr(m, itype)(name_wdata, datawidth)

        if otype == 'Reg' or otype == 'OutputReg':
            self.full = getattr(m, otype)(name_full, initval=0)
            self.almost_full = getattr(m, otype)(name_almost_full, initval=0)
        else:
            self.full = getattr(m, otype)(name_full)
            self.almost_full = getattr(m, otype)(name_almost_full)

    def connect(self, targ):
        self._connect_port(self.enq, targ.enq)
        self._connect_port(self.wdata, targ.wdata)
        self._connect_port(targ.full, self.full)
        self._connect_port(targ.almost_full, self.almost_full)

    def _connect_port(self, left, right):
        if isinstance(left, vtypes.Reg):
            left.module.Always()( left(right, blk=True) )
        else:
            left.assign(right)

class FifoReadInterface(object):
    _I = 'Reg'
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
        name_almost_empty = p_almost_empty if name is None else '_'.join([name, p_almost_empty])
    
        if itype == 'Reg' or itype == 'OutputReg':
            self.deq = getattr(m, itype)(name_deq, initval=0)
        else:
            self.deq = getattr(m, itype)(name_deq)

        if otype == 'Reg' or otype == 'OutputReg':
            self.rdata = getattr(m, otype)(name_rdata, datawidth, initval=0)
            self.empty = getattr(m, otype)(name_empty, initval=0)
            self.almost_empty = getattr(m, otype)(name_almost_empty, initval=0)
        else:
            self.rdata = getattr(m, otype)(name_rdata, datawidth)
            self.empty = getattr(m, otype)(name_empty)
            self.almost_empty = getattr(m, otype)(name_almost_empty)

    def connect(self, targ):
        self._connect_port(self.deq, targ.deq)
        self._connect_port(targ.rdata, self.rdata)
        self._connect_port(targ.empty, self.empty)
        self._connect_port(targ.almost_empty, self.almost_empty)

    def _connect_port(self, left, right):
        if isinstance(left, vtypes.Reg):
            left.module.Always()( left(right, blk=True) )
        else:
            left.assign(right)

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

#-------------------------------------------------------------------------------
def mkFifoDefinition(name, datawidth=32, addrwidth=4):
    m = module.Module(name)
    clk = m.Input('CLK')
    rst = m.Input('RST')

    wif = FifoWriteSlaveInterface(m, name, datawidth)
    rif = FifoReadSlaveInterface(m, name, datawidth)

    mem = m.Reg('mem', datawidth, length=2**addrwidth)
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

    rdata = m.Reg('rdata_reg', datawidth, initval=0)

    wif.full.assign(is_full)
    wif.almost_full.assign(is_almost_full)
    rif.empty.assign(is_empty)
    rif.almost_empty.assign(is_almost_empty)

    seq = Seq(m, '', clk, rst)
    
    seq.If(vtypes.Ands(wif.enq, vtypes.Not(is_full)))(
        mem[head](wif.wdata),
        head.inc()
    )

    seq.If(vtypes.Ands(rif.deq, vtypes.Not(is_empty)))(
        rdata(mem[tail]),
        tail.inc()
    )

    rif.rdata.assign(rdata)

    seq.make_always()

    return m

#-------------------------------------------------------------------------------
class Fifo(object):
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

        # entry counter
        self._max_size = (2 ** self.addrwidth if isinstance(self.addrwidth, int) else
                          vtypes.Int(2) ** self.addrwidth)
        
        self._count = self.m.Reg('count_' + name, self.addrwidth + 1, initval=0)
        self._count_seq = Seq(self.m, 'seq_count_' + name, self.clk, self.rst)
        
        self._count_seq.If(
            vtypes.Ands(vtypes.Ands(self.wif.enq, vtypes.Not(self.wif.full)),
                        vtypes.Ands(self.rif.deq, vtypes.Not(self.rif.empty))))(
            self._count(self._count)
        ).Elif(vtypes.Ands(self.wif.enq, vtypes.Not(self.wif.full)))(
            self._count.inc()
        ).Elif(vtypes.Ands(self.rif.deq, vtypes.Not(self.rif.empty)))(
            self._count.dec()
        )
        self._count_seq.make_always()

    def enq(self, mng, wdata, cond=None, delay=0):
        """ Enque operation with Seq or FSM object as mng """
        if cond is not None:
            mng.If(cond)

        not_full = vtypes.Not(self.wif.full)
        ack = vtypes.Ands(not_full, self.wif.enq)
        ready = vtypes.Not(self.wif.almost_full)

        current_delay = mng.current_delay
        
        mng.Delay(current_delay + delay)(
            self.wif.wdata(wdata)
        )
        mng.Then().Delay(current_delay + delay)(
            self.wif.enq(1)
        )
        mng.Then().Delay(current_delay + delay + 1)(
            self.wif.enq(0)
        )

        return ack, ready

    def deq(self, mng, rdata=None, rvalid=None, cond=None, delay=0):
        """ Deque operation with Seq or FSM object as mng """
        if cond is not None:
            mng.If(cond)

        not_empty = vtypes.Not(self.rif.empty)

        current_delay = mng.current_delay
        
        mng.Delay(current_delay + delay)(
            self.rif.deq(1)
        )
        mng.Then().Delay(current_delay + delay + 1)(
            self.rif.deq(0)
        )

        if rdata is not None:
            mng.Then().Delay(current_delay + delay + 2)(
                rdata(self.rif.rdata)
            )
        else:
            rdata = self.rif.rdata

        if rvalid is not None:
            deq_valid = self.m.TmpReg(initval=0)
            mng.Then().Delay(current_delay + delay + 1)(
                deq_valid(vtypes.Ands(not_empty, self.rif.deq))
            )
            mng.Then().Delay(current_delay + delay + 2)(
                rvalid(deq_valid)
            )
            mng.Then().Delay(current_delay + delay + 3)(
                rvalid(0)
            )
        else:
            rvalid = self.m.TmpReg(initval=0)
            mng.Then().Delay(current_delay + delay + 1)(
                rvalid(vtypes.Ands(not_empty, self.rif.deq))
            )
            mng.Then().Delay(current_delay + delay + 2)(
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
        if num < 1: return True
        return (self._count + num < self._max_size)
