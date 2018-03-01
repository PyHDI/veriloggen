from __future__ import absolute_import
from __future__ import print_function

import functools
import math

import veriloggen.core.vtypes as vtypes
import veriloggen.types.util as util
from veriloggen.seq.seq import Seq, TmpSeq
from veriloggen.fsm.fsm import FSM, TmpFSM
from veriloggen.types.axi import AxiMaster, AxiSlave
from veriloggen.optimizer import try_optimize as optimize
from veriloggen.dataflow.dtypes import make_condition

from .ttypes import _MutexFunction
from .ram import RAM, FixedRAM, MultibankRAM


class AXIM(AxiMaster, _MutexFunction):
    """ AXI Master Interface with DMA controller """

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

        cond = self._fsm_start(fsm)

        dma_fsm, done = self.dma_read_rtl(ram, req_local_addr, req_global_addr, req_size,
                                          local_stride=req_local_stride, port=port,
                                          cond=cond, ram_method=ram_method)
        fsm.goto_next()
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

        cond = self._fsm_start(fsm)

        dma_fsm, done = self.dma_read_rtl_pattern(ram, req_local_addr, req_global_addr, req_pattern,
                                                  port=port, cond=cond, ram_method=ram_method)

        fsm.goto_next()
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

        cond = self._fsm_start(fsm)

        dma_fsm, done = self.dma_write_rtl(ram, req_local_addr, req_global_addr, req_size,
                                           local_stride=req_local_stride, port=port,
                                           cond=cond, ram_method=ram_method)
        fsm.goto_next()
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

        cond = self._fsm_start(fsm)

        dma_fsm, done = self.dma_write_rtl_pattern(ram, req_local_addr, req_global_addr, req_pattern,
                                                   port=port, cond=cond, ram_method=ram_method)
        fsm.goto_next()
        fsm.If(done).goto_next()

        return 0

    def dma_write_multidim(self, fsm, ram, local_addr, global_addr, shape, order=None,
                           port=0):
        if order is None:
            order = list(reversed(range(len(shape))))

        pattern = self._to_pattern(shape, order)
        return self.dma_write_pattern(fsm, ram, local_addr, global_addr, pattern, port)

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
        return self.dma_write_pattern_async(fsm, ram, local_addr, global_addr, pattern, port)

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

    #-------------------
    # Low-level (RTL) APIs
    #-------------------
    def dma_read_rtl(self, ram, local_addr, global_addr, size,
                     local_stride, port=0, cond=None, ram_method=None):
        """ Safe API with length and 4KB boundary check """

        ram_datawidth = (ram.datawidth if ram_method is None else
                         ram.orig_datawidth if 'bcast' in ram_method.func.__name__ else
                         ram.orig_datawidth if 'block' in ram_method.func.__name__ else
                         ram.datawidth)

        if vtypes.equals(self.datawidth, ram_datawidth):
            return self._dma_read_rtl_same(ram, local_addr, global_addr, size,
                                           local_stride, port, cond, ram_method)

        comp = self.datawidth < ram_datawidth
        if not isinstance(comp, bool):
            raise ValueError('datawidth must be int, not (%s, %s)' %
                             (type(self.datawidth, ram_datawidth)))

        if comp:
            return self._dma_read_rtl_narrow(ram, local_addr, global_addr, size,
                                             local_stride, port, cond, ram_method,
                                             ram_datawidth)

        return self._dma_read_rtl_wide(ram, local_addr, global_addr, size,
                                       local_stride, port, cond, ram_method,
                                       ram_datawidth)

    def _dma_read_rtl_same(self, ram, local_addr, global_addr, size,
                           local_stride, port=0, cond=None, ram_method=None):
        fsm = TmpFSM(self.m, self.clk, self.rst)

        if cond is not None:
            fsm.If(cond).goto_next()

        req_global_addr = self.m.TmpReg(self.addrwidth, initval=0)
        req_size = self.m.TmpReg(size.bit_length() + 1, initval=0)
        rest_size = self.m.TmpReg(size.bit_length() + 1, initval=0)
        max_burstlen = 2 ** self.burst_size_width

        fsm(
            req_global_addr(self.mask_addr(global_addr)),
            rest_size(size)
        )

        wdata = self.m.TmpReg(ram.datawidth, initval=0)
        wvalid = self.m.TmpReg(initval=0)
        df_data = self.df.Variable(
            wdata, wvalid, width=ram.datawidth, signed=False)

        if ram_method is None:
            ram_method = getattr(ram, 'write_dataflow')

        done = ram_method(port, local_addr, df_data, size,
                          stride=local_stride, cond=fsm)
        fsm.goto_next()

        check_state = fsm.current

        self._check_4KB_boundary(fsm, max_burstlen,
                                 req_global_addr, req_size, rest_size)

        ack, counter = self.read_request(req_global_addr, req_size, cond=fsm)
        fsm.If(ack).goto_next()

        data, valid, last = self.read_data(cond=fsm)

        fsm.Delay(1)(
            wvalid(0)
        )
        fsm.If(valid)(
            wdata(data),
            wvalid(1),
        )

        fsm.If(valid, last)(
            req_global_addr.add(optimize(req_size * (self.datawidth // 8)))
        )
        fsm.If(valid, last, rest_size > 0).goto(check_state)
        fsm.If(valid, last, rest_size == 0).goto_next()

        done = self._fsm_done(fsm)

        return fsm, done

    def _dma_read_rtl_narrow(self, ram, local_addr, global_addr, size,
                             local_stride, port=0, cond=None, ram_method=None,
                             ram_datawidth=None):
        """ axi.datawidth < ram.datawidth """

        if ram_datawidth is None:
            ram_datawidth = ram.datawidth

        if ram_datawidth % self.datawidth != 0:
            raise ValueError(
                'ram_datawidth must be multiple number of axi.datawidth')

        pack_size = ram_datawidth // self.datawidth
        dma_size = (size << int(math.log(pack_size, 2))
                    if math.log(pack_size, 2) % 1.0 == 0.0 else
                    size * pack_size)

        fsm = TmpFSM(self.m, self.clk, self.rst)

        if cond is not None:
            fsm.If(cond).goto_next()

        req_global_addr = self.m.TmpReg(self.addrwidth, initval=0)
        req_size = self.m.TmpReg(dma_size.bit_length() + 1, initval=0)
        rest_size = self.m.TmpReg(dma_size.bit_length() + 1, initval=0)
        max_burstlen = 2 ** self.burst_size_width

        fsm(
            req_global_addr(self.mask_addr(global_addr)),
            rest_size(dma_size)
        )

        wdata = self.m.TmpReg(ram_datawidth, initval=0)
        wvalid = self.m.TmpReg(initval=0)
        df_data = self.df.Variable(
            wdata, wvalid, width=ram_datawidth, signed=False)

        if ram_method is None:
            ram_method = getattr(ram, 'write_dataflow')

        done = ram_method(port, local_addr, df_data, size,
                          stride=local_stride, cond=fsm)
        fsm.goto_next()

        check_state = fsm.current

        self._check_4KB_boundary(fsm, max_burstlen,
                                 req_global_addr, req_size, rest_size)

        ack, counter = self.read_request(req_global_addr, req_size, cond=fsm)
        fsm.If(ack).goto_next()

        pack_count = self.m.TmpReg(pack_size, initval=0)
        data, valid, last = self.read_data(cond=fsm)

        fsm.Delay(1)(
            wvalid(0)
        )
        fsm.If(valid)(
            wdata(vtypes.Cat(data, wdata[self.datawidth:ram_datawidth])),
            wvalid(0),
            pack_count.inc()
        )
        fsm.If(valid, pack_count == pack_size - 1)(
            wdata(vtypes.Cat(data, wdata[self.datawidth:ram_datawidth])),
            wvalid(1),
            pack_count(0)
        )

        fsm.If(valid, last)(
            req_global_addr.add(optimize(req_size * (self.datawidth // 8)))
        )
        fsm.If(valid, last, rest_size > 0).goto(check_state)
        fsm.If(valid, last, rest_size == 0).goto_next()

        done = self._fsm_done(fsm)

        return fsm, done

    def _dma_read_rtl_wide(self, ram, local_addr, global_addr, size,
                           local_stride, port=0, cond=None, ram_method=None,
                           ram_datawidth=None):
        """ axi.datawidth > ram.datawidth """

        if ram_datawidth is None:
            ram_datawidth = ram.datawidth

        if self.datawidth % ram_datawidth != 0:
            raise ValueError(
                'axi.datawidth must be multiple number of ram_datawidth')

        pack_size = self.datawidth // ram_datawidth
        dma_size = (size >> int(math.log(pack_size, 2))
                    if math.log(pack_size, 2) % 1.0 == 0.0 else
                    int(size // pack_size))

        fsm = TmpFSM(self.m, self.clk, self.rst)

        if cond is not None:
            fsm.If(cond).goto_next()

        req_global_addr = self.m.TmpReg(self.addrwidth, initval=0)
        req_size = self.m.TmpReg(dma_size.bit_length() + 1, initval=0)
        rest_size = self.m.TmpReg(dma_size.bit_length() + 1, initval=0)
        max_burstlen = 2 ** self.burst_size_width

        fsm(
            req_global_addr(self.mask_addr(global_addr)),
            rest_size(dma_size)
        )

        wdata = self.m.TmpReg(self.datawidth, initval=0)
        wdata_ram = self.m.TmpWire(ram_datawidth)
        wdata_ram.assign(wdata)
        wvalid = self.m.TmpReg(initval=0)
        df_data = self.df.Variable(
            wdata_ram, wvalid, width=ram_datawidth, signed=False)

        if ram_method is None:
            ram_method = getattr(ram, 'write_dataflow')

        done = ram_method(port, local_addr, df_data, size,
                          stride=local_stride, cond=fsm)
        fsm.goto_next()

        check_state = fsm.current

        last_done = self.m.TmpReg(initval=0)
        fsm(
            last_done(0)
        )

        self._check_4KB_boundary(fsm, max_burstlen,
                                 req_global_addr, req_size, rest_size)

        ack, counter = self.read_request(req_global_addr, req_size, cond=fsm)
        fsm.If(ack).goto_next()

        pack_count = self.m.TmpReg(pack_size, initval=0)
        rcond = make_condition(fsm, pack_count == 0)
        data, valid, last = self.read_data(cond=rcond)

        fsm.Delay(1)(
            wvalid(0)
        )
        fsm.If(pack_count == 0, valid, last)(
            last_done(1)
        )
        fsm.If(pack_count == 0, valid)(
            wdata(data),
            wvalid(1),
            pack_count.inc()
        )
        fsm.If(pack_count > 0)(
            wdata(wdata >> ram_datawidth),
            wvalid(1),
            pack_count.inc()
        )
        fsm.If(pack_count == pack_size - 1)(
            pack_count(0)
        )

        fsm.If(last_done, pack_count == pack_size - 1)(
            req_global_addr.add(optimize(req_size * (self.datawidth // 8)))
        )
        fsm.If(last_done, pack_count == pack_size -
               1, rest_size > 0).goto(check_state)
        fsm.If(last_done, pack_count == pack_size -
               1, rest_size == 0).goto_next()

        done = self._fsm_done(fsm)

        return fsm, done

    def dma_read_rtl_pattern(self, ram, local_addr, global_addr, pattern,
                             port=0, cond=None, ram_method=None):

        ram_datawidth = (ram.datawidth if ram_method is None else
                         ram.orig_datawidth if 'bcast' in ram_method.func.__name__ else
                         ram.orig_datawidth if 'block' in ram_method.func.__name__ else
                         ram.datawidth)

        if vtypes.equals(self.datawidth, ram_datawidth):
            return self._dma_read_rtl_pattern_same(ram, local_addr, global_addr, pattern,
                                                   port, cond, ram_method)

        comp = self.datawidth < ram_datawidth
        if not isinstance(comp, bool):
            raise ValueError('datawidth must be int, not (%s, %s)' %
                             (type(self.datawidth, ram_datawidth)))

        if comp:
            return self._dma_read_rtl_pattern_narrow(ram, local_addr, global_addr, pattern,
                                                     port, cond, ram_method,
                                                     ram_datawidth)

        return self._dma_read_rtl_pattern_wide(ram, local_addr, global_addr, pattern,
                                               port, cond, ram_method,
                                               ram_datawidth)

    def _dma_read_rtl_pattern_same(self, ram, local_addr, global_addr, pattern,
                                   port=0, cond=None, ram_method=None):

        block_size = pattern[0][0]

        fsm = TmpFSM(self.m, self.clk, self.rst)

        if cond is not None:
            fsm.If(cond).goto_next()

        req_global_addr = self.m.TmpReg(self.addrwidth, initval=0)
        req_size = self.m.TmpReg(block_size.bit_length() + 1, initval=0)
        rest_size = self.m.TmpReg(block_size.bit_length() + 1, initval=0)
        max_burstlen = 2 ** self.burst_size_width

        fsm(
            req_global_addr(self.mask_addr(global_addr)),
            rest_size(block_size)
        )

        count_list = [self.m.TmpReg(size.bit_length() + 1, initval=0)
                      for size, stride in pattern[1:]]

        for count, (size, stride) in zip(count_list, pattern[1:]):
            fsm(
                count(size - 1)
            )

        wdata = self.m.TmpReg(ram.datawidth, initval=0)
        wvalid = self.m.TmpReg(initval=0)
        df_data = self.df.Variable(
            wdata, wvalid, width=ram.datawidth, signed=False)

        if ram_method is None:
            ram_method = getattr(ram, 'write_dataflow_pattern')

        done = ram_method(port, local_addr, df_data, pattern, cond=fsm)

        fsm.goto_next()

        check_state = fsm.current

        self._check_4KB_boundary(fsm, max_burstlen,
                                 req_global_addr, req_size, rest_size)

        ack, counter = self.read_request(req_global_addr, req_size, cond=fsm)
        fsm.If(ack).goto_next()

        data, valid, last = self.read_data(cond=fsm)

        fsm.Delay(1)(
            wvalid(0)
        )
        fsm.If(valid)(
            wdata(data),
            wvalid(1),
        )

        fsm.If(valid, last)(
            req_global_addr.add(optimize(req_size * (self.datawidth // 8)))
        )

        update_count = rest_size == 0
        for count, (size, stride) in zip(count_list, pattern[1:]):
            fsm.If(valid, last, update_count)(
                count.dec()
            )
            fsm.If(valid, last, update_count, count == 0)(
                count(size - 1)
            )
            update_count = vtypes.Ands(update_count, count == 0)

        fsm.If(valid, last, rest_size == 0, vtypes.Not(update_count))(
            rest_size(block_size)
        )
        fsm.If(valid, last, rest_size > 0).goto(check_state)
        fsm.If(valid, last, rest_size == 0, vtypes.Not(
            update_count)).goto(check_state)
        fsm.If(valid, last, update_count).goto_next()

        done = self._fsm_done(fsm)

        return fsm, done

    def _dma_read_rtl_pattern_narrow(self, ram, local_addr, global_addr, pattern,
                                     port=0, cond=None, ram_method=None,
                                     ram_datawidth=None):
        """ axi.datawidth < ram.datawidth """

        if ram_datawidth is None:
            ram_datawidth = ram.datawidth

        if ram_datawidth % self.datawidth != 0:
            raise ValueError(
                'ram_datawidth must be multiple number of axi.datawidth')

        block_size = pattern[0][0]

        pack_size = ram_datawidth // self.datawidth
        dma_size = (block_size << int(math.log(pack_size, 2))
                    if math.log(pack_size, 2) % 1.0 == 0.0 else
                    block_size * pack_size)

        fsm = TmpFSM(self.m, self.clk, self.rst)

        if cond is not None:
            fsm.If(cond).goto_next()

        req_global_addr = self.m.TmpReg(self.addrwidth, initval=0)
        req_size = self.m.TmpReg(dma_size.bit_length() + 1, initval=0)
        rest_size = self.m.TmpReg(dma_size.bit_length() + 1, initval=0)
        max_burstlen = 2 ** self.burst_size_width

        fsm(
            req_global_addr(self.mask_addr(global_addr)),
            rest_size(dma_size)
        )

        count_list = [self.m.TmpReg(size.bit_length() + 1, initval=0)
                      for size, stride in pattern[1:]]

        for count, (size, stride) in zip(count_list, pattern[1:]):
            fsm(
                count(size - 1)
            )

        wdata = self.m.TmpReg(ram_datawidth, initval=0)
        wvalid = self.m.TmpReg(initval=0)
        df_data = self.df.Variable(
            wdata, wvalid, width=ram_datawidth, signed=False)

        if ram_method is None:
            ram_method = getattr(ram, 'write_dataflow_pattern')

        done = ram_method(port, local_addr, df_data, pattern, cond=fsm)
        fsm.goto_next()

        check_state = fsm.current

        self._check_4KB_boundary(fsm, max_burstlen,
                                 req_global_addr, req_size, rest_size)

        ack, counter = self.read_request(req_global_addr, req_size, cond=fsm)
        fsm.If(ack).goto_next()

        pack_count = self.m.TmpReg(pack_size, initval=0)
        data, valid, last = self.read_data(cond=fsm)

        fsm.Delay(1)(
            wvalid(0)
        )
        fsm.If(valid)(
            wdata(vtypes.Cat(data, wdata[self.datawidth:ram_datawidth])),
            wvalid(0),
            pack_count.inc()
        )
        fsm.If(valid, pack_count == pack_size - 1)(
            wdata(vtypes.Cat(data, wdata[self.datawidth:ram_datawidth])),
            wvalid(1),
            pack_count(0)
        )

        fsm.If(valid, last)(
            req_global_addr.add(optimize(req_size * (self.datawidth // 8)))
        )

        update_count = rest_size == 0
        for count, (size, stride) in zip(count_list, pattern[1:]):
            fsm.If(valid, last, update_count)(
                count.dec()
            )
            fsm.If(valid, last, update_count, count == 0)(
                count(size - 1)
            )
            update_count = vtypes.Ands(update_count, count == 0)

        fsm.If(valid, last, rest_size == 0, vtypes.Not(update_count))(
            rest_size(dma_size)
        )
        fsm.If(valid, last, rest_size > 0).goto(check_state)
        fsm.If(valid, last, rest_size == 0, vtypes.Not(
            update_count)).goto(check_state)
        fsm.If(valid, last, update_count).goto_next()

        done = self._fsm_done(fsm)

        return fsm, done

    def _dma_read_rtl_pattern_wide(self, ram, local_addr, global_addr, pattern,
                                   port=0, cond=None, ram_method=None,
                                   ram_datawidth=None):
        """ axi.datawidth > ram.datawidth """

        if ram_datawidth is None:
            ram_datawidth = ram.datawidth

        if self.datawidth % ram_datawidth != 0:
            raise ValueError(
                'axi.datawidth must be multiple number of ram_datawidth')

        block_size = pattern[0][0]

        pack_size = self.datawidth // ram_datawidth
        dma_size = (block_size >> int(math.log(pack_size, 2))
                    if math.log(pack_size, 2) % 1.0 == 0.0 else
                    int(block_size // pack_size))

        fsm = TmpFSM(self.m, self.clk, self.rst)

        if cond is not None:
            fsm.If(cond).goto_next()

        req_global_addr = self.m.TmpReg(self.addrwidth, initval=0)
        req_size = self.m.TmpReg(dma_size.bit_length() + 1, initval=0)
        rest_size = self.m.TmpReg(dma_size.bit_length() + 1, initval=0)
        max_burstlen = 2 ** self.burst_size_width

        fsm(
            req_global_addr(self.mask_addr(global_addr)),
            rest_size(dma_size)
        )

        count_list = [self.m.TmpReg(size.bit_length() + 1, initval=0)
                      for size, stride in pattern[1:]]

        for count, (size, stride) in zip(count_list, pattern[1:]):
            fsm(
                count(size - 1)
            )

        wdata = self.m.TmpReg(self.datawidth, initval=0)
        wdata_ram = self.m.TmpWire(ram_datawidth)
        wdata_ram.assign(wdata)
        wvalid = self.m.TmpReg(initval=0)
        df_data = self.df.Variable(
            wdata_ram, wvalid, width=ram_datawidth, signed=False)

        if ram_method is None:
            ram_method = getattr(ram, 'write_dataflow_pattern')

        done = ram_method(port, local_addr, df_data, pattern, cond=fsm)
        fsm.goto_next()

        check_state = fsm.current

        last_done = self.m.TmpReg(initval=0)
        fsm(
            last_done(0)
        )

        self._check_4KB_boundary(fsm, max_burstlen,
                                 req_global_addr, req_size, rest_size)

        ack, counter = self.read_request(req_global_addr, req_size, cond=fsm)
        fsm.If(ack).goto_next()

        pack_count = self.m.TmpReg(pack_size, initval=0)
        rcond = make_condition(fsm, pack_count == 0)
        data, valid, last = self.read_data(cond=rcond)

        fsm.Delay(1)(
            wvalid(0)
        )
        fsm.If(pack_count == 0, valid, last)(
            last_done(1)
        )
        fsm.If(pack_count == 0, valid)(
            wdata(data),
            wvalid(1),
            pack_count.inc()
        )
        fsm.If(pack_count > 0)(
            wdata(wdata >> ram_datawidth),
            wvalid(1),
            pack_count.inc()
        )
        fsm.If(pack_count == pack_size - 1)(
            pack_count(0)
        )

        fsm.If(last_done, pack_count == pack_size - 1)(
            req_global_addr.add(optimize(req_size * (self.datawidth // 8)))
        )

        update_count = rest_size == 0
        for count, (size, stride) in zip(count_list, pattern[1:]):
            fsm.If(last_done, pack_count == pack_size - 1, update_count)(
                count.dec()
            )
            fsm.If(last_done, pack_count == pack_size - 1, update_count, count == 0)(
                count(size - 1)
            )
            update_count = vtypes.Ands(update_count, count == 0)

        fsm.If(last_done, pack_count == pack_size - 1, rest_size == 0,
               vtypes.Not(update_count))(
            rest_size(dma_size)
        )
        fsm.If(last_done, pack_count == pack_size -
               1, rest_size > 0).goto(check_state)
        fsm.If(last_done, pack_count == pack_size - 1, rest_size == 0,
               vtypes.Not(update_count)).goto(check_state)
        fsm.If(last_done, pack_count == pack_size - 1,
               update_count).goto_next()

        done = self._fsm_done(fsm)

        return fsm, done

    def dma_read_rtl_multidim(self, ram, local_addr, global_addr, shape, order=None,
                              port=0, cond=None, ram_method=None):

        if order is None:
            order = list(reversed(range(len(shape))))

        pattern = self._to_pattern(shape, order)
        return self.dma_read_rtl_pattern(ram, local_addr, global_addr, pattern,
                                         port, cond, ram_method)

    def _to_pattern(self, shape, order):
        pattern = []
        for p in order:
            if not isinstance(p, int):
                raise TypeError(
                    "Values of 'order' must be 'int', not %s" % str(type(p)))
            size = shape[p]
            basevalue = 1 if isinstance(size, int) else vtypes.Int(1)
            stride = functools.reduce(lambda x, y: x * y,
                                      shape[p + 1:], basevalue)
            pattern.append((size, stride))
        return pattern

    def dma_read_rtl_unsafe(self, ram, local_addr, global_addr, size,
                            local_stride, port=0, cond=None, ram_method=None):
        """ Unsafe API with no length and 4KB region check """

        ram_datawidth = (ram.datawidth if ram_method is None else
                         ram.orig_datawidth if 'bcast' in ram_method.func.__name__ else
                         ram.orig_datawidth if 'block' in ram_method.func.__name__ else
                         ram.datawidth)

        if vtypes.equals(self.datawidth, ram_datawidth):
            return self._dma_read_rtl_unsafe_same(ram, local_addr, global_addr, size,
                                                  local_stride, port, cond, ram_method)

        comp = self.datawidth < ram_datawidth
        if not isinstance(comp, bool):
            raise ValueError('datawidth must be int, not (%s, %s)' %
                             (type(self.datawidth, ram_datawidth)))

        if comp:
            return self._dma_read_rtl_unsafe_narrow(ram, local_addr, global_addr, size,
                                                    local_stride, port, cond, ram_method,
                                                    ram_datawidth)

        return self._dma_read_rtl_unsafe_wide(ram, local_addr, global_addr, size,
                                              local_stride, port, cond, ram_method,
                                              ram_datawidth)

    def _dma_read_rtl_unsafe_same(self, ram, local_addr, global_addr, size,
                                  local_stride, port=0, cond=None, ram_method=None):
        fsm = TmpFSM(self.m, self.clk, self.rst)

        if cond is not None:
            fsm.If(cond).goto_next()

        ack, counter = self.read_request(global_addr, size, cond=fsm)
        fsm.If(ack).goto_next()

        wdata = self.m.TmpReg(ram.datawidth, initval=0)
        wvalid = self.m.TmpReg(initval=0)
        df_data = self.df.Variable(
            wdata, wvalid, width=ram.datawidth, signed=False)

        if ram_method is None:
            ram_method = getattr(ram, 'write_dataflow')

        done = ram_method(port, local_addr, df_data, size,
                          stride=local_stride, cond=fsm)
        fsm.goto_next()

        data, valid, last = self.read_data(cond=fsm)

        fsm(
            wvalid(0)
        )
        fsm.If(valid)(
            wdata(data),
            wvalid(1),
        )

        fsm.If(done).goto_init()

        return fsm, done

    def _dma_read_rtl_unsafe_narrow(self, ram, local_addr, global_addr, size,
                                    local_stride, port=0, cond=None, ram_method=None,
                                    ram_datawidth=None):
        """ axi.datawidth < ram.datawidth """

        if ram_datawidth is None:
            ram_datawidth = ram.datawidth

        if ram_datawidth % self.datawidth != 0:
            raise ValueError(
                'ram_datawidth must be multiple number of axi.datawidth')

        pack_size = ram_datawidth // self.datawidth
        dma_size = (size << int(math.log(pack_size, 2))
                    if math.log(pack_size, 2) % 1.0 == 0.0 else
                    size * pack_size)

        fsm = TmpFSM(self.m, self.clk, self.rst)

        if cond is not None:
            fsm.If(cond).goto_next()

        ack, counter = self.read_request(global_addr, dma_size, cond=fsm)
        fsm.If(ack).goto_next()

        wdata = self.m.TmpReg(ram_datawidth, initval=0)
        wvalid = self.m.TmpReg(initval=0)
        df_data = self.df.Variable(
            wdata, wvalid, width=ram_datawidth, signed=False)

        if ram_method is None:
            ram_method = getattr(ram, 'write_dataflow')

        done = ram_method(port, local_addr, df_data, size,
                          stride=local_stride, cond=fsm)
        fsm.goto_next()

        pack_count = self.m.TmpReg(pack_size, initval=0)
        data, valid, last = self.read_data(cond=fsm)

        fsm(
            wvalid(0)
        )
        fsm.If(valid)(
            wdata(vtypes.Cat(data, wdata[self.datawidth:ram_datawidth])),
            wvalid(0),
            pack_count.inc()
        )
        fsm.If(valid, pack_count == pack_size - 1)(
            wdata(vtypes.Cat(data, wdata[self.datawidth:ram_datawidth])),
            wvalid(1),
            pack_count(0)
        )

        fsm.If(done).goto_init()

        return fsm, done

    def _dma_read_rtl_unsafe_wide(self, ram, local_addr, global_addr, size,
                                  local_stride, port=0, cond=None, ram_method=None,
                                  ram_datawidth=None):
        """ axi.datawidth > ram.datawidth """

        if ram_datawidth is None:
            ram_datawidth = ram.datawidth

        if self.datawidth % ram_datawidth != 0:
            raise ValueError(
                'axi.datawidth must be multiple number of ram_datawidth')

        pack_size = self.datawidth // ram_datawidth
        dma_size = (size >> int(math.log(pack_size, 2))
                    if math.log(pack_size, 2) % 1.0 == 0.0 else
                    int(size // pack_size))

        fsm = TmpFSM(self.m, self.clk, self.rst)

        if cond is not None:
            fsm.If(cond).goto_next()

        ack, counter = self.read_request(global_addr, dma_size, cond=fsm)
        fsm.If(ack).goto_next()

        wdata = self.m.TmpReg(self.datawidth, initval=0)
        wdata_ram = self.m.TmpWire(ram_datawidth)
        wdata_ram.assign(wdata)
        wvalid = self.m.TmpReg(initval=0)
        df_data = self.df.Variable(
            wdata_ram, wvalid, width=ram_datawidth, signed=False)

        if ram_method is None:
            ram_method = getattr(ram, 'write_dataflow')

        done = ram_method(port, local_addr, df_data, size,
                          stride=local_stride, cond=fsm)
        fsm.goto_next()

        pack_count = self.m.TmpReg(pack_size, initval=0)
        rcond = make_condition(fsm, pack_count == 0)
        data, valid, last = self.read_data(cond=rcond)

        fsm(
            wvalid(0)
        )
        fsm.If(pack_count == 0, valid)(
            wdata(data),
            wvalid(1),
            pack_count.inc()
        )
        fsm.If(pack_count > 0)(
            wdata(wdata >> ram_datawidth),
            wvalid(1),
            pack_count.inc()
        )
        fsm.If(pack_count == pack_size - 1)(
            pack_count(0)
        )

        fsm.If(done).goto_init()

        return fsm, done

    def dma_write_rtl(self, ram, local_addr, global_addr, size,
                      local_stride, port=0, cond=None, ram_method=None):
        """ Safe API with length and 4KB boundary check """

        ram_datawidth = (ram.datawidth if ram_method is None else
                         ram.orig_datawidth if 'block' in ram_method.func.__name__ else
                         ram.datawidth)

        if vtypes.equals(self.datawidth, ram_datawidth):
            return self._dma_write_rtl_same(ram, local_addr, global_addr, size,
                                            local_stride, port, cond, ram_method)

        comp = self.datawidth < ram_datawidth
        if not isinstance(comp, bool):
            raise ValueError('datawidth must be int, not (%s, %s)' %
                             (type(self.datawidth, ram_datawidth)))

        if comp:
            return self._dma_write_rtl_narrow(ram, local_addr, global_addr, size,
                                              local_stride, port, cond, ram_method,
                                              ram_datawidth)

        return self._dma_write_rtl_wide(ram, local_addr, global_addr, size,
                                        local_stride, port, cond, ram_method,
                                        ram_datawidth)

    def _dma_write_rtl_same(self, ram, local_addr, global_addr, size,
                            local_stride, port=0, cond=None, ram_method=None):

        fsm = TmpFSM(self.m, self.clk, self.rst)

        if cond is not None:
            fsm.If(cond).goto_next()

        req_global_addr = self.m.TmpReg(self.addrwidth, initval=0)
        req_size = self.m.TmpReg(size.bit_length() + 1, initval=0)
        rest_size = self.m.TmpReg(size.bit_length() + 1, initval=0)
        max_burstlen = 2 ** self.burst_size_width

        fsm(
            req_global_addr(self.mask_addr(global_addr)),
            rest_size(size)
        )

        if ram_method is None:
            ram_method = getattr(ram, 'read_dataflow')

        data, last, done = ram_method(port, local_addr, size,
                                      stride=local_stride, cond=fsm, signed=False)
        fsm.goto_next()

        check_state = fsm.current

        self._check_4KB_boundary(fsm, max_burstlen,
                                 req_global_addr, req_size, rest_size)

        ack, counter = self.write_request(req_global_addr, req_size, cond=fsm)
        fsm.If(ack).goto_next()

        done = self.write_dataflow(data, counter, cond=fsm)

        fsm.If(done)(
            req_global_addr.add(optimize(req_size * (self.datawidth // 8)))
        )
        fsm.If(done, rest_size > 0).goto(check_state)
        fsm.If(done, rest_size == 0).goto_next()

        done = self._fsm_done(fsm)

        return fsm, done

    def _dma_write_rtl_narrow(self, ram, local_addr, global_addr, size,
                              local_stride, port=0, cond=None, ram_method=None,
                              ram_datawidth=None):
        """ axi.datawidth < ram.datawidth """

        if ram_datawidth is None:
            ram_datawidth = ram.datawidth

        if ram_datawidth % self.datawidth != 0:
            raise ValueError(
                'ram_datawidth must be multiple number of axi.datawidth')

        pack_size = ram_datawidth // self.datawidth
        dma_size = (size << int(math.log(pack_size, 2))
                    if math.log(pack_size, 2) % 1.0 == 0.0 else
                    size * pack_size)

        fsm = TmpFSM(self.m, self.clk, self.rst)

        if cond is not None:
            fsm.If(cond).goto_next()

        req_global_addr = self.m.TmpReg(self.addrwidth, initval=0)
        req_size = self.m.TmpReg(dma_size.bit_length() + 1, initval=0)
        rest_size = self.m.TmpReg(dma_size.bit_length() + 1, initval=0)
        max_burstlen = 2 ** self.burst_size_width

        fsm(
            req_global_addr(self.mask_addr(global_addr)),
            rest_size(dma_size)
        )

        if ram_method is None:
            ram_method = getattr(ram, 'read_dataflow')

        data, last, done = ram_method(port, local_addr, size,
                                      stride=local_stride, cond=fsm, signed=False)
        fsm.goto_next()

        check_state = fsm.current

        self._check_4KB_boundary(fsm, max_burstlen,
                                 req_global_addr, req_size, rest_size)

        ack, counter = self.write_request(req_global_addr, req_size, cond=fsm)
        fsm.If(ack).goto_next()

        wdata = self.m.TmpReg(ram_datawidth, initval=0)
        wvalid = self.m.TmpReg(initval=0)
        wready = self.m.TmpWire()
        ack = vtypes.Ors(wready, vtypes.Not(wvalid))

        pack_count = self.m.TmpReg(pack_size, initval=0)
        rcond = make_condition(fsm, ack, pack_count == 0)
        rdata, rvalid = data.read(cond=rcond)

        seq = TmpSeq(self.m, self.clk, self.rst)
        seq.If(ack)(
            wvalid(0)
        )
        seq.If(rvalid)(
            wdata(rdata),
            wvalid(1),
            pack_count.inc()
        )
        seq.If(ack, pack_count > 0)(
            wdata(wdata >> self.datawidth),
            wvalid(1),
            pack_count.inc()
        )
        seq.If(ack, pack_count == pack_size - 1)(
            wdata(wdata >> self.datawidth),
            wvalid(1),
            pack_count(0)
        )

        df_data = self.df.Variable(
            wdata, wvalid, wready, width=self.datawidth, signed=False)

        done = self.write_dataflow(df_data, counter, cond=fsm)

        fsm.If(done)(
            req_global_addr.add(optimize(req_size * (self.datawidth // 8)))
        )
        fsm.If(done, rest_size > 0).goto(check_state)
        fsm.If(done, rest_size == 0).goto_next()

        done = self._fsm_done(fsm)

        return fsm, done

    def _dma_write_rtl_wide(self, ram, local_addr, global_addr, size,
                            local_stride, port=0, cond=None, ram_method=None,
                            ram_datawidth=None):
        """ axi.datawidth > ram.datawidth """

        if ram_datawidth is None:
            ram_datawidth = ram.datawidth

        if self.datawidth % ram_datawidth != 0:
            raise ValueError(
                'axi.datawidth must be multiple number of ram_datawidth')

        pack_size = self.datawidth // ram_datawidth
        dma_size = (size >> int(math.log(pack_size, 2))
                    if math.log(pack_size, 2) % 1.0 == 0.0 else
                    int(size // pack_size))

        fsm = TmpFSM(self.m, self.clk, self.rst)

        if cond is not None:
            fsm.If(cond).goto_next()

        req_global_addr = self.m.TmpReg(self.addrwidth, initval=0)
        req_size = self.m.TmpReg(dma_size.bit_length() + 1, initval=0)
        rest_size = self.m.TmpReg(dma_size.bit_length() + 1, initval=0)
        max_burstlen = 2 ** self.burst_size_width

        fsm(
            req_global_addr(self.mask_addr(global_addr)),
            rest_size(dma_size)
        )

        if ram_method is None:
            ram_method = getattr(ram, 'read_dataflow')

        data, last, done = ram_method(port, local_addr, size,
                                      stride=local_stride, cond=fsm, signed=False)
        fsm.goto_next()

        check_state = fsm.current

        self._check_4KB_boundary(fsm, max_burstlen,
                                 req_global_addr, req_size, rest_size)

        ack, counter = self.write_request(req_global_addr, req_size, cond=fsm)
        fsm.If(ack).goto_next()

        wdata = self.m.TmpReg(self.datawidth, initval=0)
        wvalid = self.m.TmpReg(initval=0)
        wready = self.m.TmpWire()
        ack = vtypes.Ors(wready, vtypes.Not(wvalid))

        pack_count = self.m.TmpReg(pack_size, initval=0)
        rcond = make_condition(fsm, ack)
        rdata, rvalid = data.read(cond=rcond)

        seq = TmpSeq(self.m, self.clk, self.rst)
        seq.If(ack)(
            wvalid(0)
        )
        seq.If(rvalid)(
            wdata(vtypes.Cat(rdata, wdata[ram_datawidth:self.datawidth])),
            wvalid(0),
            pack_count.inc()
        )
        seq.If(rvalid, pack_count == pack_size - 1)(
            wdata(vtypes.Cat(rdata, wdata[ram_datawidth:self.datawidth])),
            wvalid(1),
            pack_count(0)
        )

        df_data = self.df.Variable(
            wdata, wvalid, wready, width=self.datawidth, signed=False)

        done = self.write_dataflow(df_data, counter, cond=fsm)

        fsm.If(done)(
            req_global_addr.add(optimize(req_size * (self.datawidth // 8)))
        )
        fsm.If(done, rest_size > 0).goto(check_state)
        fsm.If(done, rest_size == 0).goto_next()

        done = self._fsm_done(fsm)

        return fsm, done

    def dma_write_rtl_pattern(self, ram, local_addr, global_addr, pattern,
                              port=0, cond=None, ram_method=None):

        ram_datawidth = (ram.datawidth if ram_method is None else
                         ram.orig_datawidth if 'block' in ram_method.func.__name__ else
                         ram.datawidth)

        if vtypes.equals(self.datawidth, ram_datawidth):
            return self._dma_write_rtl_pattern_same(ram, local_addr, global_addr, pattern,
                                                    port, cond, ram_method)

        comp = self.datawidth < ram_datawidth
        if not isinstance(comp, bool):
            raise ValueError('datawidth must be int, not (%s, %s)' %
                             (type(self.datawidth, ram_datawidth)))

        if comp:
            return self._dma_write_rtl_pattern_narrow(ram, local_addr, global_addr, pattern,
                                                      port, cond, ram_method,
                                                      ram_datawidth)

        return self._dma_write_rtl_pattern_wide(ram, local_addr, global_addr, pattern,
                                                port, cond, ram_method,
                                                ram_datawidth)

    def _dma_write_rtl_pattern_same(self, ram, local_addr, global_addr, pattern,
                                    port=0, cond=None, ram_method=None):

        block_size = pattern[0][0]

        fsm = TmpFSM(self.m, self.clk, self.rst)

        if cond is not None:
            fsm.If(cond).goto_next()

        req_global_addr = self.m.TmpReg(self.addrwidth, initval=0)
        req_size = self.m.TmpReg(block_size.bit_length() + 1, initval=0)
        rest_size = self.m.TmpReg(block_size.bit_length() + 1, initval=0)
        max_burstlen = 2 ** self.burst_size_width

        fsm(
            req_global_addr(self.mask_addr(global_addr)),
            rest_size(block_size)
        )

        count_list = [self.m.TmpReg(size.bit_length() + 1, initval=0)
                      for size, stride in pattern[1:]]

        for count, (size, stride) in zip(count_list, pattern[1:]):
            fsm(
                count(size - 1)
            )

        if ram_method is None:
            ram_method = getattr(ram, 'read_dataflow_pattern')

        data, last, done = ram_method(port, local_addr, pattern,
                                      cond=fsm, signed=False)
        fsm.goto_next()

        check_state = fsm.current

        self._check_4KB_boundary(fsm, max_burstlen,
                                 req_global_addr, req_size, rest_size)

        ack, counter = self.write_request(req_global_addr, req_size, cond=fsm)
        fsm.If(ack).goto_next()

        done = self.write_dataflow(data, counter, cond=fsm)

        fsm.If(done)(
            req_global_addr.add(optimize(req_size * (self.datawidth // 8)))
        )

        update_count = rest_size == 0
        for count, (size, stride) in zip(count_list, pattern[1:]):
            fsm.If(done, update_count)(
                count.dec()
            )
            fsm.If(done, update_count, count == 0)(
                count(size - 1)
            )
            update_count = vtypes.Ands(update_count, count == 0)

        fsm.If(done, rest_size == 0, vtypes.Not(update_count))(
            rest_size(block_size)
        )
        fsm.If(done, rest_size > 0).goto(check_state)
        fsm.If(done, rest_size == 0, vtypes.Not(
            update_count)).goto(check_state)
        fsm.If(done, update_count).goto_next()

        done = self._fsm_done(fsm)

        return fsm, done

    def _dma_write_rtl_pattern_narrow(self, ram, local_addr, global_addr, pattern,
                                      port=0, cond=None, ram_method=None,
                                      ram_datawidth=None):
        """ axi.datawidth < ram.datawidth """

        if ram_datawidth is None:
            ram_datawidth = ram.datawidth

        if ram_datawidth % self.datawidth != 0:
            raise ValueError(
                'ram_datawidth must be multiple number of axi.datawidth')

        block_size = pattern[0][0]

        pack_size = ram_datawidth // self.datawidth
        dma_size = (block_size << int(math.log(pack_size, 2))
                    if math.log(pack_size, 2) % 1.0 == 0.0 else
                    block_size * pack_size)

        fsm = TmpFSM(self.m, self.clk, self.rst)

        if cond is not None:
            fsm.If(cond).goto_next()

        req_global_addr = self.m.TmpReg(self.addrwidth, initval=0)
        req_size = self.m.TmpReg(dma_size.bit_length() + 1, initval=0)
        rest_size = self.m.TmpReg(dma_size.bit_length() + 1, initval=0)
        max_burstlen = 2 ** self.burst_size_width

        fsm(
            req_global_addr(self.mask_addr(global_addr)),
            rest_size(dma_size)
        )

        count_list = [self.m.TmpReg(size.bit_length() + 1, initval=0)
                      for size, stride in pattern[1:]]

        for count, (size, stride) in zip(count_list, pattern[1:]):
            fsm(
                count(size - 1)
            )

        if ram_method is None:
            ram_method = getattr(ram, 'read_dataflow_pattern')

        data, last, done = ram_method(port, local_addr, pattern,
                                      cond=fsm, signed=False)
        fsm.goto_next()

        check_state = fsm.current

        self._check_4KB_boundary(fsm, max_burstlen,
                                 req_global_addr, req_size, rest_size)

        ack, counter = self.write_request(req_global_addr, req_size, cond=fsm)
        fsm.If(ack).goto_next()

        wdata = self.m.TmpReg(ram_datawidth, initval=0)
        wvalid = self.m.TmpReg(initval=0)
        wready = self.m.TmpWire()
        ack = vtypes.Ors(wready, vtypes.Not(wvalid))

        pack_count = self.m.TmpReg(pack_size, initval=0)
        rcond = make_condition(fsm, ack, pack_count == 0)
        rdata, rvalid = data.read(cond=rcond)

        seq = TmpSeq(self.m, self.clk, self.rst)
        seq.If(ack)(
            wvalid(0)
        )
        seq.If(rvalid)(
            wdata(rdata),
            wvalid(1),
            pack_count.inc()
        )
        seq.If(ack, pack_count > 0)(
            wdata(wdata >> self.datawidth),
            wvalid(1),
            pack_count.inc()
        )
        seq.If(ack, pack_count == pack_size - 1)(
            wdata(wdata >> self.datawidth),
            wvalid(1),
            pack_count(0)
        )

        df_data = self.df.Variable(
            wdata, wvalid, wready, width=self.datawidth, signed=False)

        done = self.write_dataflow(df_data, counter, cond=fsm)

        fsm.If(done)(
            req_global_addr.add(optimize(req_size * (self.datawidth // 8)))
        )

        update_count = rest_size == 0
        for count, (size, stride) in zip(count_list, pattern[1:]):
            fsm.If(done, update_count)(
                count.dec()
            )
            fsm.If(done, update_count, count == 0)(
                count(size - 1)
            )
            update_count = vtypes.Ands(update_count, count == 0)

        fsm.If(done, rest_size == 0, vtypes.Not(update_count))(
            rest_size(dma_size)
        )
        fsm.If(done, rest_size > 0).goto(check_state)
        fsm.If(done, rest_size == 0, vtypes.Not(
            update_count)).goto(check_state)
        fsm.If(done, update_count).goto_next()

        done = self._fsm_done(fsm)

        return fsm, done

    def _dma_write_rtl_pattern_wide(self, ram, local_addr, global_addr, pattern,
                                    port=0, cond=None, ram_method=None,
                                    ram_datawidth=None):
        """ axi.datawidth > ram.datawidth """

        if ram_datawidth is None:
            ram_datawidth = ram.datawidth

        if self.datawidth % ram_datawidth != 0:
            raise ValueError(
                'axi.datawidth must be multiple number of ram_datawidth')

        block_size = pattern[0][0]

        pack_size = self.datawidth // ram_datawidth
        dma_size = (block_size >> int(math.log(pack_size, 2))
                    if math.log(pack_size, 2) % 1.0 == 0.0 else
                    int(block_size // pack_size))

        fsm = TmpFSM(self.m, self.clk, self.rst)

        if cond is not None:
            fsm.If(cond).goto_next()

        req_global_addr = self.m.TmpReg(self.addrwidth, initval=0)
        req_size = self.m.TmpReg(dma_size.bit_length() + 1, initval=0)
        rest_size = self.m.TmpReg(dma_size.bit_length() + 1, initval=0)
        max_burstlen = 2 ** self.burst_size_width

        fsm(
            req_global_addr(self.mask_addr(global_addr)),
            rest_size(dma_size)
        )

        count_list = [self.m.TmpReg(size.bit_length() + 1, initval=0)
                      for size, stride in pattern[1:]]

        for count, (size, stride) in zip(count_list, pattern[1:]):
            fsm(
                count(size - 1)
            )

        if ram_method is None:
            ram_method = getattr(ram, 'read_dataflow_pattern')

        data, last, done = ram_method(port, local_addr, pattern,
                                      cond=fsm, signed=False)
        fsm.goto_next()

        check_state = fsm.current

        self._check_4KB_boundary(fsm, max_burstlen,
                                 req_global_addr, req_size, rest_size)

        ack, counter = self.write_request(req_global_addr, req_size, cond=fsm)
        fsm.If(ack).goto_next()

        wdata = self.m.TmpReg(self.datawidth, initval=0)
        wvalid = self.m.TmpReg(initval=0)
        wready = self.m.TmpWire()
        ack = vtypes.Ors(wready, vtypes.Not(wvalid))

        pack_count = self.m.TmpReg(pack_size, initval=0)
        rcond = make_condition(fsm, ack)
        rdata, rvalid = data.read(cond=rcond)

        seq = TmpSeq(self.m, self.clk, self.rst)
        seq.If(ack)(
            wvalid(0)
        )
        seq.If(rvalid)(
            wdata(vtypes.Cat(rdata, wdata[ram_datawidth:self.datawidth])),
            wvalid(0),
            pack_count.inc()
        )
        seq.If(rvalid, pack_count == pack_size - 1)(
            wdata(vtypes.Cat(rdata, wdata[ram_datawidth:self.datawidth])),
            wvalid(1),
            pack_count(0)
        )

        df_data = self.df.Variable(
            wdata, wvalid, wready, width=self.datawidth, signed=False)

        done = self.write_dataflow(df_data, counter, cond=fsm)

        fsm.If(done)(
            req_global_addr.add(optimize(req_size * (self.datawidth // 8)))
        )

        update_count = rest_size == 0
        for count, (size, stride) in zip(count_list, pattern[1:]):
            fsm.If(done, update_count)(
                count.dec()
            )
            fsm.If(done, update_count, count == 0)(
                count(size - 1)
            )
            update_count = vtypes.Ands(update_count, count == 0)

        fsm.If(done, rest_size == 0, vtypes.Not(update_count))(
            rest_size(dma_size)
        )
        fsm.If(done, rest_size > 0).goto(check_state)
        fsm.If(done, rest_size == 0, vtypes.Not(
            update_count)).goto(check_state)
        fsm.If(done, update_count).goto_next()

        done = self._fsm_done(fsm)

        return fsm, done

    def dma_write_rtl_multidim(self, ram, local_addr, global_addr, shape, order=None,
                               port=0, cond=None, ram_method=None):

        if order is None:
            order = list(reversed(range(len(shape))))

        pattern = self._to_pattern(shape, order)
        return self.dma_write_rtl_pattern(ram, local_addr, global_addr, pattern,
                                          port, cond, ram_method)

    def dma_write_rtl_unsafe(self, ram, local_addr, global_addr, size,
                             local_stride, port=0, cond=None, ram_method=None):
        """ Unsafe API with no length and 4KB region check """

        ram_datawidth = (ram.datawidth if ram_method is None else
                         ram.orig_datawidth if 'block' in ram_method.func.__name__ else
                         ram.datawidth)

        if vtypes.equals(self.datawidth, ram_datawidth):
            return self._dma_write_rtl_unsafe_same(ram, local_addr, global_addr, size,
                                                   local_stride, port, cond, ram_method)

        comp = self.datawidth < ram_datawidth
        if not isinstance(comp, bool):
            raise ValueError('datawidth must be int, not (%s, %s)' %
                             (type(self.datawidth, ram_datawidth)))

        if comp:
            return self._dma_write_rtl_unsafe_narrow(ram, local_addr, global_addr, size,
                                                     local_stride, port, cond, ram_method,
                                                     ram_datawidth)

        return self._dma_write_rtl_unsafe_wide(ram, local_addr, global_addr, size,
                                               local_stride, port, cond, ram_method,
                                               ram_datawidth)

    def _dma_write_rtl_unsafe_same(self, ram, local_addr, global_addr, size,
                                   local_stride, port=0, cond=None, ram_method=None):
        fsm = TmpFSM(self.m, self.clk, self.rst)

        if cond is not None:
            fsm.If(cond).goto_next()

        ack, counter = self.write_request(global_addr, size, cond=fsm)
        fsm.If(ack).goto_next()

        if ram_method is None:
            ram_method = getattr(ram, 'read_dataflow')

        data, last, done = ram_method(port, local_addr, size,
                                      stride=local_stride, cond=fsm, signed=False)
        fsm.goto_next()

        done = self.write_dataflow(data, counter, cond=fsm)
        fsm.If(done).goto_init()

        return fsm, done

    def _dma_write_rtl_unsafe_narrow(self, ram, local_addr, global_addr, size,
                                     local_stride, port=0, cond=None, ram_method=None,
                                     ram_datawidth=None):
        """ axi.datawidth < ram.datawidth """

        if ram_datawidth is None:
            ram_datawidth = ram.datawidth

        if ram_datawidth % self.datawidth != 0:
            raise ValueError(
                'ram_datawidth must be multiple number of axi.datawidth')

        pack_size = ram_datawidth // self.datawidth
        dma_size = (size << int(math.log(pack_size, 2))
                    if math.log(pack_size, 2) % 1.0 == 0.0 else
                    size * pack_size)

        fsm = TmpFSM(self.m, self.clk, self.rst)

        if cond is not None:
            fsm.If(cond).goto_next()

        ack, counter = self.write_request(global_addr, dma_size, cond=fsm)
        fsm.If(ack).goto_next()

        if ram_method is None:
            ram_method = getattr(ram, 'read_dataflow')

        data, last, done = ram_method(port, local_addr, size,
                                      stride=local_stride, cond=fsm, signed=False)
        fsm.goto_next()

        wdata = self.m.TmpReg(ram_datawidth, initval=0)
        wvalid = self.m.TmpReg(initval=0)
        wready = self.m.TmpWire()
        ack = vtypes.Ors(wready, vtypes.Not(wvalid))

        pack_count = self.m.TmpReg(pack_size, initval=0)
        rcond = make_condition(fsm, ack, pack_count == 0)
        rdata, rvalid = data.read(cond=rcond)

        seq = TmpSeq(self.m, self.clk, self.rst)
        seq.If(ack)(
            wvalid(0)
        )
        seq.If(rvalid)(
            wdata(rdata),
            wvalid(1),
            pack_count.inc()
        )
        seq.If(ack, pack_count > 0)(
            wdata(wdata >> self.datawidth),
            wvalid(1),
            pack_count.inc()
        )
        seq.If(ack, pack_count == pack_size - 1)(
            wdata(wdata >> self.datawidth),
            wvalid(1),
            pack_count(0)
        )

        df_data = self.df.Variable(
            wdata, wvalid, wready, width=self.datawidth, signed=False)

        done = self.write_dataflow(df_data, counter, cond=fsm)
        fsm.If(done).goto_init()

        return fsm, done

    def _dma_write_rtl_unsafe_wide(self, ram, local_addr, global_addr, size,
                                   local_stride, port=0, cond=None, ram_method=None,
                                   ram_datawidth=None):
        """ axi.datawidth > ram.datawidth """

        if ram_datawidth is None:
            ram_datawidth = ram.datawidth

        if self.datawidth % ram_datawidth != 0:
            raise ValueError(
                'axi.datawidth must be multiple number of ram_datawidth')

        pack_size = self.datawidth // ram_datawidth
        dma_size = (size >> int(math.log(pack_size, 2))
                    if math.log(pack_size, 2) % 1.0 == 0.0 else
                    int(size // pack_size))

        fsm = TmpFSM(self.m, self.clk, self.rst)

        if cond is not None:
            fsm.If(cond).goto_next()

        ack, counter = self.write_request(global_addr, dma_size, cond=fsm)
        fsm.If(ack).goto_next()

        if ram_method is None:
            ram_method = getattr(ram, 'read_dataflow')

        data, last, done = ram_method(port, local_addr, size,
                                      stride=local_stride, cond=fsm, signed=False)
        fsm.goto_next()

        wdata = self.m.TmpReg(self.datawidth, initval=0)
        wvalid = self.m.TmpReg(initval=0)
        wready = self.m.TmpWire()
        ack = vtypes.Ors(wready, vtypes.Not(wvalid))

        pack_count = self.m.TmpReg(pack_size, initval=0)
        rcond = make_condition(fsm, ack)
        rdata, rvalid = data.read(cond=rcond)

        seq = TmpSeq(self.m, self.clk, self.rst)
        seq.If(ack)(
            wvalid(0)
        )
        seq.If(rvalid)(
            wdata(vtypes.Cat(rdata, wdata[ram_datawidth:self.datawidth])),
            wvalid(0),
            pack_count.inc()
        )
        seq.If(rvalid, pack_count == pack_size - 1)(
            wdata(vtypes.Cat(rdata, wdata[ram_datawidth:self.datawidth])),
            wvalid(1),
            pack_count(0)
        )

        df_data = self.df.Variable(
            wdata, wvalid, wready, width=self.datawidth, signed=False)

        done = self.write_dataflow(df_data, counter, cond=fsm)
        fsm.If(done).goto_init()

        return fsm, done

    def _check_4KB_boundary(self, fsm, max_burstlen,
                            req_global_addr, req_size, rest_size):
        fsm.If(rest_size <= max_burstlen,
               self.check_boundary(req_global_addr, rest_size))(
            req_size(self.rest_boundary(req_global_addr)),
            rest_size(
                rest_size - self.rest_boundary(req_global_addr))
        ).Elif(rest_size <= max_burstlen)(
            req_size(rest_size),
            rest_size(0)
        ).Elif(self.check_boundary(req_global_addr, max_burstlen))(
            req_size(self.rest_boundary(req_global_addr)),
            rest_size(
                rest_size - self.rest_boundary(req_global_addr))
        ).Else(
            req_size(max_burstlen),
            rest_size(rest_size - max_burstlen)
        )
        fsm.goto_next()

    def _set_flag(self, fsm, prefix=None):
        flag = self.m.TmpReg(initval=0, prefix=prefix)
        fsm(
            flag(1)
        )
        fsm.Delay(1)(
            flag(0)
        )
        fsm.goto_next()
        return flag

    def _fsm_start(self, fsm):
        start = self._set_flag(fsm, 'fsm_start')
        return start

    def _fsm_done(self, fsm):
        done = self._set_flag(fsm, 'fsm_done')
        fsm.goto_init()
        return done


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
