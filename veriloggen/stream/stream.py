from __future__ import absolute_import
from __future__ import print_function
import os
import sys
import copy
import collections
import functools

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
                  no_hook=False):
    return Stream(module=module, clock=clock, reset=reset,
                  ivalid=ivalid, iready=iready,
                  ovalid=ovalid, oready=oready,
                  no_hook=no_hook)


class Stream(object):

    def __init__(self, *nodes, **opts):
        # ID for manager reuse and merge
        global _stream_counter
        self.object_id = _stream_counter
        _stream_counter += 1

        self.nodes = set(nodes)
        self.max_stage = None
        self.last_input = None
        self.last_output = None

        self.module = opts['module'] if 'module' in opts else None
        self.clock = opts['clock'] if 'clock' in opts else None
        self.reset = opts['reset'] if 'reset' in opts else None

        self.ivalid = opts['ivalid'] if 'ivalid' in opts else None
        self.iready = opts['iready'] if 'iready' in opts else None
        self.ovalid = opts['ovalid'] if 'ovalid' in opts else None
        self.oready = opts['oready'] if 'oready' in opts else None

        self.seq = None

        self.has_control = False

        if (self.module is not None and
                self.clock is not None and self.reset is not None):

            no_hook = opts['no_hook'] if 'no_hook' in opts else False
            if not no_hook:
                self.module.add_hook(self.implement)

            seq_name = (('_stream_seq_%d' % self.object_id) if 'seq_name' not in opts else
                        opts['seq_name'])
            self.seq = Seq(self.module, seq_name, self.clock, self.reset)

            self.add_control(aswire=True)
            self.has_control = True

    #-------------------------------------------------------------------------
    def add(self, *nodes):
        self.nodes.update(set(nodes))

    #-------------------------------------------------------------------------
    def to_module(self, name, clock='CLK', reset='RST'):
        """ generate a Module definion """

        m = Module(name)
        clk = m.Input(clock)
        rst = m.Input(reset)

        m = self.implement(m, clk, rst, aswire=False)

        return m

    #-------------------------------------------------------------------------
    def implement(self, m=None, clock=None, reset=None, seq_name=None, aswire=True):
        """ implemente actual registers and operations in Verilog """

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
        max_stage = None
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

        return m

    #-------------------------------------------------------------------------
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

    #-------------------------------------------------------------------------
    def draw_graph(self, filename='out.png', prog='dot', rankdir='LR', approx=False):
        if self.last_output is None:
            self.to_module()

        graph.draw_graph(self.last_output, filename=filename, prog=prog,
                         rankdir=rankdir, approx=approx)

    def enable_draw_graph(self, filename='out.png', prog='dot', rankdir='LR', approx=False):
        self.module.add_hook(self.draw_graph,
                             kwargs={'filename': filename, 'prog': prog,
                                     'rankdir': rankdir, 'approx': approx})

    #-------------------------------------------------------------------------
    def get_input(self):
        if self.last_input is None:
            return collections.OrderedDict()

        ret = collections.OrderedDict()
        for input_var in sorted(self.last_input, key=lambda x: x.object_id):
            key = str(input_var.input_data)
            value = input_var
            ret[key] = value

        return ret

    def get_output(self):
        if self.last_output is None:
            return collections.OrderedDict()

        ret = collections.OrderedDict()
        for output_var in sorted(self.last_output, key=lambda x: x.object_id):
            key = str(output_var.output_data)
            value = output_var
            ret[key] = value

        return ret

    #-------------------------------------------------------------------------
    def pipeline_depth(self):
        return self.max_stage

    #-------------------------------------------------------------------------
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
