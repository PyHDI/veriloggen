from __future__ import absolute_import
from __future__ import print_function

import math
import functools
import ast
import inspect
import textwrap
from collections import OrderedDict

import veriloggen.core.vtypes as vtypes
import veriloggen.types.fixed as fxd
from veriloggen.seq.seq import make_condition
from veriloggen.fsm.fsm import FSM
from veriloggen.seq.seq import Seq
from veriloggen.stream.stream import Stream as BaseStream
from veriloggen.stream.stypes import Substream as BaseSubstream

from . import compiler
from . import thread

mode_width = 4
mode_idle = vtypes.Int(0, mode_width, base=2)
mode_ram_normal = vtypes.Int(1 << 0, mode_width, base=2)
mode_ram_pattern = vtypes.Int(1 << 1, mode_width, base=2)
mode_ram_multipattern = vtypes.Int(1 << 2, mode_width, base=2)
mode_fifo = vtypes.Int(1 << 3, mode_width, base=2)


def TmpStream(m, clk, rst,
              datawidth=32, addrwidth=32,
              max_pattern_length=4, ram_sel_width=8,
              fsm_as_module=False):
    name = compiler._tmp_name('_tmp_stream')
    return Stream(m, name, clk, rst,
                  datawidth, addrwidth,
                  max_pattern_length, ram_sel_width,
                  fsm_as_module=False)


class Stream(BaseStream):
    __intrinsics__ = ('set_source', 'set_source_pattern', 'set_source_multidim',
                      'set_source_multipattern', 'set_source_empty',
                      'set_source_fifo',
                      'set_sink', 'set_sink_pattern', 'set_sink_multidim',
                      'set_sink_multipattern', 'set_sink_immediate',
                      'set_sink_fifo',
                      'set_sink_empty',
                      'set_constant',
                      'set_read_RAM', 'set_write_RAM', 'set_read_modify_write_RAM',
                      'read_sink',
                      'run', 'join', 'done',
                      'source_join', 'source_done',
                      'sink_join', 'sink_done',
                      'source_join_and_run',
                      'enable_dump', 'disable_dump')

    ram_delay = 0

    def __init__(self, m, name, clk, rst,
                 datawidth=32, addrwidth=32,
                 max_pattern_length=4, max_multipattern_length=2,
                 ram_sel_width=8, fsm_as_module=False,
                 dump=False, dump_base=10, dump_mode='all'):

        # pipeline control
        self.stream_ivalid = m.Reg('_'.join(['', name, 'stream_ivalid']), initval=0)
        self.stream_oready = m.Wire('_'.join(['', name, 'stream_oready']))
        self.stream_oready.assign(1)

        BaseStream.__init__(self, module=m, clock=clk, reset=rst,
                            ivalid=self.stream_ivalid,
                            oready=self.stream_oready,
                            no_hook=True,
                            dump=dump, dump_base=dump_base, dump_mode=dump_mode)

        self.name = name
        self.datawidth = datawidth
        self.addrwidth = addrwidth

        self.max_pattern_length = max_pattern_length
        self.max_multipattern_length = max_multipattern_length
        self.ram_sel_width = ram_sel_width
        self.fsm_as_module = fsm_as_module

        self.stream_synthesized = False
        self.fsm_synthesized = False

        self.fsm = FSM(self.module, '_%s_fsm' %
                       self.name, self.clock, self.reset,
                       as_module=self.fsm_as_module)

        self.run_flag = self.module.Wire(
            '_'.join(['', self.name, 'run_flag']))
        self.run_flag.assign(0)

        self.source_start = self.module.Reg(
            '_'.join(['', self.name, 'source_start']), initval=0)
        self.source_stop = self.module.Reg(
            '_'.join(['', self.name, 'source_stop']), initval=0)
        self.source_busy = self.module.Reg(
            '_'.join(['', self.name, 'source_busy']), initval=0)

        self.sink_start = self.module.Wire(
            '_'.join(['', self.name, 'sink_start']))
        self.sink_stop = self.module.Wire(
            '_'.join(['', self.name, 'sink_stop']))
        self.sink_busy = self.module.Wire(
            '_'.join(['', self.name, 'sink_busy']))

        self.busy = self.module.Wire(
            '_'.join(['', self.name, 'busy']))
        self.busy_buf = self.module.Reg(
            '_'.join(['', self.name, 'busy_buf']), initval=0)

        self.is_root = self.module.Wire('_'.join(['', self.name, 'is_root']))
        self.is_root.assign(1)

        self.reduce_reset = None
        self.reduce_reset_var = None

        self.sources = OrderedDict()
        self.sinks = OrderedDict()
        self.constants = OrderedDict()
        self.substreams = []
        self.read_rams = OrderedDict()
        self.write_rams = OrderedDict()
        self.read_modify_write_rams = OrderedDict()

        self.var_name_map = OrderedDict()
        self.var_id_map = OrderedDict()
        self.var_id_name_map = OrderedDict()
        self.var_name_id_map = OrderedDict()
        self.var_id_count = 0

        self.source_idle_map = OrderedDict()
        self.sink_when_map = OrderedDict()

        self.buf_id_count = 1  # '0' is reserved for idle
        self.buf_id_map = OrderedDict()  # key: buf._id(), value: count

        self.fsm_id_count = 0

    def source(self, name=None, datawidth=None, point=0, signed=True):
        if self.stream_synthesized:
            raise ValueError(
                'cannot modify the stream because already synthesized')

        _id = self.var_id_count
        if name is None:
            name = 'source_%d' % _id

        if name in self.var_name_map:
            raise ValueError("'%s' is already defined in stream '%s'" %
                             (name, self.name))

        prefix = self._prefix(name)

        self.var_id_count += 1

        if datawidth is None:
            datawidth = self.datawidth

        var = self.Variable(self._dataname(name), datawidth, point, signed)

        self.sources[name] = var
        self.var_id_map[_id] = var
        self.var_name_map[name] = var
        self.var_id_name_map[_id] = name
        self.var_name_id_map[name] = _id

        var.source_fsm = None
        var.source_pat_fsm = None
        var.source_multipat_fsm = None

        var.source_idle = self.module.Reg('_%s_idle' % prefix, initval=1)
        self.source_idle_map[name] = var.source_idle

        var.source_count = self.module.Reg('_%s_source_count' % prefix,
                                           self.addrwidth + 1, initval=0)

        # 4'b0000: set_source_empty, 4'b0001: set_source,
        # 4'b0010: set_source_pattern, 4'b0100: set_source_multipattern
        # 4'b1000: set_source_fifo
        var.source_mode = self.module.Reg('_%s_source_mode' % prefix, mode_width,
                                          initval=mode_idle)
        var.source_mode_buf = self.module.Reg('_%s_source_mode_buf' % prefix, mode_width,
                                              initval=mode_idle)

        # set_source
        var.source_offset = self.module.Reg('_%s_source_offset' % prefix,
                                            self.addrwidth, initval=0)
        var.source_size = self.module.Reg('_%s_source_size' % prefix,
                                          self.addrwidth + 1, initval=0)
        var.source_stride = self.module.Reg('_%s_source_stride' % prefix,
                                            self.addrwidth, initval=0)

        var.source_offset_buf = self.module.Reg('_%s_source_offset_buf' % prefix,
                                                self.addrwidth, initval=0)
        var.source_size_buf = self.module.Reg('_%s_source_size_buf' % prefix,
                                              self.addrwidth + 1, initval=0)
        var.source_stride_buf = self.module.Reg('_%s_source_stride_buf' % prefix,
                                                self.addrwidth, initval=0)

        # set_source_pattern
        var.source_pat_cur_offsets = None
        var.source_pat_sizes = None
        var.source_pat_strides = None
        var.source_pat_counts = None

        var.source_pat_size_bufs = None
        var.source_pat_stride_bufs = None

        # set_source_multipattern
        var.source_multipat_num_patterns = None
        var.source_multipat_offsets = None
        var.source_multipat_cur_offsets = None
        var.source_multipat_sizes = None
        var.source_multipat_strides = None

        var.source_multipat_offset_bufs = None
        var.source_multipat_size_bufs = None
        var.source_multipat_stride_bufs = None

        # RAM, FIFO
        var.source_id_map = OrderedDict()
        var.source_sel = self.module.Reg('_%s_source_sel' % prefix,
                                         self.ram_sel_width, initval=0)

        # RAM
        var.source_ram_raddr = self.module.Reg('_%s_source_ram_raddr' % prefix,
                                               self.addrwidth, initval=0)
        var.source_ram_renable = self.module.Reg('_%s_source_ram_renable' % prefix,
                                                 initval=0)
        var.source_ram_rdata = self.module.Wire('_%s_source_ram_rdata' % prefix,
                                                datawidth)

        # FIFO
        var.source_fifo_deq = self.module.Reg('_%s_source_fifo_deq' % prefix,
                                              initval=0)
        var.source_fifo_rdata = self.module.Wire('_%s_source_fifo_rdata' % prefix,
                                                 datawidth)

        # empty
        var.has_source_empty = False
        var.source_empty_data = self.module.Reg('_%s_source_empty_data' % prefix,
                                                datawidth, initval=0)

        # default value
        self.seq.If(self.stream_oready)(
            var.source_ram_renable(0),
            var.source_fifo_deq(0)
        )

        self.seq(
            var.source_idle(var.source_idle)
        )

        return var

    def sink(self, data, name=None, when=None, when_name=None):
        if self.stream_synthesized:
            raise ValueError(
                'cannot modify the stream because already synthesized')

        _id = self.var_id_count
        if name is None:
            name = 'sink_%d' % _id

        if name in self.var_name_map:
            raise ValueError("'%s' is already defined in stream '%s'" %
                             (name, self.name))

        elif data.output_data is not None:
            # implicit Alias
            alias = self.Alias(data)
            return self.sink(alias, name, when, when_name)

        else:
            data.output(self._dataname(name))

        prefix = self._prefix(name)

        self.var_id_count += 1

        self.sinks[name] = data
        self.var_id_map[_id] = data
        self.var_name_map[name] = data
        self.var_id_name_map[_id] = name
        self.var_name_id_map[name] = _id

        data.sink_fsm = None
        data.sink_pat_fsm = None
        data.sink_multipat_fsm = None

        data.sink_count = self.module.Reg('_%s_sink_count' % prefix,
                                          self.addrwidth + 1, initval=0)

        # 4'b0000: set_sink_empty, 4'b0001: set_sink,
        # 4'b0010: set_sink_pattern, 4'b0100: set_sink_multipattern
        # 4'b1000: set_sink_fifo
        data.sink_mode = self.module.Reg('_%s_sink_mode' % prefix, mode_width,
                                         initval=mode_idle)
        data.sink_mode_buf = self.module.Reg('_%s_sink_mode_buf' % prefix, mode_width,
                                             initval=mode_idle)

        # set_sink
        data.sink_offset = self.module.Reg('_%s_sink_offset' % prefix,
                                           self.addrwidth, initval=0)
        data.sink_size = self.module.Reg('_%s_sink_size' % prefix,
                                         self.addrwidth + 1, initval=0)
        data.sink_stride = self.module.Reg('_%s_sink_stride' % prefix,
                                           self.addrwidth, initval=0)

        data.sink_offset_buf = self.module.Reg('_%s_sink_offset_buf' % prefix,
                                               self.addrwidth, initval=0)
        data.sink_size_buf = self.module.Reg('_%s_sink_size_buf' % prefix,
                                             self.addrwidth + 1, initval=0)
        data.sink_stride_buf = self.module.Reg('_%s_sink_stride_buf' % prefix,
                                               self.addrwidth, initval=0)

        # set_sink_pattern
        data.sink_pat_cur_offsets = None
        data.sink_pat_sizes = None
        data.sink_pat_strides = None
        data.sink_pat_counts = None

        data.sink_pat_size_bufs = None
        data.sink_pat_stride_bufs = None

        # set_sink_multipattern
        data.sink_multipat_num_patterns = None
        data.sink_multipat_offsets = None
        data.sink_multipat_cur_offsets = None
        data.sink_multipat_sizes = None
        data.sink_multipat_strides = None

        data.sink_multipat_offset_bufs = None
        data.sink_multipat_size_bufs = None
        data.sink_multipat_stride_bufs = None

        # RAM, FIFO
        data.sink_id_map = OrderedDict()
        data.sink_sel = self.module.Reg('_%s_sink_sel' % prefix,
                                        self.ram_sel_width, initval=0)

        # RAM
        data.sink_ram_waddr = self.module.Reg('_%s_sink_waddr' % prefix,
                                              self.addrwidth, initval=0)
        data.sink_ram_wenable = self.module.Reg('_%s_sink_wenable' % prefix,
                                                initval=0)
        data.sink_ram_wdata = self.module.Reg('_%s_sink_wdata' % prefix,
                                              data.width, initval=0)

        # FIFO
        data.sink_fifo_enq = self.module.Reg('_%s_sink_fifo_enq' % prefix,
                                             initval=0)
        data.sink_fifo_wdata = self.module.Reg('_%s_sink_fifo_wdata' % prefix,
                                               data.width, initval=0)

        # immediate
        data.sink_immediate = self.module.Reg('_%s_sink_immediate' % prefix,
                                              data.width, initval=0)

        # default value
        self.seq.If(self.stream_oready)(
            data.sink_ram_wenable(0),
            data.sink_fifo_enq(0)
        )

        if when is not None:
            self.sink(when, when_name)
            self.sink_when_map[name] = when

    def constant(self, name=None, datawidth=None, point=0, signed=True):
        if self.stream_synthesized:
            raise ValueError(
                'cannot modify the stream because already synthesized')

        _id = self.var_id_count
        if name is None:
            name = 'constant_%d' % _id

        if name in self.var_name_map:
            raise ValueError("'%s' is already defined in stream '%s'" %
                             (name, self.name))

        prefix = self._prefix(name)

        self.var_id_count += 1

        if datawidth is None:
            datawidth = self.datawidth

        var = self.Variable(self._dataname(name), datawidth, point, signed)

        self.constants[name] = var
        self.var_id_map[_id] = var
        self.var_name_map[name] = var
        self.var_id_name_map[_id] = name
        self.var_name_id_map[name] = _id

        var.next_constant_data = self.module.Reg('_%s_next_constant_data' % prefix,
                                                 datawidth, initval=0)
        var.next_constant_data.no_write_check = True
        var.has_constant_data = False

        return var

    def substream(self, substrm):
        _id = self.var_id_count
        name = 'substream_%d' % _id

        if name in self.var_name_map:
            raise ValueError("'%s' is already defined in stream '%s'" %
                             (name, self.name))

        prefix = self._prefix(name)
        self.var_id_count += 1

        sub = Substream(self.module, self.clock, self.reset, substrm, self)
        self.substreams.append(sub)
        return sub

    def read_RAM(self, name, addr, when=None,
                 datawidth=None, point=0, signed=True):

        if self.stream_synthesized:
            raise ValueError(
                'cannot modify the stream because already synthesized')

        _id = self.var_id_count
        if name is None:
            name = 'read_ram_%d' % _id

        if name in self.var_name_map:
            raise ValueError("'%s' is already defined in stream '%s'" %
                             (name, self.name))

        prefix = self._prefix(name)

        self.var_id_count += 1

        if datawidth is None:
            datawidth = self.datawidth

        var = self.ReadRAM(addr, when=when,
                           width=datawidth, point=point, signed=signed, ram_name=name)

        self.read_rams[name] = var
        self.var_id_map[_id] = var
        self.var_name_map[name] = var
        self.var_id_name_map[_id] = name
        self.var_name_id_map[name] = _id

        var.read_ram_id_map = OrderedDict()
        var.read_ram_sel = self.module.Reg('_%s_read_ram_sel' % prefix,
                                           self.ram_sel_width, initval=0)

        return var

    def write_RAM(self, name, addr, data, when=None):

        if self.stream_synthesized:
            raise ValueError(
                'cannot modify the stream because already synthesized')

        _id = self.var_id_count
        if name is None:
            name = 'write_ram_%d' % _id

        if name in self.var_name_map:
            raise ValueError("'%s' is already defined in stream '%s'" %
                             (name, self.name))

        prefix = self._prefix(name)

        self.var_id_count += 1

        var = self.WriteRAM(addr, data, when=when, ram_name=name)

        self.write_rams[name] = var
        self.var_id_map[_id] = var
        self.var_name_map[name] = var
        self.var_id_name_map[_id] = name
        self.var_name_id_map[name] = _id

        var.write_ram_id_map = OrderedDict()
        var.write_ram_sel = self.module.Reg('_%s_write_ram_sel' % prefix,
                                            self.ram_sel_width, initval=0)

        return var

    def read_modify_write_RAM(self, name, raddrs, waddr, op, op_args, when=None,
                              datawidth_list=None, point_list=None, signed_list=None):

        if self.stream_synthesized:
            raise ValueError(
                'cannot modify the stream because already synthesized')

        _id = self.var_id_count
        if name is None:
            name = 'read_modify_write_ram_%d' % _id

        if name in self.var_name_map:
            raise ValueError("'%s' is already defined in stream '%s'" %
                             (name, self.name))

        self.var_id_count += 1

        if datawidth_list is None:
            datawidth_list = [None for raddr in raddrs]
            point_list = [None for raddr in raddrs]
            signed_list = [True for raddr in raddrs]

        if len(raddrs) > 1:
            raddrs = self.Sync(*raddrs)

        read_vars = []
        read_rams = []

        for i, (raddr, datawidth, point, signed) in enumerate(
                zip(raddrs, datawidth_list, point_list, signed_list)):

            read_name = '_'.join([name, 'read', '%d' % i])
            read_var = self.read_RAM(read_name, raddr, when=None,
                                     datawidth=datawidth, point=point, signed=signed)
            read_var.latency = 1
            read_vars.append(read_var)
            read_rams.append(read_name)

        read_vars = [self.ForwardDest(read_var, raddr)
                     for read_var, raddr in zip(read_vars, raddrs)]

        args = []
        args.extend(read_vars)
        args.extend(op_args)
        write_var = op(*args)

        for read_var in read_vars:
            self.ForwardSource(write_var, waddr, read_var)

        write_name = '_'.join([name, 'write'])
        write_var = self.write_RAM(write_name, waddr, write_var, when=when)
        write_ram = write_name

        read_rams = tuple(read_rams)

        self.read_modify_write_rams[name] = (read_rams, write_ram)
        self.var_id_map[_id] = (read_rams, write_ram)
        self.var_name_map[name] = (read_rams, write_ram)
        self.var_id_name_map[_id] = name
        self.var_name_id_map[name] = _id

        return write_var

    def set_source(self, fsm, name, ram, offset, size, stride=1, port=0):
        """ intrinsic method to assign RAM property to a source stream """

        if not self.stream_synthesized:
            self._implement_stream()

        if isinstance(name, str):
            var = self.var_name_map[name]
        elif isinstance(name, vtypes.Str):
            name = name.value
            var = self.var_name_map[name]
        elif isinstance(name, int):
            var = self.var_id_map[name]
        elif isinstance(name, vtypes.Int):
            name = name.value
            var = self.var_id_map[name]
        else:
            raise TypeError('Unsupported index name')

        if name not in self.sources:
            raise NameError("No such stream '%s'" % name)

        set_cond = self._set_flag(fsm)

        self.seq.If(set_cond)(
            var.source_mode(mode_ram_normal),
            var.source_offset(offset),
            var.source_size(size),
            var.source_stride(stride)
        )

        port = vtypes.to_int(port)
        self._setup_source_ram(ram, var, port, set_cond)
        self._synthesize_set_source(var, name)

        fsm.goto_next()

    def set_source_pattern(self, fsm, name, ram, offset, pattern, port=0):
        """ intrinsic method to assign RAM property to a source stream """

        if not self.stream_synthesized:
            self._implement_stream()

        if isinstance(name, str):
            var = self.var_name_map[name]
        elif isinstance(name, vtypes.Str):
            name = name.value
            var = self.var_name_map[name]
        elif isinstance(name, int):
            var = self.var_id_map[name]
        elif isinstance(name, vtypes.Int):
            name = name.value
            var = self.var_id_map[name]
        else:
            raise TypeError('Unsupported index name')

        if name not in self.sources:
            raise NameError("No such stream '%s'" % name)

        if not isinstance(pattern, (tuple, list)):
            raise TypeError('pattern must be list or tuple.')

        if not pattern:
            raise ValueError(
                'pattern must have one (size, stride) pair at least.')

        if not isinstance(pattern[0], (tuple, list)):
            pattern = (pattern,)

        pattern = tuple(pattern)

        if len(pattern) > self.max_pattern_length:
            raise ValueError(
                "'pattern' length exceeds maximum pattern length.")

        self._make_source_pattern_vars(var, name)

        set_cond = self._set_flag(fsm)

        self.seq.If(set_cond)(
            var.source_mode(mode_ram_pattern),
            var.source_offset(offset)
        )

        pad = tuple([(1, 0)
                     for _ in range(self.max_pattern_length - len(pattern))])

        for (source_pat_size, source_pat_stride,
             (size, stride)) in zip(var.source_pat_sizes, var.source_pat_strides,
                                    pattern + pad):
            self.seq.If(set_cond)(
                source_pat_size(size),
                source_pat_stride(stride)
            )

        port = vtypes.to_int(port)
        self._setup_source_ram(ram, var, port, set_cond)
        self._synthesize_set_source_pattern(var, name)

        fsm.goto_next()

    def set_source_multidim(self, fsm, name, ram, offset, shape, order=None, port=0):
        """ intrinsic method to assign RAM property to a source stream """

        if order is None:
            order = list(reversed(range(len(shape))))

        pattern = self._to_pattern(shape, order)
        return self.set_source_pattern(fsm, name, ram, offset, pattern, port)

    def set_source_multipattern(self, fsm, name, ram, offsets, patterns, port=0):
        """ intrinsic method to assign multiple patterns to a RAM """

        if not self.stream_synthesized:
            self._implement_stream()

        if isinstance(name, str):
            var = self.var_name_map[name]
        elif isinstance(name, vtypes.Str):
            name = name.value
            var = self.var_name_map[name]
        elif isinstance(name, int):
            var = self.var_id_map[name]
        elif isinstance(name, vtypes.Int):
            name = name.value
            var = self.var_id_map[name]
        else:
            raise TypeError('Unsupported index name')

        if name not in self.sources:
            raise NameError("No such stream '%s'" % name)

        if not isinstance(patterns, (tuple, list)):
            raise TypeError('patterns must be list or tuple.')

        if not patterns:
            raise ValueError(
                'patterns must have one [(size, stride)] list at least.')

        if not isinstance(offsets, (tuple, list)):
            offsets = [offsets] * len(patterns)

        if not offsets:
            raise ValueError('offsets must have one offset value at least.')

        offsets = tuple(offsets)
        patterns = tuple(patterns)

        if len(offsets) != len(patterns):
            raise ValueError(
                "number of offsets must be 1 or equal to the number of patterns.")

        if len(offsets) > self.max_multipattern_length:
            raise ValueError(
                "'offsets' length exceeds maximum multipattern length.")

        if len(patterns) > self.max_multipattern_length:
            raise ValueError(
                "'patterns' length exceeds maximum multipattern length.")

        for pattern in patterns:
            if len(pattern) > self.max_pattern_length:
                raise ValueError(
                    "'pattern' length exceeds maximum pattern length.")

        self._make_source_multipattern_vars(var, name)

        set_cond = self._set_flag(fsm)

        self.seq.If(set_cond)(
            var.source_mode(mode_ram_multipattern),
            var.source_multipat_num_patterns(len(patterns))
        )

        offsets_pad = tuple(
            [0 for _ in range(self.max_multipattern_length - len(patterns))])

        for offset, multipat_offset in zip(offsets + offsets_pad,
                                           var.source_multipat_offsets):
            self.seq.If(set_cond)(
                multipat_offset(offset)
            )

        for multipat_sizes, multipat_strides, pattern in zip(
                var.source_multipat_sizes, var.source_multipat_strides, patterns):
            pad = tuple([(1, 0)
                         for _ in range(self.max_pattern_length - len(pattern))])

            for (multipat_size, multipat_stride,
                 (size, stride)) in zip(multipat_sizes, multipat_strides,
                                        pattern + pad):
                self.seq.If(set_cond)(
                    multipat_size(size),
                    multipat_stride(stride)
                )

        port = vtypes.to_int(port)
        self._setup_source_ram(ram, var, port, set_cond)
        self._synthesize_set_source_multipattern(var, name)

        fsm.goto_next()

    def set_source_fifo(self, fsm, name, fifo, size):
        """ intrinsic method to assign FIFO property to a source stream """

        if not self.stream_synthesized:
            self._implement_stream()

        if isinstance(name, str):
            var = self.var_name_map[name]
        elif isinstance(name, vtypes.Str):
            name = name.value
            var = self.var_name_map[name]
        elif isinstance(name, int):
            var = self.var_id_map[name]
        elif isinstance(name, vtypes.Int):
            name = name.value
            var = self.var_id_map[name]
        else:
            raise TypeError('Unsupported index name')

        if name not in self.sources:
            raise NameError("No such stream '%s'" % name)

        set_cond = self._set_flag(fsm)

        self.seq.If(set_cond)(
            var.source_mode(mode_fifo),
            var.source_size(size),
        )

        self._setup_source_fifo(fifo, var, set_cond)
        self._synthesize_set_source_fifo(var, name)

        fsm.goto_next()

    def set_source_empty(self, fsm, name, value=0):

        if not self.stream_synthesized:
            self._implement_stream()

        if isinstance(name, str):
            var = self.var_name_map[name]
        elif isinstance(name, vtypes.Str):
            name = name.value
            var = self.var_name_map[name]
        elif isinstance(name, int):
            var = self.var_id_map[name]
        elif isinstance(name, vtypes.Int):
            name = name.value
            var = self.var_id_map[name]
        else:
            raise TypeError('Unsupported index name')

        if name not in self.sources:
            raise NameError("No such stream '%s'" % name)

        set_cond = self._set_flag(fsm)

        self.seq.If(set_cond)(
            var.source_mode(mode_idle),
            var.source_empty_data(value)
        )

        if var.has_source_empty:
            fsm.goto_next()
            return

        source_start = vtypes.Ands(self.source_start, self.stream_oready,
                                   vtypes.Not(vtypes.Uor(vtypes.And(var.source_mode, mode_idle))))

        self.seq.If(source_start)(
            var.source_idle(1)
        )

        wdata = var.source_empty_data
        wenable = vtypes.Ands(source_start, self.is_root)
        var.write(wdata, wenable)

        var.has_source_empty = True

        fsm.goto_next()

    def set_sink(self, fsm, name, ram, offset, size, stride=1, port=0):
        """ intrinsic method to assign RAM property to a sink stream """

        if not self.stream_synthesized:
            self._implement_stream()

        if isinstance(name, str):
            var = self.var_name_map[name]
        elif isinstance(name, vtypes.Str):
            name = name.value
            var = self.var_name_map[name]
        elif isinstance(name, int):
            var = self.var_id_map[name]
        elif isinstance(name, vtypes.Int):
            name = name.value
            var = self.var_id_map[name]
        else:
            raise TypeError('Unsupported index name')

        if name not in self.sinks:
            raise NameError("No such stream '%s'" % name)

        set_cond_base = self._set_flag(fsm, self.stream_oready)
        set_cond = self._delay_from_start_to_sink(set_cond_base)
        sink_offset = self._delay_from_start_to_sink(offset)
        sink_size = self._delay_from_start_to_sink(size)
        sink_stride = self._delay_from_start_to_sink(stride)

        self.seq.If(set_cond)(
            var.sink_mode(mode_ram_normal),
            var.sink_offset(sink_offset),
            var.sink_size(sink_size),
            var.sink_stride(sink_stride)
        )

        port = vtypes.to_int(port)
        self._setup_sink_ram(ram, var, port, set_cond)
        self._synthesize_set_sink(var, name)

        fsm.If(self.stream_oready).goto_next()

    def set_sink_pattern(self, fsm, name, ram, offset, pattern, port=0):
        """ intrinsic method to assign RAM property to a sink stream """

        if not self.stream_synthesized:
            self._implement_stream()

        if isinstance(name, str):
            var = self.var_name_map[name]
        elif isinstance(name, vtypes.Str):
            name = name.value
            var = self.var_name_map[name]
        elif isinstance(name, int):
            var = self.var_id_map[name]
        elif isinstance(name, vtypes.Int):
            name = name.value
            var = self.var_id_map[name]
        else:
            raise TypeError('Unsupported index name')

        if name not in self.sinks:
            raise NameError("No such stream '%s'" % name)

        if not isinstance(pattern, (tuple, list)):
            raise TypeError('pattern must be list or tuple.')

        if not pattern:
            raise ValueError(
                'pattern must have one (size, stride) pair at least.')

        if not isinstance(pattern[0], (tuple, list)):
            pattern = (pattern,)

        pattern = tuple(pattern)

        if len(pattern) > self.max_pattern_length:
            raise ValueError(
                "'pattern' length exceeds maximum pattern length.")

        self._make_sink_pattern_vars(var, name)

        set_cond_base = self._set_flag(fsm, self.stream_oready)
        set_cond = self._delay_from_start_to_sink(set_cond_base)
        sink_offset = self._delay_from_start_to_sink(offset)

        self.seq.If(set_cond)(
            var.sink_mode(mode_ram_pattern),
            var.sink_offset(sink_offset)
        )

        pad = tuple([(1, 0)
                     for _ in range(self.max_pattern_length - len(pattern))])

        for (sink_pat_size, sink_pat_stride,
             (size, stride)) in zip(var.sink_pat_sizes, var.sink_pat_strides,
                                    pattern + pad):

            sink_size = self._delay_from_start_to_sink(size)
            sink_stride = self._delay_from_start_to_sink(stride)

            self.seq.If(set_cond)(
                sink_pat_size(sink_size),
                sink_pat_stride(sink_stride)
            )

        port = vtypes.to_int(port)
        self._setup_sink_ram(ram, var, port, set_cond)
        self._synthesize_set_sink_pattern(var, name)

        fsm.If(self.stream_oready).goto_next()

    def set_sink_multidim(self, fsm, name, ram, offset, shape, order=None, port=0):
        """ intrinsic method to assign RAM property to a sink stream """

        if order is None:
            order = list(reversed(range(len(shape))))

        pattern = self._to_pattern(shape, order)
        return self.set_sink_pattern(fsm, name, ram, offset, pattern, port)

    def set_sink_multipattern(self, fsm, name, ram, offsets, patterns, port=0):
        """ intrinsic method to assign multiple patterns to a RAM """

        if not self.stream_synthesized:
            self._implement_stream()

        if isinstance(name, str):
            var = self.var_name_map[name]
        elif isinstance(name, vtypes.Str):
            name = name.value
            var = self.var_name_map[name]
        elif isinstance(name, int):
            var = self.var_id_map[name]
        elif isinstance(name, vtypes.Int):
            name = name.value
            var = self.var_id_map[name]
        else:
            raise TypeError('Unsupported index name')

        if name not in self.sinks:
            raise NameError("No such stream '%s'" % name)

        if not isinstance(patterns, (tuple, list)):
            raise TypeError('patterns must be list or tuple.')

        if not patterns:
            raise ValueError(
                'patterns must have one [(size, stride)] list at least.')

        if not isinstance(offsets, (tuple, list)):
            offsets = [offsets] * len(patterns)

        if not offsets:
            raise ValueError('offsets must have one offset value at least.')

        offsets = tuple(offsets)
        patterns = tuple(patterns)

        if len(offsets) != len(patterns):
            raise ValueError(
                "number of offsets must be 1 or equal to the number of patterns.")

        if len(offsets) > self.max_multipattern_length:
            raise ValueError(
                "'offsets' length exceeds maximum multipattern length.")

        if len(patterns) > self.max_multipattern_length:
            raise ValueError(
                "'patterns' length exceeds maximum multipattern length.")

        for pattern in patterns:
            if len(pattern) > self.max_pattern_length:
                raise ValueError(
                    "'pattern' length exceeds maximum pattern length.")

        self._make_sink_multipattern_vars(var, name)

        set_cond_base = self._set_flag(fsm, self.stream_oready)
        set_cond = self._delay_from_start_to_sink(set_cond_base)

        self.seq.If(set_cond)(
            var.sink_mode(mode_ram_multipattern),
            var.sink_multipat_num_patterns(len(patterns))
        )

        offsets_pad = tuple(
            [0 for _ in range(self.max_multipattern_length - len(patterns))])

        for offset, multipat_offset in zip(offsets + offsets_pad,
                                           var.sink_multipat_offsets):

            sink_offset = self._delay_from_start_to_sink(offset)

            self.seq.If(set_cond)(
                multipat_offset(sink_offset)
            )

        for multipat_sizes, multipat_strides, pattern in zip(
                var.sink_multipat_sizes, var.sink_multipat_strides, patterns):
            pad = tuple([(1, 0)
                         for _ in range(self.max_pattern_length - len(pattern))])

            for (multipat_size, multipat_stride,
                 (size, stride)) in zip(multipat_sizes, multipat_strides,
                                        pattern + pad):

                sink_size = self._delay_from_start_to_sink(size)
                sink_stride = self._delay_from_start_to_sink(stride)

                self.seq.If(set_cond)(
                    multipat_size(sink_size),
                    multipat_stride(sink_stride)
                )

        port = vtypes.to_int(port)
        self._setup_sink_ram(ram, var, port, set_cond)
        self._synthesize_set_sink_multipattern(var, name)

        fsm.If(self.stream_oready).goto_next()

    def set_sink_fifo(self, fsm, name, fifo, size):
        """ intrinsic method to assign FIFO property to a sink stream """

        if not self.stream_synthesized:
            self._implement_stream()

        if isinstance(name, str):
            var = self.var_name_map[name]
        elif isinstance(name, vtypes.Str):
            name = name.value
            var = self.var_name_map[name]
        elif isinstance(name, int):
            var = self.var_id_map[name]
        elif isinstance(name, vtypes.Int):
            name = name.value
            var = self.var_id_map[name]
        else:
            raise TypeError('Unsupported index name')

        if name not in self.sinks:
            raise NameError("No such stream '%s'" % name)

        set_cond_base = self._set_flag(fsm, self.stream_oready)
        set_cond = self._delay_from_start_to_sink(set_cond_base)
        sink_size = self._delay_from_start_to_sink(size)

        self.seq.If(set_cond)(
            var.sink_mode(mode_fifo),
            var.sink_size(sink_size),
        )

        self._setup_sink_fifo(fifo, var, set_cond)
        self._synthesize_set_sink_fifo(var, name)

        fsm.If(self.stream_oready).goto_next()

    def set_sink_immediate(self, fsm, name, size):
        """ intrinsic method to set a sink stream as an immediate variable """

        if not self.stream_synthesized:
            self._implement_stream()

        if isinstance(name, str):
            var = self.var_name_map[name]
        elif isinstance(name, vtypes.Str):
            name = name.value
            var = self.var_name_map[name]
        elif isinstance(name, int):
            var = self.var_id_map[name]
        elif isinstance(name, vtypes.Int):
            name = name.value
            var = self.var_id_map[name]
        else:
            raise TypeError('Unsupported index name')

        if name not in self.sinks:
            raise NameError("No such stream '%s'" % name)

        set_cond_base = self._set_flag(fsm, self.stream_oready)
        set_cond = self._delay_from_start_to_sink(set_cond_base)
        sink_mode = mode_ram_normal
        sink_size = self._delay_from_start_to_sink(size)

        self.seq.If(set_cond)(
            var.sink_mode(sink_mode),
            var.sink_size(sink_size)
        )

        ram_sel = var.sink_sel
        self.seq.If(set_cond)(
            ram_sel(0)  # '0' is reserved for empty
        )

        self._synthesize_set_sink_immediate(var, name)

        fsm.If(self.stream_oready).goto_next()

    def set_sink_empty(self, fsm, name):
        """ intrinsic method to assign RAM property to a sink stream """

        if not self.stream_synthesized:
            self._implement_stream()

        if isinstance(name, str):
            var = self.var_name_map[name]
        elif isinstance(name, vtypes.Str):
            name = name.value
            var = self.var_name_map[name]
        elif isinstance(name, int):
            var = self.var_id_map[name]
        elif isinstance(name, vtypes.Int):
            name = name.value
            var = self.var_id_map[name]
        else:
            raise TypeError('Unsupported index name')

        if name not in self.sinks:
            raise NameError("No such stream '%s'" % name)

        set_cond_base = self._set_flag(fsm, self.stream_oready)
        set_cond = self._delay_from_start_to_sink(set_cond_base)

        ram_sel = var.sink_sel
        self.seq.If(set_cond)(
            ram_sel(0)  # '0' is reserved for empty
        )

        fsm.If(self.stream_oready).goto_next()

    def set_constant(self, fsm, name, value, raw=False):
        """ intrinsic method to assign constant value to a constant stream """

        if not self.stream_synthesized:
            self._implement_stream()

        if isinstance(name, str):
            var = self.var_name_map[name]
        elif isinstance(name, vtypes.Str):
            name = name.value
            var = self.var_name_map[name]
        elif isinstance(name, int):
            var = self.var_id_map[name]
        elif isinstance(name, vtypes.Int):
            name = name.value
            var = self.var_id_map[name]
        else:
            raise TypeError('Unsupported index name')

        if name not in self.constants:
            raise NameError("No such stream '%s'" % name)

        set_cond = self._set_flag(fsm)

        if not raw:
            value = fxd.write_adjust(value, var.point)

        self.seq.If(set_cond)(
            var.next_constant_data(value)
        )

        if not var.has_constant_data:
            var.write(var.next_constant_data, self.source_start)
            var.has_constant_data = True

        fsm.goto_next()

    def set_read_RAM(self, fsm, name, ram, port=0):
        """ intrinsic method to assign RAM property to a read-RAM interface """

        if not self.stream_synthesized:
            self._implement_stream()

        if isinstance(name, str):
            var = self.var_name_map[name]
        elif isinstance(name, vtypes.Str):
            name = name.value
            var = self.var_name_map[name]
        elif isinstance(name, int):
            var = self.var_id_map[name]
        elif isinstance(name, vtypes.Int):
            name = name.value
            var = self.var_id_map[name]
        else:
            raise TypeError('Unsupported index name')

        if name not in self.read_rams:
            raise NameError("No such stream '%s'" % name)

        set_cond = self._set_flag(fsm)

        port = vtypes.to_int(port)
        self._setup_read_ram(ram, var, port, set_cond)

        fsm.goto_next()

    def set_write_RAM(self, fsm, name, ram, port=0):
        """ intrinsic method to assign RAM property to a write-RAM interface """

        if not self.stream_synthesized:
            self._implement_stream()

        if isinstance(name, str):
            var = self.var_name_map[name]
        elif isinstance(name, vtypes.Str):
            name = name.value
            var = self.var_name_map[name]
        elif isinstance(name, int):
            var = self.var_id_map[name]
        elif isinstance(name, vtypes.Int):
            name = name.value
            var = self.var_id_map[name]
        else:
            raise TypeError('Unsupported index name')

        if name not in self.write_rams:
            raise NameError("No such stream '%s'" % name)

        set_cond = self._set_flag(fsm)

        port = vtypes.to_int(port)
        self._setup_write_ram(ram, var, port, set_cond)

        fsm.goto_next()

    def set_read_modify_write_RAM(self, fsm, name, ram, read_ports=None, write_port=None):

        if not self.stream_synthesized:
            self._implement_stream()

        if isinstance(name, str):
            var = self.var_name_map[name]
        elif isinstance(name, vtypes.Str):
            name = name.value
            var = self.var_name_map[name]
        elif isinstance(name, int):
            var = self.var_id_map[name]
        elif isinstance(name, vtypes.Int):
            name = name.value
            var = self.var_id_map[name]
        else:
            raise TypeError('Unsupported index name')

        if name not in self.read_modify_write_rams:
            raise NameError("No such stream '%s'" % name)

        read_rams, write_ram = var

        if read_ports is None:
            read_ports = [i for i, read_ram in enumerate(read_ram)]

        if write_port is None:
            write_port = read_ports[-1] + 1

        for i, (read_ram, read_port) in enumerate(zip(read_rams, read_ports)):
            read_name = read_ram
            self.set_read_RAM(fsm, read_name, ram, port=read_port)
            fsm._set_index(fsm.current - 1)

        write_name = write_ram
        self.set_write_RAM(fsm, write_name, ram, port=write_port)

    def read_sink(self, fsm, name):
        """ intrinsic method to read the last output of a sink stream """

        if not self.stream_synthesized:
            self._implement_stream()

        if isinstance(name, str):
            var = self.var_name_map[name]
        elif isinstance(name, vtypes.Str):
            name = name.value
            var = self.var_name_map[name]
        elif isinstance(name, int):
            var = self.var_id_map[name]
        elif isinstance(name, vtypes.Int):
            name = name.value
            var = self.var_id_map[name]
        else:
            raise TypeError('Unsupported index name')

        if name not in self.sinks:
            raise NameError("No such stream '%s'" % name)

        fsm.goto_next()

        return var.sink_immediate

    def run(self, fsm):
        cond = self._set_flag(fsm)

        self._run(cond)
        fsm.goto_next()

        fsm.If(self.busy).goto_next()

        return 0

    def _run(self, cond):
        add_mux(self.run_flag, cond, 1)

        if not self.fsm_synthesized:
            substreams = self._collect_substreams()
            for sub in substreams:
                if not sub.substrm.fsm_synthesized:
                    sub.substrm._synthesize_run()
                    sub.substrm.fsm_synthesized = True

            self._synthesize_run()
            self.fsm_synthesized = True

        return 0

    def _synthesize_run(self):
        # entry point
        self.fsm._set_index(0)

        # start
        self.fsm.If(self.run_flag)(
            self.source_start(1)
        )
        self.fsm.If(self.run_flag).goto_next()

        start_cond = self.source_start

        self.fsm.If(start_cond, self.stream_oready)(
            self.source_start(0),
            self.source_busy(1)
        )

        self.fsm.seq.If(self._delay_from_start_to_ivalid_on(start_cond))(
            self.stream_ivalid(1)
        )

        if self.reduce_reset is not None:
            self.fsm.seq.If(self._delay_from_start_to_reduce_reset_off(start_cond))(
                self.reduce_reset(0)
            )

        if self.dump:
            self.seq.If(self._delay_from_start_to_ivalid_on(start_cond))(
                self.dump_enable(1)
            )

        self.fsm.If(start_cond, self.stream_oready).goto_next()

        substreams = self._collect_substreams()
        for sub in substreams:
            start_stage = sub.start_stage
            reset_delay = sub.reset_delay
            dump_delay = sub.reset_delay
            cond_delay = sub.reset_delay - 1
            sub_fsm = sub.substrm.fsm
            sub_fsm._set_index(0)

            sub.substrm.fsm.seq.If(start_cond, self.stream_oready)(
                sub.substrm.source_busy(1)
            )

            sub_fsm.seq.If(self._delay_from_start_to_substream_ivalid_on(start_cond, reset_delay))(
                sub.substrm.stream_ivalid(1)
            )

            if sub.substrm.reduce_reset is not None:
                sub_fsm.seq.If(self._delay_from_start_to_substream_reduce_reset_off(start_cond, reset_delay))(
                    sub.substrm.reduce_reset(0)
                )

            if self.dump and sub.substrm.dump:
                sub_fsm.seq.If(self._delay_from_start_to_substream_ivalid_on(start_cond, dump_delay))(
                    sub.substrm.dump_enable(1)
                )

            for cond in sub.conds.values():
                sub_fsm.seq.If(self._delay_from_start_to_substream_ivalid_on(start_cond, cond_delay))(
                    cond(1)
                )

        # compute (at this cycle, source_idle <- 0)
        self.fsm.If(self.stream_oready).goto_next()

        # compute and join
        done_cond = None
        for key, source_idle in sorted(self.source_idle_map.items(),
                                       key=lambda x: x[0]):
            done_cond = make_condition(done_cond, source_idle)

        end_cond = make_condition(done_cond, self.fsm.here)

        self.fsm.seq.If(self.stream_oready)(
            self.source_stop(0)
        )
        self.fsm.If(self.stream_oready, end_cond)(
            self.source_stop(1),
            self.source_busy(0)
        )

        self.fsm.If(self.stream_oready, end_cond).goto_init()

        self.fsm.seq.If(self._delay_from_start_to_ivalid_off(end_cond))(
            self.stream_ivalid(0)
        )

        # reset accumulate pipelines
        if self.reduce_reset is not None:
            self.fsm.seq.If(self._delay_from_start_to_reduce_reset_on(end_cond))(
                self.reduce_reset(1)
            )

        if self.dump:
            dump_delay = self.ram_delay
            self.seq.If(self._delay_from_start_to_ivalid_off(end_cond))(
                self.dump_enable(0)
            )

        for sub in substreams:
            sub.substrm.fsm.seq.If(end_cond)(
                sub.substrm.source_busy(0)
            )

            reset_delay = sub.reset_delay
            dump_delay = sub.reset_delay
            cond_delay = sub.reset_delay - 1
            sub_fsm = sub.substrm.fsm
            sub_fsm._set_index(0)

            sub_fsm.seq.If(self._delay_from_start_to_substream_ivalid_off(end_cond, reset_delay))(
                sub.substrm.stream_ivalid(0)
            )

            if sub.substrm.reduce_reset is not None:
                sub_fsm.seq.If(self._delay_from_start_to_substream_reduce_reset_on(end_cond, reset_delay))(
                    sub.substrm.reduce_reset(1)
                )

            if self.dump and sub.substrm.dump:
                sub_fsm.seq.If(self._delay_from_start_to_substream_ivalid_off(end_cond, dump_delay))(
                    sub.substrm.dump_enable(0)
                )

            for cond in sub.conds.values():
                sub_fsm.seq.If(self._delay_from_start_to_substream_ivalid_off(end_cond, cond_delay))(
                    cond(0)
                )

        self.sink_start.assign(self._delay_from_start_to_sink(self.source_start))
        self.sink_stop.assign(self._delay_from_start_to_sink_stop(self.source_stop))
        self.sink_busy.assign(self._delay_from_start_to_sink_busy(self.source_busy))

        self.seq.If(vtypes.Not(self.sink_busy), self.seq.Prev(self.sink_busy, 1))(
            self.busy_buf(0)
        )
        self.seq.If(self.source_busy)(
            self.busy_buf(1)
        )

        self.busy.assign(vtypes.Ors(self.source_busy, self.sink_busy, self.busy_buf))

        return 0

    def join(self, fsm):
        fsm.If(vtypes.Not(self.busy)).goto_next()
        return 0

    def done(self, fsm):
        return vtypes.Not(self.busy)

    def source_join(self, fsm):
        fsm.If(vtypes.Not(self.source_busy)).goto_next()
        return 0

    def source_done(self, fsm):
        return vtypes.Not(self.source_busy)

    def sink_join(self, fsm):
        fsm.If(vtypes.Not(self.sink_busy)).goto_next()
        return 0

    def sink_done(self, fsm):
        return vtypes.Not(self.sink_busy)

    def source_join_and_run(self, fsm):
        cond = vtypes.Ands(fsm.here, vtypes.Not(self.source_busy))

        self._run(cond)

        fsm.If(vtypes.Not(self.source_busy)).goto_next()
        fsm.goto_next()

        return 0

    def enable_dump(self, fsm):
        if not self.dump:
            raise TypeError('dump mode is disabled.')

        self.seq.If(fsm.here)(
            self.dump_mask(0)
        )

        fsm.goto_next()
        return self.dump_mask

    def disable_dump(self, fsm):
        if not self.dump:
            raise TypeError('dump mode is disabled.')

        self.seq.If(fsm.here)(
            self.dump_mask(1)
        )

        fsm.goto_next()
        return self.dump_mask

    def _delay_from_start_to_sink(self, v):
        delay = self._write_delay()
        start_value = v
        first_renable = self.seq.Prev(start_value, 1, cond=self.stream_oready)
        first_rvalid = self.seq.Prev(first_renable, 1, cond=self.stream_oready)
        sink_value = self.seq.Prev(first_rvalid, delay, cond=self.stream_oready)
        return sink_value

    def _delay_from_start_to_sink_busy(self, v):
        delay = self._write_delay()
        start_value = v
        first_renable = self.seq.Prev(start_value, 1, cond=self.stream_oready)
        first_rvalid = self.seq.Prev(first_renable, 1, cond=self.stream_oready)
        sink_value = self.seq.Prev(first_rvalid, delay, cond=self.stream_oready)
        return sink_value

    def _delay_from_start_to_sink_stop(self, v):
        delay = self._write_delay()
        start_value = v
        first_renable = start_value
        first_rvalid = first_renable
        sink_value = self.seq.Prev(first_rvalid, delay, cond=self.stream_oready)
        return sink_value

    def _delay_from_start_to_ivalid_on(self, v):
        start_value = self.seq.Prev(v, 1, cond=self.stream_oready)
        first_renable = self.seq.Prev(start_value, 1, cond=self.stream_oready)
        first_rvalid = self.seq.Prev(first_renable, 1, cond=self.stream_oready)
        source_value = vtypes.Ands(first_rvalid, self.stream_oready)
        return source_value

    def _delay_from_start_to_reduce_reset_off(self, v):
        initial_reset = self.seq.Prev(v, 1, cond=self.stream_oready)
        start_value = self.seq.Prev(initial_reset, 1, cond=self.stream_oready)
        first_renable = self.seq.Prev(start_value, 1, cond=self.stream_oready)
        first_rvalid = self.seq.Prev(first_renable, 1, cond=self.stream_oready)
        source_value = vtypes.Ands(first_rvalid, self.stream_oready)
        return source_value

    def _delay_from_start_to_ivalid_off(self, v):
        start_value = self.seq.Prev(v, 1, cond=self.stream_oready)
        source_value = vtypes.Ands(start_value, self.stream_oready)
        return source_value

    def _delay_from_start_to_reduce_reset_on(self, v):
        start_value = self.seq.Prev(v, 1, cond=self.stream_oready)
        source_value = vtypes.Ands(start_value, self.stream_oready)
        return source_value

    def _delay_from_start_to_substream_ivalid_on(self, v, delay):
        start_value = self.seq.Prev(v, 1, cond=self.stream_oready)
        first_renable = self.seq.Prev(start_value, 1, cond=self.stream_oready)
        first_rvalid = self.seq.Prev(first_renable, 1, cond=self.stream_oready)
        if delay > 0:
            delayed_value = self.seq.Prev(first_rvalid, delay, cond=self.stream_oready)
            substream_value = vtypes.Ands(delayed_value, self.stream_oready)
        else:
            substream_value = vtypes.Ands(first_rvalid, self.stream_oready)
        return substream_value

    def _delay_from_start_to_substream_reduce_reset_off(self, v, delay):
        initial_reset = self.seq.Prev(v, 1, cond=self.stream_oready)
        start_value = self.seq.Prev(initial_reset, 1, cond=self.stream_oready)
        first_renable = self.seq.Prev(start_value, 1, cond=self.stream_oready)
        first_rvalid = self.seq.Prev(first_renable, 1, cond=self.stream_oready)
        if delay > 0:
            delayed_value = self.seq.Prev(first_rvalid, delay, cond=self.stream_oready)
            substream_value = vtypes.Ands(delayed_value, self.stream_oready)
        else:
            substream_value = vtypes.Ands(first_rvalid, self.stream_oready)
        return substream_value

    def _delay_from_start_to_substream_ivalid_off(self, v, delay):
        start_value = self.seq.Prev(v, 1, cond=self.stream_oready)
        if delay > 0:
            delayed_value = self.seq.Prev(start_value, delay, cond=self.stream_oready)
            substream_value = vtypes.Ands(delayed_value, self.stream_oready)
        else:
            substream_value = vtypes.Ands(start_value, self.stream_oready)
        return substream_value

    def _delay_from_start_to_substream_reduce_reset_on(self, v, delay):
        start_value = self.seq.Prev(v, 1, cond=self.stream_oready)
        if delay > 0:
            delayed_value = self.seq.Prev(start_value, delay, cond=self.stream_oready)
            substream_value = vtypes.Ands(delayed_value, self.stream_oready)
        else:
            substream_value = vtypes.Ands(start_value, self.stream_oready)
        return substream_value

    def _setup_source_ram(self, ram, var, port, set_cond):
        if ram._id() in var.source_id_map:
            ram_id = var.source_id_map[ram._id()]
            self.seq.If(set_cond)(
                var.source_sel(ram_id)
            )
            return

        if ram._id() not in self.buf_id_map:
            ram_id = self.buf_id_count
            self.buf_id_count += 1
            self.buf_id_map[ram._id()] = ram_id
        else:
            ram_id = self.buf_id_map[ram._id()]

        var.source_id_map[ram._id()] = ram_id

        self.seq.If(set_cond)(
            var.source_sel(ram_id)
        )

        ram_cond = (var.source_sel == ram_id)
        renable = vtypes.Ands(self.stream_oready, var.source_ram_renable, ram_cond)

        d, v = ram.read_rtl(var.source_ram_raddr, port=port, cond=renable)

        d_out = d
        add_mux(var.source_ram_rdata, ram_cond, d_out)

        if (self.dump and
            (self.dump_mode == 'all' or
             self.dump_mode == 'ram' or
             (self.dump_mode == 'selective' and
                 hasattr(ram, 'dump') and ram.dump))):
            self._setup_source_ram_dump(ram, var, renable, d)

    def _setup_source_ram_dump(self, ram, var, read_enable, read_data):
        pipeline_depth = self.pipeline_depth()
        log_pipeline_depth = max(
            int(math.ceil(math.log(max(pipeline_depth, 10), 10))), 1)

        addr_base = (ram.dump_addr_base if hasattr(ram, 'dump_addr_base') else
                     self.dump_base)
        addr_base_char = ('b' if addr_base == 2 else
                          'o' if addr_base == 8 else
                          'd' if addr_base == 10 else
                          'x')
        addr_prefix = ('0b' if addr_base == 2 else
                       '0o' if addr_base == 8 else
                       '  ' if addr_base == 10 else
                       '0x')
        addr_vfmt = ''.join([addr_prefix, '%', addr_base_char])

        data_base = (ram.dump_data_base if hasattr(ram, 'dump_data_base') else
                     self.dump_base)
        data_base_char = ('b' if data_base == 2 else
                          'o' if data_base == 8 else
                          'd' if (data_base == 10 and
                                  (not hasattr(ram, 'point') or ram.point <= 0)) else
                          # 'f' if (data_base == 10 and
                          #        hasattr(ram, 'point') and ram.point > 0) else
                          'g' if (data_base == 10 and
                                  hasattr(ram, 'point') and ram.point > 0) else
                          'x')
        data_prefix = ('0b' if data_base == 2 else
                       '0o' if data_base == 8 else
                       '  ' if data_base == 10 else
                       '0x')
        # if data_base_char == 'f':
        #    point_len = int(math.ceil(ram.point / math.log(10, 2)))
        #    point_len = max(point_len, 8)
        #    total_len = int(math.ceil(ram.datawidth / math.log(10, 2)))
        #    total_len = max(total_len, point_len)
        #    data_vfmt = ''.join([data_prefix, '%',
        #                         '%d.%d' % (total_len + 1, point_len),
        #                         data_base_char])
        # else:
        #    data_vfmt = ''.join([data_prefix, '%', data_base_char])
        data_vfmt = ''.join([data_prefix, '%', data_base_char])

        name = ram.name
        fmt = ''.join(['(', self.name, ' step:%d, ',
                       'read, ', ' ' * (log_pipeline_depth + 2),
                       'age:%d) ', name,
                       '[', addr_vfmt, '] = ', data_vfmt])

        dump_ram_step_name = ('_stream_dump_ram_step_%d_%s' %
                              (self.object_id, name))
        dump_ram_step = self.module.Reg(dump_ram_step_name, 32, initval=0)

        enable = self.seq.Prev(read_enable, 2, cond=self.stream_oready)
        age = dump_ram_step
        addr = self.seq.Prev(var.source_ram_raddr, 2, cond=self.stream_oready)
        if hasattr(ram, 'point') and ram.point > 0:
            data = vtypes.Div(vtypes.SystemTask('itor', read_data),
                              1.0 * (2 ** ram.point))
        elif hasattr(ram, 'point') and ram.point < 0:
            data = vtypes.Times(read_data, 2 ** -ram.point)
        else:
            data = read_data

        self.seq(
            dump_ram_step(0)
        )
        self.seq.If(enable)(
            dump_ram_step.inc()
        )
        self.seq.If(self.dump_enable)(
            dump_ram_step.inc()
        )

        self.seq.If(enable, vtypes.Not(self.dump_mask))(
            vtypes.Display(fmt, dump_ram_step, age, addr, data)
        )

    def _synthesize_set_source(self, var, name):
        if var.source_fsm is not None:
            return

        source_start = vtypes.Ands(self.source_start,
                                   vtypes.And(var.source_mode, mode_ram_normal))

        self.seq.If(source_start, self.stream_oready)(
            # var.source_idle(0),
            var.source_offset_buf(var.source_offset),
            var.source_size_buf(var.source_size),
            var.source_stride_buf(var.source_stride)
        )

        wdata = var.source_ram_rdata
        wenable = vtypes.Ands(self.stream_oready, self.source_busy, self.is_root)
        var.write(wdata, wenable)

        fsm_id = self.fsm_id_count
        self.fsm_id_count += 1

        prefix = self._prefix(name)

        fsm_name = '_%s_source_fsm_%d' % (prefix, fsm_id)
        var.source_fsm = FSM(self.module, fsm_name, self.clock, self.reset,
                             as_module=self.fsm_as_module)

        var.source_fsm.If(source_start, self.stream_oready).goto_next()

        self.seq.If(var.source_fsm.here, self.stream_oready)(
            var.source_idle(0),
            var.source_ram_raddr(var.source_offset_buf),
            var.source_ram_renable(1),
            var.source_count(var.source_size_buf)
        )

        var.source_fsm.If(self.stream_oready).goto_next()

        self.seq.If(var.source_fsm.here, self.stream_oready)(
            var.source_ram_raddr.add(var.source_stride_buf),
            var.source_ram_renable(1),
            var.source_count.dec()
        )
        self.seq.If(var.source_fsm.here, var.source_count == 1, self.stream_oready)(
            var.source_ram_renable(0),
            var.source_idle(1)
        )

        var.source_fsm.If(var.source_count == 1, self.stream_oready).goto_init()

    def _make_source_pattern_vars(self, var, name):
        if var.source_pat_cur_offsets is not None:
            return

        prefix = self._prefix(name)

        var.source_pat_cur_offsets = [
            self.module.Reg('_source_%s_pat_cur_offset_%d' % (prefix, i),
                            self.addrwidth, initval=0)
            for i in range(self.max_pattern_length)]
        var.source_pat_sizes = [self.module.Reg('_source_%s_pat_size_%d' % (prefix, i),
                                                self.addrwidth + 1, initval=0)
                                for i in range(self.max_pattern_length)]
        var.source_pat_strides = [self.module.Reg('_source_%s_pat_stride_%d' % (prefix, i),
                                                  self.addrwidth, initval=0)
                                  for i in range(self.max_pattern_length)]
        var.source_pat_counts = [self.module.Reg('_source_%s_pat_count_%d' % (prefix, i),
                                                 self.addrwidth + 1, initval=0)
                                 for i in range(self.max_pattern_length)]

        var.source_pat_size_bufs = [self.module.Reg('_source_%s_pat_size_buf_%d' % (prefix, i),
                                                    self.addrwidth + 1, initval=0)
                                    for i in range(self.max_pattern_length)]
        var.source_pat_stride_bufs = [self.module.Reg('_source_%s_pat_stride_buf_%d' % (prefix, i),
                                                      self.addrwidth, initval=0)
                                      for i in range(self.max_pattern_length)]

    def _synthesize_set_source_pattern(self, var, name):
        if var.source_pat_fsm is not None:
            return

        source_start = vtypes.Ands(self.source_start,
                                   vtypes.And(var.source_mode, mode_ram_pattern))

        self.seq.If(source_start, self.stream_oready)(
            # var.source_idle(0),
            var.source_offset_buf(var.source_offset)
        )

        for source_pat_cur_offset in var.source_pat_cur_offsets:
            self.seq.If(source_start, self.stream_oready)(
                source_pat_cur_offset(0)
            )

        for (source_pat_size, source_pat_count) in zip(
                var.source_pat_sizes, var.source_pat_counts):
            self.seq.If(source_start, self.stream_oready)(
                source_pat_count(source_pat_size - 1)
            )

        for (source_pat_size_buf, source_pat_size) in zip(
                var.source_pat_size_bufs, var.source_pat_sizes):
            self.seq.If(source_start, self.stream_oready)(
                source_pat_size_buf(source_pat_size)
            )

        for (source_pat_stride_buf, source_pat_stride) in zip(
                var.source_pat_stride_bufs, var.source_pat_strides):
            self.seq.If(source_start, self.stream_oready)(
                source_pat_stride_buf(source_pat_stride)
            )

        wdata = var.source_ram_rdata
        wenable = vtypes.Ands(self.stream_oready, self.source_busy, self.is_root)
        var.write(wdata, wenable)

        fsm_id = self.fsm_id_count
        self.fsm_id_count += 1

        prefix = self._prefix(name)

        fsm_name = '_%s_source_pat_fsm_%d' % (prefix, fsm_id)
        var.source_pat_fsm = FSM(self.module, fsm_name,
                                 self.clock, self.reset,
                                 as_module=self.fsm_as_module)

        var.source_pat_fsm.If(source_start, self.stream_oready).goto_next()

        source_all_offset = self.module.Wire('_%s_source_pat_all_offset' % prefix,
                                             self.addrwidth)
        source_all_offset_val = var.source_offset_buf
        for source_pat_cur_offset in var.source_pat_cur_offsets:
            source_all_offset_val += source_pat_cur_offset
        source_all_offset.assign(source_all_offset_val)

        self.seq.If(var.source_pat_fsm.here, self.stream_oready)(
            var.source_idle(0),
            var.source_ram_raddr(source_all_offset),
            var.source_ram_renable(1)
        )

        upcond = None

        for (source_pat_cur_offset, source_pat_size_buf,
             source_pat_stride_buf, source_pat_count) in zip(
                 var.source_pat_cur_offsets, var.source_pat_size_bufs,
                 var.source_pat_stride_bufs, var.source_pat_counts):

            self.seq.If(var.source_pat_fsm.here, upcond, self.stream_oready)(
                source_pat_cur_offset.add(source_pat_stride_buf),
                source_pat_count.dec()
            )

            reset_cond = source_pat_count == 0
            self.seq.If(var.source_pat_fsm.here, upcond, reset_cond, self.stream_oready)(
                source_pat_cur_offset(0),
                source_pat_count(source_pat_size_buf - 1)
            )
            upcond = make_condition(upcond, reset_cond)

        fin_cond = upcond

        var.source_pat_fsm.If(fin_cond, self.stream_oready).goto_next()

        self.seq.If(var.source_pat_fsm.here, self.stream_oready)(
            var.source_ram_renable(0)
        )

        self.seq.If(var.source_pat_fsm.here, self.stream_oready)(
            var.source_idle(1)
        )

        var.source_pat_fsm.If(self.stream_oready).goto_init()

    def _make_source_multipattern_vars(self, var, name):
        if var.source_multipat_cur_offsets is not None:
            return

        prefix = self._prefix(name)

        var.source_multipat_num_patterns = self.module.Reg(
            '_source_%s_multipat_num_patterns' % prefix,
            int(math.ceil(math.log(max(self.max_multipattern_length, 2), 2))), initval=0)
        var.source_multipat_offsets = [
            self.module.Reg('_source_%s_multipat_%d_offset' % (prefix, j),
                            self.addrwidth, initval=0)
            for j in range(self.max_multipattern_length)]
        var.source_multipat_cur_offsets = [
            self.module.Reg('_source_%s_multipat_%d_cur_offset' % (prefix, i),
                            self.addrwidth, initval=0)
            for i in range(self.max_pattern_length)]
        var.source_multipat_sizes = [[self.module.Reg('_source_%s_multipat_%d_size_%d' %
                                                      (prefix, j, i),
                                                      self.addrwidth + 1, initval=0)
                                      for i in range(self.max_pattern_length)]
                                     for j in range(self.max_multipattern_length)]
        var.source_multipat_strides = [[self.module.Reg('_source_%s_multipat_%d_stride_%d' %
                                                        (prefix, j, i),
                                                        self.addrwidth, initval=0)
                                        for i in range(self.max_pattern_length)]
                                       for j in range(self.max_multipattern_length)]
        var.source_multipat_counts = [[self.module.Reg('_source_%s_multipat_%d_count_%d' %
                                                       (prefix, j, i),
                                                       self.addrwidth + 1, initval=0)
                                       for i in range(self.max_pattern_length)]
                                      for j in range(self.max_multipattern_length)]

        var.source_multipat_offset_bufs = [
            self.module.Reg('_source_%s_multipat_%d_offset_buf' % (prefix, j),
                            self.addrwidth, initval=0)
            for j in range(self.max_multipattern_length)]
        var.source_multipat_size_bufs = [[self.module.Reg('_source_%s_multipat_%d_size_buf_%d' %
                                                          (prefix, j, i),
                                                          self.addrwidth, initval=0)
                                          for i in range(self.max_pattern_length)]
                                         for j in range(self.max_multipattern_length)]
        var.source_multipat_stride_bufs = [[self.module.Reg('_source_%s_multipat_%d_stride_buf_%d' %
                                                            (prefix, j, i),
                                                            self.addrwidth, initval=0)
                                            for i in range(self.max_pattern_length)]
                                           for j in range(self.max_multipattern_length)]

    def _synthesize_set_source_multipattern(self, var, name):
        if var.source_pat_fsm is not None:
            return

        source_start = vtypes.Ands(self.source_start,
                                   vtypes.And(var.source_mode, mode_ram_multipattern))

        # self.seq.If(source_start, self.stream_oready)(
        #     # var.source_idle(0)
        # )

        for source_multipat_cur_offset in var.source_multipat_cur_offsets:
            self.seq.If(source_start, self.stream_oready)(
                source_multipat_cur_offset(0)
            )

        self.seq.If(source_start, self.stream_oready)(
            var.source_multipat_num_patterns.dec()
        )

        for (source_multipat_size, source_multipat_count) in zip(
                var.source_multipat_sizes[0], var.source_multipat_counts[0]):
            self.seq.If(source_start, self.stream_oready)(
                source_multipat_count(source_multipat_size - 1)
            )

        for (source_multipat_offset_buf,
             source_multipat_offset) in zip(var.source_multipat_offset_bufs,
                                            var.source_multipat_offsets):
            self.seq.If(source_start, self.stream_oready)(
                source_multipat_offset_buf(source_multipat_offset)
            )

        for (source_multipat_size_buf_line,
             source_multipat_size_line) in zip(var.source_multipat_size_bufs,
                                               var.source_multipat_sizes):
            for (source_multipat_size_buf,
                 source_multipat_size) in zip(source_multipat_size_buf_line,
                                              source_multipat_size_line):
                self.seq.If(source_start, self.stream_oready)(
                    source_multipat_size_buf(source_multipat_size)
                )

        for (source_multipat_stride_buf_line,
             source_multipat_stride_line) in zip(var.source_multipat_stride_bufs,
                                                 var.source_multipat_strides):
            for (source_multipat_stride_buf,
                 source_multipat_stride) in zip(source_multipat_stride_buf_line,
                                                source_multipat_stride_line):
                self.seq.If(source_start, self.stream_oready)(
                    source_multipat_stride_buf(source_multipat_stride)
                )

        wdata = var.source_ram_rdata
        wenable = vtypes.Ands(self.stream_oready, self.source_busy, self.is_root)
        var.write(wdata, wenable)

        fsm_id = self.fsm_id_count
        self.fsm_id_count += 1

        prefix = self._prefix(name)

        fsm_name = '_%s_source_multipat_fsm_%d' % (prefix, fsm_id)
        var.source_multipat_fsm = FSM(self.module, fsm_name,
                                      self.clock, self.reset,
                                      as_module=self.fsm_as_module)

        var.source_multipat_fsm.If(source_start, self.stream_oready).goto_next()

        source_all_offset = self.module.Wire('_%s_source_multipat_all_offset' % prefix,
                                             self.addrwidth)
        source_all_offset_val = var.source_multipat_offset_bufs[0]
        for source_multipat_cur_offset in var.source_multipat_cur_offsets:
            source_all_offset_val += source_multipat_cur_offset
        source_all_offset.assign(source_all_offset_val)

        self.seq.If(var.source_multipat_fsm.here, self.stream_oready)(
            var.source_idle(0),
            var.source_ram_raddr(source_all_offset),
            var.source_ram_renable(1)
        )

        upcond = None

        for (source_multipat_cur_offset, source_multipat_size_buf,
             source_multipat_stride_buf, source_multipat_count) in zip(
                 var.source_multipat_cur_offsets, var.source_multipat_size_bufs[0],
                 var.source_multipat_stride_bufs[0], var.source_multipat_counts[0]):

            self.seq.If(var.source_multipat_fsm.here, upcond, self.stream_oready)(
                source_multipat_cur_offset.add(source_multipat_stride_buf),
                source_multipat_count.dec()
            )

            reset_cond = source_multipat_count == 0
            self.seq.If(var.source_multipat_fsm.here, upcond, reset_cond, self.stream_oready)(
                source_multipat_cur_offset(0),
                source_multipat_count(source_multipat_size_buf - 1)
            )
            upcond = make_condition(upcond, reset_cond)

        fin_cond = upcond

        prev_offset = var.source_multipat_offset_bufs[0]
        for multipat_offset_buf in var.source_multipat_offset_bufs[1:]:
            self.seq.If(fin_cond, var.source_multipat_fsm.here, self.stream_oready)(
                prev_offset(multipat_offset_buf)
            )
            prev_offset = multipat_offset_buf

        prev_sizes = var.source_multipat_size_bufs[0]
        for multipat_sizes in var.source_multipat_size_bufs[1:]:
            for prev_size, size in zip(prev_sizes, multipat_sizes):
                self.seq.If(fin_cond, var.source_multipat_fsm.here, self.stream_oready)(
                    prev_size(size)
                )
            prev_sizes = multipat_sizes

        prev_strides = var.source_multipat_stride_bufs[0]
        for multipat_strides in var.source_multipat_stride_bufs[1:]:
            for prev_stride, stride in zip(prev_strides, multipat_strides):
                self.seq.If(fin_cond, var.source_multipat_fsm.here, self.stream_oready)(
                    prev_stride(stride)
                )
            prev_strides = multipat_strides

        self.seq.If(fin_cond, var.source_multipat_fsm.here, self.stream_oready)(
            var.source_multipat_num_patterns.dec()
        )

        var.source_multipat_fsm.If(fin_cond,
                                   var.source_multipat_num_patterns == 0,
                                   self.stream_oready).goto_next()

        self.seq.If(var.source_multipat_fsm.here, self.stream_oready)(
            var.source_ram_renable(0)
        )

        self.seq.If(var.source_multipat_fsm.here, self.stream_oready)(
            var.source_idle(1)
        )

        var.source_multipat_fsm.If(self.stream_oready).goto_init()

    def _setup_source_fifo(self, fifo, var, set_cond):
        if fifo._id() in var.source_id_map:
            fifo_id = var.source_id_map[fifo._id()]
            self.seq.If(set_cond)(
                var.source_sel(fifo_id)
            )
            return

        if fifo._id() not in self.buf_id_map:
            fifo_id = self.buf_id_count
            self.buf_id_count += 1
            self.buf_id_map[fifo._id()] = fifo_id
        else:
            fifo_id = self.buf_id_map[fifo._id()]

        var.source_id_map[fifo._id()] = fifo_id

        self.seq.If(set_cond)(
            var.source_sel(fifo_id)
        )

        fifo_cond = (var.source_sel == fifo_id)
        deq = vtypes.Ands(self.stream_oready, var.source_fifo_deq, fifo_cond)

        d, v, ready = fifo.deq_rtl(cond=deq)

        d_out = d
        add_mux(var.source_fifo_rdata, fifo_cond, d_out)

        # stall control
        cond = vtypes.Ands(self.source_busy, fifo_cond)
        fifo_oready = vtypes.Ors(ready, var.source_idle)
        add_cond(self.stream_oready, cond, fifo_oready)

        if (self.dump and
            (self.dump_mode == 'all' or
             self.dump_mode == 'fifo' or
             (self.dump_mode == 'selective' and
                 hasattr(fifo, 'dump') and fifo.dump))):
            # self._setup_source_fifo_dump(fifo, var, deq, d)
            raise NotImplementedError()

    def _synthesize_set_source_fifo(self, var, name):
        if var.source_fsm is not None:
            return

        source_start = vtypes.Ands(self.source_start,
                                   vtypes.And(var.source_mode, mode_fifo))

        self.seq.If(source_start, self.stream_oready)(
            var.source_idle(0),
            var.source_size_buf(var.source_size),
        )

        wdata = var.source_fifo_rdata
        wenable = vtypes.Ands(self.stream_oready, self.source_busy, self.is_root)
        var.write(wdata, wenable)

        fsm_id = self.fsm_id_count
        self.fsm_id_count += 1

        prefix = self._prefix(name)

        fsm_name = '_%s_source_fsm_%d' % (prefix, fsm_id)
        var.source_fsm = FSM(self.module, fsm_name, self.clock, self.reset,
                             as_module=self.fsm_as_module)

        var.source_fsm.If(source_start, self.stream_oready).goto_next()

        self.seq.If(var.source_fsm.here, self.stream_oready)(
            var.source_fifo_deq(1),
            var.source_count(var.source_size_buf)
        )

        var.source_fsm.If(self.stream_oready).goto_next()

        self.seq.If(var.source_fsm.here, self.stream_oready)(
            var.source_fifo_deq(1),
            var.source_count.dec()
        )
        self.seq.If(var.source_fsm.here, var.source_count == 1, self.stream_oready)(
            var.source_fifo_deq(0),
            var.source_idle(1)
        )

        var.source_fsm.If(var.source_count == 1, self.stream_oready).goto_init()

    def _setup_sink_ram(self, ram, var, port, set_cond):
        if ram._id() in var.sink_id_map:
            ram_id = var.sink_id_map[ram._id()]
            self.seq.If(set_cond)(
                var.sink_sel(ram_id)
            )
            return

        if ram._id() not in self.buf_id_map:
            ram_id = self.buf_id_count
            self.buf_id_count += 1
            self.buf_id_map[ram._id()] = ram_id
        else:
            ram_id = self.buf_id_map[ram._id()]

        var.sink_id_map[ram._id()] = ram_id

        self.seq.If(set_cond)(
            var.sink_sel(ram_id)
        )

        ram_cond = (var.sink_sel == ram_id)
        wenable = vtypes.Ands(self.stream_oready, var.sink_ram_wenable, ram_cond)
        ram.write_rtl(var.sink_ram_waddr, var.sink_ram_wdata,
                      port=port, cond=wenable)

        if (self.dump and
            (self.dump_mode == 'all' or
             self.dump_mode == 'ram' or
             (self.dump_mode == 'selective' and
                 hasattr(ram, 'dump') and ram.dump))):
            self._setup_sink_ram_dump(ram, var, wenable)

    def _setup_sink_ram_dump(self, ram, var, write_enable):
        pipeline_depth = self.pipeline_depth()
        log_pipeline_depth = max(
            int(math.ceil(math.log(max(pipeline_depth, 10), 10))), 1)

        addr_base = (ram.dump_addr_base if hasattr(ram, 'dump_addr_base') else
                     self.dump_base)
        addr_base_char = ('b' if addr_base == 2 else
                          'o' if addr_base == 8 else
                          'd' if addr_base == 10 else
                          'x')
        addr_prefix = ('0b' if addr_base == 2 else
                       '0o' if addr_base == 8 else
                       '  ' if addr_base == 10 else
                       '0x')
        addr_vfmt = ''.join([addr_prefix, '%', addr_base_char])

        data_base = (ram.dump_data_base if hasattr(ram, 'dump_data_base') else
                     self.dump_base)
        data_base_char = ('b' if data_base == 2 else
                          'o' if data_base == 8 else
                          'd' if (data_base == 10 and
                                  (not hasattr(ram, 'point') or ram.point <= 0)) else
                          # 'f' if (data_base == 10 and
                          #        hasattr(ram, 'point') and ram.point > 0) else
                          'g' if (data_base == 10 and
                                  hasattr(ram, 'point') and ram.point > 0) else
                          'x')
        data_prefix = ('0b' if data_base == 2 else
                       '0o' if data_base == 8 else
                       '  ' if data_base == 10 else
                       '0x')
        # if data_base_char == 'f':
        #    point_len = int(math.ceil(ram.point / math.log(10, 2)))
        #    point_len = max(point_len, 8)
        #    total_len = int(math.ceil(ram.datawidth / math.log(10, 2)))
        #    total_len = max(total_len, point_len)
        #    data_vfmt = ''.join([data_prefix, '%',
        #                         '%d.%d' % (total_len + 1, point_len),
        #                         data_base_char])
        # else:
        #    data_vfmt = ''.join([data_prefix, '%', data_base_char])
        data_vfmt = ''.join([data_prefix, '%', data_base_char])

        name = ram.name
        fmt = ''.join(['(', self.name, ' step:%d, ',
                       'write, ', ' ' * (log_pipeline_depth + 1),
                       'age:%d) ', name,
                       '[', addr_vfmt, '] = ', data_vfmt])

        enable = var.sink_ram_wenable
        age = self.seq.Prev(self.dump_step, pipeline_depth + 1, cond=self.stream_oready) - 1
        addr = var.sink_ram_waddr
        if hasattr(ram, 'point') and ram.point > 0:
            data = vtypes.Div(vtypes.SystemTask('itor', var.sink_ram_wdata),
                              1.0 * (2 ** ram.point))
        elif hasattr(ram, 'point') and ram.point < 0:
            data = vtypes.Times(var.sink_ram_wdata, 2 ** -ram.point)
        else:
            data = var.sink_ram_wdata

        self.seq.If(enable, vtypes.Not(self.dump_mask))(
            vtypes.Display(fmt, self.dump_step, age, addr, data)
        )

    def _synthesize_set_sink(self, var, name):
        if var.sink_fsm is not None:
            return

        sink_start = vtypes.Ands(self.sink_start,
                                 vtypes.And(var.sink_mode, mode_ram_normal))

        self.seq.If(sink_start, self.stream_oready)(
            var.sink_offset_buf(var.sink_offset),
            var.sink_size_buf(var.sink_size),
            var.sink_stride_buf(var.sink_stride)
        )

        fsm_id = self.fsm_id_count
        self.fsm_id_count += 1

        prefix = self._prefix(name)

        fsm_name = '_%s_sink_fsm_%d' % (prefix, fsm_id)
        var.sink_fsm = FSM(self.module, fsm_name, self.clock, self.reset,
                           as_module=self.fsm_as_module)

        var.sink_fsm.If(sink_start, self.stream_oready).goto_next()

        self.seq.If(var.sink_fsm.here, self.stream_oready)(
            var.sink_ram_waddr(var.sink_offset_buf - var.sink_stride_buf),
            var.sink_count(var.sink_size_buf),
        )
        var.sink_fsm.If(self.stream_oready).goto_next()

        if name in self.sink_when_map:
            when = self.sink_when_map[name]
            wcond = when.read()
        else:
            wcond = None

        rdata = var.read()

        self.seq.If(var.sink_fsm.here, wcond, self.stream_oready)(
            var.sink_ram_waddr.add(var.sink_stride_buf),
            var.sink_ram_wdata(rdata),
            var.sink_ram_wenable(1),
            var.sink_count.dec()
        )

        var.sink_fsm.If(wcond, var.sink_count == 1, self.stream_oready).goto_init()
        var.sink_fsm.If(self.sink_stop, self.stream_oready).goto_init()

    def _make_sink_pattern_vars(self, var, name):
        if var.sink_pat_cur_offsets is not None:
            return

        prefix = self._prefix(name)

        var.sink_pat_cur_offsets = [self.module.Reg('_sink_%s_pat_cur_offset_%d' % (prefix, i),
                                                    self.addrwidth, initval=0)
                                    for i in range(self.max_pattern_length)]
        var.sink_pat_sizes = [self.module.Reg('_sink_%s_pat_size_%d' % (prefix, i),
                                              self.addrwidth + 1, initval=0)
                              for i in range(self.max_pattern_length)]
        var.sink_pat_strides = [self.module.Reg('_sink_%s_pat_stride_%d' % (prefix, i),
                                                self.addrwidth, initval=0)
                                for i in range(self.max_pattern_length)]
        var.sink_pat_counts = [self.module.Reg('_sink_%s_pat_count_%d' % (prefix, i),
                                               self.addrwidth + 1, initval=0)
                               for i in range(self.max_pattern_length)]

        var.sink_pat_size_bufs = [self.module.Reg('_sink_%s_pat_size_buf_%d' % (prefix, i),
                                                  self.addrwidth + 1, initval=0)
                                  for i in range(self.max_pattern_length)]
        var.sink_pat_stride_bufs = [self.module.Reg('_sink_%s_pat_stride_buf_%d' % (prefix, i),
                                                    self.addrwidth, initval=0)
                                    for i in range(self.max_pattern_length)]

    def _synthesize_set_sink_pattern(self, var, name):
        if var.sink_pat_fsm is not None:
            return

        sink_start = vtypes.Ands(self.sink_start,
                                 vtypes.And(var.sink_mode, mode_ram_pattern))

        self.seq.If(sink_start, self.stream_oready)(
            var.sink_offset_buf(var.sink_offset)
        )

        for (sink_pat_size_buf, sink_pat_size) in zip(
                var.sink_pat_size_bufs, var.sink_pat_sizes):
            self.seq.If(sink_start, self.stream_oready)(
                sink_pat_size_buf(sink_pat_size)
            )

        for (sink_pat_stride_buf, sink_pat_stride) in zip(
                var.sink_pat_stride_bufs, var.sink_pat_strides):
            self.seq.If(sink_start, self.stream_oready)(
                sink_pat_stride_buf(sink_pat_stride)
            )

        fsm_id = self.fsm_id_count
        self.fsm_id_count += 1

        prefix = self._prefix(name)

        fsm_name = '_%s_sink_pat_fsm_%d' % (prefix, fsm_id)
        var.sink_pat_fsm = FSM(self.module, fsm_name,
                               self.clock, self.reset,
                               as_module=self.fsm_as_module)

        var.sink_pat_fsm.If(sink_start, self.stream_oready).goto_next()

        for sink_pat_cur_offset in var.sink_pat_cur_offsets:
            self.seq.If(var.sink_pat_fsm.here, self.stream_oready)(
                sink_pat_cur_offset(0)
            )

        for (sink_pat_size_buf, sink_pat_count) in zip(
                var.sink_pat_size_bufs, var.sink_pat_counts):
            self.seq.If(var.sink_pat_fsm.here, self.stream_oready)(
                sink_pat_count(sink_pat_size_buf - 1)
            )

        var.sink_pat_fsm.If(self.stream_oready).goto_next()

        if name in self.sink_when_map:
            when = self.sink_when_map[name]
            wcond = when.read()
        else:
            wcond = None

        rdata = var.read()

        sink_all_offset = self.module.Wire('_%s_sink_pat_all_offset' % prefix,
                                           self.addrwidth)
        sink_all_offset_val = var.sink_offset_buf
        for sink_pat_cur_offset in var.sink_pat_cur_offsets:
            sink_all_offset_val += sink_pat_cur_offset
        sink_all_offset.assign(sink_all_offset_val)

        self.seq.If(var.sink_pat_fsm.here, wcond, self.stream_oready)(
            var.sink_ram_waddr(sink_all_offset),
            var.sink_ram_wdata(rdata),
            var.sink_ram_wenable(1)
        )

        upcond = None

        for (sink_pat_cur_offset, sink_pat_size_buf,
             sink_pat_stride_buf, sink_pat_count) in zip(
                 var.sink_pat_cur_offsets, var.sink_pat_size_bufs,
                 var.sink_pat_stride_bufs, var.sink_pat_counts):

            self.seq.If(var.sink_pat_fsm.here, wcond, upcond, self.stream_oready)(
                sink_pat_cur_offset.add(sink_pat_stride_buf),
                sink_pat_count.dec()
            )

            reset_cond = sink_pat_count == 0
            self.seq.If(var.sink_pat_fsm.here, wcond, upcond, reset_cond, self.stream_oready)(
                sink_pat_cur_offset(0),
                sink_pat_count(sink_pat_size_buf - 1)
            )
            upcond = make_condition(upcond, reset_cond)

        fin_cond = upcond

        var.sink_pat_fsm.If(wcond, fin_cond, self.stream_oready).goto_init()
        var.sink_pat_fsm.If(self.sink_stop, self.stream_oready).goto_init()

    def _make_sink_multipattern_vars(self, var, name):
        if var.sink_multipat_cur_offsets is not None:
            return

        prefix = self._prefix(name)

        var.sink_multipat_num_patterns = self.module.Reg(
            '_sink_%s_multipat_num_patterns' % prefix,
            int(math.ceil(math.log(max(self.max_multipattern_length, 2), 2))), initval=0)
        var.sink_multipat_offsets = [
            self.module.Reg('_sink_%s_multipat_%d_offset' % (prefix, j),
                            self.addrwidth, initval=0)
            for j in range(self.max_multipattern_length)]
        var.sink_multipat_cur_offsets = [
            self.module.Reg('_sink_%s_multipat_%d_cur_offset' % (prefix, i),
                            self.addrwidth, initval=0)
            for i in range(self.max_pattern_length)]
        var.sink_multipat_sizes = [[self.module.Reg('_sink_%s_multipat_%d_size_%d' %
                                                    (prefix, j, i),
                                                    self.addrwidth + 1, initval=0)
                                    for i in range(self.max_pattern_length)]
                                   for j in range(self.max_multipattern_length)]
        var.sink_multipat_strides = [[self.module.Reg('_sink_%s_multipat_%d_stride_%d' %
                                                      (prefix, j, i),
                                                      self.addrwidth, initval=0)
                                      for i in range(self.max_pattern_length)]
                                     for j in range(self.max_multipattern_length)]
        var.sink_multipat_counts = [[self.module.Reg('_sink_%s_multipat_%d_count_%d' %
                                                     (prefix, j, i),
                                                     self.addrwidth + 1, initval=0)
                                     for i in range(self.max_pattern_length)]
                                    for j in range(self.max_multipattern_length)]

        var.sink_multipat_offset_bufs = [
            self.module.Reg('_sink_%s_multipat_%d_offset_buf' % (prefix, j),
                            self.addrwidth, initval=0)
            for j in range(self.max_multipattern_length)]
        var.sink_multipat_size_bufs = [[self.module.Reg('_sink_%s_multipat_%d_size_buf_%d' %
                                                        (prefix, j, i),
                                                        self.addrwidth, initval=0)
                                        for i in range(self.max_pattern_length)]
                                       for j in range(self.max_multipattern_length)]
        var.sink_multipat_stride_bufs = [[self.module.Reg('_sink_%s_multipat_%d_stride_buf_%d' %
                                                          (prefix, j, i),
                                                          self.addrwidth, initval=0)
                                          for i in range(self.max_pattern_length)]
                                         for j in range(self.max_multipattern_length)]

    def _synthesize_set_sink_multipattern(self, var, name):
        if var.sink_multipat_fsm is not None:
            return

        sink_start = vtypes.Ands(self.sink_start,
                                 vtypes.And(var.sink_mode, mode_ram_multipattern))

        self.seq.If(sink_start, self.stream_oready)(
            var.sink_multipat_num_patterns.dec()
        )

        for (sink_multipat_offset_buf,
             sink_multipat_offset) in zip(var.sink_multipat_offset_bufs,
                                          var.sink_multipat_offsets):
            self.seq.If(sink_start, self.stream_oready)(
                sink_multipat_offset_buf(sink_multipat_offset)
            )

        for (sink_multipat_size_buf_line,
             sink_multipat_size_line) in zip(var.sink_multipat_size_bufs,
                                             var.sink_multipat_sizes):
            for (sink_multipat_size_buf,
                 sink_multipat_size) in zip(sink_multipat_size_buf_line,
                                            sink_multipat_size_line):
                self.seq.If(sink_start, self.stream_oready)(
                    sink_multipat_size_buf(sink_multipat_size)
                )

        for (sink_multipat_stride_buf_line,
             sink_multipat_stride_line) in zip(var.sink_multipat_stride_bufs,
                                               var.sink_multipat_strides):
            for (sink_multipat_stride_buf,
                 sink_multipat_stride) in zip(sink_multipat_stride_buf_line,
                                              sink_multipat_stride_line):
                self.seq.If(sink_start, self.stream_oready)(
                    sink_multipat_stride_buf(sink_multipat_stride)
                )

        fsm_id = self.fsm_id_count
        self.fsm_id_count += 1

        prefix = self._prefix(name)

        fsm_name = '_%s_sink_multipat_fsm_%d' % (prefix, fsm_id)
        var.sink_multipat_fsm = FSM(self.module, fsm_name,
                                    self.clock, self.reset,
                                    as_module=self.fsm_as_module)

        var.sink_multipat_fsm.If(sink_start, self.stream_oready).goto_next()

        for sink_multipat_cur_offset in var.sink_multipat_cur_offsets:
            self.seq.If(var.sink_multipat_fsm.here, self.stream_oready)(
                sink_multipat_cur_offset(0)
            )

        for (sink_multipat_size, sink_multipat_count) in zip(
                var.sink_multipat_size_bufs[0], var.sink_multipat_counts[0]):
            self.seq.If(var.sink_multipat_fsm.here, self.stream_oready)(
                sink_multipat_count(sink_multipat_size - 1)
            )

        var.sink_multipat_fsm.If(self.stream_oready).goto_next()

        if name in self.sink_when_map:
            when = self.sink_when_map[name]
            wcond = when.read()
        else:
            wcond = None

        rdata = var.read()

        sink_all_offset = self.module.Wire('_%s_sink_multipat_all_offset' % prefix,
                                           self.addrwidth)
        sink_all_offset_val = var.sink_multipat_offset_bufs[0]
        for sink_multipat_cur_offset in var.sink_multipat_cur_offsets:
            sink_all_offset_val += sink_multipat_cur_offset
        sink_all_offset.assign(sink_all_offset_val)

        self.seq.If(var.sink_multipat_fsm.here, self.stream_oready)(
            var.sink_ram_wenable(0)
        )
        self.seq.If(var.sink_multipat_fsm.here, wcond, self.stream_oready)(
            var.sink_ram_waddr(sink_all_offset),
            var.sink_ram_wdata(rdata),
            var.sink_ram_wenable(1)
        )

        upcond = None

        for (sink_multipat_cur_offset, sink_multipat_size_buf,
             sink_multipat_stride_buf, sink_multipat_count) in zip(
                 var.sink_multipat_cur_offsets, var.sink_multipat_size_bufs[0],
                 var.sink_multipat_stride_bufs[0], var.sink_multipat_counts[0]):

            self.seq.If(var.sink_multipat_fsm.here, upcond, self.stream_oready)(
                sink_multipat_cur_offset.add(sink_multipat_stride_buf),
                sink_multipat_count.dec()
            )

            reset_cond = sink_multipat_count == 0
            self.seq.If(var.sink_multipat_fsm.here, upcond, reset_cond, self.stream_oready)(
                sink_multipat_cur_offset(0),
                sink_multipat_count(sink_multipat_size_buf - 1)
            )
            upcond = make_condition(upcond, reset_cond)

        fin_cond = upcond

        prev_offset = var.sink_multipat_offset_bufs[0]
        for multipat_offset_buf in var.sink_multipat_offset_bufs[1:]:
            self.seq.If(fin_cond, var.sink_multipat_fsm.here, self.stream_oready)(
                prev_offset(multipat_offset_buf)
            )
            prev_offset = multipat_offset_buf

        prev_sizes = var.sink_multipat_size_bufs[0]
        for multipat_sizes in var.sink_multipat_size_bufs[1:]:
            for prev_size, size in zip(prev_sizes, multipat_sizes):
                self.seq.If(fin_cond, var.sink_multipat_fsm.here, self.stream_oready)(
                    prev_size(size)
                )
            prev_sizes = multipat_sizes

        prev_strides = var.sink_multipat_stride_bufs[0]
        for multipat_strides in var.sink_multipat_stride_bufs[1:]:
            for prev_stride, stride in zip(prev_strides, multipat_strides):
                self.seq.If(fin_cond, var.sink_multipat_fsm.here, self.stream_oready)(
                    prev_stride(stride)
                )
            prev_strides = multipat_strides

        self.seq.If(fin_cond, var.sink_multipat_fsm.here, self.stream_oready)(
            var.sink_multipat_num_patterns.dec()
        )

        var.sink_multipat_fsm.If(fin_cond,
                                 var.sink_multipat_num_patterns == 0,
                                 self.stream_oready).goto_init()
        var.sink_multipat_fsm.If(self.sink_stop, self.stream_oready).goto_init()

    def _setup_sink_fifo(self, fifo, var, set_cond):
        if fifo._id() in var.sink_id_map:
            fifo_id = var.sink_id_map[fifo._id()]
            self.seq.If(set_cond)(
                var.sink_sel(fifo_id)
            )
            return

        if fifo._id() not in self.buf_id_map:
            fifo_id = self.buf_id_count
            self.buf_id_count += 1
            self.buf_id_map[fifo._id()] = fifo_id
        else:
            fifo_id = self.buf_id_map[fifo._id()]

        var.sink_id_map[fifo._id()] = fifo_id

        self.seq.If(set_cond)(
            var.sink_sel(fifo_id)
        )

        fifo_cond = (var.sink_sel == fifo_id)
        enq = vtypes.Ands(self.stream_oready, var.sink_fifo_enq, fifo_cond)
        ack, ready = fifo.enq_rtl(var.sink_fifo_wdata, cond=enq)

        # stall control
        cond = vtypes.Ands(self.sink_busy, fifo_cond)
        fifo_oready = ready
        add_cond(self.stream_oready, cond, fifo_oready)

        if (self.dump and
            (self.dump_mode == 'all' or
             self.dump_mode == 'fifo' or
             (self.dump_mode == 'selective' and
                 hasattr(fifo, 'dump') and fifo.dump))):
            # self._setup_sink_fifo_dump(fifo, var, wenable)
            raise NotImplementedError()

    def _synthesize_set_sink_fifo(self, var, name):
        if var.sink_fsm is not None:
            return

        sink_start = vtypes.Ands(self.sink_start,
                                 vtypes.And(var.sink_mode, mode_fifo))

        self.seq.If(sink_start, self.stream_oready)(
            var.sink_size_buf(var.sink_size),
        )

        fsm_id = self.fsm_id_count
        self.fsm_id_count += 1

        prefix = self._prefix(name)

        fsm_name = '_%s_sink_fsm_%d' % (prefix, fsm_id)
        var.sink_fsm = FSM(self.module, fsm_name, self.clock, self.reset,
                           as_module=self.fsm_as_module)

        var.sink_fsm.If(sink_start, self.stream_oready).goto_next()

        self.seq.If(var.sink_fsm.here, self.stream_oready)(
            var.sink_count(var.sink_size),
            var.sink_size_buf(var.sink_size),
        )
        var.sink_fsm.If(self.stream_oready).goto_next()

        if name in self.sink_when_map:
            when = self.sink_when_map[name]
            wcond = when.read()
        else:
            wcond = None

        rdata = var.read()

        self.seq.If(var.sink_fsm.here, wcond, self.stream_oready)(
            var.sink_fifo_wdata(rdata),
            var.sink_fifo_enq(1),
            var.sink_count.dec()
        )

        var.sink_fsm.If(wcond, var.sink_count == 1, self.stream_oready).goto_init()
        var.sink_fsm.If(self.sink_stop, self.stream_oready).goto_init()

    def _synthesize_set_sink_immediate(self, var, name):
        if var.sink_fsm is not None:
            return

        sink_start = vtypes.Ands(self.sink_start,
                                 vtypes.And(var.sink_mode, mode_ram_normal))

        self.seq.If(sink_start, self.stream_oready)(
            var.sink_size_buf(var.sink_size)
        )

        fsm_id = self.fsm_id_count
        self.fsm_id_count += 1

        prefix = self._prefix(name)

        fsm_name = '_%s_sink_fsm_%d' % (prefix, fsm_id)
        var.sink_fsm = FSM(self.module, fsm_name, self.clock, self.reset,
                           as_module=self.fsm_as_module)

        var.sink_fsm.If(sink_start, self.stream_oready).goto_next()

        self.seq.If(var.sink_fsm.here, self.stream_oready)(
            var.sink_count(var.sink_size_buf)
        )
        var.sink_fsm.If(self.stream_oready).goto_next()

        if name in self.sink_when_map:
            when = self.sink_when_map[name]
            wcond = when.read()
        else:
            wcond = None

        rdata = var.read()

        self.seq.If(var.sink_fsm.here, wcond, self.stream_oready)(
            var.sink_immediate(rdata),
            var.sink_count.dec()
        )

        var.sink_fsm.If(wcond, var.sink_count == 1, self.stream_oready).goto_init()
        var.sink_fsm.If(self.sink_stop, self.stream_oready).goto_init()

    def _setup_read_ram(self, ram, var, port, set_cond):
        if ram._id() in var.read_ram_id_map:
            ram_id = var.read_ram_id_map[ram._id()]
            self.seq.If(set_cond)(
                var.read_ram_sel(ram_id)
            )
            return

        if ram._id() not in self.buf_id_map:
            ram_id = self.buf_id_count
            self.buf_id_count += 1
            self.buf_id_map[ram._id()] = ram_id
        else:
            ram_id = self.buf_id_map[ram._id()]

        var.read_ram_id_map[ram._id()] = ram_id

        self.seq.If(set_cond)(
            var.read_ram_sel(ram_id)
        )

        ram_cond = (var.read_ram_sel == ram_id)
        renable = vtypes.Ands(self.stream_oready, var.enable, ram_cond)

        d, v = ram.read_rtl(var.addr, port=port, cond=renable)

        d_out = d
        add_mux(var.read_data, ram_cond, d_out)

        if (self.dump and
            (self.dump_mode == 'all' or
             self.dump_mode == 'ram' or
             (self.dump_mode == 'selective' and
                 hasattr(ram, 'dump') and ram.dump))):
            self._setup_read_ram_dump(ram, var, renable, d)

    def _setup_read_ram_dump(self, ram, var, read_enable, read_data):
        pipeline_depth = self.pipeline_depth()
        log_pipeline_depth = max(
            int(math.ceil(math.log(max(pipeline_depth, 10), 10))), 1)

        addr_base = (ram.dump_addr_base if hasattr(ram, 'dump_addr_base') else
                     self.dump_base)
        addr_base_char = ('b' if addr_base == 2 else
                          'o' if addr_base == 8 else
                          'd' if addr_base == 10 else
                          'x')
        addr_prefix = ('0b' if addr_base == 2 else
                       '0o' if addr_base == 8 else
                       '  ' if addr_base == 10 else
                       '0x')
        addr_vfmt = ''.join([addr_prefix, '%', addr_base_char])

        data_base = (ram.dump_data_base if hasattr(ram, 'dump_data_base') else
                     self.dump_base)
        data_base_char = ('b' if data_base == 2 else
                          'o' if data_base == 8 else
                          'd' if (data_base == 10 and
                                  (not hasattr(ram, 'point') or ram.point <= 0)) else
                          # 'f' if (data_base == 10 and
                          #        hasattr(ram, 'point') and ram.point > 0) else
                          'g' if (data_base == 10 and
                                  hasattr(ram, 'point') and ram.point > 0) else
                          'x')
        data_prefix = ('0b' if data_base == 2 else
                       '0o' if data_base == 8 else
                       '  ' if data_base == 10 else
                       '0x')
        # if data_base_char == 'f':
        #    point_len = int(math.ceil(ram.point / math.log(10, 2)))
        #    point_len = max(point_len, 8)
        #    total_len = int(math.ceil(ram.datawidth / math.log(10, 2)))
        #    total_len = max(total_len, point_len)
        #    data_vfmt = ''.join([data_prefix, '%',
        #                         '%d.%d' % (total_len + 1, point_len),
        #                         data_base_char])
        # else:
        #    data_vfmt = ''.join([data_prefix, '%', data_base_char])
        data_vfmt = ''.join([data_prefix, '%', data_base_char])

        name = ram.name
        fmt = ''.join(['(', self.name, ' step:%d, ',
                       'read, ', ' ' * (log_pipeline_depth + 2),
                       'age:%d) ', name,
                       '[', addr_vfmt, '] = ', data_vfmt])

        dump_ram_step_name = ('_stream_dump_ram_step_%d_%s' %
                              (self.object_id, name))
        dump_ram_step = self.module.Reg(dump_ram_step_name, 32, initval=0)

        enable = self.seq.Prev(read_enable, 2, cond=self.stream_oready)
        age = dump_ram_step
        addr = self.seq.Prev(var.addr, 2, cond=self.stream_oready)
        if hasattr(ram, 'point') and ram.point > 0:
            data = vtypes.Div(vtypes.SystemTask('itor', read_data),
                              1.0 * (2 ** ram.point))
        elif hasattr(ram, 'point') and ram.point < 0:
            data = vtypes.Times(read_data, 2 ** -ram.point)
        else:
            data = read_data

        self.seq(
            dump_ram_step(0)
        )
        self.seq.If(enable)(
            dump_ram_step.inc()
        )
        self.seq.If(self.dump_enable)(
            dump_ram_step.inc()
        )

        self.seq.If(enable, vtypes.Not(self.dump_mask))(
            vtypes.Display(fmt, dump_ram_step, age, addr, data)
        )

    def _setup_write_ram(self, ram, var, port, set_cond):
        if ram._id() in var.write_ram_id_map:
            ram_id = var.write_ram_id_map[ram._id()]
            self.seq.If(set_cond)(
                var.write_ram_sel(ram_id)
            )
            return

        if ram._id() not in self.buf_id_map:
            ram_id = self.buf_id_count
            self.buf_id_count += 1
            self.buf_id_map[ram._id()] = ram_id
        else:
            ram_id = self.buf_id_map[ram._id()]

        var.write_ram_id_map[ram._id()] = ram_id

        self.seq.If(set_cond)(
            var.write_ram_sel(ram_id)
        )

        ram_cond = (var.write_ram_sel == ram_id)
        wenable = vtypes.Ands(self.stream_oready, var.enable, ram_cond)

        ram.write_rtl(var.addr, var.write_data, port=port, cond=wenable)

        if (self.dump and
            (self.dump_mode == 'all' or
             self.dump_mode == 'ram' or
             (self.dump_mode == 'selective' and
                 hasattr(ram, 'dump') and ram.dump))):
            self._setup_write_ram_dump(ram, var, wenable)

    def _setup_write_ram_dump(self, ram, var, write_enable):
        pipeline_depth = self.pipeline_depth()
        log_pipeline_depth = max(
            int(math.ceil(math.log(max(pipeline_depth, 10), 10))), 1)

        addr_base = (ram.dump_addr_base if hasattr(ram, 'dump_addr_base') else
                     self.dump_base)
        addr_base_char = ('b' if addr_base == 2 else
                          'o' if addr_base == 8 else
                          'd' if addr_base == 10 else
                          'x')
        addr_prefix = ('0b' if addr_base == 2 else
                       '0o' if addr_base == 8 else
                       '  ' if addr_base == 10 else
                       '0x')
        addr_vfmt = ''.join([addr_prefix, '%', addr_base_char])

        data_base = (ram.dump_data_base if hasattr(ram, 'dump_data_base') else
                     self.dump_base)
        data_base_char = ('b' if data_base == 2 else
                          'o' if data_base == 8 else
                          'd' if (data_base == 10 and
                                  (not hasattr(ram, 'point') or ram.point <= 0)) else
                          # 'f' if (data_base == 10 and
                          #        hasattr(ram, 'point') and ram.point > 0) else
                          'g' if (data_base == 10 and
                                  hasattr(ram, 'point') and ram.point > 0) else
                          'x')
        data_prefix = ('0b' if data_base == 2 else
                       '0o' if data_base == 8 else
                       '  ' if data_base == 10 else
                       '0x')
        # if data_base_char == 'f':
        #    point_len = int(math.ceil(ram.point / math.log(10, 2)))
        #    point_len = max(point_len, 8)
        #    total_len = int(math.ceil(ram.datawidth / math.log(10, 2)))
        #    total_len = max(total_len, point_len)
        #    data_vfmt = ''.join([data_prefix, '%',
        #                         '%d.%d' % (total_len + 1, point_len),
        #                         data_base_char])
        # else:
        #    data_vfmt = ''.join([data_prefix, '%', data_base_char])
        data_vfmt = ''.join([data_prefix, '%', data_base_char])

        name = ram.name
        fmt = ''.join(['(', self.name, ' step:%d, ',
                       'write, ', ' ' * (log_pipeline_depth + 1),
                       'age:%d) ', name,
                       '[', addr_vfmt, '] = ', data_vfmt])

        enable = write_enable
        age = self.seq.Prev(self.dump_step, pipeline_depth + 1, cond=self.stream_oready) - 1
        addr = var.addr
        if hasattr(ram, 'point') and ram.point > 0:
            data = vtypes.Div(vtypes.SystemTask('itor', var.write_data),
                              1.0 * (2 ** ram.point))
        elif hasattr(ram, 'point') and ram.point < 0:
            data = vtypes.Times(var.write_data, 2 ** -ram.point)
        else:
            data = var.write_data

        self.seq.If(enable, vtypes.Not(self.dump_mask))(
            vtypes.Display(fmt, self.dump_step, age, addr, data)
        )

    def _set_flag(self, fsm, cond=None, prefix='_set_flag'):
        flag = self.module.TmpReg(initval=0, prefix=prefix)

        if cond is not None:
            set_cond = vtypes.Ands(cond, fsm.here)
        else:
            set_cond = fsm.here

        self.seq.If(cond)(
            flag(0)
        )
        self.seq.If(set_cond)(
            flag(1)
        )

        return flag

    def _implement_stream(self):
        self.implement()
        self.stream_synthesized = True

    def _write_delay(self):
        depth = self.pipeline_depth()
        return depth + self.ram_delay

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
        return tuple(pattern)

    def _prefix(self, name):
        return '%s_%s' % (self.name, name)

    def _dataname(self, name):
        return '%s_data' % self._prefix(name)

    def _collect_substreams(self):
        ret = []

        for sub in self.substreams:
            ret.extend(sub._collect_substreams())

        return ret

    def __getattr__(self, attr):
        f = BaseStream.__getattr__(self, attr)

        if (callable(f) and
            (f.__name__.startswith('Reduce') or
             f.__name__.startswith('Counter') or
             f.__name__.startswith('Pulse'))):

            if self.reduce_reset is None:
                self.reduce_reset = self.module.Reg(
                    '_'.join(['', self.name, 'reduce_reset']), initval=1)
                self.reduce_reset_var = self.Variable(
                    self.reduce_reset, width=1)

            @functools.wraps(f)
            def func(*args, **kwargs):
                if 'reset' in kwargs:
                    reset = self.Lor(self.reduce_reset_var, kwargs['reset'])
                    reset.latency = 0
                else:
                    reset = self.reduce_reset_var

                kwargs['reset'] = reset
                return f(*args, **kwargs)

            return func

        return f


class Substream(BaseSubstream):

    def __init__(self, module, clock, reset, substrm, strm=None):
        self.module = module
        self.clock = clock
        self.reset = reset
        self.reset_delay = 0

        if strm is not None:
            add_mux(substrm.stream_oready, strm.busy, strm.stream_oready)
            add_mux(substrm.is_root, strm.busy, 0)

        BaseSubstream.__init__(self, substrm, strm)

    def to_source(self, name, data):
        source_name = self.substrm._dataname(name)
        cond = self.module.Reg(compiler._tmp_name(self.name('%s_cond' % source_name)),
                               initval=0)
        BaseSubstream.write(self, source_name, data, cond)

    def to_constant(self, name, data):
        constant_name = self.substrm._dataname(name)
        cond = self.module.Reg(compiler._tmp_name(self.name('%s_cond' % constant_name)),
                               initval=0)
        BaseSubstream.write(self, constant_name, data, cond)

    def from_sink(self, name):
        sink_name = self.substrm._dataname(name)
        return BaseSubstream.read(self, sink_name)

    def _collect_substreams(self):
        ret = []
        self.reset_delay = 0
        ret.append(self)
        ret.extend(self.substrm._collect_substreams())
        for s in ret:
            s.reset_delay += 1 + self.start_stage
        return ret


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


def add_cond(targ, cond, value):
    prev_assign = targ._get_assign()
    if not prev_assign:
        targ.assign(vtypes.Mux(cond, value, 1))
    else:
        prev_value = prev_assign.statement.right
        prev_assign.overwrite_right(
            vtypes.Ands(vtypes.Mux(cond, value, 1), prev_value))
        targ.module.remove(prev_assign)
        targ.module.append(prev_assign)
