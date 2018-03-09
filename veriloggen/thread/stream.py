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
from veriloggen.stream.stream import Stream as BaseStream
from veriloggen.stream.stypes import Substream as BaseSubstream

from . import compiler
from . import thread


def TmpStream(m, clk, rst, datawidth=32, ram_sel_width=16, fsm_as_module=False):
    name = compiler._tmp_name('_tmp_stream')
    return Stream(m, name, clk, rst, datawidth, ram_sel_width, fsm_as_module=False)


class Stream(BaseStream):
    __intrinsics__ = ('set_source', 'set_source_pattern', 'set_source_multidim',
                      'set_sink', 'set_sink_pattern', 'set_sink_multidim',
                      'set_sink_empty', 'set_constant',
                      'run', 'join', 'done')

    def __init__(self, m, name, clk, rst, datawidth=32, addrwidth=32,
                 ram_sel_width=16, count_width=16,
                 fsm_as_module=False):

        BaseStream.__init__(self, module=m, clock=clk, reset=rst,
                            no_hook=True)

        self.name = name
        self.datawidth = datawidth
        self.addrwidth = addrwidth
        self.ram_sel_width = ram_sel_width
        self.count_width = count_width
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
        self.busy = self.module.Reg(
            '_'.join(['', self.name, 'busy']), initval=0)
        self.sink_wait_count = self.module.Reg(
            '_'.join(['', self.name, 'sink_wait_count']),
            self.count_width, initval=0)

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

        self.ram_delay = 3

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

        var.source_idle = self.module.Reg('_%s_idle' % prefix, initval=1)
        self.source_idle_map[name] = var.source_idle

        var.source_offset = self.module.Reg('_source_%s_offset' % prefix,
                                            self.addrwidth, initval=0)
        var.source_size = self.module.Reg('_source_%s_size' % prefix,
                                          self.addrwidth + 1, initval=0)
        var.source_stride = self.module.Reg('_source_%s_stride' % prefix,
                                            self.addrwidth, initval=0)
        var.source_count = self.module.Reg('_source_%s_count' % prefix,
                                           self.addrwidth + 1, initval=0)

        var.source_pat_sizes = []
        var.source_pat_strides = []
        var.source_pat_counts = []

        var.source_ram_id_map = OrderedDict()
        var.source_ram_sel = self.module.Reg('_source_%s_ram_sel' % prefix,
                                             self.ram_sel_width, initval=0)
        var.source_ram_raddr = self.module.Reg('_source_%s_ram_raddr' % prefix,
                                               self.addrwidth, initval=0)
        var.source_ram_renable = self.module.Reg('_source_%s_ram_renable' % prefix,
                                                 initval=0)
        var.source_ram_rdata = self.module.Wire('_source_%s_ram_rdata' % prefix,
                                                self.datawidth)
        var.source_ram_rvalid = self.module.Reg('_source_%s_ram_rvalid' % prefix,
                                                initval=0)

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

        data.sink_offset = self.module.Reg('_sink_%s_offset' % prefix,
                                           self.addrwidth, initval=0)
        data.sink_size = self.module.Reg('_sink_%s_size' % prefix,
                                         self.addrwidth + 1, initval=0)
        data.sink_stride = self.module.Reg('_sink_%s_stride' % prefix,
                                           self.addrwidth, initval=0)
        data.sink_count = self.module.Reg('_sink_%s_count' % prefix,
                                          self.addrwidth + 1, initval=0)

        data.sink_pat_sizes = []
        data.sink_pat_strides = []
        data.sink_pat_counts = []

        data.sink_ram_id_map = OrderedDict()
        data.sink_ram_sel = self.module.Reg('_sink_%s_ram_sel' % prefix,
                                            self.ram_sel_width, initval=0)
        data.sink_waddr = self.module.Reg('_sink_%s_waddr' % prefix,
                                          self.addrwidth, initval=0)
        data.sink_wenable = self.module.Reg('_sink_%s_wenable' % prefix,
                                            initval=0)
        data.sink_wdata = self.module.Reg('_sink_%s_wdata' % prefix,
                                          self.datawidth, initval=0)

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

        source_offset = var.source_offset
        source_size = var.source_size
        source_stride = var.source_stride
        source_count = var.source_count

        set_cond = (fsm.state == fsm.current)

        self.seq.If(set_cond)(
            source_offset(offset),
            source_size(size),
            source_stride(stride)
        )

        raddr = var.source_ram_raddr
        renable = var.source_ram_renable
        rdata = var.source_ram_rdata
        rvalid = var.source_ram_rvalid

        if ram._id() not in var.source_ram_id_map:
            ram_sel = var.source_ram_sel

            if ram._id() not in self.ram_id_map:
                ram_id = self.ram_id_count
                self.ram_id_count += 1
                self.ram_id_map[ram._id()] = ram_id
            else:
                ram_id = self.ram_id_map[ram._id()]

            self.seq.If(set_cond)(
                ram_sel(ram_id)
            )

            ram_cond = (ram_sel == ram_id)

            d, v = ram.read_rtl(raddr, port=port, cond=renable)
            add_mux(rdata, ram_cond, d)

        # if FSM is already synthesized, skip below
        if var.source_fsm is not None:
            fsm.goto_next()
            return

        # synthesize a new FSM
        source_idle = var.source_idle

        self.seq.If(self.start)(
            source_idle(0)
        )

        self.seq(
            rvalid(self.seq.Prev(vtypes.Ands(renable, ram_cond), 1))
        )

        prefix = self._prefix(name)
        fsm_id = self.fsm_id_count
        self.fsm_id_count += 1

        fsm_name = '_%s_fsm_%d' % (prefix, fsm_id)
        var.source_fsm = FSM(self.module, fsm_name, self.clock, self.reset,
                             as_module=self.fsm_as_module)
        source_fsm = var.source_fsm

        source_start = vtypes.Ands(self.start, source_size > 0)

        source_fsm.If(source_start)(
            raddr(source_offset),
            renable(1),
            source_count(source_size)
        )
        source_fsm.If(source_start).goto_next()

        wdata = rdata
        wenable = rvalid
        var.write(wdata, wenable)

        source_fsm(
            raddr.add(source_stride),
            renable(1),
            source_count.dec()
        )
        source_fsm.If(source_count == 1)(
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

        raise NotImplementedError('not upgraded.')

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
        source_fsm = FSM(self.module, fsm_name, self.clock, self.reset,
                         as_module=self.fsm_as_module)
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

        sink_offset = var.sink_offset
        sink_size = var.sink_size
        sink_stride = var.sink_stride
        sink_count = var.sink_count

        set_cond = (fsm.state == fsm.current)

        self.seq.If(set_cond)(
            sink_offset(offset),
            sink_size(size),
            sink_stride(stride)
        )

        waddr = var.sink_waddr
        wenable = var.sink_wenable
        wdata = var.sink_wdata
        rdata = var.read()

        if ram._id() not in var.sink_ram_id_map:
            ram_sel = var.sink_ram_sel

            if ram._id() not in self.ram_id_map:
                ram_id = self.ram_id_count
                self.ram_id_count += 1
                self.ram_id_map[ram._id()] = ram_id
            else:
                ram_id = self.ram_id_map[ram._id()]

            var.sink_ram_id_map[ram._id()] = ram_id

            self.seq.If(set_cond)(
                ram_sel(ram_id)
            )

            ram_cond = (ram_sel == ram_id)
            ram_wenable = vtypes.Ands(wenable, ram_cond)
            ram.write_rtl(waddr, wdata, port=port, cond=wenable)

        # if FSM is already synthesized, skip below
        if var.sink_fsm is not None:
            fsm.goto_next()
            return

        # synthesize a new FSM
        prefix = self._prefix(name)
        fsm_id = self.fsm_id_count
        self.fsm_id_count += 1

        fsm_name = '_%s_fsm_%d' % (prefix, fsm_id)
        var.sink_fsm = FSM(self.module, fsm_name, self.clock, self.reset,
                           as_module=self.fsm_as_module)
        sink_fsm = var.sink_fsm

        sink_fsm.seq(
            wenable(0)
        )

        sink_start = vtypes.Ands(self.start, sink_size > 0)

        sink_fsm.If(sink_start)(
            waddr(sink_offset - sink_stride),
            sink_count(sink_size),
        )
        sink_fsm.If(sink_start).goto_next()

        sink_fsm.If(self.sink_wait_count == 0).goto_next()

        if name in self.sink_when_map:
            when = self.sink_when_map[name]
            wcond = when.read()
        else:
            wcond = None

        sink_fsm.If(wcond)(
            waddr.add(sink_stride),
            wdata(rdata),
            wenable(1),
            sink_count.dec()
        )
        sink_fsm.If(wcond, sink_count == 1).goto_init()

        sink_fsm._set_index(0)

        fsm.goto_next()

    def set_sink_pattern(self, fsm, name, ram, offset, pattern, port=0):
        """ intrinsic method to assign RAM property to a sink stream """

        raise NotImplementedError('not upgraded.')

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
        sink_fsm = FSM(self.module, fsm_name, self.clock, self.reset,
                       as_module=self.fsm_as_module)
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

        set_cond = (fsm.state == fsm.current)

        ram_sel = var.sink_ram_sel

        self.seq.If(set_cond)(
            ram_sel(0)  # '0' is reserved for empty
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

        cond = (fsm.state == fsm.current)
        add_mux(self.start_flag, cond, 1)

        # after started
        if self.fsm_synthesized:
            fsm.goto_next()
            return

        self.fsm_synthesized = True

        num_wdelay = self._write_delay()

        self.fsm.seq.If(self.start_flag)(
            self.sink_wait_count(num_wdelay)
        )
        self.fsm.seq.If(self.sink_wait_count > 0)(
            self.sink_wait_count.dec()
        )

        self.fsm.If(self.start_flag)(
            self.start(1),
            self.busy(1)
        )

        if self.reduce_reset is not None:
            self.fsm.seq.If(self.seq.Prev(self.start_flag, self.ram_delay + 1))(
                self.reduce_reset(0)
            )

        substreams = self._collect_substreams()

        for sub in substreams:
            reset_delay = self.ram_delay + 1 + sub.start_stage + sub.reset_delay
            sub_fsm = sub.substrm.fsm
            sub_fsm._set_index(0)

            if sub.substrm.reduce_reset is not None:
                sub_fsm.seq.If(self.seq.Prev(self.start_flag, reset_delay))(
                    sub.substrm.reduce_reset(0)
                )

            for cond in sub.conds.values():
                sub_fsm.If(self.start_flag)(
                    cond(1)
                )

        self.fsm.If(self.start_flag).goto_next()

        self.fsm(
            self.start(0)
        )
        self.fsm.goto_next()

        done_cond = None
        for key, source_idle in sorted(self.source_idle_map.items(),
                                       key=lambda x: x[0]):
            done_cond = make_condition(done_cond, source_idle)

        done = self.module.Wire('_%s_done' % self.name)
        done.assign(done_cond)

        pipe_count = self.module.Reg('_%s_pipe_count' % self.name,
                                     self.count_width, initval=0)

        depth = self.pipeline_depth()

        self.fsm.If(done)(
            pipe_count(depth)
        )
        self.fsm.If(done).goto_next()

        self.fsm.If(pipe_count > 0)(
            pipe_count.dec()
        )
        self.fsm.If(pipe_count == 0).goto_next()

        self.fsm.goto_next()

        # reset accumulate pipelines
        if self.reduce_reset is not None:
            self.fsm(
                self.reduce_reset(1)
            )

        end_flag = self.fsm.state == self.fsm.current

        for sub in substreams:
            sub_fsm = sub.substrm.fsm
            sub_fsm._set_index(0)
            if sub.substrm.reduce_reset is not None:
                sub_fsm.If(end_flag)(
                    sub.substrm.reduce_reset(1)
                )

            for cond in sub.conds.values():
                sub_fsm.If(end_flag)(
                    cond(0)
                )

        self.fsm.goto_next()

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
            s.reset_delay += 1
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
