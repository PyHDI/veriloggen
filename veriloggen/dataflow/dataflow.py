from __future__ import absolute_import
from __future__ import print_function
import os
import sys
import copy

import veriloggen.core.vtypes as vtypes
from veriloggen.core.module import Module
from veriloggen.seq.seq import Seq

from . import visitor
from . import dtypes
from . import mul
from . import scheduler
from . import allocator
from . import graph

class Dataflow(object):
    def __init__(self, *nodes, **opts):
        self.datawidth = opts['datawidth'] if 'datawidth' in opts else 32
        self.nodes = set(nodes)
        self.max_stage = None
        self.last_result = None
        
    def add(self, *nodes):
        self.nodes.extend(nodes)
    
    #---------------------------------------------------------------------------
    def to_module(self, name, clock='CLK', reset='RST'):
        """ generate a Module definion """
        
        m = Module(name)
        clk = m.Input(clock)
        rst = m.Input(reset)

        m = self.implement(m, clk, rst, aswire=False)

        return m

    #---------------------------------------------------------------------------
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
        for node in sorted(dataflow_nodes, key=lambda x:x.object_id):
            input_vars.update( input_visitor.visit(node) )

        output_visitor = visitor.OutputVisitor()
        output_vars = set()
        for node in sorted(dataflow_nodes, key=lambda x:x.object_id):
            output_vars.update( output_visitor.visit(node) )

        # add input ports
        for input_var in sorted(input_vars, key=lambda x:x.object_id):
            input_var._implement_input(m, seq, aswire)

        # schedule
        sched = scheduler.ASAPScheduler()
        sched.schedule(output_vars)
        
        # balance output stage depth
        max_stage = None
        for output_var in sorted(output_vars, key=lambda x:x.object_id):
            max_stage = dtypes._max(max_stage, output_var.end_stage)
        self.max_stage = max_stage

        output_vars = sched.balance_output(output_vars, max_stage)

        # get all vars
        all_visitor = visitor.AllVisitor()
        all_vars = set()
        for output_var in sorted(output_vars, key=lambda x:x.object_id):
            all_vars.update( all_visitor.visit(output_var) )

        # allocate (implement signals)
        alloc = allocator.Allocator()
        alloc.allocate(m, seq, all_vars)

        # add output ports
        for output_var in sorted(output_vars, key=lambda x:x.object_id):
            output_var._implement_output(m, seq, aswire)

        # add always statement
        seq.make_always()

        # save schedule result
        self.last_result = output_vars

        return m
            
    #---------------------------------------------------------------------------
    def draw_graph(self, filename='out.png', prog='dot', rankdir='LR', approx=False):
        if self.last_result is None:
            self.to_module()
            
        graph.draw_graph(self.last_result, filename=filename, prog=prog,
                         rankdir=rankdir, approx=approx)
        
    #---------------------------------------------------------------------------
    def pipeline_depth(self):
        return self.max_stage
