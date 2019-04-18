from __future__ import absolute_import
from __future__ import print_function

import math
import functools
from collections import OrderedDict

import veriloggen.core.vtypes as vtypes
import veriloggen.types.util as util
import veriloggen.types.axi as axi
from veriloggen.seq.seq import Seq, TmpSeq
from veriloggen.fsm.fsm import FSM, TmpFSM
from veriloggen.optimizer import try_optimize as optimize
from veriloggen.dataflow.dtypes import make_condition

from .ttypes import _MutexFunction
from .ram import RAM, FixedRAM, MultibankRAM, to_multibank_ram


class AXIM(axi.AxiMaster, _MutexFunction):
    """ AXI Master Interface with DMA controller """

    __intrinsics__ = ('read', 'write',
                      'dma_read', 'dma_read_async',
                      'dma_write', 'dma_write_async',
                      'dma_wait_read', 'dma_wait_write',
                      'dma_wait_read', 'dma_wait_write', 'dma_wait',
                      'set_global_base_addr',) + _MutexFunction.__intrinsics__

    burstlen = 256

    def __init__(self, m, name, clk, rst, datawidth=32, addrwidth=32,
                 waddr_id_width=0, wdata_id_width=0, wresp_id_width=0,
                 raddr_id_width=0, rdata_id_width=0,
                 waddr_user_width=1, wdata_user_width=0, wresp_user_width=0,
                 raddr_user_width=1, rdata_user_width=0,
                 waddr_burst_mode=axi.BURST_INCR, raddr_burst_mode=axi.BURST_INCR,
                 waddr_cache_mode=axi.CACHE_HP, raddr_cache_mode=axi.CACHE_HP,
                 waddr_user_value=axi.AxUSER_DEFAULT, wdata_user_value=axi.USER_DEFAULT,
                 raddr_user_value=axi.AxUSER_DEFAULT,
                 noio=False,
                 enable_async=False, use_global_base_addr=False,
                 num_cmd_delay=0, num_data_delay=0,
                 op_sel_width=8, fsm_as_module=False):

        axi.AxiMaster.__init__(self, m, name, clk, rst, datawidth, addrwidth,
                               waddr_id_width, wdata_id_width, wresp_id_width,
                               raddr_id_width, rdata_id_width,
                               waddr_user_width, wdata_user_width, wresp_user_width,
                               raddr_user_width, rdata_user_width,
                               waddr_burst_mode, raddr_burst_mode,
                               waddr_cache_mode, raddr_cache_mode,
                               waddr_user_value, wdata_user_value,
                               raddr_user_value,
                               noio)

        self.enable_async = enable_async
        self.use_global_base_addr = use_global_base_addr
        self.num_cmd_delay = num_cmd_delay
        self.num_data_delay = num_data_delay
        self.op_sel_width = op_sel_width
        self.fsm_as_module = fsm_as_module

        self.mutex = None

        self.read_start = self.m.Reg('_'.join(['', self.name, 'read_start']),
                                     initval=0)
        self.read_op_sel = self.m.Reg('_'.join(['', self.name, 'read_op_sel']),
                                      self.op_sel_width, initval=0)
        self.read_local_addr = self.m.Reg('_'.join(['', self.name, 'read_local_addr']),
                                          self.addrwidth, initval=0)
        self.read_global_addr = self.m.Reg('_'.join(['', self.name, 'read_global_addr']),
                                           self.addrwidth, initval=0)
        self.read_size = self.m.Reg('_'.join(['', self.name, 'read_size']),
                                    self.addrwidth + 1, initval=0)
        self.read_local_stride = self.m.Reg('_'.join(['', self.name, 'read_local_stride']),
                                            self.addrwidth, initval=0)
        self.read_idle = self.m.Reg(
            '_'.join(['', self.name, 'read_idle']), initval=1)

        self.seq(
            self.read_start(0)
        )

        self.read_op_id_map = OrderedDict()
        self.read_op_id_count = 1
        self.read_reqs = OrderedDict()
        self.read_ops = []

        self.read_fsm = None
        self.read_data_wire = None
        self.read_valid_wire = None

        self.read_narrow_fsms = OrderedDict()  # key: pack_size
        self.read_narrow_pack_counts = OrderedDict()  # key: pack_size
        self.read_narrow_data_wires = OrderedDict()  # key: pack_size
        self.read_narrow_valid_wires = OrderedDict()  # key: pack_size

        self.read_wide_fsms = OrderedDict()  # key: pack_size
        self.read_wide_pack_counts = OrderedDict()  # key: pack_size
        self.read_wide_data_wires = OrderedDict()  # key: pack_size
        self.read_wide_valid_wires = OrderedDict()  # key: pack_size

        self.write_start = self.m.Reg('_'.join(['', self.name, 'write_start']),
                                      initval=0)
        self.write_op_sel = self.m.Reg('_'.join(['', self.name, 'write_op_sel']),
                                       self.op_sel_width, initval=0)
        self.write_local_addr = self.m.Reg('_'.join(['', self.name, 'write_local_addr']),
                                           self.addrwidth, initval=0)
        self.write_global_addr = self.m.Reg('_'.join(['', self.name, 'write_global_addr']),
                                            self.addrwidth, initval=0)
        self.write_size = self.m.Reg('_'.join(['', self.name, 'write_size']),
                                     self.addrwidth + 1, initval=0)
        self.write_local_stride = self.m.Reg('_'.join(['', self.name, 'write_local_stride']),
                                             self.addrwidth, initval=0)
        self.write_idle = self.m.Reg(
            '_'.join(['', self.name, 'write_idle']), initval=1)

        self.seq(
            self.write_start(0)
        )

        if self.use_global_base_addr:
            self.global_base_addr = self.m.Reg('_'.join(['', self.name, 'global_base_addr']),
                                               self.addrwidth, initval=0)
        else:
            self.global_base_addr = None

        self.write_op_id_map = OrderedDict()
        self.write_op_id_count = 1
        self.write_reqs = OrderedDict()
        self.write_ops = []

        self.write_fsm = None
        self.write_data_counter = None
        self.write_data_done = self.m.Wire(
            '_'.join(['', self.name, 'write_data_done']))

        self.write_narrow_fsms = OrderedDict()  # key: pack_size
        self.write_narrow_wdatas = OrderedDict()  # key: pack_size
        self.write_narrow_wvalids = OrderedDict()  # key: pack_size
        self.write_narrow_wreadys = OrderedDict()  # key: pack_size
        self.write_narrow_pack_counts = OrderedDict()  # key: pack_size

        self.write_wide_fsms = OrderedDict()  # key: pack_size
        self.write_wide_wdatas = OrderedDict()  # key: pack_size
        self.write_wide_wvalids = OrderedDict()  # key: pack_size
        self.write_wide_wreadys = OrderedDict()  # key: pack_size
        self.write_wide_pack_counts = OrderedDict()  # key: pack_size

    def read(self, fsm, global_addr):
        if self.use_global_base_addr:
            global_addr = self.global_base_addr + global_addr

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

        rdata = self.m.TmpReg(self.datawidth, initval=0,
                              signed=True, prefix='axim_rdata')
        fsm.If(valid)(rdata(data))
        fsm.Then().goto_next()

        return rdata

    def write(self, fsm, global_addr, value):
        if self.use_global_base_addr:
            global_addr = self.global_base_addr + global_addr

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
                 local_stride=1, port=0, ram_method=None):

        if self.enable_async:
            self.dma_wait_read(fsm)

        self._dma_read(fsm, ram, local_addr, global_addr, size,
                       local_stride, port, ram_method)

        self.dma_wait_read(fsm)

    def dma_read_async(self, fsm, ram, local_addr, global_addr, size,
                       local_stride=1, port=0, ram_method=None):

        if not self.enable_async:
            raise ValueError(
                "Async mode is disabled. Set 'True' to AXIM.enable_async.")

        self.dma_wait_read(fsm)

        self._dma_read(fsm, ram, local_addr, global_addr, size,
                       local_stride, port, ram_method)

    def dma_write(self, fsm, ram, local_addr, global_addr, size,
                  local_stride=1, port=0, ram_method=None):

        if self.enable_async:
            self.dma_wait_write(fsm)

        self._dma_write(fsm, ram, local_addr, global_addr, size,
                        local_stride, port, ram_method)

        self.dma_wait_write(fsm)

    def dma_write_async(self, fsm, ram, local_addr, global_addr, size,
                        local_stride=1, port=0, ram_method=None):

        if not self.enable_async:
            raise ValueError(
                "Async mode is disabled. Set 'True' to AXIM.enable_async.")

        self.dma_wait_write(fsm)

        self._dma_write(fsm, ram, local_addr, global_addr, size,
                        local_stride, port, ram_method)

    def dma_wait_read(self, fsm):

        fsm.If(self.read_idle).goto_next()

    def dma_wait_write(self, fsm):

        fsm.If(self.write_idle).goto_next()

    def dma_wait(self, fsm):

        fsm.If(self.read_idle, self.write_idle).goto_next()

    def set_global_base_addr(self, fsm, addr):

        if not self.use_global_base_addr:
            raise ValueError("global_base_addr is disabled.")

        flag = self._set_flag(fsm)
        self.seq.If(flag)(
            self.global_base_addr(addr)
        )

    # --------------------
    # read
    # --------------------
    def _dma_read(self, fsm, ram, local_addr, global_addr, size,
                  local_stride=1, port=0, ram_method=None):

        if isinstance(ram, (tuple, list)):
            ram = to_multibank_ram(ram)

        if not isinstance(ram, (RAM, MultibankRAM)):
            raise TypeError('RAM object is required.')

        if ram_method is None:
            ram_method = getattr(ram, 'write_dataflow')

        start = self._set_flag(fsm)

        for _ in range(self.num_cmd_delay + 1):
            fsm.goto_next()

        self._set_read_request(ram, port, ram_method, start,
                               local_addr, global_addr, size, local_stride)

        self._synthesize_read_fsm(ram, port, ram_method)

        fsm.goto_next()

    def _set_read_request(self, ram, port, ram_method, start,
                          local_addr, global_addr, size, local_stride):

        op_id = self._get_read_op_id(ram, port, ram_method)

        if op_id in self.read_reqs:
            (read_start, read_op_sel,
             read_local_addr_in, read_global_addr_in,
             read_size_in, read_local_stride_in) = self.read_reqs[op_id]

            self.seq.If(start)(
                read_start(1),
                read_op_sel(op_id),
                read_local_addr_in(local_addr),
                read_global_addr_in(global_addr),
                read_size_in(size),
                read_local_stride_in(local_stride)
            )

            return

        port = str(vtypes.to_int(port))

        read_start = self.m.Reg(
            '_'.join(['', self.name, ram.name, port, 'read_start']),
            initval=0)
        read_op_sel = self.m.Reg(
            '_'.join(['', self.name, ram.name, port, 'read_op_sel']),
            self.op_sel_width, initval=0)
        read_local_addr = self.m.Reg(
            '_'.join(['', self.name, ram.name, port, 'read_local_addr']),
            self.addrwidth, initval=0)
        read_global_addr = self.m.Reg(
            '_'.join(['', self.name, ram.name, port, 'read_global_addr']),
            self.addrwidth, initval=0)
        read_size = self.m.Reg(
            '_'.join(['', self.name, ram.name, port, 'read_size']),
            self.addrwidth + 1, initval=0)
        read_local_stride = self.m.Reg(
            '_'.join(['', self.name, ram.name, port, 'read_local_stride']),
            self.addrwidth, initval=0)

        self.seq(
            read_start(0)
        )
        self.seq.If(start)(
            read_start(1),
            read_op_sel(op_id),
            read_local_addr(local_addr),
            read_global_addr(global_addr),
            read_size(size),
            read_local_stride(local_stride)
        )

        self.read_reqs[op_id] = (read_start, read_op_sel,
                                 read_local_addr, read_global_addr,
                                 read_size, read_local_stride)

        if self.num_cmd_delay > 0:
            read_start = self.seq.Prev(read_start, self.num_cmd_delay)
            read_op_sel = self.seq.Prev(read_op_sel, self.num_cmd_delay)
            read_local_addr = self.seq.Prev(
                read_local_addr, self.num_cmd_delay)
            read_global_addr = self.seq.Prev(
                read_global_addr, self.num_cmd_delay)
            read_size = self.seq.Prev(read_size, self.num_cmd_delay)
            read_local_stride = self.seq.Prev(
                read_local_stride, self.num_cmd_delay)

        self.seq.If(read_start)(
            self.read_idle(0)
        )

        self.seq.If(read_start)(
            self.read_start(1),
            self.read_op_sel(read_op_sel),
            self.read_local_addr(read_local_addr),
            self.read_global_addr(read_global_addr),
            self.read_size(read_size),
            self.read_local_stride(read_local_stride)
        )

    def _synthesize_read_fsm(self, ram, port, ram_method):

        ram_method_name = (ram_method.func.__name__
                           if isinstance(ram_method, functools.partial) else
                           ram_method.__name__)
        ram_datawidth = (ram.datawidth if ram_method is None else
                         ram.orig_datawidth if 'bcast' in ram_method_name else
                         ram.orig_datawidth if 'block' in ram_method_name else
                         ram.datawidth)

        if not isinstance(self.datawidth, int):
            raise TypeError("axi.datawidth must be int, not '%s'" %
                            str(type(self.datawidth)))

        if not isinstance(ram_datawidth, int):
            raise TypeError("ram_datawidth must be int, not '%s'" %
                            str(type(ram_datawidth)))

        if self.datawidth == ram_datawidth:
            return self._synthesize_read_fsm_same(ram, port, ram_method, ram_datawidth)

        if self.datawidth < ram_datawidth:
            return self._synthesize_read_fsm_narrow(ram, port, ram_method, ram_datawidth)

        return self._synthesize_read_fsm_wide(ram, port, ram_method, ram_datawidth)

    def _synthesize_read_fsm_same(self, ram, port, ram_method, ram_datawidth):

        op_id = self._get_read_op_id(ram, port, ram_method)
        port = vtypes.to_int(port)

        if op_id in self.read_ops:
            """ already synthesized op """
            return

        if self.read_fsm is not None:
            """ new op """
            self.read_ops.append(op_id)

            fsm = self.read_fsm
            data = self.read_data_wire
            valid = self.read_valid_wire

            # state 0
            fsm.set_index(0)
            wdata, wvalid, w = self._get_op_write_dataflow(ram_datawidth)
            cond = vtypes.Ands(self.read_start, self.read_op_sel == op_id)
            ram_method(port, self.read_local_addr, w, self.read_size,
                       stride=self.read_local_stride, cond=cond)

            fsm.If(cond).goto_next()

            # state 3
            fsm.set_index(3)
            valid_cond = vtypes.Ands(valid, self.read_op_sel == op_id)

            fsm.Delay(1)(
                wvalid(0)
            )
            fsm.If(valid_cond)(
                wdata(data),
                wvalid(1)
            )

            return

        """ new op and fsm """
        fsm = FSM(self.m, '_'.join(['', self.name, 'read_fsm']),
                  self.clk, self.rst, as_module=self.fsm_as_module)
        self.read_fsm = fsm

        self.read_ops.append(op_id)

        cur_global_addr = self.m.Reg('_'.join(['', self.name, 'read_cur_global_addr']),
                                     self.addrwidth, initval=0)
        cur_size = self.m.Reg('_'.join(['', self.name, 'read_cur_size']),
                              self.addrwidth + 1, initval=0)
        rest_size = self.m.Reg('_'.join(['', self.name, 'read_rest_size']),
                               self.addrwidth + 1, initval=0)
        max_burstlen = 2 ** self.burst_size_width

        # state 0
        wdata, wvalid, w = self._get_op_write_dataflow(ram_datawidth)
        cond = vtypes.Ands(self.read_start, self.read_op_sel == op_id)
        ram_method(port, self.read_local_addr, w, self.read_size,
                   stride=self.read_local_stride, cond=cond)

        if not self.use_global_base_addr:
            gaddr = self.read_global_addr
        else:
            gaddr = self.read_global_addr + self.global_base_addr

        fsm.If(self.read_start)(
            cur_global_addr(self.mask_addr(gaddr)),
            rest_size(self.read_size)
        )
        fsm.If(cond).goto_next()

        # state 1
        check_state = fsm.current
        self._check_4KB_boundary(fsm, max_burstlen,
                                 cur_global_addr, cur_size, rest_size)

        # state 2
        ack, counter = self.read_request(cur_global_addr, cur_size, cond=fsm)
        fsm.If(ack).goto_next()

        # state 3
        data, valid, last = self.read_data(cond=fsm)
        self.read_data_wire = data
        self.read_valid_wire = valid

        valid_cond = vtypes.Ands(valid, self.read_op_sel == op_id)

        fsm.Delay(1)(
            wvalid(0)
        )
        fsm.If(valid_cond)(
            wdata(data),
            wvalid(1),
        )

        fsm.If(valid, last)(
            cur_global_addr.add(optimize(cur_size * (self.datawidth // 8)))
        )
        fsm.If(valid, last, rest_size > 0).goto(check_state)
        fsm.If(valid, last, rest_size == 0).goto_next()

        for _ in range(self.num_data_delay):
            fsm.goto_next()

        # state 4
        set_idle = self._set_flag(fsm)
        self.seq.If(set_idle)(
            self.read_idle(1)
        )

        fsm.goto_init()

    def _synthesize_read_fsm_narrow(self, ram, port, ram_method, ram_datawidth):
        """ axi.datawidth < ram.datawidth """

        if ram_datawidth % self.datawidth != 0:
            raise ValueError(
                'ram_datawidth must be multiple number of axi.datawidth')

        pack_size = ram_datawidth // self.datawidth
        dma_size = (self.read_size << int(math.log(pack_size, 2))
                    if math.log(pack_size, 2) % 1.0 == 0.0 else
                    self.read_size * pack_size)

        op_id = self._get_read_op_id(ram, port, ram_method)
        port = vtypes.to_int(port)

        if op_id in self.read_ops:
            """ already synthesized op """
            return

        if pack_size in self.read_narrow_fsms:
            """ new op """
            self.read_ops.append(op_id)

            fsm = self.read_narrow_fsms[pack_size]
            pack_count = self.read_narrow_pack_counts[pack_size]
            data = self.read_narrow_data_wires[pack_size]
            valid = self.read_narrow_valid_wires[pack_size]

            # state 0
            fsm.set_index(0)
            wdata, wvalid, w = self._get_op_write_dataflow(ram_datawidth)
            cond = vtypes.Ands(self.read_start, self.read_op_sel == op_id)
            ram_method(port, self.read_local_addr, w, self.read_size,
                       stride=self.read_local_stride, cond=cond)

            fsm.If(cond).goto_next()

            # state 3
            fsm.set_index(3)
            valid_cond = vtypes.Ands(valid, self.read_op_sel == op_id)

            fsm.Delay(1)(
                wvalid(0)
            )
            fsm.If(valid_cond)(
                wdata(vtypes.Cat(data, wdata[self.datawidth:ram_datawidth])),
                wvalid(0),
                pack_count.inc()
            )
            fsm.If(valid_cond, pack_count == pack_size - 1)(
                wdata(vtypes.Cat(data, wdata[self.datawidth:ram_datawidth])),
                wvalid(1),
                pack_count(0)
            )

            return

        """ new op and fsm """
        fsm = FSM(self.m, '_'.join(['', self.name,
                                    'read_narrow', str(pack_size),
                                    'fsm']),
                  self.clk, self.rst, as_module=self.fsm_as_module)
        self.read_narrow_fsms[pack_size] = fsm

        self.read_ops.append(op_id)

        cur_global_addr = self.m.Reg('_'.join(['', self.name,
                                               'read_narrow', str(pack_size),
                                               'cur_global_addr']),
                                     self.addrwidth, initval=0)
        cur_size = self.m.Reg('_'.join(['', self.name,
                                        'read_narrow', str(pack_size),
                                        'cur_size']),
                              self.addrwidth + 1, initval=0)
        rest_size = self.m.Reg('_'.join(['', self.name,
                                         'read_narrow', str(pack_size),
                                         'rest_size']),
                               self.addrwidth + 1, initval=0)
        max_burstlen = 2 ** self.burst_size_width

        # state 0
        wdata, wvalid, w = self._get_op_write_dataflow(ram_datawidth)
        cond = vtypes.Ands(self.read_start, self.read_op_sel == op_id)
        ram_method(port, self.read_local_addr, w, self.read_size,
                   stride=self.read_local_stride, cond=cond)

        if not self.use_global_base_addr:
            gaddr = self.read_global_addr
        else:
            gaddr = self.read_global_addr + self.global_base_addr

        fsm.If(self.read_start)(
            cur_global_addr(self.mask_addr(gaddr)),
            rest_size(dma_size)
        )
        fsm.If(cond).goto_next()

        # state 1
        check_state = fsm.current
        self._check_4KB_boundary(fsm, max_burstlen,
                                 cur_global_addr, cur_size, rest_size)

        # state 2
        ack, counter = self.read_request(cur_global_addr, cur_size, cond=fsm)
        fsm.If(ack).goto_next()

        # state 3
        pack_count = self.m.Reg('_'.join(['', self.name,
                                          'read_narrow', str(pack_size),
                                          'pack_count']),
                                int(math.ceil(math.log(pack_size, 2))), initval=0)
        self.read_narrow_pack_counts[pack_size] = pack_count

        data, valid, last = self.read_data(cond=fsm)
        self.read_narrow_data_wires[pack_size] = data
        self.read_narrow_valid_wires[pack_size] = valid

        valid_cond = vtypes.Ands(valid, self.read_op_sel == op_id)

        fsm.Delay(1)(
            wvalid(0)
        )
        fsm.If(valid_cond)(
            wdata(vtypes.Cat(data, wdata[self.datawidth:ram_datawidth])),
            wvalid(0),
            pack_count.inc()
        )
        fsm.If(valid_cond, pack_count == pack_size - 1)(
            wdata(vtypes.Cat(data, wdata[self.datawidth:ram_datawidth])),
            wvalid(1),
            pack_count(0)
        )

        fsm.If(valid, last)(
            cur_global_addr.add(optimize(cur_size * (self.datawidth // 8)))
        )
        fsm.If(valid, last, rest_size > 0).goto(check_state)
        fsm.If(valid, last, rest_size == 0).goto_next()

        for _ in range(self.num_data_delay):
            fsm.goto_next()

        # state 4
        set_idle = self._set_flag(fsm)
        self.seq.If(set_idle)(
            self.read_idle(1)
        )

        fsm.goto_init()

    def _synthesize_read_fsm_wide(self, ram, port, ram_method, ram_datawidth):
        """ axi.datawidth > ram.datawidth """

        if self.datawidth % ram_datawidth != 0:
            raise ValueError(
                'axi.datawidth must be multiple number of ram_datawidth')

        pack_size = self.datawidth // ram_datawidth
        shamt = int(math.log(pack_size, 2))
        res = vtypes.Mux(
            vtypes.And(self.read_size, 2 ** shamt - 1) > 0, 1, 0)
        dma_size = (self.read_size >> shamt) + res

        actual_read_size = dma_size << shamt

        op_id = self._get_read_op_id(ram, port, ram_method)
        port = vtypes.to_int(port)

        if op_id in self.read_ops:
            """ already synthesized op """
            return

        if pack_size in self.read_wide_fsms:
            """ new op """
            self.read_ops.append(op_id)

            fsm = self.read_wide_fsms[pack_size]
            pack_count = self.read_wide_pack_counts[pack_size]
            data = self.read_wide_data_wires[pack_size]
            valid = self.read_wide_valid_wires[pack_size]

            # state 0
            fsm.set_index(0)
            wdata, wvalid, w = self._get_op_write_dataflow(ram_datawidth)
            cond = vtypes.Ands(self.read_start, self.read_op_sel == op_id)
            ram_method(port, self.read_local_addr, w, actual_read_size,
                       stride=self.read_local_stride, cond=cond)

            fsm.If(cond).goto_next()

            # state 3
            fsm.set_index(3)
            valid_cond = vtypes.Ands(valid, self.read_op_sel == op_id)
            stay_cond = self.read_op_sel == op_id

            fsm.Delay(1)(
                wvalid(0)
            )
            fsm.If(pack_count == 0, valid_cond)(
                wdata(data),
                wvalid(1),
                pack_count.inc()
            )
            fsm.If(pack_count > 0, stay_cond)(
                wdata(wdata >> ram_datawidth),
                wvalid(1),
                pack_count.inc()
            )

            return

        """ new op and fsm """
        fsm = FSM(self.m, '_'.join(['', self.name,
                                    'read_wide', str(pack_size),
                                    'fsm']),
                  self.clk, self.rst, as_module=self.fsm_as_module)
        self.read_wide_fsms[pack_size] = fsm

        self.read_ops.append(op_id)

        cur_global_addr = self.m.Reg('_'.join(['', self.name,
                                               'read_wide', str(pack_size),
                                               'cur_global_addr']),
                                     self.addrwidth, initval=0)
        cur_size = self.m.Reg('_'.join(['', self.name,
                                        'read_wide', str(pack_size),
                                        'cur_size']),
                              self.addrwidth + 1, initval=0)
        rest_size = self.m.Reg('_'.join(['', self.name,
                                         'read_wide', str(pack_size),
                                         'rest_size']),
                               self.addrwidth + 1, initval=0)
        max_burstlen = 2 ** self.burst_size_width

        # state 0
        wdata, wvalid, w = self._get_op_write_dataflow(ram_datawidth)
        cond = vtypes.Ands(self.read_start, self.read_op_sel == op_id)
        ram_method(port, self.read_local_addr, w, actual_read_size,
                   stride=self.read_local_stride, cond=cond)

        if not self.use_global_base_addr:
            gaddr = self.read_global_addr
        else:
            gaddr = self.read_global_addr + self.global_base_addr

        fsm.If(self.read_start)(
            cur_global_addr(self.mask_addr(gaddr)),
            rest_size(dma_size)
        )
        fsm.If(cond).goto_next()

        # state 1
        check_state = fsm.current
        self._check_4KB_boundary(fsm, max_burstlen,
                                 cur_global_addr, cur_size, rest_size)

        # state 2
        last_done = self.m.Reg('_'.join(['', self.name,
                                         'read_wide', str(pack_size),
                                         'last_done']), initval=0)
        fsm(
            last_done(0)
        )

        ack, counter = self.read_request(cur_global_addr, cur_size, cond=fsm)
        fsm.If(ack).goto_next()

        # state 3
        pack_count = self.m.Reg('_'.join(['', self.name,
                                          'read_wide', str(pack_size),
                                          'pack_count']),
                                int(math.ceil(math.log(pack_size, 2))), initval=0)
        self.read_wide_pack_counts[pack_size] = pack_count

        cond = vtypes.Ands(fsm.here, pack_count == 0)
        data, valid, last = self.read_data(cond=cond)
        self.read_wide_data_wires[pack_size] = data
        self.read_wide_valid_wires[pack_size] = valid

        valid_cond = vtypes.Ands(valid, self.read_op_sel == op_id)
        stay_cond = self.read_op_sel == op_id

        fsm.Delay(1)(
            wvalid(0)
        )
        fsm.If(pack_count == 0, valid_cond)(
            wdata(data),
            wvalid(1),
            pack_count.inc()
        )
        fsm.If(pack_count > 0, stay_cond)(
            wdata(wdata >> ram_datawidth),
            wvalid(1),
            pack_count.inc()
        )
        fsm.If(pack_count == pack_size - 1)(
            pack_count(0)
        )

        fsm.If(pack_count == 0, valid, last)(
            last_done(1)
        )

        fsm.If(last_done, pack_count == pack_size - 1)(
            cur_global_addr.add(optimize(cur_size * (self.datawidth // 8)))
        )
        fsm.If(last_done, pack_count == pack_size - 1,
               rest_size > 0).goto(check_state)
        fsm.If(last_done, pack_count == pack_size - 1,
               rest_size == 0).goto_next()

        for _ in range(self.num_data_delay):
            fsm.goto_next()

        # state 4
        set_idle = self._set_flag(fsm)
        self.seq.If(set_idle)(
            self.read_idle(1)
        )

        fsm.goto_init()

    # --------------------
    # write
    # --------------------
    def _dma_write(self, fsm, ram, local_addr, global_addr, size,
                   local_stride=1, port=0, ram_method=None):

        if isinstance(ram, (tuple, list)):
            ram = to_multibank_ram(ram)

        if not isinstance(ram, (RAM, MultibankRAM)):
            raise TypeError('RAM object is required.')

        if ram_method is None:
            ram_method = getattr(ram, 'read_dataflow')

        start = self._set_flag(fsm)

        for _ in range(self.num_cmd_delay + 1):
            fsm.goto_next()

        self._set_write_request(ram, port, ram_method, start,
                                local_addr, global_addr, size, local_stride)

        self._synthesize_write_fsm(ram, port, ram_method)

        fsm.goto_next()

    def _set_write_request(self, ram, port, ram_method, start,
                           local_addr, global_addr, size, local_stride):

        op_id = self._get_write_op_id(ram, port, ram_method)

        if op_id in self.write_reqs:
            (write_start, write_op_sel,
             write_local_addr_in, write_global_addr_in,
             write_size_in, write_local_stride_in) = self.write_reqs[op_id]

            self.seq.If(start)(
                write_start(1),
                write_op_sel(op_id),
                write_local_addr_in(local_addr),
                write_global_addr_in(global_addr),
                write_size_in(size),
                write_local_stride_in(local_stride)
            )

            return

        port = str(vtypes.to_int(port))

        write_start = self.m.Reg(
            '_'.join(['', self.name, ram.name, port, 'write_start']),
            initval=0)
        write_op_sel = self.m.Reg(
            '_'.join(['', self.name, ram.name, port, 'write_op_sel']),
            self.op_sel_width, initval=0)
        write_local_addr = self.m.Reg(
            '_'.join(['', self.name, ram.name, port, 'write_local_addr']),
            self.addrwidth, initval=0)
        write_global_addr = self.m.Reg(
            '_'.join(['', self.name, ram.name, port, 'write_global_addr']),
            self.addrwidth, initval=0)
        write_size = self.m.Reg(
            '_'.join(['', self.name, ram.name, port, 'write_size']),
            self.addrwidth + 1, initval=0)
        write_local_stride = self.m.Reg(
            '_'.join(['', self.name, ram.name, port, 'write_local_stride']),
            self.addrwidth, initval=0)

        self.seq(
            write_start(0)
        )
        self.seq.If(start)(
            write_start(1),
            write_op_sel(op_id),
            write_local_addr(local_addr),
            write_global_addr(global_addr),
            write_size(size),
            write_local_stride(local_stride)
        )

        self.write_reqs[op_id] = (write_start, write_op_sel,
                                  write_local_addr, write_global_addr,
                                  write_size, write_local_stride)

        if self.num_cmd_delay > 0:
            write_start = self.seq.Prev(write_start, self.num_cmd_delay)
            write_op_sel = self.seq.Prev(write_op_sel, self.num_cmd_delay)
            write_local_addr = self.seq.Prev(
                write_local_addr, self.num_cmd_delay)
            write_global_addr = self.seq.Prev(
                write_global_addr, self.num_cmd_delay)
            write_size = self.seq.Prev(write_size, self.num_cmd_delay)
            write_local_stride = self.seq.Prev(
                write_local_stride, self.num_cmd_delay)

        self.seq.If(write_start)(
            self.write_idle(0)
        )

        self.seq.If(write_start)(
            self.write_start(1),
            self.write_op_sel(write_op_sel),
            self.write_local_addr(write_local_addr),
            self.write_global_addr(write_global_addr),
            self.write_size(write_size),
            self.write_local_stride(write_local_stride)
        )

    def _synthesize_write_fsm(self, ram, port, ram_method):

        ram_method_name = (ram_method.func.__name__
                           if isinstance(ram_method, functools.partial) else
                           ram_method.__name__)
        ram_datawidth = (ram.datawidth if ram_method is None else
                         ram.orig_datawidth if 'bcast' in ram_method_name else
                         ram.orig_datawidth if 'block' in ram_method_name else
                         ram.datawidth)

        if not isinstance(self.datawidth, int):
            raise TypeError("axi.datawidth must be int, not '%s'" %
                            str(type(self.datawidth)))

        if not isinstance(ram_datawidth, int):
            raise TypeError("ram_datawidth must be int, not '%s'" %
                            str(type(ram_datawidth)))

        if self.datawidth == ram_datawidth:
            return self._synthesize_write_fsm_same(ram, port, ram_method, ram_datawidth)

        if self.datawidth < ram_datawidth:
            return self._synthesize_write_fsm_narrow(ram, port, ram_method, ram_datawidth)

        return self._synthesize_write_fsm_wide(ram, port, ram_method, ram_datawidth)

    def _synthesize_write_fsm_same(self, ram, port, ram_method, ram_datawidth):

        op_id = self._get_write_op_id(ram, port, ram_method)
        port = vtypes.to_int(port)

        if op_id in self.write_ops:
            """ already synthesized op """
            return

        if self.write_fsm is not None:
            """ new op """
            self.write_ops.append(op_id)

            fsm = self.write_fsm
            counter = self.write_data_counter

            # state 0
            fsm.set_index(0)
            cond = vtypes.Ands(self.write_start, self.write_op_sel == op_id)
            data, last, done = ram_method(
                port, self.write_local_addr, self.write_size,
                stride=self.write_local_stride, cond=cond, signed=False)

            if self.num_data_delay > 0:
                for _ in range(self.num_data_delay):
                    data = self.df._Delay(data)
                    last = self.df._Delay(last)

            fsm.If(cond).goto_next()

            # state 3
            fsm.set_index(3)
            cond = vtypes.Ands(fsm.here, self.write_op_sel == op_id)
            done_out = self.write_dataflow(data, counter, cond=cond)
            add_mux(self.write_data_done, done_out, 1)

            return

        """ new op and fsm """
        fsm = FSM(self.m, '_'.join(['', self.name, 'write_fsm']),
                  self.clk, self.rst, as_module=self.fsm_as_module)
        self.write_fsm = fsm

        self.write_ops.append(op_id)

        cur_global_addr = self.m.Reg('_'.join(['', self.name, 'write_cur_global_addr']),
                                     self.addrwidth, initval=0)
        cur_size = self.m.Reg('_'.join(['', self.name, 'write_cur_size']),
                              self.addrwidth + 1, initval=0)
        rest_size = self.m.Reg('_'.join(['', self.name, 'write_rest_size']),
                               self.addrwidth + 1, initval=0)
        max_burstlen = 2 ** self.burst_size_width

        # state 0
        cond = vtypes.Ands(self.write_start, self.write_op_sel == op_id)
        data, last, done = ram_method(
            port, self.write_local_addr, self.write_size,
            stride=self.write_local_stride, cond=cond, signed=False)

        if self.num_data_delay > 0:
            for _ in range(self.num_data_delay):
                data = self.df._Delay(data)
                last = self.df._Delay(last)

        if not self.use_global_base_addr:
            gaddr = self.write_global_addr
        else:
            gaddr = self.write_global_addr + self.global_base_addr

        fsm.If(self.write_start)(
            cur_global_addr(self.mask_addr(gaddr)),
            rest_size(self.write_size)
        )
        fsm.If(cond).goto_next()

        # state 1
        check_state = fsm.current
        self._check_4KB_boundary(fsm, max_burstlen,
                                 cur_global_addr, cur_size, rest_size)

        # state 2
        ack, counter = self.write_request(cur_global_addr, cur_size, cond=fsm)
        self.write_data_counter = counter
        fsm.If(ack).goto_next()

        # state 3
        cond = vtypes.Ands(fsm.here, self.write_op_sel == op_id)
        done_out = self.write_dataflow(data, counter, cond=cond)
        add_mux(self.write_data_done, done_out, 1)

        fsm.If(self.write_data_done)(
            cur_global_addr.add(optimize(cur_size * (self.datawidth // 8)))
        )
        fsm.If(self.write_data_done, rest_size > 0).goto(check_state)
        fsm.If(self.write_data_done, rest_size == 0).goto_next()

        # state 4
        set_idle = self._set_flag(fsm)
        self.seq.If(set_idle)(
            self.write_idle(1)
        )

        fsm.goto_init()

    def _synthesize_write_fsm_narrow(self, ram, port, ram_method, ram_datawidth):
        """ axi.datawidth < ram.datawidth """

        if ram_datawidth % self.datawidth != 0:
            raise ValueError(
                'ram_datawidth must be multiple number of axi.datawidth')

        pack_size = ram_datawidth // self.datawidth
        dma_size = (self.write_size << int(math.log(pack_size, 2))
                    if math.log(pack_size, 2) % 1.0 == 0.0 else
                    self.write_size * pack_size)

        op_id = self._get_write_op_id(ram, port, ram_method)
        port = vtypes.to_int(port)

        if op_id in self.write_ops:
            """ already synthesized op """
            return

        if pack_size in self.write_narrow_fsms:
            """ new op """
            self.write_ops.append(op_id)

            fsm = self.write_narrow_fsms[pack_size]
            wdata = self.write_narrow_wdatas[pack_size]
            wvalid = self.write_narrow_wvalids[pack_size]
            wready = self.write_narrow_wreadys[pack_size]
            pack_count = self.write_narrow_pack_counts[pack_size]

            # state 0
            fsm.set_index(0)
            cond = vtypes.Ands(self.write_start, self.write_op_sel == op_id)
            data, last, done = ram_method(
                port, self.write_local_addr, self.write_size,
                stride=self.write_local_stride, cond=cond, signed=False)

            if self.num_data_delay > 0:
                for _ in range(self.num_data_delay):
                    data = self.df._Delay(data)
                    last = self.df._Delay(last)

            fsm.If(cond).goto_next()

            # state 3
            fsm.set_index(3)
            ack = vtypes.Ors(wready, vtypes.Not(wvalid))
            cond = vtypes.Ands(fsm.here, ack, pack_count == 0,
                               self.write_op_sel == op_id)
            rdata, rvalid = data.read(cond=cond)

            stay_cond = self.write_op_sel == op_id

            self.seq.If(rvalid, stay_cond)(
                wdata(rdata),
                wvalid(1),
                pack_count.inc()
            )
            self.seq.If(ack, pack_count > 0, stay_cond)(
                wdata(wdata >> self.datawidth),
                wvalid(1),
                pack_count.inc()
            )
            self.seq.If(ack, pack_count == pack_size - 1, stay_cond)(
                wdata(wdata >> self.datawidth),
                wvalid(1),
                pack_count(0)
            )

            return

        """ new op and fsm """
        fsm = FSM(self.m, '_'.join(['', self.name,
                                    'write_narrow', str(pack_size),
                                    'fsm']),
                  self.clk, self.rst, as_module=self.fsm_as_module)
        self.write_narrow_fsms[pack_size] = fsm

        self.write_ops.append(op_id)

        cur_global_addr = self.m.Reg('_'.join(['', self.name,
                                               'write_narrow', str(pack_size),
                                               'cur_global_addr']),
                                     self.addrwidth, initval=0)
        cur_size = self.m.Reg('_'.join(['', self.name,
                                        'write_narrow', str(pack_size),
                                        'cur_size']),
                              self.addrwidth + 1, initval=0)
        rest_size = self.m.Reg('_'.join(['', self.name,
                                         'write_narrow', str(pack_size),
                                         'rest_size']),
                               self.addrwidth + 1, initval=0)
        max_burstlen = 2 ** self.burst_size_width

        # state 0
        cond = vtypes.Ands(self.write_start, self.write_op_sel == op_id)
        data, last, done = ram_method(
            port, self.write_local_addr, self.write_size,
            stride=self.write_local_stride, cond=cond, signed=False)

        if self.num_data_delay > 0:
            for _ in range(self.num_data_delay):
                data = self.df._Delay(data)
                last = self.df._Delay(last)

        if not self.use_global_base_addr:
            gaddr = self.write_global_addr
        else:
            gaddr = self.write_global_addr + self.global_base_addr

        fsm.If(self.write_start)(
            cur_global_addr(self.mask_addr(gaddr)),
            rest_size(dma_size)
        )
        fsm.If(cond).goto_next()

        # state 1
        check_state = fsm.current
        self._check_4KB_boundary(fsm, max_burstlen,
                                 cur_global_addr, cur_size, rest_size)

        # state 2
        ack, counter = self.write_request(cur_global_addr, cur_size, cond=fsm)
        fsm.If(ack).goto_next()

        # state 3
        wdata = self.m.Reg('_'.join(['', self.name,
                                     'write_narrow', str(pack_size),
                                     'wdata']),
                           ram_datawidth, initval=0)
        self.write_narrow_wdatas[pack_size] = wdata
        wvalid = self.m.Reg('_'.join(['', self.name,
                                      'write_narrow', str(pack_size),
                                      'wvalid']),
                            initval=0)
        self.write_narrow_wvalids[pack_size] = wvalid
        wready = self.m.Wire('_'.join(['', self.name,
                                       'write_narrow', str(pack_size),
                                       'wready']))
        self.write_narrow_wreadys[pack_size] = wready
        pack_count = self.m.Reg('_'.join(['', self.name,
                                          'write_narrow', str(pack_size),
                                          'pack_count']),
                                int(math.ceil(math.log(pack_size, 2))), initval=0)
        self.write_narrow_pack_counts[pack_size] = pack_count

        ack = vtypes.Ors(wready, vtypes.Not(wvalid))
        cond = vtypes.Ands(fsm.here, ack, pack_count == 0,
                           self.write_op_sel == op_id)
        rdata, rvalid = data.read(cond=cond)

        stay_cond = self.write_op_sel == op_id

        self.seq.If(ack)(
            wvalid(0)
        )
        self.seq.If(rvalid, stay_cond)(
            wdata(rdata),
            wvalid(1),
            pack_count.inc()
        )
        self.seq.If(ack, pack_count > 0, stay_cond)(
            wdata(wdata >> self.datawidth),
            wvalid(1),
            pack_count.inc()
        )
        self.seq.If(ack, pack_count == pack_size - 1, stay_cond)(
            wdata(wdata >> self.datawidth),
            wvalid(1),
            pack_count(0)
        )

        data = self.df.Variable(wdata, wvalid, wready,
                                width=self.datawidth, signed=False)

        done = self.write_dataflow(data, counter, cond=fsm)

        fsm.If(done)(
            cur_global_addr.add(optimize(cur_size * (self.datawidth // 8)))
        )
        fsm.If(done, rest_size > 0).goto(check_state)
        fsm.If(done, rest_size == 0).goto_next()

        # state 4
        set_idle = self._set_flag(fsm)
        self.seq.If(set_idle)(
            self.write_idle(1)
        )

        fsm.goto_init()

    def _synthesize_write_fsm_wide(self, ram, port, ram_method, ram_datawidth):
        """ axi.datawidth > ram.datawidth """

        if self.datawidth % ram_datawidth != 0:
            raise ValueError(
                'axi.datawidth must be multiple number of ram_datawidth')

        pack_size = self.datawidth // ram_datawidth
        shamt = int(math.log(pack_size, 2))
        res = vtypes.Mux(
            vtypes.And(self.write_size, 2 ** shamt - 1) > 0, 1, 0)
        dma_size = (self.write_size >> shamt) + res

        actual_write_size = dma_size << shamt

        op_id = self._get_write_op_id(ram, port, ram_method)
        port = vtypes.to_int(port)

        if op_id in self.write_ops:
            """ already synthesized op """
            return

        if pack_size in self.write_wide_fsms:
            """ new op """
            self.write_ops.append(op_id)

            fsm = self.write_wide_fsms[pack_size]
            wdata = self.write_wide_wdatas[pack_size]
            wvalid = self.write_wide_wvalids[pack_size]
            wready = self.write_wide_wreadys[pack_size]
            pack_count = self.write_wide_pack_counts[pack_size]

            # state 0
            fsm.set_index(0)
            cond = vtypes.Ands(self.write_start, self.write_op_sel == op_id)
            data, last, done = ram_method(
                port, self.write_local_addr, actual_write_size,
                stride=self.write_local_stride, cond=cond, signed=False)

            if self.num_data_delay > 0:
                for _ in range(self.num_data_delay):
                    data = self.df._Delay(data)
                    last = self.df._Delay(last)

            fsm.If(cond).goto_next()

            # state 3
            fsm.set_index(3)
            ack = vtypes.Ors(wready, vtypes.Not(wvalid))
            cond = vtypes.Ands(fsm.here, ack, self.write_op_sel == op_id)
            rdata, rvalid = data.read(cond=cond)

            self.seq.If(rvalid)(
                wdata(vtypes.Cat(rdata, wdata[ram_datawidth:self.datawidth])),
                wvalid(0),
                pack_count.inc()
            )
            self.seq.If(rvalid, pack_count == pack_size - 1)(
                wdata(vtypes.Cat(rdata, wdata[ram_datawidth:self.datawidth])),
                wvalid(1),
                pack_count(0)
            )

            return

        """ new op and fsm """
        fsm = FSM(self.m, '_'.join(['', self.name,
                                    'write_wide', str(pack_size),
                                    'fsm']),
                  self.clk, self.rst, as_module=self.fsm_as_module)
        self.write_wide_fsms[pack_size] = fsm

        self.write_ops.append(op_id)

        cur_global_addr = self.m.Reg('_'.join(['', self.name,
                                               'write_wide', str(pack_size),
                                               'cur_global_addr']),
                                     self.addrwidth, initval=0)
        cur_size = self.m.Reg('_'.join(['', self.name,
                                        'write_wide', str(pack_size),
                                        'cur_size']),
                              self.addrwidth + 1, initval=0)
        rest_size = self.m.Reg('_'.join(['', self.name,
                                         'write_wide', str(pack_size),
                                         'rest_size']),
                               self.addrwidth + 1, initval=0)
        max_burstlen = 2 ** self.burst_size_width

        # state 0
        cond = vtypes.Ands(self.write_start, self.write_op_sel == op_id)
        data, last, done = ram_method(
            port, self.write_local_addr, actual_write_size,
            stride=self.write_local_stride, cond=cond, signed=False)

        if self.num_data_delay > 0:
            for _ in range(self.num_data_delay):
                data = self.df._Delay(data)
                last = self.df._Delay(last)

        if not self.use_global_base_addr:
            gaddr = self.write_global_addr
        else:
            gaddr = self.write_global_addr + self.global_base_addr

        fsm.If(self.write_start)(
            cur_global_addr(self.mask_addr(gaddr)),
            rest_size(dma_size)
        )
        fsm.If(cond).goto_next()

        # state 1
        check_state = fsm.current
        self._check_4KB_boundary(fsm, max_burstlen,
                                 cur_global_addr, cur_size, rest_size)

        # state 2
        ack, counter = self.write_request(cur_global_addr, cur_size, cond=fsm)
        fsm.If(ack).goto_next()

        # state 3
        wdata = self.m.Reg('_'.join(['', self.name,
                                     'write_wide', str(pack_size),
                                     'wdata']),
                           self.datawidth, initval=0)
        self.write_wide_wdatas[pack_size] = wdata
        wvalid = self.m.Reg('_'.join(['', self.name,
                                      'write_wide', str(pack_size),
                                      'wvalid']),
                            initval=0)
        self.write_wide_wvalids[pack_size] = wvalid
        wready = self.m.Wire('_'.join(['', self.name,
                                       'write_wide', str(pack_size),
                                       'wready']))
        self.write_wide_wreadys[pack_size] = wready
        pack_count = self.m.Reg('_'.join(['', self.name,
                                          'write_wide', str(pack_size),
                                          'pack_count']),
                                int(math.ceil(math.log(pack_size, 2))), initval=0)
        self.write_wide_pack_counts[pack_size] = pack_count

        ack = vtypes.Ors(wready, vtypes.Not(wvalid))
        cond = vtypes.Ands(fsm.here, ack, self.write_op_sel == op_id)
        rdata, rvalid = data.read(cond=cond)

        self.seq.If(ack)(
            wvalid(0)
        )
        self.seq.If(rvalid)(
            wdata(vtypes.Cat(rdata, wdata[ram_datawidth:self.datawidth])),
            wvalid(0),
            pack_count.inc()
        )
        self.seq.If(rvalid, pack_count == pack_size - 1)(
            wdata(vtypes.Cat(rdata, wdata[ram_datawidth:self.datawidth])),
            wvalid(1),
            pack_count(0)
        )

        data = self.df.Variable(wdata, wvalid, wready,
                                width=self.datawidth, signed=False)

        done = self.write_dataflow(data, counter, cond=fsm)

        fsm.If(done)(
            cur_global_addr.add(optimize(cur_size * (self.datawidth // 8)))
        )
        fsm.If(done, rest_size > 0).goto(check_state)
        fsm.If(done, rest_size == 0).goto_next()

        # state 4
        set_idle = self._set_flag(fsm)
        self.seq.If(set_idle)(
            self.write_idle(1)
        )

        fsm.goto_init()

    def _set_flag(self, fsm, prefix='axim_flag'):
        flag = self.m.TmpReg(initval=0, prefix=prefix)
        fsm(
            flag(1)
        )
        fsm.Delay(1)(
            flag(0)
        )
        fsm.goto_next()
        return flag

    def _get_read_op_id(self, ram, port, ram_method):

        ram_id = ram._id()
        port = vtypes.to_int(port)
        ram_method_name = (ram_method.func.__name__
                           if isinstance(ram_method, functools.partial) else
                           ram_method.__name__)
        op = (ram_id, port, ram_method_name)

        if op in self.read_op_id_map:
            op_id = self.read_op_id_map[op]
        else:
            op_id = self.read_op_id_count
            self.read_op_id_count += 1
            self.read_op_id_map[op] = op_id

        return op_id

    def _get_op_write_dataflow(self, ram_datawidth):
        if self.datawidth == ram_datawidth:
            wdata = self.m.TmpReg(ram_datawidth, initval=0, prefix='_wdata')
            wvalid = self.m.TmpReg(initval=0, prefix='_wvalid')
            w = self.df.Variable(wdata, wvalid,
                                 width=ram_datawidth, signed=False)
            if self.num_data_delay > 0:
                for _ in range(self.num_data_delay):
                    w = self.df._Delay(w)

            return (wdata, wvalid, w)

        if self.datawidth < ram_datawidth:
            wdata = self.m.TmpReg(ram_datawidth, initval=0, prefix='_wdata')
            wvalid = self.m.TmpReg(initval=0, prefix='_wvalid')
            w = self.df.Variable(wdata, wvalid,
                                 width=ram_datawidth, signed=False)
            if self.num_data_delay > 0:
                for _ in range(self.num_data_delay):
                    w = self.df._Delay(w)

            return (wdata, wvalid, w)

        wdata = self.m.TmpReg(self.datawidth, initval=0, prefix='_wdata')
        wdata_ram = self.m.TmpWire(ram_datawidth, prefix='_wdata_ram')
        wdata_ram.assign(wdata)
        wvalid = self.m.TmpReg(initval=0, prefix='_wvalid')
        w = self.df.Variable(wdata_ram, wvalid,
                             width=ram_datawidth, signed=False)
        if self.num_data_delay > 0:
            for _ in range(self.num_data_delay):
                w = self.df._Delay(w)

        return (wdata, wvalid, w)

    def _get_write_op_id(self, ram, port, ram_method):

        ram_id = ram._id()
        port = vtypes.to_int(port)
        ram_method_name = (ram_method.func.__name__
                           if isinstance(ram_method, functools.partial) else
                           ram_method.__name__)
        op = (ram_id, port, ram_method_name)

        if op in self.write_op_id_map:
            op_id = self.write_op_id_map[op]
        else:
            op_id = self.write_op_id_count
            self.write_op_id_count += 1
            self.write_op_id_map[op] = op_id

        return op_id

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


class AXIMLite(axi.AxiLiteMaster, _MutexFunction):
    """ AXI-Lite Master Interface """

    __intrinsics__ = ('read', 'write',
                      'set_global_base_addr',) + _MutexFunction.__intrinsics__

    burstlen = 256

    def __init__(self, m, name, clk, rst, datawidth=32, addrwidth=32,
                 waddr_cache_mode=axi.CACHE_HP, raddr_cache_mode=axi.CACHE_HP,
                 noio=False,
                 use_global_base_addr=False,
                 fsm_as_module=False):

        axi.AxiLiteMaster.__init__(self, m, name, clk, rst, datawidth, addrwidth,
                                   waddr_cache_mode, raddr_cache_mode,
                                   noio)

        self.use_global_base_addr = use_global_base_addr
        self.fsm_as_module = fsm_as_module

        self.mutex = None

    def read(self, fsm, global_addr):
        if self.use_global_base_addr:
            global_addr = self.global_base_addr + global_addr

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

        rdata = self.m.TmpReg(self.datawidth, initval=0,
                              signed=True, prefix='axim_rdata')
        fsm.If(valid)(rdata(data))
        fsm.Then().goto_next()

        return rdata

    def write(self, fsm, global_addr, value):
        if self.use_global_base_addr:
            global_addr = self.global_base_addr + global_addr

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

    def set_global_base_addr(self, fsm, addr):

        if not self.use_global_base_addr:
            raise ValueError("global_base_addr is disabled.")

        flag = self._set_flag(fsm)
        self.seq.If(flag)(
            self.global_base_addr(addr)
        )


class AXIS(axi.AxiSlave, _MutexFunction):
    __intrinsics__ = _MutexFunction.__intrinsics__

    def __init__(self, m, name, clk, rst, datawidth=32, addrwidth=32,
                 waddr_id_width=0, wdata_id_width=0, wresp_id_width=0,
                 raddr_id_width=0, rdata_id_width=0,
                 waddr_user_width=1, wdata_user_width=0, wresp_user_width=0,
                 raddr_user_width=1, rdata_user_width=0,
                 wresp_user_value=axi.USER_DEFAULT,
                 rdata_user_value=axi.USER_DEFAULT,
                 noio=False):

        axi.AxiSlave.__init__(self, m, name, clk, rst, datawidth, addrwidth,
                              waddr_id_width, wdata_id_width, wresp_id_width,
                              raddr_id_width, rdata_id_width,
                              waddr_user_width, wdata_user_width, wresp_user_width,
                              raddr_user_width, rdata_user_width,
                              wresp_user_value,
                              rdata_user_value,
                              noio)
        self.mutex = None


class AXISLite(axi.AxiLiteSlave, _MutexFunction):
    def __init__(self, m, name, clk, rst, datawidth=32, addrwidth=32,
                 noio=False):

        axi.AxiLiteSlave.__init__(self, m, name, clk, rst, datawidth, addrwidth,
                                  noio)
        self.mutex = None


class AXISRegister(AXIS):
    __intrinsics__ = ('read', 'write', 'write_flag', 'wait',
                      'wait_flag') + _MutexFunction.__intrinsics__

    def __init__(self, m, name, clk, rst, datawidth=32, addrwidth=32,
                 waddr_id_width=0, wdata_id_width=0, wresp_id_width=0,
                 raddr_id_width=0, rdata_id_width=0,
                 waddr_user_width=1, wdata_user_width=0, wresp_user_width=0,
                 raddr_user_width=1, rdata_user_width=0,
                 wresp_user_value=axi.USER_DEFAULT,
                 rdata_user_value=axi.USER_DEFAULT,
                 noio=False, length=4, fsm_as_module=False):

        AXIS.__init__(self, m, name, clk, rst, datawidth, addrwidth,
                      waddr_id_width, wdata_id_width, wresp_id_width,
                      raddr_id_width, rdata_id_width,
                      waddr_user_width, wdata_user_width, wresp_user_width,
                      raddr_user_width, rdata_user_width,
                      wresp_user_value,
                      rdata_user_value,
                      noio)

        self.fsm_as_module = fsm_as_module

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

        self._set_register_full_fsm()

    def _set_register_full_fsm(self):
        fsm = FSM(self.m, '_'.join(['', self.name, 'register_fsm']),
                  self.clk, self.rst, as_module=self.fsm_as_module)

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


class AXISLiteRegister(AXISLite):
    __intrinsics__ = ('read', 'write', 'write_flag', 'wait',
                      'wait_flag') + _MutexFunction.__intrinsics__

    def __init__(self, m, name, clk, rst, datawidth=32, addrwidth=32,
                 noio=False, length=4, fsm_as_module=False):

        AXISLite.__init__(self, m, name, clk, rst, datawidth, addrwidth,
                          noio)

        self.fsm_as_module = fsm_as_module

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

        self._set_register_lite_fsm()

    def _set_register_lite_fsm(self):
        fsm = FSM(self.m, '_'.join(['', self.name, 'register_fsm']),
                  self.clk, self.rst, as_module=self.fsm_as_module)

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


def add_mux(targ, cond, value):
    prev_assign = targ._get_assign()
    if not prev_assign:
        targ.assign(vtypes.Mux(cond, value, 0))
    else:
        prev_value = prev_assign.statement.right
        prev_assign.overwrite_right(
            vtypes.Mux(cond, value, prev_value))
        targ.module.remove(prev_assign)
        targ.module.append(prev_assign)
