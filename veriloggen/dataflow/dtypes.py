from __future__ import absolute_import
from __future__ import print_function

from collections import OrderedDict
import veriloggen.core.vtypes as vtypes
import veriloggen.types.fixed as fx
from . import mul
from . import div

# Object ID counter for object sorting key
global_object_counter = 0

#-------------------------------------------------------------------------------
def is_dataflow_object(*objs):
    for obj in objs:
        if isinstance(obj, _Node):
            return True
    return False

#-------------------------------------------------------------------------------
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

def Variable(data=None, valid=None, ready=None, width=32, point=0, signed=False):
    return _Variable(data, valid, ready, width, point, signed)

#-------------------------------------------------------------------------------
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
    prev_subst = var._get_subst()
    if not prev_subst:
        m.Assign( var(ready) )
    elif isinstance(prev_subst[0].right, vtypes.Int) and (prev_subst[0].right.value==1):
        var.subst[0].overwrite_right( ready )
    else:
        var.subst[0].overwrite_right( _and_vars(prev_subst[0].right, ready) )

#-------------------------------------------------------------------------------
def _to_constant(obj):
    if isinstance(obj, (int, float, bool, str)):
        return Constant(obj)
    return obj

#-------------------------------------------------------------------------------
def _tmp_data(val, prefix='_tmp_data_'):
    return ''.join([prefix, str(val)])

def _tmp_valid(val, prefix='_tmp_valid_'):
    return ''.join([prefix, str(val)])

def _tmp_ready(val, prefix='_tmp_ready_'):
    return ''.join([prefix, str(val)])

#-------------------------------------------------------------------------------
class _Node(object):
    def __init__(self):
        global global_object_counter
        self.object_id = global_object_counter
        global_object_counter += 1

    def __hash__(self):
        return hash((id(self), self.object_id))

    def __eq__(self, other):
        return (id(self), self.object_id) == (id(other), other.object_id)
    
#-------------------------------------------------------------------------------
class _Numeric(_Node):
    latency = 0
    def __hash__(self):
        return hash((id(self), self.object_id))
    
    def __init__(self):
        _Node.__init__(self)
        self.output_data = None
        self.output_valid = None
        self.output_ready = None

        self.output_node = None
        
        self.sig_data = None
        self.sig_valid = None
        self.sig_ready = None

        self.start_stage = None
        self.end_stage = None
        self.sink = []

        # set up by set_attributes()
        self.width = None
        self.point = None
        self.signed = False
        
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
        
    #--------------------------------------------------------------------------
    def set_attributes(self):
        raise NotImplementedError('set_attributes() is not implemented')

    def get_signed(self):
        return self.signed
    
    def get_point(self):
        return self.point
    
    def bit_length(self):
        return self.width

    def eval(self):
        raise NotImplementedError('eval() is not implemented')
    
    #--------------------------------------------------------------------------
    def _has_output(self):
        if self.output_data is not None: return True
        return False

    def _implement(self, m, seq):
        raise NotImplementedError('_implement() is not implemented.')
    
    def _implement_input(self, m, seq, aswire=False):
        raise NotImplementedError('_implement_input() is not implemented.')

    def _disable_output(self):
        self.output_data = None
        self.output_valid = None
        self.output_ready = None

    def _set_output_node(self, node):
        self.output_node = node
    
    def _implement_output(self, m, seq, aswire=False):
        if self.end_stage is None:
            #raise ValueError('end_stage is not fixed yet.')
            self.end_stage = 0

        width = self.bit_length()
        signed = self.get_signed()

        type_i = m.Wire if aswire else m.Input
        type_o = m.Wire if aswire else m.Output

        if isinstance(self.output_data, (vtypes.Wire, vtypes.Output)):
            data = self.output_data
        else:
            data = type_o(self.output_data, width=width, signed=signed)

        if isinstance(self.output_valid, (vtypes.Wire, vtypes.Output)):
            valid = self.output_valid
        elif self.output_valid is not None:
            valid = type_o(self.output_valid)

        if isinstance(self.output_ready, (vtypes._Numeric, int, bool)):
            ready = self.output_ready
        elif self.output_ready is not None:
            ready = type_i(self.output_ready)
            
        m.Assign( data(self.sig_data) )
        
        if self.output_valid is not None:
            m.Assign( valid(self.sig_valid) )
            
        if self.output_ready is not None:
            m.Assign( self.sig_ready(ready) )
        elif self.sig_ready is not None:
            m.Assign( self.sig_ready(1) )

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
    
    def __getitem__(self, r):
        if isinstance(r, slice):
            size = self.bit_length()

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
                    raise ValueError("Slice with step is not supported in Verilog Slice.")

                if step == 0:
                    raise ValueError("Illegal slice step: step = %d" % step)
                
                values = [ Pointer(self, i) for i in range(right, left+1, step) ]
                values.reverse()
                return Cat(*values)
            
        if isinstance(r, int) and r < 0:
            r = self.bit_length() - abs(r)
            
        return Pointer(self, r)

    def sra(self, r): # shift right arithmetically
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
        ret = self.bit_length()
        if not isinstance(ret, int):
            raise TypeError("Non int length.")
        return ret

    @property
    def raw_data(self):
        if self.sig_data is None:
            raise TypeError("Dataflow is not synthesized yet. Run Dataflow.implement().")
        return self.sig_data

    @property
    def raw_valid(self):
        if self.sig_data is None:
            raise TypeError("Dataflow is not synthesized yet. Run Dataflow.implement().")
        if self.sig_valid is None:
            return 1
        return self.sig_valid

    @property
    def raw_ready(self):
        if self.sig_data is None:
            raise TypeError("Dataflow is not synthesized yet. Run Dataflow.implement().")
        return self.sig_ready

    @property
    def data(self):
        if self.output_node is not None:
            return self.output_node.raw_data
        return self.raw_data

    @property
    def valid(self):
        if self.output_node is not None:
            return self.output_node.raw_valid
        return self.raw_valid

    @property
    def ready(self):
        if self.output_node is not None:
            return self.output_node.raw_ready
        return self.raw_ready
    
#-------------------------------------------------------------------------------
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
        self.set_attributes()

    def set_attributes(self):
        left_fp = self.left.get_point()
        right_fp = self.right.get_point()
        left = self.left.bit_length() - left_fp
        right = self.right.bit_length() - right_fp
        self.width = max(left, right) + max(left_fp, right_fp)
        self.point = max(left_fp, right_fp)
        self.signed = self.left.get_signed() and self.right.get_signed()
                
    def _implement(self, m, seq):
        if self.latency != 1:
            raise ValueError("Latency mismatch '%d' vs '%s'" % (self.latency, 1))

        width = self.bit_length()
        signed = self.get_signed()

        tmp = m.get_tmp()
        data = m.Reg(_tmp_data(tmp), width, initval=0, signed=signed)
        valid = m.Reg(_tmp_valid(tmp), initval=0)
        ready = m.Wire(_tmp_ready(tmp))
        self.sig_data = data
        self.sig_valid = valid
        self.sig_ready = ready

        lpoint = self.left.get_point()
        rpoint = self.right.get_point()
        
        ldata, rdata = fx.adjust(self.left.sig_data, self.right.sig_data, lpoint, rpoint, signed)
        
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
        
        seq( data(self.op(ldata, rdata)), cond=data_cond )
        seq( valid(0), cond=valid_reset_cond )
        seq( valid(all_valid), cond=valid_cond )
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
        self.set_attributes()
        
    def set_attributes(self):
        right = self.right.bit_length()
        right_fp = self.right.get_point()
        self.width = right
        self.point = right_fp
        self.signed = self.right.get_signed()
                
    def _implement(self, m, seq):
        if self.latency != 1:
            raise ValueError("Latency mismatch '%d' vs '%s'" % (self.latency, 1))
        
        width = self.bit_length()
        signed = self.get_signed()

        tmp = m.get_tmp()
        data = m.Reg(_tmp_data(tmp), width, initval=0, signed=signed)
        valid = m.Reg(_tmp_valid(tmp), initval=0)
        ready = m.Wire(_tmp_ready(tmp))
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
        
        seq( data(self.op(rdata)), cond=data_cond )
        seq( valid(0), cond=valid_reset_cond )
        seq( valid(all_valid), cond=valid_cond )
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
    
    def set_attributes(self):
        left_fp = self.left.get_point()
        right_fp = self.right.get_point()
        left = self.left.bit_length()
        right = self.right.bit_length()
        self.width = max(left, right)
        self.point = max(left_fp, right_fp)
        self.signed = self.left.get_signed() and self.right.get_signed()
                
    def _implement(self, m, seq):
        if self.latency <= 3:
            raise ValueError("Latency of '*' operator must be greater than 3")

        width = self.bit_length()
        signed = self.get_signed()

        tmp = m.get_tmp()
        data = m.Wire(_tmp_data(tmp), width, signed=signed)
        valid = m.Wire(_tmp_valid(tmp))
        ready = m.Wire(_tmp_ready(tmp))
        self.sig_data = data
        self.sig_valid = valid
        self.sig_ready = ready

        lwidth = self.left.bit_length()
        rwidth = self.right.bit_length()
        
        lpoint = self.left.get_point()
        rpoint = self.right.get_point()

        lsigned = self.left.get_signed()
        rsigned = self.right.get_signed()

        ldata = self.left.sig_data
        rdata = self.right.sig_data

        accept = vtypes.OrList(ready, vtypes.Not(valid))
        
        odata = m.Wire(_tmp_data(tmp, prefix='_tmp_odata_'), lwidth+rwidth, signed=signed)
        data_reg = m.Reg(_tmp_data(tmp, prefix='_tmp_data_reg_'), lwidth+rwidth,
                         signed=signed, initval=0)
        
        shift_size = min(lpoint, rpoint)
        if shift_size > 0:
            seq( data_reg(fx.shift_right(odata, shift_size, signed=signed)), cond=accept )
        else:
            seq( data_reg(odata), cond=accept )
            
        m.Assign( data(data_reg) )
        
        ovalid = m.Wire(_tmp_valid(tmp, prefix='_tmp_ovalid_'))
        valid_reg = m.Reg(_tmp_valid(tmp, prefix='_tmp_valid_reg_'), initval=0)
        
        seq( valid_reg(ovalid), cond=accept )
        m.Assign( valid(valid_reg) )

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

        enable = m.Wire(_tmp_data(tmp, prefix='_tmp_enable_') )
        update = m.Wire(_tmp_data(tmp, prefix='_tmp_update_') )
        
        m.Assign( enable(data_cond) )
        m.Assign( update(accept) ) # NOT valid_cond
        
        ports = [ ('CLK', clk), ('RST', rst),
                  ('update', update), ('enable', enable), ('valid', ovalid),
                  ('a', ldata), ('b', rdata), ('c', odata) ]
        
        m.Instance(inst, ''.join(['mul', str(tmp)]), ports=ports)
        
        _connect_ready(m, lready, ready_cond)
        _connect_ready(m, rready, ready_cond)
        
        if not self._has_output():
            _connect_ready(m, ready, vtypes.Int(1))
    
class Divide(_BinaryOperator):
    latency = 32 + 3
    variable_latency = 'bit_length'
    def eval(self):
        left = self.left.eval()
        right = self.right.eval()
        if isinstance(left, int) and isinstance(right, int):
            return int(left / right)
        return Divide(left, right)
    
    def _implement(self, m, seq):
        if self.latency <= 3:
            raise ValueError("Latency of '*' operator must be greater than 3")

        width = self.bit_length()
        signed = self.get_signed()

        tmp = m.get_tmp()
        data = m.Wire(_tmp_data(tmp), width, signed=signed)
        valid = m.Wire(_tmp_valid(tmp))
        ready = m.Wire(_tmp_ready(tmp))
        self.sig_data = data
        self.sig_valid = valid
        self.sig_ready = ready
        
        lpoint = self.left.get_point()
        rpoint = self.right.get_point()
        
        lsigned = self.left.get_signed()
        rsigned = self.right.get_signed()
        
        ldata = m.Reg(_tmp_data(tmp, prefix='_tmp_ldata_'), width, signed=lsigned, initval=0)
        rdata = m.Reg(_tmp_data(tmp, prefix='_tmp_rdata_'), width, signed=rsigned, initval=0)
        
        lval, rval = fx.adjust(self.left.sig_data, self.right.sig_data, lpoint, rpoint, signed)

        accept = vtypes.OrList(ready, vtypes.Not(valid))
        
        seq( ldata(lval), cond=accept )
        seq( rdata(rval), cond=accept )
        
        sign = vtypes.OrList(vtypes.AndList(ldata[width-1] == 0, rdata[width-1] == 0), # + , +
                             vtypes.AndList(ldata[width-1] == 1, rdata[width-1] == 1)) # - , -

        abs_ldata = m.Reg(_tmp_data(tmp, prefix='_tmp_abs_ldata_'), width, initval=0)
        abs_rdata = m.Reg(_tmp_data(tmp, prefix='_tmp_abs_rdata_'), width, initval=0)

        if not lsigned:
            seq( abs_ldata(ldata), cond=accept )
        else:
            seq( abs_ldata(vtypes.Mux(ldata[width-1] == 0, ldata, vtypes.Unot(ldata) + 1)),
                 cond=accept )
        
        if not rsigned:
            seq( abs_rdata(rdata), cond=accept )
        else:
            seq( abs_rdata(vtypes.Mux(rdata[width-1] == 0, rdata, vtypes.Unot(rdata) + 1)),
                 cond=accept )

        osign = m.Wire(_tmp_data(tmp, prefix='_tmp_osign_'))
        abs_odata = m.Wire(_tmp_data(tmp, prefix='_tmp_abs_odata_'), width, signed=signed)
        
        odata = m.Reg(_tmp_data(tmp, prefix='_tmp_odata_'), width, signed=signed, initval=0)
            
        if not signed:
            seq( odata(abs_odata), cond=accept )
        else:
            seq( odata(vtypes.Mux(osign, abs_odata, vtypes.Unot(abs_odata) + 1)),
                 cond=accept )
        
        m.Assign( data(odata) )
        
        ovalid = m.Wire(_tmp_valid(tmp, prefix='_tmp_ovalid_'))    
                    
        v = ovalid
        for i in range(3):
            nv = m.Reg(_tmp_valid(tmp, prefix='_tmp_valid_reg' + str(i) + '_'), initval=0)
            seq( nv(v), cond=accept )
            v = nv
        m.Assign( valid(v) )

        s = sign
        for i in range(self.latency):
            ns = m.Reg(_tmp_data(tmp, prefix='_tmp_sign' + str(i) + '_'), initval=0)
            seq( ns(s), cond=accept )
            s = ns
        m.Assign( osign(s) )
        
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

        enable = m.Wire(_tmp_data(tmp, prefix='_tmp_enable_') )
        update = m.Wire(_tmp_data(tmp, prefix='_tmp_update_') )
        m.Assign( enable(data_cond) )
        m.Assign( update(accept) ) # NOT valid_cond
        
        params = [ ('W_D', width) ]
        ports = [ ('CLK', clk), ('RST', rst),
                  ('update', update), ('enable', enable), ('valid', ovalid),
                  ('in_a', abs_ldata), ('in_b', abs_rdata), ('rslt', abs_odata) ]
        
        m.Instance(inst, ''.join(['div', str(tmp)]), params, ports)

        _connect_ready(m, lready, ready_cond)
        _connect_ready(m, rready, ready_cond)
        
        if not self._has_output():
            _connect_ready(m, ready, vtypes.Int(1))
    
class Mod(_BinaryOperator):
    latency = 32 + 3
    variable_latency = 'bit_length'
    def eval(self):
        return self.left.eval() % self.right.eval()
    
    def _implement(self, m, seq):
        if self.latency <= 3:
            raise ValueError("Latency of '*' operator must be greater than 3")

        width = self.bit_length()
        signed = self.get_signed()

        tmp = m.get_tmp()
        data = m.Wire(_tmp_data(tmp), width, signed=signed)
        valid = m.Wire(_tmp_valid(tmp))
        ready = m.Wire(_tmp_ready(tmp))
        self.sig_data = data
        self.sig_valid = valid
        self.sig_ready = ready
        
        lpoint = self.left.get_point()
        rpoint = self.right.get_point()
        
        lsigned = self.left.get_signed()
        rsigned = self.right.get_signed()
        
        ldata = m.Reg(_tmp_data(tmp, prefix='_tmp_ldata_'), width, signed=lsigned, initval=0)
        rdata = m.Reg(_tmp_data(tmp, prefix='_tmp_rdata_'), width, signed=rsigned, initval=0)
        
        lval, rval = fx.adjust(self.left.sig_data, self.right.sig_data, lpoint, rpoint, signed)

        accept = vtypes.OrList(ready, vtypes.Not(valid))
        
        seq( ldata(lval), cond=accept )
        seq( rdata(rval), cond=accept )
        
        sign = vtypes.OrList(vtypes.AndList(ldata[width-1] == 0, rdata[width-1] == 0), # + , +
                             vtypes.AndList(ldata[width-1] == 1, rdata[width-1] == 1)) # - , -

        abs_ldata = m.Reg(_tmp_data(tmp, prefix='_tmp_abs_ldata_'), width, initval=0)
        abs_rdata = m.Reg(_tmp_data(tmp, prefix='_tmp_abs_rdata_'), width, initval=0)

        if not lsigned:
            seq( abs_ldata(ldata), cond=accept )
        else:
            seq( abs_ldata(vtypes.Mux(ldata[width-1] == 0, ldata, vtypes.Unot(ldata) + 1)),
                 cond=accept )
        
        if not rsigned:
            seq( abs_rdata(rdata), cond=accept )
        else:
            seq( abs_rdata(vtypes.Mux(rdata[width-1] == 0, rdata, vtypes.Unot(rdata) + 1)),
                 cond=accept )

        osign = m.Wire(_tmp_data(tmp, prefix='_tmp_osign_'))
        abs_odata = m.Wire(_tmp_data(tmp, prefix='_tmp_abs_odata_'), width, signed=signed)
        
        odata = m.Reg(_tmp_data(tmp, prefix='_tmp_odata_'), width, signed=signed, initval=0)
            
        if not signed:
            seq( odata(abs_odata), cond=accept )
        else:
            seq( odata(vtypes.Mux(osign, abs_odata, vtypes.Unot(abs_odata) + 1)),
                 cond=accept )
        
        m.Assign( data(odata) )
        
        ovalid = m.Wire(_tmp_valid(tmp, prefix='_tmp_ovalid_'))    
                    
        v = ovalid
        for i in range(3):
            nv = m.Reg(_tmp_valid(tmp, prefix='_tmp_valid_reg' + str(i) + '_'), initval=0)
            seq( nv(v), cond=accept )
            v = nv
        m.Assign( valid(v) )

        s = sign
        for i in range(self.latency):
            ns = m.Reg(_tmp_data(tmp, prefix='_tmp_sign' + str(i) + '_'), initval=0)
            seq( ns(s), cond=accept )
            s = ns
        m.Assign( osign(s) )
        
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

        enable = m.Wire(_tmp_data(tmp, prefix='_tmp_enable_') )
        update = m.Wire(_tmp_data(tmp, prefix='_tmp_update_') )
        m.Assign( enable(data_cond) )
        m.Assign( update(accept) ) # NOT valid_cond
        
        params = [ ('W_D', width) ]
        ports = [ ('CLK', clk), ('RST', rst),
                  ('update', update), ('enable', enable), ('valid', ovalid),
                  ('in_a', abs_ldata), ('in_b', abs_rdata), ('mod', abs_odata) ]
        
        m.Instance(inst, ''.join(['div', str(tmp)]), params, ports)

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

class Sll(_BinaryOperator):
    max_width = 1024
    def set_attributes(self):
        v = self.right.eval()
        if isinstance(v, int):
            return self.left.bit_length() + v
        v = 2 ** self.right.bit_length()
        ret = self.left.bit_length() + v
        if ret > self.max_width:
            raise ValueError("bit_length is too large '%d'" % ret)
        self.width = ret
        left_fp = self.left.get_point()
        self.point = left_fp
        self.signed = False
    
    def _implement(self, m, seq):
        if self.right.get_point() != 0:
            raise TypeError("shift amount must be int")
        _BinaryOperator._implement(self, m, seq)
        
    def eval(self):
        return self.left.eval() << self.right.eval()
    
class Srl(_BinaryOperator):
    def set_attributes(self):
        self.width = self.left.bit_length()
        self.point = self.left.get_point()
        self.signed = False
    
    def _implement(self, m, seq):
        if self.right.get_point() != 0:
            raise TypeError("shift amount must be int")
        _BinaryOperator._implement(self, m, seq)
        
    def eval(self):
        return self.left.eval() >> self.right.eval()
    
class Sra(_BinaryOperator):
    def set_attributes(self):
        self.width = self.left.bit_length()
        self.point = self.left.get_point()
        self.signed = self.left.get_signed()
    
    def _implement(self, m, seq):
        if self.right.get_point() != 0:
            raise TypeError("shift amount must be int")
        _BinaryOperator._implement(self, m, seq)
        
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

class LessThan(_BinaryOperator):
    def set_attributes(self):
        self.width = 1
        self.point = 0
        self.signed = False
        
    def eval(self):
        return self.left.eval() < self.right.eval()
    
class GreaterThan(_BinaryOperator):
    def set_attributes(self):
        self.width = 1
        self.point = 0
        self.signed = False
        
    def eval(self):
        return self.left.eval() > self.right.eval()
    
class LessEq(_BinaryOperator):
    def set_attributes(self):
        self.width = 1
        self.point = 0
        self.signed = False
        
    def eval(self):
        return self.left.eval() <= self.right.eval()

class GreaterEq(_BinaryOperator):
    def set_attributes(self):
        self.width = 1
        self.point = 0
        self.signed = False
        
    def eval(self):
        return self.left.eval() >= self.right.eval()

class Eq(_BinaryOperator):
    def set_attributes(self):
        self.width = 1
        self.point = 0
        self.signed = False
        
    def eval(self):
        return self.left.eval() == self.right.eval()
    
class NotEq(_BinaryOperator):
    def set_attributes(self):
        self.width = 1
        self.point = 0
        self.signed = False
        
    def eval(self):
        return self.left.eval() != self.right.eval()

class _BinaryLogicalOperator(_BinaryOperator):
    def set_attributes(self):
        left = self.left.bit_length() 
        right = self.right.bit_length()
        self.width = max(left, right)
        self.point = 0
        self.signed = False
                
    def _implement(self, m, seq):
        if self.latency != 1:
            raise ValueError("Latency mismatch '%d' vs '%s'" % (self.latency, 1))

        width = self.bit_length()
        signed = False

        tmp = m.get_tmp()
        data = m.Reg(_tmp_data(tmp), width, initval=0, signed=signed)
        valid = m.Reg(_tmp_valid(tmp), initval=0)
        ready = m.Wire(_tmp_ready(tmp))
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
        
        seq( data(self.op(ldata, rdata)), cond=data_cond )
        seq( valid(0), cond=valid_reset_cond )
        seq( valid(all_valid), cond=valid_cond )
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
        ret =  left ^ right
        if isinstance(ret, int):
            return ret == 0
        return Xnor(left, right)
    
class Or(_BinaryLogicalOperator):
    def eval(self):
        return self.left.eval() | self.right.eval()
    
class Land(_BinaryLogicalOperator):
    def eval(self):
        left = self.left.eval()
        right = self.right.eval()
        if isinstance(left, (int, bool)) and isinstance(right, (int, bool)):
            return left and right
        return Land(left, right)
    
class Lor(_BinaryLogicalOperator):
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
    def set_attributes(self):
        right = self.right.bit_length()
        self.width = right
        self.point = 0
        self.signed = False
                
class Ulnot(_UnaryLogicalOperator):
    def set_attributes(self):
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
    def set_attributes(self):
        self.width = 1
        self.point = 0
        
    def eval(self):
        right = self.right.eval()
        if isinstance(right, bool):
            return right
        if isinstance(right, int):
            width = self.right.bit_length()
            for i in range(width):
                if right & 0x1 == 0:
                    return False
                right = right >> 1
            return True
        return Uand(right)
    
class Unand(_UnaryLogicalOperator):
    def set_attributes(self):
        self.width = 1
        self.point = 0
        
    def eval(self):
        right = self.right.eval()
        if isinstance(right, bool):
            return not right
        if isinstance(right, int):
            width = self.right.bit_length()
            for i in range(width):
                if right & 0x1 == 0:
                    return True
                right = right >> 1
            return False
        return Unand(right)
    
class Uor(_UnaryLogicalOperator):
    def set_attributes(self):
        self.width = 1
        self.point = 0
        
    def eval(self):
        right = self.right.eval()
        if isinstance(right, bool):
            return right
        if isinstance(right, int):
            width = self.right.bit_length()
            for i in range(width):
                if right & 0x1 == 1:
                    return True
                right = right >> 1
            return False
        return Uor(right)
    
class Unor(_UnaryLogicalOperator):
    def set_attributes(self):
        self.width = 1
        self.point = 0
        
    def eval(self):
        right = self.right.eval()
        if isinstance(right, bool):
            return not right
        if isinstance(right, int):
            width = self.right.bit_length()
            for i in range(width):
                if right & 0x1 == 1:
                    return False
                right = right >> 1
            return True
        return Unor(right)
    
class Uxor(_UnaryLogicalOperator):
    def set_attributes(self):
        self.width = 1
        self.point = 0
        
    def eval(self):
        right = self.right.eval()
        if isinstance(right, bool):
            return right
        if isinstance(right, int):
            width = self.right.bit_length()
            ret = 1
            for i in range(width):
                ret = ret ^ (right & 0x1)
                right = right >> 1
            return ret == 1
        return Uxor(right)
    
class Uxnor(_UnaryLogicalOperator):
    def set_attributes(self):
        self.width = 1
        self.point = 0
        
    def eval(self):
        right = self.right.eval()
        if isinstance(right, bool):
            return not right
        if isinstance(right, int):
            width = self.right.bit_length()
            ret = 1
            for i in range(width):
                ret = ret ^ (right & 0x1)
                right = right >> 1
            return ret == 0
        return Uxnor(right)
        
#-------------------------------------------------------------------------------
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

#-------------------------------------------------------------------------------
class _SpecialOperator(_Operator):
    latency = 1
    def __init__(self, *args):
        _Operator.__init__(self)
        self.args = [ _to_constant(arg) for arg in args ]
        for var in self.args:
            var._add_sink(self) 
        self.op = None
        self.set_attributes()

    def set_attributes(self):
        wargs = [ arg.bit_length() for arg in self.args ]
        self.width = max(*wargs)
        pargs = [ arg.get_point() for arg in self.args ]
        self.point = max(*pargs)
        self.signed = False
        for arg in self.args:
            if arg.get_signed():
                self.signed = True
                break
                
    def _implement(self, m, seq):
        if self.latency != 1:
            raise ValueError("Latency mismatch '%d' vs '%s'" % (self.latency, 1))

        width = self.bit_length()
        signed = self.get_signed()

        tmp = m.get_tmp()
        data = m.Reg(_tmp_data(tmp), width, initval=0, signed=signed)
        valid = m.Reg(_tmp_valid(tmp), initval=0)
        ready = m.Wire(_tmp_ready(tmp))
        self.sig_data = data
        self.sig_valid = valid
        self.sig_ready = ready

        arg_data = [ arg.sig_data for arg in self.args ]
        arg_valid = [ arg.sig_valid for arg in self.args ]
        arg_ready = [ arg.sig_ready for arg in self.args ]

        all_valid = _and_vars(*arg_valid)
        all_ready = _and_vars(*arg_ready)

        accept = vtypes.OrList(ready, vtypes.Not(valid))

        valid_cond = _and_vars(accept, all_ready)
        valid_reset_cond = _and_vars(valid, ready)
        data_cond = _and_vars(valid_cond, all_valid)
        ready_cond = _and_vars(accept, all_valid)
        
        seq( data(self.op(*arg_data)), cond=data_cond )
        seq( valid(0), cond=valid_reset_cond )
        seq( valid(all_valid), cond=valid_cond )

        for r in arg_ready:
            _connect_ready(m, r, ready_cond)

        if not self._has_output():
            _connect_ready(m, ready, vtypes.Int(1))
            
#-------------------------------------------------------------------------------
class Pointer(_SpecialOperator):
    def __init__(self, var, pos):
        _SpecialOperator.__init__(self, var, pos)
        self.op = vtypes.Pointer

    def set_attributes(self):
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
        _SpecialOperator.__init__(self, var, msb, lsb)
        self.op = vtypes.Slice

    def set_attributes(self):
        self.width = self.msb - self.lsb + 1
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
    
    def set_attributes(self):
        ret = 0
        for v in self.vars:
             ret += v.bit_length() 
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
        vars = [ var.eval() for var in self.vars ]
        for var in vars:
            if not isinstance(var, int):
                return Cat(*vars)
        ret = 0
        for var in vars:
            ret = (ret << var.bit_length()) | var
        return ret
    
class Repeat(_SpecialOperator):
    def __init__(self, var, times):
        times = times.eval() if isinstance(times, _Constant) else times
        if not isinstance(times, int):
            raise TypeError('times must be int')
        _SpecialOperator.__init__(self, var, times)
        self.op = vtypes.Repeat

    def set_attributes(self):
        self.width = self.var.bit_length() * self.times.eval()
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
            ret = (ret << var.bit_length()) | var
        return ret
    
class Cond(_SpecialOperator):
    def __init__(self, condition, true_value, false_value):
        _SpecialOperator.__init__(self, condition, true_value, false_value)
        self.op = vtypes.Cond

    def set_attributes(self):
        true_value_fp = self.true_value.get_point()
        false_value_fp = self.false_value.get_point()
        true_value = self.true_value.bit_length() - true_value_fp
        false_value = self.false_value.bit_length() - false_value_fp
        self.width = max(true_value, false_value) + max(true_value_fp, false_value_fp)
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
    
#-------------------------------------------------------------------------------
class CustomOp(_SpecialOperator):
    def __init__(self, op, *vars):
        _SpecialOperator.__init__(self, *vars)
        self.op = op

    def eval(self):
        return self

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
        
    def eval(self):
        return self

    def _implement(self, m, seq):
        if self.latency != 1:
            raise ValueError("Latency mismatch '%d' vs '%s'" % (self.latency, 1))
        
        width = self.bit_length()
        signed = self.get_signed()

        tmp = m.get_tmp()
        data = m.Reg(_tmp_data(tmp), width, initval=0, signed=signed)
        valid = m.Reg(_tmp_valid(tmp), initval=0)
        ready = m.Wire(_tmp_ready(tmp))
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
        
        seq( data(rdata), cond=data_cond )
        seq( valid(0), cond=valid_reset_cond )
        seq( valid(all_valid), cond=valid_cond )
        _connect_ready(m, rready, ready_cond)
        
        if not self._has_output():
            _connect_ready(m, ready, vtypes.Int(1))

#-------------------------------------------------------------------------------
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
            raise ValueError("Latency mismatch '%d' vs '%s'" % (self.latency, 0))
        
        width = self.bit_length()
        signed = self.get_signed()

        tmp = m.get_tmp()
        data = m.Reg(_tmp_data(tmp), width, initval=0, signed=signed)
        valid = self.parent_value.sig_valid
        ready  = self.parent_value.sig_ready
        self.sig_data = data
        self.sig_valid = valid
        self.sig_ready = ready
        
        rdata = self.right.sig_data

        data_cond = _and_vars(valid, ready)
        
        seq( data(rdata), cond=data_cond )

#-------------------------------------------------------------------------------
class _Constant(_Numeric):
    def __init__(self, value):
        _Numeric.__init__(self)
        self.value = value
        self.signed = False
        self.set_attributes()
        self.sig_data = self.value

    def set_attributes(self):
        self.width = self.value.bit_length() + 1
        self.point = 0
        self.signed = False

    def eval(self):
        return self.value
        
    def _implement(self, m, seq):
        data = self.value
        valid = None
        ready = None
        self.sig_data = data
        self.sig_valid = valid
        self.sig_ready = ready

#-------------------------------------------------------------------------------
class _Variable(_Numeric):
    def __init__(self, data=None, valid=None, ready=None, width=32, point=0, signed=False):
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
    
    def _implement(self, m, seq):
        if not isinstance(self.input_data, _Numeric):
            return
        
        width = self.bit_length()
        signed = self.get_signed()

        tmp = m.get_tmp()
        data = m.Wire(_tmp_data(tmp), width, signed=signed)
        valid = m.Wire(_tmp_valid(tmp))
        ready = m.Wire(_tmp_ready(tmp))
        
        m.Assign( data(self.input_data.sig_data) )
        m.Assign( valid(self.input_data.sig_valid) )
        _connect_ready(m, self.input_data.sig_ready, ready)
            
    def _implement_input(self, m, seq, aswire=False):
        if isinstance(self.input_data, _Numeric):
            return

        type_i = m.Wire if aswire else m.Input
        type_o = m.Wire if aswire else m.Output
        
        width = self.bit_length()
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
            
#-------------------------------------------------------------------------------
class _Accumulator(_UnaryOperator):
    latency = 1
    ops = ( vtypes.Plus, )
    
    def __init__(self, right, initval=None, reset=None, width=32, signed=False):
        _UnaryOperator.__init__(self, right)
        self.initval = _to_constant(initval) if initval is not None else _to_constant(0)
        if not isinstance(self.initval, _Constant):
            raise TypeError("initval must be Constant, not '%s'" % str(type(self.initval)))
        self.reset = _to_constant(reset) if reset is not None else _to_constant(0)
        self.width = width
        self.signed = signed

    def set_attributes(self):
        self.point = self.right.get_point()
        
    def eval(self):
        return self
    
    def _implement(self, m, seq):
        if self.latency != 1:
            raise ValueError("Latency mismatch '%d' vs '%s'" % (self.latency, 1))

        initval_data = self.initval.sig_data
        #initval_valid = self.initval.sig_valid
        #initval_ready = self.initval.sig_ready
        
        width = self.bit_length()
        signed = self.get_signed()

        tmp = m.get_tmp()
        data = m.Reg(_tmp_data(tmp), width, initval=initval_data, signed=signed)
        valid = m.Reg(_tmp_valid(tmp), initval=0)
        ready = m.Wire(_tmp_ready(tmp))
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

        if not isinstance(self.reset, _Constant):
            reset_data = self.reset.sig_data
            reset_valid = self.reset.sig_valid
            reset_ready = self.reset.sig_ready
            if reset_valid is None:
                raise TypeError('Reset condition of Accumulator must have a valid port')
            data_reset_cond = _and_vars(reset_valid, reset_ready)
            seq( data(reset_data), cond=data_reset_cond )
            _connect_ready(m, reset_ready, vtypes.Int(1))
        
        seq( data(value), cond=data_cond )
        seq( valid(0), cond=valid_reset_cond )
        seq( valid(all_valid), cond=valid_cond )
        _connect_ready(m, rready, ready_cond)
        
        if not self._has_output():
            _connect_ready(m, ready, vtypes.Int(1))

class Iadd(_Accumulator):
    ops = ( vtypes.Plus, )
    def __init__(self, right, initval=0, reset=None, width=32, signed=False):
        _Accumulator.__init__(self, right, initval, reset, width, signed)

class Isub(_Accumulator):
    ops = ( vtypes.Minus, )
    def __init__(self, right, initval=0, reset=None, width=32, signed=False):
        _Accumulator.__init__(self, right, initval, reset, width, signed)

class Imul(_Accumulator):
    #latency = 6
    latency = 1 
    ops = ( vtypes.Times, )
    def __init__(self, right, initval=1, reset=None, width=32, signed=False):
        _Accumulator.__init__(self, right, initval, reset, width, signed)

class Idiv(_Accumulator):
    latency = 32
    op = ()
    def __init__(self, right, initval=1, reset=None, width=32, signed=False):
        raise NotImplementedError()
        _Accumulator.__init__(self, right, initval, reset, width, signed)

class Icustom(_Accumulator):
    def __init__(self, ops, right, initval=0, reset=None, width=32, signed=False):
        _Accumulator.__init__(self, right, initval, reset, width, signed)
        if not isinstance(ops, (tuple, list)):
            ops = tuple([ ops ])
        self.ops = ops

#-------------------------------------------------------------------------------
class Int(_Constant):
    def __init__(self, value, signed=True):
        _Constant.__init__(self, value)
        self.signed = signed
        
    def set_attributes(self):
        self.width = self.value.bit_length() + 1
        self.point = 0

    def _implement(self, m, seq):
        data = vtypes.Int(self.value, width=self.width)
        valid = None
        ready = None
        self.sig_data = data
        self.sig_valid = valid
        self.sig_ready = ready

class Float(_Constant):
    def set_attributes(self):
        self.width = 32
        self.point = 0
        self.signed = True

class FixedPoint(_Constant):
    def __init__(self, value, point=0, signed=True):
        _Constant.__init__(self, value)
        self.point = point
        self.signed = signed

    def set_attributes(self):
        self.width = self.value.bit_length() + 1
        self.point = 0

    def _implement(self, m, seq):
        data = vtypes.Int(self.value, width=self.width)
        valid = None
        ready = None
        self.sig_data = data
        self.sig_valid = valid
        self.sig_ready = ready

class Str(_Constant):
    def set_attributes(self):
        self.width = 0
        self.point = 0
        self.signed = False

#-------------------------------------------------------------------------------
def Counter(step=None, maxval=None, initval=0, reset=None, width=32, signed=False):
    if step is None:
        step = 1

    if maxval is None:
        return Iadd(step, initval=initval, reset=reset, width=width, signed=signed)

    if not isinstance(step, (int, bool)) or not isinstance(maxval, (int, bool)):
        raise TypeError("step and maxval must be int, when maxval is specified.")

    if maxval > 2 ** width:
        raise ValueError("maxval > 2 ** width")

    return Icustom(lambda a, b: vtypes.Mux(a >= maxval - step, initval, a + b),
                   step, initval=initval, reset=reset, width=width, signed=signed)

def ConditionCounter(cond, step=1, maxval=None, initval=0, reset=None, width=32, signed=False):
    val = Mux(cond, step, 0)
    return Counter(val, maxval=maxval, initval=initval, reset=reset, width=width, signed=signed)
