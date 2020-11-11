from __future__ import absolute_import
from __future__ import print_function
import os
import sys
import copy
from functools import reduce

import veriloggen.core.vtypes as vtypes
from veriloggen.seq.seq import Seq


def _and_vars(*vars):
    if not vars:
        return vtypes.Int(1)
    ret = None
    for var in vars:
        if var is None:
            continue
        if ret is None:
            ret = var
        else:
            ret = vtypes.AndList(ret, var)
    if ret is None:
        return vtypes.Int(1)
    return ret


def _connect_ready(m, var, ready):
    if var is None:
        return

    prev_assign = var._get_assign()
    if not prev_assign:
        m.Assign(var(ready))
    elif (isinstance(prev_assign.statement.right, vtypes.Int) and
          prev_assign.statement.right.value == 1):
        prev_assign.overwrite_right(ready)
        m.remove(prev_assign)
        m.append(prev_assign)
    else:
        prev_assign.overwrite_right(
            _and_vars(prev_assign.statement.right, ready))
        m.remove(prev_assign)
        m.append(prev_assign)


class Pipeline(vtypes.VeriloggenNode):
    """ Pipeline Generator """

    def __init__(self, m, name, clk, rst, width=32):
        self.m = m
        self.name = name
        self.clk = clk
        self.rst = rst
        self.width = width

        self.tmp_count = 0
        self.max_stage_id = 0
        self.vars = []

        self.seq = Seq(self.m, self.name, clk, rst, nohook=True)
        self.data_visitor = DataVisitor(self)

        self.done = False

    #-------------------------------------------------------------------------
    def input(self, data, valid=None, ready=None, width=None):
        if ready is not None and not isinstance(ready, (vtypes.Wire, vtypes.Output)):
            raise TypeError('ready port of PipelineVariable must be Wire., not %s' %
                            str(type(ready)))
        ret = _PipelineVariable(self, 0, data, valid, ready,
                                _PipelineInterface(data, valid, ready))
        self.vars.append(ret)
        return ret

    #-------------------------------------------------------------------------
    # self.__call__() calls this method
    def stage(self, data, initval=0, width=None, preg=None):
        if width is None:
            width = self.width
        stage_id, raw_data, raw_valid, raw_ready = self.data_visitor.visit(
            data)
        tmp_data, tmp_valid, tmp_ready = self._make_tmp(raw_data, raw_valid, raw_ready,
                                                        width, initval)
        next_stage_id = stage_id + 1 if stage_id is not None else None

        ret = _PipelineVariable(self, next_stage_id,
                                tmp_data, tmp_valid, tmp_ready, data)

        self.vars.append(ret)
        if isinstance(preg, _PipelineVariable):
            preg._add_preg(next_stage_id, ret)

        if next_stage_id is not None and next_stage_id > self.max_stage_id:
            self.max_stage_id = next_stage_id

        return ret

    #-------------------------------------------------------------------------
    # Accumulator
    def acc_and(self, data, initval=0, resetcond=None, width=None):
        return self._accumulate([vtypes.And], data, width, initval, resetcond)

    def acc_nand(self, data, initval=0, resetcond=None, width=None):
        return self._accumulate([vtypes.And, vtypes.Unot], data, width, initval, resetcond)

    def acc_or(self, data, initval=0, resetcond=None, width=None):
        return self._accumulate([vtypes.Or], data, width, initval, resetcond)

    def acc_xor(self, data, initval=0, resetcond=None, width=None):
        return self._accumulate([vtypes.Xor], data, width, initval, resetcond)

    def acc_xnor(self, data, initval=0, resetcond=None, width=None):
        return self._accumulate([vtypes.Xor, vtypes.Unot], data, width, initval, resetcond)

    def acc_nor(self, data, initval=0, resetcond=None, width=None):
        return self._accumulate([vtypes.Or, vtypes.Unot], data, width, initval, resetcond)

    def acc_add(self, data, initval=0, resetcond=None, width=None):
        return self._accumulate([vtypes.Plus], data, width, initval, resetcond)

    def acc_sub(self, data, initval=0, resetcond=None, width=None):
        return self._accumulate([vtypes.Minus], data, width, initval, resetcond)

    def acc_mul(self, data, initval=0, resetcond=None, width=None):
        return self._accumulate([vtypes.Times], data, width, initval, resetcond)

    def acc_div(self, data, initval=0, resetcond=None, width=None):
        return self._accumulate([vtypes.Divide], data, width, initval, resetcond)

    def acc_mod(self, data, initval=0, resetcond=None, width=None):
        return self._accumulate([vtypes.Mod], data, width, initval, resetcond)

    def acc_max(self, data, initval=0, resetcond=None, width=None):
        def op(left, right):
            return vtypes.Cond(left > right, left, right)
        return self._accumulate([op], data, width, initval, resetcond, 'max')

    def acc_min(self, data, initval=0, resetcond=None, width=None):
        def op(left, right):
            return vtypes.Cond(left < right, left, right)
        return self._accumulate([op], data, width, initval, resetcond, 'min')

    def acc_custom(self, data, ops, initval=0, resetcond=None, width=None, label=None):
        if not isinstance(ops, (tuple, list)):
            ops = [ops]
        return self._accumulate(ops, data, width, initval, resetcond, label)

    #-------------------------------------------------------------------------
    def make_always(self, reset=(), body=()):
        if self.done:
            raise ValueError('make_always() has been already called.')
        self.done = True

        for var in self.vars:
            if var.output_vars is not None:
                var.make_output()

        self.m.Always(vtypes.Posedge(self.clk))(
            vtypes.If(self.rst)(
                reset,
                self.make_reset()
            )(
                body,
                self.make_code()
            ))

    #-------------------------------------------------------------------------
    def make_reset(self):
        return self.seq.make_reset()

    #-------------------------------------------------------------------------
    def make_code(self):
        return self.seq.make_code()

    #-------------------------------------------------------------------------
    def draw_graph(self, filename='out.png', prog='dot'):
        _draw_graph(self, filename, prog)

    #-------------------------------------------------------------------------
    def _accumulate(self, ops, data, width=None, initval=0, resetcond=None, oplabel=None):
        if width is None:
            width = self.width
        stage_id, raw_data, raw_valid, raw_ready = self.data_visitor.visit(
            data)
        tmp_data, tmp_valid, tmp_ready = self._make_tmp(raw_data, raw_valid, raw_ready,
                                                        width, initval, acc_ops=ops)
        next_stage_id = stage_id + 1 if stage_id is not None else None

        ret = _PipelineVariable(self, next_stage_id, tmp_data, tmp_valid, tmp_ready,
                                data, ops, resetcond, initval, oplabel)

        if resetcond is not None:
            ret.reset(resetcond, initval)

        self.vars.append(ret)

        return ret

    #-------------------------------------------------------------------------
    def _add_reg(self, prefix, count, width=None, initval=0):
        tmp_name = '_'.join(['', self.name, prefix, str(count)])
        tmp = self.m.Reg(tmp_name, width, initval=initval)
        return tmp

    def _add_wire(self, prefix, count, width=None):
        tmp_name = '_'.join(['', self.name, prefix, str(count)])
        tmp = self.m.Wire(tmp_name, width)
        return tmp

    #-------------------------------------------------------------------------
    def _make_tmp(self, data, valid, ready, width=None, initval=0, acc_ops=()):
        tmp_data = self._add_reg(
            'data', self.tmp_count, width=width, initval=initval)

        if valid is not None:
            tmp_valid = self._add_reg('valid', self.tmp_count, initval=0)
        else:
            tmp_valid = None

        if ready:
            tmp_ready = self._add_wire('ready', self.tmp_count)
        else:
            tmp_ready = None

        self.tmp_count += 1

        # all ready
        all_ready = None
        for r in ready:
            if r is None:
                continue
            if all_ready is None:
                all_ready = r
            else:
                all_ready = vtypes.AndList(all_ready, r)

        # data
        data_cond_vars = []
        if valid is not None:
            data_cond_vars.append(valid)
        if tmp_ready is not None:
            data_cond_vars.append(all_ready)
            if tmp_valid is not None:
                data_cond_vars.append(vtypes.OrList(
                    tmp_ready, vtypes.Not(tmp_valid)))
            else:
                data_cond_vars.append(tmp_ready)

        if len(data_cond_vars) == 0:
            data_cond = None
        elif len(data_cond_vars) == 1:
            data_cond = data_cond_vars[0]
        else:
            data_cond = vtypes.AndList(*data_cond_vars)

        # Accumulator
        for op in acc_ops:
            if not isinstance(op, type):
                data = op(tmp_data, data)
            elif issubclass(op, vtypes._BinaryOperator):
                data = op(tmp_data, data)
            elif issubclass(op, vtypes._UnaryOperator):
                data = op(data)

            if not isinstance(data, vtypes._Numeric):
                raise TypeError("Operator '%s' returns unsupported object type '%s'."
                                % (str(op), str(type(data))))

        self.seq.add(tmp_data(data), cond=data_cond)

        # valid
        valid_cond_vars = []
        if tmp_ready is not None:
            valid_cond_vars.append(all_ready)
            ordy = vtypes.OrList(tmp_ready, vtypes.Not(tmp_valid))
            valid_cond_vars.append(ordy)

        if len(valid_cond_vars) == 0:
            valid_cond = None
        elif len(valid_cond_vars) == 1:
            valid_cond = valid_cond_vars[0]
        else:
            valid_cond = vtypes.AndList(*valid_cond_vars)

        if tmp_valid is not None:
            if tmp_ready is not None:
                self.seq.add(tmp_valid(0), cond=vtypes.AndList(
                    tmp_valid, tmp_ready))
            self.seq.add(tmp_valid(valid), cond=valid_cond)

        # ready
        if tmp_ready is not None:
            ordy = vtypes.AndList(vtypes.OrList(
                tmp_ready, vtypes.Not(tmp_valid)), valid)
            for r in ready:
                _connect_ready(self.m, r, ordy)

        return tmp_data, tmp_valid, tmp_ready

    #-------------------------------------------------------------------------
    def _make_prev(self, data, valid, ready, width=None, initval=0):
        tmp_data = self._add_reg(
            'data', self.tmp_count, width=width, initval=initval)
        tmp_valid = valid
        tmp_ready = ready

        self.tmp_count += 1

        if valid is not None and ready is not None:
            data_cond = vtypes.AndList(valid, ready)
        elif valid is not None:
            data_cond = valid
        elif ready is not None:
            data_cond = ready
        else:
            data_cond = None

        self.seq.add(tmp_data(data), cond=data_cond)

        return tmp_data, tmp_valid, tmp_ready

    #-------------------------------------------------------------------------
    def __call__(self, data, initval=0, width=None):
        return self.stage(data, initval=initval, width=width)

#-------------------------------------------------------------------------


class _PipelineInterface(object):

    def __init__(self, data, valid=None, ready=None, output=False):
        self.data = data
        self.valid = valid
        self.ready = ready
        self.output = output

    def __str__(self):
        args = [self.data, self.valid, self.ready]
        return ','.join([str(arg) for arg in args])

#-------------------------------------------------------------------------


class _PipelineNumeric(vtypes._Numeric):
    pass


class _PipelineVariable(_PipelineNumeric):

    def __init__(self, df, stage_id, data, valid=None, ready=None,
                 src_data=None, ops=None, resetcond=None, initval=None, oplabel=None):
        self.df = df
        self.stage_id = stage_id
        self.data = data
        self.valid = valid
        self.ready = ready
        self.output_vars = None
        self.src_data = src_data
        self.dst_data = None
        self.ops = ops
        self.resetcond = resetcond
        self.initval = initval
        self.oplabel = oplabel
        self.prev_dict = {}
        self.preg_dict = {}

        if self.ready is not None:
            ready = vtypes.Int(1)
            _connect_ready(self.df.m, self.ready, ready)

    def prev(self, index, initval=0):
        if index == 0:
            return self
        if index < 0:
            raise ValueError('Index to a previous value must be positive.')

        if index in self.prev_dict:
            return self.prev_dict[index]

        width = vtypes.get_width(self.data)
        p = self

        for i in range(index):
            if (i + 1) in self.prev_dict:
                p = self.prev_dict[i + 1]
                continue

            tmp_data, tmp_valid, tmp_ready = self.df._make_prev(p.data, p.valid, p.ready,
                                                                width, initval)
            p = _PipelineVariable(self.df, p.stage_id,
                                  tmp_data, tmp_valid, tmp_ready, p)
            self.df.vars.append(p)
            self.prev_dict[i + 1] = p

        return p

    def output(self, data, valid=None, ready=None):
        self.output_vars = (data, valid, ready)

    def make_output(self):
        data, valid, ready = self.output_vars

        # Inserting delayed registers
        ovar = self
        if self.stage_id is not None:
            for i in range(self.stage_id, self.df.max_stage_id):
                ovar = self.df.stage(ovar, preg=ovar)

        if not isinstance(data, (vtypes.Wire, vtypes.Output)):
            raise TypeError('Data signal must be Wire, not %s' %
                            str(type(data)))
        else:
            ovar.df.m.Assign(data(ovar.data))

        my_valid = vtypes.Int(1) if ovar.valid is None else ovar.valid
        if valid is None:
            pass
        elif not isinstance(valid, (vtypes.Wire, vtypes.Output)):
            raise TypeError('Valid signal must be Wire, not %s' %
                            str(type(valid)))
        else:
            ovar.df.m.Assign(valid(my_valid))

        if ready is None:
            ready = vtypes.Int(1)

        _connect_ready(ovar.df.m, ovar.ready, ready)

        ovar.dst_data = _PipelineInterface(data, valid, ready, output=True)

    def reset(self, cond, initval=0):
        self.resetcond = cond
        self.initval = initval
        self.df.seq.add(self.data(initval), cond=cond)
        if self.valid is not None:
            self.df.seq.add(self.valid(0), cond=cond)

    def get_width(self):
        return vtypes.get_width(self.data)

    def _add_preg(self, stage_id, var):
        self.preg_dict[stage_id] = var

    def _get_preg(self, stage_id):
        if stage_id is None:
            return self
        if self.stage_id is None:
            return self
        if stage_id == self.stage_id:
            return self
        return self.preg_dict[stage_id]

#-------------------------------------------------------------------------


class _PipelineVisitor(object):

    def generic_visit(self, node):
        raise TypeError("Type %s is not supported." % str(type(node)))

    def visit(self, node):
        if isinstance(node, vtypes._BinaryOperator):
            return self.visit__BinaryOperator(node)

        if isinstance(node, vtypes._UnaryOperator):
            return self.visit__UnaryOperator(node)

        if isinstance(node, vtypes._Variable):
            return self.visit__Variable(node)

        if isinstance(node, vtypes._Constant):
            return self.visit__Constant(node)

        visitor = getattr(
            self, 'visit_' + node.__class__.__name__, self.generic_visit)
        return visitor(node)

    def visit__PipelineVariable(self, node):
        raise NotImplementedError(
            'visit__PipelineVariable() must be implemented')

    def visit__BinaryOperator(self, node):
        raise NotImplementedError(
            'visit__BinaryOperator() must be implemented')

    def visit__UnaryOperator(self, node):
        raise NotImplementedError('visit__UnaryOperator() must be implemented')

    def visit_Pointer(self, node):
        raise NotImplementedError('visit_Pointer() must be implemented')

    def visit_Slice(self, node):
        raise NotImplementedError('visit_Slice() must be implemented')

    def visit_Cat(self, node):
        raise NotImplementedError('visit_Cat() must be implemented')

    def visit_Repeat(self, node):
        raise NotImplementedError('visit_Repeat() must be implemented')

    def visit_Cond(self, node):
        raise NotImplementedError('visit_Cond() must be implemented')

    def visit__Variable(self, node):
        raise NotImplementedError('visit__Variable() must be implemented')

    def visit__Constant(self, node):
        raise NotImplementedError('visit__Constant() must be implemented')

    def visit_bool(self, node):
        raise NotImplementedError('visit__Constant() must be implemented')

    def visit_int(self, node):
        raise NotImplementedError('visit__Constant() must be implemented')

    def visit_str(self, node):
        raise NotImplementedError('visit__Constant() must be implemented')

    def visit_float(self, node):
        raise NotImplementedError('visit__Constant() must be implemented')

#-------------------------------------------------------------------------


class DataVisitor(_PipelineVisitor):

    def __init__(self, df):
        self.df = df

    def pack_valid(self, lvalid, rvalid):
        if rvalid is not None and lvalid is not None:
            return vtypes.AndList(lvalid, rvalid)
        elif rvalid is None and lvalid is None:
            return None
        elif rvalid is None:
            return lvalid
        elif lvalid is None:
            return rvalid
        return None

    def pack_ready(self, lready, rready):
        return lready + rready

    def pack(self, *args):
        rslts = [self.visit(arg) for arg in args]
        all_stage_none = reduce(lambda t, x: t and x is None, [
                                rslt[0] for rslt in rslts], True)

        if all_stage_none:
            data = [rslt[1] for rslt in rslts]
            valid = reduce(self.pack_valid, [rslt[2] for rslt in rslts], None)
            ready = reduce(self.pack_ready, [rslt[3] for rslt in rslts], [])
            return (None, data, valid, ready)

        max_stage = reduce(lambda x, y:
                           None if x is None and y is None else
                           x if x is not None and y is None else
                           y if y is not None and x is None else
                           max(x, y), [rslt[0] for rslt in rslts], None)

        new_args = []
        for rslt, arg in zip(rslts, args):
            stage = rslt[0]
            if stage is None:
                new_args.append(arg)
                continue
            if stage == max_stage:
                new_args.append(arg)
                continue

            diff = max_stage - stage
            p = arg
            for i in range(diff):
                width = vtypes.get_width(rslt[1])
                p = self.df.stage(p, width=width, preg=arg)

            new_args.append(p)

        new_rslts = [self.visit(arg) for arg in new_args]
        data = [rslt[1] for rslt in new_rslts]
        valid = reduce(self.pack_valid, [rslt[2] for rslt in new_rslts], None)
        ready = reduce(self.pack_ready, [rslt[3] for rslt in new_rslts], [])

        return (max_stage, data, valid, ready)

    def make_valid(self, valid, ready):
        if ready is not None and valid is not None:
            next_valid = vtypes.AndList(valid, ready)
        elif ready is not None:
            next_valid = ready
        elif valid is not None:
            next_valid = valid
        else:
            next_valid = None
        return next_valid

    def visit__PipelineVariable(self, node):
        ready = [] if node.ready is None else [node.ready]
        #valid = self.make_valid(node.valid, node.ready)
        valid = node.valid
        return (node.stage_id, node.data, valid, ready)

    def visit__Variable(self, node):
        return (None, node, None, [])

    def visit__Constant(self, node):
        return (None, node, None, [])

    def visit__BinaryOperator(self, node):
        stage, data, valid, ready = self.pack(node.left, node.right)
        cls = type(node)
        return stage, cls(*data), valid, ready

    def visit__UnaryOperator(self, node):
        return self.visit(node.right)

    def visit_Pointer(self, node):
        stage, data, valid, ready = self.pack(node.var, node.pos)
        cls = type(node)
        return stage, cls(*data), valid, ready

    def visit_Slice(self, node):
        stage, data, valid, ready = self.pack(node.var, node.msb, node.lsb)
        cls = type(node)
        return stage, cls(*data), valid, ready

    def visit_Cat(self, node):
        stage, data, valid, ready = self.pack(*node.vars)
        cls = type(node)
        return stage, cls(*data), valid, ready

    def visit_Repeat(self, node):
        stage, data, valid, ready = self.pack(node.var, node.times)
        cls = type(node)
        return stage, cls(*data), valid, ready

    def visit_Cond(self, node):
        stage, data, valid, ready = self.pack(
            node.condition, node.true_value, node.false_value)
        cls = type(node)
        return stage, cls(*data), valid, ready

    def visit_bool(self, node):
        if node:
            return (None, vtypes.Int(1), None, [])
        return (None, vtypes.Int(0), None, [])

    def visit_int(self, node):
        return (None, vtypes.Int(node), None, [])

    def visit_str(self, node):
        return (None, vtypes.Str(node), None, [])

    def visit_float(self, node):
        return (None, vtypes.Float(node), None, [])

#-------------------------------------------------------------------------


def _draw_graph(df, filename='out.png', prog='dot'):
    gg = GraphGenerator(df)
    gg.draw(filename, prog)


class GraphGenerator(_PipelineVisitor):

    def __init__(self, df):
        try:
            import pygraphviz as pgv
        except:
            raise ImportError(
                'Graph generator of lib.Pipeline requires Pygraphviz.')
        self.df = df
        self.graph = pgv.AGraph(directed=True)
        self.visited_node = set()
        self.const_node = []

    def draw(self, filename='out.png', prog='dot'):
        for var in self.df.vars:
            # traverse from only output nodes
            if isinstance(var.dst_data, _PipelineInterface):
                self.visit(var)

        self.graph.write('out.dot')
        self.graph.layout(prog=prog)
        self.graph.draw(filename)

    def _add_node(self, node, label=None, color='black', shape='box', style='solid'):
        self.visited_node.add(id(node))
        if label is None:
            self.graph.add_node(id(node), color=color,
                                shape=shape, style=style)
        else:
            self.graph.add_node(id(node), label=label,
                                color=color, shape=shape, style=style)

    def _add_edge(self, start, end, color='black', label=None, style='solid'):
        if isinstance(start, (bool, int, str, float)):
            # to append multiple first-class objects with same values
            start = copy.deepcopy(vtypes._Constant(start))
            self._add_node(start, label=str(start), shape='invtriangle')
            self.const_node.append(start)

        if isinstance(end, (bool, int, str, float)):
            # to append multiple first-class objects with same values
            end = copy.deepcopy(vtypes._Constant(end))
            self._add_node(end, label=str(end), shape='invtriangle')
            self.const_node.append(end)

        if label:
            self.graph.add_edge(id(start), id(
                end), color=color, label=label, style=style)
        else:
            self.graph.add_edge(id(start), id(end), color=color, style=style)

    def _max_stage_id(self, *args):
        maxval = None
        for arg in args:
            if arg is None or not hasattr(arg, 'stage_id'):
                continue
            if arg.stage_id is None:
                continue
            if maxval is None:
                maxval = arg.stage_id
                continue
            if arg.stage_id > maxval:
                maxval = arg.stage_id
        return maxval

    def _visited(self, node):
        return id(node) in self.visited_node

    def visit(self, node):
        if self._visited(node):
            return None
        return _PipelineVisitor.visit(self, node)

    def visit__PipelineInterface(self, node):
        if node.output:
            self._add_node(node, label=str(node), shape='trapezium')
        else:
            self._add_node(node, label=str(node), shape='invtrapezium')

    def visit__PipelineVariable(self, node):
        # standard
        if node.src_data is not None and not node.ops:
            if node.stage_id is None:
                self._add_node(node, label=str(node.data),
                               shape='box', style='dashed')
            else:
                self._add_node(node, label=''.join(
                    [str(node.stage_id), ':', str(node.data)]), shape='box')
            self.visit(node.src_data)
            self._add_edge(node.src_data, node)
        # accumulator
        if node.src_data is not None and node.ops:
            label = [str(node.stage_id)]
            label.append(':')
            label.append(str(node.data))
            if node.oplabel is not None:
                label.append(' ')
                label.append(node.oplabel)
            else:
                for op in node.ops:
                    if isinstance(op, type):
                        label.append(' ')
                        label.append(vtypes.op2mark(op.__name__))
                    else:
                        label.append(' C')
            label.append('=')
            self._add_node(node, label=''.join(label),
                           shape='box', style='rounded')
            self.visit(node.src_data)
            self._add_edge(node.src_data, node)
            if node.resetcond:
                self.visit(node.resetcond)
                self._add_edge(node.resetcond, node,
                               label='RST', style='dashed')
        if isinstance(node.dst_data, _PipelineInterface):
            self.visit(node.dst_data)
            self._add_edge(node, node.dst_data)

    def visit__Variable(self, node):
        self._add_node(node, label=node.name, shape='invtriangle')

    def visit__Constant(self, node):
        self._add_node(node, label=node.value, shape='invtriangle')

    def visit__BinaryOperator(self, node):
        mark = vtypes.op2mark(node.__class__.__name__)
        self._add_node(node, label=mark, shape='ellipse')
        maxid = self._max_stage_id(node.left, node.right)
        left = node.left
        right = node.right
        if hasattr(left, '_get_preg'):
            left = left._get_preg(maxid)
        if hasattr(right, '_get_preg'):
            right = right._get_preg(maxid)
        self.visit(left)
        self.visit(right)
        self._add_edge(left, node, label='L')
        self._add_edge(right, node, label='R')

    def visit__UnaryOperator(self, node):
        mark = vtypes.op2mark(node.__class__.__name__)
        self._add_node(node, label=mark, shape='ellipse')
        self.visit(node.right)
        self._add_edge(node.right, node)

    def visit_Pointer(self, node):
        mark = 'sel'
        self._add_node(node, label=mark, shape='ellipse')
        maxid = self._max_stage_id(node.var, node.pos)
        var = node.var
        pos = node.pos
        if hasattr(var, '_get_preg'):
            var = var._get_preg(maxid)
        if hasattr(pos, '_get_preg'):
            pos = pos._get_preg(maxid)
        self.visit(var)
        self.visit(pos)
        self._add_edge(var, node, label='V')
        self._add_edge(pos, node, label='P', style='dashed')

    def visit_Slice(self, node):
        mark = 'slice'
        self._add_node(node, label=mark, shape='ellipse')
        maxid = self._max_stage_id(node.var, node.msb, node.lsb)
        var = node.var
        msb = node.msb
        lsb = node.lsb
        if hasattr(var, '_get_preg'):
            var = var._get_preg(maxid)
        if hasattr(msb, '_get_preg'):
            msb = msb._get_preg(maxid)
        if hasattr(lsb, '_get_preg'):
            lsb = lsb._get_preg(maxid)
        self.visit(var)
        self.visit(msb)
        self.visit(lsb)
        self._add_edge(var, node, label='V')
        self._add_edge(msb, node, label='M', style='dashed')
        self._add_edge(lsb, node, label='L', style='dashed')

    def visit_Cat(self, node):
        mark = 'cat'
        self._add_node(node, label=mark, shape='ellipse')
        maxid = self._max_stage_id(*node.vars)
        for var in node.vars:
            if hasattr(var, '_get_preg'):
                var = var._get_preg(maxid)
            self.visit(var)
            self._add_edge(var, node)

    def visit_Repeat(self, node):
        mark = 'repeat'
        self._add_node(node, label=mark, shape='ellipse')
        maxid = self._max_stage_id(node.var, node.times)
        var = node.var
        times = node.times
        if hasattr(var, '_get_preg'):
            var = var._get_preg(maxid)
        if hasattr(times, '_get_preg'):
            times = times._get_preg(maxid)
        self.visit(var)
        self.visit(times)
        self._add_edge(var, node, label='V')
        self._add_edge(times, node, label='T', style='dashed')

    def visit_Cond(self, node):
        mark = 'cond'
        self._add_node(node, label=mark, shape='ellipse')
        maxid = self._max_stage_id(
            node.condition, node.true_value, node.false_value)
        condition = node.condition
        true_value = node.true_value
        false_value = node.false_value
        if hasattr(condition, '_get_preg'):
            condition = condition._get_preg(maxid)
        if hasattr(true_value, '_get_preg'):
            true_value = true_value._get_preg(maxid)
        if hasattr(false_value, '_get_preg'):
            false_value = false_value._get_preg(maxid)
        self.visit(condition)
        self.visit(true_value)
        self.visit(false_value)
        self._add_edge(condition, node, label='C', style='dashed')
        self._add_edge(true_value, node, label='T')
        self._add_edge(false_value, node, label='F')

    def visit_bool(self, node):
        pass
        #self._add_node(node, label=str(node), shape='invtriangle')

    def visit_int(self, node):
        pass
        #self._add_node(node, label=str(node), shape='invtriangle')

    def visit_str(self, node):
        pass
        #self._add_node(node, label=str(node), shape='invtriangle')

    def visit_float(self, node):
        pass
        #self._add_node(node, label=str(node), shape='invtriangle')
