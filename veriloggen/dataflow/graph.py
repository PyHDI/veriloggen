from __future__ import absolute_import
from __future__ import print_function
import os
import sys
import copy

import veriloggen.core.vtypes as vtypes

from . import dtypes
from .visitor import _Visitor

def draw_graph(vars, filename='out.png', prog='dot', rankdir='LR', nogap=False):
    gg = GraphGenerator(rankdir=rankdir, nogap=nogap)
    gg.draw(vars, filename, prog)

class GraphGenerator(_Visitor):
    def __init__(self, rankdir='LR', nogap=False):
        try:
            import pygraphviz as pgv
        except:
            raise ImportError('Graph generator requires Pygraphviz.')

        self.graph = pgv.AGraph(directed=True, rankdir=rankdir)
        
        self.nogap = nogap
        self.visited_node = {}
        self.tmp_count = 0

    def draw(self, vars, filename='out.png', prog='dot'):
        for var in vars:
            self.visit(var)

        self.graph.write('out.dot')
        self.graph.layout(prog=prog)
        self.graph.draw(filename)

    def visit(self, node):
        if node in self.visited_node:
            return self.visited_node[node]
        return _Visitor.visit(self, node)
    
    def _visited(self, node):
        return node in self.visited_node

    def _add_output(self, node, src):
        if node._has_output():
            outobj = node.output_data
            self.graph.add_node(outobj, label=node.output_data, shape='box',
                           color='lightblue', style='filled', peripheries=2)
            self.graph.add_edge(src, outobj)

    def _add_gap(self, node, mark=''):
        if self.nogap: return node
        prev = node
        for i in range(node.end_stage - node.start_stage - 1):
            tmp = self._get_tmp()
            self.graph.add_node(tmp, label=mark, shape='box', color='lightgray', style='filled')
            self.graph.add_edge(prev, tmp)
            prev = tmp
        return prev
            
    def _get_mark(self, obj):
        if obj is None:
            return ''
        if obj.__name__ in vtypes.operator_dict:
            return vtypes.operator_dict[obj.__name__]
        if hasattr(obj, '__call__'):
            return obj.__name__
        return 'custom'

    def _get_tmp(self):
        v = self.tmp_count
        self.tmp_count += 1
        return hash( (id(self), v) )
    
    def visit__BinaryOperator(self, node):
        mark = self._get_mark(node.op)
        self.graph.add_node(node, label=mark, shape='circle')
        left = self.visit(node.left)
        right = self.visit(node.right)
        self.graph.add_edge(left, node, label='L')
        self.graph.add_edge(right, node, label='R')
        prev = self._add_gap(node, mark)
        self._add_output(node, prev)
        self.visited_node[node] = prev
        return prev
    
    def visit__UnaryOperator(self, node):
        if self.nogap and isinstance(node, dtypes._Delay):
            return self.visit(node.parent_value)
        
        mark = ('delay' if isinstance(node, dtypes._Delay) else
                'prev' if isinstance(node, dtypes._Prev) else
                self._get_mark(node.op) )
        shape = 'box' if isinstance(node, (dtypes._Delay, dtypes._Prev)) else 'circle'
        color = 'lightgray' if isinstance(node, (dtypes._Delay, dtypes._Prev)) else 'black'
        style = 'filled' if isinstance(node, (dtypes._Delay, dtypes._Prev)) else None
        self.graph.add_node(node, label=mark, shape=shape, color=color, style=style)
        right = self.visit(node.right)
        self.graph.add_edge(right, node, label='R')
        prev = self._add_gap(node, mark)
        self._add_output(node, prev)
        self.visited_node[node] = prev
        return prev

    def visit__SpecialOperator(self, node):
        mark = self._get_mark(node.op)
        self.graph.add_node(node, label=mark, shape='ellipse')
        for i, arg in enumerate(node.args):
            a = self.visit(arg)
            self.graph.add_edge(a, node, label=str(i))
        prev = self._add_gap(node, mark)
        self._add_output(node, prev)
        self.visited_node[node] = prev
        return prev

    def visit__Accumulator(self, node):
        mark = ' '.join([ self._get_mark(op) for op in node.ops ])
        self.graph.add_node(node, label=mark, shape='box', style='rounded')
        right = self.visit(node.right)
        initval = self.visit(node.initval)
        reset = self.visit(node.reset)
        self.graph.add_edge(right, node, label='R')
        self.graph.add_edge(initval, node, label='initval')
        self.graph.add_edge(reset, node, label='reset')
        prev = self._add_gap(node, mark)
        self._add_output(node, prev)
        self.visited_node[node] = prev
        return prev
    
    def visit__Variable(self, node):
        if isinstance(node.input_data, dtypes._Numeric):
            self.visit(node.input_data)
            self.visited_node[node] = node
            return

        self.graph.add_node(node, label=node.input_data, shape='box', peripheries=2,
                            color='lightblue', style='filled')
        self._add_output(node, node)
        self.visited_node[node] = node
        return node

    def visit__Constant(self, node):
        if isinstance(node, dtypes.FixedPoint):
            value = "%f:%d" % (((1.0 * node.value) / (2.0 ** node.point)), node.point)
        elif isinstance(node, dtypes.Float):
            value = "%f" % node.value
        else:
            value = str(node.value)
        self.graph.add_node(node, label=value, shape='', color='lightblue', style='filled')
        self._add_output(node, node)
        self.visited_node[node] = node
        return node
