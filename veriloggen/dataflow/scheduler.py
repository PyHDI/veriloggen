from __future__ import absolute_import
from __future__ import print_function

from . import dtypes
from .visitor import _Visitor

#-------------------------------------------------------------------------------
class _Scheduler(_Visitor):
    def max_stage(self, *vars):
        return dtypes.max(*vars)
    
    def next_stage(self, node, stage):
        if stage is None: return None
        return stage + node.latency

    def schedule(self, nodes):
        raise NotImplementedError()

#-------------------------------------------------------------------------------
class ASAPScheduler(_Scheduler):
    """ Determine the scheduled cycle and insert delay variables to fill the gap """
    
    def schedule(self, nodes):
        for node in nodes:
            self.visit(node)

    def balance_output(self, nodes, max_stage):
        ret = []
        for node in nodes:
            if not node._has_output(): continue
            r = self.fill_gap(node, max_stage)
            t_data, t_valid, t_ready = node.output_data, node.output_valid, node.output_ready
            node._disable_output()
            r._disable_output()
            r.output(t_data, t_valid, t_ready)
            ret.append(r)
        return ret

    def fill_gap(self, node, end_stage):
        if end_stage is None: return node
        if node.end_stage is None: return node
        if node.end_stage == end_stage: return node
        if node.end_stage > end_stage:
            raise ValueError("Illegal stage number: node.end_stage (%d) > end_stage (%d)" %
                             node.end_stage, end_stage)

        if isinstance(node, dtypes._Delay) and node._get_parent_value() is not None:
            node = node._get_parent_value()
        
        prev = node
        cur_end_stage = prev.end_stage
        
        for i in range(cur_end_stage, end_stage):
            r = node._get_delayed_value(i + 1)
            if r is not None:
                prev = r
                continue
            r = dtypes._Delay(prev)
            r._set_start_stage(cur_end_stage)
            r._set_end_stage(cur_end_stage + 1)
            node._add_delayed_value(i + 1, r)
            r._set_parent_value(node)
            prev = r
            cur_end_stage += 1

        return prev
            
    def visit__BinaryOperator(self, node):
        if node._has_start_stage(): return node._get_end_stage()
        left = self.visit(node.left)
        right = self.visit(node.right)
        mine = self.max_stage(left, right)
        node.left = self.fill_gap(node.left, mine)
        node.right = self.fill_gap(node.right, mine)
        node._set_start_stage(mine)
        end = mine + node.latency
        node._set_end_stage(end)
        return end

    def visit__UnaryOperator(self, node):
        if node._has_start_stage(): return node._get_end_stage()
        right = self.visit(node.right)
        mine = self.max_stage(right)
        node.right = self.fill_gap(node.right, mine)
        node._set_start_stage(mine)
        end = mine + node.latency
        node._set_end_stage(end)
        return end
    
    def visit__SpecialOperator(self, node):
        if node._has_start_stage(): return node._get_end_stage()
        ret = []
        for var in node.args:
            var = self.visit(var)
            ret.append(var)
        mine = self.max_stage(*ret)
        node.arg = [ self.fill_gap(var, mine) for var in node.args ]
        node._set_start_stage(mine)
        end = mine + node.latency
        node._set_end_stage(end)
        return end
    
    def visit__Variable(self, node):
        if node._has_start_stage(): return node._get_end_stage()
        if isinstance(node.input_data, dtypes._Numeric):
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

    #def visit_Pointer(self, node):
    #    if node._has_start_stage(): return node._get_end_stage()
    #    var = self.visit(node.var)
    #    pos = self.visit(node.pos)
    #    mine = self.max_stage(var, pos)
    #    node.var = self.fill_gap(node.var, mine)
    #    node.pos = self.fill_gap(node.pos, mine)
    #    node._set_start_stage(mine)
    #    end = mine + node.latency
    #    node._set_end_stage(end)
    #    return end
    #
    #def visit_Slice(self, node):
    #    if node._has_start_stage(): return node._get_end_stage()
    #    var = self.visit(node.var)
    #    msb = self.visit(node.msb)
    #    lsb = self.visit(node.lsb)
    #    mine = self.max_stage(var, msb, lsb)
    #    node.var = self.fill_gap(node.var, mine)
    #    node.msb = self.fill_gap(node.msb, mine)
    #    node.lsb = self.fill_gap(node.lsb, mine)
    #    node._set_start_stage(mine)
    #    end = mine + node.latency
    #    node._set_end_stage(end)
    #    return end
    #
    #def visit_Cat(self, node):
    #    if node._has_start_stage(): return node._get_end_stage()
    #    ret = []
    #    for var in node.vars:
    #        var = self.visit(var)
    #        ret.append(var)
    #    mine = self.max_stage(*ret)
    #    node.vars = [ self.fill_gap(var, mine) for var in node.vars ]
    #    node._set_start_stage(mine)
    #    end = mine + node.latency
    #    node._set_end_stage(end)
    #    return end
    #
    #def visit_Repeat(self, node):
    #    if node._has_start_stage(): return node._get_end_stage()
    #    var = self.visit(node.var)
    #    times = self.visit(node.times)
    #    mine = self.max_stage(var, times)
    #    node.var = self.fill_gap(node.var, mine)
    #    node.times = self.fill_gap(node.times, mine)
    #    node._set_start_stage(mine)
    #    end = mine + node.latency
    #    node._set_end_stage(end)
    #    return end
    #
    #def visit_Cond(self, node):
    #    if node._has_start_stage(): return node._get_end_stage()
    #    condition = self.visit(node.condition)
    #    true_value = self.visit(node.true_value)
    #    false_value = self.visit(node.false_value)
    #    mine = self.max_stage(condition, true_value, false_value)
    #    node.condition = self.fill_gap(node.condition, mine)
    #    node.true_value = self.fill_gap(node.true_value, mine)
    #    node.false_value = self.fill_gap(node.false_value, mine)
    #    node._set_start_stage(mine)
    #    end = mine + node.latency
    #    node._set_end_stage(end)
    #    return end
