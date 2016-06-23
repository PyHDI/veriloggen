from __future__ import absolute_import
from __future__ import print_function
import os
import sys
import copy
from collections import defaultdict

import veriloggen.core.vtypes as vtypes

from . import dtypes
from .visitor import _Visitor

def draw_graph(vars, filename='out.png', prog='dot', rankdir='LR', approx=False):
    gg = GraphGenerator(rankdir=rankdir, approx=approx)
    gg.draw(vars, filename, prog)

class GraphGenerator(_Visitor):
    def __init__(self, rankdir='LR', approx=False):
        try:
            import pygraphviz as pgv
        except:
            raise ImportError('Graph generator requires Pygraphviz.')

        self.graph = pgv.AGraph(directed=True, rankdir=rankdir)
        
        self.approx = approx
        self.visited_node = {}
        self.tmp_count = 0

        self.ranks = defaultdict(list)
        self.input_nodes = []
        self.output_nodes = []

    def draw(self, vars, filename='out.png', prog='dot'):
        for var in vars:
            self.visit(var)

        self.graph.add_subgraph(self.input_nodes, rank='same')

        for rank, nodes in sorted(self.ranks.items(), key=lambda x:x[0]):
            self.graph.add_subgraph(nodes, rank='same')
            
        self.graph.add_subgraph(self.output_nodes, rank='same')
        
        self.graph.write('out.dot')
        self.graph.layout(prog=prog)
        self.graph.draw(filename)

    def visit(self, node):
        if node in self.visited_node:
            return self.visited_node[node]
        return _Visitor.visit(self, node)
    
    def _visited(self, node):
        return node in self.visited_node

    def _set_rank(self, rank, node):
        self.ranks[rank].append(node)
            
    def _add_output(self, node, src):
        if node._has_output():
            outobj = str(node.output_data)
            label_data = [ outobj, str(node.width) ]
            if node.point > 0:
                label_data.append(str(node.point))
            label = ':'.join(label_data)
            self.graph.add_node(outobj, label=label, shape='box',
                                color='lightblue', style='filled', peripheries=2)
            self.graph.add_edge(src, outobj)
            self.output_nodes.append(outobj)

    def _add_gap(self, node, mark=''):
        if self.approx:
            return node
        
        prev = node
        for i in range(node.end_stage - node.start_stage - 1):
            tmp = self._get_tmp()
            self.graph.add_node(tmp, label=mark, shape='box', color='lightgray', style='filled')
            self.graph.add_edge(prev, tmp)
            self._set_rank(node.start_stage + 2 + i, tmp)
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
        
        self._set_rank(node.start_stage + 1, node)
        prev = self._add_gap(node, mark)
        self._add_output(node, prev)
        self.visited_node[node] = prev
        return prev
    
    def visit__UnaryOperator(self, node):
        if self.approx and isinstance(node, dtypes._Delay):
            prev = self.visit(node.parent_value)
            self._add_output(node, prev)
            return prev
        
        mark = ('delay' if isinstance(node, dtypes._Delay) else
                'prev' if isinstance(node, dtypes._Prev) else
                self._get_mark(node.op) )
        shape = 'box' if isinstance(node, (dtypes._Delay, dtypes._Prev)) else 'circle'
        color = 'lightgray' if isinstance(node, (dtypes._Delay, dtypes._Prev)) else 'black'
        style = 'filled' if isinstance(node, (dtypes._Delay, dtypes._Prev)) else None
        self.graph.add_node(node, label=mark, shape=shape, color=color, style=style)
        
        right = self.visit(node.right)
        self.graph.add_edge(right, node, label='R')

        if isinstance(node, dtypes._Prev):
            self._set_rank(node.start_stage, node)
        else:
            self._set_rank(node.start_stage + 1, node)
        
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
            
        self._set_rank(node.start_stage + 1, node)
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
        
        self._set_rank(node.start_stage + 1, node)
        prev = self._add_gap(node, mark)
        self._add_output(node, prev)
        self.visited_node[node] = prev
        return prev
    
    def visit__Variable(self, node):
        if isinstance(node.input_data, dtypes._Numeric):
            self.visit(node.input_data)
            self.visited_node[node] = node
            return

        inobj = str(node.input_data)
        label_data = [ inobj, str(node.width) ]
        if node.point > 0:
            label_data.append(str(node.point))
        label = ':'.join(label_data)
        
        self.graph.add_node(node, label=label, shape='box',
                            color='lightblue', style='filled', peripheries=2)
        
        self.input_nodes.append(node)
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
