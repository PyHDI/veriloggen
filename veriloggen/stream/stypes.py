from __future__ import absolute_import
from __future__ import print_function

import numpy as np
import itertools
from collections import OrderedDict
from math import log, ceil

import veriloggen.core.vtypes as vtypes
import veriloggen.types.fixed as fx
import veriloggen.types.rom as rom
import veriloggen.types.ram as ram
from veriloggen.seq.seq import make_condition as _make_condition

from . import mul
from . import div
from . import madd


# Object ID counter for object sorting key
_object_counter = 0


def Constant(value, fixed=True, point=0):
    if isinstance(value, int):
        return Int(value)

    if isinstance(value, bool):
        v = 1 if value else 0
        return Int(v)

    if isinstance(value, float):
        if fixed:
            value = fx.to_fixed(value, point)
            return FixedPoint(value, point)
        return Float(value)

    if isinstance(value, str):
        return Str(value)

    raise TypeError("Unsupported type for Constant '%s'" % str(type(value)))


def Variable(data=None, width=32, point=0, signed=True):
    return _Variable(data, width, point, signed)


def Parameter(name, value, width=32, point=0, signed=True):
    """ parameter with an immediate value """
    if not isinstance(name, str):
        raise TypeError("'name' must be str, not '%s'" % str(tyep(name)))
    return _ParameterVariable(name, width, point, signed, value=value)


def ParameterVariable(data, width=32, point=0, signed=True):
    """ parameter with an existing object """
    if isinstance(data, float):
        return Constant(data, point=point)
    if isinstance(data, (int, bool)):
        data = vtypes.Int(data, width=width)
    return _ParameterVariable(data, width, point, signed)


class _Node(object):

    def __init__(self):
        global _object_counter
        self.object_id = _object_counter
        _object_counter += 1

        # for graph visualizer
        self.graph_label = None
        self.graph_shape = 'circle'
        self.graph_color = 'black'
        self.graph_style = ''
        self.graph_peripheries = 1

    def __hash__(self):
        object_id = self.object_id if hasattr(self, 'object_id') else None
        return hash((id(self), object_id))

    def __eq__(self, other):
        return (id(self), self.object_id) == (id(other), other.object_id)

    def name(self, prefix=None):
        clsname = self.__class__.__name__.lower()
        if prefix is None:
            prefix = 'tmp'
        return '_'.join(['', clsname, prefix, str(self.object_id)])


class _Numeric(_Node):
    latency = 0

    def __hash__(self):
        object_id = self.object_id if hasattr(self, 'object_id') else None
        return hash((id(self), object_id))

    def __init__(self):
        _Node.__init__(self)

        # set up by _set_managers()
        self.m = None
        self.strm = None
        self.seq = None

        self.output_data = None
        self.output_sig_data = None

        self.output_node = None

        self.sig_data = None

        self.start_stage = None
        self.end_stage = None
        self.sink = []

        # set up by _set_attributes()
        self.width = None
        self.point = None
        self.signed = False

        # stage numbers incremented
        self.delayed_value = OrderedDict()

        # stage numbers NOT incremented
        self.previous_value = OrderedDict()

    def output(self, data):
        if self.output_data is not None:
            raise ValueError('output_data is already assigned.')
        self.output_data = data

        if self.strm is not None:
            self.strm.add(self)

    def output_tmp(self):
        if self.m is None:
            raise ValueError("Module information is not set.")

        self.output(self.name('odata'))

    def prev(self, index):
        if index < 0:
            raise ValueError("index must be greater than 0")

        prev = self
        for i in range(index):
            r = self._get_previous_value(i + 1)
            if r is not None:
                prev = r
                continue
            r = _Prev(prev)
            r._set_parent_value(self)
            self._add_previous_value(i + 1, r)
            prev = r

        return prev

    def write(self, wdata, cond=None):
        raise TypeError("Unsupported method.")

    def read(self):
        if self.output_node is not None and id(self) != id(self.output_node):
            return self.output_node.read()

        if self.output_sig_data is None:
            # set default name
            if self.output_data is None:
                self.output_tmp()

            self._implement_output_sig(self.m, self.seq, aswire=True)

        data = self.output_sig_data

        return data

    def get_signed(self):
        return self.signed

    def get_point(self):
        return self.point

    def get_width(self):
        return self.width

    def eval(self):
        raise NotImplementedError('eval() is not implemented')

    def _set_attributes(self):
        raise NotImplementedError('_set_attributes() is not implemented')

    def _set_managers(self):
        raise NotImplementedError('_set_managers() is not implemented')

    def _set_module(self, m):
        self.m = m

    def _set_strm(self, strm):
        self.strm = strm

    def _set_seq(self, seq):
        self.seq = seq

    def _implement(self, m, seq, svalid=None, senable=None):
        raise NotImplementedError('_implement() is not implemented.')

    def _implement_input(self, m, seq, aswire=False):
        raise NotImplementedError('_implement_input() is not implemented.')

    def _implement_output(self, m, seq, aswire=False):
        if self.end_stage is None:
            self.end_stage = 0

        self._implement_output_sig(m, seq, aswire)
        data = self.output_sig_data

        m.Assign(data(self.sig_data))

    def _implement_output_sig(self, m, seq, aswire=False):
        if self.output_sig_data is not None:
            return

        if self.m is None:
            raise ValueError("Module information is not set.")

        width = self.get_width()
        signed = self.get_signed()

        type_i = m.Wire if aswire else m.Input
        type_o = m.Wire if aswire else m.Output

        if isinstance(self.output_data, (vtypes.Wire, vtypes.Output)):
            data = self.output_data
            self.output_sig_data = data
        else:
            data = type_o(self.output_data, width=width, signed=signed)
            self.output_sig_data = data

    def _has_output(self):
        if self.output_data is not None:
            return True
        return False

    def _disable_output(self):
        self.output_data = None

    def _disable_output_sig(self):
        self.output_sig_data = None

    def _set_output_node(self, node):
        self.output_node = node

    def _set_start_stage(self, stage):
        self.start_stage = stage

    def _get_start_stage(self):
        return self.start_stage

    def _has_start_stage(self):
        if self.start_stage is None:
            return False
        return True

    def _set_end_stage(self, stage):
        self.end_stage = stage

    def _get_end_stage(self):
        return self.end_stage

    def _has_end_stage(self):
        if self.end_stage is None:
            return False
        return True

    def _add_sink(self, value):
        self.sink.append(value)

    def _add_delayed_value(self, delay, value):
        if delay in self.delayed_value:
            raise ValueError('%d-delayed value is already allocated.' % delay)
        self.delayed_value[delay] = value

    def _get_delayed_value(self, delay):
        if delay not in self.delayed_value:
            return None
        return self.delayed_value[delay]

    def _add_previous_value(self, delay, value):
        if delay in self.delayed_value:
            raise ValueError('%d-delayed value is already allocated.' % delay)
        self.previous_value[delay] = value

    def _get_previous_value(self, delay):
        if delay not in self.previous_value:
            return None
        return self.previous_value[delay]

    def __lt__(self, r):
        return LessThan(self, r)

    def __le__(self, r):
        return LessEq(self, r)

    def __eq__(self, r):
        return Eq(self, r)

    def __ne__(self, r):
        return NotEq(self, r)

    def __ge__(self, r):
        return GreaterEq(self, r)

    def __gt__(self, r):
        return GreaterThan(self, r)

    def __add__(self, r):
        return Plus(self, r)

    def __sub__(self, r):
        return Minus(self, r)

    def __pow__(self, r):
        return Power(self, r)

    def __mul__(self, r):
        return Times(self, r)

    def __div__(self, r):
        return Divide(self, r)

    def __truediv__(self, r):
        return Divide(self, r)

    def __mod__(self, r):
        return Mod(self, r)

    def __and__(self, r):
        return And(self, r)

    def __or__(self, r):
        return Or(self, r)

    def __xor__(self, r):
        return Xor(self, r)

    def __lshift__(self, r):
        return Sll(self, r)

    def __rshift__(self, r):
        return Srl(self, r)

    def __neg__(self):
        return Uminus(self)

    def __pos__(self):
        return Uplus(self)

    def __abs__(self):
        return Abs(self)

    def __getitem__(self, r):
        if isinstance(r, slice):
            size = self.get_width()

            right = r.start
            if right is None:
                right = 0
            elif isinstance(right, int) and right < 0:
                right = size - abs(right)

            left = r.stop
            if left is None:
                left = size
            elif isinstance(left, int) and left < 0:
                left = size - abs(left)
            left -= 1

            if isinstance(left, int) and left < 0:
                raise ValueError("Illegal slice index: left = %d" % left)

            step = r.step
            if step is None:
                return Slice(self, left, right)
            else:
                if not (isinstance(left, int) and
                        isinstance(right, int) and
                        isinstance(step, int)):
                    raise ValueError(
                        "Slice with step is not supported in Verilog Slice.")

                if step == 0:
                    raise ValueError("Illegal slice step: step = %d" % step)

                values = [Pointer(self, i)
                          for i in range(right, left + 1, step)]
                values.reverse()
                return Cat(*values)

        if isinstance(r, int) and r < 0:
            r = self.get_width() - abs(r)

        return Pointer(self, r)

    def sra(self, r):  # shift right arithmetically
        return Sra(self, r)

    def repeat(self, times):
        return Repeat(self, times)

    def slice(self, msb, lsb):
        return Slice(self, msb, lsb)

    def __iter__(self):
        self.iter_size = len(self)
        self.iter_count = 0
        return self

    def __next__(self):
        if self.iter_count >= self.iter_size:
            raise StopIteration()

        ret = Pointer(self, self.iter_count)
        self.iter_count += 1
        return ret

    # for Python2
    def next(self):
        return self.__next__()

    def __len__(self):
        ret = self.get_width()
        if not isinstance(ret, int):
            raise ValueError("Non int length.")
        return ret

    @property
    def raw_data(self):
        if self.sig_data is None:
            raise ValueError(
                "Stream is not synthesized yet. Run Stream.implement().")
        return self.sig_data

    @property
    def data(self):
        if self.output_node is not None:
            return self.output_node.output_sig_data
        return self.raw_data


class _Operator(_Numeric):
    latency = 1

    def _implement(self, m, seq, svalid=None, senable=None):
        raise NotImplementedError('_implement() is not implemented.')


class _BinaryOperator(_Operator):
    latency = 1

    def __init__(self, left, right):
        _Operator.__init__(self)
        self.left = _to_constant(left)
        self.right = _to_constant(right)
        self.left._add_sink(self)
        self.right._add_sink(self)
        self.op = getattr(vtypes, self.__class__.__name__, None)
        self._set_attributes()
        self._set_managers()

    def _set_attributes(self):
        left_fp = self.left.get_point()
        right_fp = self.right.get_point()
        left = self.left.get_width() - left_fp
        right = self.right.get_width() - right_fp
        self.width = max(left, right) + max(left_fp, right_fp)
        self.point = max(left_fp, right_fp)
        self.signed = self.left.get_signed() and self.right.get_signed()

    def _set_managers(self):
        self._set_strm(_get_strm(self.left, self.right))
        self._set_module(getattr(self.strm, 'module', None))
        self._set_seq(getattr(self.strm, 'seq', None))

    def _implement(self, m, seq, svalid=None, senable=None):
        width = self.get_width()
        signed = self.get_signed()

        lpoint = self.left.get_point()
        rpoint = self.right.get_point()
        ldata, rdata = fx.adjust(self.left.sig_data, self.right.sig_data,
                                 lpoint, rpoint, signed)

        if self.latency == 0:
            data = m.Wire(self.name('data'), width, signed=signed)
            data.assign(self.op(ldata, rdata))
            self.sig_data = data

        elif self.latency == 1:
            data = m.Reg(self.name('data'), width, initval=0, signed=signed)
            self.sig_data = data
            seq(data(self.op(ldata, rdata)), cond=senable)

        else:
            prev_data = None

            for i in range(self.latency):
                data = m.Reg(self.name('data_d%d' % i),
                             width, initval=0, signed=signed)
                if i == 0:
                    seq(data(self.op(ldata, rdata)), cond=senable)
                else:
                    seq(data(prev_data), cond=senable)
                prev_data = data

            self.sig_data = data


class _UnaryOperator(_Operator):
    latency = 1

    def __init__(self, right):
        _Operator.__init__(self)
        self.right = _to_constant(right)
        self.right._add_sink(self)
        self.op = getattr(vtypes, self.__class__.__name__, None)
        self._set_attributes()
        self._set_managers()

    def _set_attributes(self):
        right = self.right.get_width()
        right_fp = self.right.get_point()
        self.width = right
        self.point = right_fp
        self.signed = self.right.get_signed()

    def _set_managers(self):
        self._set_strm(_get_strm(self.right))
        self._set_module(getattr(self.strm, 'module', None))
        self._set_seq(getattr(self.strm, 'seq', None))

    def _implement(self, m, seq, svalid=None, senable=None):
        width = self.get_width()
        signed = self.get_signed()
        rdata = self.right.sig_data

        if self.latency == 0:
            data = m.Wire(self.name('data'), width, signed=signed)
            data.assign(self.op(rdata))
            self.sig_data = data

        elif self.latency == 1:
            data = m.Reg(self.name('data'), width, initval=0, signed=signed)
            self.sig_data = data
            seq(data(self.op(rdata)), cond=senable)

        else:
            prev_data = None

            for i in range(self.latency):
                data = m.Reg(self.name('data_d%d' % i),
                             width, initval=0, signed=signed)
                if i == 0:
                    seq(data(self.op(rdata)), cond=senable)
                else:
                    seq(data(prev_data), cond=senable)
                prev_data = data

            self.sig_data = data


class Power(_BinaryOperator):
    latency = 0

    def eval(self):
        return self.left.eval() ** self.right.eval()

    def _implement(self, m, seq, svalid=None, senable=None):
        raise NotImplementedError('_implement() is not implemented.')


class Times(_BinaryOperator):
    latency = 6 + 1

    def eval(self):
        return self.left.eval() * self.right.eval()

    def _set_attributes(self):
        left_fp = self.left.get_point()
        right_fp = self.right.get_point()
        left = self.left.get_width()
        right = self.right.get_width()
        self.width = max(left, right)
        self.point = min(max(left_fp, right_fp), left_fp + right_fp)
        self.signed = self.left.get_signed() and self.right.get_signed()

    def _implement(self, m, seq, svalid=None, senable=None):
        if self.latency <= 3:
            raise ValueError("Latency of '*' operator must be greater than 3")

        width = self.get_width()
        signed = self.get_signed()

        lpoint = self.left.get_point()
        rpoint = self.right.get_point()
        lwidth = self.left.get_width()
        rwidth = self.right.get_width()
        lsigned = self.left.get_signed()
        rsigned = self.right.get_signed()
        ldata = self.left.sig_data
        rdata = self.right.sig_data

        odata = m.Wire(self.name('mul_odata'), lwidth + rwidth, signed=signed)
        odata_reg = m.Reg(self.name('mul_odata_reg'),
                          lwidth + rwidth, signed=signed, initval=0)

        data = m.Wire(self.name('data'), width, signed=signed)
        self.sig_data = data

        shift_size = lpoint + rpoint - self.point
        if shift_size > 0:
            seq(odata_reg(fx.shift_right(odata, shift_size, signed=signed)), cond=senable)
        else:
            seq(odata_reg(odata), cond=senable)

        m.Assign(data(odata_reg))

        depth = self.latency - 1

        inst = mul.get_mul(lwidth, rwidth, lsigned, rsigned, depth)
        clk = m._clock

        update = m.Wire(self.name('mul_update'))

        if senable is not None:
            m.Assign(update(senable))
        else:
            m.Assign(update(vtypes.Int(1, 1)))

        ports = [('CLK', clk), ('update', update),
                 ('a', ldata), ('b', rdata), ('c', odata)]

        m.Instance(inst, self.name('mul'), ports=ports)


class Divide(_BinaryOperator):
    latency = 32 + 5
    variable_latency = 'get_latency'

    def get_latency(self):
        return self.get_width() + 5

    def eval(self):
        left = self.left.eval()
        right = self.right.eval()
        if isinstance(left, int) and isinstance(right, int):
            return int(left / right)
        return Divide(left, right)

    def _implement(self, m, seq, svalid=None, senable=None):
        if self.latency <= 5:
            raise ValueError("Latency of div operator must be greater than 5")

        width = self.get_width()
        signed = self.get_signed()

        lpoint = self.left.get_point()
        rpoint = self.right.get_point()
        lsigned = self.left.get_signed()
        rsigned = self.right.get_signed()

        lval, rval = fx.adjust(self.left.sig_data, self.right.sig_data,
                               lpoint, rpoint, signed)

        ldata = m.Reg(self.name('div_ldata'), width, signed=lsigned, initval=0)
        rdata = m.Reg(self.name('div_rdata'), width, signed=rsigned, initval=0)

        seq(ldata(lval), cond=senable)
        seq(rdata(rval), cond=senable)

        sign = vtypes.Not(
            vtypes.OrList(vtypes.AndList(ldata[width - 1] == 0,
                                         rdata[width - 1] == 0),  # + , +
                          vtypes.AndList(ldata[width - 1] == 1,
                                         rdata[width - 1] == 1)))  # - , -

        abs_ldata = m.Reg(self.name('div_abs_ldata'), width, initval=0)
        abs_rdata = m.Reg(self.name('div_abs_rdata'), width, initval=0)

        if not lsigned:
            seq(abs_ldata(ldata), cond=senable)
        else:
            seq(abs_ldata(vtypes.Mux(ldata[width - 1] == 0, ldata, vtypes.Unot(ldata) + 1)),
                cond=senable)

        if not rsigned:
            seq(abs_rdata(rdata), cond=senable)
        else:
            seq(abs_rdata(vtypes.Mux(rdata[width - 1] == 0, rdata, vtypes.Unot(rdata) + 1)),
                cond=senable)

        osign = m.Wire(self.name('div_osign'))
        abs_odata = m.Wire(self.name('div_abs_odata'), width, signed=signed)
        odata = m.Reg(self.name('div_odata'), width, signed=signed, initval=0)

        if not signed:
            seq(odata(abs_odata), cond=senable)
        else:
            seq(odata(vtypes.Mux(osign == 0, abs_odata, vtypes.Unot(abs_odata) + 1)),
                cond=senable)

        data = m.Wire(self.name('data'), width, signed=signed)
        self.sig_data = data

        m.Assign(data(odata))

        s = sign
        for i in range(self.latency - 2):
            ns = m.Reg(self.name('div_sign_tmp_%d' % i), initval=0)
            seq(ns(s), cond=senable)
            s = ns
        m.Assign(osign(s))

        inst = div.get_div()
        clk = m._clock
        rst = m._reset

        update = m.Wire(self.name('div_update'))

        if senable is not None:
            m.Assign(update(senable))
        else:
            m.Assign(update(vtypes.Int(1, 1)))

        params = [('W_D', width)]
        ports = [('CLK', clk), ('RST', rst), ('update', update), ('enable', vtypes.Int(1, 1)),
                 ('in_a', abs_ldata), ('in_b', abs_rdata), ('rslt', abs_odata)]

        m.Instance(inst, self.name('div'), params, ports)


class Mod(_BinaryOperator):
    latency = 32 + 5
    variable_latency = 'get_latency'

    def get_latency(self):
        return self.get_width() + 5

    def eval(self):
        return self.left.eval() % self.right.eval()

    def _implement(self, m, seq, svalid=None, senable=None):
        if self.latency <= 5:
            raise ValueError("Latency of div operator must be greater than 5")

        width = self.get_width()
        signed = self.get_signed()

        lpoint = self.left.get_point()
        rpoint = self.right.get_point()
        lsigned = self.left.get_signed()
        rsigned = self.right.get_signed()

        lval, rval = fx.adjust(self.left.sig_data, self.right.sig_data,
                               lpoint, rpoint, signed)

        ldata = m.Reg(self.name('mod_ldata'), width, signed=lsigned, initval=0)
        rdata = m.Reg(self.name('mod_rdata'), width, signed=rsigned, initval=0)

        seq(ldata(lval), cond=senable)
        seq(rdata(rval), cond=senable)

        sign = vtypes.Not(
            vtypes.OrList(vtypes.AndList(ldata[width - 1] == 0,
                                         rdata[width - 1] == 0),  # + , +
                          vtypes.AndList(ldata[width - 1] == 1,
                                         rdata[width - 1] == 1)))  # - , -

        abs_ldata = m.Reg(self.name('div_abs_ldata'), width, initval=0)
        abs_rdata = m.Reg(self.name('div_abs_rdata'), width, initval=0)

        if not lsigned:
            seq(abs_ldata(ldata), cond=senable)
        else:
            seq(abs_ldata(vtypes.Mux(ldata[width - 1] == 0, ldata, vtypes.Unot(ldata) + 1)),
                cond=senable)

        if not rsigned:
            seq(abs_rdata(rdata), cond=senable)
        else:
            seq(abs_rdata(vtypes.Mux(rdata[width - 1] == 0, rdata, vtypes.Unot(rdata) + 1)),
                cond=senable)

        osign = m.Wire(self.name('mod_osign'))
        abs_odata = m.Wire(self.name('mod_abs_odata'), width, signed=signed)
        odata = m.Reg(self.name('mod_odata'), width, signed=signed, initval=0)

        if not signed:
            seq(odata(abs_odata), cond=senable)
        else:
            seq(odata(vtypes.Mux(osign == 0, abs_odata, vtypes.Unot(abs_odata) + 1)),
                cond=senable)

        data = m.Wire(self.name('data'), width, signed=signed)
        self.sig_data = data

        m.Assign(data(odata))

        s = sign
        for i in range(self.latency - 2):
            ns = m.Reg(self.name('div_sign_tmp_%d' % i), initval=0)
            seq(ns(s), cond=senable)
            s = ns
        m.Assign(osign(s))

        inst = div.get_div()
        clk = m._clock
        rst = m._reset

        update = m.Wire(self.name('mod_update'))

        if senable is not None:
            m.Assign(update(senable))
        else:
            m.Assign(update(vtypes.Int(1, 1)))

        params = [('W_D', width)]
        ports = [('CLK', clk), ('RST', rst), ('update', update), ('enable', vtypes.Int(1, 1)),
                 ('in_a', abs_ldata), ('in_b', abs_rdata), ('mod', abs_odata)]

        m.Instance(inst, self.name('div'), params, ports)


class Plus(_BinaryOperator):

    def eval(self):
        return self.left.eval() + self.right.eval()


class Minus(_BinaryOperator):

    def eval(self):
        return self.left.eval() - self.right.eval()


# general name alias
def Add(left, right):
    return Plus(left, right)


def Sub(left, right):
    return Minus(left, right)


def Mul(left, right):
    return Times(left, right)


def Div(left, right):
    return Divide(left, right)


def Neg(right):
    return Uminus(right)


class LessThan(_BinaryOperator):

    def _set_attributes(self):
        self.width = 1
        self.point = 0
        self.signed = False

    def eval(self):
        return self.left.eval() < self.right.eval()


class GreaterThan(_BinaryOperator):

    def _set_attributes(self):
        self.width = 1
        self.point = 0
        self.signed = False

    def eval(self):
        return self.left.eval() > self.right.eval()


class LessEq(_BinaryOperator):

    def _set_attributes(self):
        self.width = 1
        self.point = 0
        self.signed = False

    def eval(self):
        return self.left.eval() <= self.right.eval()


class GreaterEq(_BinaryOperator):

    def _set_attributes(self):
        self.width = 1
        self.point = 0
        self.signed = False

    def eval(self):
        return self.left.eval() >= self.right.eval()


class Eq(_BinaryOperator):

    def _set_attributes(self):
        self.width = 1
        self.point = 0
        self.signed = False

    def eval(self):
        return self.left.eval() == self.right.eval()


class NotEq(_BinaryOperator):

    def _set_attributes(self):
        self.width = 1
        self.point = 0
        self.signed = False

    def eval(self):
        return self.left.eval() != self.right.eval()


class _BinaryShiftOperator(_BinaryOperator):

    def __init__(self, left, right):
        _BinaryOperator.__init__(self, left, right)
        s = self.right.eval()
        if isinstance(s, int):
            self.latency = 0

    def _implement(self, m, seq, svalid=None, senable=None):
        if self.right.get_point() != 0:
            raise TypeError("shift amount must be int")

        width = self.get_width()
        signed = self.get_signed()

        lpoint = self.left.get_point()
        rpoint = self.right.get_point()
        ldata, rdata = self.left.sig_data, self.right.sig_data

        if self.latency == 0:
            data = m.Wire(self.name('data'), width, signed=signed)
            data.assign(self.op(ldata, rdata))
            self.sig_data = data

        elif self.latency == 1:
            data = m.Reg(self.name('data'), width, initval=0, signed=signed)
            self.sig_data = data
            seq(data(self.op(ldata, rdata)), cond=senable)

        else:
            prev_data = None

            for i in range(self.latency):
                data = m.Reg(self.name('data_d%d' % i),
                             width, initval=0, signed=signed)
                if i == 0:
                    seq(data(self.op(ldata, rdata)), cond=senable)
                else:
                    seq(data(prev_data), cond=senable)
                prev_data = data

            self.sig_data = data


class Sll(_BinaryShiftOperator):
    max_width = 1024

    def _set_attributes(self):
        v = self.right.eval()
        if isinstance(v, int):
            width = self.left.get_width() + v
        else:
            v = 2 ** self.right.get_width()
            width = self.left.get_width() + v

        if width > self.max_width:
            raise ValueError("bitwidth is too large '%d'" % width)

        self.width = width
        self.point = self.left.get_point()
        self.signed = self.left.get_signed()

    def eval(self):
        return self.left.eval() << self.right.eval()


class Srl(_BinaryShiftOperator):

    def _set_attributes(self):
        self.width = self.left.get_width()
        self.point = self.left.get_point()
        self.signed = False

    def eval(self):
        return self.left.eval() >> self.right.eval()


class Sra(_BinaryShiftOperator):

    def _set_attributes(self):
        self.width = self.left.get_width()
        self.point = self.left.get_point()
        self.signed = self.left.get_signed()

    def eval(self):
        left = self.left.eval()
        right = self.right.eval()
        if isinstance(left, int) and isinstance(right, int):
            sign = left >= 0
            left = abs(left)
            ret = left >> right
            if not sign:
                return -1 * ret
            return ret
        return Sra(left, right)


class _BinaryLogicalOperator(_BinaryOperator):

    def _set_attributes(self):
        left = self.left.get_width()
        right = self.right.get_width()
        self.width = max(left, right)
        self.point = 0
        self.signed = False

    def _implement(self, m, seq, svalid=None, senable=None):
        width = self.get_width()
        signed = False

        lpoint = self.left.get_point()
        rpoint = self.right.get_point()
        ldata, rdata = self.left.sig_data, self.right.sig_data

        if self.latency == 0:
            data = m.Wire(self.name('data'), width, signed=signed)
            data.assign(self.op(ldata, rdata))
            self.sig_data = data

        elif self.latency == 1:
            data = m.Reg(self.name('data'), width, initval=0, signed=signed)
            self.sig_data = data
            seq(data(self.op(ldata, rdata)), cond=senable)

        else:
            prev_data = None

            for i in range(self.latency):
                data = m.Reg(self.name('data_d%d' % i),
                             width, initval=0, signed=signed)
                if i == 0:
                    seq(data(self.op(ldata, rdata)), cond=senable)
                else:
                    seq(data(prev_data), cond=senable)
                prev_data = data

            self.sig_data = data


class And(_BinaryLogicalOperator):

    def eval(self):
        return self.left.eval() & self.right.eval()


class Xor(_BinaryLogicalOperator):

    def eval(self):
        return self.left.eval() ^ self.right.eval()


class Xnor(_BinaryLogicalOperator):

    def eval(self):
        left = self.left.eval()
        right = self.right.eval()
        ret = left ^ right
        if isinstance(ret, int):
            return ret == 0
        return Xnor(left, right)


class Or(_BinaryLogicalOperator):

    def eval(self):
        return self.left.eval() | self.right.eval()


class Land(_BinaryLogicalOperator):

    def _set_attributes(self):
        self.width = 1
        self.point = 0
        self.signed = False

    def eval(self):
        left = self.left.eval()
        right = self.right.eval()
        if isinstance(left, (int, bool)) and isinstance(right, (int, bool)):
            return left and right
        return Land(left, right)


class Lor(_BinaryLogicalOperator):

    def _set_attributes(self):
        self.width = 1
        self.point = 0
        self.signed = False

    def eval(self):
        left = self.left.eval()
        right = self.right.eval()
        if isinstance(left, (int, bool)) and isinstance(right, (int, bool)):
            return left or right
        return Land(left, right)


class Uplus(_UnaryOperator):

    def eval(self):
        return self.right.eval()


class Uminus(_UnaryOperator):

    def eval(self):
        return - self.right.eval()


class _UnaryLogicalOperator(_UnaryOperator):

    def _set_attributes(self):
        right = self.right.get_width()
        self.width = right
        self.point = 0
        self.signed = False


class Ulnot(_UnaryLogicalOperator):

    def _set_attributes(self):
        self.width = 1
        self.point = 0

    def eval(self):
        right = self.right.eval()
        if isinstance(right, (int, bool)):
            return not right
        return Ulnot(right)


class Unot(_UnaryLogicalOperator):

    def eval(self):
        right = self.right.eval()
        try:
            v = ~right
        except:
            v = Ulnot(right)
        return v


class Uand(_UnaryLogicalOperator):

    def _set_attributes(self):
        self.width = 1
        self.point = 0

    def eval(self):
        right = self.right.eval()
        if isinstance(right, bool):
            return right
        if isinstance(right, int):
            width = self.right.get_width()
            for i in range(width):
                if right & 0x1 == 0:
                    return False
                right = right >> 1
            return True
        return Uand(right)


class Unand(_UnaryLogicalOperator):

    def _set_attributes(self):
        self.width = 1
        self.point = 0

    def eval(self):
        right = self.right.eval()
        if isinstance(right, bool):
            return not right
        if isinstance(right, int):
            width = self.right.get_width()
            for i in range(width):
                if right & 0x1 == 0:
                    return True
                right = right >> 1
            return False
        return Unand(right)


class Uor(_UnaryLogicalOperator):

    def _set_attributes(self):
        self.width = 1
        self.point = 0

    def eval(self):
        right = self.right.eval()
        if isinstance(right, bool):
            return right
        if isinstance(right, int):
            width = self.right.get_width()
            for i in range(width):
                if right & 0x1 == 1:
                    return True
                right = right >> 1
            return False
        return Uor(right)


class Unor(_UnaryLogicalOperator):

    def _set_attributes(self):
        self.width = 1
        self.point = 0

    def eval(self):
        right = self.right.eval()
        if isinstance(right, bool):
            return not right
        if isinstance(right, int):
            width = self.right.get_width()
            for i in range(width):
                if right & 0x1 == 1:
                    return False
                right = right >> 1
            return True
        return Unor(right)


class Uxor(_UnaryLogicalOperator):

    def _set_attributes(self):
        self.width = 1
        self.point = 0

    def eval(self):
        right = self.right.eval()
        if isinstance(right, bool):
            return right
        if isinstance(right, int):
            width = self.right.get_width()
            ret = 1
            for i in range(width):
                ret = ret ^ (right & 0x1)
                right = right >> 1
            return ret == 1
        return Uxor(right)


class Uxnor(_UnaryLogicalOperator):

    def _set_attributes(self):
        self.width = 1
        self.point = 0

    def eval(self):
        right = self.right.eval()
        if isinstance(right, bool):
            return not right
        if isinstance(right, int):
            width = self.right.get_width()
            ret = 1
            for i in range(width):
                ret = ret ^ (right & 0x1)
                right = right >> 1
            return ret == 0
        return Uxnor(right)


# alias
def Not(*args):
    return Ulnot(*args)


def AndList(*args):
    if len(args) == 0:
        raise ValueError("LandList requires at least one argument.")
    if len(args) == 1:
        return args[0]
    left = args[0]
    for right in args[1:]:
        left = Land(left, right)
    return left


def OrList(*args):
    if len(args) == 0:
        raise ValueError("LorList requires at least one argument.")
    if len(args) == 1:
        return args[0]
    left = args[0]
    for right in args[1:]:
        left = Lor(left, right)
    return left


Ands = AndList
Ors = OrList


class Cast(_UnaryOperator):
    latency = 0

    def __init__(self, data, width=None, point=None, signed=None):
        _UnaryOperator.__init__(self, data)
        if width is not None:
            self.width = width
        if point is not None:
            self.point = point
        if signed is not None:
            self.signed = signed

    def _implement(self, m, seq, svalid=None, senable=None):
        if self.latency != 0:
            raise ValueError("Latency mismatch '%d' vs '%s'" %
                             (self.latency, 0))

        width = self.get_width()
        signed = self.get_signed()

        rdata = self.right.sig_data
        rwidth = self.right.get_width()
        rpoint = self.right.get_point()
        rsigned = self.right.get_signed()

        rdata_src = m.Wire(self.name('src'), rwidth, signed=rsigned)
        rdata_src.assign(rdata)

        if rpoint > self.point:
            rdata_src = fx.shift_right(rdata_src, rpoint - self.point, rsigned)
        elif rpoint < self.point:
            rdata_src = fx.shift_left(rdata_src, self.point - rpoint, rsigned)

        data = m.Wire(self.name('data'), width, signed=signed)
        self.sig_data = data

        m.Assign(data(rdata_src))

    def eval(self):
        return self


class ReinterpretCast(Cast):

    def _implement(self, m, seq, svalid=None, senable=None):
        if self.latency != 0:
            raise ValueError("Latency mismatch '%d' vs '%s'" %
                             (self.latency, 0))

        width = self.get_width()
        signed = self.get_signed()

        rdata = self.right.sig_data
        rwidth = self.right.get_width()
        rsigned = self.right.get_signed()

        rdata_src = m.Wire(self.name('src'), rwidth, signed=rsigned)
        rdata_src.assign(rdata)

        data = m.Wire(self.name('data'), width, signed=signed)
        self.sig_data = data

        m.Assign(data(rdata_src))

    def eval(self):
        return self


class _SpecialOperator(_Operator):
    latency = 1

    def __init__(self, *args):
        _Operator.__init__(self)
        self.args = [_to_constant(arg) for arg in args]
        for var in self.args:
            var._add_sink(self)
        self.op = None
        self._set_attributes()
        self._set_managers()

        self.graph_shape = 'ellipse'

    def _set_attributes(self):
        if len(self.args) > 1:
            wargs = [arg.get_width() for arg in self.args]
            self.width = max(*wargs)
            pargs = [arg.get_point() for arg in self.args]
            self.point = max(*pargs)
        elif self.args:
            self.width = self.args[0].get_width()
            self.point = self.args[0].get_point()
        else:
            self.width = 1
            self.point = 0

        self.signed = False
        for arg in self.args:
            if arg.get_signed():
                self.signed = True
                break

    def _set_managers(self):
        self._set_strm(_get_strm(*self.args))
        self._set_module(getattr(self.strm, 'module', None))
        self._set_seq(getattr(self.strm, 'seq', None))

    def _implement(self, m, seq, svalid=None, senable=None):
        width = self.get_width()
        signed = self.get_signed()

        arg_data = [arg.sig_data for arg in self.args]

        if self.latency == 0:
            data = m.Wire(self.name('data'), width, signed=signed)
            data.assign(self.op(*arg_data))
            self.sig_data = data

        elif self.latency == 1:
            data = m.Reg(self.name('data'), width, initval=0, signed=signed)
            self.sig_data = data
            seq(data(self.op(*arg_data)), cond=senable)

        else:
            prev_data = None

            for i in range(self.latency):
                data = m.Reg(self.name('data_d%d' % i),
                             width, initval=0, signed=signed)
                if i == 0:
                    seq(data(self.op(*arg_data)), cond=senable)
                else:
                    seq(data(prev_data), cond=senable)
                prev_data = data

            self.sig_data = data


class Pointer(_SpecialOperator):

    def __init__(self, var, pos):
        _SpecialOperator.__init__(self, var, pos)
        self.op = vtypes.Pointer

        p = self.args[1].eval()
        if isinstance(p, int):
            self.latency = 0

    def _set_attributes(self):
        self.width = 1
        self.point = 0
        self.signed = False

    @property
    def var(self):
        return self.args[0]

    @var.setter
    def var(self, var):
        self.args[0] = var

    @property
    def pos(self):
        return self.args[1]

    @pos.setter
    def pos(self, pos):
        self.args[1] = pos

    def eval(self):
        var = self.var.eval()
        pos = self.pos.eval()
        if isinstance(var, int) and isinstance(pos, int):
            return (var >> pos) & 0x1
        return Pointer(var, pos)


class Slice(_SpecialOperator):
    latency = 0

    def __init__(self, var, msb, lsb):
        msb = msb.eval() if isinstance(msb, _Constant) else msb
        lsb = lsb.eval() if isinstance(lsb, _Constant) else lsb
        if not isinstance(msb, int) or not isinstance(lsb, int):
            raise TypeError('msb and lsb must be int')
        msb = Int(msb, signed=False)
        lsb = Int(lsb, signed=False)
        _SpecialOperator.__init__(self, var, msb, lsb)
        self.op = vtypes.Slice

    def _set_attributes(self):
        self.width = self.msb.eval() - self.lsb.eval() + 1
        self.point = 0
        self.signed = False

    @property
    def var(self):
        return self.args[0]

    @var.setter
    def var(self, var):
        self.args[0] = var

    @property
    def msb(self):
        return self.args[1]

    @msb.setter
    def msb(self, msb):
        self.args[1] = msb

    @property
    def lsb(self):
        return self.args[2]

    @lsb.setter
    def lsb(self, lsb):
        self.args[2] = lsb

    def eval(self):
        var = self.var.eval()
        msb = self.msb.eval()
        lsb = self.lsb.eval()
        if isinstance(var, int) and isinstance(msb, int) and isinstance(lsb, int):
            mask = 0
            for i in range(msb - lsb + 1):
                mask = (mask << 1) | 0x1
            return (var >> lsb) & mask
        return Slice(var, msb, lsb)


def Split(data, width=None, point=None, signed=None, num_chunks=None, reverse=False):
    """
    Split the given data into multiple chunks

    Parameters
    ----------
    data : _Numeric
        Input data

    width : int
        Data width of separated chunks (default: same as input data)

    point : int
        Fixed-point position of separated chunks (default: same as input data)

    signed : bool
        Sign (default: same as input data)

    num_chunks: int
        The number of separated chunks (default: (input data width) / width)

    reverse: bool
        reverse flag. If true, a reversed list is returned

    Returns
    -------
    chunks : list
        A list of separated chunks

        For the consistency with Cat operator, the order of chunks is higher-bit first.
        If data is a 32-bit value, and width is 8, returned list of chunks will be
            chunks = [data[31:24], data[23:16], data[15:8], data[7:0]]
        If reverse == True, it returns the reversed list of chunks
    """

    data = _to_constant(data)

    if width is None and num_chunks is None:
        raise ValueError('width or num_chunks must be specified.')

    if width is not None and num_chunks is not None:
        raise ValueError('Either of width or num_chunks must be specified.')

    if width is None:
        width = int(ceil(data.get_width() / num_chunks))
    elif num_chunks is None:
        num_chunks = int(ceil(data.get_width() / width))

    if point is None:
        point = data.get_point()

    if signed is None:
        signed = data.get_signed()

    total_width = width * num_chunks
    ret = []
    for i in range(0, total_width, width):
        if i + width > data.get_width():
            if signed:
                sign = data[-1]
                sign.latency = 0
                pad = Repeat(sign, total_width - data.get_width())
                pad.latency = 0
            else:
                pad = Int(0, signed=False)
                pad.width = total_width - data.get_width()

            slc = Slice(data, data.get_width() - 1, i)
            slc.latency = 0
            v = Cat(pad, slc)
            v.latency = 0
        else:
            v = Slice(data, i + width - 1, i)
            v.latency = 0

        ret.append(ReinterpretCast(v, width, point, signed))

    if not reverse:
        ret.reverse()

    return ret


class Cat(_SpecialOperator):
    latency = 0

    def __init__(self, *vars):
        _SpecialOperator.__init__(self, *vars)
        self.op = vtypes.Cat

    def _set_attributes(self):
        ret = 0
        for v in self.vars:
            ret += v.get_width()
        self.width = ret
        self.point = 0
        self.signed = False

    @property
    def vars(self):
        return self.args

    @vars.setter
    def vars(self, vars):
        self.args = list(vars)

    def eval(self):
        vars = [var.eval() for var in self.vars]
        for var in vars:
            if not isinstance(var, int):
                return Cat(*vars)
        ret = 0
        for var in vars:
            ret = (ret << var.get_width()) | var
        return ret


class Repeat(_SpecialOperator):

    def __init__(self, var, times):
        times = times.eval() if isinstance(times, _Constant) else times
        if not isinstance(times, int):
            raise TypeError('times must be int')
        _SpecialOperator.__init__(self, var, times)
        self.op = vtypes.Repeat

    def _set_attributes(self):
        self.width = self.var.get_width() * self.times.eval()
        self.point = 0
        self.signed = False

    @property
    def var(self):
        return self.args[0]

    @var.setter
    def var(self, var):
        self.args[0] = var

    @property
    def times(self):
        return self.args[1]

    @times.setter
    def times(self, times):
        self.args[1] = times

    def eval(self):
        var = self.var.eval()
        times = self.times.eval()
        ret = 0
        for i in times:
            ret = (ret << var.get_width()) | var
        return ret


class Cond(_SpecialOperator):

    def __init__(self, condition, true_value, false_value):
        _SpecialOperator.__init__(self, condition, true_value, false_value)
        self.op = vtypes.Cond

    def _set_attributes(self):
        true_value_fp = self.true_value.get_point()
        false_value_fp = self.false_value.get_point()
        true_value = self.true_value.get_width() - true_value_fp
        false_value = self.false_value.get_width() - false_value_fp
        self.width = max(true_value, false_value) + \
            max(true_value_fp, false_value_fp)
        self.point = max(true_value_fp, false_value_fp)
        self.signed = self.true_value.get_signed() or self.false_value.get_signed()

    @property
    def condition(self):
        return self.args[0]

    @condition.setter
    def condition(self, condition):
        self.args[0] = condition

    @property
    def true_value(self):
        return self.args[1]

    @true_value.setter
    def true_value(self, true_value):
        self.args[1] = true_value

    @property
    def false_value(self):
        return self.args[2]

    @false_value.setter
    def false_value(self, false_value):
        self.args[2] = false_value

    def eval(self):
        condition = self.condition.eval()
        true_value = self.true_value.eval()
        false_value = self.false_value.eval()
        if isinstance(condition, (int, bool)):
            if condition:
                return true_value
            else:
                return false_value
        return Cond(condition, true_value, false_value)


def Mux(condition, true_value, false_value):
    # return the result immediately if the condition can be resolved now
    if isinstance(condition, (bool, int, float, str, list, tuple)):
        return true_value if condition else false_value
    return Cond(condition, true_value, false_value)


class _Sync(_SpecialOperator):
    latency = 0

    def __init__(self, vars, index):
        self.index = index
        _SpecialOperator.__init__(self, *vars)
        self.op = lambda *args: args[index]
        self.graph_label = 'Sync %d' % index

    def _set_attributes(self):
        var = self.args[self.index]
        self.width = var.get_width()
        self.point = var.get_point()
        self.signed = var.get_signed()


def Sync(*vars):
    """ Synchronize 'start_stage' of multiple variables """

    ret_vars = []
    for i, var in enumerate(vars):
        ret_vars.append(_Sync(vars, i))

    return tuple(ret_vars)


class ForwardDest(_SpecialOperator):
    latency = 0

    def __init__(self, value, index):
        _SpecialOperator.__init__(self, value, index)
        self.graph_label = 'ForwardDest'
        self.graph_shape = 'box'
        self.forward_value = None
        self.forward_index = None

    def _set_attributes(self):
        value = self.args[0]
        self.width = value.get_width()
        self.point = value.get_point()
        self.signed = value.get_signed()

    def _implement(self, m, seq, svalid=None, senable=None):
        if self.latency != 0:
            raise ValueError("Latency mismatch '%d' vs '%s'" %
                             (self.latency, 0))

        width = self.get_width()
        signed = self.get_signed()

        value = self.args[0].sig_data
        index = self.args[1].sig_data

        index_width = self.args[1].get_width()
        index_signed = self.args[1].get_signed()

        self.forward_value = m.Wire(self.name('forward_value'), width, signed=signed)
        self.forward_index = m.Wire(self.name('forward_index'), index_width, signed=index_signed)
        self.forward_valid = m.Wire(self.name('forward_valid'))

        data = m.Wire(self.name('data'), width, signed=signed)
        data.assign(vtypes.Mux(_and_vars(self.forward_valid, index == self.forward_index),
                               self.forward_value, value))
        self.sig_data = data


class ForwardSource(_SpecialOperator):
    latency = 0

    def __init__(self, value, index, dest):
        _SpecialOperator.__init__(self, value, index)
        self.dest = dest

        self.output_tmp()

        self.graph_label = 'ForwardSource'
        self.graph_shape = 'box'

    def _set_attributes(self):
        value = self.args[0]
        self.width = value.get_width()
        self.point = value.get_point()
        self.signed = value.get_signed()

    def _implement(self, m, seq, svalid=None, senable=None):
        if self.latency != 0:
            raise ValueError("Latency mismatch '%d' vs '%s'" %
                             (self.latency, 0))

        if self.args[0].end_stage != self.dest.end_stage + 1:
            raise ValueError("Latency of operator between ForwardDest and ForwardSource must be 1.")

        if svalid is None:
            svalid = vtypes.Int(1, width=1)

        width = self.get_width()
        signed = self.get_signed()
        value = self.args[0].sig_data
        index = self.args[1].sig_data

        data = m.Wire(self.name('data'), width, signed=signed)
        data.assign(value)
        self.sig_data = data

        self.dest.forward_value.assign(value)
        self.dest.forward_index.assign(index)
        self.dest.forward_valid.assign(svalid)


class CustomOp(_SpecialOperator):

    def __init__(self, op, *vars):
        _SpecialOperator.__init__(self, *vars)
        self.op = op

    def eval(self):
        return self


class LUT(_SpecialOperator):
    latency = 1

    def __init__(self, address, patterns, width=32, point=0, signed=True):
        _SpecialOperator.__init__(self, address)
        self.op = None
        self.width = width
        self.point = point
        self.signed = signed
        self.patterns = patterns
        self.graph_label = 'LUT'

    def _set_attributes(self):
        pass

    @property
    def address(self):
        return self.args[0]

    @address.setter
    def address(self, address):
        self.args[0] = address

    def _implement(self, m, seq, svalid=None, senable=None):
        if self.latency != 1:
            raise ValueError("Latency mismatch '%d' vs '%s'" %
                             (self.latency, 1))

        width = self.get_width()
        signed = self.get_signed()

        arg_data = self.address.sig_data

        size = int(log(len(self.patterns), 2))
        address = m.Wire(self.name('lut_address'), width=size)
        address.assign(arg_data)

        data = m.Wire(self.name('data'), width, signed=signed)
        self.sig_data = data

        inst = rom.mkROMDefinition(self.name('LUT_ROM'), self.patterns,
                                   size, width, sync=True, with_enable=True)
        clk = m._clock
        if senable is not None:
            enable = senable
        else:
            enable = vtypes.Int(1, 1)

        ports = [('CLK', clk), ('addr', address),
                 ('enable', enable), ('val', data)]

        m.Instance(inst, self.name('lut'), ports=ports)


class Complement2(_SpecialOperator):

    def __init__(self, var):
        _SpecialOperator.__init__(self, var)
        self.op = vtypes.Complement2

    def _set_attributes(self):
        self.width = self.var.get_width()
        self.point = self.var.get_point()
        self.signed = self.var.get_signed()

    @property
    def var(self):
        return self.args[0]

    @var.setter
    def var(self, var):
        self.args[0] = var

    def eval(self):
        var = self.var.eval()
        ret = Complement2(var)
        return ret


class Abs(_SpecialOperator):

    def __init__(self, var):
        _SpecialOperator.__init__(self, var)
        self.op = vtypes.Abs

    def _set_attributes(self):
        self.width = self.var.get_width()
        self.point = self.var.get_point()
        self.signed = self.var.get_signed()

    @property
    def var(self):
        return self.args[0]

    @var.setter
    def var(self, var):
        self.args[0] = var

    def eval(self):
        var = self.var.eval()
        ret = abs(var)
        return ret


class Sign(_SpecialOperator):

    def __init__(self, var):
        _SpecialOperator.__init__(self, var)
        self.op = vtypes.Sign

    def _set_attributes(self):
        self.width = self.var.get_width()
        self.point = self.var.get_point()
        self.signed = self.var.get_signed()

    @property
    def var(self):
        return self.args[0]

    @var.setter
    def var(self, var):
        self.args[0] = var

    def eval(self):
        var = self.var.eval()
        ret = Sign(var)
        return ret


class _Delay(_UnaryOperator):
    latency = 1

    def __init__(self, right):
        _UnaryOperator.__init__(self, right)
        # parent value for delayed_value and previous_value
        self.parent_value = None

        self.graph_label = 'Delay'
        self.graph_shape = 'box'
        self.graph_color = 'lightgray'
        self.graph_style = 'filled'

    def _set_parent_value(self, value):
        self.parent_value = value

    def _get_parent_value(self):
        return self.parent_value

    def eval(self):
        return self

    def _implement(self, m, seq, svalid=None, senable=None):
        if self.latency != 1:
            raise ValueError("Latency mismatch '%d' vs '%s'" %
                             (self.latency, 1))

        width = self.get_width()
        signed = self.get_signed()
        rdata = self.right.sig_data

        data = m.Reg(self.name('data'), width, initval=0, signed=signed)
        self.sig_data = data

        seq(data(rdata), cond=senable)


class _Prev(_UnaryOperator):
    latency = 0

    def __init__(self, right):
        _UnaryOperator.__init__(self, right)
        # parent value for delayed_value and previous_value
        self.parent_value = None

        self.graph_label = 'Prev'
        self.graph_shape = 'box'

    def _set_parent_value(self, value):
        self.parent_value = value

    def _get_parent_value(self):
        return self.parent_value

    def eval(self):
        return self

    def _implement(self, m, seq, svalid=None, senable=None):
        if self.latency != 0:
            raise ValueError("Latency mismatch '%d' vs '%s'" %
                             (self.latency, 0))

        width = self.get_width()
        signed = self.get_signed()
        rdata = self.right.sig_data

        data = m.Reg(self.name('data'), width, initval=0, signed=signed)
        self.sig_data = data

        seq(data(rdata), cond=senable)


class Alias(_UnaryOperator):
    latency = 0

    def __init__(self, right):
        _UnaryOperator.__init__(self, right)
        self.op = lambda x: x

        self.graph_label = 'Alias'
        self.graph_shape = 'box'
        self.graph_color = 'lightgray'
        self.graph_style = 'filled'


class Probe(_UnaryOperator):
    latency = 0

    def __init__(self, right, prefix='Probe'):
        _UnaryOperator.__init__(self, right)
        self.op = lambda x: x

        self.probe_name = '{}_{}'.format(prefix, self.object_id)
        self.graph_label = self.probe_name
        self.graph_shape = 'box'
        self.graph_color = 'lightgray'
        self.graph_style = 'filled'

    def name(self, prefix=None):
        clsname = self.__class__.__name__.lower()
        if prefix is None:
            prefix = 'tmp'
        return '_'.join(['', clsname, prefix, self.probe_name])


class _PlusN(_SpecialOperator):
    latency = 1

    def __init__(self, *vars):
        _SpecialOperator.__init__(self, *vars)

        for arg in self.args:
            if arg.point != 0:
                raise ValueError('Fixed point is not supported.')

        def plus_n(*args):
            ret = args[0]
            for arg in args[1:]:
                ret += arg
            return ret

        self.op = plus_n
        self.graph_label = 'PlusN'

    def eval(self):
        vars = [var.eval() for var in self.vars]
        for var in vars:
            if not isinstance(var, int):
                return PlusN(*vars)
        ret = 0
        for var in vars:
            ret += var
        return ret


class _MulAdd(_SpecialOperator):
    latency = 6 + 1

    def __init__(self, a, b, c):
        _SpecialOperator.__init__(self, a, b, c)

        if self.a.point + self.b.point != self.c.point:
            raise ValueError('Unsupported fixed point combination')

        self.graph_label = 'MulAdd'

    @property
    def a(self):
        return self.args[0]

    @a.setter
    def a(self, a):
        self.args[0] = a

    @property
    def b(self):
        return self.args[1]

    @b.setter
    def b(self, b):
        self.args[1] = b

    @property
    def c(self):
        return self.args[2]

    @c.setter
    def c(self, c):
        self.args[2] = c

    def _set_attributes(self):
        a_fp = self.a.get_point()
        b_fp = self.b.get_point()
        c_fp = self.c.get_point()
        a = self.a.get_width()
        b = self.b.get_width()
        c = self.c.get_width()
        self.width = max(a, b, c)
        self.point = a_fp + b_fp
        self.signed = self.a.get_signed() and self.b.get_signed() and self.c.get_signed()

    def _implement(self, m, seq, svalid=None, senable=None):
        if self.latency <= 3:
            raise ValueError("Latency of '*' operator must be greater than 3")

        width = self.get_width()
        signed = self.get_signed()

        apoint = self.a.get_point()
        bpoint = self.b.get_point()
        cpoint = self.c.get_point()
        awidth = self.a.get_width()
        bwidth = self.b.get_width()
        cwidth = self.c.get_width()
        asigned = self.a.get_signed()
        bsigned = self.b.get_signed()
        csigned = self.c.get_signed()
        adata = self.a.sig_data
        bdata = self.b.sig_data
        cdata = self.c.sig_data

        odata = m.Wire(self.name('madd_odata'),
                       max(awidth + bwidth, cwidth), signed=signed)
        odata_reg = m.Reg(self.name('madd_odata_reg'),
                          max(awidth + bwidth, cwidth), signed=signed, initval=0)

        data = m.Wire(self.name('data'), width, signed=signed)
        self.sig_data = data

        seq(odata_reg(odata), cond=senable)

        m.Assign(data(odata_reg))

        depth = self.latency - 1

        inst = madd.get_madd(awidth, bwidth, cwidth,
                             asigned, bsigned, csigned, depth)
        clk = m._clock

        update = m.Wire(self.name('madd_update'))

        if senable is not None:
            m.Assign(update(senable))
        else:
            m.Assign(update(vtypes.Int(1, 1)))

        ports = [('CLK', clk), ('update', update),
                 ('a', adata), ('b', bdata), ('c', cdata), ('d', odata)]

        m.Instance(inst, self.name('madd'), ports=ports)

    def eval(self):
        vars = [var.eval() for var in self.vars]
        for var in vars:
            if not isinstance(var, int):
                return MulAdd(*vars)

        return vars[0] * vars[1] + vars[2]


def MulAdd(a, b, c):
    a_point = a.point if isinstance(a, _Numeric) else 0
    b_point = b.point if isinstance(b, _Numeric) else 0
    c_point = c.point if isinstance(c, _Numeric) else 0
    if a_point + b_point != c_point:
        return Plus(Times(a, b), c)

    return _MulAdd(a, b, c)


def Madd(a, b, c):
    return MulAdd(a, b, c)


def op_tree(op, initval, latency, *args):
    if len(args) == 0:
        return initval

    if len(args) == 1:
        return args[0]

    half_len = len(args) // 2
    ret = op(op_tree(op, initval, latency, *args[:half_len]),
             op_tree(op, initval, latency, *args[half_len:]))

    if latency is not None:
        ret.latency = latency

    return ret


def PlusN(*args):
    for arg in args:
        if isinstance(arg, _Numeric) and arg.point != 0:
            ret = op_tree(Plus, Int(0, signed=True), 0, *args)
            ret.latency = 1
            return ret

    return _PlusN(*args)


def AddN(*args):
    return PlusN(*args)


def AddTree(*args):
    return op_tree(Plus, Int(0, signed=True), None, *args)


def Max(*args):
    if len(args) == 1:
        return args[0]
    initval = args[0]
    return op_tree(lambda x, y: Mux(x > y, x, y), initval, None, *args)


def Min(*args):
    if len(args) == 1:
        return args[0]
    initval = args[0]
    return op_tree(lambda x, y: Mux(x < y, x, y), initval, None, *args)


def Average(*args):
    sum = AddTree(*args)
    length = len(args)
    if length & (length - 1) == 0:
        return Sra(sum, int(log(length, 2)))
    return Div(sum, Int(length, signed=True))


def AverageRound(*args):
    sum = AddTree(*args)
    length = len(args)
    sum += length // 2
    if length & (length - 1) == 0:
        return Sra(sum, int(log(length, 2)))
    return Div(sum, Int(length, signed=True))


def SraRound(left, right):
    msb = left[-1]
    msb.latency = 0

    if isinstance(right, int) and right <= 0:
        rounder = 0
    elif isinstance(right, int):
        rounder = 1 << (right - 1)
    else:
        right_slice = right
        right_width = int(ceil(log(left.width, 2)))
        if right_width < right.width:
            right_slice = right[0:right_width]
            right_slice.latency = 0

        right_minus_one = right_slice - 1
        right_minus_one.latency = 0
        rounder = Sll(Int(1), right_minus_one)
        rounder.latency = 0

    rounder_sign = Mux(msb, Int(-1), Int(0))
    rounder_sign.latency = 0

    pre_round = left + rounder
    pre_round.width = left.width + 1
    pre_round.latency = 0

    pre_round = pre_round + rounder_sign
    pre_round.latency = 0

    shifted = Sra(pre_round, right)
    shifted.width = left.width
    shifted.latency = 0

    cond = right == Int(0)
    cond.latency = 0

    return Mux(cond, left, shifted)


class _Constant(_Numeric):

    def __init__(self, value):
        _Numeric.__init__(self)
        self.value = value
        self.signed = False
        self._set_attributes()
        self._set_managers()
        self.sig_data = self.value

        self.graph_shape = 'box'
        self.graph_color = 'lightblue'
        self.graph_style = 'rounded,filled'
        self.graph_peripheries = 1

    def _set_attributes(self):
        self.width = vtypes.get_width(self.value)
        self.point = 0
        self.signed = False

    def _set_managers(self):
        self._set_strm(_get_strm(self.value))
        self._set_module(getattr(self.strm, 'module', None))
        self._set_seq(getattr(self.strm, 'seq', None))

    def eval(self):
        return self.value

    def _implement(self, m, seq, svalid=None, senable=None):
        data = self.value
        self.sig_data = data


class _Variable(_Numeric):

    def __init__(self, data=None, width=32, point=0, signed=True):
        _Numeric.__init__(self)
        self.input_data = data
        if isinstance(self.input_data, _Numeric):
            self.input_data._add_sink(self)
        self.width = width
        self.point = point
        self.signed = signed

        if isinstance(self.input_data, _Numeric):
            self.graph_label = self.input_data.graph_label
        else:
            inobj = str(self.input_data)
            label_data = [inobj, str(self.width)]
            if self.point > 0:
                label_data.append(str(self.point))
            self.graph_label = ':'.join(label_data)

        self.graph_shape = 'box'
        self.graph_color = 'lightblue'
        self.graph_style = 'filled'
        self.graph_peripheries = 2

    def eval(self):
        return self

    def output(self, data):
        if isinstance(self.input_data, _Numeric):
            self.input_data.output(data)
            return
        _Numeric.output(self, data)

    def connect(self, data):
        if self.sig_data is not None:
            raise ValueError("Input signals are already synthesized.")

        if not isinstance(data, (_Numeric, vtypes._Numeric, int, bool)):
            raise TypeError(
                "'data' must be stypes._Numeric or vtypes._Numeric.")

        self.input_data = data
        if isinstance(self.input_data, _Numeric):
            self.input_data._add_sink(self)

    def write(self, wdata, cond=None):
        if self.sig_data is None:
            if self.m is None:
                raise ValueError("Module information is not set.")
            self._implement_input(self.m, self.seq, aswire=True)

        if isinstance(self.sig_data, vtypes.Input):
            raise TypeError("Variable with Input type is not supported.")

        if isinstance(self.sig_data, vtypes.Wire):
            width = self.get_width()
            signed = self.get_signed()
            if hasattr(self, 'sig_data_write'):
                data = self.sig_data_write
            else:
                data = self.m.Reg(self.name('wdata'),
                                  width, initval=0, signed=signed)
                self.sig_data_write = data
                self.sig_data.assign(data)
        else:
            data = self.sig_data

        if cond is not None:
            self.seq.If(cond)

        self.seq(
            data(wdata)
        )

    def _implement(self, m, seq, svalid=None, senable=None):
        if self.input_data is None:
            raise TypeError("'input_data' must not be None.")

        # if input_data is a standard signal, skip
        if not isinstance(self.input_data, _Numeric):
            return

        if self.input_data.sig_data is None:
            self.input_data._implement(m, seq)

        self.sig_data = self.input_data.sig_data

    def _implement_input(self, m, seq, aswire=False):
        if self.input_data is None:
            raise TypeError("'input_data' must not be None")

        # if input_data is an other variable, skip
        if isinstance(self.input_data, _Numeric):
            return

        # if already synthesized
        if self.sig_data is not None:
            return

        type_i = m.Wire if aswire else m.Input
        type_o = m.Wire if aswire else m.Output

        width = self.get_width()
        signed = self.get_signed()

        if isinstance(self.input_data, (vtypes._Numeric, int, bool)):
            self.sig_data = self.input_data
        else:
            self.sig_data = type_i(self.input_data, width, signed=signed)

    def _implement_output(self, m, seq, aswire=False):
        if isinstance(self.input_data, _Numeric):
            if self.input_data.output_sig_data is None:
                self.input_data._implement_output(m, seq, aswire)
            self.output_sig_data = self.input_data.output_sig_data
            return
        _Numeric._implement_output(self, m, seq, aswire)

    # __getattribute__() method is always called,
    # whenever fields of the node is accessed.
    def __getattribute__(self, attr):
        # for isinstance method
        if attr == '__class__':
            return _Numeric.__getattribute__(self, '__class__')

        try:
            input_data = _Numeric.__getattribute__(self, 'input_data')
        except AttributeError:
            return _Numeric.__getattribute__(self, attr)

        # always returns input_data for 'input_data' attribute
        if attr == 'input_data':
            return input_data

        # if it has a variable alias, redirect to it
        if isinstance(input_data, _Numeric):
            return getattr(input_data, attr)

        # nornal access
        return _Numeric.__getattribute__(self, attr)


class _ParameterVariable(_Variable):

    def __init__(self, data, width=32, point=0, signed=True, value=None):
        if isinstance(data, _Numeric):
            raise TypeError(
                "_ParameterVariable cannot receive type '%s'" % str(type(data)))

        if value is not None and not isinstance(data, str):
            raise TypeError(
                "Required str for 'data', when 'value' is assigned")

        _Variable.__init__(self, data=data, width=width,
                           point=point, signed=signed)
        self.value = value

        inobj = str(self.input_data)
        label_data = [inobj, str(self.width)]
        if self.point > 0:
            label_data.append(str(self.point))
        self.graph_label = ':'.join(label_data)

        self.graph_shape = 'circle'
        self.graph_color = 'lightblue'
        self.graph_style = 'filled'
        self.graph_peripheries = 1

    def _implement(self, m, seq, svalid=None, senable=None):
        pass

    def _implement_input(self, m, seq, aswire=False):
        type_i = m.Wire if aswire else m.Input

        width = self.get_width()
        signed = self.get_signed()

        if isinstance(self.input_data, (vtypes._Numeric, int, bool)):
            self.sig_data = self.input_data
        elif self.value is not None:
            self.sig_data = m.Parameter(self.input_data, self.value,
                                        width=self.width, signed=self.signed)
        else:
            self.sig_data = type_i(
                self.input_data, self.width, signed=self.signed)

    def __getattribute__(self, attr):
        # normal access
        return _Numeric.__getattribute__(self, attr)


class _Accumulator(_UnaryOperator):
    latency = 1
    ops = (vtypes.Plus, )

    def __init__(self, right, size=None, interval=None, initval=None, offset=None,
                 dependency=None, enable=None, reset=None, width=32, signed=True):

        self.size = _to_constant(size) if size is not None else None
        self.interval = _to_constant(interval) if interval is not None else None
        self.initval = (_to_constant(initval)
                        if initval is not None else _to_constant(0))
        self.offset = (_to_constant(offset)
                       if offset is not None else None)

        if not isinstance(self.initval, _Constant):
            raise TypeError("initval must be Constant, not '%s'" %
                            str(type(self.initval)))

        self.dependency = dependency

        self.enable = _to_constant(enable)
        if self.enable is not None:
            self.enable._add_sink(self)

        self.reset = _to_constant(reset)
        if self.reset is not None:
            self.reset._add_sink(self)

        _UnaryOperator.__init__(self, right)
        self.width = width
        self.signed = signed

        self.graph_shape = 'box'
        self.graph_style = 'rounded'

    def _set_attributes(self):
        self.point = self.right.get_point()

    def _set_managers(self):
        self._set_strm(_get_strm(self.right, self.initval,
                                 self.offset, self.dependency,
                                 self.enable, self.reset))
        self._set_module(getattr(self.strm, 'module', None))
        self._set_seq(getattr(self.strm, 'seq', None))

    def eval(self):
        return self

    def _implement(self, m, seq, svalid=None, senable=None):
        if self.latency != 1:
            raise ValueError("Latency mismatch '%d' vs '%s'" %
                             (self.latency, 1))

        size_data = self.size.sig_data if self.size is not None else None
        interval_data = self.interval.sig_data if self.interval is not None else None

        initval_data = self.initval.sig_data
        width = self.get_width()
        signed = self.get_signed()

        # for Pulse
        if not self.ops and self.size is not None:
            width = 1

        data = m.Reg(self.name('data'), width,
                     initval=initval_data, signed=signed)

        self.sig_data = data

        rdata = self.right.sig_data
        enabledata = self.enable.sig_data if self.enable is not None else None
        resetdata = self.reset.sig_data if self.reset is not None else None

        if self.interval is not None:
            interval_count = m.Reg(self.name('interval_count'), width, initval=0)

        reset_cond_values = []

        if self.reset is not None:
            reset_cond_values.append(resetdata)

        if self.size is not None:
            count = m.Reg(self.name('count'),
                          size_data.get_width() + 1, initval=0)
            prev_count_max = m.Reg(self.name('prev_count_max'), initval=0)
            reset_cond_values.append(prev_count_max)

        reset_cond = m.Wire(self.name('reset_cond'))

        if len(reset_cond_values) > 0:
            reset_cond.assign(vtypes.Ors(*reset_cond_values))
            if self.size is not None:
                current_count = vtypes.Mux(reset_cond, 0, count)
            if self.interval is not None:
                current_interval_count = vtypes.Mux(reset_cond, 0, interval_count)

            current_data = vtypes.Mux(reset_cond, initval_data, data)

        else:
            reset_cond.assign(0)
            if self.size is not None:
                current_count = count
            if self.interval is not None:
                current_interval_count = interval_count

            current_data = data

        if self.size is not None:
            next_count_value = vtypes.Mux(current_count >= size_data - 1,
                                          0, current_count + 1)
            count_max = (current_count >= size_data - 1)

        if self.interval is not None:
            next_interval_count = vtypes.Mux(current_interval_count >= interval_data - 1,
                                             0, current_interval_count + 1)
            interval_enable = (current_interval_count == interval_data - 1)

        value = current_data
        for op in self.ops:
            if not isinstance(op, type):
                value = op(value, rdata)
            elif issubclass(op, vtypes._BinaryOperator):
                value = op(value, rdata)
            elif issubclass(op, vtypes._UnaryOperator):
                value = op(value)

            if not isinstance(value, vtypes._Numeric):
                raise TypeError("Operator '%s' returns unsupported object type '%s'."
                                % (str(op), str(type(value))))

        # for Pulse
        if not self.ops and self.size is not None:
            value = (current_count >= (size_data - 1))

        enable_cond = _and_vars(svalid, senable)

        if self.reset is not None:
            enable_reset_cond = _and_vars(enable_cond, reset_cond)
            seq(data(initval_data), cond=enable_reset_cond)

        if self.enable is not None:
            enable_cond = _and_vars(enable_cond, enabledata)

        if self.interval is not None:
            seq(interval_count(next_interval_count), cond=enable_cond)
            enable_cond = _and_vars(enable_cond, interval_enable)

        seq(data(value), cond=enable_cond)

        if self.size is not None:
            seq(count(next_count_value), cond=enable_cond)
            seq(prev_count_max(count_max), cond=enable_cond)


class ReduceAdd(_Accumulator):
    ops = (vtypes.Plus, )

    def __init__(self, right, size=None, interval=None, initval=0,
                 enable=None, reset=None, width=32, signed=True):
        offset = None
        dependency = None
        _Accumulator.__init__(self, right, size, interval, initval, offset,
                              dependency, enable, reset, width, signed)
        self.graph_label = 'ReduceAdd'


class ReduceSub(_Accumulator):
    ops = (vtypes.Minus, )

    def __init__(self, right, size=None, interval=None, initval=0,
                 enable=None, reset=None, width=32, signed=True):
        offset = None
        dependency = None
        _Accumulator.__init__(self, right, size, interval, initval, offset,
                              dependency, enable, reset, width, signed)
        self.graph_label = 'ReduceSub'


class ReduceMul(_Accumulator):
    latency = 1
    ops = (vtypes.Times, )

    def __init__(self, right, size=None, interval=None, initval=0,
                 enable=None, reset=None, width=32, signed=True):
        offset = None
        dependency = None
        _Accumulator.__init__(self, right, size, interval, initval, offset,
                              dependency, enable, reset, width, signed)
        self.graph_label = 'ReduceMul'


class ReduceDiv(_Accumulator):
    latency = 32
    ops = ()

    def __init__(self, right, size=None, interval=None, initval=0,
                 enable=None, reset=None, width=32, signed=True):
        raise NotImplementedError()
        offset = None
        dependency = None
        _Accumulator.__init__(self, right, size, interval, initval, offset,
                              dependency, enable, reset, width, signed)
        self.graph_label = 'ReduceDiv'


class ReduceMax(_Accumulator):
    ops = (lambda x, y: vtypes.Mux(x < y, y, x), )

    def __init__(self, right, size=None, interval=None, initval=0,
                 enable=None, reset=None, width=32, signed=True):
        offset = None
        dependency = None
        _Accumulator.__init__(self, right, size, interval, initval, offset,
                              dependency, enable, reset, width, signed)
        self.graph_label = 'ReduceMax'


class ReduceMin(_Accumulator):
    ops = (lambda x, y: vtypes.Mux(x > y, y, x), )

    def __init__(self, right, size=None, interval=None, initval=0,
                 enable=None, reset=None, width=32, signed=True):
        offset = None
        dependency = None
        _Accumulator.__init__(self, right, size, interval, initval, offset,
                              dependency, enable, reset, width, signed)
        self.graph_label = 'ReduceMin'


class ReduceCustom(_Accumulator):

    def __init__(self, ops, right, size=None, interval=None, initval=0,
                 enable=None, reset=None, width=32, signed=True, label=None):
        offset = None
        dependency = None
        _Accumulator.__init__(self, right, size, interval, initval, offset,
                              dependency, enable, reset, width, signed)
        if not isinstance(ops, (tuple, list)):
            ops = tuple([ops])
        self.ops = ops
        self.graph_label = label


class Counter(_Accumulator):

    def __init__(self, size=None, step=1, interval=None, initval=0, offset=None,
                 dependency=None, enable=None, reset=None, width=32, signed=False):

        _Accumulator.__init__(self, step, size, interval, initval, offset,
                              dependency, enable, reset, width, signed)
        self.graph_label = 'Counter'

    def _implement(self, m, seq, svalid=None, senable=None):
        if self.latency != 1:
            raise ValueError("Latency mismatch '%d' vs '%s'" %
                             (self.latency, 1))

        size_data = self.size.sig_data if self.size is not None else None
        interval_data = self.interval.sig_data if self.interval is not None else None

        initval_data = self.initval.sig_data
        width = self.get_width()
        signed = self.get_signed()

        step = self.right.sig_data
        offset_data = self.offset.sig_data if self.offset is not None else None

        data = m.Reg(self.name('data'), width,
                     initval=initval_data, signed=signed)

        count = m.Reg(self.name('count'), width,
                      initval=initval_data, signed=signed)

        self.sig_data = data

        enabledata = self.enable.sig_data if self.enable is not None else None
        resetdata = self.reset.sig_data if self.reset is not None else None

        if self.interval is not None:
            interval_count = m.Reg(self.name('interval_count'), width, initval=0)

        reset_cond = m.Wire(self.name('reset_cond'))
        if self.reset is not None:
            reset_cond.assign(resetdata)
            current_count = vtypes.Mux(reset_cond, initval_data, count)
        else:
            reset_cond.assign(0)
            current_count = count

        if self.interval is not None:
            current_interval_count = vtypes.Mux(reset_cond, 0, interval_count)

        next_count_value = current_count + step

        if self.size is not None and self.offset is not None:
            next_count_value = vtypes.Mux(current_count >= size_data - step,
                                          offset_data, next_count_value)
        elif self.size is not None:
            next_count_value = vtypes.Mux(current_count >= size_data - step,
                                          next_count_value - size_data, next_count_value)

        if self.interval is not None:
            next_interval_count = vtypes.Mux(current_interval_count >= interval_data - 1,
                                             0, current_interval_count + 1)
            interval_enable = (current_interval_count == interval_data - 1)

        enable_cond = _and_vars(svalid, senable)

        if self.reset is not None:
            enable_reset_cond = _and_vars(enable_cond, reset_cond)
            seq(data(initval_data), cond=enable_reset_cond)

        seq(data(count), cond=enable_cond)

        if self.enable is not None:
            enable_cond = _and_vars(enable_cond, enabledata)

        if self.interval is not None:
            seq(interval_count(next_interval_count), cond=enable_cond)
            enable_cond = _and_vars(enable_cond, interval_enable)

        seq(count(next_count_value), cond=enable_cond)


class Pulse(_Accumulator):
    ops = ()

    def __init__(self, size, interval=None,
                 dependency=None, enable=None, reset=None):

        right = 0
        if dependency is not None:
            right = dependency

        initval = 0
        offset = None
        width = 1
        signed = False

        _Accumulator.__init__(self, right, size, interval, initval, offset,
                              dependency, enable, reset, width, signed)
        self.graph_label = 'Pulse'


def _ReduceValid(cls, right, size, interval=None, initval=0,
                 enable=None, reset=None, width=32, signed=True):

    data = cls(right, size, interval, initval,
               enable, reset, width, signed)
    valid = Pulse(size, dependency=right, enable=enable, reset=reset)

    return data, valid


def ReduceAddValid(right, size, interval=None, initval=0,
                   enable=None, reset=None, width=32, signed=True):

    cls = ReduceAdd
    return _ReduceValid(cls, right, size, interval, initval,
                        enable, reset, width, signed)


def ReduceSubValid(right, size, interval=None, initval=0,
                   enable=None, reset=None, width=32, signed=True):

    cls = ReduceSub
    return _ReduceValid(cls, right, size, interval, initval,
                        enable, reset, width, signed)


def ReduceMulValid(right, size, interval=None, initval=0,
                   enable=None, reset=None, width=32, signed=True):

    cls = ReduceMul
    return _ReduceValid(cls, right, size, interval, initval,
                        enable, reset, width, signed)


def ReduceDivValid(right, size, interval=None, initval=0,
                   enable=None, reset=None, width=32, signed=True):

    cls = ReduceDiv
    return _ReduceValid(cls, right, size, interval, initval,
                        enable, reset, width, signed)


def ReduceMaxValid(right, size, interval=None, initval=0,
                   enable=None, reset=None, width=32, signed=True):

    cls = ReduceMax
    return _ReduceValid(cls, right, size, interval, initval,
                        enable, reset, width, signed)


def ReduceMinValid(right, size, interval=None, initval=0,
                   enable=None, reset=None, width=32, signed=True):

    cls = ReduceMin
    return _ReduceValid(cls, right, size, interval, initval,
                        enable, reset, width, signed)


def ReduceCustomValid(ops, right, size, interval=None, initval=0,
                      enable=None, reset=None, width=32, signed=True):

    data = ReduceCustom(ops, right, size, interval, initval,
                        enable, reset, width, signed)
    valid = Pulse(size, dependency=right, enable=enable, reset=reset)

    return data, valid


def CounterValid(size, step=1, interval=None, initval=0, offset=None,
                 dependency=None, enable=None, reset=None, width=32, signed=False):

    data = Counter(size, step, interval, initval, offset,
                   dependency, enable, reset, width, signed)
    valid = Pulse(size, dependency=dependency, enable=enable, reset=reset)

    return data, valid


class Int(_Constant):

    def __init__(self, value, signed=True):
        _Constant.__init__(self, value)
        self.signed = signed

    def _set_attributes(self):
        self.width = vtypes.get_width(self.value)
        self.point = 0

    def _implement(self, m, seq, svalid=None, senable=None):
        data = vtypes.Int(self.value, width=self.width, signed=self.signed)
        self.sig_data = data


class Float(_Constant):

    def _set_attributes(self):
        self.width = 32
        self.point = 0
        self.signed = True


class FixedPoint(_Constant):

    def __init__(self, value, point=0, signed=True):
        _Constant.__init__(self, value)
        self.point = point
        self.signed = signed

    def _set_attributes(self):
        self.width = vtypes.get_width(self.value)
        self.point = 0

    def _implement(self, m, seq, svalid=None, senable=None):
        data = vtypes.Int(self.value, width=self.width)
        self.sig_data = data


class Str(_Constant):

    def _set_attributes(self):
        self.width = 0
        self.point = 0
        self.signed = False


class Substream(_SpecialOperator):
    def __init__(self, substrm, strm=None):
        _SpecialOperator.__init__(self)
        self.strm = strm
        self._set_managers()

        self.width = 1
        self.point = 0
        self.signed = True

        self.graph_label = substrm.name if hasattr(substrm, 'name') else 'Substream'
        self.graph_shape = 'box'
        self.graph_peripheries = 2

        if not substrm.aswire:
            raise ValueError('aswire must be True.')
        if substrm.module is None:
            raise ValueError('module must not be None.')
        if substrm.clock is None:
            raise ValueError('clock must not be None.')
        if substrm.reset is None:
            raise ValueError('reset must not be None.')

        if not substrm.implemented:
            substrm.implement()

        self.substrm = substrm
        self.latency = substrm.pipeline_depth() + 1
        self.conds = OrderedDict()

    def _set_managers(self):
        self._set_module(getattr(self.strm, 'module', None))
        self._set_seq(getattr(self.strm, 'seq', None))

    def write(self, name, data, cond=None):
        wdata = _to_constant(data)
        self.args.append(wdata)
        if name in self.conds:
            raise ValueError('already assigned')
        self.conds[name] = cond

    def read(self, name):
        var = self.substrm.get_named_numeric(name)
        if self.strm is None:
            return _SubstreamOutput(self, var)
        return self.strm._SubstreamOutput(self, var, name)

    def _implement(self, m, seq, svalid=None, senable=None):
        arg_data = [arg.sig_data for arg in self.args]

        for data, (name, cond) in zip(arg_data, self.conds.items()):
            var = self.substrm.get_named_numeric(name)
            if senable is not None and cond is not None:
                write_cond = vtypes.Ands(cond, senable)
            elif senable is not None:
                write_cond = senable
            else:
                write_cond = cond
            var.write(data, write_cond)

        self.sig_data = vtypes.Int(0)


class _SubstreamOutput(_UnaryOperator):

    def __init__(self, substrm, output_var, var_name):
        _UnaryOperator.__init__(self, substrm)
        self.var_name = var_name
        self.output_var = output_var

        self.width = output_var.get_width()
        self.point = output_var.get_point()
        self.signed = output_var.get_signed()

        self.graph_label = substrm.graph_label + '\n' + self.var_name
        self.graph_shape = 'box'
        self.graph_peripheries = 2

    def _implement(self, m, seq, svalid=None, senable=None):
        width = self.get_width()
        signed = self.get_signed()
        rdata = self.output_var.read()

        if self.latency == 0:
            data = m.Wire(self.name('data'), width, signed=signed)
            data.assign(rdata)
            self.sig_data = data

        elif self.latency == 1:
            data = m.Reg(self.name('data'), width, initval=0, signed=signed)
            self.sig_data = data
            seq(data(rdata), cond=senable)

        else:
            prev_data = None

            for i in range(self.latency):
                data = m.Reg(self.name('data_d%d' % i),
                             width, initval=0, signed=signed)
                if i == 0:
                    seq(data(rdata), cond=senable)
                else:
                    seq(data(prev_data), cond=senable)
                prev_data = data

            self.sig_data = data


class RingBuffer(_UnaryOperator):
    latency = 1

    def __init__(self, var, length, enable=None):

        self.enable = _to_constant(enable)
        if self.enable is not None:
            self.enable._add_sink(self)

        self.length = length

        _UnaryOperator.__init__(self, var)

        self.num_ports = 1
        self.read_vars = []

        self.graph_label = 'RingBufferIn'
        self.graph_shape = 'box'

    def _set_managers(self):
        self._set_strm(_get_strm(self.right, self.enable))
        self._set_module(getattr(self.strm, 'module', None))
        self._set_seq(getattr(self.strm, 'seq', None))

    def read(self, offset):
        var = _RingBufferOutput(self, offset, self.num_ports, self.enable)
        self.read_vars.append(var)
        self.num_ports += 1
        return var

    def _implement(self, m, seq, svalid=None, senable=None):
        if self.latency != 1:
            raise ValueError("Latency mismatch '%d' vs '%s'" %
                             (self.latency, 1))

        datawidth = self.get_width()
        addrwidth = int(ceil(log(self.length, 2)))
        signed = self.get_signed()

        clk = m._clock
        self.ram = ram.SyncRAM(m, self.name('ram'),
                               clk, datawidth, addrwidth, self.num_ports)

        enabledata = self.enable.sig_data if self.enable is not None else None

        wdata = m.Wire(self.name('wdata'), datawidth, signed=signed)
        wdata.assign(self.right.sig_data)

        waddr = m.Reg(self.name('waddr'), addrwidth, initval=0)
        self.waddr = waddr

        wcond = _and_vars(svalid, senable, enabledata)

        next_waddr = vtypes.Mux(waddr == self.length - 1, 0, waddr + 1)
        seq(waddr(next_waddr), cond=wcond)

        wenable = wcond
        self.ram.connect(0, waddr, wdata, wenable)

        self.sig_data = wdata


class _RingBufferOutput(_BinaryOperator):
    latency = 1

    def __init__(self, buf, offset, port, enable=None):

        self.enable = _to_constant(enable)
        if self.enable is not None:
            self.enable._add_sink(self)

        self.port = port

        _BinaryOperator.__init__(self, buf, offset)
        self.buf = buf

        self.graph_label = 'RingBufferOut'
        self.graph_shape = 'box'

    def _set_managers(self):
        self._set_strm(_get_strm(self.left, self.right, self.enable))
        self._set_module(getattr(self.strm, 'module', None))
        self._set_seq(getattr(self.strm, 'seq', None))

    def _implement(self, m, seq, svalid=None, senable=None):
        if self.latency != 1:
            raise ValueError("Latency mismatch '%d' vs '%s'" %
                             (self.latency, 1))

        datawidth = self.get_width()
        addrwidth = int(ceil(log(self.buf.length, 2)))
        signed = self.get_signed()

        enabledata = self.enable.sig_data if self.enable is not None else None

        rdata = m.Wire(self.name('rdata'), datawidth, signed=signed)

        diff_latency = self.start_stage - self.buf.start_stage
        raddr_base = seq.Prev(self.buf.waddr, diff_latency)

        raddr = raddr_base + self.right.sig_data
        raddr = vtypes.Mux(raddr >= self.buf.length,
                           raddr - self.buf.length, raddr)

        self.buf.ram.connect(self.port, raddr, 0, 0)
        rdata.assign(self.buf.ram.rdata(self.port))

        self.sig_data = rdata


class Scratchpad(_BinaryOperator):
    latency = 1

    def __init__(self, var, addr, length, when=None):

        self.enable = _to_constant(when)
        if self.enable is not None:
            self.enable._add_sink(self)

        self.length = length

        _BinaryOperator.__init__(self, var, addr)

        self.num_ports = 1
        self.read_vars = []

        self.graph_label = 'ScratchpadIn'
        self.graph_shape = 'box'

    def _set_managers(self):
        self._set_strm(_get_strm(self.left, self.right, self.enable))
        self._set_module(getattr(self.strm, 'module', None))
        self._set_seq(getattr(self.strm, 'seq', None))

    def read(self, addr):
        var = _ScratchpadOutput(self, addr, self.num_ports)
        self.read_vars.append(var)
        self.num_ports += 1
        return var

    def _implement(self, m, seq, svalid=None, senable=None):
        if self.latency != 1:
            raise ValueError("Latency mismatch '%d' vs '%s'" %
                             (self.latency, 1))

        datawidth = self.get_width()
        addrwidth = int(ceil(log(self.length, 2)))
        signed = self.get_signed()

        clk = m._clock
        self.ram = ram.SyncRAM(m, self.name('ram'),
                               clk, datawidth, addrwidth, self.num_ports)

        enabledata = self.enable.sig_data if self.enable is not None else None

        wdata = m.Wire(self.name('wdata'), datawidth, signed=signed)
        wdata.assign(self.left.sig_data)

        waddr = m.Wire(self.name('waddr'), addrwidth)
        waddr.assign(self.right.sig_data)

        wenable = _and_vars(svalid, senable, enabledata)
        self.ram.connect(0, waddr, wdata, wenable)

        self.sig_data = wdata


class _ScratchpadOutput(_BinaryOperator):
    latency = 1

    def __init__(self, sp, addr, port):
        self.port = port
        _BinaryOperator.__init__(self, sp, addr)
        self.sp = sp

        self.graph_label = 'ScratchpadOut'
        self.graph_shape = 'box'

    def _implement(self, m, seq, svalid=None, senable=None):
        if self.latency != 1:
            raise ValueError("Latency mismatch '%d' vs '%s'" %
                             (self.latency, 1))

        datawidth = self.get_width()
        addrwidth = int(ceil(log(self.sp.length, 2)))
        signed = self.get_signed()

        rdata = m.Wire(self.name('rdata'), datawidth, signed=signed)

        raddr = m.Wire(self.name('raddr'), addrwidth)
        raddr.assign(self.right.sig_data)

        self.sp.ram.connect(self.port, raddr, 0, 0)
        rdata.assign(self.sp.ram.rdata(self.port))

        self.sig_data = rdata


class ToExtern(_SpecialOperator):
    latency = 1

    def __init__(self, value):
        _SpecialOperator.__init__(self, value)

        self.output_tmp()

        self.graph_label = 'ToExtern'
        self.graph_shape = 'box'

    @property
    def data(self):
        return self.sig_data

    def eval(self):
        return self

    def _implement(self, m, seq, svalid=None, senable=None):
        width = self.get_width()
        point = self.get_point()
        signed = self.get_signed()
        ldata = self.args[0].sig_data

        valid_value = _and_vars(svalid, senable)

        if self.latency == 0:
            valid = m.Wire(self.name('valid'))
            valid.assign(valid_value)
            self.valid = valid

            data = fx.FixedWire(m, self.name('data'), width, point, signed=signed)
            data.assign(ldata)
            self.sig_data = data

        elif self.latency == 1:
            valid = m.Reg(self.name('valid'), initval=0)
            self.valid = valid
            seq(valid(valid_value), cond=senable)

            data = fx.FixedReg(m, self.name('data'), width, point, initval=0, signed=signed)
            self.sig_data = data
            seq(data(ldata), cond=senable)

        else:
            prev_valid = None
            prev_data = None

            for i in range(self.latency):
                valid = m.Reg(self.name('valid_d%d' % i), initval=0)
                data = fx.FixedReg(m, self.name('data_d%d' % i),
                                   width, point, initval=0, signed=signed)
                if i == 0:
                    seq(valid(valid_value), cond=senable)
                    seq(data(self.op(ldata)), cond=senable)
                else:
                    seq(valid(prev_valid), cond=senable)
                    seq(data(prev_data), cond=senable)

                prev_valid = valid
                prev_data = data

            self.sig_data = data


class FromExtern(_UnaryOperator):
    __intrinsics__ = ('write')
    latency = 1

    def __init__(self, right, width=None, point=None, signed=True, latency=1):
        _UnaryOperator.__init__(self, right)

        if width is not None:
            self.width = width

        if point is not None:
            self.point = point

        self.signed = signed

        self.latency = latency

        self.graph_label = 'FromExtern'
        self.graph_shape = 'box'

    @property
    def data(self):
        return self.sig_data

    def eval(self):
        return self

    def _implement(self, m, seq, svalid=None, senable=None):
        width = self.get_width()
        point = self.get_point()
        signed = self.get_signed()

        self.valid = svalid
        self.enable = senable

        data = fx.FixedReg(m, self.name('data'), width, point, initval=0, signed=signed)
        self.sig_data = data

    def write(self, fsm, value):
        cond = fsm.here

        self.seq.If(cond)(
            self.sig_data(value)
        )


class _LineBufferOut(_UnaryOperator):
    latency = 1

    def index_to_index_tuple(self, index):
        orig_index = index
        index_list = []
        def prod(l): return 1 if len(l) == 0 else l[0] * prod(l[1:])

        for i in range(1, self.linebuf.n_dim):
            elmnum = prod(self.linebuf.shape[:-i])
            index_list = [index // elmnum] + index_list
            index = index % elmnum

        index_list = [index] + index_list
        return tuple(index_list)

    def __init__(self, linebuf, index):
        self.linebuf = linebuf

        if isinstance(index, tuple) and all(isinstance(i, int) for i in index):
            self.index = index
        elif isinstance(index, int):
            self.index = self.index_to_index_tuple(index)
        else:
            raise ValueError("index must be int constant or tuple of int constant")

        self.width = linebuf.width
        self.point = linebuf.point
        self.signed = linebuf.signed
        _UnaryOperator.__init__(self, linebuf)
        self.graph_label = 'LineBufOut'
        self.graph_shape = 'box'

    def _implement(self, m, seq, svalid=None, senable=None):
        self.sig_data = self.linebuf.windowreg[self.index]


class LineBuffer(_SpecialOperator):
    latency = 1

    def __init__(self, shape, memlens, data,
                 head_initvals, tail_initvals,
                 shift_cond, rotate_conds=None):

        if (not isinstance(shape, tuple) or
                all(isinstance(d, int) for d in shape) is False):
            raise ValueError("shape must be tuple of int constant")

        if (isinstance(memlens, list) is False or
                all([isinstance(memlen, int) for memlen in memlens]) is False):
            raise ValueError("memlen must be list of int constant")

        self.shape = shape
        self.n_dim = len(self.shape)

        if (not isinstance(head_initvals, list) or
            len(head_initvals) != self.n_dim - 1 or
                all([isinstance(val, int) for val in head_initvals]) is False):
            raise ValueError(
                "head_initval must be list of int constant whose length is len(shape)-1")

        if (not isinstance(tail_initvals, list) or
            len(tail_initvals) != self.n_dim - 1 or
                all([isinstance(val, int) for val in tail_initvals]) is False):
            raise ValueError(
                "tail_initval must be list of int constant whose length is len(shape)-1")

        args = [data, shift_cond]

        if rotate_conds is not None:
            if len(rotate_conds) != self.n_dim - 1:
                raise ValueError("len(rotate_conds) must be equal to len(shape)-1")
            args.extend(rotate_conds)

        _SpecialOperator.__init__(self, *args)

        self.width = data.get_width()
        self.point = data.get_point()
        self.signed = data.get_signed()
        self.graph_label = 'LineBuffer'
        self.graph_shape = 'box'

        def prod(l): return 1 if len(l) == 0 else l[0] * prod(l[1:])
        self.window_num = prod(self.shape)
        self.windowreg = np.empty(self.shape, dtype=object)
        self.head_initvals = head_initvals
        self.tail_initvals = tail_initvals
        self.memlens = memlens
        self._delay_cnt = 0

#    def _delayed(self, m, seq, data):
#        if data is None:
#            return None
#
#        delayed = fx.FixedReg(m, self.name('delay' + str(self._delay_cnt)),
#                              data.get_width(), 0, initval=0, signed=data.get_signed())
#        seq(delayed(data))
#        self._delay_cnt += 1
#        return delayed

    def _implement(self, m, seq, svalid=None, senable=None):
        width = self.get_width()
        point = self.get_point()
        signed = self.get_signed()

        window_indices = list(itertools.product(*[range(d) for d in self.shape]))

        for index in window_indices:
            window_index_s = '_'.join(list(map(str, index)))
            self.windowreg[index] = fx.FixedReg(m, self.name(
                'winreg' + window_index_s), width, point, initval=0, signed=signed)

        shiftmemout = [None] * (self.n_dim)
        for i in range(1, self.n_dim):
            dim_i_memshape = self.shape[i:]
            shiftmemout[i] = np.empty(dim_i_memshape, dtype=object)
            dim_i_rangelist = [range(d) for d in dim_i_memshape]
            dim_i_mem_indices = itertools.product(*dim_i_rangelist)
            for mem_index in dim_i_mem_indices:
                mem_index_s = '_'.join(list(map(str, mem_index)))
                shiftmemout[i][mem_index] = fx.FixedWire(m, self.name(
                    'shiftmemout' + mem_index_s), width, point, signed=signed)

        arg_data = [arg.sig_data for arg in self.args]

        #delayed_src = self._delayed(m, seq, arg_data[0])
        delayed_src = seq.Prev(arg_data[0], 1, cond=senable)
        shift_cond = arg_data[1]
        #delayed_shift_cond = _and_vars(svalid, senable, self._delayed(m, seq, arg_data[1]))
        delayed_shift_cond = _and_vars(svalid, senable,
                                       seq.Prev(arg_data[1], 1, cond=senable))

        if len(arg_data) == 2:
            delayed_rotate_conds = None
            delayed_enable = _and_vars(svalid, senable, delayed_shift_cond)
            enable = _and_vars(svalid, senable, arg_data[1])
            head_tail_enables = [enable] * (self.n_dim - 1)
        else:
            #delayed_rotate_conds = [self._delayed(m, seq, cond) for cond in arg_data[2:]]
            delayed_rotate_conds = [seq.Prev(cond, 1, cond=senable) for cond in arg_data[2:]]
            delayed_enable = _and_vars(svalid, senable,
                                       (vtypes.OrList(*([delayed_shift_cond] + delayed_rotate_conds))))
            enable = _and_vars(svalid, senable, (vtypes.OrList(*arg_data[1:])))
            head_tail_enables = [_and_vars(svalid, senable,
                                           (vtypes.OrList(*([shift_cond] + arg_data[2 + i - 1:]))))
                                 for i in range(1, self.n_dim)]

        def increment_index(index):
            # get incremented index accoring to shape
            incremented = list(index)
            c = True
            d = 1
            while c:
                if c is False:
                    break
                incremented[d] += 1
                c = False
                if incremented[d] == self.shape[d]:
                    c = True
                    incremented[d] = 0
                d += 1
            return tuple(incremented)

        # connect window registers input
        for index in window_indices:
            is_dim_edge = [i == dim - 1 for i, dim in zip(index, self.shape)]
            mine = self.windowreg[index]
            cond_data_pairs = []

            if is_dim_edge[0] is True:
                # shift input
                if all(is_dim_edge):
                    shift_mem_dim = self.n_dim
                    cond_data_pairs.append([delayed_shift_cond, delayed_src])
                else:
                    def find_first_false(x, i=0):
                        return i if x[0] is False else find_first_false(x[1:], i + 1)
                    first_false_index = find_first_false(is_dim_edge)
                    shift_mem_dim = first_false_index
                    shift_mem_index = increment_index(index)[shift_mem_dim:]
                    shift_data = shiftmemout[shift_mem_dim][shift_mem_index]
                    cond_data_pairs.append([delayed_shift_cond, shift_data])

                # rotate input
                if delayed_rotate_conds is not None:
                    for rotate_dim, rotate_cond in zip(range(1, self.n_dim), delayed_rotate_conds):
                        if shift_mem_dim >= rotate_dim:
                            rotate_mem_index = index[rotate_dim:]
                            rotate_data = shiftmemout[rotate_dim][rotate_mem_index]
                            cond_data_pairs.append([rotate_cond, rotate_data])
                        else:
                            # rotate input is same as shift input
                            cond = cond_data_pairs[0][0]
                            cond_data_pairs[0][0] = vtypes.Or(cond, rotate_cond)
                # create MUX
                newdata = cond_data_pairs[0][1]
                for cond, data in cond_data_pairs[1:]:
                    newdata = vtypes.Mux(cond, data, newdata)

            else:
                # input from previous window register
                prev_index = (index[0] + 1,) + index[1:]
                newdata = self.windowreg[prev_index]
            # assign window register input
            seq(mine(newdata), cond=delayed_enable)

        # head, tail
        heads = [None] * self.n_dim
        tails = [None] * self.n_dim
        for (dim, head_initval, tail_initval, memlen, head_tail_enable) in zip(
                range(1, self.n_dim), self.head_initvals, self.tail_initvals, self.memlens, head_tail_enables):
            heads[dim] = fx.FixedReg(m, self.name('head' + str(dim)),
                                     width, point, initval=head_initval, signed=signed)
            tails[dim] = fx.FixedReg(m, self.name('tail' + str(dim)),
                                     width, point, initval=tail_initval, signed=signed)
            next_head = vtypes.Mux(heads[dim] == memlen - 1, 0, heads[dim] + 1)
            next_tail = vtypes.Mux(tails[dim] == memlen - 1, 0, tails[dim] + 1)
            seq(heads[dim](next_head), cond=head_tail_enable)
            seq(tails[dim](next_tail), cond=head_tail_enable)

        raddrs = heads
        #waddrs = [self._delayed(m, seq, tail) for tail in tails]
        waddrs = [(seq.Prev(tail, 1, cond=senable) if tail is not None else tail)
                  for tail in tails]

        # connect shift memory
        for (mem_dim, raddr_data, waddr_data, memlen) in zip(
                range(1, self.n_dim), raddrs[1:], waddrs[1:], self.memlens):
            if delayed_rotate_conds is None:
                wenable = _and_vars(svalid, senable, delayed_shift_cond)
            else:
                wenable = _and_vars(svalid, senable,
                                    vtypes.OrList(*([delayed_shift_cond] + delayed_rotate_conds[mem_dim - 1:])))

            mem_indices = itertools.product(*[range(d) for d in self.shape[mem_dim:]])
            for mem_index in mem_indices:
                datawidth = self.get_width()
                addrwidth = int(ceil(log(memlen, 2)))
                num_ports = 2
                clk = m._clock
                shiftmem_name = 'shiftmem_' + '_'.join(list(map(str, mem_index)))
                shiftmem = ram.SyncRAM(m, self.name(shiftmem_name), clk,
                                       datawidth, addrwidth, num_ports)
                if mem_dim == 1:
                    window_index = (0, ) + mem_index
                    wdata_data = self.windowreg[window_index]
                else:
                    mem_input_index = (0, ) + mem_index
                    wdata_data = shiftmemout[mem_dim - 1][mem_input_index]
                wdata = m.Wire(self.name(shiftmem_name + '_wdata'), datawidth, signed=signed)
                wdata.assign(wdata_data)
                waddr = m.Wire(self.name(shiftmem_name + '_waddr'), addrwidth)
                waddr.assign(waddr_data)
                shiftmem.connect(0, waddr, wdata, wenable)
                rdata = m.Wire(self.name(shiftmem_name + '_rdata'), datawidth, signed=signed)
                raddr = m.Wire(self.name(shiftmem_name + '_raddr'), addrwidth)
                raddr.assign(raddr_data)
                shiftmem.connect(1, raddr, 0, 0)

                # connect shiftmemout wire
                shiftmemout[mem_dim][mem_index].assign(shiftmem.rdata(1))

        self.sig_data = delayed_src  # dummy output

    def get_window(self, index):
        return _LineBufferOut(self, index)


class Predicate(_SpecialOperator):
    latency = 1

    def __init__(self, data, when=None):

        self.when_index = 0

        args = [data]
        if when is not None:
            args.append(when)

        _SpecialOperator.__init__(self, *args)

        self.width = data.get_width()
        self.point = data.get_point()
        self.signed = data.get_signed()

        self.graph_label = 'Predicate'
        self.graph_shape = 'box'

    def _implement(self, m, seq, svalid=None, senable=None):
        if self.latency != 1:
            raise ValueError("Latency mismatch '%d' != '%s'" %
                             (self.latency, 1))

        width = self.get_width()
        point = self.get_point()
        signed = self.get_signed()

        arg_data = [arg.sig_data for arg in self.args]

        data = fx.FixedReg(m, self.name('data'), width, point, initval=0, signed=signed)
        self.sig_data = data

        when_cond = self.args[1].sig_data if len(self.args) == 2 else None
        enable = _and_vars(svalid, senable, when_cond)

        seq(data(arg_data[0]), cond=enable)


class Reg(Predicate):
    __intrinsics__ = ('write')

    def __init__(self, data, when=None):
        Predicate.__init__(self, data, when)
        self.graph_label = 'Reg'
        self.graph_shape = 'box'

    def write(self, fsm, value):
        cond = fsm.here

        self.seq.If(cond)(
            self.sig_data(value)
        )


class ReadRAM(_SpecialOperator):
    latency = 1

    def __init__(self, addr, when=None,
                 width=None, point=None, signed=True, ram_name=None):

        args = [addr]
        if when is not None:
            args.append(when)

        _SpecialOperator.__init__(self, *args)

        if width is not None:
            self.width = width

        if point is not None:
            self.point = point

        self.signed = signed

        self.graph_label = 'ReadRAM' if ram_name is None else ('ReadRAM\n%s' % ram_name)
        self.graph_shape = 'box'

    def _implement(self, m, seq, svalid=None, senable=None):
        if self.latency < 1:
            raise ValueError("Latency mismatch '%d' < '%s'" %
                             (self.latency, 1))

        datawidth = self.get_width()
        signed = self.get_signed()
        rdata = m.Wire(self.name('rdata'), datawidth, signed=signed)
        self.read_data = rdata

        when_cond = self.args[1].sig_data if len(self.args) == 2 else None
        enable_value = _and_vars(svalid, senable, when_cond)
        enable = m.Wire(self.name('enable'))
        enable.assign(enable_value)
        self.enable = enable

        if self.latency == 1:
            data = m.Wire(self.name('data'), datawidth, signed=signed)
            data.assign(rdata)
            self.sig_data = data

        elif self.latency == 2:
            data = m.Reg(self.name('data'), datawidth, initval=0, signed=signed)
            self.sig_data = data
            when_cond = self.args[2].sig_data if len(self.args) == 3 else None
            if when_cond is not None:
                when_cond = seq.Prev(when_cond, 1)
            enable = _and_vars(senable, when_cond)
            seq(data(rdata), cond=enable)

        else:
            prev_data = None

            when_cond_base = self.args[2].sig_data if len(self.args) == 3 else None

            for i in range(self.latency - 1):
                data = m.Reg(self.name('data_d%d' % i), datawidth,
                             initval=0, signed=signed)
                if when_cond_base is not None:
                    when_cond = seq.Prev(when_cond, i + 1)
                else:
                    when_cond = None
                enable = _and_vars(senable, when_cond)
                if i == 0:
                    seq(data(rdata), cond=enable)
                else:
                    seq(data(prev_data), cond=enable)
                prev_data = data

            self.sig_data = data

    @property
    def addr(self):
        return self.args[0].sig_data


class WriteRAM(_SpecialOperator):
    latency = 1

    def __init__(self, addr, data, when=None,
                 ram_name=None):

        args = [addr, data]
        if when is not None:
            args.append(when)

        _SpecialOperator.__init__(self, *args)

        self.width = 1
        self.point = 0
        self.signed = True

        self.output_tmp()

        self.graph_label = 'WriteRAM' if ram_name is None else ('WriteRAM\n%s' % ram_name)
        self.graph_shape = 'box'

    def _implement(self, m, seq, svalid=None, senable=None):
        if self.latency != 1:
            raise ValueError("Latency mismatch '%d' != '%s'" %
                             (self.latency, 1))

        when_cond = self.args[2].sig_data if len(self.args) == 3 else None
        enable_value = _and_vars(svalid, senable, when_cond)
        enable = m.Wire(self.name('enable'))
        enable.assign(enable_value)
        self.enable = enable

        self.sig_data = vtypes.Int(0)

    @property
    def addr(self):
        return self.args[0].sig_data

    @property
    def write_data(self):
        return self.args[1].sig_data


def ReduceArgMax(right, size=None, interval=None, initval=0,
                 enable=None, reset=None, width=32, signed=True):

    _max = ReduceMax(right, size, interval, initval,
                     enable, reset, width, signed)
    counter = Counter(size, dependency=right, enable=enable, reset=reset)
    update = NotEq(_max, _max.prev(1))
    update.latency = 0
    index = Predicate(counter, update)
    return index, _max


def ReduceArgMin(right, size=None, interval=None, initval=0,
                 enable=None, reset=None, width=32, signed=True):

    _min = ReduceMin(right, size, interval, initval,
                     enable, reset, width, signed)
    counter = Counter(size, dependency=right, enable=enable, reset=reset)
    update = NotEq(_min, reduce_min.prev(1))
    update.latency = 0
    index = Predicate(counter, update)
    return index, _min


def ReduceArgMaxValid(right, size=None, interval=None, initval=0,
                      enable=None, reset=None, width=32, signed=True):

    _max, valid = ReduceMaxValid(right, size, interval, initval,
                                 enable, reset, width, signed)
    counter = Counter(size, dependency=right, enable=enable, reset=reset)
    update = NotEq(_max, _max.prev(1))
    update.latency = 0
    index = Predicate(counter, update)
    return index, _max, valid


def ReduceArgMinValid(right, size=None, interval=None, initval=0,
                      enable=None, reset=None, width=32, signed=True):

    _min, valid = ReduceMinValid(right, size, interval, initval,
                                 enable, reset, width, signed)
    counter = Counter(size, dependency=right, enable=enable, reset=reset)
    update = NotEq(_min, _min.prev(1))
    update.latency = 0
    index = Predicate(counter, update)
    return index, _min, valid


def make_condition(*cond, **kwargs):
    ready = kwargs['ready'] if 'ready' in kwargs else None

    _cond = []
    for c in cond:
        if isinstance(c, (tuple, list)):
            _cond.extend(c)
        else:
            _cond.append(c)

    cond = _cond

    new_cond = []
    for c in cond:
        if c is None:
            continue
        if isinstance(c, _Numeric):
            d, v = c.read(cond=ready)
            new_cond.append(d)
            new_cond.append(v)
        else:
            new_cond.append(c)

    return _make_condition(*new_cond)


def is_stream_object(*objs):
    for obj in objs:
        if isinstance(obj, _Node):
            return True
    return False


def _to_constant(obj):
    if isinstance(obj, (int, float, bool, str)):
        return Constant(obj)
    if isinstance(obj, vtypes._Numeric):
        return _from_vtypes_value(obj)
    return obj


def _get_strm(*vars):
    ret = None
    for var in vars:
        v = getattr(var, 'strm', None)
        if v is None:
            continue
        if ret is None:
            ret = v
            continue
        if v.object_id < ret.object_id:
            if v.module != ret.module:
                raise ValueError("Different modules")
            if id(v.clock) != id(ret.clock):
                raise ValueError("Different clock domains: '%s' and '%s'" %
                                 (str(v.clock), str(ret.clock)))
            if id(v.reset) != id(ret.reset):
                raise ValueError("Different reset domains: '%s' and '%s'" %
                                 (str(v.reset), str(ret.reset)))
            ret = v
    return ret


def _max(*vars):
    m = None
    for v in vars:
        if v is None:
            continue
        if m is None:
            m = v
            continue
        if m < v:
            m = v
    return m


def _and_vars(*vars):
    ret = None
    for var in vars:
        if var is None:
            continue
        if ret is None:
            ret = var
        else:
            ret = vtypes.AndList(ret, var)
    return ret


def _from_vtypes_value(value):
    if isinstance(value, vtypes.Int):
        if not isinstance(value.value, int):
            raise TypeError("Unsupported type for Constant '%s'" %
                            str(type(value)))
        return Int(value.value)

    if isinstance(value, vtypes.Float):
        return Float(value.value)

    if isinstance(value, vtypes.Str):
        return Str(value.value)

    if isinstance(value, vtypes._Numeric):
        return ParameterVariable(value)

    raise TypeError("Unsupported type '%s'" % str(type(value)))
