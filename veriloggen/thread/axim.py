from __future__ import absolute_import
from __future__ import print_function

import math
import functools
from collections import OrderedDict

import veriloggen.core.vtypes as vtypes
import veriloggen.types.util as util
import veriloggen.types.axi as axi
from veriloggen.fsm.fsm import FSM
from veriloggen.optimizer import try_optimize as optimize
from veriloggen.seq.seq import make_condition

from .ttypes import _MutexFunction
from .ram import RAM, MultibankRAM, to_multibank_ram
from .fifo import FIFO


class AXIM(axi.AxiMaster, _MutexFunction):
    """ AXI Master Interface with DMA controller """

    __intrinsics__ = ('read', 'write',
                      'dma_read', 'dma_read_async',
                      'dma_write', 'dma_write_async',
                      'dma_wait_read', 'dma_wait_write',
                      'dma_wait_write_idle', 'dma_wait_write_response',
                      'dma_wait',
                      'set_global_base_addr',) + _MutexFunction.__intrinsics__

    burstlen = 256

    def __init__(self, m, name, clk, rst, datawidth=32, addrwidth=32,
                 waddr_id_width=0, wdata_id_width=0, wresp_id_width=0,
                 raddr_id_width=0, rdata_id_width=0,
                 waddr_user_width=2, wdata_user_width=0, wresp_user_width=0,
                 raddr_user_width=2, rdata_user_width=0,
                 waddr_burst_mode=axi.BURST_INCR, raddr_burst_mode=axi.BURST_INCR,
                 waddr_cache_mode=axi.AxCACHE_NONCOHERENT, raddr_cache_mode=axi.AxCACHE_NONCOHERENT,
                 waddr_prot_mode=axi.AxPROT_NONCOHERENT, raddr_prot_mode=axi.AxPROT_NONCOHERENT,
                 waddr_user_mode=axi.AxUSER_NONCOHERENT, wdata_user_mode=axi.xUSER_DEFAULT,
                 raddr_user_mode=axi.AxUSER_NONCOHERENT,
                 noio=False,
                 enable_async=False, use_global_base_addr=False,
                 op_sel_width=8, req_fifo_addrwidth=3, fsm_as_module=False):

        axi.AxiMaster.__init__(self, m, name, clk, rst, datawidth, addrwidth,
                               waddr_id_width, wdata_id_width, wresp_id_width,
                               raddr_id_width, rdata_id_width,
                               waddr_user_width, wdata_user_width, wresp_user_width,
                               raddr_user_width, rdata_user_width,
                               waddr_burst_mode, raddr_burst_mode,
                               waddr_cache_mode, raddr_cache_mode,
                               waddr_prot_mode, raddr_prot_mode,
                               waddr_user_mode, wdata_user_mode,
                               raddr_user_mode,
                               noio)

        self.enable_async = enable_async
        self.use_global_base_addr = use_global_base_addr
        self.op_sel_width = op_sel_width
        self.req_fifo_addrwidth = req_fifo_addrwidth
        self.fsm_as_module = fsm_as_module

        self.mutex = None

        # Read
        self.read_start = self.m.Reg('_'.join(['', self.name, 'read_start']),
                                     initval=0)
        self.read_op_sel = self.m.Reg('_'.join(['', self.name, 'read_op_sel']),
                                      self.op_sel_width, initval=0)
        self.read_global_addr = self.m.Reg('_'.join(['', self.name, 'read_global_addr']),
                                           self.addrwidth, initval=0)
        self.read_global_size = self.m.Reg('_'.join(['', self.name, 'read_global_size']),
                                           self.addrwidth + 1, initval=0)
        self.read_local_addr = self.m.Reg('_'.join(['', self.name, 'read_local_addr']),
                                          self.addrwidth, initval=0)
        self.read_local_stride = self.m.Reg('_'.join(['', self.name, 'read_local_stride']),
                                            self.addrwidth, initval=0)
        self.read_local_size = self.m.Reg('_'.join(['', self.name, 'read_local_size']),
                                          self.addrwidth + 1, initval=0)

        self.read_req_fifo = FIFO(self.m, '_'.join(['', self.name, 'read_req_fifo']),
                                  self.clk, self.rst,
                                  datawidth=self.op_sel_width + self.addrwidth * 3 + 1,
                                  addrwidth=self.req_fifo_addrwidth,
                                  sync=False)

        self.read_op_sel_fifo = self.m.Wire('_'.join(['', self.name,
                                                      'read_op_sel_fifo']),
                                            self.op_sel_width)
        self.read_local_addr_fifo = self.m.Wire('_'.join(['', self.name,
                                                          'read_local_addr_fifo']),
                                                self.addrwidth)
        self.read_local_stride_fifo = self.m.Wire('_'.join(['', self.name,
                                                            'read_local_stride_fifo']),
                                                  self.addrwidth)
        self.read_local_size_fifo = self.m.Wire('_'.join(['', self.name,
                                                          'read_local_size_fifo']),
                                                self.addrwidth + 1)

        read_unpack_values = self.unpack_read_req(self.read_req_fifo.rdata)
        self.read_op_sel_fifo.assign(read_unpack_values[0])
        self.read_local_addr_fifo.assign(read_unpack_values[1])
        self.read_local_stride_fifo.assign(read_unpack_values[2])
        self.read_local_size_fifo.assign(read_unpack_values[3])

        self.read_op_sel_buf = self.m.Reg('_'.join(['', self.name,
                                                    'read_op_sel_buf']),
                                          self.op_sel_width, initval=0)
        self.read_local_addr_buf = self.m.Reg('_'.join(['', self.name,
                                                        'read_local_addr_buf']),
                                              self.addrwidth, initval=0)
        self.read_local_stride_buf = self.m.Reg('_'.join(['', self.name,
                                                          'read_local_stride_buf']),
                                                self.addrwidth, initval=0)
        self.read_local_size_buf = self.m.Reg('_'.join(['', self.name,
                                                        'read_local_size_buf']),
                                              self.addrwidth + 1, initval=0)

        self.read_req_idle =  self.m.Reg(
            '_'.join(['', self.name, 'read_req_idle']), initval=1)
        self.read_data_idle = self.m.Reg(
            '_'.join(['', self.name, 'read_data_idle']), initval=1)

        self.read_idle = self.m.Wire('_'.join(['', self.name, 'read_idle']))
        self.read_idle.assign(
            vtypes.Ands(vtypes.Not(self.read_start), self.read_req_idle,
                        self.read_req_fifo.empty, self.read_data_idle))

        self.seq(
            self.read_start(0)
        )

        self.read_op_id_map = OrderedDict()
        self.read_op_id_count = 1
        self.read_ops = []

        self.read_req_fsm = None
        self.read_data_fsm = None
        self.read_data_narrow_fsm = None
        self.read_data_wide_fsm = None

        # Write
        self.write_start = self.m.Reg('_'.join(['', self.name, 'write_start']),
                                      initval=0)
        self.write_op_sel = self.m.Reg('_'.join(['', self.name, 'write_op_sel']),
                                       self.op_sel_width, initval=0)
        self.write_global_addr = self.m.Reg('_'.join(['', self.name, 'write_global_addr']),
                                            self.addrwidth, initval=0)
        self.write_global_size = self.m.Reg('_'.join(['', self.name, 'write_global_size']),
                                         self.addrwidth + 1, initval=0)
        self.write_local_addr = self.m.Reg('_'.join(['', self.name, 'write_local_addr']),
                                           self.addrwidth, initval=0)
        self.write_local_stride = self.m.Reg('_'.join(['', self.name, 'write_local_stride']),
                                             self.addrwidth, initval=0)
        self.write_local_size = self.m.Reg('_'.join(['', self.name, 'write_local_size']),
                                     self.addrwidth + 1, initval=0)

        self.write_req_fifo = FIFO(self.m, '_'.join(['', self.name, 'write_req_fifo']),
                                   self.clk, self.rst,
                                   datawidth=self.op_sel_width + self.addrwidth * 3 + 1 + 1,
                                   addrwidth=self.req_fifo_addrwidth,
                                   sync=False)

        self.write_op_sel_fifo = self.m.Wire('_'.join(['', self.name,
                                                       'write_op_sel_fifo']),
                                             self.op_sel_width)
        self.write_local_addr_fifo = self.m.Wire('_'.join(['', self.name,
                                                           'write_local_addr_fifo']),
                                                 self.addrwidth)
        self.write_local_stride_fifo = self.m.Wire('_'.join(['', self.name,
                                                             'write_local_stride_fifo']),
                                                   self.addrwidth)
        self.write_local_size_fifo = self.m.Wire('_'.join(['', self.name,
                                                           'write_local_size_fifo']),
                                                 self.addrwidth + 1)
        self.write_update_local_addr_fifo = self.m.Wire('_'.join(['', self.name,
                                                                  'write_update_local_addr_fifo']))

        write_unpack_values = self.unpack_write_req(self.write_req_fifo.rdata)
        self.write_op_sel_fifo.assign(write_unpack_values[0])
        self.write_local_addr_fifo.assign(write_unpack_values[1])
        self.write_local_stride_fifo.assign(write_unpack_values[2])
        self.write_local_size_fifo.assign(write_unpack_values[3])
        self.write_update_local_addr_fifo.assign(write_unpack_values[4])

        self.write_op_sel_buf = self.m.Reg('_'.join(['', self.name,
                                                     'write_op_sel_buf']),
                                           self.op_sel_width, initval=0)
        self.write_local_addr_buf = self.m.Reg('_'.join(['', self.name,
                                                         'write_local_addr_buf']),
                                               self.addrwidth, initval=0)
        self.write_local_stride_buf = self.m.Reg('_'.join(['', self.name,
                                                           'write_local_stride_buf']),
                                                 self.addrwidth, initval=0)
        self.write_local_size_buf = self.m.Reg('_'.join(['', self.name,
                                                         'write_local_size_buf']),
                                               self.addrwidth + 1, initval=0)

        self.write_req_idle =  self.m.Reg(
            '_'.join(['', self.name, 'write_req_idle']), initval=1)
        self.write_data_idle = self.m.Reg(
            '_'.join(['', self.name, 'write_data_idle']), initval=1)

        self.write_idle = self.m.Wire('_'.join(['', self.name, 'write_idle']))
        self.write_idle.assign(
            vtypes.Ands(vtypes.Not(self.write_start), self.write_req_idle,
                        self.write_req_fifo.empty, self.write_data_idle))

        self.seq(
            self.write_start(0)
        )

        self.write_op_id_map = OrderedDict()
        self.write_op_id_count = 1
        self.write_ops = []

        self.write_req_fsm = None
        self.write_data_fsm = None
        self.write_data_narrow_fsm = None
        self.write_data_wide_fsm = None

        if self.use_global_base_addr:
            self.global_base_addr = self.m.Reg('_'.join(['', self.name, 'global_base_addr']),
                                               self.addrwidth, initval=0)
        else:
            self.global_base_addr = None

    def read(self, fsm, global_addr):
        ### ???
        if self.use_global_base_addr:
            global_addr = self.global_base_addr + global_addr

        ack, counter = self.read_request_counter(global_addr, length=1, cond=fsm)
        fsm.If(ack).goto_next()

        ret = self.read_data(counter, cond=fsm)
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
        ### ???
        if self.use_global_base_addr:
            global_addr = self.global_base_addr + global_addr

        ack, counter = self.write_request_counter(global_addr, length=1, cond=fsm)
        fsm.If(ack).goto_next()

        ret = self.write_data(value, counter, cond=fsm)
        if isinstance(ret, (tuple)):
            ack, last = ret
        else:
            ack, last = ret, None

        fsm.If(ack).goto_next()

    def dma_read(self, fsm, ram, local_addr, global_addr, size,
                 local_stride=1, port=0, ram_method=None):

        self._dma_read(fsm, ram, local_addr, global_addr, size,
                       local_stride, port, ram_method)

        self.dma_wait_read(fsm)

    def dma_read_async(self, fsm, ram, local_addr, global_addr, size,
                       local_stride=1, port=0, ram_method=None):

        if not self.enable_async:
            raise ValueError(
                "Async mode is disabled. Set 'True' to AXIM.enable_async.")

        self._dma_read(fsm, ram, local_addr, global_addr, size,
                       local_stride, port, ram_method)

    def dma_write(self, fsm, ram, local_addr, global_addr, size,
                  local_stride=1, port=0, ram_method=None):

        self._dma_write(fsm, ram, local_addr, global_addr, size,
                        local_stride, port, ram_method)

        self.dma_wait_write(fsm)

    def dma_write_async(self, fsm, ram, local_addr, global_addr, size,
                        local_stride=1, port=0, ram_method=None):

        if not self.enable_async:
            raise ValueError(
                "Async mode is disabled. Set 'True' to AXIM.enable_async.")

        self._dma_write(fsm, ram, local_addr, global_addr, size,
                        local_stride, port, ram_method)

    def dma_wait_read(self, fsm):

        fsm.If(self.read_idle).goto_next()

    def dma_wait_write(self, fsm):

        res = self.write_completed()
        fsm.If(self.write_idle, res).goto_next()

    def dma_wait_write_idle(self, fsm):

        fsm.If(self.write_idle).goto_next()

    def dma_wait_write_response(self, fsm):

        res = self.write_completed()
        fsm.If(res).goto_next()

    def dma_wait(self, fsm):

        res = self.write_completed()
        fsm.If(self.read_idle, self.write_idle, res).goto_next()

    def set_global_base_addr(self, fsm, addr):

        if not self.use_global_base_addr:
            raise ValueError("global_base_addr is disabled.")

        flag = self._set_flag(fsm)
        self.seq.If(flag)(
            self.global_base_addr(addr)
        )
        fsm.goto_next()

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
            ram_method = getattr(ram, 'write_burst')

        start = vtypes.Ands(fsm.here, self.read_req_idle)

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

        self._set_read_request(ram, port, ram_method, ram_datawidth,
                               start, local_addr, global_addr, size, local_stride)
        self._synthesize_read_req_fsm()
        self._synthesize_read_data_fsm(ram, port, ram_method, ram_datawidth)

        fsm.If(self.read_req_idle).goto_next()

    def _set_read_request(self, ram, port, ram_method, ram_datawidth,
                          start, local_addr, global_addr, size, local_stride):

        if self.datawidth == ram_datawidth:
            # same
            global_size = size

        elif self.datawidth < ram_datawidth:
            # narrow
            pack_size = ram_datawidth // self.datawidth
            global_size = (size << int(math.log(pack_size, 2))
                           if pack_size & (pack_size - 1) == 0 else
                           size * pack_size)

        elif self.datawidth > ram_datawidth:
            # wide
            pack_size = self.datawidth // ram_datawidth
            shamt = int(math.log(pack_size, 2))
            res = vtypes.Mux(
                vtypes.And(size, 2 ** shamt - 1) > 0, 1, 0)
            global_size = (size >> shamt) + res

        local_size = size
        op_id = self._get_read_op_id(ram, port, ram_method)

        self.seq.If(start)(
            self.read_start(1),
            self.read_op_sel(op_id),
            self.read_global_addr(global_addr),
            self.read_global_size(global_size),
            self.read_local_addr(local_addr),
            self.read_local_stride(local_stride),
            self.read_local_size(local_size),
        )

    def _synthesize_read_req_fsm(self):

        if self.read_req_fsm is not None:
            return

        req_fsm = FSM(self.m, '_'.join(['', self.name, 'read_req_fsm']),
                      self.clk, self.rst, as_module=self.fsm_as_module)
        self.read_req_fsm = req_fsm

        cur_global_addr = self.m.Reg('_'.join(['', self.name, 'read_cur_global_addr']),
                                     self.addrwidth, initval=0)
        cur_global_size = self.m.Reg('_'.join(['', self.name, 'read_cur_global_size']),
                              self.addrwidth + 1, initval=0)
        rest_global_size = self.m.Reg('_'.join(['', self.name, 'read_rest_global_size']),
                               self.addrwidth + 1, initval=0)
        max_burstlen = 2 ** self.burst_size_width

        # Req state 0
        if not self.use_global_base_addr:
            gaddr = self.read_global_addr
        else:
            gaddr = self.read_global_addr + self.global_base_addr

        req_fsm.If(self.read_start)(
            cur_global_addr(self.mask_addr(gaddr)),
            rest_global_size(self.read_global_size),
            self.read_req_idle(0)
        )

        enq_cond = vtypes.Ands(req_fsm.here, self.read_start)

        _ = self.read_req_fifo.enq_rtl(self.pack_read_req(self.read_op_sel,
                                                          self.read_local_addr,
                                                          self.read_local_stride,
                                                          self.read_local_size),
                                       cond=enq_cond)
        req_fsm.If(self.read_start).goto_next()

        # Req state 1
        check_state = req_fsm.current
        self._check_4KB_boundary(req_fsm, max_burstlen,
                                 cur_global_addr, cur_global_size, rest_global_size)

        # Req state 2
        ack = self.read_request(cur_global_addr, cur_global_size, cond=req_fsm)
        req_fsm.goto_next()

        # Req state 3
        req_fsm.If(ack)(
            cur_global_addr.add(optimize(cur_global_size * (self.datawidth // 8)))
        )
        req_fsm.If(ack).goto(check_state)
        req_fsm.If(ack, rest_global_size == 0).goto_init()
        self.seq.If(req_fsm.here, ack, rest_global_size == 0)(
            self.read_req_idle(1)
        )

    def _synthesize_read_data_fsm(self, ram, port, ram_method, ram_datawidth):

        if self.datawidth == ram_datawidth:
            return self._synthesize_read_data_fsm_same(ram, port, ram_method, ram_datawidth)

        if self.datawidth < ram_datawidth:
            return self._synthesize_read_data_fsm_narrow(ram, port, ram_method, ram_datawidth)

        return self._synthesize_read_data_fsm_wide(ram, port, ram_method, ram_datawidth)

    def _synthesize_read_data_fsm_same(self, ram, port, ram_method, ram_datawidth):

        op_id = self._get_read_op_id(ram, port, ram_method)
        port = vtypes.to_int(port)

        if op_id in self.read_ops:
            """ already synthesized op """
            return

        if self.read_data_fsm is not None:
            """ new op """
            self.read_ops.append(op_id)

            data_fsm = self.read_data_fsm

            # Data state 1
            data_fsm.set_index(1)
            ram_cond = vtypes.Ands(data_fsm.here, self.read_op_sel_buf == op_id)
            ram_method(
                self.read_local_addr_buf, self.read_local_stride_buf, self.read_local_size_buf,
                self.rdata.rdata, self.rdata.rvalid, False,
                port=port, cond=ram_cond)
            return

        # Data FSM
        self.read_ops.append(op_id)

        data_fsm = FSM(self.m, '_'.join(['', self.name, 'read_data_fsm']),
                      self.clk, self.rst, as_module=self.fsm_as_module)
        self.read_data_fsm = data_fsm

        # Data state 0
        cond = vtypes.Ands(self.read_data_idle,
                           vtypes.Not(self.read_req_fifo.empty))
        self.seq.If(data_fsm.here, cond)(
            self.read_data_idle(0),
            self.read_op_sel_buf(self.read_op_sel_fifo),
            self.read_local_addr_buf(self.read_local_addr_fifo),
            self.read_local_stride_buf(self.read_local_stride_fifo),
            self.read_local_size_buf(self.read_local_size_fifo),
        )
        deq_cond = vtypes.Ands(data_fsm.here, cond)
        _ = self.read_req_fifo.deq_rtl(cond=deq_cond)
        data_fsm.If(cond).goto_next()

        # Data state 1
        ram_cond = vtypes.Ands(data_fsm.here, self.read_op_sel_buf == op_id)
        ram_method(self.read_local_addr_buf, self.read_local_stride_buf, self.read_local_size_buf,
                   self.rdata.rdata, self.rdata.rvalid, False,
                   port=port, cond=ram_cond)
        data_fsm.goto_next()

        # Data state 2
        _ = self.read_data(cond=data_fsm)
        self.seq.If(data_fsm.here, self.rdata.rvalid)(
            self.read_local_size_buf.dec()
        )

        data_fsm.If(self.rdata.rvalid, self.read_local_size_buf <= 1).goto_init()
        self.seq.If(data_fsm.here, self.rdata.rvalid, self.read_local_size_buf <= 1)(
            self.read_data_idle(1)
        )

    def _synthesize_read_data_fsm_narrow(self, ram, port, ram_method, ram_datawidth):
        """ axi.datawidth < ram.datawidth """

        if ram_datawidth % self.datawidth != 0:
            raise ValueError(
                'ram_datawidth must be multiple number of axi.datawidth')

        op_id = self._get_read_op_id(ram, port, ram_method)
        port = vtypes.to_int(port)
        pack_size = ram_datawidth // self.datawidth
        log_pack_size = int(math.log(pack_size, 2))

        if op_id in self.read_ops:
            """ already synthesized op """
            return

        if self.read_data_narrow_fsm is not None:
            """ new op """
            self.read_ops.append(op_id)

            data_fsm = self.read_data_narrow_fsm

            # Data state 1
            data_fsm.set_index(1)
            ram_cond = vtypes.Ands(data_fsm.here, self.read_op_sel_buf == op_id)
            wdata = self.m.TmpReg(ram_datawidth, initval=0,
                                  prefix='_'.join(['', self.name, 'read_narrow_wdata']))
            wvalid = self.m.TmpReg(initval=0,
                                   prefix='_'.join(['', self.name, 'read_narrow_wvalid']))
            count = self.m.TmpReg(log_pack_size, initval=0,
                                  prefix='_'.join(['', self.name, 'read_narrow_count']))
            ram_method(
                self.read_local_addr_buf, self.read_local_stride_buf, self.read_local_size_buf,
                wdata, wvalid, False, port=port, cond=ram_cond)
            data_fsm(
                count(0),
                wvalid(0)
            )

            # Data state 2
            data_fsm.set_index(2)
            cond = self.read_op_sel_buf == op_id
            data_fsm.If(cond)(
                wvalid(0)
            )
            data_fsm.If(cond, self.rdata.rvalid, count < pack_size - 1)(
                count.inc(),
                wdata(vtypes.Cat(self.rdata.rdata, wdata[self.datawidth:])),
                wvalid(0),
            )
            data_fsm.If(cond, self.rdata.rvalid, count == pack_size - 1)(
                count(0),
                wdata(vtypes.Cat(self.rdata.rdata, wdata[self.datawidth:])),
                wvalid(1)
            )
            self.seq.If(data_fsm.here, cond, self.rdata.rvalid, count == pack_size - 1)(
                self.read_local_size_buf.dec()
            )
            data_fsm.If(cond, self.rdata.rvalid, self.read_local_size_buf <= 1,
                        count == pack_size -1).goto_init()
            self.seq.If(data_fsm.here, cond, self.rdata.rvalid, self.read_local_size_buf <= 1,
                        count == pack_size - 1)(
                self.read_data_idle(1)
            )
            return

        # Data FSM
        self.read_ops.append(op_id)

        data_fsm = FSM(self.m, '_'.join(['', self.name, 'read_data_narrow_fsm']),
                      self.clk, self.rst, as_module=self.fsm_as_module)
        self.read_data_narrow_fsm = data_fsm

        # Data state 0
        cond = vtypes.Ands(self.read_data_idle,
                           vtypes.Not(self.read_req_fifo.empty))
        self.seq.If(data_fsm.here, cond)(
            self.read_data_idle(0),
            self.read_op_sel_buf(self.read_op_sel_fifo),
            self.read_local_addr_buf(self.read_local_addr_fifo),
            self.read_local_stride_buf(self.read_local_stride_fifo),
            self.read_local_size_buf(self.read_local_size_fifo),
        )
        deq_cond = vtypes.Ands(data_fsm.here, cond)
        _ = self.read_req_fifo.deq_rtl(cond=deq_cond)
        data_fsm.If(cond).goto_next()

        # Data state 1
        ram_cond = vtypes.Ands(data_fsm.here, self.read_op_sel_buf == op_id)
        wdata = self.m.TmpReg(ram_datawidth, initval=0,
                              prefix='_'.join(['', self.name, 'read_narrow_wdata']))
        wvalid = self.m.TmpReg(initval=0, prefix='_'.join(['', self.name, 'read_narrow_wvalid']))
        count = self.m.TmpReg(log_pack_size, initval=0,
                              prefix='_'.join(['', self.name, 'read_narrow_count']))
        ram_method(self.read_local_addr_buf, self.read_local_stride_buf, self.read_local_size_buf,
                   wdata, wvalid, False, port=port, cond=ram_cond)
        data_fsm(
            count(0),
            wvalid(0)
        )
        data_fsm.goto_next()

        # Data state 2
        _ = self.read_data(cond=data_fsm)
        cond = self.read_op_sel_buf == op_id
        data_fsm.If(cond)(
            wvalid(0)
        )
        data_fsm.If(cond, self.rdata.rvalid, count < pack_size - 1)(
            count.inc(),
            wdata(vtypes.Cat(self.rdata.rdata, wdata[self.datawidth:])),
            wvalid(0),
        )
        data_fsm.If(cond, self.rdata.rvalid, count == pack_size - 1)(
            count(0),
            wdata(vtypes.Cat(self.rdata.rdata, wdata[self.datawidth:])),
            wvalid(1)
        )
        self.seq.If(data_fsm.here, cond, self.rdata.rvalid, count == pack_size - 1)(
            self.read_local_size_buf.dec()
        )

        data_fsm.If(cond, self.rdata.rvalid, self.read_local_size_buf <= 1,
                    count == pack_size -1).goto_init()
        self.seq.If(data_fsm.here, cond, self.rdata.rvalid, self.read_local_size_buf <= 1,
                    count == pack_size - 1)(
            self.read_data_idle(1)
        )

    def _synthesize_read_data_fsm_wide(self, ram, port, ram_method, ram_datawidth):
        """ axi.datawidth > ram.datawidth """

        if self.datawidth % ram_datawidth != 0:
            raise ValueError(
                'axi.datawidth must be multiple number of ram_datawidth')

        op_id = self._get_read_op_id(ram, port, ram_method)
        port = vtypes.to_int(port)
        pack_size = self.datawidth // ram_datawidth
        log_pack_size = int(math.log(pack_size, 2))

        if op_id in self.read_ops:
            """ already synthesized op """
            return

        if self.read_data_wide_fsm is not None:
            """ new op """
            self.read_ops.append(op_id)

            data_fsm = self.read_data_wide_fsm

            # Data state 1
            data_fsm.set_index(1)
            ram_cond = vtypes.Ands(data_fsm.here, self.read_op_sel_buf == op_id)
            wdata = self.m.TmpReg(self.datawidth, initval=0,
                                  prefix='_'.join(['', self.name, 'read_wide_wdata']))
            wvalid = self.m.TmpReg(initval=0, prefix='_'.join(['', self.name, 'read_wide_wvalid']))
            count = self.m.TmpReg(log_pack_size, initval=0,
                                  prefix='_'.join(['', self.name, 'read_wide_count']))
            _wdata = wdata[:ram_datawidth]
            ram_method(
                self.read_local_addr_buf, self.read_local_stride_buf, self.read_local_size_buf,
                _wdata, wvalid, False, port=port, cond=ram_cond)
            data_fsm(
                count(0),
                wvalid(0)
            )

            # Data state 2
            data_fsm.set_index(2)
            cond = self.read_op_sel_buf == op_id
            rcond = vtypes.Ands(data_fsm.here, cond, count == 0)
            _ = self.read_data(cond=rcond)
            data_fsm.If(cond)(
                wvalid(0)
            )
            data_fsm.If(cond, self.rdata.rvalid, count == 0)(
                count.inc(),
                wdata(self.rdata.rdata),
                wvalid(1),
            )
            self.seq.If(data_fsm.here, cond, self.rdata.rvalid, count == 0)(
                self.read_local_size_buf.dec()
            )
            data_fsm.If(cond, count > 0)(
                count.inc(),
                wdata(wdata >> ram_datawidth),
                wvalid(1),
            )
            self.seq.If(data_fsm.here, cond, count > 0)(
                self.read_local_size_buf.dec()
            )
            data_fsm.If(cond, count == pack_size - 1)(
                count(0)
            )

            data_fsm.If(self.read_local_size_buf <= 1,
                        cond, count > 0).goto_init()
            data_fsm.If(self.read_local_size_buf <= 1,
                        cond, self.rdata.rvalid, count == 0).goto_init()
            self.seq.If(data_fsm.here, self.read_local_size_buf <= 1,
                        cond, count > 0)(
                self.read_data_idle(1)
            )
            self.seq.If(data_fsm.here, self.read_local_size_buf <= 1,
                        cond, self.rdata.rvalid, count == 0)(
                 self.read_data_idle(1)
            )
            return

        # Data FSM
        self.read_ops.append(op_id)

        data_fsm = FSM(self.m, '_'.join(['', self.name, 'read_data_wide_fsm']),
                      self.clk, self.rst, as_module=self.fsm_as_module)
        self.read_data_wide_fsm = data_fsm

        # Data state 0
        cond = vtypes.Ands(self.read_data_idle,
                           vtypes.Not(self.read_req_fifo.empty))
        self.seq.If(data_fsm.here, cond)(
            self.read_data_idle(0),
            self.read_op_sel_buf(self.read_op_sel_fifo),
            self.read_local_addr_buf(self.read_local_addr_fifo),
            self.read_local_stride_buf(self.read_local_stride_fifo),
            self.read_local_size_buf(self.read_local_size_fifo),
        )
        deq_cond = vtypes.Ands(data_fsm.here, cond)
        _ = self.read_req_fifo.deq_rtl(cond=deq_cond)
        data_fsm.If(cond).goto_next()

        # Data state 1
        ram_cond = vtypes.Ands(data_fsm.here, self.read_op_sel_buf == op_id)
        wdata = self.m.TmpReg(self.datawidth, initval=0,
                              prefix='_'.join(['', self.name, 'read_wide_wdata']))
        wvalid = self.m.TmpReg(initval=0, prefix='_'.join(['', self.name, 'read_wide_wvalid']))
        count = self.m.TmpReg(log_pack_size, initval=0,
                              prefix='_'.join(['', self.name, 'read_wide_count']))
        _wdata = wdata[:ram_datawidth]
        ram_method(self.read_local_addr_buf, self.read_local_stride_buf, self.read_local_size_buf,
                   _wdata, wvalid, False, port=port, cond=ram_cond)
        data_fsm(
            count(0),
            wvalid(0)
        )
        data_fsm.goto_next()

        # Data state 2
        cond = self.read_op_sel_buf == op_id
        rcond = vtypes.Ands(data_fsm.here, cond, count == 0)
        _ = self.read_data(cond=rcond)
        data_fsm.If(cond)(
            wvalid(0)
        )
        data_fsm.If(cond, self.rdata.rvalid, count == 0)(
            count.inc(),
            wdata(self.rdata.rdata),
            wvalid(1),
        )
        self.seq.If(data_fsm.here, cond, self.rdata.rvalid, count == 0)(
            self.read_local_size_buf.dec()
        )
        data_fsm.If(cond, count > 0)(
            count.inc(),
            wdata(wdata >> ram_datawidth),
            wvalid(1),
        )
        self.seq.If(data_fsm.here, cond, count > 0)(
            self.read_local_size_buf.dec()
        )
        data_fsm.If(cond, count == pack_size - 1)(
            count(0)
        )

        data_fsm.If(self.read_local_size_buf <= 1,
                    cond, count > 0).goto_init()
        data_fsm.If(self.read_local_size_buf <= 1,
                    cond, self.rdata.rvalid, count == 0).goto_init()
        self.seq.If(data_fsm.here, self.read_local_size_buf <= 1,
                    cond, count > 0)(
            self.read_data_idle(1)
        )
        self.seq.If(data_fsm.here, self.read_local_size_buf <= 1,
                    cond, self.rdata.rvalid, count == 0)(
            self.read_data_idle(1)
        )

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
            ram_method = getattr(ram, 'read_burst')

        start = vtypes.Ands(fsm.here, self.write_req_idle)

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

        self._set_write_request(ram, port, ram_method, ram_datawidth,
                                start, local_addr, global_addr, size, local_stride)
        self._synthesize_write_req_fsm()
        self._synthesize_write_data_fsm(ram, port, ram_method, ram_datawidth)

        fsm.If(self.write_req_idle).goto_next()

    def _set_write_request(self, ram, port, ram_method, ram_datawidth,
                           start, local_addr, global_addr, size, local_stride):

        if self.datawidth == ram_datawidth:
            # same
            global_size = size

        elif self.datawidth < ram_datawidth:
            # narrow
            pack_size = ram_datawidth // self.datawidth
            global_size = (size << int(math.log(pack_size, 2))
                           if pack_size & (pack_size - 1) == 0 else
                           size * pack_size)

        elif self.datawidth > ram_datawidth:
            # wide
            pack_size = self.datawidth // ram_datawidth
            shamt = int(math.log(pack_size, 2))
            res = vtypes.Mux(
                vtypes.And(size, 2 ** shamt - 1) > 0, 1, 0)
            global_size = (size >> shamt) + res

        local_size = size
        op_id = self._get_write_op_id(ram, port, ram_method)

        self.seq.If(start)(
            self.write_start(1),
            self.write_op_sel(op_id),
            self.write_global_addr(global_addr),
            self.write_global_size(global_size),
            self.write_local_addr(local_addr),
            self.write_local_stride(local_stride),
            self.write_local_size(local_size),
        )

    def _synthesize_write_req_fsm(self):

        if self.write_req_fsm is not None:
            return

        req_fsm = FSM(self.m, '_'.join(['', self.name, 'write_req_fsm']),
                      self.clk, self.rst, as_module=self.fsm_as_module)
        self.write_req_fsm = req_fsm

        cur_global_addr = self.m.Reg('_'.join(['', self.name, 'write_cur_global_addr']),
                                     self.addrwidth, initval=0)
        cur_local_addr = self.m.Reg('_'.join(['', self.name, 'write_cur_local_addr']),
                                    self.addrwidth, initval=0)
        cur_global_size = self.m.Reg('_'.join(['', self.name, 'write_cur_global_size']),
                              self.addrwidth + 1, initval=0)
        rest_global_size = self.m.Reg('_'.join(['', self.name, 'write_rest_global_size']),
                               self.addrwidth + 1, initval=0)
        update_local_addr = self.m.Reg('_'.join(['', self.name, 'write_update_local_addr']),
                                         initval=1)
        max_burstlen = 2 ** self.burst_size_width

        # Req state 0
        if not self.use_global_base_addr:
            gaddr = self.write_global_addr
        else:
            gaddr = self.write_global_addr + self.global_base_addr

        req_fsm.If(self.write_start)(
            cur_global_addr(self.mask_addr(gaddr)),
            cur_local_addr(self.write_local_addr),
            rest_global_size(self.write_global_size),
            update_local_addr(1),
            self.write_req_idle(0)
        )
        req_fsm.If(self.write_start).goto_next()

        # Req state 1
        check_state = req_fsm.current
        self._check_4KB_boundary(req_fsm, max_burstlen,
                                 cur_global_addr, cur_global_size, rest_global_size)

        # Req state 2
        cond = vtypes.Ands(req_fsm.here, self.write_acceptable())
        ack = self.write_request(cur_global_addr, cur_global_size, cond=cond)
        req_fsm.goto_next()

        # Req state 3
        enq_cond = vtypes.Ands(req_fsm.here, ack)
        _ = self.write_req_fifo.enq_rtl(self.pack_write_req(self.write_op_sel,
                                                            cur_local_addr,
                                                            self.write_local_stride,
                                                            cur_global_size,
                                                            update_local_addr),
                                        cond=enq_cond)

        req_fsm.If(ack)(
            cur_global_addr.add(optimize(cur_global_size * (self.datawidth // 8))),
            update_local_addr(0),
        )
        req_fsm.If(ack).goto(check_state)
        req_fsm.If(ack, rest_global_size == 0).goto_init()
        self.seq.If(req_fsm.here, ack, rest_global_size == 0)(
            self.write_req_idle(1)
        )

    def _synthesize_write_data_fsm(self, ram, port, ram_method, ram_datawidth):

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
            return self._synthesize_write_data_fsm_same(ram, port, ram_method, ram_datawidth)

        if self.datawidth < ram_datawidth:
            return self._synthesize_write_data_fsm_narrow(ram, port, ram_method, ram_datawidth)

        return self._synthesize_write_data_fsm_wide(ram, port, ram_method, ram_datawidth)

    def _synthesize_write_data_fsm_same(self, ram, port, ram_method, ram_datawidth):

        op_id = self._get_write_op_id(ram, port, ram_method)
        port = vtypes.to_int(port)

        if op_id in self.write_ops:
            """ already synthesized op """
            return

        if self.write_data_fsm is not None:
            """ new op """
            self.write_ops.append(op_id)

            data_fsm = self.write_data_fsm

            # Data state 1
            data_fsm.set_index(1)
            ram_cond = vtypes.Ands(data_fsm.here, self.write_op_sel_buf == op_id)
            rready = vtypes.Ors(self.wdata.wready, vtypes.Not(self.wdata.wvalid))
            rdata, rvalid, rlast = ram_method(
                self.write_local_addr_buf, self.write_local_stride_buf, self.write_local_size_buf,
                rready, port=port, cond=ram_cond)

            cond = self.write_op_sel_buf == op_id
            self.seq.If(cond, rvalid, rready)(
                self.write_local_addr_buf.add(self.write_local_stride_buf)
            )

            # Data state 2
            data_fsm.set_index(2)
            wcond = vtypes.Ands(cond, rvalid)
            _ = self.write_data(rdata, rlast, cond=wcond)

            data_fsm.If(wcond, rlast).goto_init()
            self.seq.If(data_fsm.here, wcond, rlast)(
                self.write_data_idle(1)
            )
            return

        # Data FSM
        self.write_ops.append(op_id)

        data_fsm = FSM(self.m, '_'.join(['', self.name, 'write_data_fsm']),
                      self.clk, self.rst, as_module=self.fsm_as_module)
        self.write_data_fsm = data_fsm

        # Data state 0
        cond = vtypes.Ands(self.write_data_idle,
                           vtypes.Not(self.write_req_fifo.empty))
        self.seq.If(data_fsm.here, cond)(
            self.write_data_idle(0),
            self.write_op_sel_buf(self.write_op_sel_fifo),
            self.write_local_stride_buf(self.write_local_stride_fifo),
            self.write_local_size_buf(self.write_local_size_fifo),
        )
        self.seq.If(data_fsm.here, cond, self.write_update_local_addr_fifo)(
            self.write_local_addr_buf(self.write_local_addr_fifo),
        )
        deq_cond = vtypes.Ands(data_fsm.here, cond)
        _ = self.write_req_fifo.deq_rtl(cond=deq_cond)
        data_fsm.If(cond).goto_next()

        # Data state 1
        ram_cond = vtypes.Ands(data_fsm.here, self.write_op_sel_buf == op_id)
        rready = vtypes.Ors(self.wdata.wready, vtypes.Not(self.wdata.wvalid))
        rdata, rvalid, rlast = ram_method(
            self.write_local_addr_buf, self.write_local_stride_buf, self.write_local_size_buf,
            rready, port=port, cond=ram_cond)

        cond = self.write_op_sel_buf == op_id
        self.seq.If(cond, rvalid, rready)(
            self.write_local_addr_buf.add(self.write_local_stride_buf)
        )
        data_fsm.goto_next()

        # Data state 2
        wcond = vtypes.Ands(cond, rvalid)
        _ = self.write_data(rdata, rlast, cond=wcond)

        data_fsm.If(wcond, rlast).goto_init()
        self.seq.If(data_fsm.here, wcond, rlast)(
            self.write_data_idle(1)
        )

    def _synthesize_write_data_fsm_narrow(self, ram, port, ram_method, ram_datawidth):
        """ axi.datawidth < ram.datawidth """

        if ram_datawidth % self.datawidth != 0:
            raise ValueError(
                'ram_datawidth must be multiple number of axi.datawidth')

        op_id = self._get_write_op_id(ram, port, ram_method)
        port = vtypes.to_int(port)
        pack_size = ram_datawidth // self.datawidth
        log_pack_size = int(math.log(pack_size, 2))

        if op_id in self.write_ops:
            """ already synthesized op """
            return

        if self.write_data_narrow_fsm is not None:
            """ new op """
            self.write_ops.append(op_id)

            data_fsm = self.read_data_narrow_fsm

            # Data state 1
            data_fsm.set_index(1)
            ram_cond = vtypes.Ands(data_fsm.here, self.write_op_sel_buf == op_id)
            count = self.m.TmpReg(log_pack_size, initval=0,
                                  prefix='_'.join(['', self.name, 'write_narrow_count']))
            rready = vtypes.Ands(vtypes.Ors(self.wdata.wready, vtypes.Not(self.wdata.wvalid)),
                                 count == 0)
            rdata, rvalid, rlast = ram_method(
                self.write_local_addr_buf, self.write_local_stride_buf, self.write_local_size_buf,
                rready, port=port, cond=ram_cond)

            cond = self.write_op_sel_buf == op_id
            self.seq.If(cond, rvalid, rready)(
                self.write_local_addr_buf.add(self.write_local_stride_buf)
            )

            data_fsm(
                count(0)
            )

            # Data state 2
            data_fsm.set_index(2)
            rstate = data_fsm.current
            cond = self.write_op_sel == op_id
            wack = vtypes.Ors(self.wdata.wready, vtypes.Not(self.wdata.wvalid))
            wcond = vtypes.Ands(data_fsm.here, cond, rvalid, wack)
            wdata = self.m.TmpReg(ram_datawidth, initval=0,
                                  prefix='_'.join(['', self.name, 'write_narrow_wdata']))
            wlast = self.m.TmpReg(initval=0,
                                  prefix='_'.join(['', self.name, 'write_narrow_wlast']))
            _ = self.write_data(rdata[:self.datawidth], False, cond=wcond)
            data_fsm.If(wcond)(
                wdata(rdata[self.datawidth:]),
                wlast(rlast),
                count.inc(),
            )
            data_fsm.If(wcond).goto_next()

            # Data state 3
            data_fsm.set_index(3)
            cond = self.write_op_sel == op_id
            wack = vtypes.Ors(self.wdata.wready, vtypes.Not(self.wdata.wvalid))
            wcond = vtypes.Ands(data_fsm.here, cond, wack)
            _wdata = wdata[:self.datawidth]
            _wlast = vtypes.Ands(wlast, count == pack_size - 1)
            _ = self.write_data(_wdata, _wlast, cond=wcond)
            data_fsm.If(wcond)(
                wdata(wdata >> self.datawidth),
                count.inc()
            )
            data_fsm.If(wcond, count == pack_size - 1)(
                count(0)
            )
            data_fsm.If(wcond, count == pack_size - 1).goto(rstate)
            data_fsm.If(wcond, count == pack_size - 1, wlast).goto_init()

            self.seq.If(data_fsm.here, wcond, count == pack_size - 1, wlast)(
                self.write_data_idle(1)
            )

            return

        # Data FSM
        self.write_ops.append(op_id)

        data_fsm = FSM(self.m, '_'.join(['', self.name, 'write_data_narrow_fsm']),
                      self.clk, self.rst, as_module=self.fsm_as_module)
        self.write_data_narrow_fsm = data_fsm

        # Data state 0
        cond = vtypes.Ands(self.write_data_idle,
                           vtypes.Not(self.write_req_fifo.empty))
        self.seq.If(data_fsm.here, cond)(
            self.write_data_idle(0),
            self.write_op_sel_buf(self.write_op_sel_fifo),
            self.write_local_stride_buf(self.write_local_stride_fifo),
            self.write_local_size_buf(self.write_local_size_fifo >> log_pack_size),
        )
        self.seq.If(data_fsm.here, cond, self.write_update_local_addr_fifo)(
            self.write_local_addr_buf(self.write_local_addr_fifo),
        )
        deq_cond = vtypes.Ands(data_fsm.here, cond)
        _ = self.write_req_fifo.deq_rtl(cond=deq_cond)
        data_fsm.If(cond).goto_next()

        # Data state 1
        ram_cond = vtypes.Ands(data_fsm.here, self.write_op_sel_buf == op_id)
        count = self.m.TmpReg(log_pack_size, initval=0,
                              prefix='_'.join(['', self.name, 'write_narrow_count']))
        rready = vtypes.Ands(vtypes.Ors(self.wdata.wready, vtypes.Not(self.wdata.wvalid)),
                             count == 0)
        rdata, rvalid, rlast = ram_method(
            self.write_local_addr_buf, self.write_local_stride_buf, self.write_local_size_buf,
            rready, port=port, cond=ram_cond)

        cond = self.write_op_sel_buf == op_id
        self.seq.If(cond, rvalid, rready)(
            self.write_local_addr_buf.add(self.write_local_stride_buf)
        )

        data_fsm(
            count(0)
        )
        data_fsm.goto_next()

        # Data state 2
        rstate = data_fsm.current
        cond = self.write_op_sel == op_id
        wack = vtypes.Ors(self.wdata.wready, vtypes.Not(self.wdata.wvalid))
        wcond = vtypes.Ands(data_fsm.here, cond, rvalid, wack)
        wdata = self.m.TmpReg(ram_datawidth, initval=0,
                              prefix='_'.join(['', self.name, 'write_narrow_wdata']))
        wlast = self.m.TmpReg(initval=0,
                              prefix='_'.join(['', self.name, 'write_narrow_wlast']))
        _ = self.write_data(rdata[:self.datawidth], False, cond=wcond)
        data_fsm.If(wcond)(
            wdata(rdata[self.datawidth:]),
            wlast(rlast),
            count.inc(),
        )
        data_fsm.If(wcond).goto_next()

        # Data state 3
        cond = self.write_op_sel == op_id
        wack = vtypes.Ors(self.wdata.wready, vtypes.Not(self.wdata.wvalid))
        wcond = vtypes.Ands(data_fsm.here, cond, wack)
        _wdata = wdata[:self.datawidth]
        _wlast = vtypes.Ands(wlast, count == pack_size - 1)
        _ = self.write_data(_wdata, _wlast, cond=wcond)
        data_fsm.If(wcond)(
            wdata(wdata >> self.datawidth),
            count.inc(),
        )
        data_fsm.If(wcond, count == pack_size - 1)(
            count(0)
        )
        data_fsm.If(wcond, count == pack_size - 1).goto(rstate)
        data_fsm.If(wcond, count == pack_size - 1, wlast).goto_init()

        self.seq.If(data_fsm.here, wcond, count == pack_size - 1, wlast)(
            self.write_data_idle(1)
        )

    def _synthesize_write_data_fsm_wide(self, ram, port, ram_method, ram_datawidth):
        """ axi.datawidth > ram.datawidth """

        if self.datawidth % ram_datawidth != 0:
            raise ValueError(
                'axi.datawidth must be multiple number of ram_datawidth')

        op_id = self._get_write_op_id(ram, port, ram_method)
        port = vtypes.to_int(port)
        pack_size = self.datawidth // ram_datawidth
        log_pack_size = int(math.log(pack_size, 2))

        if op_id in self.write_ops:
            """ already synthesized op """
            return

        if self.write_data_wide_fsm is not None:
            """ new op """
            self.write_ops.append(op_id)

            data_fsm = self.read_data_wide_fsm

            # Data state 1
            data_fsm.set_index(1)
            ram_cond = vtypes.Ands(data_fsm.here, self.write_op_sel_buf == op_id)
            count = self.m.TmpReg(log_pack_size, initval=0,
                                  prefix='_'.join(['', self.name, 'write_wide_count']))
            rready = vtypes.Ors(self.wdata.wready, vtypes.Not(self.wdata.wvalid),
                                count > 0)
            rdata, rvalid, rlast = ram_method(
                self.write_local_addr_buf, self.write_local_stride_buf, self.write_local_size_buf,
                rready, port=port, cond=ram_cond)

            cond = self.write_op_sel_buf == op_id
            self.seq.If(cond, rvalid, rready)(
                self.write_local_addr_buf.add(self.write_local_stride_buf)
            )

            data_fsm(
                count(0)
            )

            # Data state 1
            data_fsm.set_index(2)
            cond = self.write_op_sel == op_id
            wcond = vtypes.Ands(data_fsm.here, cond, count == pack_size - 1, rvalid)
            wdata = self.m.TmpReg(self.datawidth, initval=0,
                                  prefix='_'.join(['', self.name, 'write_wide_wdata']))
            _wdata = vtypes.Cat(rdata, wdata[ram_datawidth:self.datawidth])
            _ = self.write_data(_wdata, rlast, cond=wcond)
            data_fsm.If(rvalid, rready)(
                wdata(_wdata),
                count.inc(),
            )
            data_fsm.If(rvalid, rready, count == pack_size - 1)(
                count(0)
            )
            data_fsm.If(cond, count == pack_size - 1, rvalid, rlast).goto_init()

            self.seq.If(data_fsm.here, cond, count == pack_size - 1, rvalid, rlast)(
                self.write_data_idle(1)
            )
            return

        # Data FSM
        self.write_ops.append(op_id)

        data_fsm = FSM(self.m, '_'.join(['', self.name, 'write_data_wide_fsm']),
                      self.clk, self.rst, as_module=self.fsm_as_module)
        self.write_data_wide_fsm = data_fsm

        # Data state 0
        cond = vtypes.Ands(self.write_data_idle,
                           vtypes.Not(self.write_req_fifo.empty))
        self.seq.If(data_fsm.here, cond)(
            self.write_data_idle(0),
            self.write_op_sel_buf(self.write_op_sel_fifo),
            self.write_local_stride_buf(self.write_local_stride_fifo),
            self.write_local_size_buf(self.write_local_size_fifo << log_pack_size),
        )
        self.seq.If(data_fsm.here, cond, self.write_update_local_addr_fifo)(
            self.write_local_addr_buf(self.write_local_addr_fifo),
        )
        deq_cond = vtypes.Ands(data_fsm.here, cond)
        _ = self.write_req_fifo.deq_rtl(cond=deq_cond)
        data_fsm.If(cond).goto_next()

        # Data state 1
        ram_cond = vtypes.Ands(data_fsm.here, self.write_op_sel_buf == op_id)
        count = self.m.TmpReg(log_pack_size, initval=0,
                              prefix='_'.join(['', self.name, 'write_wide_count']))
        rready = vtypes.Ors(self.wdata.wready, vtypes.Not(self.wdata.wvalid),
                            count > 0)
        rdata, rvalid, rlast = ram_method(
            self.write_local_addr_buf, self.write_local_stride_buf, self.write_local_size_buf,
            rready, port=port, cond=ram_cond)

        cond = self.write_op_sel_buf == op_id
        self.seq.If(cond, rvalid, rready)(
            self.write_local_addr_buf.add(self.write_local_stride_buf)
        )

        data_fsm(
            count(0)
        )
        data_fsm.goto_next()

        # Data state 2
        cond = self.write_op_sel == op_id
        wcond = vtypes.Ands(data_fsm.here, cond, count == pack_size - 1, rvalid)
        wdata = self.m.TmpReg(self.datawidth, initval=0,
                              prefix='_'.join(['', self.name, 'write_wide_wdata']))
        _wdata = vtypes.Cat(rdata, wdata[ram_datawidth:self.datawidth])
        _ = self.write_data(_wdata, rlast, cond=wcond)
        data_fsm.If(rvalid, rready)(
            wdata(_wdata),
            count.inc(),
        )
        data_fsm.If(rvalid, rready, count == pack_size - 1)(
            count(0)
        )
        data_fsm.If(cond, count == pack_size - 1, rvalid, rlast).goto_init()

        self.seq.If(data_fsm.here, cond, count == pack_size - 1, rvalid, rlast)(
            self.write_data_idle(1)
        )

    def _set_flag(self, fsm, prefix='axim_flag'):
        flag = self.m.TmpWire(prefix=prefix)
        flag.assign(fsm.here)
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

    def pack_read_req(self, op_sel, local_addr, local_stride, local_size):
        return vtypes.Cat(op_sel, local_addr, local_stride, local_size)

    def unpack_read_req(self, v):
        op_sel = v[self.addrwidth * 3 + 1:self.addrwidth * 3 + 1 + self.op_sel_width]
        local_addr = v[self.addrwidth * 2 + 1:self.addrwidth * 2 + 1 + self.addrwidth]
        local_stride = v[self.addrwidth + 1:self.addrwidth + 1 + self.addrwidth]
        local_size = v[0:self.addrwidth + 1]
        return op_sel, local_addr, local_stride, local_size

    def pack_write_req(self, op_sel, local_addr, local_stride, local_size, update_local_addr):
        return vtypes.Cat(op_sel, local_addr, local_stride, local_size, update_local_addr)

    def unpack_write_req(self, v):
        op_sel = v[self.addrwidth * 3 + 1 + 1:self.addrwidth * 3 + 1 + 1 + self.op_sel_width]
        local_addr = v[self.addrwidth * 2 + 1 + 1:self.addrwidth * 2 + 1 + 1 + self.addrwidth]
        local_stride = v[self.addrwidth + 1 + 1:self.addrwidth + 1 + 1 + self.addrwidth]
        local_size = v[1:self.addrwidth + 1 + 1]
        update_local_addr = v[0]
        return op_sel, local_addr, local_stride, local_size, update_local_addr


class AXIMVerify(AXIM):
    __intrinsics__ = ('read_delayed', 'write_delayed') + AXIM.__intrinsics__

    def read_delayed(self, fsm, global_addr, delay):
        if self.use_global_base_addr:
            global_addr = self.global_base_addr + global_addr

        ack, counter = self.read_request_counter(global_addr, length=1, cond=fsm)
        delay_count = self.m.TmpReg(self.addrwidth, initval=0, prefix='delay_count')
        fsm(
            delay_count(delay)
        )
        fsm.If(ack).goto_next()

        fsm(
            delay_count.dec()
        )
        fsm.If(delay_count == 0).goto_next()

        ret = self.read_data(counter, cond=fsm)
        if len(ret) == 3:
            data, valid, last = ret
        else:
            data, valid = ret

        rdata = self.m.TmpReg(self.datawidth, initval=0,
                              signed=True, prefix='axim_rdata')
        fsm.If(valid)(rdata(data))
        fsm.Then().goto_next()

        return rdata

    def write_delayed(self, fsm, global_addr, value, delay):
        if self.use_global_base_addr:
            global_addr = self.global_base_addr + global_addr

        ack, counter = self.write_request_counter(global_addr, length=1, cond=fsm)
        delay_count = self.m.TmpReg(self.addrwidth, initval=0, prefix='delay_count')
        fsm(
            delay_count(delay)
        )
        fsm.If(ack).goto_next()

        fsm(
            delay_count.dec()
        )
        fsm.If(delay_count == 0).goto_next()

        ret = self.write_data(value, counter, cond=fsm)
        if isinstance(ret, (tuple)):
            ack, last = ret
        else:
            ack, last = ret, None

        fsm.If(ack).goto_next()


class AXIMLite(axi.AxiLiteMaster, _MutexFunction):
    """ AXI-Lite Master Interface """

    __intrinsics__ = ('read', 'write',
                      'set_global_base_addr',) + _MutexFunction.__intrinsics__

    burstlen = 256

    def __init__(self, m, name, clk, rst, datawidth=32, addrwidth=32,
                 waddr_cache_mode=axi.AxCACHE_NONCOHERENT, raddr_cache_mode=axi.AxCACHE_NONCOHERENT,
                 waddr_prot_mode=axi.AxPROT_NONCOHERENT, raddr_prot_mode=axi.AxPROT_NONCOHERENT,
                 noio=False,
                 use_global_base_addr=False,
                 fsm_as_module=False):

        axi.AxiLiteMaster.__init__(self, m, name, clk, rst, datawidth, addrwidth,
                                   waddr_cache_mode, raddr_cache_mode,
                                   waddr_prot_mode, raddr_prot_mode,
                                   noio)

        self.use_global_base_addr = use_global_base_addr
        self.fsm_as_module = fsm_as_module

        self.mutex = None

    def read(self, fsm, global_addr):
        ### ???
        if self.use_global_base_addr:
            global_addr = self.global_base_addr + global_addr

        ack = self.read_request(global_addr, length=1, cond=fsm)
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
        ### ???
        if self.use_global_base_addr:
            global_addr = self.global_base_addr + global_addr

        ack = self.write_request(global_addr, length=1, cond=fsm)
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


class AXIMLiteVerify(AXIMLite):
    __intrinsics__ = ('read_delayed', 'write_delayed') + AXIMLite.__intrinsics__

    def read_delayed(self, fsm, global_addr, delay):
        if self.use_global_base_addr:
            global_addr = self.global_base_addr + global_addr

        ack = self.read_request(global_addr, length=1, cond=fsm)
        delay_count = self.m.TmpReg(self.addrwidth, initval=0, prefix='delay_count')
        fsm(
            delay_count(delay)
        )
        fsm.If(ack).goto_next()

        fsm(
            delay_count.dec()
        )
        fsm.If(delay_count == 0).goto_next()

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

    def write_delayed(self, fsm, global_addr, value, delay):
        if self.use_global_base_addr:
            global_addr = self.global_base_addr + global_addr

        ack = self.write_request(global_addr, length=1, cond=fsm)
        delay_count = self.m.TmpReg(self.addrwidth, initval=0, prefix='delay_count')
        fsm(
            delay_count(delay)
        )
        fsm.If(ack).goto_next()

        fsm(
            delay_count.dec()
        )
        fsm.If(delay_count == 0).goto_next()

        ret = self.write_data(value, cond=fsm)
        if isinstance(ret, (tuple)):
            ack, last = ret
        else:
            ack, last = ret, None

        fsm.If(ack).goto_next()
