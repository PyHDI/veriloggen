from __future__ import absolute_import
from __future__ import print_function
import os
import sys
import copy
from collections import defaultdict

import veriloggen.core.vtypes as vtypes

from . import stypes
from .visitor import _Visitor


def draw_graph(vars, filename='out.png', prog='dot', rankdir='LR', approx=False):
    gg = GraphGenerator(rankdir=rankdir, approx=approx)
    gg.draw(vars, filename, prog)


class GraphGenerator(_Visitor):

    def __init__(self, rankdir='LR', approx=False):
        _Visitor.__init__(self)

        try:
            import pygraphviz as pgv
        except:
            raise ImportError('Graph generator requires Pygraphviz.')

        self.graph = pgv.AGraph(directed=True, rankdir=rankdir)

        self.approx = approx
        self.tmp_count = 0

        self.ranks = defaultdict(list)
        self.input_nodes = []
        self.output_nodes = []

    def draw(self, vars, filename='out.png', prog='dot'):
        for var in vars:
            self.visit(var)

        self.graph.add_subgraph(self.input_nodes, rank='same')

        for rank, nodes in sorted(self.ranks.items(), key=lambda x: x[0]):
            self.graph.add_subgraph(nodes, rank='same')

        self.graph.add_subgraph(self.output_nodes, rank='same')

        self.graph.write('out.dot')
        self.graph.layout(prog=prog)
        self.graph.draw(filename)

    def _set_rank(self, rank, node):
        self.ranks[rank].append(node)

    def _add_output(self, node, src):
        if node._has_output():
            outobj = str(node.output_data)
            label_data = [outobj, str(node.width)]
            if node.point > 0:
                label_data.append(str(node.point))
            label = ':'.join(label_data)
            self.graph.add_node(outobj, label=label, shape='box',
                                color='lightblue', style='filled', peripheries=2)
            self.graph.add_edge(src, outobj)
            self.output_nodes.append(outobj)

    def _add_gap(self, node, label=''):
        if self.approx:
            return node

        if node.start_stage is None or node.end_stage is None:
            return node

        prev = node
        for i in range(node.end_stage - node.start_stage - 1):
            tmp = self._get_tmp()
            self.graph.add_node(tmp, label=label, shape='box',
                                color='lightgray', style='filled')
            self.graph.add_edge(prev, tmp)
            self._set_rank(node.start_stage + 2 + i, tmp)
            prev = tmp
        return prev

    def _get_op_label(self, op):
        if op.__name__ in vtypes.operator_dict:
            return vtypes.operator_dict[op.__name__]

        if hasattr(op, '__call__'):
            return op.__name__

        return 'custom_op'

    def _get_label(self, obj):
        if obj.graph_label is not None:
            return obj.graph_label

        if hasattr(obj, 'ops'):
            return ' '.join([self._get_op_label(op) for op in obj.ops])

        if not hasattr(obj, 'op') or obj.op is None:
            return obj.__class__.__name__

        op = obj.op
        return self._get_op_label(op)

    def _get_shape(self, node):
        if node.graph_shape is not None:
            return node.graph_shape
        return 'circle'

    def _get_color(self, node):
        if node.graph_color is not None:
            return node.graph_color
        return 'black'

    def _get_style(self, node):
        if node.graph_style is not None:
            return node.graph_style
        return ''

    def _get_peripheries(self, node):
        return node.graph_peripheries

    def _get_tmp(self):
        v = self.tmp_count
        self.tmp_count += 1
        return hash((id(self), v))

    def visit__BinaryOperator(self, node):
        label = self._get_label(node)
        shape = self._get_shape(node)
        color = self._get_color(node)
        style = self._get_style(node)
        self.graph.add_node(node,
                            label=label, shape=shape,
                            color=color, style=style)

        left = self.visit(node.left)
        right = self.visit(node.right)
        self.graph.add_edge(left, node, label='L')
        self.graph.add_edge(right, node, label='R')

        if node.start_stage is not None:
            self._set_rank(node.start_stage + 1, node)

        prev = self._add_gap(node, label)
        self._add_output(node, prev)
        return prev

    def visit__UnaryOperator(self, node):
        if self.approx and isinstance(node, stypes._Delay):
            prev = self.visit(node.parent_value)
            self._add_output(node, prev)
            return prev

        label = self._get_label(node)
        shape = self._get_shape(node)
        color = self._get_color(node)
        style = self._get_style(node)
        peripheries = self._get_peripheries(node)
        self.graph.add_node(node,
                            label=label, shape=shape,
                            color=color, style=style,
                            peripheries=peripheries)

        right = self.visit(node.right)
        self.graph.add_edge(right, node, label='')

        if node.start_stage is None:
            pass
        elif isinstance(node, stypes._Prev):
            self._set_rank(node.start_stage, node)
        else:
            self._set_rank(node.start_stage + 1, node)

        prev = self._add_gap(node, label)
        self._add_output(node, prev)
        return prev

    def visit__SpecialOperator(self, node):
        label = self._get_label(node)
        shape = self._get_shape(node)
        color = self._get_color(node)
        style = self._get_style(node)
        peripheries = self._get_peripheries(node)
        self.graph.add_node(node,
                            label=label, shape=shape,
                            color=color, style=style,
                            peripheries=peripheries)

        for i, arg in enumerate(node.args):
            a = self.visit(arg)
            self.graph.add_edge(a, node, label='a%d' % i)

        if node.start_stage is not None:
            self._set_rank(node.start_stage + 1, node)

        prev = self._add_gap(node, label)
        self._add_output(node, prev)
        return prev

    def visit__Accumulator(self, node):
        label = self._get_label(node)
        shape = self._get_shape(node)
        color = self._get_color(node)
        style = self._get_style(node)
        peripheries = self._get_peripheries(node)
        self.graph.add_node(node,
                            label=label, shape=shape,
                            color=color, style=style,
                            peripheries=peripheries)

        right = self.visit(node.right)
        if node.size is not None:
            size = self.visit(node.size)
        if node.interval is not None:
            interval = self.visit(node.interval)
        initval = self.visit(node.initval)
        if node.offset is not None:
            offset = self.visit(node.offset)
        if node.dependency is not None:
            dependency = self.visit(node.dependency)
        if node.enable is not None:
            enable = self.visit(node.enable)
        if node.reset is not None:
            reset = self.visit(node.reset)
        self.graph.add_edge(right, node, label='data')
        if node.size is not None:
            self.graph.add_edge(size, node, label='size')
        if node.interval is not None:
            self.graph.add_edge(interval, node, label='interval')
        self.graph.add_edge(initval, node, label='initval')
        if node.offset is not None:
            self.graph.add_edge(offset, node, label='offset')
        if node.dependency is not None:
            self.graph.add_edge(dependency, node, label='dependency')
        if node.enable is not None:
            self.graph.add_edge(enable, node, label='enable')
        if node.reset is not None:
            self.graph.add_edge(reset, node, label='reset')
        # reg_initval = self.visit(node.reg_initval)

        if node.start_stage is not None:
            self._set_rank(node.start_stage + 1, node)

        prev = self._add_gap(node, label)
        self._add_output(node, prev)
        return prev

    def visit_Substream(self, node):
        label = self._get_label(node)
        shape = self._get_shape(node)
        color = self._get_color(node)
        style = self._get_style(node)
        peripheries = self._get_peripheries(node)
        self.graph.add_node(node,
                            label=label, shape=shape,
                            color=color, style=style,
                            peripheries=peripheries)

        for arg, name in zip(node.args, node.conds.keys()):
            a = self.visit(arg)
            self.graph.add_edge(a, node, label=name)

        if node.start_stage is not None:
            self._set_rank(node.start_stage + 1, node)

        prev = self._add_gap(node, label)
        self._add_output(node, prev)
        return prev

    def visit__Sync(self, node):
        label = self._get_label(node)
        shape = self._get_shape(node)
        color = self._get_color(node)
        style = self._get_style(node)
        peripheries = self._get_peripheries(node)
        self.graph.add_node(node,
                            label=label, shape=shape,
                            color=color, style=style,
                            peripheries=peripheries)

        for i, arg in enumerate(node.args):
            if i != node.index:
                continue
            a = self.visit(arg)
            self.graph.add_edge(a, node, label='a%d' % i)

        if node.start_stage is not None:
            self._set_rank(node.start_stage + 1, node)

        prev = self._add_gap(node, label)
        self._add_output(node, prev)
        return prev

    def visit_ForwardDest(self, node):
        label = self._get_label(node)
        shape = self._get_shape(node)
        color = self._get_color(node)
        style = self._get_style(node)
        peripheries = self._get_peripheries(node)
        self.graph.add_node(node,
                            label=label, shape=shape,
                            color=color, style=style,
                            peripheries=peripheries)

        value = self.visit(node.args[0])
        self.graph.add_edge(value, node, label='value')
        index = self.visit(node.args[1])
        self.graph.add_edge(index, node, label='index')

        if node.start_stage is not None:
            self._set_rank(node.start_stage + 1, node)

        prev = self._add_gap(node, label)
        self._add_output(node, prev)
        return prev

    def visit_ForwardSource(self, node):
        label = self._get_label(node)
        shape = self._get_shape(node)
        color = self._get_color(node)
        style = self._get_style(node)
        peripheries = self._get_peripheries(node)
        self.graph.add_node(node,
                            label=label, shape=shape,
                            color=color, style=style,
                            peripheries=peripheries)

        value = self.visit(node.args[0])
        self.graph.add_edge(value, node, label='value')
        index = self.visit(node.args[1])
        self.graph.add_edge(index, node, label='index')
        dest = self.visit(node.dest)
        self.graph.add_edge(node, dest, label='dest')

        if node.start_stage is not None:
            self._set_rank(node.start_stage + 1, node)

        prev = self._add_gap(node, label)
        self._add_output(node, prev)
        return prev

    def visit_Consumer(self, node):
        label = self._get_label(node)
        shape = self._get_shape(node)
        color = self._get_color(node)
        style = self._get_style(node)
        peripheries = self._get_peripheries(node)
        self.graph.add_node(node,
                            label=label, shape=shape,
                            color=color, style=style,
                            peripheries=peripheries)

        initval = self.visit(node.args[0])
        self.graph.add_edge(initval, node, label='initval')

        if node.start_stage is not None:
            self._set_rank(node.start_stage + 1, node)

        prev = self._add_gap(node, label)
        self._add_output(node, prev)
        return prev

    def visit_Producer(self, node):
        label = self._get_label(node)
        shape = self._get_shape(node)
        color = self._get_color(node)
        style = self._get_style(node)
        peripheries = self._get_peripheries(node)
        self.graph.add_node(node,
                            label=label, shape=shape,
                            color=color, style=style,
                            peripheries=peripheries)

        dest = self.visit(node.dest)
        self.graph.add_edge(node, dest, label='dest')
        value = self.visit(node.args[0])
        self.graph.add_edge(value, node, label='value')
        if node.when_index > 0:
            when = self.visit(node.args[node.when_index])
            self.graph.add_edge(when, node, label='when')
        if node.reset_index > 0:
            reset = self.visit(node.args[node.reset_index])
            self.graph.add_edge(reset, node, label='reset')

        if node.start_stage is not None:
            self._set_rank(node.start_stage + 1, node)

        prev = self._add_gap(node, label)
        self._add_output(node, prev)
        return prev

    def visit_ReadRAM(self, node):
        label = self._get_label(node)
        shape = self._get_shape(node)
        color = self._get_color(node)
        style = self._get_style(node)
        peripheries = self._get_peripheries(node)
        self.graph.add_node(node,
                            label=label, shape=shape,
                            color=color, style=style,
                            peripheries=peripheries)

        addr = self.visit(node.args[0])
        self.graph.add_edge(addr, node, label='addr')

        if len(node.args) == 3:
            when = self.visit(node.args[2])
            self.graph.add_edge(when, node, label='when')

        if node.start_stage is not None:
            self._set_rank(node.start_stage + 1, node)

        prev = self._add_gap(node, label)
        self._add_output(node, prev)
        return prev

    def visit_WriteRAM(self, node):
        label = self._get_label(node)
        shape = self._get_shape(node)
        color = self._get_color(node)
        style = self._get_style(node)
        peripheries = self._get_peripheries(node)
        self.graph.add_node(node,
                            label=label, shape=shape,
                            color=color, style=style,
                            peripheries=peripheries)

        addr = self.visit(node.args[0])
        self.graph.add_edge(addr, node, label='addr')
        data = self.visit(node.args[1])
        self.graph.add_edge(data, node, label='data')

        if len(node.args) == 4:
            when = self.visit(node.args[3])
            self.graph.add_edge(when, node, label='when')

        if node.start_stage is not None:
            self._set_rank(node.start_stage + 1, node)

        prev = self._add_gap(node, label)
        self._add_output(node, prev)
        return prev

    def visit_RingBuffer(self, node):
        label = self._get_label(node)
        shape = self._get_shape(node)
        color = self._get_color(node)
        style = self._get_style(node)
        peripheries = self._get_peripheries(node)
        self.graph.add_node(node,
                            label=label, shape=shape,
                            color=color, style=style,
                            peripheries=peripheries)

        data = self.visit(node.args[0])
        self.graph.add_edge(data, node, label='data')
        if len(node.args) > 1:
            enable = self.visit(node.args[1])
            self.graph.add_edge(enable, node, label='enable')

        if node.start_stage is not None:
            self._set_rank(node.start_stage + 1, node)

        prev = self._add_gap(node, label)
        self._add_output(node, prev)
        return prev

    def visit__RingBufferOutput(self, node):
        label = self._get_label(node)
        shape = self._get_shape(node)
        color = self._get_color(node)
        style = self._get_style(node)
        peripheries = self._get_peripheries(node)
        self.graph.add_node(node,
                            label=label, shape=shape,
                            color=color, style=style,
                            peripheries=peripheries)

        buf = self.visit(node.args[0])
        offset = self.visit(node.args[1])
        self.graph.add_edge(buf, node, label='buf')
        self.graph.add_edge(offset, node, label='offset')
        if len(node.args) > 2:
            enable = self.visit(node.args[2])
            self.graph.add_edge(enable, node, label='enable')

        if node.start_stage is not None:
            self._set_rank(node.start_stage + 1, node)

        prev = self._add_gap(node, label)
        self._add_output(node, prev)
        return prev

    def visit_Scratchpad(self, node):
        label = self._get_label(node)
        shape = self._get_shape(node)
        color = self._get_color(node)
        style = self._get_style(node)
        peripheries = self._get_peripheries(node)
        self.graph.add_node(node,
                            label=label, shape=shape,
                            color=color, style=style,
                            peripheries=peripheries)

        data = self.visit(node.args[0])
        self.graph.add_edge(data, node, label='data')
        addr = self.visit(node.args[1])
        self.graph.add_edge(addr, node, label='addr')
        if len(node.args) > 2:
            enable = self.visit(node.args[2])
            self.graph.add_edge(enable, node, label='enable')

        if node.start_stage is not None:
            self._set_rank(node.start_stage + 1, node)

        prev = self._add_gap(node, label)
        self._add_output(node, prev)
        return prev

    def visit__ScratchpadOutput(self, node):
        label = self._get_label(node)
        shape = self._get_shape(node)
        color = self._get_color(node)
        style = self._get_style(node)
        peripheries = self._get_peripheries(node)
        self.graph.add_node(node,
                            label=label, shape=shape,
                            color=color, style=style,
                            peripheries=peripheries)

        sp = self.visit(node.args[0])
        addr = self.visit(node.args[1])
        self.graph.add_edge(sp, node, label='sp')
        self.graph.add_edge(addr, node, label='addr')
        if len(node.args) > 2:
            enable = self.visit(node.args[2])
            self.graph.add_edge(enable, node, label='enable')

        if node.start_stage is not None:
            self._set_rank(node.start_stage + 1, node)

        prev = self._add_gap(node, label)
        self._add_output(node, prev)
        return prev

    def visit__ParameterVariable(self, node):
        label = self._get_label(node)
        shape = self._get_shape(node)
        color = self._get_color(node)
        style = self._get_style(node)
        peripheries = self._get_peripheries(node)
        self.graph.add_node(node,
                            label=label, shape=shape,
                            color=color, style=style,
                            peripheries=peripheries)

        self.input_nodes.append(node)
        self._add_output(node, node)
        return node

    def visit__Variable(self, node):
        if isinstance(node.input_data, stypes._Numeric):
            input_data = self.visit(node.input_data)
            return input_data

        label = self._get_label(node)
        shape = self._get_shape(node)
        color = self._get_color(node)
        style = self._get_style(node)
        peripheries = self._get_peripheries(node)
        self.graph.add_node(node,
                            label=label, shape=shape,
                            color=color, style=style,
                            peripheries=peripheries)

        self.input_nodes.append(node)
        self._add_output(node, node)
        return node

    def visit__Constant(self, node):
        if isinstance(node, stypes.FixedPoint):
            value = "%f:%d" % (
                ((1.0 * node.value) / (2.0 ** node.point)), node.point)
        elif isinstance(node, stypes.Float):
            value = "%f" % node.value
        else:
            value = str(node.value)

        label = value
        shape = self._get_shape(node)
        color = self._get_color(node)
        style = self._get_style(node)
        peripheries = self._get_peripheries(node)
        self.graph.add_node(node,
                            label=label, shape=shape,
                            color=color, style=style,
                            peripheries=peripheries)

        self._add_output(node, node)
        return node
