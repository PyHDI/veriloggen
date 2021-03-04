from __future__ import absolute_import
from __future__ import print_function

from . import stypes
from .visitor import _Visitor


class _Scheduler(_Visitor):

    def max_stage(self, *vars):
        return stypes._max(*vars)

    def next_stage(self, node, stage):
        if stage is None:
            return 0
        return stage + node.latency

    def schedule(self, nodes):
        raise NotImplementedError()


class ASAPScheduler(_Scheduler):
    """ Determine the scheduled cycle and insert delay variables to fill the gap """

    def schedule(self, nodes):
        for node in sorted(nodes, key=lambda x: x.object_id):
            self.visit(node)

    def balance_output(self, nodes, max_stage):
        ret = []
        for node in sorted(nodes, key=lambda x: x.object_id):
            if not node._has_output():
                continue
            r = self.fill_gap(node, max_stage)
            t_data = node.output_data
            t_sig_data = node.output_sig_data
            node._disable_output()
            node._disable_output_sig()
            node._set_output_node(r)
            r._disable_output()
            r._disable_output_sig()
            r.output_data = t_data
            r.output_sig_data = t_sig_data
            ret.append(r)
        return ret

    def fill_gap(self, node, end_stage):
        if end_stage is None:
            return node
        if node.end_stage is None:
            return node
        if node.end_stage == end_stage:
            return node
        if node.end_stage > end_stage:
            raise ValueError("Illegal stage number: node.end_stage (%d) > end_stage (%d)" %
                             node.end_stage, end_stage)

        if isinstance(node, stypes._Delay) and node._get_parent_value() is not None:
            node = node._get_parent_value()

        prev = node
        cur_end_stage = prev.end_stage

        for i in range(cur_end_stage, end_stage):
            r = node._get_delayed_value(i + 1)
            if r is not None:
                prev = r
                cur_end_stage += 1
                continue
            r = stypes._Delay(prev)
            r._set_start_stage(cur_end_stage)
            r._set_end_stage(cur_end_stage + 1)
            node._add_delayed_value(i + 1, r)
            r._set_parent_value(node)
            prev = r
            cur_end_stage += 1

        return prev

    def visit__BinaryOperator(self, node):
        if node._has_start_stage():
            return node._get_end_stage()
        left = self.visit(node.left)
        right = self.visit(node.right)
        mine = self.max_stage(left, right)
        if mine is None:
            mine = 0
        node.left = self.fill_gap(node.left, mine)
        node.right = self.fill_gap(node.right, mine)
        node._set_start_stage(mine)
        if getattr(node, 'variable_latency', None):
            node.latency = getattr(node, node.variable_latency)()
        if getattr(node, 'variable_iteration_interval', None):
            node.iteration_interval = getattr(node, node.variable_iteration_interval)()
        end = self.next_stage(node, mine)
        node._set_end_stage(end)
        return end

    def visit__UnaryOperator(self, node):
        if node._has_start_stage():
            return node._get_end_stage()
        right = self.visit(node.right)
        mine = self.max_stage(right)
        if mine is None:
            mine = 0
        node.right = self.fill_gap(node.right, mine)
        node._set_start_stage(mine)
        if getattr(node, 'variable_latency', None):
            node.latency = getattr(node, node.variable_latency)()
        if getattr(node, 'variable_iteration_interval', None):
            node.iteration_interval = getattr(node, node.variable_iteration_interval)()
        end = self.next_stage(node, mine)
        node._set_end_stage(end)
        return end

    def visit__SpecialOperator(self, node):
        if node._has_start_stage():
            return node._get_end_stage()
        ret = []
        for var in node.args:
            var = self.visit(var)
            ret.append(var)
        mine = self.max_stage(*ret)
        if mine is None:
            mine = 0
        node.args = [self.fill_gap(var, mine) for var in node.args]
        node._set_start_stage(mine)
        if getattr(node, 'variable_latency', None):
            node.latency = getattr(node, node.variable_latency)()
        if getattr(node, 'variable_iteration_interval', None):
            node.iteration_interval = getattr(node, node.variable_iteration_interval)()
        end = self.next_stage(node, mine)
        node._set_end_stage(end)
        return end

    def visit__Accumulator(self, node):
        if node._has_start_stage():
            return node._get_end_stage()
        right = self.visit(node.right)
        size = self.visit(node.size) if node.size is not None else None
        interval = (self.visit(node.interval)
                    if node.interval is not None else None)
        initval = self.visit(node.initval)
        offset = (self.visit(node.offset)
                  if node.offset is not None else None)
        dependency = (self.visit(node.dependency)
                      if node.dependency is not None else None)
        enable = self.visit(node.enable) if node.enable is not None else None
        reset = self.visit(node.reset) if node.reset is not None else None
        mine = self.max_stage(right, size, interval, initval,
                              offset, dependency, enable, reset)
        if mine is None:
            mine = 0
        node.right = self.fill_gap(node.right, mine)
        if node.size is not None:
            node.size = self.fill_gap(node.size, mine)
        if node.interval is not None:
            node.interval = self.fill_gap(node.interval, mine)
        node.initval = self.fill_gap(node.initval, mine)
        if node.offset is not None:
            node.offset = self.fill_gap(node.offset, mine)
        if node.enable is not None:
            node.enable = self.fill_gap(node.enable, mine)
        if node.reset is not None:
            node.reset = self.fill_gap(node.reset, mine)
        node.reg_initval = self.fill_gap(node.reg_initval, mine)
        node._set_start_stage(mine)
        if getattr(node, 'variable_latency', None):
            node.latency = getattr(node, node.variable_latency)()
        if getattr(node, 'variable_iteration_interval', None):
            node.iteration_interval = getattr(node, node.variable_iteration_interval)()
        end = self.next_stage(node, mine)
        node._set_end_stage(end)
        return end

    def visit__ParameterVariable(self, node):
        return None

    def visit__Variable(self, node):
        if node._has_start_stage():
            return node._get_end_stage()
        if isinstance(node.input_data, stypes._Numeric):
            data = self.visit(node.input_data)
            node._set_start_stage(data)
            return data
        mine = 0
        node._set_start_stage(mine)
        end = mine
        node._set_end_stage(end)
        return end

    def visit__Constant(self, node):
        return None
