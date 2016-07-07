from __future__ import absolute_import
from __future__ import print_function
import os
import sys
import copy
import collections

import veriloggen.core.vtypes as vtypes
from veriloggen.core.module import Module
from veriloggen.seq.seq import Seq

from . import visitor
from . import dtypes
from . import mul
from . import scheduler
from . import allocator
from . import graph


def DataflowManager(module, clock, reset):
    return Dataflow(module=module, clock=clock, reset=reset)


class Dataflow(object):

    def __init__(self, *nodes, **opts):
        self.nodes = set(nodes)
        self.max_stage = None
        self.last_input = None
        self.last_output = None

        self.module = opts['module'] if 'module' in opts else None
        self.clock = opts['clock'] if 'clock' in opts else None
        self.reset = opts['reset'] if 'reset' in opts else None

        if (self.module is not None and
                self.clock is not None and self.reset is not None):
            self.module.add_hook(self.implement,
                                 args=(self.module, self.clock, self.reset))

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
    def implement(self, m, clock, reset, seq_name='seq', aswire=True):
        """ implemente actual registers and operations in Verilog """

        mul.reset()

        seq = Seq(m, seq_name, clock, reset)

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
        max_stage = None
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
            var._set_seq(seq)

        # add output ports
        for output_var in sorted(output_vars, key=lambda x: x.object_id):
            output_var._implement_output(m, seq, aswire)

        # save schedule result
        self.last_input = input_vars
        self.last_output = output_vars

        return m

    #-------------------------------------------------------------------------
    def draw_graph(self, filename='out.png', prog='dot', rankdir='LR', approx=False):
        if self.last_output is None:
            self.to_module()

        graph.draw_graph(self.last_output, filename=filename, prog=prog,
                         rankdir=rankdir, approx=approx)

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
        func = getattr(dtypes, attr)

        def wrapper(*args, **kwargs):
            v = func(*args, **kwargs)
            if isinstance(v, dtypes._Numeric):
                self.add(v)
            return v

        return wrapper
