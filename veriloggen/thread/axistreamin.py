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


class AXIStreamIn(axi.AxiStreamIn, _MutexFunction):
    """ AXI Stream Interface for Input """

    __intrinsics__ = ('read',
                      'write_ram', 'write_ram_async',
                      'wait_write_ram')

    def __init__(self, m, name, clk, rst, datawidth=32, addrwidth=32,
                 with_last=False,
                 id_width=0, user_width=0, dest_width=0,
                 noio=False,
                 enable_async=True,
                 num_cmd_delay=0, num_data_delay=0,
                 op_sel_width=8, fsm_as_module=False):

        axi.AxiStreamIn.__init__(self, m, name, clk, rst, datawidth,
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

        self.read_start = self.m.Reg('_'.join(['', self.name, 'read_start']),
                                     initval=0)
        self.read_op_sel = self.m.Reg('_'.join(['', self.name, 'read_op_sel']),
                                      self.op_sel_width, initval=0)
        self.read_local_addr = self.m.Reg('_'.join(['', self.name, 'read_local_addr']),
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
        self.read_rest_size = None

        self.read_narrow_fsms = OrderedDict()  # key: pack_size
        self.read_narrow_pack_counts = OrderedDict()  # key: pack_size
        self.read_narrow_data_wires = OrderedDict()  # key: pack_size
        self.read_narrow_valid_wires = OrderedDict()  # key: pack_size
        self.read_narrow_rest_size_wires = OrderedDict()  # key: pack_size

        self.read_wide_fsms = OrderedDict()  # key: pack_size
        self.read_wide_pack_counts = OrderedDict()  # key: pack_size
        self.read_wide_data_wires = OrderedDict()  # key: pack_size
        self.read_wide_valid_wires = OrderedDict()  # key: pack_size
        self.read_wide_rest_size_wires = OrderedDict()  # key: pack_size

    def read(self, fsm):
        data, last, _id, user, dest, valid = self.read_data(cond=fsm)

        rdata = self.m.TmpReg(self.datawidth, initval=0,
                              signed=True, prefix='axistreamin_rdata')

        if last is not None:
            rlast = self.m.TmpReg(1, initval=0,
                                  signed=False, prefix='axistreamin_rlast')
        else:
            rlast = True

        fsm.If(valid)(
            rdata(data),
            rlast(last) if last is not None else ()
        )
        fsm.Then().goto_next()

        return rdata, rlast

    def write_ram(self, fsm, ram, local_addr, size,
                  local_stride=1, port=0, ram_method=None):

        if self.enable_async:
            self.wait_write_ram(fsm)

        self._write_ram(fsm, ram, local_addr, size,
                        local_stride, port, ram_method)

        self.wait_write_ram(fsm)

    def write_ram_async(self, fsm, ram, local_addr, size,
                        local_stride=1, port=0, ram_method=None):

        if not self.enable_async:
            raise ValueError(
                "Async mode is disabled. Set 'True' to AXIM.enable_async.")

        self.wait_write_ram(fsm)

        self._write_ram(fsm, ram, local_addr, size,
                        local_stride, port, ram_method)

    def wait_write_ram(self, fsm):

        fsm.If(self.read_idle).goto_next()

    def _write_ram(self, fsm, ram, local_addr, size,
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
                               local_addr, size, local_stride)

        self._synthesize_read_fsm(ram, port, ram_method)

        fsm.goto_next()

    def _set_read_request(self, ram, port, ram_method, start,
                          local_addr, size, local_stride):

        op_id = self._get_read_op_id(ram, port, ram_method)

        if op_id in self.read_reqs:
            (read_start, read_op_sel,
             read_local_addr_in,
             read_size_in, read_local_stride_in) = self.read_reqs[op_id]

            self.seq.If(start)(
                read_start(1),
                read_op_sel(op_id),
                read_local_addr_in(local_addr),
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
            read_size(size),
            read_local_stride(local_stride)
        )

        self.read_reqs[op_id] = (read_start, read_op_sel,
                                 read_local_addr,
                                 read_size, read_local_stride)

        if self.num_cmd_delay > 0:
            read_start = self.seq.Prev(read_start, self.num_cmd_delay)
            read_op_sel = self.seq.Prev(read_op_sel, self.num_cmd_delay)
            read_local_addr = self.seq.Prev(
                read_local_addr, self.num_cmd_delay)
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
            rest_size = self.read_rest_size

            # state 0
            fsm.set_index(0)
            wdata, wvalid, w = self._get_op_write_dataflow(ram_datawidth)
            cond = vtypes.Ands(self.read_start, self.read_op_sel == op_id)
            ram_method(port, self.read_local_addr, w, self.read_size,
                       stride=self.read_local_stride, cond=cond)

            fsm.If(cond).goto_next()

            # state 1
            fsm.set_index(1)
            valid_cond = vtypes.Ands(valid, self.read_op_sel == op_id)

            fsm.Delay(1)(
                wvalid(0)
            )
            fsm.If(valid_cond)(
                wdata(data),
                wvalid(1)
            )
            fsm.If(valid_cond)(
                rest_size.dec()
            )

            return

        """ new op and fsm """
        fsm = FSM(self.m, '_'.join(['', self.name, 'read_fsm']),
                  self.clk, self.rst, as_module=self.fsm_as_module)
        self.read_fsm = fsm

        self.read_ops.append(op_id)

        rest_size = self.m.Reg('_'.join(['', self.name, 'read_rest_size']),
                               self.addrwidth + 1, initval=0)
        self.read_rest_size = rest_size

        # state 0
        wdata, wvalid, w = self._get_op_write_dataflow(ram_datawidth)
        cond = vtypes.Ands(self.read_start, self.read_op_sel == op_id)
        ram_method(port, self.read_local_addr, w, self.read_size,
                   stride=self.read_local_stride, cond=cond)

        fsm.If(self.read_start)(
            rest_size(self.read_size)
        )
        fsm.If(cond).goto_next()

        # state 1
        data, last, _id, user, dest, valid = self.read_data(cond=fsm)
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
        fsm.If(valid_cond)(
            rest_size.dec()
        )

        fsm.If(valid, rest_size <= 1).goto_next()

        for _ in range(self.num_data_delay):
            fsm.goto_next()

        # state 2
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
            rest_size = self.read_narrow_rest_size_wires[pack_size]

            # state 0
            fsm.set_index(0)
            wdata, wvalid, w = self._get_op_write_dataflow(ram_datawidth)
            cond = vtypes.Ands(self.read_start, self.read_op_sel == op_id)
            ram_method(port, self.read_local_addr, w, self.read_size,
                       stride=self.read_local_stride, cond=cond)

            fsm.If(cond).goto_next()

            # state 1
            fsm.set_index(1)
            valid_cond = vtypes.Ands(valid, self.read_op_sel == op_id)

            fsm.Delay(1)(
                wvalid(0)
            )
            fsm.If(rest_size == 0, pack_count > 0)(
                wdata(vtypes.Cat(data, wdata[self.datawidth:ram_datawidth])),
                wvalid(0),
                pack_count.inc()
            )
            fsm.If(valid_cond)(
                wdata(vtypes.Cat(data, wdata[self.datawidth:ram_datawidth])),
                wvalid(0),
                pack_count.inc()
            )
            fsm.If(rest_size == 0, pack_count == pack_size - 1)(
                wdata(vtypes.Cat(data, wdata[self.datawidth:ram_datawidth])),
                wvalid(1),
                pack_count(0)
            )
            fsm.If(valid_cond, pack_count == pack_size - 1)(
                wdata(vtypes.Cat(data, wdata[self.datawidth:ram_datawidth])),
                wvalid(1),
                pack_count(0)
            )
            fsm.If(valid_cond)(
                rest_size.dec()
            )

            return

        """ new op and fsm """
        fsm = FSM(self.m, '_'.join(['', self.name,
                                    'read_narrow', str(pack_size),
                                    'fsm']),
                  self.clk, self.rst, as_module=self.fsm_as_module)
        self.read_narrow_fsms[pack_size] = fsm

        self.read_ops.append(op_id)

        rest_size = self.m.Reg('_'.join(['', self.name,
                                         'read_narrow', str(pack_size),
                                         'rest_size']),
                               self.addrwidth + 1, initval=0)
        self.read_narrow_rest_size_wires[pack_size] = rest_size

        # state 0
        wdata, wvalid, w = self._get_op_write_dataflow(ram_datawidth)
        cond = vtypes.Ands(self.read_start, self.read_op_sel == op_id)
        ram_method(port, self.read_local_addr, w, self.read_size,
                   stride=self.read_local_stride, cond=cond)

        fsm.If(self.read_start)(
            rest_size(dma_size)
        )
        fsm.If(cond).goto_next()

        # state 1
        pack_count = self.m.Reg('_'.join(['', self.name,
                                          'read_narrow', str(pack_size),
                                          'pack_count']),
                                int(math.ceil(math.log(pack_size, 2))), initval=0)
        self.read_narrow_pack_counts[pack_size] = pack_count

        data, last, _id, user, dest, valid = self.read_data(cond=fsm)
        self.read_narrow_data_wires[pack_size] = data
        self.read_narrow_valid_wires[pack_size] = valid

        valid_cond = vtypes.Ands(valid, self.read_op_sel == op_id)

        fsm.Delay(1)(
            wvalid(0)
        )
        fsm.If(rest_size == 0, pack_count > 0)(
            wdata(vtypes.Cat(data, wdata[self.datawidth:ram_datawidth])),
            wvalid(0),
            pack_count.inc()
        )
        fsm.If(valid_cond)(
            wdata(vtypes.Cat(data, wdata[self.datawidth:ram_datawidth])),
            wvalid(0),
            pack_count.inc()
        )
        fsm.If(rest_size == 0, pack_count == pack_size - 1)(
            wdata(vtypes.Cat(data, wdata[self.datawidth:ram_datawidth])),
            wvalid(1),
            pack_count(0)
        )
        fsm.If(valid_cond, pack_count == pack_size - 1)(
            wdata(vtypes.Cat(data, wdata[self.datawidth:ram_datawidth])),
            wvalid(1),
            pack_count(0)
        )
        fsm.If(valid_cond)(
            rest_size.dec()
        )

        fsm.If(wvalid, rest_size == 0).goto_next()

        for _ in range(self.num_data_delay):
            fsm.goto_next()

        # state 2
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
            rest_size = self.read_wide_rest_size_wires[pack_size]

            # state 0
            fsm.set_index(0)
            wdata, wvalid, w = self._get_op_write_dataflow(ram_datawidth)
            cond = vtypes.Ands(self.read_start, self.read_op_sel == op_id)
            ram_method(port, self.read_local_addr, w, actual_read_size,
                       stride=self.read_local_stride, cond=cond)

            fsm.If(cond).goto_next()

            # state 1
            fsm.set_index(1)
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
            fsm.If(valid_cond)(
                rest_size.dec()
            )

            return

        """ new op and fsm """
        fsm = FSM(self.m, '_'.join(['', self.name,
                                    'read_wide', str(pack_size),
                                    'fsm']),
                  self.clk, self.rst, as_module=self.fsm_as_module)
        self.read_wide_fsms[pack_size] = fsm

        self.read_ops.append(op_id)

        rest_size = self.m.Reg('_'.join(['', self.name,
                                         'read_wide', str(pack_size),
                                         'rest_size']),
                               self.addrwidth + 1, initval=0)
        self.read_wide_rest_size_wires[pack_size] = rest_size

        # state 0
        wdata, wvalid, w = self._get_op_write_dataflow(ram_datawidth)
        cond = vtypes.Ands(self.read_start, self.read_op_sel == op_id)
        ram_method(port, self.read_local_addr, w, actual_read_size,
                   stride=self.read_local_stride, cond=cond)

        fsm.If(self.read_start)(
            rest_size(dma_size)
        )
        fsm.If(cond).goto_next()

        # state 1
        pack_count = self.m.Reg('_'.join(['', self.name,
                                          'read_wide', str(pack_size),
                                          'pack_count']),
                                int(math.ceil(math.log(pack_size, 2))), initval=0)
        self.read_wide_pack_counts[pack_size] = pack_count

        cond = vtypes.Ands(fsm.here, pack_count == 0)
        data, last, _id, user, dest, valid = self.read_data(cond=cond)
        self.read_wide_data_wires[pack_size] = data
        self.read_wide_valid_wires[pack_size] = valid

        valid_cond = vtypes.Ands(valid, self.read_op_sel == op_id)
        stay_cond = self.read_op_sel == op_id

        wlast = self.m.Reg('_'.join(['', self.name,
                                     'read_wide', str(pack_size),
                                     'wlast']),
                           initval=0)

        fsm.Delay(1)(
            wvalid(0)
        )
        fsm.If(pack_count == 0, valid_cond)(
            wdata(data),
            wvalid(1),
            wlast(last),
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

        fsm.If(pack_count == 0, valid_cond)(
            rest_size.dec()
        )

        fsm.If(pack_count == pack_size - 1, rest_size == 0).goto_next()

        for _ in range(self.num_data_delay):
            fsm.goto_next()

        # state 2
        set_idle = self._set_flag(fsm)
        self.seq.If(set_idle)(
            self.read_idle(1)
        )

        fsm.goto_init()

    def _set_flag(self, fsm, prefix='axistreamin_flag'):
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


class AXIStreamInFifo(AXIStreamIn):
    """ AXI Stream Interface to FIFO for Input """

    __intrinsics__ = ('read',
                      'write_fifo',
                      'wait_write_fifo')

    def write_ram(self, fsm, ram, local_addr, size,
                  local_stride=1, port=0, ram_method=None):

        raise NotImplementedError('Use AXIStreamIn.')

    def write_ram_async(self, fsm, ram, local_addr, size,
                        local_stride=1, port=0, ram_method=None):

        raise NotImplementedError('Use AXIStreamIn.')

    def wait_write_ram(self, fsm):

        raise NotImplementedError('Use AXIStreamIn.')

    def write_fifo(self, fsm, fifo, size):

        if not self.enable_async:
            raise ValueError(
                "Async mode is disabled. Set 'True' to AXIM.enable_async.")

        self.wait_write_fifo(fsm)

        self._write_fifo(fsm, fifo, size)

    def wait_write_fifo(self, fsm):

        fsm.If(self.read_idle).goto_next()

    def _get_read_op_id_fifo(self, fifo):

        fifo_id = fifo._id()
        op = fifo_id

        if op in self.read_op_id_map:
            op_id = self.read_op_id_map[op]
        else:
            op_id = self.read_op_id_count
            self.read_op_id_count += 1
            self.read_op_id_map[op] = op_id

        return op_id

    def _write_fifo(self, fsm, fifo, size):

        if self.num_data_delay != 0:
            raise ValueError('num_data_delay must be 0.')

        if not isinstance(fifo, FIFO):
            raise TypeError('FIFO object is required.')

        start = self._set_flag(fsm)

        for _ in range(self.num_cmd_delay + 1):
            fsm.goto_next()

        self._set_read_request_fifo(fifo, start, size)

        self._synthesize_read_fsm_fifo(fifo)

    def _set_read_request_fifo(self, fifo, start, size):

        op_id = self._get_read_op_id_fifo(fifo)

        if op_id in self.read_ops:
            (read_start, read_op_sel, read_size_in) = self.read_ops[op_id]

            self.seq.If(start)(
                read_start(1),
                read_op_sel(op_id)
            )

            return

        read_start = self.m.Reg(
            '_'.join(['', self.name, fifo.name, 'read_start']),
            initval=0)
        read_op_sel = self.m.Reg(
            '_'.join(['', self.name, fifo.name, 'read_op_sel']),
            self.op_sel_width, initval=0)
        read_size = self.m.Reg(
            '_'.join(['', self.name, fifo.name, 'read_size']),
            self.addrwidth + 1, initval=0)

        self.seq(
            read_start(0)
        )
        self.seq.If(start)(
            read_start(1),
            read_op_sel(op_id),
            read_size(size),
        )

        self.read_reqs[op_id] = (read_start, read_op_sel, read_size)

        if self.num_cmd_delay > 0:
            read_start = self.seq.Prev(read_start, self.num_cmd_delay)
            read_op_sel = self.seq.Prev(read_op_sel, self.num_cmd_delay)
            read_size = self.seq.Prev(read_size, self.num_cmd_delay)

        self.seq.If(read_start)(
            self.read_idle(0)
        )

        self.seq.If(read_start)(
            self.read_start(1),
            self.read_op_sel(read_op_sel),
            self.read_size(read_size),
        )

    def _synthesize_read_fsm_fifo(self, fifo):

        fifo_datawidth = fifo.datawidth

        if not isinstance(fifo_datawidth, int):
            raise TypeError("fifo_datawidth must be int, not '%s'" %
                            str(type(fifo_datawidth)))

        if self.datawidth == fifo_datawidth:
            return self._synthesize_read_fsm_fifo_same(fifo, fifo_datawidth)

        if self.datawidth < fifo_datawidth:
            return self._synthesize_read_fsm_fifo_narrow(fifo, fifo_datawidth)

        return self._synthesize_read_fsm_fifo_wide(fifo, fifo_datawidth)

    def _synthesize_read_fsm_fifo_same(self, fifo, fifo_datawidth):

        op_id = self._get_read_op_id_fifo(fifo)

        if op_id in self.read_ops:
            """ already synthesized op """
            return

        if self.read_fsm is not None:
            """ new op """
            self.read_ops.append(op_id)

            fsm = self.read_fsm
            data = self.read_data_wire
            valid = self.read_valid_wire
            rest_size = self.read_rest_size

            # state 0
            fsm.set_index(0)
            cond = vtypes.Ands(self.read_start, self.read_op_sel == op_id)

            fsm.If(cond).goto_next()

            # state 1
            fsm.set_index(1)
            valid_cond = vtypes.Ands(valid, self.read_op_sel == op_id)

            ack, _ = fifo.enq_rtl(data, cond=valid_cond)

            fsm.If(valid_cond)(
                rest_size.dec()
            )

            return

        """ new op and fsm """
        fsm = FSM(self.m, '_'.join(['', self.name, 'read_fsm']),
                  self.clk, self.rst, as_module=self.fsm_as_module)
        self.read_fsm = fsm

        self.read_ops.append(op_id)

        rest_size = self.m.Reg('_'.join(['', self.name, 'read_rest_size']),
                               self.addrwidth + 1, initval=0)
        self.read_rest_size = rest_size

        # state 0
        cond = vtypes.Ands(self.read_start, self.read_op_sel == op_id)

        fsm.If(self.read_start)(
            rest_size(self.read_size)
        )
        fsm.If(cond).goto_next()

        # state 1
        ready = vtypes.Not(fifo.almost_full)
        read_cond = vtypes.Ands(fsm.here, ready)

        data, last, _id, user, dest, valid = self.read_data(cond=read_cond)
        self.read_data_wire = data
        self.read_valid_wire = valid

        valid_cond = vtypes.Ands(valid, self.read_op_sel == op_id)

        ack, _ = fifo.enq_rtl(data, cond=valid_cond)

        fsm.If(valid_cond)(
            rest_size.dec()
        )

        fsm.If(valid, rest_size <= 1).goto_next()

        # state 2
        set_idle = self._set_flag(fsm)
        self.seq.If(set_idle)(
            self.read_idle(1)
        )

        fsm.goto_init()

    def _synthesize_read_fsm_fifo_narrow(self, fifo, fifo_datawidth):
        """ axi.datawidth < fifo.datawidth """

        if fifo_datawidth % self.datawidth != 0:
            raise ValueError(
                'fifo_datawidth must be multiple number of axi.datawidth')

        pack_size = fifo_datawidth // self.datawidth
        dma_size = (self.read_size << int(math.log(pack_size, 2))
                    if math.log(pack_size, 2) % 1.0 == 0.0 else
                    self.read_size * pack_size)

        op_id = self._get_read_op_id_fifo(fifo)

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
            rest_size = self.read_narrow_rest_size_wires[pack_size]

            # state 0
            fsm.set_index(0)
            cond = vtypes.Ands(self.read_start, self.read_op_sel == op_id)

            fsm.If(cond).goto_next()

            # state 1
            fsm.set_index(1)

            wdata = self.m.Reg('_'.join(['', self.name,
                                         'read_narrow', str(pack_size),
                                         'wdata']),
                               fifo_datawidth, initval=0)
            wvalid = self.m.Reg('_'.join(['', self.name,
                                          'read_narrow', str(pack_size),
                                          'wvalid']))

            valid_cond = vtypes.Ands(valid, self.read_op_sel == op_id)
            ack, _ = fifo.enq_rtl(wdata, cond=wvalid)

            fsm.Delay(1)(
                wvalid(0)
            )
            fsm.If(rest_size == 0, pack_count > 0)(
                wdata(vtypes.Cat(data, wdata[self.datawidth:fifo_datawidth])),
                wvalid(0),
                pack_count.inc()
            )
            fsm.If(valid_cond)(
                wdata(vtypes.Cat(data, wdata[self.datawidth:fifo_datawidth])),
                wvalid(0),
                pack_count.inc()
            )
            fsm.If(rest_size == 0, pack_count == pack_size - 1)(
                wdata(vtypes.Cat(data, wdata[self.datawidth:fifo_datawidth])),
                wvalid(1),
                pack_count(0)
            )
            fsm.If(valid_cond, pack_count == pack_size - 1)(
                wdata(vtypes.Cat(data, wdata[self.datawidth:fifo_datawidth])),
                wvalid(1),
                pack_count(0)
            )
            fsm.If(valid_cond)(
                rest_size.dec()
            )

            return

        """ new op and fsm """
        fsm = FSM(self.m, '_'.join(['', self.name,
                                    'read_narrow', str(pack_size),
                                    'fsm']),
                  self.clk, self.rst, as_module=self.fsm_as_module)
        self.read_narrow_fsms[pack_size] = fsm

        self.read_ops.append(op_id)

        rest_size = self.m.Reg('_'.join(['', self.name,
                                         'read_narrow', str(pack_size),
                                         'rest_size']),
                               self.addrwidth + 1, initval=0)
        self.read_narrow_rest_size_wires[pack_size] = rest_size

        # state 0
        cond = vtypes.Ands(self.read_start, self.read_op_sel == op_id)

        fsm.If(self.read_start)(
            rest_size(dma_size)
        )
        fsm.If(cond).goto_next()

        # state 1
        pack_count = self.m.Reg('_'.join(['', self.name,
                                          'read_narrow', str(pack_size),
                                          'pack_count']),
                                int(math.ceil(math.log(pack_size, 2))), initval=0)
        self.read_narrow_pack_counts[pack_size] = pack_count

        ready = vtypes.Not(fifo.almost_full)
        read_cond = vtypes.Ands(fsm.here, ready)

        data, last, _id, user, dest, valid = self.read_data(cond=read_cond)
        self.read_narrow_data_wires[pack_size] = data
        self.read_narrow_valid_wires[pack_size] = valid

        wdata = self.m.Reg('_'.join(['', self.name,
                                     'read_narrow', str(pack_size),
                                     'wdata']),
                           fifo_datawidth, initval=0)
        wvalid = self.m.Reg('_'.join(['', self.name,
                                      'read_narrow', str(pack_size),
                                      'wvalid']))

        valid_cond = vtypes.Ands(valid, self.read_op_sel == op_id)
        ack, _ = fifo.enq_rtl(wdata, cond=wvalid)

        fsm.Delay(1)(
            wvalid(0)
        )
        fsm.If(rest_size == 0, pack_count > 0)(
            wdata(vtypes.Cat(data, wdata[self.datawidth:fifo_datawidth])),
            wvalid(0),
            pack_count.inc()
        )
        fsm.If(valid_cond)(
            wdata(vtypes.Cat(data, wdata[self.datawidth:fifo_datawidth])),
            wvalid(0),
            pack_count.inc()
        )
        fsm.If(rest_size == 0, pack_count == pack_size - 1)(
            wdata(vtypes.Cat(data, wdata[self.datawidth:fifo_datawidth])),
            wvalid(1),
            pack_count(0)
        )
        fsm.If(valid_cond, pack_count == pack_size - 1)(
            wdata(vtypes.Cat(data, wdata[self.datawidth:fifo_datawidth])),
            wvalid(1),
            pack_count(0)
        )
        fsm.If(valid_cond)(
            rest_size.dec()
        )

        fsm.If(wvalid, rest_size == 0).goto_next()

        # state 2
        set_idle = self._set_flag(fsm)
        self.seq.If(set_idle)(
            self.read_idle(1)
        )

        fsm.goto_init()

    def _synthesize_read_fsm_fifo_wide(self, fifo, fifo_datawidth):
        """ axi.datawidth > fifo.datawidth """

        if self.datawidth % fifo_datawidth != 0:
            raise ValueError(
                'axi.datawidth must be multiple number of fifo_datawidth')

        pack_size = self.datawidth // fifo_datawidth
        shamt = int(math.log(pack_size, 2))
        res = vtypes.Mux(
            vtypes.And(self.read_size, 2 ** shamt - 1) > 0, 1, 0)
        dma_size = (self.read_size >> shamt) + res

        actual_read_size = dma_size << shamt

        op_id = self._get_read_op_id_fifo(fifo)

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
            rest_size = self.read_wide_rest_size_wires[pack_size]

            # state 0
            fsm.set_index(0)
            cond = vtypes.Ands(self.read_start, self.read_op_sel == op_id)
            fsm.If(cond).goto_next()

            # state 1
            fsm.set_index(1)
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
                wdata(wdata >> fifo_datawidth),
                wvalid(1),
                pack_count.inc()
            )
            fsm.If(valid_cond)(
                rest_size.dec()
            )

            return

        """ new op and fsm """
        fsm = FSM(self.m, '_'.join(['', self.name,
                                    'read_wide', str(pack_size),
                                    'fsm']),
                  self.clk, self.rst, as_module=self.fsm_as_module)
        self.read_wide_fsms[pack_size] = fsm

        self.read_ops.append(op_id)

        rest_size = self.m.Reg('_'.join(['', self.name,
                                         'read_wide', str(pack_size),
                                         'rest_size']),
                               self.addrwidth + 1, initval=0)
        self.read_wide_rest_size_wires[pack_size] = rest_size

        # state 0
        cond = vtypes.Ands(self.read_start, self.read_op_sel == op_id)

        fsm.If(self.read_start)(
            rest_size(dma_size)
        )
        fsm.If(cond).goto_next()

        # state 1
        pack_count = self.m.Reg('_'.join(['', self.name,
                                          'read_wide', str(pack_size),
                                          'pack_count']),
                                int(math.ceil(math.log(pack_size, 2))), initval=0)
        self.read_wide_pack_counts[pack_size] = pack_count

        ready = vtypes.Not(fifo.almost_full)
        read_cond = vtypes.Ands(fsm.here, ready)

        cond = vtypes.Ands(fsm.here, pack_count == 0, read_cond)
        data, last, _id, user, dest, valid = self.read_data(cond=cond)
        self.read_wide_data_wires[pack_size] = data
        self.read_wide_valid_wires[pack_size] = valid

        wdata = self.m.Reg('_'.join(['', self.name,
                                     'read_wide', str(pack_size),
                                     'wdata']),
                           self.datawidth, initval=0)
        wvalid = self.m.Reg('_'.join(['', self.name,
                                      'read_wide', str(pack_size),
                                      'wvalid']))

        valid_cond = vtypes.Ands(valid, self.read_op_sel == op_id)
        stay_cond = self.read_op_sel == op_id

        ack, _ = fifo.enq_rtl(wdata, cond=wvalid)

        wlast = self.m.Reg('_'.join(['', self.name,
                                     'read_wide', str(pack_size),
                                     'wlast']),
                           initval=0)

        fsm.Delay(1)(
            wvalid(0)
        )
        fsm.If(pack_count == 0, valid_cond)(
            wdata(data),
            wvalid(1),
            wlast(last),
            pack_count.inc()
        )
        fsm.If(pack_count > 0, stay_cond)(
            wdata(wdata >> fifo_datawidth),
            wvalid(1),
            pack_count.inc()
        )
        fsm.If(pack_count == pack_size - 1)(
            pack_count(0)
        )

        fsm.If(pack_count == 0, valid_cond)(
            rest_size.dec()
        )

        fsm.If(pack_count == pack_size - 1, rest_size == 0).goto_next()

        # state 2
        set_idle = self._set_flag(fsm)
        self.seq.If(set_idle)(
            self.read_idle(1)
        )

        fsm.goto_init()
