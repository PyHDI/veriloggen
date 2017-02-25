from __future__ import absolute_import
from __future__ import print_function

import math

import veriloggen.core.vtypes as vtypes
import veriloggen.types.ram as ram
import veriloggen.types.fifo as fifo
import veriloggen.types.axi as axi
from veriloggen.seq.seq import Seq


class Mutex(object):
    __intrinsics__ = ('lock', 'try_lock', 'unlock')

    def __init__(self, m, name, clk, rst, width=32):

        self.m = m
        self.name = name
        self.clk = clk
        self.rst = rst
        self.width = width

        self.seq = Seq(self.m, self.name, self.clk, self.rst)

        self.lock_reg = self.m.Reg(
            '_'.join(['', self.name, 'lock_reg']), initval=0)
        self.lock_id = self.m.Reg(
            '_'.join(['', self.name, 'lock_id']), self.width, initval=0)

        self.id_map = {}
        self.id_map_count = 0

    def lock(self, fsm):
        name = fsm.name
        new_lock_id = self._get_id(name)

        if new_lock_id > 2 ** self.width - 1:
            raise ValueError('too many lock IDs')

        # try
        try_state = fsm.current
        cond = vtypes.Ors(vtypes.Not(self.lock_reg),
                          self.lock_id == new_lock_id)
        state_cond = fsm.state == fsm.current

        self.seq.If(state_cond, cond)(
            self.lock_reg(1),
            self.lock_id(new_lock_id)
        )

        fsm.If(cond).goto_next()

        # verify
        cond = vtypes.Ands(self.lock_reg, self.lock_id == new_lock_id)
        fsm.If(vtypes.Not(cond)).goto(try_state)  # try again
        fsm.If(cond).goto_next()  # OK

        return 1

    def try_lock(self, fsm):
        name = fsm.name
        new_lock_id = self._get_id(name)

        if new_lock_id > 2 ** self.width - 1:
            raise ValueError('too many lock IDs')

        # try
        try_state = fsm.current
        cond = vtypes.Or(vtypes.Not(self.lock_reg),
                         self.lock_id == new_lock_id)
        state_cond = fsm.state == fsm.current

        self.seq.If(state_cond, cond)(
            self.lock_reg(1),
            self.lock_id(new_lock_id)
        )

        fsm.goto_next()

        # verify
        cond = vtypes.And(self.lock_reg, self.lock_id == new_lock_id)
        result = self.m.TmpReg(initval=0)
        fsm(
            result(cond)
        )
        fsm.goto_next()

        return result

    def unlock(self, fsm):
        name = fsm.name
        new_lock_id = self._get_id(name)

        if new_lock_id > 2 ** self.width - 1:
            raise ValueError('too many lock IDs')

        state_cond = fsm.state == fsm.current

        self.seq.If(state_cond, self.lock_id == new_lock_id)(
            self.lock_reg(0)
        )

        fsm.goto_next()

    def _get_id(self, name):
        if name not in self.id_map:
            self.id_map[name] = self.id_map_count
            self.id_map_count += 1

        return self.id_map[name]


class Shared(object):
    __intrinsics__ = ('read', 'write',
                      'lock', 'try_lock', 'unlock')

    def __init__(self, value):
        self._value = value
        self.seq = None
        self.mutex = None

    @property
    def value(self):
        return self._value

    def read(self, fsm):
        return self._value

    def write(self, fsm, value, *part):
        if self.seq is None:
            self.seq = Seq(fsm.m, '_'.join(
                ['seq', self._value.name]), fsm.clk, fsm.rst)

        cond = fsm.state == fsm.current

        def getval(v, p):
            if isinstance(p, (tuple, list)):
                return v[p[0], p[1]]
            return v[p]

        if len(part) == 0:
            targ = self._value
        elif len(part) == 1:
            targ = getval(self._value, part[0])
        elif len(part) == 2:
            targ = getval(getval(self._value, part[0]), part[1])
        else:
            raise TypeError('unsupported type')

        self.seq.If(cond)(
            targ(value)
        )

        fsm.goto_next()
        return 0

    def lock(self, fsm):
        if self.mutex is None:
            self.mutex = Mutex(self.m, '_'.join(
                ['', self.name, 'mutex']), self.clk, self.rst)

        return self.mutex.lock(fsm)

    def try_lock(self, fsm):
        if self.mutex is None:
            self.mutex = Mutex(self.m, '_'.join(
                ['', self.name, 'mutex']), self.clk, self.rst)

        return self.mutex.try_lock(fsm)

    def unlock(self, fsm):
        if self.mutex is None:
            self.mutex = Mutex(self.m, '_'.join(
                ['', self.name, 'mutex']), self.clk, self.rst)

        return self.mutex.unlock(fsm)


class RAM(ram.SyncRAMManager):
    __intrinsics__ = ('read', 'write', 'dma_read', 'dma_write',
                      'lock', 'try_lock', 'unlock')

    def __init__(self, m, name, clk, rst,
                 datawidth=32, addrwidth=10, numports=1):

        ram.SyncRAMManager.__init__(
            self, m, name, clk, rst, datawidth, addrwidth, numports)

        self.mutex = None

    def read(self, fsm, addr, port=0, unified=False):
        """ intrinsic read operation """

        if unified:
            return self._unified_read(fsm, addr, port)

        return self._shared_read(fsm, addr, port)

    def write(self, fsm, addr, wdata, port=0, unified=False):
        """ intrinsic write operation """

        if unified:
            return self._unified_write(fsm, addr, wdata, port)

        return self._shared_write(fsm, addr, wdata, port)

    def _shared_read(self, fsm, addr, port=0):
        """ intrinsic read operation using a shared Seq object """

        cond = fsm.state == fsm.current

        rdata, rvalid = ram.SyncRAMManager.read(self, port, addr, cond)
        rdata_reg = self.m.TmpReg(self.datawidth, initval=0, signed=True)

        fsm.If(rvalid)(
            rdata_reg(rdata)
        )
        fsm.Then().goto_next()

        return rdata_reg

    def _shared_write(self, fsm, addr, wdata, port=0):
        """ intrinsic write operation using a shared Seq object """

        cond = fsm.state == fsm.current

        ram.SyncRAMManager.write(self, port, addr, wdata, cond)
        fsm.goto_next()

        return 0

    def _unified_read(self, fsm, addr, port=0):
        """ intrinsic read operation using the given FSM object """

        fsm(
            self.interfaces[port].addr(addr)
        )

        for _ in range(2):
            fsm.goto_next()

        rdata = self.m.TmpReg(self.datawidth, initval=0, signed=True)

        fsm(
            rdata(self.interfaces[port].rdata)
        )
        fsm.goto_next()

        return rdata

    def _unified_write(self, fsm, addr, wdata, port=0):
        """ intrinsic write operation using the given FSM object """

        if self._write_disabled[port]:
            raise TypeError('Write disabled.')

        fsm(
            self.interfaces[port].addr(addr),
            self.interfaces[port].wdata(wdata),
            self.interfaces[port].wenable(1)
        )
        fsm.Delay(1)(
            self.interfaces[port].wenable(0)
        )
        fsm.goto_next()

        return 0

    def dma_read(self, fsm, bus, local_addr, global_addr, size, port=0):
        if not isinstance(bus, AXIM):
            raise TypeError('AXIM interface is required')

        return bus.dma_read(fsm, self, local_addr, global_addr, size, port)

    def dma_write(self, fsm, bus, local_addr, global_addr, size, port=0):
        if not isinstance(bus, AXIM):
            raise TypeError('AXIM interface is required')

        return bus.dma_write(fsm, self, local_addr, global_addr, size, port)

    def lock(self, fsm):
        if self.mutex is None:
            self.mutex = Mutex(self.m, '_'.join(
                ['', self.name, 'mutex']), self.clk, self.rst)

        return self.mutex.lock(fsm)

    def try_lock(self, fsm):
        if self.mutex is None:
            self.mutex = Mutex(self.m, '_'.join(
                ['', self.name, 'mutex']), self.clk, self.rst)

        return self.mutex.try_lock(fsm)

    def unlock(self, fsm):
        if self.mutex is None:
            self.mutex = Mutex(self.m, '_'.join(
                ['', self.name, 'mutex']), self.clk, self.rst)

        return self.mutex.unlock(fsm)


class FIFO(fifo.Fifo):
    __intrinsics__ = ('enq', 'deq', 'try_enq', 'try_deq',
                      'is_empty', 'is_almost_empty',
                      'is_full', 'is_almost_full',
                      'lock', 'try_lock', 'unlock')

    def __init__(self, m, name, clk, rst, datawidth=32, addrwidth=4):
        fifo.Fifo.__init__(self, m, name, clk, rst, datawidth, addrwidth)
        self.mutex = None

    def enq(self, fsm, wdata):
        cond = fsm.state == fsm.current

        ack, ready = fifo.Fifo.enq(self, wdata, cond=cond)
        fsm.If(ready).goto_next()

        return 0

    def deq(self, fsm):
        cond = fsm.state == fsm.current

        rdata, rvalid = fifo.Fifo.deq(self, cond=cond)
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

        ack, ready = fifo.Fifo.enq(self, wdata, cond=cond)
        fsm.goto_next()

        ack_reg = self.m.TmpReg(initval=0)
        fsm(
            ack_reg(ack)
        )
        fsm.goto_next()

        return ack_reg

    def try_deq(self, fsm):
        cond = fsm.state == fsm.current

        rdata, rvalid = fifo.Fifo.deq(self, cond=cond)
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

    def lock(self, fsm):
        if self.mutex is None:
            self.mutex = Mutex(self.m, '_'.join(
                ['', self.name, 'mutex']), self.clk, self.rst)

        return self.mutex.lock(fsm)

    def try_lock(self, fsm):
        if self.mutex is None:
            self.mutex = Mutex(self.m, '_'.join(
                ['', self.name, 'mutex']), self.clk, self.rst)

        return self.mutex.try_lock(fsm)

    def unlock(self, fsm):
        if self.mutex is None:
            self.mutex = Mutex(self.m, '_'.join(
                ['', self.name, 'mutex']), self.clk, self.rst)

        return self.mutex.unlock(fsm)


class AXIM(axi.AxiMaster):
    __intrinsics__ = ('dma_read', 'dma_write',
                      'lock', 'try_lock', 'unlock')

    burstlen = 256

    def __init__(self, m, name, clk, rst, datawidth=32, addrwidth=32):
        axi.AxiMaster.__init__(self, m, name, clk, rst, datawidth, addrwidth)
        self.mutex = None

    def dma_read(self, fsm, ram, local_addr, global_addr, size, port=0):
        if not isinstance(ram, RAM):
            raise TypeError('RAM is required')

        req_local_addr = self.m.TmpReg(ram.addrwidth, initval=0)
        req_global_addr = self.m.TmpReg(self.addrwidth, initval=0)
        req_size = self.m.TmpReg(self.addrwidth, initval=0)
        rest_size = self.m.TmpReg(self.addrwidth, initval=0)

        fsm(
            req_local_addr(local_addr),
            req_global_addr(global_addr),
            rest_size(size)
        )
        fsm.goto_next()

        check_state = fsm.current
        fsm.If(rest_size <= self.burstlen)(
            req_size(rest_size),
            rest_size(0)
        ).Else(
            req_size(self.burstlen),
            rest_size(rest_size - self.burstlen)
        )
        fsm.goto_next()

        cond = fsm.state == fsm.current

        done = axi.AxiMaster.dma_read(self, ram, req_global_addr, req_local_addr, req_size,
                                      cond=cond, ram_port=port)

        fsm.If(done)(
            req_local_addr.add(req_size),
            req_global_addr.add(req_size * (self.datawidth // 8))
        )
        fsm.If(done, rest_size > 0).goto(check_state)
        fsm.If(done, rest_size == 0).goto_next()

        return 0

    def dma_write(self, fsm, ram, local_addr, global_addr, size, port=0):
        if not isinstance(ram, RAM):
            raise TypeError('RAM is required')

        req_local_addr = self.m.TmpReg(ram.addrwidth, initval=0)
        req_global_addr = self.m.TmpReg(self.addrwidth, initval=0)
        req_size = self.m.TmpReg(self.addrwidth, initval=0)
        rest_size = self.m.TmpReg(self.addrwidth, initval=0)

        fsm(
            req_local_addr(local_addr),
            req_global_addr(global_addr),
            rest_size(size)
        )
        fsm.goto_next()

        check_state = fsm.current
        fsm.If(rest_size <= self.burstlen)(
            req_size(rest_size),
            rest_size(0)
        ).Else(
            req_size(self.burstlen),
            rest_size(rest_size - self.burstlen)
        )
        fsm.goto_next()

        cond = fsm.state == fsm.current

        done = axi.AxiMaster.dma_write(self, ram, req_global_addr, req_local_addr, req_size,
                                       cond=cond, ram_port=port)

        fsm.If(done)(
            req_local_addr.add(req_size),
            req_global_addr.add(req_size * (self.datawidth // 8))
        )
        fsm.If(done, rest_size > 0).goto(check_state)
        fsm.If(done, rest_size == 0).goto_next()

        return 0

    def lock(self, fsm):
        if self.mutex is None:
            self.mutex = Mutex(self.m, '_'.join(
                ['', self.name, 'mutex']), self.clk, self.rst)

        return self.mutex.lock(fsm)

    def try_lock(self, fsm):
        if self.mutex is None:
            self.mutex = Mutex(self.m, '_'.join(
                ['', self.name, 'mutex']), self.clk, self.rst)

        return self.mutex.try_lock(fsm)

    def unlock(self, fsm):
        if self.mutex is None:
            self.mutex = Mutex(self.m, '_'.join(
                ['', self.name, 'mutex']), self.clk, self.rst)

        return self.mutex.unlock(fsm)


class AXIS(axi.AxiSlave):
    __intrinsics__ = ('lock', 'try_lock', 'unlock')

    def __init__(self, m, name, clk, rst, datawidth=32, addrwidth=32):
        axi.AxiSlave.__init__(self, m, name, clk, rst, datawidth, addrwidth)
        self.mutex = None

    def lock(self, fsm):
        if self.mutex is None:
            self.mutex = Mutex(self.m, '_'.join(
                ['', self.name, 'mutex']), self.clk, self.rst)

        return self.mutex.lock(fsm)

    def try_lock(self, fsm):
        if self.mutex is None:
            self.mutex = Mutex(self.m, '_'.join(
                ['', self.name, 'mutex']), self.clk, self.rst)

        return self.mutex.try_lock(fsm)

    def unlock(self, fsm):
        if self.mutex is None:
            self.mutex = Mutex(self.m, '_'.join(
                ['', self.name, 'mutex']), self.clk, self.rst)

        return self.mutex.unlock(fsm)
