from __future__ import absolute_import
from __future__ import print_function

import os
import sys
import math
import copy
import functools
from collections import OrderedDict

import veriloggen.core.vtypes as vtypes
from veriloggen.core.module import Module
from veriloggen.seq.seq import Seq

from . import visitor
from . import stypes
from . import mul
from . import scheduler
from . import allocator
from . import graph


# ID counter for 'Stream'
_stream_counter = 0


def reset():
    global _stream_counter
    _stream_counter = 0
    stypes._object_counter = 0
    mul.reset()


def StreamManager(module, clock, reset,
                  ivalid=None, iready=None,
                  ovalid=None, oready=None,
                  aswire=True, no_hook=False):
    return Stream(module=module, clock=clock, reset=reset,
                  ivalid=ivalid, iready=iready,
                  ovalid=ovalid, oready=oready,
                  aswire=aswire, no_hook=no_hook)


class Stream(object):

    def __init__(self, *nodes, **opts):
        # ID for manager reuse and merge
        global _stream_counter
        self.object_id = _stream_counter
        _stream_counter += 1

        self.nodes = set()
        self.named_numerics = OrderedDict()

        self.add(*nodes)

        self.max_stage = 0
        self.last_input = None
        self.last_output = None

        self.module = opts['module'] if 'module' in opts else None
        self.clock = opts['clock'] if 'clock' in opts else None
        self.reset = opts['reset'] if 'reset' in opts else None

        self.ivalid = opts['ivalid'] if 'ivalid' in opts else None
        self.iready = opts['iready'] if 'iready' in opts else None
        self.ovalid = opts['ovalid'] if 'ovalid' in opts else None
        self.oready = opts['oready'] if 'oready' in opts else None

        self.aswire = opts['aswire'] if 'aswire' in opts else True
        self.dump = opts['dump'] if 'dump' in opts else False
        self.dump_base = opts['dump_base'] if 'dump_base' in opts else 10
        self.dump_mode = opts['dump_mode'] if 'dump_mode' in opts else 'all'

        self.seq = None
        self.has_control = False

        self.implemented = False

        if (self.module is not None and
                self.clock is not None and self.reset is not None):

            no_hook = opts['no_hook'] if 'no_hook' in opts else False
            if not no_hook:
                self.module.add_hook(self.implement)

            seq_name = (opts['seq_name'] if 'seq_name' in opts else
                        '_stream_seq_%d' % self.object_id)
            self.seq = Seq(self.module, seq_name, self.clock, self.reset)

    # -------------------------------------------------------------------------
    def add(self, *nodes):
        self.nodes.update(set(nodes))

        for node in nodes:
            if hasattr(node, 'input_data'):
                if isinstance(node.input_data, str):
                    name = node.input_data
                else:
                    name = node.input_data.name
                self.named_numerics[name] = node

            elif hasattr(node, 'output_data'):
                if node.output_data is None:
                    continue
                if isinstance(node.output_data, str):
                    name = node.output_data
                else:
                    name = node.output_data.name
                self.named_numerics[name] = node

    # -------------------------------------------------------------------------
    def to_module(self, name, clock='CLK', reset='RST', aswire=False, seq_name=None):
        """ generate a Module definion """

        m = Module(name)
        clk = m.Input(clock)
        rst = m.Input(reset)

        m = self.implement(m, clk, rst, aswire=aswire, seq_name=seq_name)

        return m

    # -------------------------------------------------------------------------
    def implement(self, m=None, clock=None, reset=None, aswire=None, seq_name=None):
        """ implemente actual registers and operations in Verilog """

        if self.implemented:
            if m is None:
                return self.module
            raise ValueError('already implemented.')

        self.implemented = True

        if m is None:
            m = self.module

        if self.module is None:
            self.module = m

        if clock is None:
            clock = self.clock

        if reset is None:
            reset = self.reset

        if self.seq is None:
            if seq_name is None:
                seq_name = '_stream_seq_%d' % self.object_id
            seq = Seq(m, seq_name, clock, reset)
        else:
            seq = self.seq

        if aswire is None:
            aswire = self.aswire

        self.add_control(aswire=aswire)
        self.has_control = True

        # for mult and div
        m._clock = clock
        m._reset = reset

        stream_nodes = self.nodes

        input_visitor = visitor.InputVisitor()
        input_vars = set()
        for node in sorted(stream_nodes, key=lambda x: x.object_id):
            input_vars.update(input_visitor.visit(node))

        output_visitor = visitor.OutputVisitor()
        output_vars = set()
        for node in sorted(stream_nodes, key=lambda x: x.object_id):
            output_vars.update(output_visitor.visit(node))

        # add input ports
        for input_var in sorted(input_vars, key=lambda x: x.object_id):
            input_var._implement_input(m, seq, aswire)

        # schedule
        sched = scheduler.ASAPScheduler()
        sched.schedule(output_vars)

        # balance output stage depth
        max_stage = 0
        for output_var in sorted(output_vars, key=lambda x: x.object_id):
            max_stage = stypes._max(max_stage, output_var.end_stage)
        self.max_stage = max_stage

        output_vars = sched.balance_output(output_vars, max_stage)

        # get all vars
        all_visitor = visitor.AllVisitor()
        all_vars = set()
        for output_var in sorted(output_vars, key=lambda x: x.object_id):
            all_vars.update(all_visitor.visit(output_var))

        # control (valid and ready)
        if not self.has_control:
            self.add_control(aswire)

        self.implement_control(seq)

        # allocate (implement signals)
        alloc = allocator.Allocator()
        alloc.allocate(m, seq, all_vars, self.valid_list, self.senable)

        # set default module information
        for var in sorted(all_vars, key=lambda x: x.object_id):
            var._set_module(m)
            var._set_strm(self)

            if var.seq is not None:
                seq.update(var.seq)

            var._set_seq(seq)

        # add output ports
        for output_var in sorted(output_vars, key=lambda x: x.object_id):
            output_var._implement_output(m, seq, aswire)

        # save schedule result
        self.last_input = input_vars
        self.last_output = output_vars

        if self.dump:
            self.add_dump(m, seq, input_vars, output_vars, all_vars)

        return m

    def add_dump(self, m, seq, input_vars, output_vars, all_vars):
        dump_enable_name = '_stream_dump_enable_%d' % self.object_id
        dump_enable = m.Reg(dump_enable_name, initval=0)
        dump_iter_name = '_stream_dump_iter_%d' % self.object_id
        dump_iter = m.Reg(dump_iter_name, 32, initval=0)

        self.dump_enable = dump_enable

        pipeline_depth = self.pipeline_depth()
        log_pipeline_depth = int(math.ceil(math.log(pipeline_depth, 10)))

        seq(
            dump_iter(0)
        )

        for i in range(pipeline_depth + 1):
            seq.If(seq.Prev(dump_enable, i))(
                dump_iter.inc()
            )

        def get_name(obj):
            if hasattr(obj, 'name'):
                return obj.name
            if isinstance(obj, vtypes._Constant):
                return obj.__class__.__name__
            raise TypeError()

        longest_name_len = 0
        for input_var in sorted(input_vars, key=lambda x: x.object_id):
            if not (self.dump_mode == 'all' or self.dump_mode == 'input' or
                    self.dump_mode == 'inout' or
                    (self.dump_mode == 'selective' and
                     hasattr(input_var, 'dump') and input_var.dump)):
                continue

            name = get_name(input_var.sig_data)
            length = len(name) + 6
            longest_name_len = max(longest_name_len, length)

        for var in sorted(all_vars, key=lambda x: (-1, x.object_id)
                          if x.end_stage is None else
                          (x.end_stage, x.object_id)):
            if not (self.dump_mode == 'all' or
                    (self.dump_mode == 'selective' and
                     hasattr(var, 'dump') and var.dump)):
                continue

            name = get_name(var.sig_data)
            length = len(name) + 6
            longest_name_len = max(longest_name_len, length)

        for output_var in sorted(output_vars, key=lambda x: x.object_id):
            if not (self.dump_mode == 'all' or self.dump_mode == 'output' or
                    self.dump_mode == 'inout' or
                    (self.dump_mode == 'selective' and
                     hasattr(output_var, 'dump') and output_var.dump)):
                continue

            name = get_name(output_var.output_sig_data)
            length = len(name) + 6
            longest_name_len = max(longest_name_len, length)

        longest_var_len = 0
        for var in sorted(all_vars, key=lambda x: (-1, x.object_id)
                          if x.start_stage is None else
                          (x.start_stage, x.object_id)):
            bit_length = var.sig_data.bit_length()
            if bit_length is None:
                bit_length = 1
            if bit_length <= 0:
                bit_length = 1

            base = (var.dump_base if hasattr(var, 'dump_base') else
                    self.dump_base)
            length = int(math.ceil(bit_length / math.log(base, 2)))
            longest_var_len = max(longest_var_len, length)

        for var in sorted(all_vars, key=lambda x: (-1, x.object_id)
                          if x.start_stage is None else
                          (x.start_stage, x.object_id)):

            base = (var.dump_base if hasattr(var, 'dump_base') else
                    self.dump_base)
            base_char = ('b' if base == 2 else
                         'o' if base == 8 else
                         'd' if base == 10 else
                         'x')
            prefix = ('0b' if base == 2 else
                      '0o' if base == 8 else
                      '  ' if base == 10 else
                      '0x')
            var.dump_fmt = ''.join(
                [prefix, '%', '%d' % (longest_var_len + 1), base_char])

        enables = []
        for input_var in sorted(input_vars, key=lambda x: x.object_id):
            if not (self.dump_mode == 'all' or self.dump_mode == 'input' or
                    self.dump_mode == 'inout' or
                    (self.dump_mode == 'selective' and
                     hasattr(input_var, 'dump') and input_var.dump)):
                continue

            vfmt = input_var.dump_fmt

            name = get_name(input_var.sig_data)
            name_alignment = ' ' * (longest_name_len - len(name) -
                                    len('(in) '))
            fmt = ''.join(['<', self.name, '> (iter %d) ',
                           '(stage %', str(log_pipeline_depth), 'd, age %d) ', '(in) ',
                           name_alignment, name, ' = ', vfmt])

            stage = input_var.end_stage if input_var.end_stage is not None else 0
            enable = seq.Prev(dump_enable, stage)
            enables.append(enable)
            age = seq.Prev(dump_iter, stage)

            seq.If(enable)(
                vtypes.Display(fmt, dump_iter, stage, age, input_var.sig_data)
            )

        for var in sorted(all_vars, key=lambda x: (-1, x.object_id)
                          if x.end_stage is None else
                          (x.end_stage, x.object_id)):
            if not (self.dump_mode == 'all' or
                    (self.dump_mode == 'selective' and
                     hasattr(var, 'dump') and var.dump)):
                continue

            vfmt = var.dump_fmt

            name = get_name(var.sig_data)
            name_alignment = ' ' * (longest_name_len - len(name))
            stage = var.end_stage if var.end_stage is not None else 0

            fmt = ''.join(['<', self.name, '> (iter %d) ',
                           '(stage %', str(log_pipeline_depth), 'd, age %d) ',
                           name_alignment, name, ' = ', vfmt])

            enable = seq.Prev(dump_enable, stage)
            enables.append(enable)
            age = seq.Prev(dump_iter, stage)

            seq.If(enable)(
                vtypes.Display(fmt, dump_iter, stage, age, var.sig_data)
            )

        for output_var in sorted(output_vars, key=lambda x: x.object_id):
            if not (self.dump_mode == 'all' or self.dump_mode == 'output' or
                    self.dump_mode == 'inout' or
                    (self.dump_mode == 'selective' and
                     hasattr(output_var, 'dump') and output_var.dump)):
                continue

            vfmt = output_var.dump_fmt

            name = get_name(output_var.output_sig_data)
            name_alignment = ' ' * (longest_name_len - len(name) -
                                    len('(out) '))
            fmt = ''.join(['<', self.name, '> (iter %d) ',
                           '(stage %', str(log_pipeline_depth), 'd, age %d) ', '(out) ',
                           name_alignment, name, ' = ', vfmt])

            stage = output_var.end_stage if output_var.end_stage is not None else 0
            enable = seq.Prev(dump_enable, stage)
            enables.append(enable)
            age = seq.Prev(dump_iter, stage)

            seq.If(enable)(
                vtypes.Display(fmt, dump_iter, stage, age,
                               output_var.output_sig_data)
            )

        if enables:
            seq.If(vtypes.Ors(*enables))(
                vtypes.Display(''.join(['<', self.name, '> (iter %d) ', '--------']),
                               dump_iter)
            )

    # -------------------------------------------------------------------------
    def add_control(self, aswire=True):
        if self.ivalid is not None and isinstance(self.ivalid, str):
            if aswire:
                self.ivalid = self.module.Wire(self.ivalid)
            else:
                self.ivalid = self.module.Input(self.ivalid)

        if self.iready is not None and isinstance(self.iready, str):
            if aswire:
                self.iready = self.module.Wire(self.iready)
            else:
                self.iready = self.module.Output(self.iready)

        if self.ovalid is not None and isinstance(self.ovalid, str):
            if aswire:
                self.ovalid = self.module.Wire(self.ovalid)
            else:
                self.ovalid = self.module.Output(self.ovalid)

        if self.oready is not None and isinstance(self.oready, str):
            if aswire:
                self.oready = self.module.Wire(self.oready)
            else:
                self.oready = self.module.Input(self.oready)

    def implement_control(self, seq):
        self.valid_list = None

        if self.ivalid is None and self.oready is None:
            if self.ovalid is not None:
                self.ovalid.assign(1)
            if self.iready is not None:
                self.iready.assign(1)
            self.senable = None
            return

        if self.oready is None:
            self._make_valid_chain(seq)
            self.senable = None
            return

        if self.ivalid is None:
            self.iready.assign(self.oready)
            self.senable = self.oready
            return

        cond = vtypes.OrList(vtypes.Not(self.ovalid), self.oready)
        self.senable = self.module.TmpWire()
        self.senable.assign(cond)

        self._make_valid_chain(seq, self.senable)
        self.iready.assign(self.senable)

    def _make_valid_chain(self, seq, cond=None):
        self.valid_list = []
        self.valid_list.append(self.ivalid)

        name = self.ivalid.name
        prev = self.ivalid

        for i in range(self.max_stage):
            v = self.module.Reg("_{}_{}".format(name, i), initval=0)
            self.valid_list.append(v)
            seq(v(prev), cond=cond)
            prev = v

        if self.ovalid is not None:
            self.ovalid.assign(prev)

    # -------------------------------------------------------------------------
    def draw_graph(self, filename='out.png', prog='dot', rankdir='LR', approx=False):
        if self.last_output is None:
            self.to_module()

        graph.draw_graph(self.last_output, filename=filename, prog=prog,
                         rankdir=rankdir, approx=approx)

    def enable_draw_graph(self, filename='out.png', prog='dot', rankdir='LR', approx=False):
        self.module.add_hook(self.draw_graph,
                             kwargs={'filename': filename, 'prog': prog,
                                     'rankdir': rankdir, 'approx': approx})

    # -------------------------------------------------------------------------
    def get_input(self):
        if self.last_input is None:
            return OrderedDict()

        ret = OrderedDict()
        for input_var in sorted(self.last_input, key=lambda x: x.object_id):
            key = str(input_var.input_data)
            value = input_var
            ret[key] = value

        return ret

    def get_output(self):
        if self.last_output is None:
            return OrderedDict()

        ret = OrderedDict()
        for output_var in sorted(self.last_output, key=lambda x: x.object_id):
            key = str(output_var.output_data)
            value = output_var
            ret[key] = value

        return ret

    # -------------------------------------------------------------------------
    def pipeline_depth(self):
        return self.max_stage

    # -------------------------------------------------------------------------
    def __getattr__(self, attr):
        try:
            return object.__getattr__(self, attr)

        except AttributeError as e:
            if attr.startswith('__') or attr not in dir(stypes):
                raise e

            func = getattr(stypes, attr)

            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                v = func(*args, **kwargs)
                if isinstance(v, (tuple, list)):
                    for item in v:
                        self._set_info(item)
                else:
                    self._set_info(v)
                return v

            return wrapper

    def _set_info(self, v):
        if isinstance(v, stypes._Numeric):
            v._set_module(self.module)
            v._set_strm(self)
            v._set_seq(self.seq)

            self.add(v)

    def get_named_numeric(self, name):
        if name not in self.named_numerics:
            raise NameError("Numeric '%s' is not defined." % name)

        return self.named_numerics[name]
