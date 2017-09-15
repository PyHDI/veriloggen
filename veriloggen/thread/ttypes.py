from __future__ import absolute_import
from __future__ import print_function

import functools
import math
import inspect
import collections

import veriloggen.core.vtypes as vtypes
import veriloggen.dataflow.dtypes as dtypes
from veriloggen.dataflow.dataflow import DataflowManager
from veriloggen.seq.seq import Seq
from veriloggen.fsm.fsm import FSM, TmpFSM
from veriloggen.optimizer import try_optimize as optimize

import veriloggen.types.uart as uart
import veriloggen.types.util as util
import veriloggen.types.fixed as fxd
from veriloggen.types.ram import SyncRAMManager
from veriloggen.types.fifo import Fifo
from veriloggen.types.axi import AxiMaster, AxiSlave


class _verilog_meta(type):
    """ metaclass for verilog operator intrinsics """

    __verilog_classes__ = dict(inspect.getmembers(vtypes))
    __intrinsics__ = tuple(__verilog_classes__.keys())

    def __getattr__(self, key):
        if key in self.__verilog_classes__:
            cls = self.__verilog_classes__[key]

            @functools.wraps(cls)
            def wrapper(fsm, *args, **kwargs):
                return cls(*args, **kwargs)
            return wrapper

        raise NameError("name '%s' is not defined" % key)


_verilog = _verilog_meta('verilog', (object,),
                         {'__doc__': _verilog_meta.__doc__})


class verilog(_verilog):
    """ verilog operator intrinsics """
    pass


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
        self.width = util.log2(self.numparties) + 1

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
    __intrinsics__ = ('read', 'write') + _MutexFunction.__intrinsics__

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
    __intrinsics__ = ('read', 'write',
                      'read_bank', 'write_bank',
                      'dma_read_bank', 'dma_write_bank') + _MutexFunction.__intrinsics__

    def __init__(self, m=None, name=None, clk=None, rst=None,
                 datawidth=32, addrwidth=10, numports=1,
                 numbanks=2, rams=None):

        if rams is not None:
            if not isinstance(rams, (tuple, list)):
                rams = [rams]

            if math.log(len(rams), 2) % 1.0 != 0.0:
                raise ValueError('numbanks must be power-of-2')

            if len(rams) < 2:
                raise ValueError('numbanks must be 2 or more')

            max_datawidth = 0
            for ram in rams:
                max_datawidth = max(max_datawidth, ram.datawidth)

            max_addrwidth = 0
            for ram in rams:
                max_addrwidth = max(max_addrwidth, ram.addrwidth)

            max_numports = rams[0].numports
            for ram in rams[1:]:
                if max_numports != ram.numports:
                    raise ValueError('numports must be same')

            self.m = rams[0].m
            self.name = rams[0].name
            self.clk = rams[0].clk
            self.rst = rams[0].rst
            self.orig_datawidth = max_datawidth
            self.datawidth = max_datawidth * len(rams)
            self.addrwidth = max_addrwidth
            self.numports = max_numports
            self.numbanks = len(rams)
            self.shift = util.log2(self.numbanks)
            self.rams = rams

        elif (m is not None and name is not None and
              clk is not None and rst is not None):

            if math.log(numbanks, 2) % 1.0 != 0.0:
                raise ValueError('numbanks must be power-of-2')

            if numbanks < 2:
                raise ValueError('numbanks must be 2 or more')

            self.m = m
            self.name = name
            self.clk = clk
            self.rst = rst
            self.orig_datawidth = datawidth
            self.datawidth = datawidth * numbanks
            self.addrwidth = addrwidth
            self.numports = numports
            self.numbanks = numbanks
            self.shift = util.log2(self.numbanks)
            self.rams = [RAM(m, '_'.join([name, '%d' % i]),
                             clk, rst, datawidth, addrwidth, numports)
                         for i in range(numbanks)]

        for i, ram in enumerate(self.rams):
            ram.bid = i

        self.df = DataflowManager(self.m, self.clk, self.rst)

        self.mutex = None

    def __getitem__(self, index):
        return self.rams[index]

    def disable_write(self, port):
        for ram in self.rams:
            ram.seq(
                ram.interfaces[port].wdata(0),
                ram.interfaces[port].wenable(0)
            )
            ram._write_disabled[port] = True

    def read(self, fsm, addr, port=0):
        """ intrinsic read operation for multiple RAMs """

        port = vtypes.to_int(port)
        cond = fsm.state == fsm.current

        rdata_list = []
        rvalid_list = []

        bank = self.m.TmpWire(self.shift)
        bank.assign(addr)
        addr = addr >> self.shift

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

    def write(self, fsm, addr, wdata, port=0, cond=None):
        if cond is None:
            cond = fsm.state == fsm.current
        else:
            cond = vtypes.Ands(cond, fsm.state == fsm.current)

        bank = self.m.TmpWire(self.shift)
        bank.assign(addr)
        addr = addr >> self.shift

        for i, ram in enumerate(self.rams):
            bank_cond = vtypes.Ands(cond, bank == i)
            SyncRAMManager.write(ram, port, addr, wdata, bank_cond)

        fsm.goto_next()

        return 0

    def read_bank(self, fsm, bank, addr, port=0):
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

    def write_bank(self, fsm, bank, addr, wdata, port=0, cond=None):
        if cond is None:
            cond = fsm.state == fsm.current
        else:
            cond = vtypes.Ands(cond, fsm.state == fsm.current)

        for i, ram in enumerate(self.rams):
            bank_cond = vtypes.Ands(cond, bank == i)
            SyncRAMManager.write(ram, port, addr, wdata, bank_cond)

        fsm.goto_next()

        return 0

    def dma_read_bank(self, fsm, bank, bus, local_addr, global_addr, size,
                      local_stride=1, port=0):
        check = fsm.current
        fsm.set_index(check + 1)

        starts = []
        ends = []
        for i, ram in enumerate(self.rams):
            starts.append(fsm.current)
            bus.dma_read(fsm, ram, local_addr, global_addr, size,
                         local_stride, port)
            ends.append(fsm.current)
            fsm.set_index(fsm.current + 1)

        fin = fsm.current

        for i, (s, e) in enumerate(zip(starts, ends)):
            fsm.goto_from(check, s, cond=bank == i)
            fsm.goto_from(e, fin)

        return 0

    def dma_write_bank(self, fsm, bank, bus, local_addr, global_addr, size,
                       local_stride=1, port=0):
        check = fsm.current
        fsm.set_index(check + 1)

        starts = []
        ends = []
        for i, ram in enumerate(self.rams):
            starts.append(fsm.current)
            bus.dma_write(fsm, ram, local_addr, global_addr, size,
                          local_stride, port)
            ends.append(fsm.current)
            fsm.set_index(fsm.current + 1)

        fin = fsm.current

        for i, (s, e) in enumerate(zip(starts, ends)):
            fsm.goto_from(check, s, cond=bank == i)
            fsm.goto_from(e, fin)

        return 0

    def read_dataflow(self, port, addr, length=1,
                      stride=1, cond=None, point=0, signed=False):
        """ 
        @return data, last, done
        """

        data_list = []
        last_list = []
        done_list = []
        for ram in self.rams:
            data, last, done = ram.read_dataflow(
                port, addr, length, stride, cond, point, signed)
            data_list.insert(0, data)
            last_list.insert(0, last)
            done_list.insert(0, done)

        merged_data = dtypes.Cat(*data_list)
        merged_last = last_list[-1]
        merged_done = done_list[-1]

        return merged_data, merged_last, merged_done

    def read_dataflow_interleave(self, port, addr, length=1,
                                 stride=1, cond=None, point=0, signed=False):
        """ 
        @return data, last, done
        """

        if not hasattr(self, 'seq'):
            self.seq = Seq(self.m, self.name, self.clk, self.rst)

        data_valid = self.m.TmpReg(initval=0)
        last_valid = self.m.TmpReg(initval=0)
        data_ready = self.m.TmpWire()
        last_ready = self.m.TmpWire()
        data_ready.assign(1)
        last_ready.assign(1)

        data_ack = vtypes.Ors(data_ready, vtypes.Not(data_valid))
        last_ack = vtypes.Ors(last_ready, vtypes.Not(last_valid))

        ext_cond = dtypes.make_condition(cond)
        data_cond = dtypes.make_condition(data_ack, last_ack)
        prev_data_cond = self.seq.Prev(data_cond, 1)

        data_list = [self.m.TmpWireLike(ram.interfaces[port].rdata)
                     for ram in self.rams]

        prev_data_list = [self.seq.Prev(data, 1) for data in data_list]
        for data, prev_data, ram in zip(data_list, prev_data_list, self.rams):
            data.assign(vtypes.Mux(prev_data_cond,
                                   ram.interfaces[port].rdata, prev_data))

        log_numbanks = util.log2(self.numbanks)
        reg_addr = self.m.TmpReg(self.addrwidth + log_numbanks, initval=0)
        next_addr = self.m.TmpWire(self.addrwidth + log_numbanks)
        next_addr.assign(reg_addr + stride)
        ram_addr_list = [self.m.TmpWire(ram.addrwidth) for ram in self.rams]
        for ram_addr in ram_addr_list:
            ram_addr.assign(next_addr >> log_numbanks)

        bank_sel = self.m.TmpWire(log_numbanks)
        bank_sel.assign(reg_addr[0:log_numbanks])
        reg_bank_sel = self.m.TmpReg(log_numbanks, initval=0)
        prev_reg_bank_sel = self.seq.Prev(reg_bank_sel, 1)
        self.seq(
            reg_bank_sel(bank_sel)
        )

        patterns = [(reg_bank_sel == i, data)
                    for i, data in enumerate(data_list)]
        patterns.append((None, 0))
        prev_patterns = [(prev_reg_bank_sel == i, data)
                         for i, data in enumerate(prev_data_list)]
        prev_patterns.append((None, 0))
        data = self.m.TmpWire(self.orig_datawidth)
        data.assign(vtypes.Mux(prev_data_cond,
                               vtypes.PatternMux(*patterns),
                               vtypes.PatternMux(*prev_patterns)))

        next_valid_on = self.m.TmpReg(initval=0)
        next_valid_off = self.m.TmpReg(initval=0)

        next_last = self.m.TmpReg(initval=0)
        last = self.m.TmpReg(initval=0)

        counter = self.m.TmpReg(length.bit_length() + 1, initval=0)

        self.seq.If(data_cond, next_valid_off)(
            last(0),
            data_valid(0),
            last_valid(0),
            next_valid_off(0)
        )

        self.seq.If(data_cond, next_valid_on)(
            data_valid(1),
            last_valid(1),
            last(next_last),
            next_last(0),
            next_valid_on(0),
            next_valid_off(1)
        )

        self.seq.If(ext_cond, counter == 0,
                    vtypes.Not(next_last), vtypes.Not(last))(
            reg_addr(addr),
            counter(length - 1),
            next_valid_on(1),
            next_last(length == 1)
        )

        for ram in self.rams:
            ram.seq.If(ext_cond, counter == 0,
                       vtypes.Not(next_last), vtypes.Not(last))(
                ram.interfaces[port].addr(addr >> log_numbanks)
            )

        self.seq.If(data_cond, counter > 0)(
            reg_addr(reg_addr + stride),
            counter.dec(),
            next_valid_on(1),
            next_last(0)
        )

        for ram, ram_addr in zip(self.rams, ram_addr_list):
            ram.seq.If(data_cond, counter > 0)(
                ram.interfaces[port].addr(ram_addr)
            )

        self.seq.If(data_cond, counter == 1)(
            next_last(1)
        )

        df = self.df if self.df is not None else dataflow

        df_data = df.Variable(data, data_valid, data_ready,
                              width=self.orig_datawidth, point=point, signed=signed)
        df_last = df.Variable(last, last_valid, last_ready, width=1)
        done = last

        return df_data, df_last, done

    def read_dataflow_pattern_interleave(self, port, addr, pattern,
                                         cond=None, point=0, signed=False):
        """ 
        @return data, last, done
        """

        if not hasattr(self, 'seq'):
            self.seq = Seq(self.m, self.name, self.clk, self.rst)

        if not isinstance(pattern, (tuple, list)):
            raise TypeError('pattern must be list or tuple.')

        if not pattern:
            raise ValueError(
                'pattern must have one (size, stride) pair at least.')

        if not isinstance(pattern[0], (tuple, list)):
            pattern = (pattern,)

        data_valid = self.m.TmpReg(initval=0)
        last_valid = self.m.TmpReg(initval=0)
        data_ready = self.m.TmpWire()
        last_ready = self.m.TmpWire()
        data_ready.assign(1)
        last_ready.assign(1)

        data_ack = vtypes.Ors(data_ready, vtypes.Not(data_valid))
        last_ack = vtypes.Ors(last_ready, vtypes.Not(last_valid))

        ext_cond = dtypes.make_condition(cond)
        data_cond = dtypes.make_condition(data_ack, last_ack)
        prev_data_cond = self.seq.Prev(data_cond, 1)

        data_list = [self.m.TmpWireLike(ram.interfaces[port].rdata)
                     for ram in self.rams]

        prev_data_list = [self.seq.Prev(data, 1) for data in data_list]
        for data, prev_data, ram in zip(data_list, prev_data_list, self.rams):
            data.assign(vtypes.Mux(prev_data_cond,
                                   ram.interfaces[port].rdata, prev_data))

        log_numbanks = util.log2(self.numbanks)
        reg_addr = self.m.TmpReg(self.addrwidth + log_numbanks, initval=0)

        bank_sel = self.m.TmpWire(log_numbanks)
        bank_sel.assign(reg_addr[0:log_numbanks])
        reg_bank_sel = self.m.TmpReg(log_numbanks, initval=0)
        prev_reg_bank_sel = self.seq.Prev(reg_bank_sel, 1)
        self.seq(
            reg_bank_sel(bank_sel)
        )

        patterns = [(reg_bank_sel == i, data)
                    for i, data in enumerate(data_list)]
        patterns.append((None, 0))
        prev_patterns = [(prev_reg_bank_sel == i, data)
                         for i, data in enumerate(prev_data_list)]
        prev_patterns.append((None, 0))
        data = self.m.TmpWire(self.orig_datawidth)
        data.assign(vtypes.Mux(prev_data_cond,
                               vtypes.PatternMux(*patterns),
                               vtypes.PatternMux(*prev_patterns)))

        next_valid_on = self.m.TmpReg(initval=0)
        next_valid_off = self.m.TmpReg(initval=0)

        next_last = self.m.TmpReg(initval=0)
        last = self.m.TmpReg(initval=0)

        running = self.m.TmpReg(initval=0)

        next_addr = self.m.TmpWire(self.addrwidth + log_numbanks)
        offset_addr = self.m.TmpWire(self.addrwidth + log_numbanks)
        offsets = [self.m.TmpReg(self.addrwidth + log_numbanks, initval=0)
                   for _ in pattern[1:]]

        ram_addr_list = [self.m.TmpWire(ram.addrwidth) for ram in self.rams]
        for ram_addr in ram_addr_list:
            ram_addr.assign(next_addr >> log_numbanks)

        offset_addr_value = addr
        for offset in offsets:
            offset_addr_value = offset + offset_addr_value
        offset_addr.assign(offset_addr_value)

        offsets.insert(0, None)

        count_list = [self.m.TmpReg(out_size.bit_length() + 1, initval=0)
                      for (out_size, out_stride) in pattern]

        self.seq.If(data_cond, next_valid_off)(
            last(0),
            data_valid(0),
            last_valid(0),
            next_valid_off(0)
        )

        self.seq.If(data_cond, next_valid_on)(
            data_valid(1),
            last_valid(1),
            last(next_last),
            next_last(0),
            next_valid_on(0),
            next_valid_off(1)
        )

        self.seq.If(ext_cond, vtypes.Not(running),
                    vtypes.Not(next_last), vtypes.Not(last))(
            reg_addr(addr),
            running(1),
            next_valid_on(1)
        )

        for ram in self.rams:
            ram.seq.If(ext_cond, vtypes.Not(running),
                       vtypes.Not(next_last), vtypes.Not(last))(
                ram.interfaces[port].addr(addr >> log_numbanks)
            )

        self.seq.If(data_cond, running)(
            reg_addr(next_addr),
            next_valid_on(1),
            next_last(0)
        )

        for ram in self.rams:
            ram.seq.If(data_cond, running)(
                ram.interfaces[port].addr(ram_addr)
            )

        update_count = None
        update_offset = None
        update_addr = None
        last_one = None
        stride_value = None
        carry = None

        for offset, count, (out_size, out_stride) in zip(offsets, count_list, pattern):
            self.seq.If(ext_cond, vtypes.Not(running),
                        vtypes.Not(next_last), vtypes.Not(last))(
                count(out_size - 1)
            )
            self.seq.If(data_cond, running, update_count)(
                count.dec()
            )
            self.seq.If(data_cond, running, update_count, count == 0)(
                count(out_size - 1)
            )

            if offset is not None:
                self.seq.If(ext_cond, vtypes.Not(running),
                            vtypes.Not(next_last), vtypes.Not(last))(
                    offset(0)
                )
                self.seq.If(data_cond, running, update_offset, vtypes.Not(carry))(
                    offset(offset + out_stride)
                )
                self.seq.If(data_cond, running, update_offset, count == 0)(
                    offset(0)
                )

            if update_count is None:
                update_count = count == 0
            else:
                update_count = vtypes.Ands(update_count, count == 0)

            if update_offset is None:
                update_offset = vtypes.Mux(out_size == 1, 1, count == 1)
            else:
                update_offset = vtypes.Ands(update_offset, count == carry)

            if update_addr is None:
                update_addr = count == 0
            else:
                update_addr = vtypes.Mux(carry, count == 0, update_addr)

            if last_one is None:
                last_one = count == 0
            else:
                last_one = vtypes.Ands(last_one, count == 0)

            if stride_value is None:
                stride_value = out_stride
            else:
                stride_value = vtypes.Mux(carry, out_stride, stride_value)

            if carry is None:
                carry = out_size == 1
            else:
                carry = vtypes.Ands(carry, out_size == 1)

        next_addr.assign(vtypes.Mux(update_addr, offset_addr,
                                    reg_addr + stride_value))

        self.seq.If(data_cond, running, last_one)(
            running(0),
            next_last(1)
        )

        df = self.df if self.df is not None else dataflow

        df_data = df.Variable(data, data_valid, data_ready,
                              width=self.datawidth, point=point, signed=signed)
        df_last = df.Variable(last, last_valid, last_ready, width=1)
        done = last

        return df_data, df_last, done

    def read_dataflow_multidim_interleave(self, port, addr, shape, order=None,
                                          cond=None, point=0, signed=False):
        """ 
        @return data, last, done
        """
        if order is None:
            order = list(range(len(shape)))

        pattern = self._to_pattern(shape, order)
        return self.read_dataflow_pattern_interleave(port, addr, pattern,
                                                     cond=cond, point=point, signed=signed)

    def write_dataflow(self, port, addr, data, length=1,
                       stride=1, cond=None, when=None):
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
                port, addr, bank_data, length, stride, cond, when)
            done_list.insert(0, done)
            lsb = msb

        merged_done = done_list[-1]
        return merged_done

    def write_dataflow_interleave(self, port, addr, data, length=1,
                                  stride=1, cond=None, when=None):
        """ 
        @return done
        'data' and 'when' must be dataflow variables
        """

        if not hasattr(self, 'seq'):
            self.seq = Seq(self.m, self.name, self.clk, self.rst)

        for ram in self.rams:
            if ram._write_disabled[port]:
                raise TypeError('Write disabled.')

        counter = self.m.TmpReg(length.bit_length() + 1, initval=0)
        last = self.m.TmpReg(initval=0)

        ext_cond = dtypes.make_condition(cond)
        data_cond = dtypes.make_condition(counter > 0, vtypes.Not(last))

        if when is None or not isinstance(when, df_numeric):
            raw_data, raw_valid = data.read(cond=data_cond)
        else:
            data_list, raw_valid = dtypes.read_multi(
                self.m, data, when, cond=data_cond)
            raw_data = data_list[0]
            when = data_list[1]

        when_cond = dtypes.make_condition(when, ready=data_cond)
        if when_cond is not None:
            raw_valid = vtypes.Ands(when_cond, raw_valid)

        log_numbanks = util.log2(self.numbanks)
        reg_addr = self.m.TmpReg(self.addrwidth + log_numbanks, initval=0)
        next_addr = self.m.TmpWire(self.addrwidth + log_numbanks)
        next_addr.assign(reg_addr + stride)
        ram_addr_list = [self.m.TmpWire(ram.addrwidth) for ram in self.rams]
        for ram_addr in ram_addr_list:
            ram_addr.assign(next_addr >> log_numbanks)

        bank_sel = self.m.TmpWire(log_numbanks)
        bank_sel.assign(next_addr)

        self.seq.If(ext_cond, counter == 0)(
            reg_addr(addr - stride),
            counter(length),
        )

        self.seq.If(raw_valid, counter > 0)(
            reg_addr(next_addr),
            counter.dec()
        )

        for i, (ram, ram_addr) in enumerate(zip(self.rams, ram_addr_list)):
            ram.seq.If(raw_valid, counter > 0)(
                ram.interfaces[port].addr(ram_addr),
                ram.interfaces[port].wdata(raw_data),
                ram.interfaces[port].wenable(bank_sel == i)
            )

        self.seq.If(raw_valid, counter == 1)(
            last(1)
        )

        # de-assert
        self.seq.Delay(1)(
            last(0)
        )

        for ram in self.rams:
            ram.seq.Delay(1)(
                ram.interfaces[port].wenable(0)
            )

        done = last

        return done

    def write_dataflow_pattern_interleave(self, port, addr, data, pattern,
                                          cond=None, when=None):
        """ 
        @return done
        'data' and 'when' must be dataflow variables
        """

        if not hasattr(self, 'seq'):
            self.seq = Seq(self.m, self.name, self.clk, self.rst)

        for ram in self.rams:
            if ram._write_disabled[port]:
                raise TypeError('Write disabled.')

        if not isinstance(pattern, (tuple, list)):
            raise TypeError('pattern must be list or tuple.')

        if not pattern:
            raise ValueError(
                'pattern must have one (size, stride) pair at least.')

        if not isinstance(pattern[0], (tuple, list)):
            pattern = (pattern,)

        last = self.m.TmpReg(initval=0)

        running = self.m.TmpReg(initval=0)

        ext_cond = dtypes.make_condition(cond)
        data_cond = dtypes.make_condition(running, vtypes.Not(last))

        if when is None or not isinstance(when, df_numeric):
            raw_data, raw_valid = data.read(cond=data_cond)
        else:
            data_list, raw_valid = dtypes.read_multi(
                self.m, data, when, cond=data_cond)
            raw_data = data_list[0]
            when = data_list[1]

        when_cond = dtypes.make_condition(when, ready=data_cond)
        if when_cond is not None:
            raw_valid = vtypes.Ands(when_cond, raw_valid)

        offset_addr = self.m.TmpWire(self.addrwidth)
        offsets = [self.m.TmpReg(self.addrwidth, initval=0) for _ in pattern]

        offset_addr_value = addr
        for offset in offsets:
            offset_addr_value = offset + offset_addr_value
        offset_addr.assign(offset_addr_value)

        log_numbanks = util.log2(self.numbanks)
        ram_addr_list = [self.m.TmpWire(ram.addrwidth) for ram in self.rams]
        for ram_addr in ram_addr_list:
            ram_addr.assign(offset_addr >> log_numbanks)

        bank_sel = self.m.TmpWire(log_numbanks)
        bank_sel.assign(offset_addr)

        count_list = [self.m.TmpReg(out_size.bit_length() + 1, initval=0)
                      for (out_size, out_stride) in pattern]

        self.seq.If(ext_cond, vtypes.Not(running))(
            running(1)
        )

        for i, (ram, ram_addr) in enumerate(zip(self.rams, ram_addr_list)):
            ram.seq.If(raw_valid, running)(
                ram.interfaces[port].addr(ram_addr),
                ram.interfaces[port].wdata(raw_data),
                ram.interfaces[port].wenable(bank_sel == i)
            )

        update_count = None
        last_one = None

        for offset, count, (out_size, out_stride) in zip(offsets, count_list, pattern):
            self.seq.If(ext_cond, vtypes.Not(running))(
                count(out_size - 1),
                offset(0)
            )
            self.seq.If(raw_valid, running, update_count)(
                count.dec(),
                offset(offset + out_stride)
            )
            self.seq.If(raw_valid, running, update_count, count == 0)(
                count(out_size - 1),
                offset(0)
            )

            if update_count is None:
                update_count = count == 0
            else:
                update_count = vtypes.Ands(update_count, count == 0)

            if last_one is None:
                last_one = count == 0
            else:
                last_one = vtypes.Ands(last_one, count == 0)

        self.seq.If(raw_valid, last_one)(
            running(0),
            last(1)
        )

        # de-assert
        self.seq.Delay(1)(
            last(0)
        )

        for ram in self.rams:
            ram.seq.Delay(1)(
                ram.interfaces[port].wenable(0)
            )

        done = last

        return done

    def write_dataflow_multidim_interleave(self, port, addr, data, shape, order=None,
                                           cond=None, when=None):
        """ 
        @return done
        'data' and 'when' must be dataflow variables
        """
        if order is None:
            order = list(range(len(shape)))

        pattern = self._to_pattern(shape, order)
        return self.write_dataflow_pattern_interleave(port, addr, data, pattern,
                                                      cond=cond, when=when)


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
    __intrinsics__ = ('read', 'write',
                      'dma_read', 'dma_write',
                      'dma_read_async', 'dma_write_async',
                      'dma_read_pattern', 'dma_write_pattern',
                      'dma_read_pattern_async', 'dma_write_pattern_async',
                      'dma_read_multidim', 'dma_write_multidim',
                      'dma_read_multidim_async', 'dma_write_multidim_async',
                      'dma_wait', 'dma_idle') + _MutexFunction.__intrinsics__

    burstlen = 256

    def __init__(self, m, name, clk, rst, datawidth=32, addrwidth=32,
                 lite=False, noio=False, enable_async=False):
        AxiMaster.__init__(self, m, name, clk, rst, datawidth, addrwidth,
                           lite=lite, noio=noio)
        self.mutex = None
        self.enable_async = enable_async
        if self.enable_async:
            self.dma_fsm = FSM(self.m, '_'.join(['', self.name, 'dma_async_fsm']),
                               self.clk, self.rst)
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

    def dma_read(self, fsm, ram, local_addr, global_addr, size,
                 local_stride=1, port=0):
        if self.enable_async:
            self.dma_wait(fsm)

        return self._dma_read(fsm, ram, local_addr, global_addr, size,
                              local_stride, port)

    def _dma_read(self, fsm, ram, local_addr, global_addr, size,
                  local_stride=1, port=0):
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
        if isinstance(local_stride, (int, vtypes.Int)):
            req_local_stride = local_stride
        else:
            req_local_stride = self.m.TmpReg(ram.addrwidth, initval=1)

        fsm(
            req_local_addr(local_addr),
            req_global_addr(global_addr),
            req_size(size),
        )
        if not isinstance(local_stride, (int, vtypes.Int)):
            fsm(
                req_local_stride(local_stride)
            )
        fsm.goto_next()

        cond = fsm.state == fsm.current

        done = AxiMaster.dma_read(self, ram, req_global_addr, req_local_addr, req_size,
                                  stride=req_local_stride,
                                  cond=cond, ram_port=port)

        fsm.If(done).goto_next()

        return 0

    def dma_read_pattern(self, fsm, ram, local_addr, global_addr, pattern,
                         port=0):
        if self.enable_async:
            self.dma_wait(fsm)

        return self._dma_read_pattern(fsm, ram, local_addr, global_addr, pattern,
                                      port)

    def _dma_read_pattern(self, fsm, ram, local_addr, global_addr, pattern,
                          port=0):
        if self.lite:
            raise TypeError('Lite-interface does not support DMA')

        if isinstance(ram, (tuple, list)):
            ram = MultibankRAM(rams=ram)

        if not isinstance(ram, (RAM, MultibankRAM)):
            raise TypeError('RAM is required')

        # for pattern
        if not isinstance(pattern, (tuple, list)):
            raise TypeError('pattern must be list or tuple.')

        if not pattern:
            raise ValueError(
                'pattern must have one (size, stride) pair at least.')

        if not isinstance(pattern[0], (tuple, list)):
            pattern = (pattern,)

        port = vtypes.to_int(port)
        req_local_addr = self.m.TmpReg(ram.addrwidth, initval=0)
        req_global_addr = self.m.TmpReg(self.addrwidth, initval=0)

        req_pattern = []
        for size, stride in pattern:
            req_pattern.append((self.m.TmpReg(size.bit_length() + 1, initval=0),
                                self.m.TmpReg(stride.bit_length() + 1, initval=0)))

        fsm(
            req_local_addr(local_addr),
            req_global_addr(global_addr)
        )
        for (req_size, req_stride), (size, stride) in zip(req_pattern, pattern):
            fsm(
                req_size(size),
                req_stride(stride)
            )
        fsm.goto_next()

        cond = fsm.state == fsm.current

        done = AxiMaster.dma_read_pattern(self, ram, req_global_addr, req_local_addr,
                                          req_pattern,
                                          cond=cond, ram_port=port)

        fsm.If(done).goto_next()

        return 0

    def dma_read_multidim(self, fsm, ram, local_addr, global_addr, shape, order=None,
                          port=0):
        if order is None:
            order = list(range(len(shape)))

        pattern = self._to_pattern(shape, order)
        return self.dma_read_pattern(fsm, ram, local_addr, global_addr, pattern,
                                     port)

    def dma_write(self, fsm, ram, local_addr, global_addr, size,
                  local_stride=1, port=0):
        if self.enable_async:
            self.dma_wait(fsm)

        return self._dma_write(fsm, ram, local_addr, global_addr, size,
                               local_stride, port)

    def _dma_write(self, fsm, ram, local_addr, global_addr, size,
                   local_stride=1, port=0):
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
        if isinstance(local_stride, (int, vtypes.Int)):
            req_local_stride = local_stride
        else:
            req_local_stride = self.m.TmpReg(ram.addrwidth, initval=1)

        fsm(
            req_local_addr(local_addr),
            req_global_addr(global_addr),
            req_size(size)
        )
        if not isinstance(local_stride, (int, vtypes.Int)):
            fsm(
                req_local_stride(local_stride)
            )
        fsm.goto_next()

        cond = fsm.state == fsm.current

        done = AxiMaster.dma_write(self, ram, req_global_addr, req_local_addr, req_size,
                                   stride=req_local_stride,
                                   cond=cond, ram_port=port)

        fsm.If(done).goto_next()

        return 0

    def dma_write_pattern(self, fsm, ram, local_addr, global_addr, pattern,
                          port=0):
        if self.enable_async:
            self.dma_wait(fsm)

        return self._dma_write_pattern(fsm, ram, local_addr, global_addr, pattern,
                                       port)

    def _dma_write_pattern(self, fsm, ram, local_addr, global_addr, pattern,
                           port=0):
        if self.lite:
            raise TypeError('Lite-interface does not support DMA')

        if isinstance(ram, (tuple, list)):
            ram = MultibankRAM(rams=ram)

        if not isinstance(ram, (RAM, MultibankRAM)):
            raise TypeError('RAM is required')

        # for pattern
        if not isinstance(pattern, (tuple, list)):
            raise TypeError('pattern must be list or tuple.')

        if not pattern:
            raise ValueError(
                'pattern must have one (size, stride) pair at least.')

        if not isinstance(pattern[0], (tuple, list)):
            pattern = (pattern,)

        port = vtypes.to_int(port)
        req_local_addr = self.m.TmpReg(ram.addrwidth, initval=0)
        req_global_addr = self.m.TmpReg(self.addrwidth, initval=0)

        req_pattern = []
        for size, stride in pattern:
            req_pattern.append((self.m.TmpReg(size.bit_length() + 1, initval=0),
                                self.m.TmpReg(stride.bit_length() + 1, initval=0)))

        fsm(
            req_local_addr(local_addr),
            req_global_addr(global_addr)
        )
        for (req_size, req_stride), (size, stride) in zip(req_pattern, pattern):
            fsm(
                req_size(size),
                req_stride(stride)
            )
        fsm.goto_next()

        cond = fsm.state == fsm.current

        done = AxiMaster.dma_write_pattern(self, ram, req_global_addr, req_local_addr,
                                           req_pattern,
                                           cond=cond, ram_port=port)

        fsm.If(done).goto_next()

        return 0

    def dma_write_multidim(self, fsm, ram, local_addr, global_addr, shape, order=None,
                           port=0):
        if order is None:
            order = list(range(len(shape)))

        pattern = self._to_pattern(shape, order)
        return self.dma_write_pattern(fsm, ram, local_addr, global_addr, pattern,
                                      port)

    def dma_read_async(self, fsm, ram, local_addr, global_addr, size,
                       local_stride=1, port=0):
        if not self.enable_async:
            raise ValueError('async DMA is disabled.')

        # init state
        start_state = 0
        self.dma_fsm.set_index(start_state)

        # start
        next_state = self.dma_fsm_max_state + 1
        self.dma_fsm.If(fsm.state == fsm.current).goto(next_state)
        self.dma_fsm.set_index(next_state)

        # call dma
        self._dma_read(self.dma_fsm, ram, local_addr,
                       global_addr, size, local_stride, port)

        # remember maximum state
        self.dma_fsm_max_state = self.dma_fsm.current

        # reset
        self.dma_fsm.goto_init()

        # wait idle state by master fsm
        self.dma_wait(fsm)

        return 0

    def dma_read_pattern_async(self, fsm, ram, local_addr, global_addr, pattern,
                               port=0):
        if not self.enable_async:
            raise ValueError('async DMA is disabled.')

        # init state
        start_state = 0
        self.dma_fsm.set_index(start_state)

        # start
        next_state = self.dma_fsm_max_state + 1
        self.dma_fsm.If(fsm.state == fsm.current).goto(next_state)
        self.dma_fsm.set_index(next_state)

        # call dma
        self._dma_read_pattern(self.dma_fsm, ram, local_addr, global_addr,
                               pattern, port)

        # remember maximum state
        self.dma_fsm_max_state = self.dma_fsm.current

        # reset
        self.dma_fsm.goto_init()

        # wait idle state by master fsm
        self.dma_wait(fsm)

        return 0

    def dma_read_multidim_async(self, fsm, ram, local_addr, global_addr, shape,
                                order=None, port=0):
        if order is None:
            order = list(range(len(shape)))

        pattern = self._to_pattern(shape, order)
        return self.dma_read_pattern_async(fsm, ram, local_addr, global_addr,
                                           pattern, port)

    def dma_write_async(self, fsm, ram, local_addr, global_addr, size,
                        local_stride=1, port=0):
        if not self.enable_async:
            raise ValueError('async DMA is disabled.')

        # init state
        start_state = 0
        self.dma_fsm.set_index(start_state)

        # start
        next_state = self.dma_fsm_max_state + 1
        self.dma_fsm.If(fsm.state == fsm.current).goto(next_state)
        self.dma_fsm.set_index(next_state)

        # call dma
        self._dma_write(self.dma_fsm, ram, local_addr,
                        global_addr, size, local_stride, port)

        # remember maximum state
        self.dma_fsm_max_state = self.dma_fsm.current

        # reset
        self.dma_fsm.goto_init()

        # wait idle state by master fsm
        self.dma_wait(fsm)

        return 0

    def dma_write_pattern_async(self, fsm, ram, local_addr, global_addr, pattern,
                                port=0):
        if not self.enable_async:
            raise ValueError('async DMA is disabled.')

        # init state
        start_state = 0
        self.dma_fsm.set_index(start_state)

        # start
        next_state = self.dma_fsm_max_state + 1
        self.dma_fsm.If(fsm.state == fsm.current).goto(next_state)
        self.dma_fsm.set_index(next_state)

        # call dma
        self._dma_write_pattern(self.dma_fsm, ram, local_addr, global_addr,
                                pattern, port)

        # remember maximum state
        self.dma_fsm_max_state = self.dma_fsm.current

        # reset
        self.dma_fsm.goto_init()

        # wait idle state by master fsm
        self.dma_wait(fsm)

        return 0

    def dma_write_multidim_async(self, fsm, ram, local_addr, global_addr, shape,
                                 order=None, port=0):
        if order is None:
            order = list(range(len(shape)))

        pattern = self._to_pattern(shape, order)
        return self.dma_write_pattern_async(fsm, ram, local_addr, global_addr,
                                            pattern, port)

    def dma_wait(self, fsm):
        if not self.enable_async:
            raise ValueError('async DMA is disabled.')

        start_state = 0
        fsm.If(self.dma_fsm.state == start_state).goto_next()
        return 0

    def dma_idle(self, fsm):
        if not self.enable_async:
            raise ValueError('async DMA is disabled.')

        start_state = 0
        flag = self.dma_fsm.state == start_state
        return flag

    def _to_pattern(self, shape, order):
        pattern = []
        for p in order:
            size = shape[p]
            stride = functools.reduce(lambda x, y: x * y,
                                      shape[:p], 1) if p > 0 else 1
            pattern.append((size, stride))
        return pattern


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
                                           util.log2(length))
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
