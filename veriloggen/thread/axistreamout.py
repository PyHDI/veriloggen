from __future__ import absolute_import
from __future__ import print_function

import math
import functools
from collections import OrderedDict

import veriloggen.core.vtypes as vtypes
import veriloggen.types.axi as axi
from veriloggen.fsm.fsm import FSM
from veriloggen.optimizer import try_optimize as optimize

from .ttypes import _MutexFunction
from .ram import RAM, MultibankRAM, to_multibank_ram
from .fifo import FIFO


class AXIStreamOut(axi.AxiStreamOut, _MutexFunction):
    """ AXI Stream Interface for Output """

    __intrinsics__ = ('write',
                      'read_ram', 'read_ram_async',
                      'wait_read_ram')

    def __init__(self, m, name, clk, rst, datawidth=32, addrwidth=32,
                 with_last=False,
                 id_width=0, user_width=0, dest_width=0,
                 noio=False,
                 enable_async=True,
                 num_cmd_delay=0, num_data_delay=0,
                 op_sel_width=8, fsm_as_module=False):

        axi.AxiStreamOut.__init__(self, m, name, clk, rst, datawidth,
                                  with_last,
                                  id_width, user_width, dest_width,
                                  noio)

        self.addrwidth = addrwidth

        self.enable_async = enable_async
        self.num_cmd_delay = num_cmd_delay
        self.num_data_delay = num_data_delay
        self.op_sel_width = op_sel_width
        self.fsm_as_module = fsm_as_module

        self.mutex = None

        self.write_start = self.m.Reg('_'.join(['', self.name, 'write_start']),
                                      initval=0)
        self.write_op_sel = self.m.Reg('_'.join(['', self.name, 'write_op_sel']),
                                       self.op_sel_width, initval=0)
        self.write_local_addr = self.m.Reg('_'.join(['', self.name, 'write_local_addr']),
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

        self.write_op_id_map = OrderedDict()
        self.write_op_id_count = 1
        self.write_reqs = OrderedDict()
        self.write_ops = []

        self.write_fsm = None
        self.write_counter = None

        self.write_narrow_fsms = OrderedDict()  # key: pack_size
        self.write_narrow_counters = OrderedDict()  # key: pack_size
        self.write_narrow_wdatas = OrderedDict()  # key: pack_size
        self.write_narrow_wvalids = OrderedDict()  # key: pack_size
        self.write_narrow_wlasts = OrderedDict()  # key: pack_size
        self.write_narrow_pack_counts = OrderedDict()  # key: pack_size

        self.write_wide_fsms = OrderedDict()  # key: pack_size
        self.write_wide_counters = OrderedDict()  # key: pack_size
        self.write_wide_wdatas = OrderedDict()  # key: pack_size
        self.write_wide_wvalids = OrderedDict()  # key: pack_size
        self.write_wide_wlasts = OrderedDict()  # key: pack_size
        self.write_wide_pack_counts = OrderedDict()  # key: pack_size

    def write(self, fsm, value, last=False):
        ack = self.write_data(value, last, cond=fsm)
        fsm.If(ack).goto_next()

    def read_ram(self, fsm, ram, local_addr, size,
                 local_stride=1, port=0, ram_method=None):

        if self.enable_async:
            self.wait_read_ram(fsm)

        self._read_ram(fsm, ram, local_addr, size,
                       local_stride, port, ram_method)

        self.wait_read_ram(fsm)

    def read_ram_async(self, fsm, ram, local_addr, size,
                       local_stride=1, port=0, ram_method=None):

        if not self.enable_async:
            raise ValueError(
                "Async mode is disabled. Set 'True' to AXIM.enable_async.")

        self.wait_read_ram(fsm)

        self._read_ram(fsm, ram, local_addr, size,
                       local_stride, port, ram_method)

    def wait_read_ram(self, fsm):

        fsm.If(self.write_idle).goto_next()

    def _read_ram(self, fsm, ram, local_addr, size,
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
                                local_addr, size, local_stride)

        self._synthesize_write_fsm(ram, port, ram_method)

        fsm.goto_next()

    def _set_write_request(self, ram, port, ram_method, start,
                           local_addr, size, local_stride):

        op_id = self._get_write_op_id(ram, port, ram_method)

        if op_id in self.write_reqs:
            (write_start, write_op_sel,
             write_local_addr_in,
             write_size_in, write_local_stride_in) = self.write_reqs[op_id]

            self.seq.If(start)(
                write_start(1),
                write_op_sel(op_id),
                write_local_addr_in(local_addr),
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
            write_size(size),
            write_local_stride(local_stride)
        )

        self.write_reqs[op_id] = (write_start, write_op_sel,
                                  write_local_addr,
                                  write_size, write_local_stride)

        if self.num_cmd_delay > 0:
            write_start = self.seq.Prev(write_start, self.num_cmd_delay)
            write_op_sel = self.seq.Prev(write_op_sel, self.num_cmd_delay)
            write_local_addr = self.seq.Prev(
                write_local_addr, self.num_cmd_delay)
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
            counter = self.write_counter

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

            # state 1
            fsm.set_index(1)
            cond = vtypes.Ands(fsm.here, self.write_op_sel == op_id)

            write_ready = vtypes.Ors(self.tdata.tready, vtypes.Not(self.tdata.tvalid))
            read_cond = vtypes.Ands(cond, write_ready)

            rdata, rvalid = data.read(cond=read_cond)
            rlast, _ = last.read(cond=read_cond)

            _ = self.write_data(rdata, rlast, cond=rvalid)

            return

        """ new op and fsm """
        fsm = FSM(self.m, '_'.join(['', self.name, 'write_fsm']),
                  self.clk, self.rst, as_module=self.fsm_as_module)
        self.write_fsm = fsm

        self.write_ops.append(op_id)

        # state 0
        cond = vtypes.Ands(self.write_start, self.write_op_sel == op_id)
        data, last, done = ram_method(
            port, self.write_local_addr, self.write_size,
            stride=self.write_local_stride, cond=cond, signed=False)

        if self.num_data_delay > 0:
            for _ in range(self.num_data_delay):
                data = self.df._Delay(data)
                last = self.df._Delay(last)

        counter = self.m.Reg('_'.join(['', self.name, 'write_counter']),
                             self.addrwidth + 1, initval=0)
        self.write_counter = counter

        fsm.If(self.write_start)(
            counter(self.write_size)
        )
        fsm.If(cond).goto_next()

        # state 1
        cond = vtypes.Ands(fsm.here, self.write_op_sel == op_id)

        write_ready = vtypes.Ors(self.tdata.tready, vtypes.Not(self.tdata.tvalid))
        read_cond = vtypes.Ands(cond, write_ready)

        rdata, rvalid = data.read(cond=read_cond)
        rlast, _ = last.read(cond=read_cond)

        _ = self.write_data(rdata, rlast, cond=rvalid)

        ack = vtypes.Ands(self.tdata.tvalid, self.tdata.tready)

        fsm.If(ack)(
            counter.dec()
        )

        done = counter == 0
        fsm.If(done).goto_next()

        # state 2
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
            counter = self.write_narrow_counters[pack_size]
            wdata = self.write_narrow_wdatas[pack_size]
            wvalid = self.write_narrow_wvalids[pack_size]
            wlast = self.write_narrow_wlasts[pack_size]
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

            # state 1
            fsm.set_index(1)
            cond = vtypes.Ands(fsm.here, self.write_op_sel == op_id)

            write_ready = vtypes.Ors(self.tdata.tready, vtypes.Not(self.tdata.tvalid))
            read_cond = vtyeps.Ands(cond, write_ready, pack_count == 0)

            rdata, rvalid = data.read(cond=read_cond)
            rlast, _ = last.read(cond=read_cond)

            stay_cond = self.write_op_sel == op_id

            self.seq.If(write_ready, rvalid, stay_cond)(
                wdata(rdata),
                wvalid(1),
                wlast(rlast),
                pack_count.inc()
            )

            return

        """ new op and fsm """
        fsm = FSM(self.m, '_'.join(['', self.name,
                                    'write_narrow', str(pack_size),
                                    'fsm']),
                  self.clk, self.rst, as_module=self.fsm_as_module)
        self.write_narrow_fsms[pack_size] = fsm

        self.write_ops.append(op_id)

        # state 0
        cond = vtypes.Ands(self.write_start, self.write_op_sel == op_id)
        data, last, done = ram_method(
            port, self.write_local_addr, self.write_size,
            stride=self.write_local_stride, cond=cond, signed=False)

        if self.num_data_delay > 0:
            for _ in range(self.num_data_delay):
                data = self.df._Delay(data)
                last = self.df._Delay(last)

        counter = self.m.Reg('_'.join(['', self.name,
                                       'write_narrow', str(pack_size), 'counter']),
                             self.addrwidth + 1, initval=0)
        self.write_narrow_counters[pack_size] = counter

        fsm.If(self.write_start)(
            counter(dma_size)
        )
        fsm.If(cond).goto_next()

        # state 1
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
        wlast = self.m.Reg('_'.join(['', self.name,
                                     'write_narrow', str(pack_size),
                                     'wlast']),
                           initval=0)
        self.write_narrow_wlasts[pack_size] = wlast
        pack_count = self.m.Reg('_'.join(['', self.name,
                                          'write_narrow', str(pack_size),
                                          'pack_count']),
                                int(math.ceil(math.log(pack_size, 2))), initval=0)
        self.write_narrow_pack_counts[pack_size] = pack_count

        cond = vtypes.Ands(fsm.here, self.write_op_sel == op_id)

        write_ready = vtypes.Ors(self.tdata.tready, vtypes.Not(self.tdata.tvalid))
        read_cond = vtypes.Ands(cond, write_ready, pack_count == 0)

        rdata, rvalid = data.read(cond=read_cond)
        rlast, _ = last.read(cond=read_cond)

        stay_cond = self.write_op_sel == op_id

        self.seq.If(write_ready)(
            wvalid(0),
            wlast(0)
        )
        self.seq.If(write_ready, rvalid, stay_cond)(
            wdata(rdata),
            wvalid(1),
            wlast(rlast),
            pack_count.inc()
        )
        self.seq.If(write_ready, pack_count > 0)(
            wdata(wdata >> self.datawidth),
            wvalid(1),
            pack_count.inc()
        )
        self.seq.If(write_ready, pack_count == pack_size - 1)(
            wdata(wdata >> self.datawidth),
            wvalid(1),
            pack_count(0)
        )

        _ = self.write_data(wdata, wlast, cond=wvalid)

        ack = vtypes.Ands(self.tdata.tvalid, self.tdata.tready)
        fsm.If(ack)(
            counter.dec()
        )

        done = counter == 0
        fsm.If(done).goto_next()

        # state 2
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
            counter = self.write_wide_counters[pack_size]
            wdata = self.write_wide_wdatas[pack_size]
            wvalid = self.write_wide_wvalids[pack_size]
            wlast = self.write_wide_wlasts[pack_size]
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

            # state 1
            fsm.set_index(1)
            cond = vtypes.Ands(fsm.here, self.write_op_sel == op_id)

            write_ready = vtypes.Ors(self.tdata.tready, vtypes.Not(self.tdata.tvalid))
            read_cond = cond

            rdata, rvalid = data.read(cond=read_cond)
            rlast, _ = last.read(cond=read_cond)

            stay_cond = self.write_op_sel == op_id

            ack = vtypes.Ors(wready, vtypes.Not(wvalid))
            cond = vtypes.Ands(fsm.here, ack, self.write_op_sel == op_id)
            rdata, rvalid = data.read(cond=cond)

            self.seq.If(rvalid, stay_cond)(
                wdata(vtypes.Cat(rdata, wdata[ram_datawidth:self.datawidth])),
                wvalid(0),
                wlast(0),
                pack_count.inc()
            )
            self.seq.If(rvalid, stay_cond, pack_count == pack_size - 1)(
                wdata(vtypes.Cat(rdata, wdata[ram_datawidth:self.datawidth])),
                wvalid(1),
                wlast(rlast),
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

        # state 0
        cond = vtypes.Ands(self.write_start, self.write_op_sel == op_id)
        data, last, done = ram_method(
            port, self.write_local_addr, actual_write_size,
            stride=self.write_local_stride, cond=cond, signed=False)

        if self.num_data_delay > 0:
            for _ in range(self.num_data_delay):
                data = self.df._Delay(data)
                last = self.df._Delay(last)

        counter = self.m.Reg('_'.join(['', self.name,
                                       'write_wide', str(pack_size), 'counter']),
                             self.addrwidth + 1, initval=0)
        self.write_wide_counters[pack_size] = counter

        fsm.If(self.write_start)(
            counter(dma_size)
        )
        fsm.If(cond).goto_next()

        # state 1
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
        wlast = self.m.Reg('_'.join(['', self.name,
                                     'write_wide', str(pack_size),
                                     'wlast']),
                           initval=0)
        self.write_wide_wlasts[pack_size] = wlast
        pack_count = self.m.Reg('_'.join(['', self.name,
                                          'write_wide', str(pack_size),
                                          'pack_count']),
                                int(math.ceil(math.log(pack_size, 2))), initval=0)
        self.write_wide_pack_counts[pack_size] = pack_count

        cond = vtypes.Ands(fsm.here, self.write_op_sel == op_id)

        write_ready = vtypes.Ors(self.tdata.tready, vtypes.Not(self.tdata.tvalid))
        read_cond = cond

        rdata, rvalid = data.read(cond=read_cond)
        rlast, _ = last.read(cond=read_cond)

        stay_cond = self.write_op_sel == op_id

        self.seq.If(write_ready)(
            wvalid(0),
            wlast(0)
        )
        self.seq.If(rvalid, stay_cond)(
            wdata(vtypes.Cat(rdata, wdata[ram_datawidth:self.datawidth])),
            wvalid(0),
            wlast(0),
            pack_count.inc()
        )
        self.seq.If(rvalid, stay_cond, pack_count == pack_size - 1)(
            wdata(vtypes.Cat(rdata, wdata[ram_datawidth:self.datawidth])),
            wvalid(1),
            wlast(rlast),
            pack_count(0)
        )

        _ = self.write_data(wdata, wlast, cond=wvalid)

        ack = vtypes.Ands(self.tdata.tvalid, self.tdata.tready)
        fsm.If(ack)(
            counter.dec()
        )

        done = counter == 0
        fsm.If(done).goto_next()

        # state 2
        set_idle = self._set_flag(fsm)
        self.seq.If(set_idle)(
            self.write_idle(1)
        )

        fsm.goto_init()

    def _set_flag(self, fsm, prefix='axistreamout_flag'):
        flag = self.m.TmpReg(initval=0, prefix=prefix)
        fsm(
            flag(1)
        )
        fsm.Delay(1)(
            flag(0)
        )
        fsm.goto_next()
        return flag

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


class AXIStreamOutFifo(AXIStreamOut):
    """ AXI Stream Interface from FIFO for Output """

    __intrinsics__ = ('write',
                      'read_fifo',
                      'wait_read_fifo')

    def read_ram(self, fsm, ram, local_addr, size,
                 local_stride=1, port=0, ram_method=None):

        raise NotImplementedError('Use AXIStreamOut.')

    def read_ram_async(self, fsm, ram, local_addr, size,
                       local_stride=1, port=0, ram_method=None):

        raise NotImplementedError('Use AXIStreamOut.')

    def wait_read_ram(self, fsm):

        raise NotImplementedError('Use AXIStreamOut.')

    def read_fifo(self, fsm, fifo, size):

        if not self.enable_async:
            raise ValueError(
                "Async mode is disabled. Set 'True' to AXIM.enable_async.")

        self.wait_read_fifo(fsm)

        self._read_fifo(fsm, fifo, size)

    def wait_read_fifo(self, fsm):

        fsm.If(self.write_idle).goto_next()

    def _get_write_op_id_fifo(self, fifo):

        fifo_id = fifo._id()
        op = fifo_id

        if op in self.write_op_id_map:
            op_id = self.write_op_id_map[op]
        else:
            op_id = self.write_op_id_count
            self.write_op_id_count += 1
            self.write_op_id_map[op] = op_id

        return op_id

    def _read_fifo(self, fsm, fifo, size):

        if self.num_data_delay != 0:
            raise ValueError('num_data_delay must be 0.')

        if not isinstance(fifo, FIFO):
            raise TypeError('FIFO object is required.')

        start = self._set_flag(fsm)

        for _ in range(self.num_cmd_delay + 1):
            fsm.goto_next()

        self._set_write_request_fifo(fifo, start, size)

        self._synthesize_write_fsm_fifo(fifo)

        fsm.goto_next()

    def _set_write_request_fifo(self, fifo, start, size):

        op_id = self._get_write_op_id_fifo(fifo)

        if op_id in self.write_ops:
            (write_start, write_op_sel, write_size_in) = self.write_ops[op_id]

            self.seq.If(start)(
                write_start(1),
                write_op_sel(op_id)
            )

            return

        write_start = self.m.Reg(
            '_'.join(['', self.name, fifo.name, 'write_start']),
            initval=0)
        write_op_sel = self.m.Reg(
            '_'.join(['', self.name, fifo.name, 'write_op_sel']),
            self.op_sel_width, initval=0)
        write_size = self.m.Reg(
            '_'.join(['', self.name, fifo.name, 'write_size']),
            self.addrwidth + 1, initval=0)

        self.seq(
            write_start(0)
        )
        self.seq.If(start)(
            write_start(1),
            write_op_sel(op_id),
            write_size(size),
        )

        self.write_reqs[op_id] = (write_start, write_op_sel, write_size)

        if self.num_cmd_delay > 0:
            write_start = self.seq.Prev(write_start, self.num_cmd_delay)
            write_op_sel = self.seq.Prev(write_op_sel, self.num_cmd_delay)
            write_size = self.seq.Prev(write_size, self.num_cmd_delay)

        self.seq.If(write_start)(
            self.write_idle(0)
        )

        self.seq.If(write_start)(
            self.write_start(1),
            self.write_op_sel(write_op_sel),
            self.write_size(write_size),
        )

    def _synthesize_write_fsm_fifo(self, fifo):

        fifo_datawidth = fifo.datawidth

        if not isinstance(fifo_datawidth, int):
            raise TypeError("fifo_datawidth must be int, not '%s'" %
                            str(type(fifo_datawidth)))

        if self.datawidth == fifo_datawidth:
            return self._synthesize_write_fsm_fifo_same(fifo, fifo_datawidth)

        if self.datawidth < fifo_datawidth:
            return self._synthesize_write_fsm_fifo_narrow(fifo, fifo_datawidth)

        return self._synthesize_write_fsm_fifo_wide(fifo, fifo_datawidth)

    def _synthesize_write_fsm_fifo_same(self, fifo, fifo_datawidth):

        op_id = self._get_write_op_id_fifo(fifo)

        if op_id in self.write_ops:
            """ already synthesized op """
            return

        if self.write_fsm is not None:
            """ new op """
            self.write_ops.append(op_id)

            fsm = self.write_fsm
            counter = self.write_counter

            # state 0
            fsm.set_index(0)
            cond = vtypes.Ands(self.write_start, self.write_op_sel == op_id)

            fifo_counter = self.m.TmpReg(prefix='_'.join(['', self.name, 'write_fifo_counter']),
                                         width=self.addrwidth + 1, initval=0)
            fsm.If(self.write_start)(
                fifo_counter(self.write_size)
            )

            fsm.If(cond).goto_next()

            # state 1
            fsm.set_index(1)
            cond = vtypes.Ands(fsm.here, self.write_op_sel == op_id)
            write_ready = vtypes.Ors(self.tdata.tready, vtypes.Not(self.tdata.tvalid))
            fifo_ready = vtypes.Not(fifo.empty)
            deq_cond = vtypes.Ands(cond, write_ready, fifo_ready, fifo_counter > 0)

            rdata, rvalid, _ = fifo.deq_rtl(cond=deq_cond)
            rlast = self.m.TmpReg(prefix='rlast', initval=0)
            self.seq.If(deq_cond)(
                rlast(fifo_counter <= 1)
            )
            fsm.If(deq_cond)(
                fifo_counter.dec()
            )

            repeat_rvalid = self.m.TmpReg(prefix='repeat_rvalid', initval=0)
            self.seq(repeat_rvalid(0))
            self.seq.If(rvalid, vtypes.Not(write_ready))(repeat_rvalid(1))
            self.seq.If(repeat_rvalid, vtypes.Not(write_ready))(repeat_rvalid(1))
            cur_rvalid = vtypes.Ors(rvalid, repeat_rvalid)

            _ = self.write_data(rdata, rlast, cond=cur_rvalid)

            return

        """ new op and fsm """
        fsm = FSM(self.m, '_'.join(['', self.name, 'write_fsm']),
                  self.clk, self.rst, as_module=self.fsm_as_module)
        self.write_fsm = fsm

        self.write_ops.append(op_id)

        # state 0
        cond = vtypes.Ands(self.write_start, self.write_op_sel == op_id)

        counter = self.m.Reg('_'.join(['', self.name, 'write_counter']),
                             self.addrwidth + 1, initval=0)
        self.write_counter = counter

        fsm.If(self.write_start)(
            counter(self.write_size)
        )

        fifo_counter = self.m.TmpReg(prefix='_'.join(['', self.name, 'write_fifo_counter']),
                                     width=self.addrwidth + 1, initval=0)
        fsm.If(self.write_start)(
            fifo_counter(self.write_size)
        )

        fsm.If(cond).goto_next()

        # state 1
        cond = vtypes.Ands(fsm.here, self.write_op_sel == op_id)
        write_ready = vtypes.Ors(self.tdata.tready, vtypes.Not(self.tdata.tvalid))
        fifo_ready = vtypes.Not(fifo.empty)
        deq_cond = vtypes.Ands(cond, write_ready, fifo_ready, fifo_counter > 0)

        rdata, rvalid, _ = fifo.deq_rtl(cond=deq_cond)
        rlast = self.m.TmpReg(prefix='rlast', initval=0)
        self.seq.If(deq_cond)(
            rlast(fifo_counter <= 1)
        )
        fsm.If(deq_cond)(
            fifo_counter.dec()
        )

        repeat_rvalid = self.m.TmpReg(prefix='repeat_rvalid', initval=0)
        self.seq(repeat_rvalid(0))
        self.seq.If(rvalid, vtypes.Not(write_ready))(repeat_rvalid(1))
        self.seq.If(repeat_rvalid, vtypes.Not(write_ready))(repeat_rvalid(1))
        cur_rvalid = vtypes.Ors(rvalid, repeat_rvalid)

        _ = self.write_data(rdata, rlast, cond=cur_rvalid)

        ack = vtypes.Ands(self.tdata.tvalid, self.tdata.tready)

        fsm.If(ack)(
            counter.dec()
        )

        done = counter == 0
        fsm.If(done).goto_next()

        # state 2
        set_idle = self._set_flag(fsm)
        self.seq.If(set_idle)(
            self.write_idle(1)
        )

        fsm.goto_init()

    def _synthesize_write_fsm_fifo_narrow(self, fifo, fifo_datawidth):
        """ axi.datawidth < fifo.datawidth """

        if fifo_datawidth % self.datawidth != 0:
            raise ValueError(
                'fifo_datawidth must be multiple number of axi.datawidth')

        pack_size = fifo_datawidth // self.datawidth
        dma_size = (self.write_size << int(math.log(pack_size, 2))
                    if math.log(pack_size, 2) % 1.0 == 0.0 else
                    self.write_size * pack_size)

        op_id = self._get_write_op_id_fifo(fifo)

        if op_id in self.write_ops:
            """ already synthesized op """
            return

        if pack_size in self.write_narrow_fsms:
            """ new op """
            self.write_ops.append(op_id)

            fsm = self.write_narrow_fsms[pack_size]
            counter = self.write_narrow_counters[pack_size]
            wdata = self.write_narrow_wdatas[pack_size]
            wvalid = self.write_narrow_wvalids[pack_size]
            wlast = self.write_narrow_wlasts[pack_size]
            pack_count = self.write_narrow_pack_counts[pack_size]

            # state 0
            fsm.set_index(0)
            cond = vtypes.Ands(self.write_start, self.write_op_sel == op_id)

            fifo_counter = self.m.TmpReg(prefix='_'.join(
                ['', self.name, 'write_narrow', str(pack_size), 'counter']),
                                         width=self.addrwidth + 1, initval=0)
            fsm.If(self.write_start)(
                fifo_counter(self.write_size)
            )

            fsm.If(cond).goto_next()

            # state 1
            fsm.set_index(1)
            cond = vtypes.Ands(fsm.here, self.write_op_sel == op_id)

            write_ready = vtypes.Ors(self.tdata.tready, vtypes.Not(self.tdata.tvalid))
            fifo_ready = vtypes.Not(fifo.empty)
            deq_cond = vtypes.Ands(cond, write_ready, fifo_ready,
                                   vtypes.Ors(pack_count == pack_size - 1,
                                              vtypes.Ands(pack_count == 0,
                                                          fifo_counter == self.write_size)),
                                   fifo_counter > 0)

            rdata, rvalid, _ = fifo.deq_rtl(cond=deq_cond)
            rlast = self.m.TmpReg(prefix='rlast', initval=0)
            self.seq.If(deq_cond)(
                rlast(fifo_counter <= 1)
            )
            fsm.If(deq_cond)(
                fifo_counter.dec()
            )

            repeat_rvalid = self.m.TmpReg(prefix='repeat_rvalid', initval=0)
            self.seq(repeat_rvalid(0))
            self.seq.If(rvalid, vtypes.Not(write_ready))(repeat_rvalid(1))
            self.seq.If(repeat_rvalid, vtypes.Not(write_ready))(repeat_rvalid(1))
            cur_rvalid = vtypes.Ors(rvalid, repeat_rvalid)

            stay_cond = self.write_op_sel == op_id

            self.seq.If(write_ready, cur_rvalid, stay_cond)(
                wdata(rdata),
                wvalid(1),
                wlast(0),
                pack_count.inc()
            )
            self.seq.If(write_ready, pack_count == pack_size - 1)(
                wdata(wdata >> self.datawidth),
                wvalid(1),
                wlast(rlast),
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

        # state 0
        cond = vtypes.Ands(self.write_start, self.write_op_sel == op_id)

        counter = self.m.Reg('_'.join(['', self.name,
                                       'write_narrow', str(pack_size), 'counter']),
                             self.addrwidth + 1, initval=0)
        self.write_narrow_counters[pack_size] = counter

        fsm.If(self.write_start)(
            counter(dma_size)
        )

        fifo_counter = self.m.TmpReg(prefix='_'.join(['', self.name,
                                                      'write_narrow', str(pack_size), 'counter']),
                                     width=self.addrwidth + 1, initval=0)
        fsm.If(self.write_start)(
            fifo_counter(self.write_size)
        )

        fsm.If(cond).goto_next()

        # state 1
        wdata = self.m.Reg('_'.join(['', self.name,
                                     'write_narrow', str(pack_size),
                                     'wdata']),
                           fifo_datawidth, initval=0)
        self.write_narrow_wdatas[pack_size] = wdata
        wvalid = self.m.Reg('_'.join(['', self.name,
                                      'write_narrow', str(pack_size),
                                      'wvalid']),
                            initval=0)
        self.write_narrow_wvalids[pack_size] = wvalid
        wlast = self.m.Reg('_'.join(['', self.name,
                                     'write_narrow', str(pack_size),
                                     'wlast']),
                           initval=0)
        self.write_narrow_wlasts[pack_size] = wlast
        pack_count = self.m.Reg('_'.join(['', self.name,
                                          'write_narrow', str(pack_size),
                                          'pack_count']),
                                int(math.ceil(math.log(pack_size, 2))), initval=0)
        self.write_narrow_pack_counts[pack_size] = pack_count

        cond = vtypes.Ands(fsm.here, self.write_op_sel == op_id)

        write_ready = vtypes.Ors(self.tdata.tready, vtypes.Not(self.tdata.tvalid))
        fifo_ready = vtypes.Not(fifo.empty)
        deq_cond = vtypes.Ands(cond, write_ready, fifo_ready,
                               vtypes.Ors(pack_count == pack_size - 1,
                                          vtypes.Ands(pack_count == 0,
                                                      fifo_counter == self.write_size)),
                               fifo_counter > 0)

        rdata, rvalid, _ = fifo.deq_rtl(cond=deq_cond)
        rlast = self.m.TmpReg(prefix='rlast', initval=0)
        self.seq.If(deq_cond)(
            rlast(fifo_counter <= 1)
        )
        fsm.If(deq_cond)(
            fifo_counter.dec()
        )

        repeat_rvalid = self.m.TmpReg(prefix='repeat_rvalid', initval=0)
        self.seq(repeat_rvalid(0))
        self.seq.If(rvalid, vtypes.Not(write_ready))(repeat_rvalid(1))
        self.seq.If(repeat_rvalid, vtypes.Not(write_ready))(repeat_rvalid(1))
        cur_rvalid = vtypes.Ors(rvalid, repeat_rvalid)

        self.m.TmpWireLike(rdata, prefix='debug_rdata').assign(rdata)
        self.m.TmpWireLike(rvalid, prefix='debug_rvalid').assign(rvalid)

        stay_cond = self.write_op_sel == op_id

        self.seq.If(write_ready)(
            wvalid(0),
            wlast(0)
        )
        self.seq.If(write_ready, cur_rvalid, stay_cond)(
            wdata(rdata),
            wvalid(1),
            wlast(0),
            pack_count.inc()
        )
        self.seq.If(write_ready, pack_count > 0)(
            wdata(wdata >> self.datawidth),
            wvalid(1),
            wlast(0),
            pack_count.inc()
        )
        self.seq.If(write_ready, pack_count == pack_size - 1)(
            wdata(wdata >> self.datawidth),
            wvalid(1),
            wlast(rlast),
            pack_count(0)
        )

        _ = self.write_data(wdata, wlast, cond=wvalid)

        ack = vtypes.Ands(self.tdata.tvalid, self.tdata.tready)
        fsm.If(ack)(
            counter.dec()
        )

        done = counter == 0
        fsm.If(done).goto_next()

        # state 2
        set_idle = self._set_flag(fsm)
        self.seq.If(set_idle)(
            self.write_idle(1)
        )

        fsm.goto_init()

    def _synthesize_write_fsm_fifo_wide(self, fifo, fifo_datawidth):
        """ axi.datawidth > fifo.datawidth """

        if self.datawidth % fifo_datawidth != 0:
            raise ValueError(
                'axi.datawidth must be multiple number of fifo_datawidth')

        pack_size = self.datawidth // fifo_datawidth
        shamt = int(math.log(pack_size, 2))
        res = vtypes.Mux(
            vtypes.And(self.write_size, 2 ** shamt - 1) > 0, 1, 0)
        dma_size = (self.write_size >> shamt) + res

        actual_write_size = dma_size << shamt

        op_id = self._get_write_op_id_fifo(fifo)

        if op_id in self.write_ops:
            """ already synthesized op """
            return

        if pack_size in self.write_wide_fsms:
            """ new op """
            self.write_ops.append(op_id)

            fsm = self.write_narrow_fsms[pack_size]
            counter = self.write_narrow_counters[pack_size]
            wdata = self.write_narrow_wdatas[pack_size]
            wvalid = self.write_narrow_wvalids[pack_size]
            wlast = self.write_narrow_wlasts[pack_size]
            pack_count = self.write_narrow_pack_counts[pack_size]

            # state 0
            fsm.set_index(0)
            cond = vtypes.Ands(self.write_start, self.write_op_sel == op_id)

            fsm.If(cond).goto_next()

            # state 1
            fsm.set_index(1)
            cond = vtypes.Ands(fsm.here, self.write_op_sel == op_id)

            write_ready = vtypes.Ors(self.tdata.tready, vtypes.Not(self.tdata.tvalid))
            fifo_ready = vtypes.Not(fifo.empty)
            deq_cond = vtypes.Ands(cond, fifo_ready, counter > 0)

            rdata, rvalid, _ = fifo.deq_rtl(cond=deq_cond)
            rlast = counter <= 1

            repeat_rvalid = self.m.TmpReg(prefix='repeat_rvalid', initval=0)
            self.seq(repeat_rvalid(0))
            self.seq.If(rvalid, vtypes.Not(write_ready))(repeat_rvalid(1))
            self.seq.If(repeat_rvalid, vtypes.Not(write_ready))(repeat_rvalid(1))
            cur_rvalid = vtypes.Ors(rvalid, repeat_rvalid)

            stay_cond = self.write_op_sel == op_id

            self.seq.If(write_ready)(
                wvalid(0),
                wlast(0)
            )
            self.seq.If(cur_rvalid, stay_cond)(
                wdata(vtypes.Cat(rdata, wdata[fifo_datawidth:self.datawidth])),
                wvalid(0),
                wlast(0),
                pack_count.inc()
            )
            self.seq.If(cur_rvalid, stay_cond, pack_count == pack_size - 1)(
                wdata(vtypes.Cat(rdata, wdata[fifo_datawidth:self.datawidth])),
                wvalid(1),
                wlast(rlast),
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

        # state 0
        cond = vtypes.Ands(self.write_start, self.write_op_sel == op_id)

        counter = self.m.Reg('_'.join(['', self.name,
                                       'write_wide', str(pack_size), 'counter']),
                             self.addrwidth + 1, initval=0)
        self.write_wide_counters[pack_size] = counter

        fsm.If(self.write_start)(
            counter(dma_size)
        )
        fsm.If(cond).goto_next()

        # state 1
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
        wlast = self.m.Reg('_'.join(['', self.name,
                                     'write_wide', str(pack_size),
                                     'wlast']),
                           initval=0)
        self.write_wide_wlasts[pack_size] = wlast
        pack_count = self.m.Reg('_'.join(['', self.name,
                                          'write_wide', str(pack_size),
                                          'pack_count']),
                                int(math.ceil(math.log(pack_size, 2))), initval=0)
        self.write_wide_pack_counts[pack_size] = pack_count

        cond = vtypes.Ands(fsm.here, self.write_op_sel == op_id)

        write_ready = vtypes.Ors(self.tdata.tready, vtypes.Not(self.tdata.tvalid))
        fifo_ready = vtypes.Not(fifo.empty)
        deq_cond = vtypes.Ands(cond, fifo_ready, counter > 0)

        rdata, rvalid, _ = fifo.deq_rtl(cond=deq_cond)
        rlast = counter <= 1

        repeat_rvalid = self.m.TmpReg(prefix='repeat_rvalid', initval=0)
        self.seq(repeat_rvalid(0))
        self.seq.If(rvalid, vtypes.Not(write_ready))(repeat_rvalid(1))
        self.seq.If(repeat_rvalid, vtypes.Not(write_ready))(repeat_rvalid(1))
        cur_rvalid = vtypes.Ors(rvalid, repeat_rvalid)

        stay_cond = self.write_op_sel == op_id

        self.seq.If(write_ready)(
            wvalid(0),
            wlast(0)
        )
        self.seq.If(cur_rvalid, stay_cond)(
            wdata(vtypes.Cat(rdata, wdata[fifo_datawidth:self.datawidth])),
            wvalid(0),
            wlast(0),
            pack_count.inc()
        )
        self.seq.If(cur_rvalid, stay_cond, pack_count == pack_size - 1)(
            wdata(vtypes.Cat(rdata, wdata[fifo_datawidth:self.datawidth])),
            wvalid(1),
            wlast(rlast),
            pack_count(0)
        )

        _ = self.write_data(wdata, wlast, cond=wvalid)

        ack = vtypes.Ands(self.tdata.tvalid, self.tdata.tready)
        fsm.If(ack)(
            counter.dec()
        )

        done = counter == 0
        fsm.If(done).goto_next()

        # state 2
        set_idle = self._set_flag(fsm)
        self.seq.If(set_idle)(
            self.write_idle(1)
        )

        fsm.goto_init()
