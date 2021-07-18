from __future__ import absolute_import
from __future__ import print_function
import os
import sys
import collections
import functools

import veriloggen.core.vtypes as vtypes
from veriloggen.core.module import Module
from veriloggen.core.submodule import Submodule
from veriloggen.seq.subst_visitor import *
from veriloggen.seq.reset_visitor import ResetVisitor
from veriloggen.seq.seq import Seq, make_condition


_tmp_count = 0


def reset():
    global _tmp_count
    _tmp_count = 0


def _tmp_name(prefix='_tmp_fsm'):
    global _tmp_count
    v = _tmp_count
    _tmp_count += 1
    ret = '_'.join([prefix, str(v)])
    return ret


def TmpFSM(m, clk, rst, width=32, initname='init',
           nohook=False, as_module=False, prefix=None):
    if prefix is None:
        prefix = '_tmp_fsm'
    name = _tmp_name(prefix)
    return FSM(m, name, clk, rst, width, initname, nohook, as_module)


class FSM(vtypes.VeriloggenNode):
    """ Finite State Machine Generator """

    def __init__(self, m, name, clk, rst, width=32, initname='init',
                 nohook=False, as_module=False):
        self.m = m
        self.name = name
        self.clk = clk
        self.rst = rst
        self.width = width
        self.state_count = 0
        self.state = self.m.Reg(name, width)  # set initval later

        self.mark = collections.OrderedDict()  # key:index
        self._set_mark(0, self.name + '_' + initname)
        self.state.initval = self._get_mark(0)

        self.body = collections.defaultdict(list)
        self.jump = collections.defaultdict(list)

        self.delay_amount = 0
        self.delayed_state = collections.OrderedDict()  # key:delay
        self.delayed_body = collections.defaultdict(
            functools.partial(collections.defaultdict, list))  # key:delay
        self.delayed_cond = collections.OrderedDict()  # key:name
        self.tmp_count = 0

        self.dst_var = collections.OrderedDict()
        self.dst_visitor = SubstDstVisitor()
        self.reset_visitor = ResetVisitor()

        self.seq = Seq(self.m, self.name + '_par', clk, rst, nohook=True)

        self.done = False

        self.last_cond = []
        self.last_kwargs = {}
        self.last_if_statement = None
        self.next_else = False
        self.elif_cond = None
        self.next_kwargs = {}

        self.as_module = as_module

        if not nohook:
            self.m.add_hook(self.implement)

    # -------------------------------------------------------------------------
    def goto(self, dst, cond=None, else_dst=None):
        if cond is None and 'cond' in self.next_kwargs:
            cond = self.next_kwargs['cond']

        if 'index' in self.next_kwargs:
            index = self.next_kwargs['index']
        else:
            index = None

        self._clear_next_kwargs()
        # self._clear_last_if_statement()
        # self._clear_last_cond()
        # self._clear_elif_cond()

        if index is None:
            src = self.current
        else:
            src = index

        self._go(src, dst, cond, else_dst)
        return dst

    def goto_init(self, cond=None):
        if cond is None and 'cond' in self.next_kwargs:
            cond = self.next_kwargs['cond']

        if 'index' in self.next_kwargs:
            index = self.next_kwargs['index']
        else:
            index = None

        self._clear_next_kwargs()
        # self._clear_last_if_statement()
        # self._clear_last_cond()
        # self._clear_elif_cond()

        if index is None:
            src = self.current
        else:
            src = index

        dst = 0
        self._go(src, dst, cond)
        return dst

    def goto_next(self, cond=None):
        if cond is None and 'cond' in self.next_kwargs:
            cond = self.next_kwargs['cond']

        if 'index' in self.next_kwargs:
            index = self.next_kwargs['index']
        else:
            index = None

        self._clear_next_kwargs()
        # self._clear_last_if_statement()
        # self._clear_last_cond()
        # self._clear_elif_cond()

        if index is None:
            src = self.current
        else:
            src = index

        dst = src + 1
        self._go(src, dst, cond=cond)
        self.inc()
        return dst

    def goto_from(self, src, dst, cond=None, else_dst=None):
        if cond is None and 'cond' in self.next_kwargs:
            cond = self.next_kwargs['cond']

        self._clear_next_kwargs()
        # self._clear_last_if_statement()
        # self._clear_last_cond()
        # self._clear_elif_cond()

        self._go(src, dst, cond, else_dst)
        return dst

    def inc(self):
        return self._set_index(None)

    # -------------------------------------------------------------------------
    def add(self, *statement, **kwargs):
        """ Adding new assignments. This method is usually called via __call__(). """
        kwargs.update(self.next_kwargs)
        self.last_kwargs = kwargs
        self._clear_next_kwargs()

        # if there is no attributes, Elif object is reused.
        has_args = not (len(kwargs) == 0 or  # has no args
                        (len(kwargs) == 1 and 'cond' in kwargs) or  # has only 'cond'
                        (len(kwargs) == 1 and 'index' in kwargs) or  # has only 'index'
                        (len(kwargs) == 2 and
                         'cond' in kwargs and 'index' in kwargs))  # has only 'cond' and 'index'

        if self.elif_cond is not None and not has_args:
            next_call = self.last_if_statement.Elif(self.elif_cond)
            next_call(*statement)
            self.last_if_statement = next_call
            self._add_dst_var(statement)
            self._clear_elif_cond()
            return self

        if self.next_else and not has_args:
            next_call = self.last_if_statement.Else
            next_call(*statement)
            self._add_dst_var(statement)
            self._clear_last_if_statement()
            self._clear_elif_cond()
            return self

        self._clear_last_if_statement()
        return self._add_statement(statement, **kwargs)

    # -------------------------------------------------------------------------
    def add_reset(self, v):
        return self.seq.add_reset(v)

    # -------------------------------------------------------------------------
    def Prev(self, var, delay, initval=0, cond=None, prefix=None):
        return self.seq.Prev(var, delay, initval, cond, prefix)

    # -------------------------------------------------------------------------
    def If(self, *cond):
        self._clear_elif_cond()

        cond = make_condition(*cond)

        if cond is None:
            return self

        if 'cond' not in self.next_kwargs:
            self.next_kwargs['cond'] = cond
        else:
            self.next_kwargs['cond'] = vtypes.Ands(
                self.next_kwargs['cond'], cond)

        self.last_cond = [self.next_kwargs['cond']]

        return self

    @property
    def Else(self):
        self._clear_elif_cond()

        if len(self.last_cond) == 0:
            raise ValueError("No previous condition for Else.")

        old = self.last_cond.pop()
        self.last_cond.append(vtypes.Not(old))

        # if the true-statement has delay attributes,
        # Else statement is separated.
        if 'delay' in self.last_kwargs and self.last_kwargs['delay'] > 0:
            prev_cond = self.last_cond
            ret = self.Then()
            self.last_cond = prev_cond
            return ret

        # if not isinstance(self.last_if_statement, vtypes.If):
        #     raise ValueError("Last if-statement is not If")

        # self.next_else = True

        if isinstance(self.last_if_statement, vtypes.If):
            self.next_else = True

        cond = self._make_cond(self.last_cond)
        self.next_kwargs['cond'] = cond

        return self

    def Elif(self, *cond):
        if len(self.last_cond) == 0:
            raise ValueError("No previous condition for Else.")

        cond = make_condition(*cond)

        old = self.last_cond.pop()
        self.last_cond.append(vtypes.Not(old))
        self.last_cond.append(cond)

        # if the true-statement has delay attributes,
        # Else statement is separated.
        if 'delay' in self.last_kwargs and self.last_kwargs['delay'] > 0:
            prev_cond = self.last_cond
            ret = self.Then()
            self.last_cond = prev_cond
            return ret

        # if not isinstance(self.last_if_statement, vtypes.If):
        #     raise ValueError("Last if-statement is not If")

        # self.elif_cond = cond

        if isinstance(self.last_if_statement, vtypes.If):
            self.elif_cond = cond

        cond = self._make_cond(self.last_cond)
        self.next_kwargs['cond'] = cond

        return self

    def Then(self):
        cond = self._make_cond(self.last_cond)
        self._clear_last_cond()
        self.If(cond)
        return self

    def Delay(self, delay):
        self.next_kwargs['delay'] = delay
        return self

    def Keep(self, keep):
        self.next_kwargs['keep'] = keep
        return self

    def LazyCond(self, value=True):
        self.next_kwargs['lazy_cond'] = value
        return self

    def EagerVal(self, value=True):
        self.next_kwargs['eager_val'] = value
        return self

    def When(self, index):
        self.next_kwargs['index'] = index
        return self

    def State(self, index=None):
        if index is None:
            index = fsm.current
        return State(self, index)

    def Clear(self):
        self._clear_next_kwargs()
        self._clear_last_if_statement()
        self._clear_last_cond()
        self._clear_elif_cond()
        return self

    # -------------------------------------------------------------------------
    @property
    def Always(self):
        return self.seq

    @property
    def init(self):
        return 0

    @property
    def current(self):
        return self.state_count

    @property
    def next(self):
        return self.state_count + 1

    @property
    def current_delay(self):
        if 'delay' in self.next_kwargs:
            return self.next_kwargs['delay']
        return 0

    @property
    def last_delay(self):
        if 'delay' in self.last_kwargs:
            return self.last_kwargs['delay']
        return 0

    @property
    def current_condition(self):
        cond = self.next_kwargs['cond'] if 'cond' in self.next_kwargs else None
        if cond is not None:
            cond = vtypes.AndList(self.state == self.state_count, cond)
        else:
            cond = self.state == self.state_count
        return cond

    @property
    def last_condition(self):
        cond = self._make_cond(self.last_cond)
        if cond is not None:
            cond = vtypes.AndList(self.state == self.state_count, cond)
        else:
            cond = self.state == self.state_count
        return cond

    @property
    def then(self):
        return self.last_condition

    @property
    def here(self):
        return self.state == self.current

    # -------------------------------------------------------------------------
    def implement(self):
        if self.as_module:
            self.make_module()
            return

        self.make_always()

    # -------------------------------------------------------------------------
    def make_always(self, reset=(), body=(), case=True):
        if self.done:
            #raise ValueError('make_always() has been already called.')
            return

        self.done = True

        part_reset = self.make_reset(reset)
        part_body = list(body) + list(self.make_case()
                                      if case else self.make_if())
        self.m.Always(vtypes.Posedge(self.clk))(
            vtypes.If(self.rst)(
                part_reset,
            )(
                part_body,
            ))

    # -------------------------------------------------------------------------
    def make_module(self, reset=(), body=(), case=True):
        if self.done:
            #raise ValueError('make_always() has been already called.')
            return

        self.done = True

        m = Module('sub_%s' % self.name)

        clk = m.Input('CLK')

        if self.rst is not None:
            rst = m.Input('RST')
        else:
            rst = None

        body = list(body) + list(self.make_case()
                                 if case else self.make_if())
        dst_var = self.seq.dst_var
        dst_var.update(self.dst_var)
        dsts = dst_var.values()
        src_visitor = SubstSrcVisitor()

        # collect sources in destination variable definitions
        for dst in dsts:
            if isinstance(dst, (vtypes.Pointer, vtypes.Slice, vtypes.Cat)):
                raise ValueError(
                    'Partial assignment is not supported by as_module mode.')

            if isinstance(dst, vtypes._Variable):
                if dst.width is not None:
                    src_visitor.visit(dst.width)
                if dst.dims is not None:
                    for dim in dst.dims:
                        src_visitor.visit(dim)

        # collect sources in statements
        for statement in body:
            src_visitor.visit(statement)

        srcs = src_visitor.srcs.values()

        # collect sources in source variable definitions
        for src in srcs:
            if isinstance(src, vtypes._Variable):
                if src.width is not None:
                    src_visitor.visit(src.width)
                if src.dims is not None:
                    for dim in src.dims:
                        src_visitor.visit(dim)

        srcs = src_visitor.srcs.values()

        params = collections.OrderedDict()
        ports = collections.OrderedDict()
        src_rename_dict = collections.OrderedDict()

        fsm_orig_labels = [v.name for v in self.mark.values()]
        fsm_labels = collections.OrderedDict()

        # create parameter/localparam definitions
        for src in srcs:
            if isinstance(src, (vtypes.Parameter, vtypes.Localparam)):
                if src.name in fsm_orig_labels:
                    fsm_labels[src.name] = m.Localparam(src.name, src.value)
                    continue

                arg_name = src.name
                v = m.Parameter(arg_name, src.value, src.width, src.signed)
                src_rename_dict[src.name] = v
                params[arg_name] = src

        src_rename_visitor = SrcRenameVisitor(src_rename_dict)

        state_width = src_rename_visitor.visit(self.state.width)
        state_initval = src_rename_visitor.visit(self.state.initval)
        state = m.OutputReg(self.state.name, state_width,
                            initval=state_initval)
        out_state = self.m.TmpWire(state_width,
                                   prefix='_%s_out' % self.state.name)
        self.m.Always()(self.state(out_state, blk=True))
        ports[state.name] = out_state

        src_rename_dict[self.state.name] = state

        for delay, s in sorted(self.delayed_state.items(), key=lambda x: x[0]):
            s_width = src_rename_visitor.visit(s.width)
            s_initval = src_rename_visitor.visit(s.initval)
            d = m.OutputReg(s.name, s_width, initval=s_initval)
            out_d = self.m.TmpWire(s_width, prefix='_%s_out' % d.name)
            self.m.Always()(s(out_d, blk=True))
            ports[s.name] = out_d

        state_names = [self.state.name]
        state_names.extend([s.name for s in self.delayed_state.values()])

        for src in srcs:
            if isinstance(src, (vtypes.Parameter, vtypes.Localparam)):
                continue

            if src.name in state_names:
                continue

            if src.name in list(self.delayed_cond.keys()):
                rep_width = (src_rename_visitor.visit(src.width)
                             if src.width is not None else None)
                v = m.Reg(src.name, rep_width, initval=0)
                src_rename_dict[src.name] = v
                continue

            arg_name = 'i_%s' % src.name

            if src.dims is not None:
                # outside FSM-module
                width = src.get_width()
                dims = src.dims
                length = None
                for dim in dims:
                    if length is None:
                        length = dim
                    else:
                        length *= dim
                pack_width = vtypes.Mul(width, length)
                out_line = self.m.TmpWire(pack_width, prefix='_%s' % self.name)

                g = self.m
                s = src
                a = None
                for d, dim in enumerate(dims):
                    i = g.TmpGenvar(prefix='i')
                    g = g.GenerateFor(i(0), i < dim, i(i + 1))
                    s = vtypes.Pointer(s, i)
                    b = None
                    for dm in dims[d + 1:]:
                        if b is None:
                            b = dm
                        else:
                            b *= dm
                    if a is None:
                        if b is None:
                            a = i
                        else:
                            a = i * b
                    else:
                        if b is None:
                            a += i
                        else:
                            a += i * b

                v = out_line[a * width:(a + 1) * width]
                p = g.Assign(v(s))

                # inside FSM-module
                rep_width = (src_rename_visitor.visit(src.width)
                             if src.width is not None else None)
                rep_dims = src_rename_visitor.visit(src.dims)
                rep_length = None
                for rep_dim in rep_dims:
                    if rep_length is None:
                        rep_length = rep_dim
                    else:
                        rep_length *= rep_dim
                pack_width = (rep_length if rep_width is None else
                              vtypes.Mul(rep_length, rep_width))
                in_line = m.Input(arg_name + '_line', pack_width,
                                  signed=src.get_signed())
                in_array = m.Wire(arg_name, rep_width, rep_length,
                                  signed=src.get_signed())

                g = m
                ia = in_array
                a = None
                for rep_dim in rep_dims:
                    i = g.TmpGenvar(prefix='i')
                    g = g.GenerateFor(i(0), i < rep_dim, i(i + 1))
                    ia = vtypes.Pointer(ia, i)
                    b = None
                    for rep_dm in rep_dims[d + 1:]:
                        if b is None:
                            b = rep_dm
                        else:
                            b *= rep_dm
                    if a is None:
                        if b is None:
                            a = i
                        else:
                            a = i * b
                    else:
                        if b is None:
                            a += i
                        else:
                            a += i * b

                v = in_line[a * rep_width:(a + 1) * rep_width]
                p = g.Assign(ia(v))

                src_rename_dict[src.name] = in_array
                ports[in_line.name] = out_line

            else:
                rep_width = (src_rename_visitor.visit(src.width)
                             if src.width is not None else None)
                v = m.Input(arg_name, rep_width, signed=src.get_signed())

                src_rename_dict[src.name] = v
                ports[arg_name] = src

        for dst in dsts:
            if dst.name in list(self.delayed_cond.keys()):
                continue

            arg_name = dst.name

            rep_width = (src_rename_visitor.visit(dst.width)
                         if dst.width is not None else None)
            out = m.OutputReg(arg_name, rep_width, signed=dst.get_signed())
            out_wire = self.m.TmpWire(rep_width, signed=dst.get_signed(),
                                      prefix='_%s_%s' % (self.name, arg_name))
            self.m.Always()(dst(out_wire, blk=True))
            ports[arg_name] = out_wire

        body = [src_rename_visitor.visit(statement)
                for statement in body]

        reset = self.make_reset(reset)

        if not reset and not body:
            pass
        elif not reset or rst is None:
            m.Always(vtypes.Posedge(clk))(
                body,
            )
        else:
            m.Always(vtypes.Posedge(clk))(
                vtypes.If(rst)(
                    reset,
                )(
                    body,
                ))

        arg_params = [(name, param) for name, param in params.items()]

        arg_ports = [('CLK', self.clk)]
        if self.rst is not None:
            arg_ports.append(('RST', self.rst))

        arg_ports.extend([(name, port) for name, port in ports.items()])

        sub = Submodule(self.m, m, 'inst_' + m.name, '_%s_' % self.name,
                        arg_params=arg_params, arg_ports=arg_ports)

    # -------------------------------------------------------------------------
    def make_case(self):
        indexes = set(self.body.keys())
        indexes.update(set(self.jump.keys()))

        for index in indexes:
            self._add_mark(index)

        ret = []
        ret.extend(self.seq.make_code())
        ret.extend(self._get_delayed_substs())

        for delay, dct in sorted(self.delayed_body.items(),
                                 key=lambda x: x[0], reverse=True):
            body = tuple([self._get_delayed_when_statement(index, delay)
                          for index in sorted(dct.keys(), key=lambda x:x)])
            case = vtypes.Case(self._get_delayed_state(delay))(*body)
            ret.append(case)

        body = tuple([self._get_when_statement(index)
                      for index in sorted(indexes, key=lambda x:x)])
        case = vtypes.Case(self.state)(*body)

        if len(case.statement) > 0:
            ret.append(case)

        return ret

    def make_if(self):
        indexes = set(self.body.keys())
        indexes.update(set(self.jump.keys()))

        for index in indexes:
            self._add_mark(index)

        ret = []
        ret.extend(self.seq.make_code())
        ret.extend(self._get_delayed_substs())

        for delay, dct in sorted(self.delayed_body.items(),
                                 key=lambda x: x[0], reverse=True):
            ret.append([self._get_delayed_if_statement(index, delay)
                        for index in sorted(dct.keys(), key=lambda x:x)])

        ret.extend([self._get_if_statement(index)
                    for index in sorted(indexes, key=lambda x:x)])
        return ret

    # -------------------------------------------------------------------------
    def make_reset(self, reset):
        ret = collections.OrderedDict()

        for v in reset:
            if not isinstance(v, vtypes.Subst):
                raise TypeError(
                    'make_reset requires Subst, not %s' % str(type(v)))
            key = str(v.left)
            if key not in ret:
                ret[key] = v

        v = self.reset_visitor.visit(self.state)
        key = str(self.state)
        if v is not None and key not in ret:
            ret[key] = v

        for dst in self.delayed_state.values():
            v = self.reset_visitor.visit(dst)
            if v is None:
                continue
            key = str(v.left)
            if key not in ret:
                ret[key] = v

        for dst in self.dst_var.values():
            v = self.reset_visitor.visit(dst)
            if v is None:
                continue
            key = str(v.left)
            if key not in ret:
                ret[key] = v

        for v in self.seq.make_reset():
            if not isinstance(v, vtypes.Subst):
                raise TypeError(
                    'make_reset requires Subst, not %s' % str(type(v)))
            key = str(v.left)
            if key not in ret:
                ret[key] = v

        return list(ret.values())

    # -------------------------------------------------------------------------
    def set_index(self, index):
        return self._set_index(index)

    # -------------------------------------------------------------------------
    def _go(self, src, dst, cond=None, else_dst=None):
        self._add_jump(src, dst, cond, else_dst)
        return self

    def _add_jump(self, src, dst, cond=None, else_dst=None):
        self.jump[src].append((dst, cond, else_dst))

    # -------------------------------------------------------------------------
    def _add_statement(self, statement, index=None, keep=None, delay=None, cond=None,
                       lazy_cond=False, eager_val=False, no_delay_cond=False):

        cond = make_condition(cond)
        index = self._to_index(index) if index is not None else self.current

        if keep is not None:
            for i in range(keep):
                new_delay = i if delay is None else delay + i
                self._add_statement(statement, index=index,
                                    keep=None, delay=new_delay, cond=cond,
                                    lazy_cond=lazy_cond, eager_val=eager_val,
                                    no_delay_cond=no_delay_cond)
            return self

        if delay is not None and delay > 0:
            self._add_delayed_state(delay)

            if eager_val:
                statement = [self._add_delayed_subst(s, index, delay)
                             for s in statement]

            if not no_delay_cond:
                if cond is None:
                    cond = 1

                if not lazy_cond:
                    cond = self._add_delayed_cond(cond, index, delay)

                else:  # lazy condition
                    t = self._add_delayed_cond(1, index, delay)
                    if isinstance(cond, int) and cond == 1:
                        cond = t
                    else:
                        cond = vtypes.Ands(t, cond)

                statement = [vtypes.If(cond)(*statement)]

            self.delayed_body[delay][index].extend(statement)
            self._add_dst_var(statement)

            return self

        if cond is not None:
            statement = [vtypes.If(cond)(*statement)]
            self.last_if_statement = statement[0]

        self.body[index].extend(statement)
        self._add_dst_var(statement)

        return self

    # -------------------------------------------------------------------------
    def _add_dst_var(self, statement):
        for s in statement:
            values = self.dst_visitor.visit(s)
            for v in values:
                k = str(v)
                if k not in self.dst_var:
                    self.dst_var[k] = v

    # -------------------------------------------------------------------------
    def _add_delayed_cond(self, statement, index, delay):
        name_prefix = '_'.join(
            ['', self.name, 'cond', str(index), str(self.tmp_count)])
        self.tmp_count += 1
        prev = statement
        for i in range(delay):
            tmp_name = '_'.join([name_prefix, str(i + 1)])
            tmp = self.m.Reg(tmp_name, initval=0)
            self.delayed_cond[tmp_name] = tmp
            self._add_statement([tmp(prev)], delay=i, no_delay_cond=True)
            prev = tmp
        return prev

    # -------------------------------------------------------------------------
    def _add_delayed_subst(self, subst, index, delay):
        if not isinstance(subst, vtypes.Subst):
            return subst
        left = subst.left
        right = subst.right
        if isinstance(right, (bool, int, float, str,
                              vtypes._Constant, vtypes._ParameterVariable)):
            return subst
        width = vtypes.get_width(left)
        signed = vtypes.get_signed(left)
        prev = right

        name_prefix = ('_'.join(['', left.name, str(index), str(self.tmp_count)])
                       if isinstance(left, vtypes._Variable) else
                       '_'.join(['', self.name, 'sbst', str(index), str(self.tmp_count)]))
        self.tmp_count += 1

        for i in range(delay):
            tmp_name = '_'.join([name_prefix, str(i + 1)])
            tmp = self.m.Reg(tmp_name, width, initval=0, signed=signed)
            self._add_statement([tmp(prev)], delay=i, no_delay_cond=True)
            prev = tmp
        return left(prev)

    # -------------------------------------------------------------------------
    def _clear_next_kwargs(self):
        self.next_kwargs = {}

    def _clear_last_if_statement(self):
        self.last_if_statement = None
        self.next_else = False

    def _clear_last_cond(self):
        self.last_cond = []

    def _clear_elif_cond(self):
        self.elif_cond = None

    def _make_cond(self, condlist):
        ret = None
        for cond in condlist:
            if ret is None:
                ret = cond
            else:
                ret = vtypes.Ands(ret, cond)
        return ret

    # -------------------------------------------------------------------------
    def _set_index(self, index=None):
        self._clear_next_kwargs()
        self._clear_last_if_statement()
        self._clear_last_cond()
        self._clear_elif_cond()

        if index is None:
            self.state_count += 1
            return self.state_count

        self.state_count = index
        return self.state_count

    def _get_mark(self, index=None):
        if index is None:
            index = self.state_count
        if index not in self.mark:
            raise KeyError("No such index in FSM marks: %s" % index)
        return self.mark[index]

    def _set_mark(self, index=None, name=None):
        if index is None:
            index = self.state_count
        if name is None:
            name = self.name + '_' + str(index)
        self.mark[index] = self.m.Localparam(name, index)

    def _get_mark_index(self, s):
        for index, m in self.mark.items():
            if m.name == s.name:
                return index
        raise KeyError("No such mark in FSM marks: %s" % s.name)

    # -------------------------------------------------------------------------
    def _add_mark(self, index):
        index = self._to_index(index)
        if index not in self.mark:
            self._set_mark(index)
        mark = self._get_mark(index)
        return mark

    def _to_index(self, index):
        if not isinstance(index, int):
            index = self._get_mark_index(index)
        return index

    # -------------------------------------------------------------------------
    def _add_delayed_state(self, value):
        if not isinstance(value, int):
            raise TypeError("Delay amount must be int, not '%s'" %
                            str(type(value)))

        if value < 0:
            raise ValueError("Delay amount must be positive number")

        if value == 0:
            return self.state

        if value <= self.delay_amount:
            return self._get_delayed_state(value)

        for i in range(self.delay_amount + 1, value + 1):
            d = self.m.Reg(''.join(['_d', str(i), '_', self.name]), self.width,
                           initval=self._get_mark(0))
            self.delayed_state[i] = d

        self.delay_amount = value
        return d

    def _get_delayed_state(self, value):
        if value == 0:
            return self.state
        if value not in self.delayed_state:
            raise IndexError('No such index %d in delayed state' % value)
        return self.delayed_state[value]

    def _get_delayed_substs(self):
        ret = []
        prev = self.state
        for d in range(1, self.delay_amount + 1):
            ret.append(vtypes.Subst(self.delayed_state[d], prev))
            prev = self.delayed_state[d]
        return ret

    def _init_delayed_state(self):
        ret = []
        for d in range(1, self.delay_amount + 1):
            ret.append(vtypes.Subst(self.delayed_state[d], self._get_mark(0)))
        return ret

    def _to_state_assign(self, dst, cond=None, else_dst=None):
        dst_mark = self._get_mark(dst)
        value = self.state(dst_mark)
        if cond is not None:
            value = vtypes.If(cond)(value)
            if else_dst is not None:
                else_dst_mark = self._get_mark(else_dst)
                value = value.Else(self.state(else_dst_mark))
        return value

    # -------------------------------------------------------------------------
    def _cond_case(self, index):
        if index not in self.mark:
            self._set_mark(index)
        return self._get_mark(index)

    def _cond_if(self, index):
        if index not in self.mark:
            self._set_mark(index)
        return (self.state == self._get_mark(index))

    def _delayed_cond_if(self, index, delay):
        if index not in self.mark:
            self._set_mark(index)
        if delay > 0 and delay not in self.delayed_state:
            self._add_delayed_state(delay)
        return (self._get_delayed_state(delay) == self._get_mark(index))

    def _get_when_statement(self, index):
        body = []
        body.extend(self.body[index])
        for dst, cond, else_dst in self.jump[index]:
            self._add_mark(dst)
            if else_dst is not None:
                self._add_mark(else_dst)
            body.append(self._to_state_assign(dst, cond, else_dst))
        return vtypes.When(self._cond_case(index))(*body)

    def _get_delayed_when_statement(self, index, delay):
        return vtypes.When(self._cond_case(index))(*self.delayed_body[delay][index])

    def _get_if_statement(self, index):
        body = []
        body.extend(self.body[index])
        for dst, cond, else_dst in self.jump[index]:
            self._add_mark(dst)
            if else_dst is not None:
                self._add_mark(else_dst)
            body.append(self._to_state_assign(dst, cond, else_dst))
        return vtypes.If(self._cond_if(index))(*body)

    def _get_delayed_if_statement(self, index, delay):
        return vtypes.If(self._delayed_cond_if(index, delay))(*self.delayed_body[delay][index])

    # -------------------------------------------------------------------------
    def __call__(self, *statement, **kwargs):
        return self.add(*statement, **kwargs)

    def __getitem__(self, index):
        return self.body[index]

    def __len__(self):
        return self.state_count + 1


class State(vtypes.VeriloggenNode):
    """ FSM with a specic state index """

    def __init__(self, fsm, index):
        while isinstance(fsm, State):
            fsm = fsm.fsm

        while isinstance(index, State):
            index = index.index

        if not isinstance(fsm, FSM):
            raise TypeError("'fsm' must be FSM, not '%s'" % str(type(fsm)))

        if not isinstance(index, int):
            raise TypeError("'index' must be int, not '%s'" % str(type(index)))

        self.fsm = fsm
        self.index = index

    def __getattr__(self, attr):
        self.fsm.When(self.index)
        return getattr(self.fsm, attr)

    def __call__(self, *statement, **kwargs):
        self.fsm.When(self.index)
        return self.fsm.__call__(*statement, **kwargs)

    def __add__(self, r):
        if isinstance(r, State):
            r = r.index

        return self.index + r

    def __sub__(self, r):
        if isinstance(r, State):
            r = r.index

        return self.index - r
