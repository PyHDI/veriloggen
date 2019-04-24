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

mode_width = 3
mode_idle = vtypes.Int(0, mode_width, base=2)
mode_normal = vtypes.Int(1, mode_width, base=2)
mode_pattern = vtypes.Int(2, mode_width, base=2)
mode_multipattern = vtypes.Int(4, mode_width, base=2)


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
                      'set_sink', 'set_sink_pattern', 'set_sink_multidim',
                      'set_sink_multipattern', 'set_sink_immediate',
                      'set_sink_empty', 'set_constant',
                      'read_sink',
                      'run', 'join', 'done',
                      'source_join', 'source_done',
                      'sink_join', 'sink_done',
                      'enable_dump', 'disable_dump')
    ram_delay = 4

    def __init__(self, m, name, clk, rst,
                 datawidth=32, addrwidth=32,
                 max_pattern_length=4, max_multipattern_length=2,
                 ram_sel_width=8, fsm_as_module=False,
                 dump=False, dump_base=10, dump_mode='all'):

        BaseStream.__init__(self, module=m, clock=clk, reset=rst,
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
        self.start_flag = self.module.Wire(
            '_'.join(['', self.name, 'start_flag']))
        self.start = self.module.Reg(
            '_'.join(['', self.name, 'start']), initval=0)

        self.end_flag = self.module.Reg(
            '_'.join(['', self.name, 'end_flag']), initval=0)
        self.term_sink = self.module.Reg(
            '_'.join(['', self.name, 'term_sink']), initval=0)

        self.source_busy = self.module.Reg(
            '_'.join(['', self.name, 'source_busy']), initval=0)
        self.sink_busy = self.module.Reg(
            '_'.join(['', self.name, 'sink_busy']), initval=0)
        self.sink_wait_count = None

        self.reduce_reset = None
        self.reduce_reset_var = None

        self.sources = OrderedDict()
        self.sinks = OrderedDict()
        self.constants = OrderedDict()
        self.substreams = []

        self.var_name_map = OrderedDict()
        self.var_id_map = OrderedDict()
        self.var_id_name_map = OrderedDict()
        self.var_name_id_map = OrderedDict()
        self.var_id_count = 0

        self.source_idle_map = OrderedDict()
        self.sink_when_map = OrderedDict()

        self.ram_id_count = 1  # '0' is reserved for idle
        self.ram_id_map = OrderedDict()  # key: ran._id(), value: count

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

        # 3'b000: set_source_empty, 3'b001: set_source,
        # 3'b010: set_source_pattern, 3'b100: set_source_multipattern
        var.source_mode = self.module.Reg('_%s_source_mode' % prefix, mode_width,
                                          initval=mode_idle)

        var.source_offset = self.module.Reg('_%s_source_offset' % prefix,
                                            self.addrwidth, initval=0)
        var.source_size = self.module.Reg('_%s_source_size' % prefix,
                                          self.addrwidth + 1, initval=0)
        var.source_stride = self.module.Reg('_%s_source_stride' % prefix,
                                            self.addrwidth, initval=0)
        var.source_count = self.module.Reg('_%s_source_count' % prefix,
                                           self.addrwidth + 1, initval=0)

        var.source_offset_buf = self.module.Reg('_%s_source_offset_buf' % prefix,
                                                self.addrwidth, initval=0)
        var.source_stride_buf = self.module.Reg('_%s_source_stride_buf' % prefix,
                                                self.addrwidth, initval=0)

        var.source_pat_cur_offsets = None
        var.source_pat_sizes = None
        var.source_pat_strides = None
        var.source_pat_counts = None

        var.source_pat_size_bufs = None
        var.source_pat_stride_bufs = None

        var.source_multipat_num_patterns = None
        var.source_multipat_offsets = None
        var.source_multipat_cur_offsets = None
        var.source_multipat_sizes = None
        var.source_multipat_strides = None

        var.source_multipat_offset_bufs = None
        var.source_multipat_size_bufs = None
        var.source_multipat_stride_bufs = None

        var.source_ram_id_map = OrderedDict()
        var.source_ram_sel = self.module.Reg('_%s_source_ram_sel' % prefix,
                                             self.ram_sel_width, initval=0)
        var.source_ram_raddr = self.module.Reg('_%s_source_ram_raddr' % prefix,
                                               self.addrwidth, initval=0)
        var.source_ram_renable = self.module.Reg('_%s_source_ram_renable' % prefix,
                                                 initval=0)
        var.source_ram_rdata = self.module.Wire('_%s_source_ram_rdata' % prefix,
                                                datawidth)
        var.source_ram_rvalid = self.module.Reg('_%s_source_ram_rvalid' % prefix,
                                                initval=0)

        var.has_source_empty = False
        var.source_empty_data = self.module.Reg('_%s_source_empty_data' % prefix,
                                                datawidth, initval=0)

        self.seq(
            var.source_idle(var.source_idle),
            var.source_ram_rvalid(0)
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

        # 3'b001: set_sink, 3'b010: set_sink_pattern, 3'b100: set_sink_multipattern
        data.sink_mode = self.module.Reg('_%s_sink_mode' % prefix, mode_width,
                                         initval=mode_idle)

        data.sink_offset = self.module.Reg('_%s_sink_offset' % prefix,
                                           self.addrwidth, initval=0)
        data.sink_size = self.module.Reg('_%s_sink_size' % prefix,
                                         self.addrwidth + 1, initval=0)
        data.sink_stride = self.module.Reg('_%s_sink_stride' % prefix,
                                           self.addrwidth, initval=0)
        data.sink_count = self.module.Reg('_%s_sink_count' % prefix,
                                          self.addrwidth + 1, initval=0)

        data.sink_offset_buf = self.module.Reg('_%s_sink_offset_buf' % prefix,
                                               self.addrwidth, initval=0)
        data.sink_stride_buf = self.module.Reg('_%s_sink_stride_buf' % prefix,
                                               self.addrwidth, initval=0)

        data.sink_pat_cur_offsets = None
        data.sink_pat_sizes = None
        data.sink_pat_strides = None
        data.sink_pat_counts = None

        data.sink_pat_size_bufs = None
        data.sink_pat_stride_bufs = None

        data.sink_multipat_num_patterns = None
        data.sink_multipat_offsets = None
        data.sink_multipat_cur_offsets = None
        data.sink_multipat_sizes = None
        data.sink_multipat_strides = None

        data.sink_multipat_offset_bufs = None
        data.sink_multipat_size_bufs = None
        data.sink_multipat_stride_bufs = None

        data.sink_ram_id_map = OrderedDict()
        data.sink_ram_sel = self.module.Reg('_%s_sink_ram_sel' % prefix,
                                            self.ram_sel_width, initval=0)
        data.sink_ram_waddr = self.module.Reg('_%s_sink_waddr' % prefix,
                                              self.addrwidth, initval=0)
        data.sink_ram_wenable = self.module.Reg('_%s_sink_wenable' % prefix,
                                                initval=0)
        data.sink_ram_wdata = self.module.Reg('_%s_sink_wdata' % prefix,
                                              data.width, initval=0)

        # default value
        self.seq(
            data.sink_ram_wenable(0)
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
        sub = Substream(self.module, self.clock, self.reset, substrm, self)
        self.substreams.append(sub)
        return sub

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
            var.source_mode(mode_normal),
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
            var.source_mode(mode_pattern),
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
            var.source_mode(mode_multipattern),
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

        source_start = vtypes.Ands(self.start,
                                   vtypes.Not(vtypes.Uor(vtypes.And(var.source_mode, mode_idle))))

        self.seq.If(source_start)(
            var.source_idle(1)
        )

        wdata = var.source_empty_data
        wenable = source_start
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

        set_cond = self._set_flag(fsm)
        start_delay = self._write_delay() - 1

        self.seq.If(set_cond).Delay(start_delay).EagerVal()(
            var.sink_mode(mode_normal),
            var.sink_offset(offset),
            var.sink_size(size),
            var.sink_stride(stride)
        )

        set_cond = self.seq.Prev(set_cond, start_delay)

        port = vtypes.to_int(port)
        self._setup_sink_ram(ram, var, port, set_cond)
        self._synthesize_set_sink(var, name)

        fsm.goto_next()

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

        set_cond = self._set_flag(fsm)
        start_delay = self._write_delay() - 1

        self.seq.If(set_cond).Delay(start_delay).EagerVal()(
            var.sink_mode(mode_pattern),
            var.sink_offset(offset)
        )

        pad = tuple([(1, 0)
                     for _ in range(self.max_pattern_length - len(pattern))])

        for (sink_pat_size, sink_pat_stride,
             (size, stride)) in zip(var.sink_pat_sizes, var.sink_pat_strides,
                                    pattern + pad):
            self.seq.If(set_cond).Delay(start_delay).EagerVal()(
                sink_pat_size(size),
                sink_pat_stride(stride)
            )

        set_cond = self.seq.Prev(set_cond, start_delay)

        port = vtypes.to_int(port)
        self._setup_sink_ram(ram, var, port, set_cond)
        self._synthesize_set_sink_pattern(var, name)

        fsm.goto_next()

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

        set_cond = self._set_flag(fsm)
        start_delay = self._write_delay() - 1

        self.seq.If(set_cond).Delay(start_delay).EagerVal()(
            var.sink_mode(mode_multipattern),
            var.sink_multipat_num_patterns(len(patterns))
        )

        offsets_pad = tuple(
            [0 for _ in range(self.max_multipattern_length - len(patterns))])

        for offset, multipat_offset in zip(offsets + offsets_pad,
                                           var.sink_multipat_offsets):
            self.seq.If(set_cond).Delay(start_delay).EagerVal()(
                multipat_offset(offset)
            )

        for multipat_sizes, multipat_strides, pattern in zip(
                var.sink_multipat_sizes, var.sink_multipat_strides, patterns):
            pad = tuple([(1, 0)
                         for _ in range(self.max_pattern_length - len(pattern))])

            for (multipat_size, multipat_stride,
                 (size, stride)) in zip(multipat_sizes, multipat_strides,
                                        pattern + pad):
                self.seq.If(set_cond).Delay(start_delay).EagerVal()(
                    multipat_size(size),
                    multipat_stride(stride)
                )

        set_cond = self.seq.Prev(set_cond, start_delay)

        port = vtypes.to_int(port)
        self._setup_sink_ram(ram, var, port, set_cond)
        self._synthesize_set_sink_multipattern(var, name)

        fsm.goto_next()

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

        set_cond = self._set_flag(fsm)
        start_delay = self._write_delay() - 1

        self.seq.If(set_cond).Delay(start_delay).EagerVal()(
            var.sink_mode(mode_normal),
            var.sink_size(size)
        )

        set_cond = self.seq.Prev(set_cond, start_delay)

        ram_sel = var.sink_ram_sel
        self.seq.If(set_cond)(
            ram_sel(0)  # '0' is reserved for empty
        )

        self._synthesize_set_sink(var, name)

        fsm.goto_next()

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

        set_cond = self._set_flag(fsm)
        start_delay = self._write_delay() - 1
        set_cond = self.seq.Prev(set_cond, start_delay)

        ram_sel = var.sink_ram_sel

        self.seq.If(set_cond)(
            ram_sel(0)  # '0' is reserved for empty
        )

        fsm.goto_next()

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
            var.write(var.next_constant_data, self.start)
            var.has_constant_data = True

        fsm.goto_next()

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

        return var.sink_ram_wdata

    def run(self, fsm):
        # entry point
        self.fsm._set_index(0)

        cond = self._set_flag(fsm)
        add_mux(self.start_flag, cond, 1)

        # after started
        if self.fsm_synthesized:
            fsm.goto_next()
            fsm.goto_next()
            return

        self.fsm_synthesized = True

        start_cond = vtypes.Ands(self.fsm.here, self.start_flag)

        # start pulse
        self.fsm.seq(
            self.start(0)
        )

        self.fsm.If(self.start_flag)(
            self.start(1),
            self.source_busy(1)
        )

        if self.reduce_reset is not None:
            reset_delay = self.ram_delay + 1
            self.fsm.seq.If(self.seq.Prev(start_cond, reset_delay))(
                self.reduce_reset(0)
            )

        if self.dump:
            dump_delay = self.ram_delay + 1
            self.seq.If(self.seq.Prev(start_cond, dump_delay))(
                self.dump_enable(1)
            )

        substreams = self._collect_substreams()
        for sub in substreams:
            sub.substrm.fsm.seq.If(start_cond)(
                sub.substrm.source_busy(1)
            )

            start_stage = sub.start_stage
            reset_delay = self.ram_delay + 1 + sub.reset_delay
            dump_delay = self.ram_delay + 1 + sub.reset_delay
            cond_delay = self.ram_delay + 1 + sub.reset_delay - 2
            sub_fsm = sub.substrm.fsm
            sub_fsm._set_index(0)

            if sub.substrm.reduce_reset is not None:
                sub_fsm.seq.If(self.seq.Prev(start_cond, reset_delay))(
                    sub.substrm.reduce_reset(0)
                )

            if self.dump and sub.substrm.dump:
                sub_fsm.seq.If(self.seq.Prev(start_cond, dump_delay))(
                    sub.substrm.dump_enable(1)
                )

            for cond in sub.conds.values():
                sub_fsm.seq.If(self.seq.Prev(start_cond, cond_delay))(
                    cond(1)
                )

        self.fsm.If(self.start_flag).goto_next()
        self.fsm.goto_next()

        done_cond = None
        for key, source_idle in sorted(self.source_idle_map.items(),
                                       key=lambda x: x[0]):
            done_cond = make_condition(done_cond, source_idle)

        done = self.module.Wire('_%s_done' % self.name)
        done.assign(done_cond)

        self.fsm.If(done).goto_next()

        self.fsm(
            self.source_busy(0)
        )

        end_cond = self.fsm.here

        # reset accumulate pipelines
        if self.reduce_reset is not None:
            reset_delay = 1
            self.fsm.seq.If(self.seq.Prev(end_cond, reset_delay))(
                self.reduce_reset(1)
            )

        if self.dump:
            dump_delay = 1
            self.seq.If(self.seq.Prev(end_cond, dump_delay))(
                self.dump_enable(0)
            )

        for sub in substreams:
            sub.substrm.fsm.seq.If(end_cond)(
                sub.substrm.source_busy(0)
            )

            reset_delay = 1 + sub.reset_delay
            dump_delay = 1 + sub.reset_delay
            cond_delay = 1 + sub.reset_delay - 1
            sub_fsm = sub.substrm.fsm
            sub_fsm._set_index(0)

            if sub.substrm.reduce_reset is not None:
                sub_fsm.seq.If(self.seq.Prev(end_cond, reset_delay))(
                    sub.substrm.reduce_reset(1)
                )

            if self.dump and sub.substrm.dump:
                sub_fsm.seq.If(self.seq.Prev(end_cond, dump_delay))(
                    sub.substrm.dump_enable(0)
                )

            for cond in sub.conds.values():
                sub_fsm.seq.If(self.seq.Prev(end_cond, cond_delay))(
                    cond(0)
                )

            num_wdelay = sub.substrm._write_delay()

            if sub.substrm.sink_wait_count is None:
                sub.substrm.sink_wait_count = sub.substrm.module.Reg(
                    '_'.join(['', sub.substrm.name, 'sink_wait_count']),
                    int(math.ceil(math.log(num_wdelay, 2))), initval=0)

            sub.substrm.fsm.seq.If(sub.substrm.sink_wait_count == 1,
                                   vtypes.Not(start_cond),
                                   sub.substrm.seq.Prev(end_cond, num_wdelay))(
                sub.substrm.sink_busy(0)
            )
            sub.substrm.fsm.seq.If(start_cond)(
                sub.substrm.sink_busy(1)
            )
            sub.substrm.fsm.seq.If(vtypes.Not(start_cond),
                                   sub.substrm.seq.Prev(end_cond, num_wdelay))(
                sub.substrm.sink_wait_count.dec()
            )
            sub.substrm.fsm.seq.If(start_cond,
                                   vtypes.Not(sub.substrm.seq.Prev(end_cond, num_wdelay)))(
                sub.substrm.sink_wait_count.inc()
            )

        num_wdelay = self._write_delay()

        if self.sink_wait_count is None:
            self.sink_wait_count = self.module.Reg(
                '_'.join(['', self.name, 'sink_wait_count']),
                int(math.ceil(math.log(num_wdelay, 2))), initval=0)

        self.fsm.seq.If(self.sink_wait_count == 1,
                        vtypes.Not(start_cond),
                        self.seq.Prev(end_cond, num_wdelay))(
            self.sink_busy(0)
        )
        self.fsm.seq.If(start_cond)(
            self.sink_busy(1)
        )
        self.fsm.seq.If(vtypes.Not(start_cond),
                        self.seq.Prev(end_cond, num_wdelay))(
            self.sink_wait_count.dec()
        )
        self.fsm.seq.If(start_cond,
                        vtypes.Not(self.seq.Prev(end_cond, num_wdelay)))(
            self.sink_wait_count.inc()
        )

        self.fsm.seq(
            self.end_flag(0)
        )
        self.fsm.seq.If(self.seq.Prev(end_cond, num_wdelay))(
            self.end_flag(1)
        )

        pipeline_depth = self.pipeline_depth()

        self.fsm.seq(
            self.term_sink(0)
        )
        self.fsm.seq.If(self.seq.Prev(end_cond, pipeline_depth))(
            self.term_sink(1)
        )

        self.fsm.goto_init()

        fsm.goto_next()
        fsm.goto_next()

        return 0

    def join(self, fsm):
        fsm.If(vtypes.Not(self.source_busy),
               vtypes.Not(self.sink_busy)).goto_next()
        return 0

    def done(self, fsm):
        return vtypes.Ands(vtypes.Not(self.source_busy),
                           vtypes.Not(self.sink_busy))

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

    def _setup_source_ram(self, ram, var, port, set_cond):
        if ram._id() in var.source_ram_id_map:
            ram_id = var.source_ram_id_map[ram._id()]
            self.seq.If(set_cond)(
                var.source_ram_sel(ram_id)
            )
            return

        if ram._id() not in self.ram_id_map:
            ram_id = self.ram_id_count
            self.ram_id_count += 1
            self.ram_id_map[ram._id()] = ram_id
        else:
            ram_id = self.ram_id_map[ram._id()]

        var.source_ram_id_map[ram._id()] = ram_id

        self.seq.If(set_cond)(
            var.source_ram_sel(ram_id)
        )

        ram_cond = (var.source_ram_sel == ram_id)
        renable = vtypes.Ands(var.source_ram_renable, ram_cond)

        d, v = ram.read_rtl(var.source_ram_raddr, port=port, cond=renable)
        add_mux(var.source_ram_rdata, ram_cond, d)

        self.seq.If(self.seq.Prev(renable, 1))(
            var.source_ram_rvalid(1)
        )

        if (self.dump and
            (self.dump_mode == 'all' or
             self.dump_mode == 'ram' or
             (self.dump_mode == 'selective' and
              hasattr(ram, 'dump') and ram.dump))):
            self._setup_source_ram_dump(ram, var, renable, d)

    def _setup_source_ram_dump(self, ram, var, read_enable, read_data):
        pipeline_depth = self.pipeline_depth()
        log_pipeline_depth = max(
            int(math.ceil(math.log(pipeline_depth, 10))), 1)

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
                                  (not hasattr(ram, 'point') or ram.point == 0)) else
                          'f' if (data_base == 10 and
                                  hasattr(ram, 'point') and ram.point > 0) else
                          'x')
        data_prefix = ('0b' if data_base == 2 else
                       '0o' if data_base == 8 else
                       '  ' if data_base == 10 else
                       '0x')
        data_vfmt = ''.join([data_prefix, '%', data_base_char])

        name = ram.name
        fmt = ''.join(['(', self.name, ' step:%d, ',
                       'read, ', ' ' * (log_pipeline_depth + 2),
                       'age:%d) ', name,
                       '[', addr_vfmt, '] = ', data_vfmt])

        dump_ram_step_name = ('_stream_dump_ram_step_%d_%s' %
                              (self.object_id, name))
        dump_ram_step = self.module.Reg(dump_ram_step_name, 32, initval=0)

        enable = self.seq.Prev(read_enable, 2)
        age = dump_ram_step
        addr = self.seq.Prev(var.source_ram_raddr, 2)
        if hasattr(ram, 'point') and ram.point > 0:
            data = vtypes.Div(vtypes.SystemTask('itor', read_data),
                              1.0 * (2 ** ram.point))
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

        wdata = var.source_ram_rdata
        wenable = var.source_ram_rvalid
        var.write(wdata, wenable)

        source_start = vtypes.Ands(self.start,
                                   vtypes.And(var.source_mode, mode_normal))

        self.seq.If(source_start)(
            var.source_idle(0),
            var.source_offset_buf(var.source_offset),
            var.source_stride_buf(var.source_stride)
        )

        fsm_id = self.fsm_id_count
        self.fsm_id_count += 1

        prefix = self._prefix(name)

        fsm_name = '_%s_source_fsm_%d' % (prefix, fsm_id)
        var.source_fsm = FSM(self.module, fsm_name, self.clock, self.reset,
                             as_module=self.fsm_as_module)

        var.source_fsm.If(source_start).goto_next()

        self.seq.If(var.source_fsm.here)(
            var.source_ram_raddr(var.source_offset_buf),
            var.source_ram_renable(1),
            var.source_count(var.source_size)
        )

        var.source_fsm.goto_next()

        self.seq.If(var.source_fsm.here)(
            var.source_ram_raddr.add(var.source_stride_buf),
            var.source_ram_renable(1),
            var.source_count.dec()
        )
        self.seq.If(var.source_fsm.here, var.source_count == 1)(
            var.source_ram_renable(0),
            var.source_idle(1)
        )

        var.source_fsm.If(var.source_count == 1).goto_init()

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

        wdata = var.source_ram_rdata
        wenable = var.source_ram_rvalid
        var.write(wdata, wenable)

        source_start = vtypes.Ands(self.start,
                                   vtypes.And(var.source_mode, mode_pattern))

        self.seq.If(source_start)(
            var.source_idle(0),
            var.source_offset_buf(var.source_offset)
        )

        for source_pat_cur_offset in var.source_pat_cur_offsets:
            self.seq.If(source_start)(
                source_pat_cur_offset(0)
            )

        for (source_pat_size, source_pat_count) in zip(
                var.source_pat_sizes, var.source_pat_counts):
            self.seq.If(source_start)(
                source_pat_count(source_pat_size - 1)
            )

        for (source_pat_size_buf, source_pat_size) in zip(
                var.source_pat_size_bufs, var.source_pat_sizes):
            self.seq.If(source_start)(
                source_pat_size_buf(source_pat_size)
            )

        for (source_pat_stride_buf, source_pat_stride) in zip(
                var.source_pat_stride_bufs, var.source_pat_strides):
            self.seq.If(source_start)(
                source_pat_stride_buf(source_pat_stride)
            )

        fsm_id = self.fsm_id_count
        self.fsm_id_count += 1

        prefix = self._prefix(name)

        fsm_name = '_%s_source_pat_fsm_%d' % (prefix, fsm_id)
        var.source_pat_fsm = FSM(self.module, fsm_name,
                                 self.clock, self.reset,
                                 as_module=self.fsm_as_module)

        var.source_pat_fsm.If(source_start).goto_next()

        source_all_offset = self.module.Wire('_%s_source_pat_all_offset' % prefix,
                                             self.addrwidth)
        source_all_offset_val = var.source_offset_buf
        for source_pat_cur_offset in var.source_pat_cur_offsets:
            source_all_offset_val += source_pat_cur_offset
        source_all_offset.assign(source_all_offset_val)

        self.seq.If(var.source_pat_fsm.here)(
            var.source_ram_raddr(source_all_offset),
            var.source_ram_renable(1)
        )

        upcond = None

        for (source_pat_cur_offset, source_pat_size_buf,
             source_pat_stride_buf, source_pat_count) in zip(
                 var.source_pat_cur_offsets, var.source_pat_size_bufs,
                 var.source_pat_stride_bufs, var.source_pat_counts):

            self.seq.If(var.source_pat_fsm.here, upcond)(
                source_pat_cur_offset.add(source_pat_stride_buf),
                source_pat_count.dec()
            )

            reset_cond = source_pat_count == 0
            self.seq.If(var.source_pat_fsm.here, upcond, reset_cond)(
                source_pat_cur_offset(0),
                source_pat_count(source_pat_size_buf - 1)
            )
            upcond = make_condition(upcond, reset_cond)

        fin_cond = upcond

        var.source_pat_fsm.If(fin_cond).goto_next()

        self.seq.If(var.source_pat_fsm.here)(
            var.source_ram_renable(0),
            var.source_idle(1)
        )

        var.source_pat_fsm.goto_init()

    def _make_source_multipattern_vars(self, var, name):
        if var.source_multipat_cur_offsets is not None:
            return

        prefix = self._prefix(name)

        var.source_multipat_num_patterns = self.module.Reg(
            '_source_%s_multipat_num_patterns' % prefix,
            int(math.ceil(math.log(self.max_multipattern_length, 2))), initval=0)
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

        wdata = var.source_ram_rdata
        wenable = var.source_ram_rvalid
        var.write(wdata, wenable)

        source_start = vtypes.Ands(self.start,
                                   vtypes.And(var.source_mode, mode_multipattern))

        self.seq.If(source_start)(
            var.source_idle(0)
        )

        for source_multipat_offset_buf, source_multipat_offset in zip(var.source_multipat_offset_bufs,
                                                                      var.source_multipat_offsets):
            self.seq.If(source_start)(
                source_multipat_offset_buf(source_multipat_offset)
            )

        for source_multipat_size_buf_line, source_multipat_size_line in zip(var.source_multipat_size_bufs,
                                                                            var.source_multipat_sizes):
            for source_multipat_size_buf, source_multipat_size in zip(source_multipat_size_buf_line,
                                                                      source_multipat_size_line):
                self.seq.If(source_start)(
                    source_multipat_size_buf(source_multipat_size)
                )

        for source_multipat_stride_buf_line, source_multipat_stride_line in zip(var.source_multipat_stride_bufs,
                                                                                var.source_multipat_strides):
            for source_multipat_stride_buf, source_multipat_stride in zip(source_multipat_stride_buf_line,
                                                                          source_multipat_stride_line):
                self.seq.If(source_start)(
                    source_multipat_stride_buf(source_multipat_stride)
                )

        self.seq.If(source_start)(
            var.source_multipat_num_patterns.dec()
        )

        for source_multipat_cur_offset in var.source_multipat_cur_offsets:
            self.seq.If(source_start)(
                source_multipat_cur_offset(0)
            )

        for (source_multipat_size, source_multipat_count) in zip(
                var.source_multipat_sizes[0], var.source_multipat_counts[0]):
            self.seq.If(source_start)(
                source_multipat_count(source_multipat_size - 1)
            )

        fsm_id = self.fsm_id_count
        self.fsm_id_count += 1

        prefix = self._prefix(name)

        fsm_name = '_%s_source_multipat_fsm_%d' % (prefix, fsm_id)
        var.source_multipat_fsm = FSM(self.module, fsm_name,
                                      self.clock, self.reset,
                                      as_module=self.fsm_as_module)

        var.source_multipat_fsm.If(source_start).goto_next()

        source_all_offset = self.module.Wire('_%s_source_multipat_all_offset' % prefix,
                                             self.addrwidth)
        source_all_offset_val = var.source_multipat_offset_bufs[0]
        for source_multipat_cur_offset in var.source_multipat_cur_offsets:
            source_all_offset_val += source_multipat_cur_offset
        source_all_offset.assign(source_all_offset_val)

        self.seq.If(var.source_multipat_fsm.here)(
            var.source_ram_raddr(source_all_offset),
            var.source_ram_renable(1)
        )

        upcond = None

        for (source_multipat_cur_offset, source_multipat_size_buf,
             source_multipat_stride_buf, source_multipat_count) in zip(
                 var.source_multipat_cur_offsets, var.source_multipat_size_bufs[0],
                 var.source_multipat_stride_bufs[0], var.source_multipat_counts[0]):

            self.seq.If(var.source_multipat_fsm.here, upcond)(
                source_multipat_cur_offset.add(source_multipat_stride_buf),
                source_multipat_count.dec()
            )

            reset_cond = source_multipat_count == 0
            self.seq.If(var.source_multipat_fsm.here, upcond, reset_cond)(
                source_multipat_cur_offset(0),
                source_multipat_count(source_multipat_size_buf - 1)
            )
            upcond = make_condition(upcond, reset_cond)

        fin_cond = upcond

        prev_offset = var.source_multipat_offset_bufs[0]
        for multipat_offset_buf in var.source_multipat_offset_bufs[1:]:
            self.seq.If(fin_cond, var.source_multipat_fsm.here)(
                prev_offset(multipat_offset_buf)
            )
            prev_offset = multipat_offset_buf

        prev_sizes = var.source_multipat_size_bufs[0]
        for multipat_sizes in var.source_multipat_size_bufs[1:]:
            for prev_size, size in zip(prev_sizes, multipat_sizes):
                self.seq.If(fin_cond, var.source_multipat_fsm.here)(
                    prev_size(size)
                )
            prev_sizes = multipat_sizes

        prev_strides = var.source_multipat_stride_bufs[0]
        for multipat_strides in var.source_multipat_stride_bufs[1:]:
            for prev_stride, stride in zip(prev_strides, multipat_strides):
                self.seq.If(fin_cond, var.source_multipat_fsm.here)(
                    prev_stride(stride)
                )
            prev_strides = multipat_strides

        self.seq.If(fin_cond, var.source_multipat_fsm.here)(
            var.source_multipat_num_patterns.dec()
        )

        var.source_multipat_fsm.If(fin_cond,
                                   var.source_multipat_num_patterns == 0).goto_next()

        self.seq.If(var.source_multipat_fsm.here)(
            var.source_ram_renable(0),
            var.source_idle(1)
        )

        var.source_multipat_fsm.goto_init()

    def _setup_sink_ram(self, ram, var, port, set_cond):
        if ram._id() in var.sink_ram_id_map:
            ram_id = var.sink_ram_id_map[ram._id()]
            self.seq.If(set_cond)(
                var.sink_ram_sel(ram_id)
            )
            return

        if ram._id() not in self.ram_id_map:
            ram_id = self.ram_id_count
            self.ram_id_count += 1
            self.ram_id_map[ram._id()] = ram_id
        else:
            ram_id = self.ram_id_map[ram._id()]

        var.sink_ram_id_map[ram._id()] = ram_id

        self.seq.If(set_cond)(
            var.sink_ram_sel(ram_id)
        )

        ram_cond = (var.sink_ram_sel == ram_id)
        wenable = vtypes.Ands(var.sink_ram_wenable, ram_cond)
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
            int(math.ceil(math.log(pipeline_depth, 10))), 1)

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
                                  (not hasattr(ram, 'point') or ram.point == 0)) else
                          'f' if (data_base == 10 and
                                  hasattr(ram, 'point') and ram.point > 0) else
                          'x')
        data_prefix = ('0b' if data_base == 2 else
                       '0o' if data_base == 8 else
                       '  ' if data_base == 10 else
                       '0x')
        data_vfmt = ''.join([data_prefix, '%', data_base_char])

        name = ram.name
        fmt = ''.join(['(', self.name, ' step:%d, ',
                       'write, ', ' ' * (log_pipeline_depth + 1),
                       'age:%d) ', name,
                       '[', addr_vfmt, '] = ', data_vfmt])

        enable = var.sink_ram_wenable
        age = self.seq.Prev(self.dump_step, pipeline_depth + 1) - 1
        addr = var.sink_ram_waddr
        if hasattr(ram, 'point') and ram.point > 0:
            data = vtypes.Div(vtypes.SystemTask('itor', var.sink_ram_wdata),
                              1.0 * (2 ** ram.point))
        else:
            data = var.sink_ram_wdata

        self.seq.If(enable, vtypes.Not(self.dump_mask))(
            vtypes.Display(fmt, self.dump_step, age, addr, data)
        )

    def _synthesize_set_sink(self, var, name):
        if var.sink_fsm is not None:
            return

        start_delay = self._write_delay()
        start = self.seq.Prev(self.start, start_delay)
        sink_start = vtypes.Ands(start,
                                 vtypes.And(var.sink_mode, mode_normal))

        fsm_id = self.fsm_id_count
        self.fsm_id_count += 1

        prefix = self._prefix(name)

        fsm_name = '_%s_sink_fsm_%d' % (prefix, fsm_id)
        var.sink_fsm = FSM(self.module, fsm_name, self.clock, self.reset,
                           as_module=self.fsm_as_module)

        self.seq.If(sink_start)(
            var.sink_ram_waddr(var.sink_offset - var.sink_stride),
            var.sink_count(var.sink_size),
            var.sink_offset_buf(var.sink_offset),
            var.sink_stride_buf(var.sink_stride)
        )
        var.sink_fsm.If(sink_start).goto_next()

        if name in self.sink_when_map:
            when = self.sink_when_map[name]
            wcond = when.read()
        else:
            wcond = None

        rdata = var.read()

        self.seq.If(var.sink_fsm.here, wcond)(
            var.sink_ram_waddr.add(var.sink_stride_buf),
            var.sink_ram_wdata(rdata),
            var.sink_ram_wenable(1),
            var.sink_count.dec()
        )

        var.sink_fsm.If(wcond, var.sink_count == 1).goto_init()
        var.sink_fsm.If(self.term_sink).goto_init()

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

        start_delay = self._write_delay()
        start = self.seq.Prev(self.start, start_delay)
        sink_start = vtypes.Ands(start,
                                 vtypes.And(var.sink_mode, mode_pattern))

        fsm_id = self.fsm_id_count
        self.fsm_id_count += 1

        prefix = self._prefix(name)

        fsm_name = '_%s_sink_pat_fsm_%d' % (prefix, fsm_id)
        var.sink_pat_fsm = FSM(self.module, fsm_name,
                               self.clock, self.reset,
                               as_module=self.fsm_as_module)

        self.seq.If(sink_start)(
            var.sink_offset_buf(var.sink_offset)
        )

        for sink_pat_cur_offset in var.sink_pat_cur_offsets:
            self.seq.If(sink_start)(
                sink_pat_cur_offset(0),
            )

        for (sink_pat_size, sink_pat_count) in zip(
                var.sink_pat_sizes, var.sink_pat_counts):
            self.seq.If(sink_start)(
                sink_pat_count(sink_pat_size - 1)
            )

        for (sink_pat_size_buf, sink_pat_size) in zip(
                var.sink_pat_size_bufs, var.sink_pat_sizes):
            self.seq.If(sink_start)(
                sink_pat_size_buf(sink_pat_size)
            )

        for (sink_pat_stride_buf, sink_pat_stride) in zip(
                var.sink_pat_stride_bufs, var.sink_pat_strides):
            self.seq.If(sink_start)(
                sink_pat_stride_buf(sink_pat_stride)
            )

        var.sink_pat_fsm.If(sink_start).goto_next()

        if name in self.sink_when_map:
            when = self.sink_when_map[name]
            wcond = when.read()
        else:
            wcond = None

        sink_all_offset = self.module.Wire('_%s_sink_pat_all_offset' % prefix,
                                           self.addrwidth)
        sink_all_offset_val = var.sink_offset_buf
        for sink_pat_cur_offset in var.sink_pat_cur_offsets:
            sink_all_offset_val += sink_pat_cur_offset
        sink_all_offset.assign(sink_all_offset_val)

        if name in self.sink_when_map:
            when = self.sink_when_map[name]
            wcond = when.read()
        else:
            wcond = None

        rdata = var.read()

        self.seq.If(var.sink_pat_fsm.here, wcond)(
            var.sink_ram_waddr(sink_all_offset),
            var.sink_ram_wdata(rdata),
            var.sink_ram_wenable(1)
        )

        upcond = None

        for (sink_pat_cur_offset, sink_pat_size_buf,
             sink_pat_stride_buf, sink_pat_count) in zip(
                 var.sink_pat_cur_offsets, var.sink_pat_size_bufs,
                 var.sink_pat_stride_bufs, var.sink_pat_counts):

            self.seq.If(var.sink_pat_fsm.here, upcond)(
                sink_pat_cur_offset.add(sink_pat_stride_buf),
                sink_pat_count.dec()
            )

            reset_cond = sink_pat_count == 0
            self.seq.If(var.sink_pat_fsm.here, upcond, reset_cond)(
                sink_pat_cur_offset(0),
                sink_pat_count(sink_pat_size_buf - 1)
            )
            upcond = make_condition(upcond, reset_cond)

        fin_cond = upcond

        var.sink_pat_fsm.If(fin_cond).goto_init()
        var.sink_pat_fsm.If(self.term_sink).goto_init()

    def _make_sink_multipattern_vars(self, var, name):
        if var.sink_multipat_cur_offsets is not None:
            return

        prefix = self._prefix(name)

        var.sink_multipat_num_patterns = self.module.Reg(
            '_sink_%s_multipat_num_patterns' % prefix,
            int(math.ceil(math.log(self.max_multipattern_length, 2))), initval=0)
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

        start_delay = self._write_delay()
        start = self.seq.Prev(self.start, start_delay)
        sink_start = vtypes.Ands(start,
                                 vtypes.And(var.sink_mode, mode_multipattern))

        fsm_id = self.fsm_id_count
        self.fsm_id_count += 1

        prefix = self._prefix(name)

        fsm_name = '_%s_sink_multipat_fsm_%d' % (prefix, fsm_id)
        var.sink_multipat_fsm = FSM(self.module, fsm_name,
                                    self.clock, self.reset,
                                    as_module=self.fsm_as_module)

        for sink_multipat_offset_buf, sink_multipat_offset in zip(var.sink_multipat_offset_bufs,
                                                                  var.sink_multipat_offsets):
            self.seq.If(sink_start)(
                sink_multipat_offset_buf(sink_multipat_offset)
            )

        for sink_multipat_size_buf_line, sink_multipat_size_line in zip(var.sink_multipat_size_bufs,
                                                                        var.sink_multipat_sizes):
            for sink_multipat_size_buf, sink_multipat_size in zip(sink_multipat_size_buf_line,
                                                                  sink_multipat_size_line):
                self.seq.If(sink_start)(
                    sink_multipat_size_buf(sink_multipat_size)
                )

        for sink_multipat_stride_buf_line, sink_multipat_stride_line in zip(var.sink_multipat_stride_bufs,
                                                                            var.sink_multipat_strides):
            for sink_multipat_stride_buf, sink_multipat_stride in zip(sink_multipat_stride_buf_line,
                                                                      sink_multipat_stride_line):
                self.seq.If(sink_start)(
                    sink_multipat_stride_buf(sink_multipat_stride)
                )

        self.seq.If(sink_start)(
            var.sink_multipat_num_patterns.dec()
        )

        for sink_multipat_cur_offset in var.sink_multipat_cur_offsets:
            self.seq.If(sink_start)(
                sink_multipat_cur_offset(0)
            )

        for (sink_multipat_size, sink_multipat_count) in zip(
                var.sink_multipat_size_bufs[0], var.sink_multipat_counts[0]):
            self.seq.If(sink_start)(
                sink_multipat_count(sink_multipat_size - 1)
            )

        var.sink_multipat_fsm.If(sink_start).goto_next()

        if name in self.sink_when_map:
            when = self.sink_when_map[name]
            wcond = when.read()
        else:
            wcond = None

        sink_all_offset = self.module.Wire('_%s_sink_multipat_all_offset' % prefix,
                                           self.addrwidth)
        sink_all_offset_val = var.sink_multipat_offsets[0]
        for sink_multipat_cur_offset in var.sink_multipat_cur_offsets:
            sink_all_offset_val += sink_multipat_cur_offset
        sink_all_offset.assign(sink_all_offset_val)

        if name in self.sink_when_map:
            when = self.sink_when_map[name]
            wcond = when.read()
        else:
            wcond = None

        rdata = var.read()

        self.seq.If(var.sink_multipat_fsm.here)(
            var.sink_ram_wenable(0)
        )
        self.seq.If(var.sink_multipat_fsm.here, wcond)(
            var.sink_ram_waddr(sink_all_offset),
            var.sink_ram_wdata(rdata),
            var.sink_ram_wenable(1)
        )

        upcond = None

        for (sink_multipat_cur_offset, sink_multipat_size_buf,
             sink_multipat_stride_buf, sink_multipat_count) in zip(
                 var.sink_multipat_cur_offsets, var.sink_multipat_size_bufs[0],
                 var.sink_multipat_stride_bufs[0], var.sink_multipat_counts[0]):

            self.seq.If(var.sink_multipat_fsm.here, upcond)(
                sink_multipat_cur_offset.add(sink_multipat_stride_buf),
                sink_multipat_count.dec()
            )

            reset_cond = sink_multipat_count == 0
            self.seq.If(var.sink_multipat_fsm.here, upcond, reset_cond)(
                sink_multipat_cur_offset(0),
                sink_multipat_count(sink_multipat_size_buf - 1)
            )
            upcond = make_condition(upcond, reset_cond)

        fin_cond = upcond

        prev_offset = var.sink_multipat_offset_bufs[0]
        for multipat_offset_buf in var.sink_multipat_offset_bufs[1:]:
            self.seq.If(fin_cond, var.sink_multipat_fsm.here)(
                prev_offset(multipat_offset_buf)
            )
            prev_offset = multipat_offset_buf

        prev_sizes = var.sink_multipat_size_bufs[0]
        for multipat_sizes in var.sink_multipat_size_bufs[1:]:
            for prev_size, size in zip(prev_sizes, multipat_sizes):
                self.seq.If(fin_cond, var.sink_multipat_fsm.here)(
                    prev_size(size)
                )
            prev_sizes = multipat_sizes

        prev_strides = var.sink_multipat_stride_bufs[0]
        for multipat_strides in var.sink_multipat_stride_bufs[1:]:
            for prev_stride, stride in zip(prev_strides, multipat_strides):
                self.seq.If(fin_cond, var.sink_multipat_fsm.here)(
                    prev_stride(stride)
                )
            prev_strides = multipat_strides

        self.seq.If(fin_cond, var.sink_multipat_fsm.here)(
            var.sink_multipat_num_patterns.dec()
        )

        var.sink_multipat_fsm.If(fin_cond,
                                 var.sink_multipat_num_patterns == 0).goto_init()
        var.sink_multipat_fsm.If(self.term_sink).goto_init()

    def _set_flag(self, fsm, prefix='_set_flag'):
        flag = self.module.TmpReg(initval=0, prefix=prefix)
        cond = fsm.here

        self.seq(
            flag(0)
        )
        self.seq.If(cond)(
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
             f.__name__.startswith('Pulse') or
             f.__name__.startswith('RingBuffer'))):
            if self.reduce_reset is None:
                self.reduce_reset = self.module.Reg(
                    '_'.join(['', self.name, 'reduce_reset']), initval=1)
                self.reduce_reset_var = self.Variable(
                    self.reduce_reset, width=1)

            return functools.partial(f, reset=self.reduce_reset_var)

        return f


class Substream(BaseSubstream):

    def __init__(self, module, clock, reset, substrm, strm=None):
        self.module = module
        self.clock = clock
        self.reset = reset
        self.reset_delay = 0
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
