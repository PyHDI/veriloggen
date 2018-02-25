from __future__ import absolute_import
from __future__ import print_function

import functools

import veriloggen.core.vtypes as vtypes
import veriloggen.types.util as util
from veriloggen.types.axi import AxiMaster, AxiSlave
from veriloggen.fsm.fsm import FSM

from .ttypes import _MutexFunction
from .ram import RAM, FixedRAM, MultibankRAM


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

        rdata = self.m.TmpReg(self.datawidth, initval=0, signed=True)
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
                  local_stride=1, port=0, ram_method=None):
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
                                  cond=cond, ram_port=port, ram_method=ram_method)

        fsm.If(done).goto_next()

        return 0

    def dma_read_pattern(self, fsm, ram, local_addr, global_addr, pattern,
                         port=0):
        if self.enable_async:
            self.dma_wait(fsm)

        return self._dma_read_pattern(fsm, ram, local_addr, global_addr, pattern,
                                      port)

    def _dma_read_pattern(self, fsm, ram, local_addr, global_addr, pattern,
                          port=0, ram_method=None):
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
                                          cond=cond, ram_port=port, ram_method=ram_method)

        fsm.If(done).goto_next()

        return 0

    def dma_read_multidim(self, fsm, ram, local_addr, global_addr, shape, order=None,
                          port=0):
        if order is None:
            order = list(reversed(range(len(shape))))

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
                   local_stride=1, port=0, ram_method=None):
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
                                   cond=cond, ram_port=port, ram_method=ram_method)

        fsm.If(done).goto_next()

        return 0

    def dma_write_pattern(self, fsm, ram, local_addr, global_addr, pattern,
                          port=0):
        if self.enable_async:
            self.dma_wait(fsm)

        return self._dma_write_pattern(fsm, ram, local_addr, global_addr, pattern,
                                       port)

    def _dma_write_pattern(self, fsm, ram, local_addr, global_addr, pattern,
                           port=0, ram_method=None):
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
                                           cond=cond, ram_port=port, ram_method=ram_method)

        fsm.If(done).goto_next()

        return 0

    def dma_write_multidim(self, fsm, ram, local_addr, global_addr, shape, order=None,
                           port=0):
        if order is None:
            order = list(reversed(range(len(shape))))

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
            order = list(reversed(range(len(shape))))

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
            order = list(reversed(range(len(shape))))

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
                                      shape[p + 1:], 1)
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
                                    width=self.datawidth, initval=0, signed=True)
                         for i in range(length)]
        self.flag = [self.m.Reg('_'.join(['', self.name, 'flag', '%d' % i]), initval=0)
                     for i in range(length)]
        self.resetval = [self.m.Reg('_'.join(['', self.name, 'resetval', '%d' % i]),
                                    width=self.datawidth, initval=0, signed=True)
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

        rdata = self.m.TmpWire(self.datawidth, signed=True)
        pat = [(maskaddr == i, r) for i, r in enumerate(self.register)]
        pat.append((None, vtypes.IntX()))
        rval = vtypes.PatternMux(pat)
        rdata.assign(rval)

        flag = self.m.TmpWire()
        pat = [(maskaddr == i, r) for i, r in enumerate(self.flag)]
        pat.append((None, vtypes.IntX()))
        rval = vtypes.PatternMux(pat)
        flag.assign(rval)

        resetval = self.m.TmpWire(self.datawidth, signed=True)
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

        rdata = self.m.TmpWire(self.datawidth, signed=True)
        pat = [(maskaddr == i, r) for i, r in enumerate(self.register)]
        pat.append((None, vtypes.IntX()))
        rval = vtypes.PatternMux(pat)
        rdata.assign(rval)

        flag = self.m.TmpWire()
        pat = [(maskaddr == i, r) for i, r in enumerate(self.flag)]
        pat.append((None, vtypes.IntX()))
        rval = vtypes.PatternMux(pat)
        flag.assign(rval)

        resetval = self.m.TmpWire(self.datawidth, signed=True)
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
