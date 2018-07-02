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
from . import dtypes
from . import mul
from . import scheduler
from . import allocator
from . import graph


# ID counter for 'Dataflow'
_dataflow_counter = 0


def reset():
    global _dataflow_counter
    _dataflow_counter = 0
    dtypes._object_counter = 0
    mul.reset()


def DataflowManager(module, clock, reset,
                    aswire=True, no_hook=False):
    return Dataflow(module=module, clock=clock, reset=reset,
                    aswire=aswire, no_hook=no_hook)


class Dataflow(object):

    def __init__(self, *nodes, **opts):
        # ID for manager reuse and merge
        global _dataflow_counter
        self.object_id = _dataflow_counter
        _dataflow_counter += 1

        self.nodes = set(nodes)
        self.max_stage = 0
        self.last_input = None
        self.last_output = None

        self.module = opts['module'] if 'module' in opts else None
        self.clock = opts['clock'] if 'clock' in opts else None
        self.reset = opts['reset'] if 'reset' in opts else None

        self.aswire = opts['aswire'] if 'aswire' in opts else True

        self.seq = None

        if (self.module is not None and
                self.clock is not None and self.reset is not None):

            no_hook = opts['no_hook'] if 'no_hook' in opts else False
            if not no_hook:
                self.module.add_hook(self.implement)

            seq_name = (opts['seq_name'] if 'seq_name' in opts else
                        '_dataflow_seq_%d' % self.object_id)
            self.seq = Seq(self.module, seq_name, self.clock, self.reset)

    # -------------------------------------------------------------------------
    def add(self, *nodes):
        self.nodes.update(set(nodes))

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

        if m is None:
            m = self.module

        if clock is None:
            clock = self.clock

        if reset is None:
            reset = self.reset

        if self.seq is None or self.seq.done:
            if seq_name is None:
                seq_name = '_dataflow_seq_%d' % self.object_id
            seq = Seq(m, seq_name, clock, reset)
        else:
            seq = self.seq

        if aswire is None:
            aswire = self.aswire

        # for mult and div
        m._clock = clock
        m._reset = reset

        dataflow_nodes = self.nodes

        input_visitor = visitor.InputVisitor()
        input_vars = set()
        for node in sorted(dataflow_nodes, key=lambda x: x.object_id):
            input_vars.update(input_visitor.visit(node))

        output_visitor = visitor.OutputVisitor()
        output_vars = set()
        for node in sorted(dataflow_nodes, key=lambda x: x.object_id):
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
            max_stage = dtypes._max(max_stage, output_var.end_stage)
        self.max_stage = max_stage

        output_vars = sched.balance_output(output_vars, max_stage)

        # get all vars
        all_visitor = visitor.AllVisitor()
        all_vars = set()
        for output_var in sorted(output_vars, key=lambda x: x.object_id):
            all_vars.update(all_visitor.visit(output_var))

        # allocate (implement signals)
        alloc = allocator.Allocator()
        alloc.allocate(m, seq, all_vars)

        # set default module information
        for var in sorted(all_vars, key=lambda x: x.object_id):
            var._set_module(m)
            var._set_df(self)

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

    # -------------------------------------------------------------------------
    def pipeline_depth(self):
        return self.max_stage

    # -------------------------------------------------------------------------
    def __getattr__(self, attr):
        try:
            return object.__getattr__(self, attr)

        except AttributeError as e:
            if attr.startswith('__') or attr not in dir(dtypes):
                raise e

            func = getattr(dtypes, attr)

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
        if isinstance(v, dtypes._Numeric):
            v._set_module(self.module)
            v._set_df(self)
            v._set_seq(self.seq)
