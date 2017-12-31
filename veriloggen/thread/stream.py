from __future__ import absolute_import
from __future__ import print_function

import functools
import ast
import inspect
import textwrap
from collections import OrderedDict

import veriloggen.core.vtypes as vtypes
from veriloggen.seq.seq import make_condition
from veriloggen.fsm.fsm import FSM
from veriloggen.seq.seq import Seq
from veriloggen.types.ram import SyncRAMManager
from veriloggen.stream.stream import Stream as BaseStream
from veriloggen.stream.stypes import Substream as BaseSubstream

from . import compiler
from . import thread


class Stream(BaseStream):
    __intrinsics__ = ('set_source', 'set_source_pattern', 'set_source_multidim',
                      'set_sink', 'set_sink_pattern', 'set_sink_multidim',
                      'set_sink_empty', 'set_constant',
                      'run', 'join', 'done')

    def __init__(self, m, name, clk, rst, datawidth=32, fsm_sel_width=16):
        BaseStream.__init__(self, module=m, clock=clk, reset=rst,
                            no_hook=True)

        self.name = name
        self.datawidth = datawidth
        self.fsm_sel_width = fsm_sel_width
        self.stream_synthesized = False
        self.fsm_synthesized = False

        self.fsm = FSM(self.module, '_%s_fsm' %
                       self.name, self.clock, self.reset)
        self.start = self.module.Reg(
            '_'.join(['', self.name, 'start']), initval=0)
        self.busy = self.module.Reg(
            '_'.join(['', self.name, 'busy']), initval=0)

        self.reduce_reset = None
        self.reduce_reset_var = None

        self.sources = {}
        self.sinks = {}
        self.constants = {}
        self.substreams = []

        self.var_name_map = {}
        self.var_id_map = {}
        self.var_id_name_map = {}
        self.var_name_id_map = {}
        self.var_id_count = 0
        self.source_idle_map = {}
        self.sink_when_map = {}

        self.fsm_id_map = {}
        self.fsm_id_count = 1  # '0' is reserved for idle
        self.var_id_fsm_sel_map = {}  # key: var_id, value: fsm_id reg

        self.ram_delay = 4

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
        self.var_id_fsm_sel_map[_id] = self.module.Reg('_%s_fsm_sel' % prefix,
                                                       self.fsm_sel_width, initval=0)
        self.source_idle_map[name] = self.module.Reg('_%s_idle' % prefix,
                                                     initval=1)

        return var

    def sink(self, data, name=None, when=None, when_name=None):
        if self.stream_synthesized:
            raise ValueError(
                'cannot modify the stream because already synthesized')

        _id = self.var_id_count
        if name is None:
            name = 'source_%d' % _id

        prefix = self._prefix(name)

        if name in self.var_name_map:
            raise ValueError("'%s' is already defined in stream '%s'" %
                             (name, self.name))
        else:
            data.output(self._dataname(name))

        self.var_id_count += 1

        self.sinks[name] = data
        self.var_id_map[_id] = data
        self.var_name_map[name] = data
        self.var_id_name_map[_id] = name
        self.var_name_id_map[name] = _id
        self.var_id_fsm_sel_map[_id] = self.module.Reg('_%s_fsm_sel' % prefix,
                                                       self.fsm_sel_width, initval=0)

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

        var = self.ParameterVariable(self._dataname(name), datawidth,
                                     point, signed)

        self.constants[name] = var
        self.var_id_map[_id] = var
        self.var_name_map[name] = var
        self.var_id_name_map[_id] = name
        self.var_name_id_map[name] = _id
        self.var_id_fsm_sel_map[_id] = self.module.Reg('_%s_fsm_sel' % prefix,
                                                       self.fsm_sel_width, initval=0)

        return var

    def substream(self, substrm):
        sub = Substream(self.module, self.clock, self.reset, substrm)
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

        prefix = self._prefix(name)

        fsm_id = self.fsm_id_count
        fsm_name = '_%s_fsm_%d' % (prefix, fsm_id)
        source_fsm = FSM(self.module, fsm_name, self.clock, self.reset)
        self.fsm_id_map[fsm_id] = source_fsm
        self.fsm_id_count += 1

        source_idle = self.source_idle_map[name]
        source_offset = self.module.Reg('_%s_offset_%d' % (prefix, fsm_id),
                                        ram.addrwidth, initval=0)
        source_size = self.module.Reg('_%s_size_%d' % (prefix, fsm_id),
                                      ram.addrwidth + 1, initval=0)
        source_stride = self.module.Reg('_%s_stride_%d' % (prefix, fsm_id),
                                        ram.addrwidth, initval=0)
        source_count = self.module.Reg('_%s_count_%d' % (prefix, fsm_id),
                                       ram.addrwidth + 1, initval=0)

        var_id = self.var_name_id_map[name]
        fsm_sel = self.var_id_fsm_sel_map[var_id]

        set_cond = (fsm.state == fsm.current)

        source_fsm.If(set_cond)(
            source_offset(offset),
            source_size(size),
            source_stride(stride)
        )
        self.seq.If(set_cond)(
            fsm_sel(fsm_id)
        )

        self.seq.If(self.start)(
            source_idle(0)
        )

        source_start = vtypes.Ands(
            self.start, fsm_sel == fsm_id, source_size > 0)

        source_fsm.If(source_start)(
            source_count(source_size)
        )
        source_fsm.If(source_start).goto_next()

        raddr = self.module.Reg('_%s_raddr_%d' % (prefix, fsm_id),
                                ram.addrwidth, initval=0)
        renable = self.module.Reg('_%s_renable_%d' % (prefix, fsm_id),
                                  initval=0)

        rdata, rvalid = ram.read_rtl(raddr, port=port, cond=renable)

        wdata = rdata
        wenable = rvalid
        var.write(wdata, wenable)

        source_fsm(
            raddr(source_offset),
            renable(1),
            source_count.dec()
        )
        source_fsm.Delay(1)(
            renable(0)
        )
        self.seq.If(source_fsm.state == source_fsm.current,
                    source_count == 1)(
            source_idle(1)
        )
        source_fsm.If(source_count == 1).goto_init()
        source_fsm.If(source_count > 1).goto_next()

        source_fsm(
            raddr.add(source_stride),
            renable(1),
            source_count.dec()
        )
        source_fsm.Delay(1)(
            renable(0)
        )
        source_fsm.If(source_count == 1).goto_init()

        self.seq.If(source_fsm.state == source_fsm.current,
                    source_count == 1)(
            source_idle(1)
        )

        source_fsm._set_index(0)

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

        prefix = self._prefix(name)

        fsm_id = self.fsm_id_count
        fsm_name = '_%s_fsm_%d' % (prefix, fsm_id)
        source_fsm = FSM(self.module, fsm_name, self.clock, self.reset)
        self.fsm_id_map[fsm_id] = source_fsm
        self.fsm_id_count += 1

        source_idle = self.source_idle_map[name]
        source_offset = self.module.Reg('_%s_offset_%d' % (prefix, fsm_id),
                                        ram.addrwidth, initval=0)
        source_pat_offsets = [self.module.Reg('_%s_pat_offset_%d_%d' % (prefix, fsm_id, i),
                                              ram.addrwidth, initval=0)
                              for i, _ in enumerate(pattern)]
        source_pat_sizes = [self.module.Reg('_%s_pat_size_%d_%d' % (prefix, fsm_id, i),
                                            ram.addrwidth + 1, initval=0)
                            for i, _ in enumerate(pattern)]
        source_pat_strides = [self.module.Reg('_%s_pat_stride_%d_%d' % (prefix, fsm_id, i),
                                              ram.addrwidth, initval=0)
                              for i, _ in enumerate(pattern)]
        source_pat_counts = [self.module.Reg('_%s_pat_count_%d_%d' % (prefix, fsm_id, i),
                                             ram.addrwidth + 1, initval=0)
                             for i, _ in enumerate(pattern)]

        var_id = self.var_name_id_map[name]
        fsm_sel = self.var_id_fsm_sel_map[var_id]

        set_cond = (fsm.state == fsm.current)

        source_fsm.If(set_cond)(
            source_offset(offset)
        )
        self.seq.If(set_cond)(
            fsm_sel(fsm_id)
        )

        for source_pat_offset in source_pat_offsets:
            source_fsm.If(set_cond)(
                source_pat_offset(0)
            )

        for (source_pat_size, source_pat_stride, (size, stride)) in zip(
                source_pat_sizes, source_pat_strides, pattern):
            source_fsm.If(set_cond)(
                source_pat_size(size),
                source_pat_stride(stride)
            )

        self.seq.If(self.start)(
            source_idle(0)
        )

        source_start = vtypes.Ands(self.start, fsm_sel == fsm_id)
        for source_pat_size in source_pat_sizes:
            source_start = vtypes.Ands(source_start, source_pat_size > 0)

        for (source_pat_size, source_pat_count) in zip(
                source_pat_sizes, source_pat_counts):
            source_fsm.If(source_start)(
                source_pat_count(source_pat_size - 1)
            )

        source_fsm.If(source_start).goto_next()

        source_all_offset = self.module.Wire('_%s_all_offset_%d' % (prefix, fsm_id),
                                             ram.addrwidth)
        source_all_offset_val = source_offset
        for source_pat_offset in source_pat_offsets:
            source_all_offset_val += source_pat_offset
        source_all_offset.assign(source_all_offset_val)

        raddr = self.module.Reg('_%s_raddr_%d' % (prefix, fsm_id),
                                ram.addrwidth, initval=0)
        renable = self.module.Reg('_%s_renable_%d' % (prefix, fsm_id),
                                  initval=0)

        rdata, rvalid = ram.read_rtl(raddr, port=port, cond=renable)

        wdata = rdata
        wenable = rvalid
        var.write(wdata, wenable)

        source_fsm(
            raddr(source_all_offset),
            renable(1)
        )
        source_fsm.Delay(1)(
            renable(0)
        )

        upcond = None

        for (source_pat_offset, source_pat_size,
             source_pat_stride, source_pat_count) in zip(
                 source_pat_offsets, source_pat_sizes,
                 source_pat_strides, source_pat_counts):
            source_fsm.If(upcond)(
                source_pat_offset.add(source_pat_stride),
                source_pat_count.dec()
            )
            reset_cond = source_pat_count == 0
            source_fsm.If(upcond, reset_cond)(
                source_pat_offset(0),
                source_pat_count(source_pat_size - 1)
            )
            upcond = make_condition(upcond, reset_cond)

        fin_cond = upcond

        source_fsm.If(fin_cond).goto_init()

        self.seq.If(source_fsm.state == source_fsm.current,
                    fin_cond)(
            source_idle(1)
        )

        source_fsm._set_index(0)

        fsm.goto_next()

    def set_source_multidim(self, fsm, name, ram, offset, shape, order=None, port=0):
        """ intrinsic method to assign RAM property to a source stream """

        if order is None:
            order = list(reversed(range(len(shape))))

        pattern = self._to_pattern(shape, order)
        return self.set_source_pattern(fsm, name, ram, offset, pattern, port)

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

        prefix = self._prefix(name)

        fsm_id = self.fsm_id_count
        fsm_name = '_%s_fsm_%d' % (prefix, fsm_id)
        sink_fsm = FSM(self.module, fsm_name, self.clock, self.reset)
        self.fsm_id_map[fsm_id] = sink_fsm
        self.fsm_id_count += 1

        sink_offset = self.module.Reg('_%s_offset_%d' % (prefix, fsm_id),
                                      ram.addrwidth, initval=0)
        sink_size = self.module.Reg('_%s_size_%d' % (prefix, fsm_id),
                                    ram.addrwidth + 1, initval=0)
        sink_stride = self.module.Reg('_%s_stride_%d' % (prefix, fsm_id),
                                      ram.addrwidth, initval=0)
        sink_count = self.module.Reg('_%s_count_%d' % (prefix, fsm_id),
                                     ram.addrwidth + 1, initval=0)

        var_id = self.var_name_id_map[name]
        fsm_sel = self.var_id_fsm_sel_map[var_id]

        set_cond = (fsm.state == fsm.current)

        sink_fsm.If(set_cond)(
            sink_offset(offset),
            sink_size(size),
            sink_stride(stride)
        )
        self.seq.If(set_cond)(
            fsm_sel(fsm_id)
        )

        sink_start = vtypes.Ands(
            self.start, fsm_sel == fsm_id, sink_size > 0)

        sink_fsm.If(sink_start)(
            sink_count(sink_size)
        )
        sink_fsm.If(sink_start).goto_next()

        num_wdelay = self._write_delay()

        for i in range(num_wdelay):
            sink_fsm.goto_next()

        waddr = self.module.Reg('_%s_waddr_%d' % (prefix, fsm_id),
                                ram.addrwidth, initval=0)
        wenable = self.module.Reg('_%s_wenable_%d' % (prefix, fsm_id),
                                  initval=0)
        wdata = self.module.Reg('_%s_wdata_%d' % (prefix, fsm_id),
                                ram.datawidth, initval=0, signed=True)
        rdata = var.read()

        ram.write_rtl(waddr, wdata, port=port, cond=wenable)

        if name in self.sink_when_map:
            when = self.sink_when_map[name]
            wcond = when.read()
        else:
            wcond = None

        sink_fsm.If(wcond)(
            waddr(sink_offset),
            wdata(rdata),
            wenable(1),
            sink_count.dec()
        )
        sink_fsm.Delay(1)(
            wenable(0)
        )
        sink_fsm.If(wcond, sink_count == 1).goto_init()
        sink_fsm.If(wcond, sink_count > 1).goto_next()

        sink_fsm.If(wcond)(
            waddr.add(sink_stride),
            wdata(rdata),
            wenable(1),
            sink_count.dec()
        )
        sink_fsm.Delay(1)(
            wenable(0)
        )
        sink_fsm.If(wcond, sink_count == 1).goto_init()

        sink_fsm._set_index(0)

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

        prefix = self._prefix(name)

        fsm_id = self.fsm_id_count
        fsm_name = '_%s_fsm_%d' % (prefix, fsm_id)
        sink_fsm = FSM(self.module, fsm_name, self.clock, self.reset)
        self.fsm_id_map[fsm_id] = sink_fsm
        self.fsm_id_count += 1

        sink_offset = self.module.Reg('_%s_offset_%d' % (prefix, fsm_id),
                                      ram.addrwidth, initval=0)
        sink_pat_offsets = [self.module.Reg('_%s_pat_offset_%d_%d' % (prefix, fsm_id, i),
                                            ram.addrwidth, initval=0)
                            for i, _ in enumerate(pattern)]
        sink_pat_sizes = [self.module.Reg('_%s_pat_size_%d_%d' % (prefix, fsm_id, i),
                                          ram.addrwidth + 1, initval=0)
                          for i, _ in enumerate(pattern)]
        sink_pat_strides = [self.module.Reg('_%s_pat_stride_%d_%d' % (prefix, fsm_id, i),
                                            ram.addrwidth, initval=0)
                            for i, _ in enumerate(pattern)]
        sink_pat_counts = [self.module.Reg('_%s_pat_count_%d_%d' % (prefix, fsm_id, i),
                                           ram.addrwidth + 1, initval=0)
                           for i, _ in enumerate(pattern)]

        var_id = self.var_name_id_map[name]
        fsm_sel = self.var_id_fsm_sel_map[var_id]

        set_cond = (fsm.state == fsm.current)

        sink_fsm.If(set_cond)(
            sink_offset(offset)
        )
        self.seq.If(set_cond)(
            fsm_sel(fsm_id)
        )

        for sink_pat_offset in sink_pat_offsets:
            sink_fsm.If(set_cond)(
                sink_pat_offset(0)
            )

        for (sink_pat_size, sink_pat_stride, (size, stride)) in zip(
                sink_pat_sizes, sink_pat_strides, pattern):
            sink_fsm.If(set_cond)(
                sink_pat_size(size),
                sink_pat_stride(stride)
            )

        sink_start = vtypes.Ands(self.start, fsm_sel == fsm_id)
        for sink_pat_size in sink_pat_sizes:
            sink_start = vtypes.Ands(sink_start, sink_pat_size > 0)

        for (sink_pat_size, sink_pat_count) in zip(
                sink_pat_sizes, sink_pat_counts):
            sink_fsm.If(sink_start)(
                sink_pat_count(sink_pat_size - 1)
            )

        sink_fsm.If(sink_start).goto_next()

        num_wdelay = self._write_delay()

        for i in range(num_wdelay):
            sink_fsm.goto_next()

        sink_all_offset = self.module.Wire('_%s_all_offset_%d' % (prefix, fsm_id),
                                           ram.addrwidth)
        sink_all_offset_val = sink_offset
        for sink_pat_offset in sink_pat_offsets:
            sink_all_offset_val += sink_pat_offset
        sink_all_offset.assign(sink_all_offset_val)

        waddr = self.module.Reg('_%s_waddr_%d' % (prefix, fsm_id),
                                ram.addrwidth, initval=0)
        wenable = self.module.Reg('_%s_wenable_%d' % (prefix, fsm_id),
                                  initval=0)
        wdata = self.module.Reg('_%s_wdata_%d' % (prefix, fsm_id),
                                ram.datawidth, initval=0, signed=True)
        rdata = var.read()

        ram.write_rtl(waddr, wdata, port=port, cond=wenable)

        if name in self.sink_when_map:
            when = self.sink_when_map[name]
            wcond = when.read()
        else:
            wcond = None

        sink_fsm.If(wcond)(
            waddr(sink_all_offset),
            wdata(rdata),
            wenable(1)
        )
        sink_fsm.Delay(1)(
            wenable(0)
        )

        upcond = None

        for (sink_pat_offset, sink_pat_size,
             sink_pat_stride, sink_pat_count) in zip(
                 sink_pat_offsets, sink_pat_sizes,
                 sink_pat_strides, sink_pat_counts):
            sink_fsm.If(upcond)(
                sink_pat_offset.add(sink_pat_stride),
                sink_pat_count.dec()
            )
            reset_cond = sink_pat_count == 0
            sink_fsm.If(upcond, reset_cond)(
                sink_pat_offset(0),
                sink_pat_count(sink_pat_size - 1)
            )
            upcond = make_condition(upcond, reset_cond)

        fin_cond = upcond

        sink_fsm.If(fin_cond).goto_init()

        sink_fsm._set_index(0)

        fsm.goto_next()

    def set_sink_multidim(self, fsm, name, ram, offset, shape, order=None, port=0):
        """ intrinsic method to assign RAM property to a sink stream """

        if order is None:
            order = list(reversed(range(len(shape))))

        pattern = self._to_pattern(shape, order)
        return self.set_sink_pattern(fsm, name, ram, offset, pattern, port)

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

        prefix = self._prefix(name)

        fsm_id = self.fsm_id_count
        fsm_name = '_%s_fsm_%d' % (prefix, fsm_id)
        sink_fsm = None
        self.fsm_id_map[fsm_id] = sink_fsm
        self.fsm_id_count += 1

        var_id = self.var_name_id_map[name]
        fsm_sel = self.var_id_fsm_sel_map[var_id]

        set_cond = (fsm.state == fsm.current)

        self.seq.If(set_cond)(
            fsm_sel(fsm_id)
        )

        fsm.goto_next()

    def set_constant(self, fsm, name, value):
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

        set_cond = (fsm.state == fsm.current)

        wdata = value
        wenable = set_cond
        var.write(wdata, wenable)

        fsm.goto_next()

    def run(self, fsm):
        # entry point
        self.fsm._set_index(0)

        start_flag = (fsm.state == fsm.current)

        self.fsm.If(start_flag)(
            self.start(1),
            self.busy(1)
        )
        self.fsm.If(start_flag).Delay(1)(
            self.start(0)
        )

        if self.reduce_reset is not None:
            self.fsm.If(start_flag).Delay(self.ram_delay + 1)(
                self.reduce_reset(0)
            )

        substreams = self._collect_substreams()

        for sub in substreams:
            reset_delay = self.ram_delay + 1 + sub.start_stage
            if sub.substrm.reduce_reset is not None:
                self.fsm.If(start_flag).Delay(reset_delay)(
                    sub.substrm.reduce_reset(0)
                )

            for cond in sub.conds.values():
                self.fsm.If(start_flag)(
                    cond(1)
                )

        self.fsm.If(start_flag).goto_next()

        # after started
        if self.fsm_synthesized:
            fsm.goto_next()
            return

        self.fsm_synthesized = True

        self.fsm.goto_next()

        done_cond = None
        for key, source_idle in sorted(self.source_idle_map.items(),
                                       key=lambda x: x[0]):
            done_cond = make_condition(done_cond, source_idle)

        done = self.module.Wire('_%s_done' % self.name)
        done.assign(done_cond)
        self.fsm.If(done).goto_next()

        depth = self.pipeline_depth()
        num_wdelay = self._write_delay()

        # pipeline delay
        for i in range(depth):
            self.fsm.goto_next()

        self.fsm.goto_next()

        # reset accumulate pipelines
        if self.reduce_reset is not None:
            self.fsm(
                self.reduce_reset(1)
            )

        for sub in substreams:
            reset_delay = sub.start_stage
            if sub.substrm.reduce_reset is not None:
                self.fsm(
                    sub.substrm.reduce_reset(1)
                )

            for cond in sub.conds.values():
                self.fsm(
                    cond(0)
                )

        for i in range(num_wdelay - depth - 1):
            self.fsm.goto_next()

        # finish
        self.fsm(
            self.busy(0)
        )

        self.fsm.goto_init()

        fsm.goto_next()

        return 0

    def join(self, fsm):
        fsm.If(vtypes.Not(self.busy)).goto_next()
        return 0

    def done(self, fsm):
        return vtypes.Not(self.busy)

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
        return pattern

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

        if callable(f) and f.__name__.startswith('Reduce'):
            if self.reduce_reset is None:
                self.reduce_reset = self.module.Reg(
                    '_'.join(['', self.name, 'reduce_reset']), initval=1)
                self.reduce_reset_var = self.Variable(
                    self.reduce_reset, width=1)

            return functools.partial(f, reset=self.reduce_reset_var)

        return f


class Substream(BaseSubstream):

    def __init__(self, module, clock, reset, substrm):
        self.module = module
        self.clock = clock
        self.reset = reset
        BaseSubstream.__init__(self, substrm)

    def to_source(self, name, data):
        source_name = self.substrm._dataname(name)
        cond = self.module.Reg(compiler._tmp_name(self.name('%s_cond' % source_name)),
                               initval=0)
        BaseSubstream.write(self, source_name, data, cond)

    def from_sink(self, name):
        sink_name = self.substrm._dataname(name)
        return BaseSubstream.read(self, sink_name)

    def _collect_substreams(self):
        ret = []
        ret.append(self)
        ret.extend(self.substrm._collect_substreams())
        return ret
