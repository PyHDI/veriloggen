from __future__ import absolute_import
from __future__ import print_function

import math
import functools
from collections import OrderedDict

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
                      'dma_read', 'dma_write') + _MutexFunction.__intrinsics__

    burstlen = 256

    def __init__(self, m, name, clk, rst,
                 datawidth=32, addrwidth=32, lite=False, noio=False,
                 num_cmd_delay=0, num_data_delay=0,
                 op_sel_width=8, fsm_as_module=False):

        AxiMaster.__init__(self, m, name, clk, rst,
                           datawidth, addrwidth, lite=lite, noio=noio)

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

        self.read_op_id_map = OrderedDict()
        self.read_op_id_count = 1
        self.read_reqs = OrderedDict()
        self.read_ops = []

        self.read_fsm = None
        self.read_data_wire = None
        self.read_valid_wire = None

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

        rdata = self.m.TmpReg(self.datawidth, initval=0,
                              signed=True, prefix='axim_rdata')
        fsm.If(valid)(rdata(data))
        fsm.Then().goto_next()

        return rdata

    def write(self, fsm, global_addr):
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

        if self.lite:
            raise TypeError('AXIM-lite does not support DMA.')

        if isinstance(ram, (tuple, list)):
            ram = MultibankRAM(rams=ram)

        if not isinstance(ram, (RAM, MultibankRAM)):
            raise TypeError('RAM object is required.')

        if ram_method is None:
            ram_method = getattr(ram, 'write_dataflow')

        start = self._set_flag(fsm)

        for _ in range(self.num_cmd_delay + 1):
            fsm.goto_next()

        self._set_read_request(ram, ram_method, start,
                               local_addr, global_addr, size, local_stride)

        self._synthesize_read_fsm(ram, port, ram_method)

        fsm.goto_next()
        fsm.If(self.read_idle).goto_next()

    def dma_write(self, fsm, ram, local_addr, global_addr, size,
                  local_stride=1, port=0, ram_method=None):

        pass

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

    def _get_op_id(self, ram, ram_method):

        ram_id = ram._id()
        ram_method_name = (ram_method.func.__name__
                           if isinstance(ram_method, functools.partial) else
                           ram_method.__name__)
        op = (ram_id, ram_method_name)

        if op in self.read_op_id_map:
            op_id = self.read_op_id_map[op]
        else:
            op_id = self.read_op_id_count
            self.read_op_id_count += 1
            self.read_op_id_map[op] = op_id

        return op_id

    def _set_read_request(self, ram, ram_method, start,
                          local_addr, global_addr, size, local_stride):

        op_id = self._get_op_id(ram, ram_method)

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

        read_start = self.m.Reg('_'.join(['', self.name, ram.name, 'read_start']),
                                initval=0)
        read_op_sel = self.m.Reg('_'.join(['', self.name, ram.name, 'read_op_sel']),
                                 self.op_sel_width, initval=0)
        read_local_addr = self.m.Reg('_'.join(['', self.name, ram.name, 'read_local_addr']),
                                     self.addrwidth, initval=0)
        read_global_addr = self.m.Reg('_'.join(['', self.name, ram.name, 'read_global_addr']),
                                      self.addrwidth, initval=0)
        read_size = self.m.Reg('_'.join(['', self.name, ram.name, 'read_size']),
                               self.addrwidth + 1, initval=0)
        read_local_stride = self.m.Reg('_'.join(['', self.name, ram.name, 'read_local_stride']),
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

        self.seq(
            self.read_start(read_start),
            self.read_op_sel(read_op_sel),
            self.read_local_addr(read_local_addr),
            self.read_global_addr(read_global_addr),
            self.read_size(read_size),
            self.read_local_stride(read_local_stride)
        )

    def _synthesize_read_fsm(self, ram, port, ram_method):

        port = vtypes.to_int(port)
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

        op_id = self._get_op_id(ram, ram_method)

        if op_id in self.read_ops:
            """ already synthesized op """
            return

        if self.read_fsm is not None:
            """ new op """
            self.read_ops.append(op_id)

            wdata, wvalid, w = self._get_op_write_dataflow(ram_datawidth)

            # state 0
            self.read_fsm.set_index(0)
            cond = vtypes.Ands(self.read_start, self.read_op_sel == op_id)
            ram_method(port, self.read_local_addr, w, self.read_size,
                       stride=self.read_local_stride, cond=cond)

            # state 2
            self.read_fsm.set_index(2)
            self.read_fsm.Delay(1)(
                wvalid(0)
            )
            self.read_fsm.If(self.read_valid_wire)(
                wdata(self.read_data_wire),
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

        fsm.If(self.read_start)(
            cur_global_addr(self.mask_addr(self.read_global_addr)),
            rest_size(self.read_size)
        )
        fsm.If(self.read_start).goto_next()

        # state 1
        check_state = fsm.current
        self._check_4KB_boundary(fsm, max_burstlen,
                                 cur_global_addr, cur_size, rest_size)

        ack, counter = self.read_request(cur_global_addr, cur_size, cond=fsm)
        fsm.If(ack).goto_next()

        # state 2
        data, valid, last = self.read_data(cond=fsm)
        self.read_data_wire = data
        self.read_valid_wire = valid

        fsm.Delay(1)(
            wvalid(0)
        )
        fsm.If(valid)(
            wdata(data),
            wvalid(1),
        )

        fsm.If(valid, last)(
            cur_global_addr.add(optimize(cur_size * (self.datawidth // 8)))
        )
        fsm.If(valid, last, rest_size > 0).goto(check_state)
        fsm.If(valid, last, rest_size == 0).goto_next()

        set_idle = self._set_flag(fsm)
        self.seq.If(set_idle)(
            self.read_idle(1)
        )

        fsm.goto_init()

    def _synthesize_read_fsm_narrow(self, ram, port, ram_method, ram_datawidth):
        pass

    def _synthesize_read_fsm_wide(self, ram, port, ram_method, ram_datawidth):
        pass

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
                 lite=False, noio=False, length=4, fsm_as_module=False):

        AXIS.__init__(self, m, name, clk, rst, datawidth=datawidth, addrwidth=addrwidth,
                      lite=lite, noio=noio)

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

        if self.lite:
            self._set_register_lite_fsm()
        else:
            self._set_register_full_fsm()

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


def AXIMLite(m, name, clk, rst, datawidth=32, addrwidth=32,
             noio=False):

    return AXIM(m, name, clk, rst, datawidth=datawidth, addrwidth=addrwidth,
                lite=True, noio=noio)


def AXISLite(m, name, clk, rst, datawidth=32, addrwidth=32,
             noio=False):

    return AXIS(m, name, clk, rst, datawidth=datawidth, addrwidth=addrwidth,
                lite=True, noio=noio)


def AXISLiteRegister(m, name, clk, rst, datawidth=32, addrwidth=32,
                     noio=False, length=4, fsm_as_module=False):

    return AXISRegister(m, name, clk, rst, datawidth=datawidth, addrwidth=addrwidth,
                        lite=True, noio=noio, length=length, fsm_as_module=fsm_as_module)
