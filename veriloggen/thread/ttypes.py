from __future__ import absolute_import
from __future__ import print_function

import math

import veriloggen.core.vtypes as vtypes
from veriloggen.types.ram import SyncRAMManager
from veriloggen.types.fifo import Fifo
from veriloggen.types.axi import AxiMaster, AxiSlave
import veriloggen.types.uart as uart
import veriloggen.types.util as util
import veriloggen.types.fixed as fxd
from veriloggen.seq.seq import Seq
from veriloggen.fsm.fsm import FSM, TmpFSM
import veriloggen.dataflow.dtypes as dtypes

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


class RAM(SyncRAMManager, _MutexFunction):
    __intrinsics__ = ('read', 'write', 'dma_read',
                      'dma_write') + _MutexFunction.__intrinsics__

    def __init__(self, m, name, clk, rst,
                 datawidth=32, addrwidth=10, numports=1):

        SyncRAMManager.__init__(self, m, name, clk, rst,
                                datawidth, addrwidth, numports)
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
        return SyncRAMManager.read(self, port, addr, cond)

    def write_rtl(self, addr, data, port=0, cond=None):
        """
        @return None
        """
        return SyncRAMManager.write(self, port, addr, data, cond)

    def read(self, fsm, addr, port=0):
        """ intrinsic read operation using a shared Seq object """

        port = vtypes.to_int(port)
        cond = fsm.state == fsm.current

        rdata, rvalid = SyncRAMManager.read(self, port, addr, cond)
        rdata_reg = self.m.TmpReg(self.datawidth, initval=0, signed=True)

        fsm.If(rvalid)(
            rdata_reg(rdata)
        )
        fsm.Then().goto_next()

        return rdata_reg

    def write(self, fsm, addr, wdata, port=0, cond=None):
        """ intrinsic write operation using a shared Seq object """

        port = vtypes.to_int(port)

        if cond is None:
            cond = fsm.state == fsm.current
        else:
            cond = vtypes.Ands(cond, fsm.state == fsm.current)

        SyncRAMManager.write(self, port, addr, wdata, cond)
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

    def read(self, fsm, addr, port=0, raw=False):
        raw_value = RAM.read(self, fsm, addr, port)
        if raw:
            return raw_value
        return fxd.as_fixed(raw_value, self.point)

    def write(self, fsm, addr, wdata, port=0, cond=None, raw=False):
        if raw:
            fixed_wdata = wdata
        else:
            fixed_wdata = fxd.write_adjust(wdata, self.point)

        return RAM.write(self, fsm, addr, fixed_wdata, port, cond)


class MultibankRAM(object):
    __intrinsics__ = ('read', 'write', 'dma_read_bank', 'dma_write_bank',
                      'dma_read', 'dma_write') + _MutexFunction.__intrinsics__

    def __init__(self, m=None, name=None, clk=None, rst=None,
                 datawidth=32, addrwidth=10, numports=1,
                 numbanks=2, rams=None):

        if rams is not None:
            if not isinstance(rams, (tuple, list)):
                rams = [rams]

            self.m = rams[0].m
            self.name = rams[0].name
            self.clk = rams[0].clk
            self.rst = rams[0].rst
            self.orig_datawidth = rams[0].datawidth
            self.datawidth = rams[0].datawidth * len(rams)
            self.addrwidth = rams[0].addrwidth
            self.numports = rams[0].numports
            self.numbanks = len(rams)
            self.rams = rams

        elif (m is not None and name is not None and
              clk is not None and rst is not None):

            self.m = m
            self.name = name
            self.clk = clk
            self.rst = rst
            self.orig_datawidth = datawidth
            self.datawidth = datawidth * numbanks
            self.addrwidth = addrwidth
            self.numports = numports
            self.numbanks = numbanks
            self.rams = [RAM(m, '_'.join([name, '%d' % i]),
                             clk, rst, datawidth, addrwidth, numports)
                         for i in range(numbanks)]

        for i, ram in enumerate(self.rams):
            ram.bid = i

        self.mutex = None

    def __getitem__(self, index):
        return self.rams[index]

    def read(self, fsm, bank, addr, port=0):
        """ intrinsic read operation for multiple RAMs """

        port = vtypes.to_int(port)
        cond = fsm.state == fsm.current

        rdata_list = []
        rvalid_list = []
        for ram in self.rams:
            rdata, rvalid = SyncRAMManager.read(ram, port, addr, cond)
            rdata_list.append(rdata)
            rvalid_list.append(rvalid)

        rdata_reg = self.m.TmpReg(self.orig_datawidth, initval=0, signed=True)

        for i, ram in enumerate(self.rams):
            fsm.If(rvalid_list[i], bank == i)(
                rdata_reg(rdata_list[i])
            )

        fsm.If(rvalid_list[0]).goto_next()

        return rdata_reg

    def write(self, fsm, bank, addr, wdata, port=0, cond=None):
        if cond is None:
            cond = fsm.state == fsm.current
        else:
            cond = vtypes.Ands(cond, fsm.state == fsm.current)

        for i, ram in enumerate(self.rams):
            bank_cond = vtypes.Ands(cond, bank == i)
            SyncRAMManager.write(ram, port, addr, wdata, bank_cond)

        fsm.goto_next()

        return 0

    def dma_read_bank(self, fsm, bank, bus, local_addr, global_addr, size, port=0):
        check = fsm.current
        fsm.set_index(check + 1)

        starts = []
        ends = []
        for i, ram in enumerate(self.rams):
            starts.append(fsm.current)
            ram.dma_read(fsm, bus, local_addr, global_addr, size, port)
            ends.append(fsm.current)
            fsm.set_index(fsm.current + 1)

        fin = fsm.current

        for i, (s, e) in enumerate(zip(starts, ends)):
            fsm.goto_from(check, s, cond=bank == i)
            fsm.goto_from(e, fin)

        return 0

    def dma_write_bank(self, fsm, bank, bus, local_addr, global_addr, size, port=0):
        check = fsm.current
        fsm.set_index(check + 1)

        starts = []
        ends = []
        for i, ram in enumerate(self.rams):
            starts.append(fsm.current)
            ram.dma_write(fsm, bus, local_addr, global_addr, size, port)
            ends.append(fsm.current)
            fsm.set_index(fsm.current + 1)

        fin = fsm.current

        for i, (s, e) in enumerate(zip(starts, ends)):
            fsm.goto_from(check, s, cond=bank == i)
            fsm.goto_from(e, fin)

        return 0

    def dma_read(self, fsm, bus, local_addr, global_addr, size, port=0):
        if not isinstance(bus, AXIM):
            raise TypeError('AXIM interface is required')

        return bus.dma_read(fsm, self, local_addr, global_addr, size, port)

    def dma_write(self, fsm, bus, local_addr, global_addr, size, port=0):
        if not isinstance(bus, AXIM):
            raise TypeError('AXIM interface is required')

        return bus.dma_write(fsm, self, local_addr, global_addr, size, port)

    def read_dataflow(self, port, addr, length=1, cond=None, point=0, signed=False):
        """ 
        @return data, last, done
        """

        data_list = []
        last_list = []
        done_list = []
        for ram in self.rams:
            data, last, done = ram.read_dataflow(
                port, addr, length, cond, point, signed)
            data_list.insert(0, data)
            last_list.insert(0, last)
            done_list.insert(0, done)

        merged_data = dtypes.Cat(*data_list)
        merged_last = last_list[-1]
        merged_done = done_list[-1]

        return merged_data, merged_last, merged_done

    def write_dataflow(self, port, addr, data, length=1, cond=None, when=None):
        """ 
        @return done
        """

        done_list = []
        lsb = 0
        msb = 0
        for ram in self.rams:
            msb = msb + ram.datawidth
            bank_data = dtypes.Slice(data, msb, lsb)
            done = ram.write_dataflow(
                port, addr, bank_data, length, cond, when)
            done_list.insert(0, done)
            lsb = msb

        merged_done = done_list[-1]
        return merged_done


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


class AXIM(AxiMaster, _MutexFunction):
    __intrinsics__ = ('read', 'write', 'dma_read', 'dma_write',
                      'dma_read_async', 'dma_write_async',
                      'dma_wait', 'dma_idle') + _MutexFunction.__intrinsics__

    burstlen = 256

    def __init__(self, m, name, clk, rst, datawidth=32, addrwidth=32,
                 lite=False, noio=False):
        AxiMaster.__init__(self, m, name, clk, rst, datawidth, addrwidth,
                           lite=lite, noio=noio)
        self.mutex = None
        self.dma_fsm = None
        self.dma_fsm_max_state = 0

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

    def get_max_burstlen(self, ram):
        if vtypes.equals(self.datawidth, ram.datawidth):
            return self.burstlen

        comp = self.datawidth < ram.datawidth
        if not isinstance(comp, bool):
            raise ValueError('datawidth must be int, not (%s, %s)' %
                             (type(self.datawidth, ram.datawidth)))

        if comp:
            return int(self.burstlen // int(ram.datawidth // self.datawidth))

        return self.burstlen

    def dma_read(self, fsm, ram, local_addr, global_addr, size, port=0):
        if self.dma_fsm is not None:
            self.dma_wait(fsm)

        return self._dma_read(fsm, ram, local_addr, global_addr, size, port)

    def _dma_read(self, fsm, ram, local_addr, global_addr, size, port=0):
        if self.lite:
            raise TypeError('Lite-interface does not support DMA')

        if isinstance(ram, (tuple, list)):
            ram = MultibankRAM(rams=ram)

        if not isinstance(ram, (RAM, MultibankRAM)):
            raise TypeError('RAM is required')

        port = vtypes.to_int(port)
        req_local_addr = self.m.TmpReg(ram.addrwidth, initval=0)
        req_global_addr = self.m.TmpReg(self.addrwidth, initval=0)
        req_size = self.m.TmpReg(self.addrwidth, initval=0)
        rest_size = self.m.TmpReg(self.addrwidth, initval=0)

        max_burstlen = self.get_max_burstlen(ram)

        fsm(
            req_local_addr(local_addr),
            req_global_addr(global_addr),
            rest_size(size)
        )
        fsm.goto_next()

        check_state = fsm.current
        fsm.If(rest_size <= max_burstlen)(
            req_size(rest_size),
            rest_size(0)
        ).Else(
            req_size(max_burstlen),
            rest_size(rest_size - max_burstlen)
        )
        fsm.goto_next()

        cond = fsm.state == fsm.current

        done = AxiMaster.dma_read(self, ram, req_global_addr, req_local_addr, req_size,
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
        if self.dma_fsm is not None:
            self.dma_wait(fsm)

        return self._dma_write(fsm, ram, local_addr, global_addr, size, port)

    def _dma_write(self, fsm, ram, local_addr, global_addr, size, port=0):
        if self.lite:
            raise TypeError('Lite-interface does not support DMA')

        if isinstance(ram, (tuple, list)):
            ram = MultibankRAM(rams=ram)

        if not isinstance(ram, (RAM, MultibankRAM)):
            raise TypeError('RAM is required')

        port = vtypes.to_int(port)
        req_local_addr = self.m.TmpReg(ram.addrwidth, initval=0)
        req_global_addr = self.m.TmpReg(self.addrwidth, initval=0)
        req_size = self.m.TmpReg(self.addrwidth, initval=0)
        rest_size = self.m.TmpReg(self.addrwidth, initval=0)

        max_burstlen = self.get_max_burstlen(ram)

        fsm(
            req_local_addr(local_addr),
            req_global_addr(global_addr),
            rest_size(size)
        )
        fsm.goto_next()

        check_state = fsm.current
        fsm.If(rest_size <= max_burstlen)(
            req_size(rest_size),
            rest_size(0)
        ).Else(
            req_size(max_burstlen),
            rest_size(rest_size - max_burstlen)
        )
        fsm.goto_next()

        cond = fsm.state == fsm.current

        done = AxiMaster.dma_write(self, ram, req_global_addr, req_local_addr, req_size,
                                   cond=cond, ram_port=port)

        fsm.If(done)(
            req_local_addr.add(req_size),
            req_global_addr.add(compiler.optimize(
                req_size * (self.datawidth // 8)))
        )
        fsm.If(done, rest_size > 0).goto(check_state)
        fsm.If(done, rest_size == 0).goto_next()

        return 0

    def dma_read_async(self, fsm, ram, local_addr, global_addr, size, port=0):
        if self.dma_fsm is None:
            self.dma_fsm = FSM(self.m, '_'.join(['', self.name, 'dma_fsm']),
                               self.clk, self.rst)

        # init state
        start_state = 0
        self.dma_fsm.set_index(start_state)

        # start
        next_state = self.dma_fsm_max_state + 1
        self.dma_fsm.If(fsm.state == fsm.current).goto(next_state)
        self.dma_fsm.set_index(next_state)

        # call dma
        self._dma_read(self.dma_fsm, ram, local_addr,
                       global_addr, size, port)

        # remember maximum state
        self.dma_fsm_max_state = self.dma_fsm.current

        # reset
        self.dma_fsm.goto_init()

        # wait idle state by master fsm
        self.dma_wait(fsm)

        return 0

    def dma_write_async(self, fsm, ram, local_addr, global_addr, size, port=0):
        if self.dma_fsm is None:
            self.dma_fsm = FSM(self.m, '_'.join(['', self.name, 'dma_fsm']),
                               self.clk, self.rst)

        # init state
        start_state = 0
        self.dma_fsm.set_index(start_state)

        # start
        next_state = self.dma_fsm_max_state + 1
        self.dma_fsm.If(fsm.state == fsm.current).goto(next_state)
        self.dma_fsm.set_index(next_state)

        # call dma
        self._dma_write(self.dma_fsm, ram, local_addr,
                        global_addr, size, port)

        # remember maximum state
        self.dma_fsm_max_state = self.dma_fsm.current

        # reset
        self.dma_fsm.goto_init()

        # wait idle state by master fsm
        self.dma_wait(fsm)

        return 0

    def dma_wait(self, fsm):
        start_state = 0
        fsm.If(self.dma_fsm.state == start_state).goto_next()
        return 0

    def dma_idle(self, fsm):
        start_state = 0
        flag = self.dma_fsm.state == start_state
        return flag


class AXIS(AxiSlave, _MutexFunction):
    __intrinsics__ = _MutexFunction.__intrinsics__

    def __init__(self, m, name, clk, rst, datawidth=32, addrwidth=32,
                 lite=False, noio=False):
        AxiSlave.__init__(self, m, name, clk, rst, datawidth, addrwidth,
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
