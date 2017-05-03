from __future__ import absolute_import
from __future__ import print_function

import math

import veriloggen.core.vtypes as vtypes
import veriloggen.types.ram as ram
import veriloggen.types.fifo as fifo
import veriloggen.types.axi as axi
import veriloggen.types.uart as uart
import veriloggen.types.util as util
import veriloggen.types.fixed as fxd
from veriloggen.seq.seq import Seq
from veriloggen.fsm.fsm import FSM

from . import compiler


def Lock(m, name, clk, rst, width=32):
    """ alias of Mutex class """
    return Mutex(m, name, clk, rst, width)


class Mutex(object):
    __intrinsics__ = ('lock', 'try_lock', 'unlock',
                      'acquire', 'release')

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

        state_cond = fsm.state == fsm.current
        try_cond = vtypes.Not(self.lock_reg)
        fsm_cond = vtypes.Ors(try_cond, self.lock_id == new_lock_id)

        self.seq.If(state_cond, try_cond)(
            self.lock_reg(1),
            self.lock_id(new_lock_id)
        )

        fsm.If(fsm_cond).goto_next()

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

        state_cond = fsm.state == fsm.current
        try_cond = vtypes.Not(self.lock_reg)

        self.seq.If(state_cond, try_cond)(
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

        return 0

    def _get_id(self, name):
        if name not in self.id_map:
            self.id_map[name] = self.id_map_count
            self.id_map_count += 1

        return self.id_map[name]

    def acquire(self, fsm, blocking=True):
        """ alias of lock() """

        if not isinstance(blocking, (bool, int)):
            raise TypeError('blocking argument must be bool')

        if blocking:
            return self.lock(fsm)

        return self.try_lock(fsm)

    def release(self, fsm):
        """ alias of unlock() """

        return self.unlock(fsm)


class _MutexFunction(object):
    __intrinsics__ = ('lock', 'try_lock', 'unlock')

    def _check_mutex(self, fsm):
        if self.mutex is None:
            self.mutex = Mutex(self.m, '_'.join(
                ['', self.name, 'mutex']), self.clk, self.rst)

    def lock(self, fsm):
        self._check_mutex(fsm)
        return self.mutex.lock(fsm)

    def try_lock(self, fsm):
        self._check_mutex(fsm)
        return self.mutex.try_lock(fsm)

    def unlock(self, fsm):
        self._check_mutex(fsm)
        return self.mutex.unlock(fsm)


class Barrier(object):
    __intrinsics__ = ('wait', )

    def __init__(self, m, name, clk, rst, numparties):

        self.m = m
        self.name = name
        self.clk = clk
        self.rst = rst
        self.numparties = numparties
        self.width = int(math.ceil(math.log(self.numparties, 2))) + 1

        self.seq = Seq(self.m, self.name, self.clk, self.rst)

        self.count = self.m.Reg(
            '_'.join(['', self.name, 'barrier_count']), self.width, initval=0)
        self.done = self.m.Reg(
            '_'.join(['', self.name, 'barrier_done']), initval=0)
        self.mutex = Mutex(self.m, '_'.join(
            ['', self.name, 'barrier_mutex']), self.clk, self.rst)

        # reset condition
        self.seq(
            self.done(0)
        )
        self.seq.If(self.count == self.numparties)(
            self.count(0),
            self.done(1)
        )

    def wait(self, fsm):

        self.mutex.lock(fsm)

        state_cond = fsm.state == fsm.current
        self.seq.If(state_cond)(
            self.count.inc()
        )
        fsm.goto_next()

        self.mutex.unlock(fsm)

        fsm.If(self.done).goto_next()

        return 0


class Shared(_MutexFunction):
    __intrinsics__ = ('read', 'write') + _MutexFunction.__intrinsics__

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
            m = fsm.m
            clk = fsm.clk
            rst = fsm.rst
            name = self._value.name
            self.seq = Seq(m, '_'.join(['seq', name]), clk, rst)

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

    def _check_mutex(self, fsm):
        if self.mutex is None:
            m = fsm.m
            clk = fsm.clk
            rst = fsm.rst
            name = self._value.name
            self.mutex = Mutex(m, '_'.join(['', name, 'mutex']), clk, rst)


class RAM(ram.SyncRAMManager, _MutexFunction):
    __intrinsics__ = ('read', 'write', 'dma_read',
                      'dma_write') + _MutexFunction.__intrinsics__

    def __init__(self, m, name, clk, rst,
                 datawidth=32, addrwidth=10, numports=1):

        ram.SyncRAMManager.__init__(
            self, m, name, clk, rst, datawidth, addrwidth, numports)

        self.mutex = None

    def connect_rtl(self, port, addr, wdata=None, wenable=None, rdata=None):
        """ connect native signals to the internal RAM interface """

        self.interfaces[port].addr.connect(addr)
        if wdata is not None:
            self.interfaces[port].wdata.connect(wdata)
        if wenable is not None:
            self.interfaces[port].wenable.connect(wenable)
        if rdata is not None:
            rdata.connect(self.interfaces[port].rdata)

    def read_rtl(self, addr, port=0, cond=None):
        """
        @return data, valid
        """
        return ram.SyncRAMManager.read(self, port, addr, cond)

    def write_rtl(self, addr, data, port=0, cond=None):
        """
        @return None
        """
        return ram.SyncRAMManager.write(self, port, addr, data, cond)

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


class FixedRAM(RAM):

    def __init__(self, m, name, clk, rst,
                 datawidth=32, addrwidth=10, numports=1, point=0):

        RAM.__init__(self, m, name, clk, rst,
                     datawidth, addrwidth, numports)

        self.point = point

    def read(self, fsm, addr, port=0, unified=False, raw=False):
        raw_value = RAM.read(self, fsm, addr, port, unified)
        if raw:
            return raw_value
        return fxd.as_fixed(raw_value, self.point)

    def write(self, fsm, addr, wdata, port=0, unified=False, raw=False):
        if raw:
            fixed_wdata = wdata
        else:
            fixed_wdata = fxd.write_adjust(wdata, self.point)

        return RAM.write(self, fsm, addr, fixed_wdata, port, unified)


class FIFO(fifo.Fifo, _MutexFunction):
    __intrinsics__ = ('enq', 'deq', 'try_enq', 'try_deq',
                      'is_empty', 'is_almost_empty',
                      'is_full', 'is_almost_full') + _MutexFunction.__intrinsics__

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


class AXIM(axi.AxiMaster, _MutexFunction):
    __intrinsics__ = ('read', 'write', 'dma_read',
                      'dma_write') + _MutexFunction.__intrinsics__

    burstlen = 256

    def __init__(self, m, name, clk, rst, datawidth=32, addrwidth=32,
                 lite=False, noio=False):
        axi.AxiMaster.__init__(self, m, name, clk, rst, datawidth, addrwidth,
                               lite=lite, noio=noio)
        self.mutex = None

    def read(self, fsm, global_addr):
        ret = self.read_request(global_addr, length=1, cond=fsm)
        if isinstance(ret, (tuple)):
            ack, counter = ret
        else:
            ack = ret
        fsm.If(ack).goto_next()

        ret = self.read_data(cond=fsm)
        if len(ret) == 3:
            data, valid, last = ret
        else:
            data, valid = ret

        rdata = self.m.TmpReg(self.datawidth, initval=0)
        fsm.If(valid)(rdata(data))
        fsm.Then().goto_next()

        return rdata

    def write(self, fsm, global_addr, value):
        ret = self.write_request(global_addr, length=1, cond=fsm)
        if isinstance(ret, (tuple)):
            ack, counter = ret
        else:
            ack = ret
        fsm.If(ack).goto_next()

        ret = self.write_data(value, cond=fsm)
        if isinstance(ret, (tuple)):
            ack, last = ret
        else:
            ack, last = ret, None

        fsm.If(ack).goto_next()

    def dma_read(self, fsm, ram, local_addr, global_addr, size, port=0):
        if self.lite:
            raise TypeError('Lite-interface does not support DMA')

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
            req_global_addr.add(compiler.optimize(
                req_size * (self.datawidth // 8)))
        )
        fsm.If(done, rest_size > 0).goto(check_state)
        fsm.If(done, rest_size == 0).goto_next()

        return 0

    def dma_write(self, fsm, ram, local_addr, global_addr, size, port=0):
        if self.lite:
            raise TypeError('Lite-interface does not support DMA')

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
            req_global_addr.add(compiler.optimize(
                req_size * (self.datawidth // 8)))
        )
        fsm.If(done, rest_size > 0).goto(check_state)
        fsm.If(done, rest_size == 0).goto_next()

        return 0


class AXIS(axi.AxiSlave, _MutexFunction):
    __intrinsics__ = _MutexFunction.__intrinsics__

    def __init__(self, m, name, clk, rst, datawidth=32, addrwidth=32,
                 lite=False, noio=False):
        axi.AxiSlave.__init__(self, m, name, clk, rst, datawidth, addrwidth,
                              lite=lite, noio=noio)
        self.mutex = None


class AXISRegister(AXIS, _MutexFunction):
    __intrinsics__ = ('read', 'write', 'write_flag', 'wait',
                      'wait_flag') + _MutexFunction.__intrinsics__

    def __init__(self, m, name, clk, rst, datawidth=32, addrwidth=32,
                 lite=False, noio=False, length=4):
        AXIS.__init__(self, m, name, clk, rst, datawidth=datawidth, addrwidth=addrwidth,
                      lite=lite, noio=noio)

        if not isinstance(length, int):
            raise TypeError("length must be 'int', not '%s'" %
                            str(type(length)))

        self.register = [self.m.Reg('_'.join(['', self.name, 'register', '%d' % i]),
                                    width=self.datawidth, initval=0)
                         for i in range(length)]
        self.flag = [self.m.Reg('_'.join(['', self.name, 'flag', '%d' % i]), initval=0)
                     for i in range(length)]
        self.resetval = [self.m.Reg('_'.join(['', self.name, 'resetval', '%d' % i]),
                                    width=self.datawidth, initval=0)
                         for i in range(length)]
        self.length = length
        self.maskwidth = self.m.Localparam('_'.join(['', self.name, 'maskwidth']),
                                           int(math.ceil(math.log(length, 2))))
        self.mask = self.m.Localparam('_'.join(['', self.name, 'mask']),
                                      vtypes.Repeat(vtypes.Int(1, 1), self.maskwidth))
        self.shift = self.m.Localparam('_'.join(['', self.name, 'shift']),
                                       util.log2(self.datawidth // 8))

        if self.lite:
            self._setup_register_lite_fsm()
        else:
            self._setup_register_full_fsm()

    def _setup_register_lite_fsm(self):
        fsm = FSM(self.m, '_'.join(
            ['', self.name, 'register_fsm']), self.clk, self.rst)

        # request
        addr, readvalid, writevalid = self.pull_request(cond=fsm)

        maskaddr = self.m.TmpReg(self.maskwidth)
        fsm.If(vtypes.Ors(readvalid, writevalid))(
            maskaddr((addr >> self.shift) & self.mask),
        )

        init_state = fsm.current

        # read
        read_state = fsm.current + 1
        fsm.If(readvalid).goto_from(init_state, read_state)
        fsm.set_index(read_state)

        rdata = self.m.TmpWire(self.datawidth)
        pat = [(maskaddr == i, r) for i, r in enumerate(self.register)]
        pat.append((None, vtypes.IntX()))
        rval = vtypes.PatternMux(pat)
        rdata.assign(rval)

        flag = self.m.TmpWire()
        pat = [(maskaddr == i, r) for i, r in enumerate(self.flag)]
        pat.append((None, vtypes.IntX()))
        rval = vtypes.PatternMux(pat)
        flag.assign(rval)

        resetval = self.m.TmpWire(self.datawidth)
        pat = [(maskaddr == i, r) for i, r in enumerate(self.resetval)]
        pat.append((None, vtypes.IntX()))
        rval = vtypes.PatternMux(pat)
        resetval.assign(rval)

        ack = self.push_read_data(rdata, cond=fsm)

        # flag reset
        state_cond = fsm.state == fsm.current
        for i, r in enumerate(self.register):
            self.seq.If(state_cond, ack, flag, maskaddr == i)(
                self.register[i](resetval),
                self.flag[i](0)
            )

        fsm.If(ack).goto_init()

        # write
        write_state = fsm.current + 1
        fsm.If(writevalid).goto_from(init_state, write_state)
        fsm.set_index(write_state)

        data, mask, valid = self.pull_write_data(cond=fsm)

        state_cond = fsm.state == fsm.current
        for i, r in enumerate(self.register):
            self.seq.If(state_cond, valid, maskaddr == i)(
                self.register[i](data)
            )
        fsm.goto_init()

    def _setup_register_full_fsm(self):
        fsm = FSM(self.m, '_'.join(
            ['', self.name, 'register_fsm']), self.clk, self.rst)

        # request
        addr, counter, readvalid, writevalid = self.pull_request(cond=fsm)

        maskaddr = self.m.TmpReg(self.maskwidth)
        fsm.If(vtypes.Ors(readvalid, writevalid))(
            maskaddr((addr >> self.shift) & self.mask),
        )

        init_state = fsm.current

        # read
        read_state = fsm.current + 1
        fsm.If(readvalid).goto_from(init_state, read_state)
        fsm.set_index(read_state)

        rdata = self.m.TmpWire(self.datawidth)
        pat = [(maskaddr == i, r) for i, r in enumerate(self.register)]
        pat.append((None, vtypes.IntX()))
        rval = vtypes.PatternMux(pat)
        rdata.assign(rval)

        flag = self.m.TmpWire()
        pat = [(maskaddr == i, r) for i, r in enumerate(self.flag)]
        pat.append((None, vtypes.IntX()))
        rval = vtypes.PatternMux(pat)
        flag.assign(rval)

        resetval = self.m.TmpWire(self.datawidth)
        pat = [(maskaddr == i, r) for i, r in enumerate(self.resetval)]
        pat.append((None, vtypes.IntX()))
        rval = vtypes.PatternMux(pat)
        resetval.assign(rval)

        ack, last = self.push_read_data(rdata, counter, cond=fsm)

        # flag reset
        state_cond = fsm.state == fsm.current
        for i, r in enumerate(self.register):
            self.seq.If(state_cond, ack, flag, maskaddr == i)(
                self.register[i](resetval),
                self.flag[i](0)
            )

        fsm.If(ack)(
            maskaddr.inc()
        )
        fsm.If(ack, last).goto_init()

        # write
        write_state = fsm.current + 1
        fsm.If(writevalid).goto_from(init_state, write_state)
        fsm.set_index(write_state)

        data, mask, valid, last = self.pull_write_data(counter, cond=fsm)

        state_cond = fsm.state == fsm.current
        for i, r in enumerate(self.register):
            self.seq.If(state_cond, valid, maskaddr == i)(
                self.register[i](data)
            )
        fsm.If(valid)(
            maskaddr.inc()
        )
        fsm.goto_init()

    def read(self, fsm, addr):
        if isinstance(addr, int):
            rval = self.register[addr]
        elif isinstance(addr, vtypes.Int):
            rval = self.register[addr.value]
        else:
            pat = [(addr == i, r) for i, r in enumerate(self.register)]
            pat.append((None, vtypes.IntX()))
            rval = vtypes.PatternMux(pat)
        return rval

    def write(self, fsm, addr, value):
        state_cond = fsm.state == fsm.current
        for i, r in enumerate(self.register):
            self.seq.If(state_cond, addr == i)(
                self.register[i](value),
                self.flag[i](0)
            )
        fsm.goto_next()

    def write_flag(self, fsm, addr, value, resetvalue=0):
        state_cond = fsm.state == fsm.current
        for i, r in enumerate(self.register):
            self.seq.If(state_cond, addr == i)(
                self.register[i](value),
                self.flag[i](1),
                self.resetval[i](resetvalue)
            )
        fsm.goto_next()

    def wait(self, fsm, addr, value, polarity=True):
        if isinstance(addr, int):
            rval = self.register[addr]
        elif isinstance(addr, vtypes.Int):
            rval = self.register[addr.value]
        else:
            pat = [(addr == i, r) for i, r in enumerate(self.register)]
            pat.append((None, vtypes.IntX()))
            rval = vtypes.PatternMux(pat)

        if polarity:
            wait_cond = (rval == value)
        else:
            wait_cond = (rval != value)

        fsm.If(wait_cond).goto_next()

    def wait_flag(self, fsm, addr, value, resetvalue=0, polarity=True):
        if isinstance(addr, int):
            rval = self.register[addr]
        elif isinstance(addr, vtypes.Int):
            rval = self.register[addr.value]
        else:
            pat = [(addr == i, r) for i, r in enumerate(self.register)]
            pat.append((None, vtypes.IntX()))
            rval = vtypes.PatternMux(pat)

        if polarity:
            wait_cond = (rval == value)
        else:
            wait_cond = (rval != value)

        state_cond = fsm.state == fsm.current

        # flag reset
        for i, r in enumerate(self.register):
            self.seq.If(wait_cond, state_cond, addr == i)(
                self.register[i](resetvalue)
            )

        fsm.If(wait_cond).goto_next()


def AXIMLite(m, name, clk, rst, datawidth=32, addrwidth=32,
             noio=False):

    return AXIM(m, name, clk, rst, datawidth=datawidth, addrwidth=addrwidth,
                lite=True, noio=noio)


def AXISLite(m, name, clk, rst, datawidth=32, addrwidth=32,
             noio=False):

    return AXIS(m, name, clk, rst, datawidth=datawidth, addrwidth=addrwidth,
                lite=True, noio=noio)


def AXISLiteRegister(m, name, clk, rst, datawidth=32, addrwidth=32,
                     noio=False, length=4):

    return AXISRegister(m, name, clk, rst, datawidth=datawidth, addrwidth=addrwidth,
                        lite=True, noio=noio, length=length)


class UartTx(uart.UartTx, _MutexFunction):
    __intrinsics__ = ('send',) + _MutexFunction.__intrinsics__

    def __init__(self, m, name, prefix, clk, rst, txd=None,
                 arg_params=None, arg_ports=None,
                 as_io=None, as_wire=None,
                 baudrate=19200, clockfreq=100 * 1000 * 1000):

        uart.UartTx.__init__(self, m, name, prefix, clk, rst, txd=txd,
                             arg_params=arg_params, arg_ports=arg_ports,
                             as_io=as_io, as_wire=as_wire,
                             baudrate=baudrate, clockfreq=clockfreq)

        self.mutex = None


class UartRx(uart.UartRx, _MutexFunction):
    __intrinsics__ = ('recv',) + _MutexFunction.__intrinsics__

    def __init__(self, m, name, prefix, clk, rst, rxd=None,
                 arg_params=None, arg_ports=None,
                 as_io=None, as_wire=None,
                 baudrate=19200, clockfreq=100 * 1000 * 1000):

        uart.UartRx.__init__(self, m, name, prefix, clk, rst, rxd=rxd,
                             arg_params=arg_params, arg_ports=arg_ports,
                             as_io=as_io, as_wire=as_wire,
                             baudrate=baudrate, clockfreq=clockfreq)

        self.mutex = None
