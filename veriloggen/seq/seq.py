from __future__ import absolute_import
from __future__ import print_function
import os
import sys
import collections

import veriloggen.core.vtypes as vtypes
from veriloggen.core.module import Module
from veriloggen.core.submodule import Submodule
from veriloggen.seq.subst_visitor import *
from veriloggen.seq.reset_visitor import ResetVisitor


_tmp_count = 0


def reset():
    global _tmp_count
    _tmp_count = 0


def _tmp_name(prefix='_tmp_seq'):
    global _tmp_count
    v = _tmp_count
    _tmp_count += 1
    ret = '_'.join([prefix, str(v)])
    return ret


def make_condition(*cond):
    _cond = []
    for c in cond:
        if isinstance(c, (tuple, list)):
            _cond.extend(c)
        else:
            _cond.append(c)

    cond = _cond

    if not cond:
        return None

    ret = None
    for c in cond:
        c = _get_manager_cond(c)
        if ret is None:
            ret = c
        else:
            ret = vtypes.Ands(ret, c) if c is not None else ret

    return ret


def _get_manager_cond(cond):
    if hasattr(cond, 'current_condition'):
        cond = getattr(cond, 'current_condition', None)
    if cond is not None and not isinstance(cond, (vtypes._Numeric, int, bool)):
        raise TypeError("Unsupported condition type '%s'" % str(type(cond)))
    return cond


def TmpSeq(m, clk, rst=None, nohook=False, as_module=False, prefix=None):
    if prefix is None:
        prefix = '_tmp_seq'
    name = _tmp_name(prefix)
    return Seq(m, name, clk, rst, nohook, as_module)


class Seq(vtypes.VeriloggenNode):
    """ Sequential Logic Manager """

    def __init__(self, m, name, clk, rst=None, nohook=False, as_module=False):
        self.m = m
        self.name = name
        self.clk = clk
        self.rst = rst

        self.tmp_count = 0
        self.delay_amount = 0
        self.delayed_body = collections.defaultdict(list)
        self.prev_dict = collections.OrderedDict()
        self.body = []

        self.dst_var = collections.OrderedDict()
        self.dst_visitor = SubstDstVisitor()
        self.reset_visitor = ResetVisitor()

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
    def add(self, *statement, **kwargs):
        """ Adding new assignments. This method is usually called via __call__(). """
        kwargs.update(self.next_kwargs)
        self.last_kwargs = kwargs
        self._clear_next_kwargs()

        # if there is no attributes, Elif object is reused.
        has_args = not (len(kwargs) == 0 or  # has no args
                        (len(kwargs) == 1 and 'cond' in kwargs))  # has only 'cond'

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
        k = str(v)
        if k not in self.dst_var:
            self.dst_var[k] = v

    # -------------------------------------------------------------------------
    def Prev(self, var, delay, initval=0, cond=None, prefix=None):
        """ returns a value with the specified delay """
        if not isinstance(delay, int):
            raise TypeError('delay must be int, not %s' % str(type(delay)))

        if delay <= 0:
            return var

        if isinstance(var, (int, float, bool)):
            return var

        if isinstance(var, vtypes._Constant):
            return var

        if prefix is None:
            prefix = '_'

        width = vtypes.get_width(var)
        signed = vtypes.get_signed(var)

        if not isinstance(var, vtypes._Variable):
            width = self.m.TmpLocalparam(width)
            w = self.m.TmpWire(width, signed=signed)
            w.assign(var)
            var = w

        if hasattr(var, 'name'):
            name_prefix = prefix + var.name
        else:
            name_prefix = _tmp_name(prefix)

        key = '_'.join([name_prefix, str(delay)])
        if key in self.prev_dict:
            return self.prev_dict[key]

        p = var
        for i in range(delay):
            cond = make_condition(cond)
            if cond is not None:
                tmp = self.m.TmpReg(width=width, initval=initval, signed=signed)
                self._add_statement([tmp(p)], cond=cond)
                p = tmp

            else:
                tmp_name = '_'.join([name_prefix, str(i + 1)])
                if tmp_name in self.prev_dict:
                    p = self.prev_dict[tmp_name]
                    continue
                tmp = self.m.Reg(
                    tmp_name, width, initval=initval, signed=signed)
                self.prev_dict[tmp_name] = tmp
                self._add_statement([tmp(p)])
                p = tmp

        return p

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

        if not isinstance(self.last_if_statement, vtypes.If):
            raise ValueError("Last if-statement is not If")

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

        if not isinstance(self.last_if_statement, vtypes.If):
            raise ValueError("Last if-statement is not If")

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

    def Clear(self):
        self._clear_next_kwargs()
        self._clear_last_if_statement()
        self._clear_last_cond()
        self._clear_elif_cond()
        return self

    # -------------------------------------------------------------------------
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
        return cond

    @property
    def last_condition(self):
        cond = self._make_cond(self.last_cond)
        return cond

    @property
    def then(self):
        return self.last_condition

    # -------------------------------------------------------------------------
    def update(self, src):

        if not isinstance(src, Seq):
            raise TypeError("src must be Seq object, not '%s'" %
                            str(type(src)))

        if self.done:
            raise ValueError("Destination Seq is already synthesized.")

        if src.done:
            return

        if id(self) == id(src):
            return

        if id(self.m) != id(src.m):
            raise ValueError("Two Seq objects have a different module.")
        if id(self.clk) != id(src.clk):
            raise ValueError("Two Seq objects have a different clock.")
        if id(self.rst) != id(src.rst):
            raise ValueError("Two Seq objects have a different reset.")

        if self.name == src.name:
            raise ValueError("Two Seq objects have a same name.")

        for delay, body in sorted(src.delayed_body.items(), key=lambda x: x[0]):
            self.delayed_body[delay].extend(body)

        self.prev_dict.update(src.prev_dict)
        self.body.extend(src.body)
        self.dst_var.update(src.dst_var)

        # Invalidated source Seq
        src.done = True

    # -------------------------------------------------------------------------
    def implement(self):
        if self.as_module:
            self.make_module()
            return

        self.make_always()

    # -------------------------------------------------------------------------
    def make_always(self, reset=(), body=()):
        if self.done:
            #raise ValueError('make_always() has been already called.')
            return

        self.done = True

        part_reset = list(reset) + list(self.make_reset())
        part_body = list(body) + list(self.make_code())

        if not part_reset and not part_body:
            pass
        elif not part_reset or self.rst is None:
            self.m.Always(vtypes.Posedge(self.clk))(
                part_body,
            )
        else:
            self.m.Always(vtypes.Posedge(self.clk))(
                vtypes.If(self.rst)(
                    part_reset,
                )(
                    part_body,
                ))

    # -------------------------------------------------------------------------
    def make_module(self, reset=(), body=()):
        if self.done:
            #raise ValueError('make_always() has been already called.')
            return

        self.done = True

        m = Module(self.name)

        clk = m.Input('CLK')

        if self.rst is not None:
            rst = m.Input('RST')
        else:
            rst = None

        body = list(body) + list(self.make_code())
        dsts = self.dst_var.values()
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
                    src_visitor.visit(dst.dims)

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
                    src_visitor.visit(src.dims)

        srcs = src_visitor.srcs.values()

        params = collections.OrderedDict()
        ports = collections.OrderedDict()
        src_rename_dict = collections.OrderedDict()

        # create parameter/localparam definitions
        for src in srcs:
            if isinstance(src, (vtypes.Parameter, vtypes.Localparam)):
                arg_name = src.name
                v = m.Parameter(arg_name, src.value, src.width, src.signed)
                src_rename_dict[src.name] = v
                params[arg_name] = src

        src_rename_visitor = SrcRenameVisitor(src_rename_dict)

        for src in srcs:
            if isinstance(src, (vtypes.Parameter, vtypes.Localparam)):
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
                out_line = self.m.TmpWire(pack_width, prefix='_%s_%s' % (self.name, src.name))

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

        reset = list(reset) + list(self.make_reset())

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
    def make_code(self):
        ret = []

        for delay, body in sorted(self.delayed_body.items(), key=lambda x: x[0],
                                  reverse=True):
            ret.extend(body)

        ret.extend(self.body)
        return ret

    # -------------------------------------------------------------------------
    def make_reset(self):
        ret = []
        for dst in self.dst_var.values():
            v = self.reset_visitor.visit(dst)
            if v is not None:
                ret.append(v)
        return ret

    # -------------------------------------------------------------------------
    def _add_statement(self, statement, keep=None, delay=None, cond=None,
                       lazy_cond=False, eager_val=False, no_delay_cond=False):

        cond = make_condition(cond)

        if keep is not None:
            for i in range(keep):
                new_delay = i if delay is None else delay + i
                self._add_statement(statement,
                                    keep=None, delay=new_delay, cond=cond,
                                    lazy_cond=lazy_cond, eager_val=eager_val,
                                    no_delay_cond=no_delay_cond)
            return self

        if delay is not None and delay > 0:
            if eager_val:
                statement = [self._add_delayed_subst(s, delay)
                             for s in statement]

            if not no_delay_cond:
                if cond is None:
                    cond = 1

                if not lazy_cond:
                    cond = self._add_delayed_cond(cond, delay)

                else:  # lazy condition
                    t = self._add_delayed_cond(1, delay)
                    if isinstance(cond, int) and cond == 1:
                        cond = t
                    else:
                        cond = vtypes.Ands(t, cond)

                statement = [vtypes.If(cond)(*statement)]

            self.delayed_body[delay].extend(statement)
            self._add_dst_var(statement)

            return self

        if cond is not None:
            statement = [vtypes.If(cond)(*statement)]
            self.last_if_statement = statement[0]

        self.body.extend(statement)
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
    def _add_delayed_cond(self, statement, delay):
        name_prefix = '_'.join(['', self.name, 'cond', str(self.tmp_count)])
        self.tmp_count += 1
        prev = statement
        for i in range(delay):
            tmp_name = '_'.join([name_prefix, str(i + 1)])
            tmp = self.m.Reg(tmp_name, initval=0)
            self._add_statement([tmp(prev)], delay=i, no_delay_cond=True)
            prev = tmp
        return prev

    # -------------------------------------------------------------------------
    def _add_delayed_subst(self, subst, delay):
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

        name_prefix = ('_'.join(['', left.name, str(self.tmp_count)])
                       if isinstance(left, vtypes._Variable) else
                       '_'.join(['', self.name, 'sbst', str(self.tmp_count)]))
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
    def __call__(self, *statement, **kwargs):
        return self.add(*statement, **kwargs)
