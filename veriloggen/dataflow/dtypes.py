from __future__ import absolute_import
from __future__ import print_function

from functools import partial
from collections import OrderedDict
from math import log

import veriloggen.core.vtypes as vtypes
import veriloggen.types.fixed as fx
import veriloggen.types.rom as rom
from veriloggen.seq.seq import make_condition as _make_condition

from . import mul
from . import div


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


def Variable(data=None, valid=None, ready=None, width=32, point=0, signed=True):
    return _Variable(data, valid, ready, width, point, signed)


def Parameter(name, value, width=32, point=0, signed=True):
    """ parameter with an immediate value """
    if not isinstance(name, str):
        raise TypeError("'name' must be str, not '%s'" % str(type(name)))
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

    def __hash__(self):
        object_id = self.object_id if hasattr(self, 'object_id') else None
        return hash((id(self), object_id))

    def __eq__(self, other):
        return (id(self), self.object_id) == (id(other), other.object_id)

    def name(self, prefix=None):
        clsname = self.__class__.__name__.lower()
        if prefix is None:
            prefix = 'tmp'
        return '_'.join(['_dataflow', clsname, prefix, str(self.object_id)])


class _Numeric(_Node):
    latency = 0

    def __hash__(self):
        object_id = self.object_id if hasattr(self, 'object_id') else None
        return hash((id(self), object_id))

    def __init__(self):
        _Node.__init__(self)

        # set up by _set_managers()
        self.m = None
        self.df = None
        self.seq = None

        self.output_data = None
        self.output_valid = None
        self.output_ready = None

        self.output_sig_data = None
        self.output_sig_valid = None
        self.output_sig_ready = None

        self.output_node = None

        self.sig_data = None
        self.sig_valid = None
        self.sig_ready = None

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

    def output(self, data, valid=None, ready=None):
        if self.output_data is not None:
            raise ValueError('output_data is already assigned.')
        self.output_data = data
        self.output_valid = valid
        self.output_ready = ready

        if self.df is not None:
            self.df.add(self)

    def output_tmp(self):
        if self.m is None:
            raise ValueError("Module information is not set.")

        self.output(self.name('odata'),
                    self.name('ovalid'), self.name('oready'))

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

    def read(self, cond=None):
        if self.output_node is not None and id(self) != id(self.output_node):
            return self.output_node.read(cond)

        if self.output_sig_data is None:

            # set default name
            if self.output_data is None:
                self.output_tmp()

            self._implement_output_sig(self.m, self.seq, aswire=True)

        data = self.output_sig_data
        valid = self.output_sig_valid

        if valid is None:
            valid = 1

        ready = make_condition(cond)
        val = 1 if ready is None else ready

        if ready is not None and self.output_sig_ready is None:
            raise ValueError("Dataflow ready port is required for throttling.")

        if self.output_sig_ready is not None:
            prev_assign = self.output_sig_ready._get_assign()
            if not prev_assign:
                self.output_sig_ready.assign(val)
            else:
                prev_assign.overwrite_right(
                    vtypes.OrList(prev_assign.statement.right, val))
                m = self.output_sig_ready._get_module()
                m.remove(prev_assign)
                m.append(prev_assign)

        if ready is not None:
            ack = vtypes.AndList(valid, ready)
        else:
            ack = valid

        rdata = data
        rvalid = ack

        return rdata, rvalid

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

    def _set_df(self, df):
        self.df = df

    def _set_seq(self, seq):
        self.seq = seq

    def _implement(self, m, seq):
        raise NotImplementedError('_implement() is not implemented.')

    def _implement_input(self, m, seq, aswire=False):
        raise NotImplementedError('_implement_input() is not implemented.')

    def _implement_output(self, m, seq, aswire=False):
        if self.end_stage is None:
            self.end_stage = 0

        self._implement_output_sig(m, seq, aswire)
        data = self.output_sig_data
        valid = self.output_sig_valid
        ready = self.output_sig_ready

        if len(data.subst) == 0:
            m.Assign(data(self.sig_data))

        if self.output_valid is not None and len(valid.subst) == 0:
            m.Assign(valid(self.sig_valid))

        if self.output_ready is not None:
            _connect_ready(m, self.sig_ready, ready)
        elif self.sig_ready is not None:
            _connect_ready(m, self.sig_ready, 1)

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

        if isinstance(self.output_valid, (vtypes.Wire, vtypes.Output)):
            valid = self.output_valid
            self.output_sig_valid = valid
        elif self.output_valid is not None:
            valid = type_o(self.output_valid)
            self.output_sig_valid = valid

        if isinstance(self.output_ready, (vtypes._Numeric, int, bool)):
            ready = self.output_ready
            self.output_sig_ready = ready
        elif self.output_ready is not None:
            ready = type_i(self.output_ready)
            self.output_sig_ready = ready

    def _has_output(self):
        if self.output_data is not None:
            return True
        return False

    def _disable_output(self):
        self.output_data = None
        self.output_valid = None
        self.output_ready = None

    def _disable_output_sig(self):
        self.output_sig_data = None
        self.output_sig_valid = None
        self.output_sig_ready = None

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

    def __floordiv__(self, r):
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

    def __invert__(self):
        return Unot(self)

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
                "Dataflow is not synthesized yet. Run Dataflow.implement().")
        return self.sig_data

    @property
    def raw_valid(self):
        if self.sig_data is None:
            raise ValueError(
                "Dataflow is not synthesized yet. Run Dataflow.implement().")
        if self.sig_valid is None:
            return 1
        return self.sig_valid

    @property
    def raw_ready(self):
        if self.sig_data is None:
            raise ValueError(
                "Dataflow is not synthesized yet. Run Dataflow.implement().")
        return self.sig_ready

    @property
    def data(self):
        if self.output_node is not None:
            return self.output_node.output_sig_data
        return self.raw_data

    @property
    def valid(self):
        if self.output_node is not None:
            return self.output_node.output_sig_valid
        return self.raw_valid

    @property
    def ready(self):
        if self.output_node is not None:
            return self.output_node.output_sig_ready
        return self.raw_ready


class _Operator(_Numeric):
    latency = 1

    def _implement(self, m, seq):
        raise NotImplementedError('_implement() is not implemented.')


class _BinaryOperator(_Operator):

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
        self._set_df(_get_df(self.left, self.right))
        self._set_module(getattr(self.df, 'module', None))
        self._set_seq(getattr(self.df, 'seq', None))

    def _implement(self, m, seq):
        if self.latency != 1:
            raise ValueError("Latency mismatch '%d' vs '%s'" %
                             (self.latency, 1))

        width = self.get_width()
        signed = self.get_signed()

        data = m.Reg(self.name('data'), width, initval=0, signed=signed)
        valid = m.Reg(self.name('valid'), initval=0)
        ready = m.Wire(self.name('ready'))
        self.sig_data = data
        self.sig_valid = valid
        self.sig_ready = ready

        lpoint = self.left.get_point()
        rpoint = self.right.get_point()

        ldata, rdata = fx.adjust(
            self.left.sig_data, self.right.sig_data, lpoint, rpoint, signed)

        lvalid = self.left.sig_valid
        rvalid = self.right.sig_valid

        lready = self.left.sig_ready
        rready = self.right.sig_ready

        all_valid = _and_vars(lvalid, rvalid)
        all_ready = _and_vars(lready, rready)

        accept = vtypes.OrList(ready, vtypes.Not(valid))

        valid_cond = _and_vars(accept, all_ready)
        valid_reset_cond = _and_vars(valid, ready)
        data_cond = _and_vars(valid_cond, all_valid)
        ready_cond = _and_vars(accept, all_valid)

        seq(data(self.op(ldata, rdata)), cond=data_cond)
        seq(valid(0), cond=valid_reset_cond)
        seq(valid(all_valid), cond=valid_cond)
        _connect_ready(m, lready, ready_cond)
        _connect_ready(m, rready, ready_cond)

        if not self._has_output():
            _connect_ready(m, ready, vtypes.Int(1))


class _UnaryOperator(_Operator):

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
        self._set_df(_get_df(self.right))
        self._set_module(getattr(self.df, 'module', None))
        self._set_seq(getattr(self.df, 'seq', None))

    def _implement(self, m, seq):
        if self.latency != 1:
            raise ValueError("Latency mismatch '%d' vs '%s'" %
                             (self.latency, 1))

        width = self.get_width()
        signed = self.get_signed()

        data = m.Reg(self.name('data'), width, initval=0, signed=signed)
        valid = m.Reg(self.name('valid'), initval=0)
        ready = m.Wire(self.name('ready'))
        self.sig_data = data
        self.sig_valid = valid
        self.sig_ready = ready

        rdata = self.right.sig_data

        rvalid = self.right.sig_valid

        rready = self.right.sig_ready

        all_valid = _and_vars(rvalid)
        all_ready = _and_vars(rready)

        accept = vtypes.OrList(ready, vtypes.Not(valid))

        valid_cond = _and_vars(accept, all_ready)
        valid_reset_cond = _and_vars(valid, ready)
        data_cond = _and_vars(valid_cond, all_valid)
        ready_cond = _and_vars(accept, all_valid)

        seq(data(self.op(rdata)), cond=data_cond)
        seq(valid(0), cond=valid_reset_cond)
        seq(valid(all_valid), cond=valid_cond)
        _connect_ready(m, rready, ready_cond)

        if not self._has_output():
            _connect_ready(m, ready, vtypes.Int(1))


class Power(_BinaryOperator):
    latency = 0

    def eval(self):
        return self.left.eval() ** self.right.eval()

    def _implement(self, m, seq):
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
        self.point = max(left_fp, right_fp)
        self.signed = self.left.get_signed() and self.right.get_signed()

    def _implement(self, m, seq):
        if self.latency < 3:
            raise ValueError("Latency of '*' operator must be greater than 2")

        width = self.get_width()
        signed = self.get_signed()

        data = m.Wire(self.name('data'), width, signed=signed)
        valid = m.Wire(self.name('valid'))
        ready = m.Wire(self.name('ready'))
        self.sig_data = data
        self.sig_valid = valid
        self.sig_ready = ready

        lwidth = self.left.get_width()
        rwidth = self.right.get_width()

        lpoint = self.left.get_point()
        rpoint = self.right.get_point()

        lsigned = self.left.get_signed()
        rsigned = self.right.get_signed()

        ldata = self.left.sig_data
        rdata = self.right.sig_data

        accept = vtypes.OrList(ready, vtypes.Not(valid))

        odata = m.Wire(self.name('mul_odata'),
                       lwidth + rwidth, signed=signed)
        odata_reg = m.Reg(self.name('mul_odata_reg'), lwidth + rwidth,
                          signed=signed, initval=0)

        shift_size = min(lpoint, rpoint)
        if shift_size > 0:
            seq(odata_reg(fx.shift_right(odata, shift_size, signed=signed)), cond=accept)
        else:
            seq(odata_reg(odata), cond=accept)

        m.Assign(data(odata_reg))

        ovalid = m.Wire(self.name('mul_ovalid'))
        valid_reg = m.Reg(self.name('mul_valid_reg'), initval=0)

        seq(valid_reg(ovalid), cond=accept)
        m.Assign(valid(valid_reg))

        lvalid = self.left.sig_valid
        rvalid = self.right.sig_valid

        lready = self.left.sig_ready
        rready = self.right.sig_ready

        all_valid = _and_vars(lvalid, rvalid)
        all_ready = _and_vars(lready, rready)

        valid_cond = _and_vars(accept, all_ready)
        valid_reset_cond = _and_vars(valid, ready)
        data_cond = _and_vars(valid_cond, all_valid)
        ready_cond = _and_vars(accept, all_valid)

        depth = self.latency - 1

        inst = mul.get_mul(lwidth, rwidth, lsigned, rsigned, depth)
        clk = m._clock
        rst = m._reset

        enable = m.Wire(self.name('mul_enable'))
        update = m.Wire(self.name('mul_update'))

        m.Assign(enable(data_cond))
        m.Assign(update(accept))  # NOT valid_cond

        ports = [('CLK', clk), ('RST', rst),
                 ('update', update), ('enable', enable), ('valid', ovalid),
                 ('a', ldata), ('b', rdata), ('c', odata)]

        m.Instance(inst, self.name('mul'), ports=ports)

        _connect_ready(m, lready, ready_cond)
        _connect_ready(m, rready, ready_cond)

        if not self._has_output():
            _connect_ready(m, ready, vtypes.Int(1))


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

    def _implement(self, m, seq):
        if self.latency <= 5:
            raise ValueError("Latency of div operator must be greater than 5")

        width = self.get_width()
        signed = self.get_signed()

        data = m.Wire(self.name('data'), width, signed=signed)
        valid = m.Wire(self.name('valid'))
        ready = m.Wire(self.name('ready'))
        self.sig_data = data
        self.sig_valid = valid
        self.sig_ready = ready

        lpoint = self.left.get_point()
        rpoint = self.right.get_point()

        lsigned = self.left.get_signed()
        rsigned = self.right.get_signed()

        ldata = m.Reg(self.name('div_ldata'),
                      width, signed=lsigned, initval=0)
        rdata = m.Reg(self.name('div_rdata'),
                      width, signed=rsigned, initval=0)

        point = max(lpoint, rpoint)

        if lpoint <= rpoint:
            lval, rval = fx.adjust(
                self.left.sig_data, self.right.sig_data, lpoint, rpoint, signed)
            shift_size = point
        else:
            lval = self.left.sig_data
            rval = self.right.sig_data
            shift_size = point - (lpoint - rpoint)

        accept = vtypes.OrList(ready, vtypes.Not(valid))

        seq(ldata(lval), cond=accept)
        seq(rdata(rval), cond=accept)

        sign = vtypes.Not(vtypes.OrList(vtypes.AndList(ldata[width - 1] == 0, rdata[width - 1] == 0),  # + , +
                                        vtypes.AndList(ldata[width - 1] == 1, rdata[width - 1] == 1)))  # - , -

        abs_ldata = m.Reg(
            self.name('div_abs_ldata'), width, initval=0)
        abs_rdata = m.Reg(
            self.name('div_abs_rdata'), width, initval=0)

        if not lsigned:
            seq(abs_ldata(ldata), cond=accept)
        else:
            seq(abs_ldata(vtypes.Mux(ldata[width - 1] == 0, ldata, vtypes.Unot(ldata) + 1)),
                cond=accept)

        if not rsigned:
            seq(abs_rdata(rdata), cond=accept)
        else:
            seq(abs_rdata(vtypes.Mux(rdata[width - 1] == 0, rdata, vtypes.Unot(rdata) + 1)),
                cond=accept)

        osign = m.Wire(self.name('div_osign'))
        abs_odata = m.Wire(
            self.name('div_abs_odata'), width, signed=signed)

        if shift_size > 0:
            shifted_abs_odata = vtypes.Sll(abs_odata, shift_size)
        else:
            shifted_abs_odata = abs_odata

        odata = m.Reg(self.name('div_odata'),
                      width, signed=signed, initval=0)

        if not signed:
            seq(odata(shifted_abs_odata), cond=accept)
        else:
            seq(odata(vtypes.Mux(osign == 0, shifted_abs_odata, vtypes.Unot(shifted_abs_odata) + 1)),
                cond=accept)

        m.Assign(data(odata))

        ovalid = m.Wire(self.name('div_ovalid'))

        v = ovalid
        for i in range(3):
            nv = m.Reg(self.name('div_valid_reg_tmp_%d' % i), initval=0)
            seq(nv(v), cond=accept)
            v = nv
        m.Assign(valid(v))

        s = sign
        for i in range(self.latency - 2):
            ns = m.Reg(self.name('div_sign_tmp_%d' % i), initval=0)
            seq(ns(s), cond=accept)
            s = ns
        m.Assign(osign(s))

        lvalid = self.left.sig_valid
        rvalid = self.right.sig_valid

        lready = self.left.sig_ready
        rready = self.right.sig_ready

        all_valid = _and_vars(lvalid, rvalid)
        all_ready = _and_vars(lready, rready)

        valid_cond = _and_vars(accept, all_ready)
        valid_reset_cond = _and_vars(valid, ready)
        data_cond = _and_vars(valid_cond, all_valid)
        ready_cond = _and_vars(accept, all_valid)

        inst = div.get_div()
        clk = m._clock
        rst = m._reset

        enable = m.Wire(self.name('div_enable'))
        update = m.Wire(self.name('div_update'))
        m.Assign(enable(data_cond))
        m.Assign(update(accept))  # NOT valid_cond

        params = [('W_D', width)]
        ports = [('CLK', clk), ('RST', rst),
                 ('update', update), ('enable', enable), ('valid', ovalid),
                 ('in_a', abs_ldata), ('in_b', abs_rdata), ('rslt', abs_odata)]

        m.Instance(inst, self.name('div'), params, ports)

        _connect_ready(m, lready, ready_cond)
        _connect_ready(m, rready, ready_cond)

        if not self._has_output():
            _connect_ready(m, ready, vtypes.Int(1))


class Mod(_BinaryOperator):
    latency = 32 + 5
    variable_latency = 'get_latency'

    def get_latency(self):
        return self.get_width() + 5

    def eval(self):
        return self.left.eval() % self.right.eval()

    def _implement(self, m, seq):
        if self.latency <= 5:
            raise ValueError("Latency of div operator must be greater than 5")

        width = self.get_width()
        signed = self.get_signed()

        data = m.Wire(self.name('data'), width, signed=signed)
        valid = m.Wire(self.name('valid'))
        ready = m.Wire(self.name('ready'))
        self.sig_data = data
        self.sig_valid = valid
        self.sig_ready = ready

        lpoint = self.left.get_point()
        rpoint = self.right.get_point()

        lsigned = self.left.get_signed()
        rsigned = self.right.get_signed()

        ldata = m.Reg(self.name('mod_ldata'),
                      width, signed=lsigned, initval=0)
        rdata = m.Reg(self.name('mod_rdata'),
                      width, signed=rsigned, initval=0)

        point = max(lpoint, rpoint)

        if lpoint <= rpoint:
            lval, rval = fx.adjust(
                self.left.sig_data, self.right.sig_data, lpoint, rpoint, signed)
            shift_size = point
        else:
            lval = self.left.sig_data
            rval = self.right.sig_data
            shift_size = point - (lpoint - rpoint)

        accept = vtypes.OrList(ready, vtypes.Not(valid))

        seq(ldata(lval), cond=accept)
        seq(rdata(rval), cond=accept)

        sign = vtypes.Not(vtypes.OrList(vtypes.AndList(ldata[width - 1] == 0, rdata[width - 1] == 0),  # + , +
                                        vtypes.AndList(ldata[width - 1] == 1, rdata[width - 1] == 1)))  # - , -

        abs_ldata = m.Reg(
            self.name('mod_abs_ldata'), width, initval=0)
        abs_rdata = m.Reg(
            self.name('mod_abs_rdata'), width, initval=0)

        if not lsigned:
            seq(abs_ldata(ldata), cond=accept)
        else:
            seq(abs_ldata(vtypes.Mux(ldata[width - 1] == 0, ldata, vtypes.Unot(ldata) + 1)),
                cond=accept)

        if not rsigned:
            seq(abs_rdata(rdata), cond=accept)
        else:
            seq(abs_rdata(vtypes.Mux(rdata[width - 1] == 0, rdata, vtypes.Unot(rdata) + 1)),
                cond=accept)

        osign = m.Wire(self.name('mod_osign'))
        abs_odata = m.Wire(
            self.name('mod_abs_odata'), width, signed=signed)

        if shift_size > 0:
            shifted_abs_odata = vtypes.Sll(abs_odata, shift_size)
        else:
            shifted_abs_odata = abs_odata

        odata = m.Reg(self.name('mod_odata'),
                      width, signed=signed, initval=0)

        if not signed:
            seq(odata(shifted_abs_odata), cond=accept)
        else:
            seq(odata(vtypes.Mux(osign == 0, shifted_abs_odata, vtypes.Unot(shifted_abs_odata) + 1)),
                cond=accept)

        m.Assign(data(odata))

        ovalid = m.Wire(self.name('mod_ovalid'))

        v = ovalid
        for i in range(3):
            nv = m.Reg(self.name('mod_valid_reg_tmp_%d' % i), initval=0)

            seq(nv(v), cond=accept)
            v = nv
        m.Assign(valid(v))

        s = sign
        for i in range(self.latency - 2):
            ns = m.Reg(self.name('mod_sign_tmp_%d' % i), initval=0)
            seq(ns(s), cond=accept)
            s = ns
        m.Assign(osign(s))

        lvalid = self.left.sig_valid
        rvalid = self.right.sig_valid

        lready = self.left.sig_ready
        rready = self.right.sig_ready

        all_valid = _and_vars(lvalid, rvalid)
        all_ready = _and_vars(lready, rready)

        valid_cond = _and_vars(accept, all_ready)
        valid_reset_cond = _and_vars(valid, ready)
        data_cond = _and_vars(valid_cond, all_valid)
        ready_cond = _and_vars(accept, all_valid)

        inst = div.get_div()
        clk = m._clock
        rst = m._reset

        enable = m.Wire(self.name('mod_enable'))
        update = m.Wire(self.name('mod_update'))
        m.Assign(enable(data_cond))
        m.Assign(update(accept))  # NOT valid_cond

        params = [('W_D', width)]
        ports = [('CLK', clk), ('RST', rst),
                 ('update', update), ('enable', enable), ('valid', ovalid),
                 ('in_a', abs_ldata), ('in_b', abs_rdata), ('mod', abs_odata)]

        m.Instance(inst, self.name('div'), params, ports)

        _connect_ready(m, lready, ready_cond)
        _connect_ready(m, rready, ready_cond)

        if not self._has_output():
            _connect_ready(m, ready, vtypes.Int(1))


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

    def _implement(self, m, seq):
        if self.right.get_point() != 0:
            raise TypeError("shift amount must be int")

        if self.latency != 1:
            raise ValueError("Latency mismatch '%d' vs '%s'" %
                             (self.latency, 1))

        width = self.get_width()
        signed = self.get_signed()

        data = m.Reg(self.name('data'), width, initval=0, signed=signed)
        valid = m.Reg(self.name('valid'), initval=0)
        ready = m.Wire(self.name('ready'))
        self.sig_data = data
        self.sig_valid = valid
        self.sig_ready = ready

        lpoint = self.left.get_point()
        rpoint = self.right.get_point()

        ldata, rdata = self.left.sig_data, self.right.sig_data

        lvalid = self.left.sig_valid
        rvalid = self.right.sig_valid

        lready = self.left.sig_ready
        rready = self.right.sig_ready

        all_valid = _and_vars(lvalid, rvalid)
        all_ready = _and_vars(lready, rready)

        accept = vtypes.OrList(ready, vtypes.Not(valid))

        valid_cond = _and_vars(accept, all_ready)
        valid_reset_cond = _and_vars(valid, ready)
        data_cond = _and_vars(valid_cond, all_valid)
        ready_cond = _and_vars(accept, all_valid)

        seq(data(self.op(ldata, rdata)), cond=data_cond)
        seq(valid(0), cond=valid_reset_cond)
        seq(valid(all_valid), cond=valid_cond)
        _connect_ready(m, lready, ready_cond)
        _connect_ready(m, rready, ready_cond)

        if not self._has_output():
            _connect_ready(m, ready, vtypes.Int(1))


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
        left_fp = self.left.get_point()
        self.point = left_fp
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

    def _implement(self, m, seq):
        if self.latency != 1:
            raise ValueError("Latency mismatch '%d' vs '%s'" %
                             (self.latency, 1))

        width = self.get_width()
        signed = False

        data = m.Reg(self.name('data'), width, initval=0, signed=signed)
        valid = m.Reg(self.name('valid'), initval=0)
        ready = m.Wire(self.name('ready'))
        self.sig_data = data
        self.sig_valid = valid
        self.sig_ready = ready

        ldata = self.left.sig_data
        rdata = self.right.sig_data

        lvalid = self.left.sig_valid
        rvalid = self.right.sig_valid

        lready = self.left.sig_ready
        rready = self.right.sig_ready

        all_valid = _and_vars(lvalid, rvalid)
        all_ready = _and_vars(lready, rready)

        accept = vtypes.OrList(ready, vtypes.Not(valid))

        valid_cond = _and_vars(accept, all_ready)
        valid_reset_cond = _and_vars(valid, ready)
        data_cond = _and_vars(valid_cond, all_valid)
        ready_cond = _and_vars(accept, all_valid)

        seq(data(self.op(ldata, rdata)), cond=data_cond)
        seq(valid(0), cond=valid_reset_cond)
        seq(valid(all_valid), cond=valid_cond)
        _connect_ready(m, lready, ready_cond)
        _connect_ready(m, rready, ready_cond)

        if not self._has_output():
            _connect_ready(m, ready, vtypes.Int(1))


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
        return ~ self.right.eval()


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

    def _set_attributes(self):
        wargs = [arg.get_width() for arg in self.args]
        self.width = max(*wargs)
        pargs = [arg.get_point() for arg in self.args]
        self.point = max(*pargs)
        self.signed = False
        for arg in self.args:
            if arg.get_signed():
                self.signed = True
                break

    def _set_managers(self):
        self._set_df(_get_df(*self.args))
        self._set_module(getattr(self.df, 'module', None))
        self._set_seq(getattr(self.df, 'seq', None))

    def _implement(self, m, seq):
        if self.latency != 1:
            raise ValueError("Latency mismatch '%d' vs '%s'" %
                             (self.latency, 1))

        width = self.get_width()
        signed = self.get_signed()

        data = m.Reg(self.name('data'), width, initval=0, signed=signed)
        valid = m.Reg(self.name('valid'), initval=0)
        ready = m.Wire(self.name('ready'))
        self.sig_data = data
        self.sig_valid = valid
        self.sig_ready = ready

        arg_data = [arg.sig_data for arg in self.args]
        arg_valid = [arg.sig_valid for arg in self.args]
        arg_ready = [arg.sig_ready for arg in self.args]

        all_valid = _and_vars(*arg_valid)
        all_ready = _and_vars(*arg_ready)

        accept = vtypes.OrList(ready, vtypes.Not(valid))

        valid_cond = _and_vars(accept, all_ready)
        valid_reset_cond = _and_vars(valid, ready)
        data_cond = _and_vars(valid_cond, all_valid)
        ready_cond = _and_vars(accept, all_valid)

        seq(data(self.op(*arg_data)), cond=data_cond)
        seq(valid(0), cond=valid_reset_cond)
        seq(valid(all_valid), cond=valid_cond)

        for r in arg_ready:
            _connect_ready(m, r, ready_cond)

        if not self._has_output():
            _connect_ready(m, ready, vtypes.Int(1))


class Pointer(_SpecialOperator):

    def __init__(self, var, pos):
        _SpecialOperator.__init__(self, var, pos)
        self.op = vtypes.Pointer

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


class Cat(_SpecialOperator):

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


def Abs(value):
    if isinstance(value, (bool, int, float, str, list, tuple)):
        return abs(value)

    signed = value.get_signed()
    if not signed:
        return value

    return Mux(value < Constant(0), Uminus(value), value)


def Sign(value):
    if isinstance(value, (bool, int, float, str, list, tuple)):
        return value >= 0

    signed = value.get_signed()
    if not signed:
        return 1

    return value >= Constant(0)


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

    def _set_attributes(self):
        pass

    @property
    def address(self):
        return self.args[0]

    @address.setter
    def address(self, address):
        self.args[0] = address

    def _implement(self, m, seq):
        if self.latency != 1:
            raise ValueError("Latency mismatch '%d' vs '%s'" %
                             (self.latency, 1))

        width = self.get_width()
        signed = self.get_signed()

        data = m.Wire(self.name('data'), width, signed=signed)
        valid = m.Reg(self.name('valid'), initval=0)
        ready = m.Wire(self.name('ready'))
        self.sig_data = data
        self.sig_valid = valid
        self.sig_ready = ready

        arg_data = self.address.sig_data

        arg_valid = self.address.sig_valid

        arg_ready = self.address.sig_ready

        all_valid = _and_vars(arg_valid)
        all_ready = _and_vars(arg_ready)

        accept = vtypes.OrList(ready, vtypes.Not(valid))

        valid_cond = _and_vars(accept, all_ready)
        valid_reset_cond = _and_vars(valid, ready)
        data_cond = _and_vars(valid_cond, all_valid)
        ready_cond = _and_vars(accept, all_valid)

        size = int(log(len(self.patterns), 2))

        inst = rom.mkROMDefinition(self.name('LUT_ROM'), self.patterns,
                                   size, width, sync=True, with_enable=True)

        address = m.Wire(self.name('lut_address'), width=size)
        address.assign(arg_data)

        clk = m._clock

        ports = [('CLK', clk), ('addr', address),
                 ('enable', data_cond), ('val', data)]

        m.Instance(inst, self.name('lut'), ports=ports)

        seq(valid(0), cond=valid_reset_cond)
        seq(valid(all_valid), cond=valid_cond)

        _connect_ready(m, arg_ready, ready_cond)

        if not self._has_output():
            _connect_ready(m, ready, vtypes.Int(1))


class _Delay(_UnaryOperator):

    def __init__(self, right):
        _UnaryOperator.__init__(self, right)
        # parent value for delayed_value and previous_value
        self.parent_value = None

    def _set_parent_value(self, value):
        self.parent_value = value

    def _get_parent_value(self):
        return self.parent_value

    def eval(self):
        return self

    def _implement(self, m, seq):
        if self.latency != 1:
            raise ValueError("Latency mismatch '%d' vs '%s'" %
                             (self.latency, 1))

        width = self.get_width()
        signed = self.get_signed()

        data = m.Reg(self.name('data'), width, initval=0, signed=signed)
        valid = m.Reg(self.name('valid'), initval=0)
        ready = m.Wire(self.name('ready'))
        self.sig_data = data
        self.sig_valid = valid
        self.sig_ready = ready

        rdata = self.right.sig_data

        rvalid = self.right.sig_valid

        rready = self.right.sig_ready

        all_valid = _and_vars(rvalid)
        all_ready = _and_vars(rready)

        accept = vtypes.OrList(ready, vtypes.Not(valid))

        valid_cond = _and_vars(accept, all_ready)
        valid_reset_cond = _and_vars(valid, ready)
        data_cond = _and_vars(valid_cond, all_valid)
        ready_cond = _and_vars(accept, all_valid)

        seq(data(rdata), cond=data_cond)
        seq(valid(0), cond=valid_reset_cond)
        seq(valid(all_valid), cond=valid_cond)
        _connect_ready(m, rready, ready_cond)

        if not self._has_output():
            _connect_ready(m, ready, vtypes.Int(1))


class _Prev(_UnaryOperator):
    latency = 0

    def __init__(self, right):
        _UnaryOperator.__init__(self, right)
        # parent value for delayed_value and previous_value
        self.parent_value = None

    def _set_parent_value(self, value):
        self.parent_value = value

    def _get_parent_value(self):
        return self.parent_value

    def eval(self):
        return self

    def _implement(self, m, seq):
        if self.latency != 0:
            raise ValueError("Latency mismatch '%d' vs '%s'" %
                             (self.latency, 0))

        width = self.get_width()
        signed = self.get_signed()

        data = m.Reg(self.name('data'), width, initval=0, signed=signed)
        valid = self.parent_value.sig_valid
        ready = self.parent_value.sig_ready
        self.sig_data = data
        self.sig_valid = valid
        self.sig_ready = ready

        rdata = self.right.sig_data

        data_cond = _and_vars(valid, ready)

        seq(data(rdata), cond=data_cond)


class _Constant(_Numeric):

    def __init__(self, value):
        _Numeric.__init__(self)
        self.value = value
        self.signed = False
        self._set_attributes()
        self._set_managers()
        self.sig_data = self.value

    def _set_attributes(self):
        self.width = vtypes.get_width(self.value)
        self.point = 0
        self.signed = False

    def _set_managers(self):
        self._set_df(_get_df(self.value))
        self._set_module(getattr(self.df, 'module', None))
        self._set_seq(getattr(self.df, 'seq', None))

    def eval(self):
        return self.value

    def _implement(self, m, seq):
        data = self.value
        valid = None
        ready = None
        self.sig_data = data
        self.sig_valid = valid
        self.sig_ready = ready


class _Variable(_Numeric):

    def __init__(self, data=None, valid=None, ready=None, width=32, point=0, signed=True):
        _Numeric.__init__(self)
        self.input_data = data
        self.input_valid = valid
        self.input_ready = ready
        if isinstance(self.input_data, _Numeric):
            self.input_data._add_sink(self)
        self.width = width
        self.point = point
        self.signed = signed

    def eval(self):
        return self

    def output(self, data, valid=None, ready=None):
        if isinstance(self.input_data, _Numeric):
            self.input_data.output(data, valid, ready)
            return
        _Numeric.output(self, data, valid, ready)

    def connect(self, data, valid=None, ready=None):
        if self.sig_data is not None:
            raise ValueError("Input signals are already synthesized.")

        if not isinstance(data, (_Numeric, vtypes._Numeric, int, bool)):
            raise TypeError(
                "'data' must be dtypes._Numeric or vtypes._Numeric.")
        if valid is not None and not isinstance(valid, (vtypes._Numeric, int, bool)):
            raise TypeError(
                "'valid' must be None, vtypes._Numeric, int, or bool.")
        if ready is not None and not isinstance(ready, vtypes._Numeric):
            raise TypeError("'ready' must be None or vtypes._Numeric.")

        self.input_data = data
        self.input_valid = valid
        self.input_ready = ready
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
            if hasattr(self, 'sig_data_write'):
                data = self.sig_data_write
            else:
                data = self.m.TmpReg(self.get_width(), initval=0,
                                     signed=self.get_signed())
                self.sig_data_write = data
                self.sig_data.assign(data)
        else:
            data = self.sig_data

        if self.sig_valid is None:
            valid = 1
        elif isinstance(self.sig_valid, vtypes.Wire):
            if hasattr(self, 'sig_valid_write'):
                valid = self.sig_valid_write
            else:
                valid = self.m.TmpReg(initval=0)
                self.sig_valid_write = valid
                self.sig_valid.assign(valid)
        else:
            valid = self.sig_valid

        if self.sig_ready is None:
            ready = 1
        else:
            ready = self.sig_ready

        if cond is not None:
            self.seq.If(cond)

        if self.sig_ready is None:
            ack = None
        else:
            ack = vtypes.OrList(ready, vtypes.Not(valid))

        self.seq.If(ack)(
            data(wdata)
        )

        if self.sig_valid is not None:
            self.seq.Then()(
                valid(1),
            )
            self.seq.Delay(1)(
                valid(0)
            )
            if self.sig_ready is not None:
                self.seq.If(vtypes.AndList(valid, vtypes.Not(ready)))(
                    valid(valid)  # overwrite previous de-assertion
                )

        return ack

    def _implement(self, m, seq):
        if self.input_data is None:
            raise TypeError("'input_data' must not be None.")

        # if input_data is a standard signal, skip
        if not isinstance(self.input_data, _Numeric):
            return

        if self.input_data.sig_data is None:
            self.input_data._implement(m, seq)

        self.sig_data = self.input_data.sig_data
        self.sig_valid = self.input_data.sig_valid
        self.sig_ready = self.input_data.sig_ready

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

        if isinstance(self.input_valid, (vtypes._Numeric, int, bool)):
            self.sig_valid = self.input_valid
        elif self.input_valid is not None:
            self.sig_valid = type_i(self.input_valid)
        else:
            self.sig_valid = None

        if isinstance(self.input_ready, (vtypes.Wire, vtypes.Output)):
            self.sig_ready = self.input_ready
        elif self.input_ready is not None:
            self.sig_ready = type_o(self.input_ready)
        else:
            self.sig_ready = None

    def _implement_output(self, m, seq, aswire=False):
        if isinstance(self.input_data, _Numeric):
            if self.input_data.output_sig_data is None:
                self.input_data._implement_output(m, seq, aswire)
            self.output_sig_data = self.input_data.output_sig_data
            self.output_sig_valid = self.input_data.output_sig_valid
            self.output_sig_ready = self.input_data.output_sig_ready
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

    def _implement(self, m, seq):
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

        self.sig_valid = None
        self.sig_ready = None

    def __getattribute__(self, attr):
        # normal access
        return _Numeric.__getattribute__(self, attr)


class _Accumulator(_UnaryOperator):
    latency = 1
    ops = (vtypes.Plus, )

    def __init__(self, right, size=None, initval=None,
                 enable=None, reset=None, width=None, signed=None, label=None):

        self.size = _to_constant(size) if size is not None else None

        if (self.size is not None and
            not isinstance(self.size, _Constant) and
                not isinstance(self.size, _ParameterVariable)):
            raise TypeError("size must be _Constant or _ParameterVariable, not '%s'" %
                            str(type(self.size)))

        self.initval = (_to_constant(initval)
                        if initval is not None else _to_constant(0))

        if not isinstance(self.initval, _Constant):
            raise TypeError("initval must be Constant, not '%s'" %
                            str(type(self.initval)))

        self.enable = _to_constant(enable)
        if self.enable is not None:
            self.enable._add_sink(self)

        self.reset = _to_constant(reset)
        if self.reset is not None:
            self.reset._add_sink(self)

        _UnaryOperator.__init__(self, right)

        if width is not None:
            self.width = width

        if signed is not None:
            self.signed = signed

        self.label = label

    def _set_managers(self):
        self._set_df(_get_df(self.right, self.initval,
                             self.enable, self.reset))
        self._set_module(getattr(self.df, 'module', None))
        self._set_seq(getattr(self.df, 'seq', None))

    def eval(self):
        return self

    def _implement(self, m, seq):
        if self.latency != 1:
            raise ValueError("Latency mismatch '%d' vs '%s'" %
                             (self.latency, 1))

        size_data = self.size.sig_data if self.size is not None else None
        #size_valid = self.size.sig_valid if self.size is not None else None
        #size_ready = self.size.sig_ready if self.size is not None else None

        initval_data = self.initval.sig_data
        #initval_valid = self.initval.sig_valid
        #initval_ready = self.initval.sig_ready

        width = self.get_width()
        signed = self.get_signed()

        # for Pulse
        if not self.ops and self.size is not None:
            width = 1

        data = m.Reg(self.name('data'), width,
                     initval=initval_data, signed=signed)
        valid = m.Reg(self.name('valid'), initval=0)
        ready = m.Wire(self.name('ready'))

        if self.size is not None:
            count = m.Reg(self.name('count'),
                          size_data.get_width() + 1, initval=0)
            next_count_value = vtypes.Mux(count == size_data - 1,
                                          0, count + 1)
            count_zero = (count == 0)

        self.sig_data = data
        self.sig_valid = valid
        self.sig_ready = ready

        rdata = self.right.sig_data
        enabledata = self.enable.sig_data if self.enable is not None else None
        resetdata = self.reset.sig_data if self.reset is not None else None

        rvalid = self.right.sig_valid
        enablevalid = self.enable.sig_valid if self.enable is not None else None
        resetvalid = self.reset.sig_valid if self.reset is not None else None

        rready = self.right.sig_ready
        enableready = self.enable.sig_ready if self.enable is not None else None
        resetready = self.reset.sig_ready if self.reset is not None else None

        all_valid = _and_vars(rvalid, enablevalid, resetvalid)
        all_ready = _and_vars(rready, enableready, resetready)

        accept = vtypes.OrList(ready, vtypes.Not(valid))

        valid_cond = _and_vars(accept, all_ready)
        valid_reset_cond = _and_vars(valid, ready)
        data_cond = _and_vars(valid_cond, all_valid)
        ready_cond = _and_vars(accept, all_valid)

        value = data
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
            value = (count == (size_data - 1))

        if self.reset is not None or self.size is not None:
            reset_value = initval_data
            for op in self.ops:
                if not isinstance(op, type):
                    reset_value = op(reset_value, rdata)
                elif issubclass(op, vtypes._BinaryOperator):
                    reset_value = op(reset_value, rdata)
                elif issubclass(op, vtypes._UnaryOperator):
                    reset_value = op(reset_value)

                if not isinstance(reset_value, vtypes._Numeric):
                    raise TypeError("Operator '%s' returns unsupported object type '%s'."
                                    % (str(op), str(type(reset_value))))

            if not self.ops and self.size is not None:
                reset_value = (count == (size_data - 1))

        if self.enable is not None:
            enable_data_cond = _and_vars(data_cond, enabledata)
            seq(data(value), cond=enable_data_cond)

            if self.size is not None:
                seq(count(next_count_value), cond=enable_data_cond)

            _connect_ready(m, enableready, ready_cond)

        else:
            seq(data(value), cond=data_cond)

            if self.size is not None:
                seq(count(next_count_value), cond=data_cond)

        seq(valid(0), cond=valid_reset_cond)
        seq(valid(all_valid), cond=valid_cond)

        _connect_ready(m, rready, ready_cond)

        if self.reset is not None:
            if self.enable is None:
                reset_data_cond = _and_vars(data_cond, resetdata)
                seq(data(reset_value), cond=reset_data_cond)

                if self.size is not None:
                    seq(count(0), cond=reset_data_cond)
                    reset_data_cond = _and_vars(data_cond, count_zero)
                    seq(data(reset_value), cond=reset_data_cond)

            else:
                reset_data_cond = _and_vars(data_cond, resetdata)
                seq(data(initval_data), cond=reset_data_cond)

                reset_enable_data_cond = _and_vars(data_cond,
                                                   enabledata, resetdata)
                seq(data(reset_value), cond=reset_enable_data_cond)

                if self.size is not None:
                    seq(count(0), cond=reset_enable_data_cond)
                    reset_enable_data_cond = _and_vars(
                        data_cond, enabledata, count_zero)
                    seq(data(reset_value), cond=reset_enable_data_cond)

            _connect_ready(m, resetready, ready_cond)

        elif self.size is not None:
            if self.enable is not None:
                reset_enable_data_cond = _and_vars(
                    data_cond, enabledata, count_zero)
                seq(data(reset_value), cond=reset_enable_data_cond)
            else:
                reset_data_cond = _and_vars(data_cond, count_zero)
                seq(data(reset_value), cond=reset_data_cond)

        if not self._has_output():
            _connect_ready(m, ready, vtypes.Int(1))


class ReduceAdd(_Accumulator):
    ops = (vtypes.Plus, )

    def __init__(self, right, size=None, initval=0,
                 enable=None, reset=None, width=None, signed=None):
        _Accumulator.__init__(self, right, size, initval,
                              enable, reset, width, signed)


class ReduceSub(_Accumulator):
    ops = (vtypes.Minus, )

    def __init__(self, right, size=None, initval=0,
                 enable=None, reset=None, width=None, signed=None):
        _Accumulator.__init__(self, right, size, initval,
                              enable, reset, width, signed)


class ReduceMul(_Accumulator):
    latency = 1
    ops = (vtypes.Times, )

    def __init__(self, right, size=None, initval=0,
                 enable=None, reset=None, width=None, signed=None):
        _Accumulator.__init__(self, right, size, initval,
                              enable, reset, width, signed)


class ReduceDiv(_Accumulator):
    latency = 32
    ops = ()

    def __init__(self, right, size=None, initval=0,
                 enable=None, reset=None, width=None, signed=None):
        raise NotImplementedError()
        _Accumulator.__init__(self, right, size, initval,
                              enable, reset, width, signed)


class ReduceCustom(_Accumulator):

    def __init__(self, ops, right, size=None, initval=0,
                 enable=None, reset=None, width=None, signed=None, label=None):
        _Accumulator.__init__(self, right, size, initval,
                              enable, reset, width, signed, label)

        if not isinstance(ops, (tuple, list)):
            ops = tuple([ops])

        self.ops = ops


class Counter(_Accumulator):

    def __init__(self, step=1, size=None, initval=0,
                 control=None, enable=None, reset=None, width=32, signed=False):

        self.ops = (lambda x, y: x + step, )

        if control is None:
            control = 0

        initval -= step

        _Accumulator.__init__(self, control, size, initval,
                              enable, reset, width, signed, 'Counter')


class Pulse(_Accumulator):
    ops = ()

    def __init__(self, size, control=None, enable=None, reset=None):

        if control is None:
            control = 0

        step = 1
        initval = 0
        width = 1
        signed = False

        _Accumulator.__init__(self, control, size, initval,
                              enable, reset, width, signed, 'Pulse')


def _ReduceValid(cls, right, size, initval=0,
                 enable=None, reset=None, width=None, signed=None):

    data = cls(right, size, initval,
               enable, reset, width, signed)
    valid = Pulse(size, right, enable, reset)

    return data, valid


def ReduceAddValid(right, size, initval=0,
                   enable=None, reset=None, width=None, signed=None):

    cls = ReduceAdd
    return _ReduceValid(cls, right, size, initval,
                        enable, reset, width, signed)


def ReduceSubValid(right, size, initval=0,
                   enable=None, reset=None, width=None, signed=None):

    cls = ReduceSub
    return _ReduceValid(cls, right, size, initval,
                        enable, reset, width, signed)


def ReduceMulValid(right, size, initval=0,
                   enable=None, reset=None, width=None, signed=None):

    cls = ReduceMul
    return _ReduceValid(cls, right, size, initval,
                        enable, reset, width, signed)


def ReduceDivValid(right, size, initval=0,
                   enable=None, reset=None, width=None, signed=None):

    cls = ReduceDiv
    return _ReduceValid(cls, right, size, initval,
                        enable, reset, width, signed)


def ReduceCustomValid(ops, right, size, initval=0,
                      enable=None, reset=None, width=None, signed=None):

    data = ReduceCustom(ops, right, size, initval,
                        enable, reset, width, signed)
    valid = Pulse(size, right, enable, reset)

    return data, valid


class Int(_Constant):

    def __init__(self, value, signed=True):
        _Constant.__init__(self, value)
        self.signed = signed

    def _set_attributes(self):
        self.width = vtypes.get_width(self.value)
        self.point = 0

    def _implement(self, m, seq):
        data = vtypes.Int(self.value, width=self.width, signed=self.signed)
        valid = None
        ready = None
        self.sig_data = data
        self.sig_valid = valid
        self.sig_ready = ready


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

    def _implement(self, m, seq):
        data = vtypes.Int(self.value, width=self.width, signed=self.signed)
        valid = None
        ready = None
        self.sig_data = data
        self.sig_valid = valid
        self.sig_ready = ready


class Str(_Constant):

    def _set_attributes(self):
        self.width = 0
        self.point = 0
        self.signed = False


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


def is_dataflow_object(*objs):
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


def _get_df(*vars):
    ret = None
    for var in vars:
        v = getattr(var, 'df', None)
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


def read_multi(m, *vars, **opts):
    """ read multiple variables """

    cond = opts['cond'] if 'cond' in opts else None

    if not vars:
        raise ValueError('No variables.')

    all_valid = m.Wire('_dataflow_tmp_all_valid_%d' % m.get_tmp())

    all_valid_list = []
    rdata_list = []
    rvalid_list = []

    for var in vars:
        if not isinstance(var, _Numeric):
            raise TypeError("var '%s' is not dataflow variable." % str(var))

        if var.output_node is not None and id(var) != id(var.output_node):
            var = var.output_node

        elif var.output_sig_data is None:

            # set default name
            if var.output_data is None:
                var.output_tmp()

            var._implement_output_sig(var.m, var.seq, aswire=True)

        data = var.output_sig_data
        valid = var.output_sig_valid

        if valid is None:
            valid = 1

        all_valid_list.append(valid)

        ready = make_condition(cond, all_valid)
        val = 1 if ready is None else ready

        if ready is not None and var.output_sig_ready is None:
            raise ValueError("Dataflow ready port is required for throttling.")

        if var.output_sig_ready is not None:
            prev_assign = var.output_sig_ready._get_assign()
            if not prev_assign:
                var.output_sig_ready.assign(val)
            else:
                prev_assign.overwrite_right(
                    vtypes.OrList(prev_assign.statement.right, val))
                m = var.output_sig_ready._get_module()
                m.remove(prev_assign)
                m.append(prev_assign)

        if ready is not None:
            ack = vtypes.AndList(valid, ready)
        else:
            ack = valid

        rdata = data
        rvalid = ack

        rdata_list.append(rdata)
        rvalid_list.append(rvalid)

    all_valid.assign(vtypes.Ands(*all_valid_list))

    return rdata_list, rvalid_list[0]
