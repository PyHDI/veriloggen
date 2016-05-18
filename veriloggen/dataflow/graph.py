from __future__ import absolute_import
from __future__ import print_function
import os
import sys
import copy

import veriloggen.core.vtypes as vtypes

from . import dtypes
from .visitor import _Visitor

def draw_graph(vars, filename='out.png', prog='dot', skip_gap=False):
    gg = GraphGenerator(skip_gap=skip_gap)
    gg.draw(vars, filename, prog)

class GraphGenerator(_Visitor):
    def __init__(self, skip_gap=False):
        try:
            import pygraphviz as pgv
        except:
            raise ImportError('Graph generator requires Pygraphviz.')

        self.skip_gap = skip_gap
        self.graph = pgv.AGraph(directed=True)
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
    
    def _add_node(self, node, label='', color='black', shape='box', style='solid'):
        self.graph.add_node(node, label=label, color=color, shape=shape, style=style)

    def _add_edge(self, start, end, color='black', label='', style='solid'):
        self.graph.add_edge(start, end, color=color, label=label, style=style)

    def _add_output(self, node, src):
        if node._has_output():
            outobj = node.output_data
            self._add_node(outobj, label=node.output_data, shape='trapezium')
            self._add_edge(src, outobj)

    def _add_gap(self, node, mark=''):
        if self.skip_gap: return node
        prev = node
        for i in range(node.end_stage - node.start_stage - 1):
            tmp = self._get_tmp()
            self._add_node(tmp, label=mark, shape='box')
            self._add_edge(prev, tmp)
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
        self._add_node(node, label=mark, shape='ellipse')
        left = self.visit(node.left)
        right = self.visit(node.right)
        self._add_edge(left, node, label='L')
        self._add_edge(right, node, label='R')
        prev = self._add_gap(node, mark)
        self._add_output(node, prev)
        self.visited_node[node] = prev
        return prev
    
    def visit__UnaryOperator(self, node):
        mark = ('delay' if isinstance(node, dtypes._Delay) else
                'prev' if isinstance(node, dtypes._Prev) else
                self._get_mark(node.op) )
        shape = 'box' if isinstance(node, (dtypes._Delay, dtypes._Prev)) else 'ellipse' 
        self._add_node(node, label=mark, shape=shape)
        right = self.visit(node.right)
        self._add_edge(right, node, label='R')
        prev = self._add_gap(node, mark)
        self._add_output(node, prev)
        self.visited_node[node] = prev
        return prev

    def visit__SpecialOperator(self, node):
        mark = self._get_mark(node.op)
        self._add_node(node, label=mark, shape='ellipse')
        for i, arg in enumerate(node.args):
            a = self.visit(arg)
            self._add_edge(a, node, label=str(i))
        prev = self._add_gap(node, mark)
        self._add_output(node, prev)
        self.visited_node[node] = prev
        return prev

    def visit__Accumulator(self, node):
        mark = ' '.join([ self._get_mark(op) for op in node.ops ])
        self._add_node(node, label=mark, shape='box', style='rounded')
        right = self.visit(node.right)
        initval = self.visit(node.initval)
        reset = self.visit(node.reset)
        self._add_edge(right, node, label='R')
        self._add_edge(initval, node, label='initval')
        self._add_edge(reset, node, label='reset')
        prev = self._add_gap(node, mark)
        self._add_output(node, prev)
        self.visited_node[node] = prev
        return prev
    
    def visit__Variable(self, node):
        if isinstance(node.input_data, dtypes._Numeric):
            self.visit(node.input_data)
            return
        
        self._add_node(node, label=node.input_data, shape='invtrapezium')
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
        self._add_node(node, label=value, shape='oval')
        self._add_output(node, node)
        self.visited_node[node] = node
        return node
