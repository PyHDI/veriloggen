from __future__ import absolute_import
from __future__ import print_function

from collections import OrderedDict
import veriloggen.core.vtypes as vtypes

def max(*vars):
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

def connect_ready(m, var, ready):
    prev_subst = var.get_subst()
    if not prev_subst:
        m.Assign( var(ready) )
    elif isinstance(prev_subst[0].right, vtypes.Int) and (prev_subst[0].right.value==1):
        var.subst[0].overwrite_right( ready )
    else:
        var.subst[0].overwrite_right( vtypes.AndList(prev_subst[0].right, ready) )

#-------------------------------------------------------------------------------
def tmp_data(val, prefix='_tmp_data_'):
    return ''.join([prefix, str(val)])

def tmp_valid(val, prefix='_tmp_valid_'):
    return ''.join([prefix, str(val)])

def tmp_ready(val, prefix='_tmp_ready_'):
    return ''.join([prefix, str(val)])

#-------------------------------------------------------------------------------
def to_constant(obj):
    if isinstance(obj, (int, float, bool, str)):
        return Constant(obj)
    return obj

#-------------------------------------------------------------------------------
class _Node(object): pass

#-------------------------------------------------------------------------------
class _Numeric(_Node):
    latency = 0
    def __init__(self):
        self.output_data = None
        self.output_valid = None
        self.output_ready = None
        
        self.sig_data = None
        self.sig_valid = None
        self.sig_ready = None

        self.start_stage = None
        self.end_stage = None
        self.sink = []
        
        # stage numbers incremented
        self.delayed_value = OrderedDict()
        
        # stage numbers NOT incremented
        self.previous_value = OrderedDict()

    def output(self, data=None, valid=None, ready=None):
        if self.output_data is not None:
            raise ValueError('output_data is already assigned.')
        self.output_data = data
        self.output_valid = valid
        self.output_ready = ready

    #--------------------------------------------------------------------------
    def __hash__(self):
        return id(self)

    def _has_output(self):
        if self.output_data is not None: return True
        return False

    def _implement(self, m, seq, width=32):
        raise TypeError('_implement() is not implemented on this class.')
    
    def _implement_input(self, m, seq, width=32):
        raise TypeError('_implement_input() is not implemented on this class.')

    def _disable_output(self):
        self.output_data = None
        self.output_valid = None
        self.output_ready = None
    
    def _implement_output(self, m, seq, width=32):
        if self.end_stage is None:
            raise ValueError('end_stage is not fixed yet.')
        
        data = m.Output(self.output_data, width=width)
        if self.output_valid is not None:
            valid = m.Output(self.output_valid)
        if self.output_ready is not None:
            ready = m.Input(self.output_ready)
            
        m.Assign( data(self.sig_data) )
        if self.output_valid is not None:
            m.Assign( valid(self.sig_valid) )
        if self.output_ready is not None:
            m.Assign( self.sig_ready(ready) )

    def _set_start_stage(self, stage):
        self.start_stage = stage

    def _get_start_stage(self):
        return self.start_stage

    def _has_start_stage(self):
        if self.start_stage is None: return False
        return True

    def _set_end_stage(self, stage):
        self.end_stage = stage

    def _get_end_stage(self):
        return self.end_stage

    def _has_end_stage(self):
        if self.end_stage is None: return False
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

    #--------------------------------------------------------------------------
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
    
    def __getitem__(self, r):
        if isinstance(r, slice):
            left = r.start
            right = r.stop
            step = r.step
            if step is None:
                return Slice(self, left, right)
            else:
                raise ValueError("slice with step is not supported in Verilog Slice.")
        return Pointer(self, r)

    def sra(self, r): # shift right arithmetically
        return Sra(self, r)

    def repeat(self, times):
        return Repeat(self, times)

    def bit_length(self):
        return None

#-------------------------------------------------------------------------------
class _Operator(_Numeric):
    latency = 1
    
class _BinaryOperator(_Operator):
    def __init__(self, left, right):
        _Operator.__init__(self)
        self.left = left
        self.right = to_constant(right)
        self.left._add_sink(self)
        self.right._add_sink(self)
        
    def bit_length(self):
        return max(self.left.bit_length(), self.right.bit_length())

    def _implement(self, m, seq, width=32):
        if self.latency != 1:
            raise ValueError('This implement() is designed for %d latency' % self.latency)

        tmp = m.get_tmp()
        data = m.Reg(tmp_data(tmp), width, initval=0)
        valid = m.Reg(tmp_valid(tmp), initval=0)
        ready = m.Wire(tmp_ready(tmp))
        self.sig_data = data
        self.sig_valid = valid
        self.sig_ready = ready
        
        ldata = self.left.sig_data
        rdata = self.right.sig_data
        
        lvalid = self.left.sig_valid
        rvalid = self.right.sig_valid
        
        lready = self.left.sig_ready
        rready = self.right.sig_ready
        
        all_valid = vtypes.AndList(lvalid, rvalid)
        all_ready = vtypes.AndList(lready, rready)

        ack = vtypes.AndList(valid, ready)
        accept = vtypes.OrList(ready, vtypes.Not(valid))

        valid_cond = vtypes.AndList(accept, all_ready)
        data_cond = vtypes.AndList(valid_cond, all_valid)
        ready_cond = vtypes.AndList(accept, all_valid)
        
        op = getattr(vtypes, self.__class__.__name__)

        seq( data(op(ldata, rdata)), cond=data_cond )
        seq( valid(0), cond=ack )
        seq( valid(all_valid), cond=valid_cond )
        connect_ready(m, lready, ready_cond)
        connect_ready(m, rready, ready_cond)

        if not self._has_output():
            connect_ready(m, ready, vtypes.Int(1))
            
class _UnaryOperator(_Operator):
    def __init__(self, right):
        _Operator.__init__(self)
        self.right = to_constant(right)
        self.right._add_sink(self)
        
    def bit_length(self):
        return self.right.bit_length()

    def _implement(self, m, seq, width=32):
        if self.latency != 1:
            raise ValueError('This implement() is designed for %d latency' % self.latency)
        
        tmp = m.get_tmp()
        data = m.Reg(tmp_data(tmp), width, initval=0)
        valid = m.Reg(tmp_valid(tmp), initval=0)
        ready = m.Wire(tmp_ready(tmp))
        self.sig_data = data
        self.sig_valid = valid
        self.sig_ready = ready
        
        rdata = self.right.sig_data
        
        rvalid = self.right.sig_valid
        
        rready = self.right.sig_ready

        all_valid = rvalid
        all_ready = rready

        ack = vtypes.AndList(valid, ready)
        accept = vtypes.OrList(ready, vtypes.Not(valid))

        valid_cond = vtypes.AndList(accept, all_ready)
        data_cond = vtypes.AndList(valid_cond, all_valid)
        ready_cond = vtypes.AndList(accept, all_valid)
        
        op = getattr(vtypes, self.__class__.__name__)
        
        seq( data(op(rdata)), cond=data_cond )
        seq( valid(0), cond=ack )
        seq( valid(all_valid), cond=valid_cond )
        connect_ready(m, rready, ready_cond)
        
        if not self._has_output():
            connect_ready(m, ready, vtypes.Int(1))

class Power(_BinaryOperator): latency = 0
class Times(_BinaryOperator): latency = 6
class Divide(_BinaryOperator): latency = 32
class Mod(_BinaryOperator): latency = 32
class Plus(_BinaryOperator): pass
class Minus(_BinaryOperator): pass

class Sll(_BinaryOperator): pass
class Srl(_BinaryOperator): pass
class Sra(_BinaryOperator): pass

class LessThan(_BinaryOperator): pass
class GreaterThan(_BinaryOperator): pass
class LessEq(_BinaryOperator): pass
class GreaterEq(_BinaryOperator): pass

class Eq(_BinaryOperator): pass
class NotEq(_BinaryOperator): pass
class Eql(_BinaryOperator): pass # ===
class NotEql(_BinaryOperator): pass # !==

class And(_BinaryOperator): pass
class Xor(_BinaryOperator): pass
class Xnor(_BinaryOperator): pass
class Or(_BinaryOperator): pass
class Land(_BinaryOperator): pass
class Lor(_BinaryOperator): pass

class Uplus(_UnaryOperator): pass
class Uminus(_UnaryOperator): pass
class Ulnot(_UnaryOperator): pass
class Unot(_UnaryOperator): pass
class Uand(_UnaryOperator): pass
class Unand(_UnaryOperator): pass
class Uor(_UnaryOperator): pass
class Unor(_UnaryOperator): pass
class Uxor(_UnaryOperator): pass
class Uxnor(_UnaryOperator): pass
        
#-------------------------------------------------------------------------------
class _SpecialOperator(_Operator):
    def __init__(self, *args, **kwargs):
        _Operator.__init__(self)
        self.args = args
        self.kwargs = kwargs

#-------------------------------------------------------------------------------
class Pointer(_SpecialOperator):
    def __init__(self, var, pos):
        _SpecialOperator.__init__(self)
        self.var = var
        self.pos = pos
        self.var._add_sink(self)
        self.pos._add_sink(self)
        
    def bit_length(self):
        if isinstance(var, _Variable) and var.length is not None:
            return self.var.bit_length()
        return 1
    
class Slice(_SpecialOperator):
    def __init__(self, var, msb, lsb):
        _SpecialOperator.__init__(self)
        self.var = var
        self.msb = msb
        self.lsb = lsb
        self.var._add_sink(self)
        self.msb._add_sink(self)
        self.lsb._add_sink(self)

    def bit_length(self):
        raise NotImplementedError('bit_length is not implemented.')
    
class Cat(_SpecialOperator):
    def __init__(self, *vars):
        _SpecialOperator.__init__(self)
        self.vars = tuple(vars)
        for var in self.vars:
            var._add_sink(self)
    
    def bit_length(self):
        values = [ v.bit_length() for v in self.vars ]
        ret = values[0]
        for v in values[1:]:
            ret = ret + v
        return ret

class Repeat(_SpecialOperator):
    def __init__(self, var, times):
        _SpecialOperator.__init__(self)
        self.var = var
        self.times = times
        self.var._add_sink(self)
        self.times._add_sink(self)

    def bit_length(self):
        return self.var.bit_length() * self.times
        
#-------------------------------------------------------------------------------
class Cond(_SpecialOperator):
    def __init__(self, condition, true_value, false_value):
        _Operator.__init__(self)
        self.condition = condition
        self.true_value = true_value
        self.false_value = false_value
        self.condition._add_sink(self)
        self.true_value._add_sink(self)
        self.false_value._add_sink(self)
        
    def bit_length(self):
        raise NotImplementedError('bit_length is not implemented.')

# Alias of Cond
Mux = Cond
    
#-------------------------------------------------------------------------------
class _Delay(_UnaryOperator):
    def __init__(self, right):
        _UnaryOperator.__init__(self, right)
        # parent value for delayed_value and previous_value
        self.parent_value = None
        
    def _set_parent_value(self, value):
        self.parent_value = value

    def _get_parent_value(self):
        return self.parent_value
        
    def _implement(self, m, seq, width=32):
        if self.latency != 1:
            raise ValueError('This implement() is designed for %d latency' % self.latency)
        
        tmp = m.get_tmp()
        data = m.Reg(tmp_data(tmp), width, initval=0)
        valid = m.Reg(tmp_valid(tmp), initval=0)
        ready = m.Wire(tmp_ready(tmp))
        self.sig_data = data
        self.sig_valid = valid
        self.sig_ready = ready
        
        rdata = self.right.sig_data
        
        rvalid = self.right.sig_valid
        
        rready = self.right.sig_ready

        all_valid = rvalid
        all_ready = rready

        ack = vtypes.AndList(valid, ready)
        accept = vtypes.OrList(ready, vtypes.Not(valid))

        valid_cond = vtypes.AndList(accept, all_ready)
        data_cond = vtypes.AndList(valid_cond, all_valid)
        ready_cond = vtypes.AndList(accept, all_valid)
        
        seq( data(rdata), cond=data_cond )
        seq( valid(0), cond=ack )
        seq( valid(all_valid), cond=valid_cond )
        connect_ready(m, rready, ready_cond)
        
        if not self._has_output():
            connect_ready(m, ready, vtypes.Int(1))

#-------------------------------------------------------------------------------
class _Constant(_Numeric):
    def __init__(self, value):
        _Numeric.__init__(self)
        self.value = value

    def __hash__(self):
        return hash(self.value)

    def _implement(self, m, seq, width=32):
        tmp = m.get_tmp()
        data = self.value
        valid = vtypes.Int(1, base=2, width=1)
        ready = m.Wire(tmp_ready(tmp))
        self.sig_data = data
        self.sig_valid = valid
        self.sig_ready = ready
        
#-------------------------------------------------------------------------------
class _Variable(_Numeric):
    def __init__(self, data=None, valid=None, ready=None):
        _Numeric.__init__(self)
        self.input_data = data
        self.input_valid = valid
        self.input_ready = ready
        if isinstance(self.input_data, _Numeric):
            self.input_data._add_sink(self)
        
    def __hash__(self):
        return id(self)

    def _implement(self, m, seq, width=32):
        if not isinstance(self.input_data, _Numeric):
            return
        tmp = m.get_tmp()
        data = m.Wire(tmp_data(tmp), width)
        valid = m.Wire(tmp_valid(tmp))
        ready = m.Wire(tmp_ready(tmp))
        m.Assign( data(self.input_data.sig_data) )
        m.Assign( valid(self.input_data.sig_valid) )
        connect_ready(m, self.input_data.sig_ready, ready)
            
    def _implement_input(self, m, seq, width=32):
        if isinstance(self.input_data, _Numeric):
            return
        self.sig_data = m.Input(self.input_data, width)
        if self.input_valid is not None:
            self.sig_valid = m.Input(self.input_valid)
        else:
            self.sig_valid = vtypes.Int(1)
        if self.input_ready is not None:
            self.sig_ready = m.Output(self.input_ready)
        else:
            tmp = m.get_tmp()
            self.sig_ready = m.Wire(tmp_ready(tmp))
            

#-------------------------------------------------------------------------------
class _Accumulator(_Variable):
    latency = 1
    def __init__(self, data, init=None, reset=None):
        _Variable.__init__(self, data=data, valid=None, ready=None)
        self.init = init
        self.reset = reset

#-------------------------------------------------------------------------------
class Int(_Constant):
    pass

class Bool(_Constant):
    pass

class Float(_Constant):
    pass

class Str(_Constant):
    pass

def Constant(value):
    if isinstance(value, int):
        return Int(value)
    if isinstance(value, bool):
        return Bool(value)
    if isinstance(value, float):
        return Float(value)
    if isinstance(value, str):
        return Str(value)
    raise TypeError("Unsupported type for Constant '%s'" % str(type(value)))

#-------------------------------------------------------------------------------
class Variable(_Variable):
    pass

#-------------------------------------------------------------------------------
class Iadd(_Accumulator):
    pass

class Isub(_Accumulator):
    pass

class Imul(_Accumulator):
    pass

class Idiv(_Accumulator):
    pass

class Icustom(_Accumulator):
    pass
