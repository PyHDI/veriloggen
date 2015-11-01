from __future__ import absolute_import
from __future__ import print_function

operator_dict = {
    'Uminus':'-', 'Ulnot':'!', 'Unot':'~', 'Uand':'&', 'Unand':'~&',
    'Uor':'|', 'Unor':'~|', 'Uxor':'^', 'Uxnor':'~^',
    'Power':'**', 'Times':'*', 'Divide':'/', 'Mod':'%', 
    'Plus':'+', 'Minus':'-',
    'Sll':'<<', 'Srl':'>>', 'Sra':'>>>',
    'LessThan':'<', 'GreaterThan':'>', 'LessEq':'<=', 'GreaterEq':'>=',
    'Eq':'==', 'NotEq':'!=', 'Eql':'===', 'NotEql':'!==',
    'And':'&', 'Xor':'^', 'Xnor':'~^',
    'Or':'|', 'Land':'&&', 'Lor':'||'
    }

def op2mark(op):
    return operator_dict[op]

#-------------------------------------------------------------------------------
class VeriloggenNode(object):
    """ Base class of Veriloggen AST object """
    def __lt__(self, r):
        raise TypeError('Not allowed operation.')
    
    def __le__(self, r):
        raise TypeError('Not allowed operation.')
    
    #def __eq__(self, r):
    #    raise TypeError('Not allowed operation.')
    
    #def __ne__(self, r):
    #    raise TypeError('Not allowed operation.')

    def __ge__(self, r):
        raise TypeError('Not allowed operation.')
    
    def __gt__(self, r):
        raise TypeError('Not allowed operation.')

    def __add__(self, r):
        raise TypeError('Not allowed operation.')
    
    def __sub__(self, r):
        raise TypeError('Not allowed operation.')
    
    def __pow__(self, r):
        raise TypeError('Not allowed operation.')
    
    def __mul__(self, r):
        raise TypeError('Not allowed operation.')
    
    def __div__(self, r):
        raise TypeError('Not allowed operation.')
    
    def __truediv__(self, r):
        raise TypeError('Not allowed operation.')
    
    def __and__(self, r):
        raise TypeError('Not allowed operation.')

    def __or__(self, r):
        raise TypeError('Not allowed operation.')
    
    def __xor__(self, r):
        raise TypeError('Not allowed operation.')
    
    def __lshift__(self, r):
        raise TypeError('Not allowed operation.')

    def __rshift__(self, r):
        raise TypeError('Not allowed operation.')

    def __neg__(self):
        raise TypeError('Not allowed operation.')
    
    def __pos__(self):
        raise TypeError('Not allowed operation.')
    
    def __getitem__(self, r):
        raise TypeError('Not allowed operation.')

#-------------------------------------------------------------------------------
class _Numeric(VeriloggenNode):
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
class _Variable(_Numeric):
    def __init__(self, name, width=1, length=None, signed=False, value=None, initval=None):
        self.name = name
        self.width = width
        self.length = length
        self.signed = signed
        self.value = value
        self.initval = initval
        self.subst = []
    
    def __call__(self, r, ldelay=None, rdelay=None):
        return self.next(r, ldelay, rdelay)

    def next(self, r, ldelay=None, rdelay=None):
        return Subst(self, r, ldelay=ldelay, rdelay=rdelay)
    
    def connect(self, prefix='', postfix=''):
        return ( prefix + self.name + postfix, self )

    def reset(self):
        return None

    def add_subst(self, s):
        self.subst.append(s)

    def get_subst(self):
        return self.subst
    
    def bit_length(self):
        return self.width

    def __str__(self):
        return self.name

#-------------------------------------------------------------------------------
class Input(_Variable): pass
class Output(_Variable): pass
class Inout(_Variable): pass
class Tri(_Variable): pass

class Reg(_Variable):
    def reset(self):
        if self.initval is None:
            return None
        return self.next(self.initval)
    def add(self, r):
        return Subst(self, Plus(self, r))
    def sub(self, r):
        return Subst(self, Minus(self, r))
    def inc(self):
        return self.add(1)
    def dec(self):
        return self.sub(1)
    
class Wire(_Variable):
    def add_subst(self, s):
        if len(self.subst) > 0:
            raise ValueError('Wire %s is already assigned.' % self.name)
        self.subst.append(s)
    
class Integer(_Variable):
    def reset(self):
        if self.initval is None:
            return None
        return self.next(self.initval)
    def add(self, r):
        return Subst(self, Plus(self, r))
    def sub(self, r):
        return Subst(self, Minus(self, r))
    def inc(self):
        return self.add(1)
    def dec(self):
        return self.sub(1)
    
class Real(_Variable):
    def reset(self):
        if self.initval is None:
            return None
        return self.next(self.initval)
    def add(self, r):
        return Subst(self, Plus(self, r))
    def sub(self, r):
        return Subst(self, Minus(self, r))
    def inc(self):
        return self.add(1)
    def dec(self):
        return self.sub(1)
    
class Genvar(_Variable):
    def add(self, r):
        return Subst(self, Plus(self, r))
    def sub(self, r):
        return Subst(self, Minus(self, r))
    def inc(self):
        return self.add(1)
    def dec(self):
        return self.sub(1)

# for undetermined identifier
class AnyType(_Variable): pass

#-------------------------------------------------------------------------------
class _ParameterVairable(_Variable):
    def __init__(self, name, value, width=None, signed=False):
        if isinstance(value, _ParameterVairable):
            value = value.value
        _Variable.__init__(self, name, width=width, signed=signed, value=value)
        
class Parameter(_ParameterVairable): pass
class Localparam(_ParameterVairable): pass
class Supply(_ParameterVairable): pass

#-------------------------------------------------------------------------------
class _Constant(_Numeric):
    def __init__(self, value, width=None, base=None):
        self._type_check_value(value)
        self._type_check_width(width)
        self._type_check_base(base)
    def _type_check_value(self, value): pass
    def _type_check_width(self, width): pass
    def _type_check_base(self, base): pass

    def __str__(self):
        return str(value)
        
class Int(_Constant):
    def __init__(self, value, width=None, base=None, signed=False):
        _Constant.__init__(self, value, width, base)
        self.value = value
        self.width = width
        self.base = base
        self.signed = signed

    def _type_check_value(self, value):
        if not isinstance(value, int):
            raise TypeError('value of Int must be int, not %s.' % type(value))

    def _type_check_width(self, width):
        if width is None: return
        if not isinstance(width, int):
            raise TypeError('width of Int must be int, not %s.' % type(width))

    def _type_check_base(self, base):
        if base is None: return 
        if not isinstance(base, int):
            raise TypeError('base of Int must be int, not %s.' % type(base))

    def __str__(self):
        value_list = []
        if node.width:
            value_list.append(str(node.width))
            
        if node.base is None:
            if node.signed:
                value_list.append("'sd")
            elif node.width:
                value_list.append("'d")
            value_list.append(str(node.value))
        elif node.base == 2:
            if node.signed:
                value_list.append("'sb")
            else:
                value_list.append("'b")
            value_list.append(bin(node.value).replace('0b', ''))
        elif node.base == 8:
            if node.signed:
                value_list.append("'so")
            else:
                value_list.append("'o")
            value_list.append(oct(node.value).replace('0o', ''))
        elif node.base == 10:
            if node.signed:
                value_list.append("'sd")
            else:
                value_list.append("'d")
            value_list.append(str(node.value))
        elif node.base == 16:
            if node.signed:
                value_list.append("'sh")
            else:
                value_list.append("'h")
            value_list.append(hex(node.value).replace('0x', ''))
        else:
            raise ValueError("Int.base must be 2, 8, 10, or 16")

        return ''.join(value_list)

class IntX(Int):
    def __init__(self, width=None, base=None, signed=False):
        _Constant.__init__(self, None, width, base)
        self.value = 'x'
        self.width = width
        self.base = base
        self.signed = signed
    
    def _type_check_value(self, value):
        pass

    def __str__(self):
        value_list = []
        if node.width:
            value_list.append(str(node.width))
            
        if node.base is None:
            if node.signed:
                value_list.append("'sd")
            else:
                value_list.append("'d")
            value_list.append(node.value)
        elif node.base == 2:
            if node.signed:
                value_list.append("'sb")
            else:
                value_list.append("'b")
            value_list.append(node.value)
        elif node.base == 8:
            if node.signed:
                value_list.append("'so")
            else:
                value_list.append("'o")
            value_list.append(node.value)
        elif node.base == 10:
            if node.signed:
                value_list.append("'sd")
            else:
                value_list.append("'d")
            value_list.append(node.value)
        elif node.base == 16:
            if node.signed:
                value_list.append("'sh")
            else:
                value_list.append("'h")
            value_list.append(node.value)
        else:
            raise ValueError("Int.base must be 2, 8, 10, or 16")

        return ''.join(value_list)

class IntZ(Int):
    def __init__(self, width=None, base=None, signed=False):
        _Constant.__init__(self, None, width, base)
        self.value = 'z'
        self.width = width
        self.base = base
        self.signed = False
    
    def _type_check_value(self, value):
        pass

    def __str__(self):
        value_list = []
        if node.width:
            value_list.append(str(node.width))
            
        if node.base is None:
            if node.signed:
                value_list.append("'sd")
            else:
                value_list.append("'d")
            value_list.append(node.value)
        elif node.base == 2:
            if node.signed:
                value_list.append("'sb")
            else:
                value_list.append("'b")
            value_list.append(node.value)
        elif node.base == 8:
            if node.signed:
                value_list.append("'so")
            else:
                value_list.append("'o")
            value_list.append(node.value)
        elif node.base == 10:
            if node.signed:
                value_list.append("'sd")
            else:
                value_list.append("'d")
            value_list.append(node.value)
        elif node.base == 16:
            if node.signed:
                value_list.append("'sh")
            else:
                value_list.append("'h")
            value_list.append(node.value)
        else:
            raise ValueError("Int.base must be 2, 8, 10, or 16")

        return ''.join(value_list)

class Float(_Constant):
    def __init__(self, value):
        _Constant.__init__(self, value, None, None)
        self.value = value

    def _type_check_value(self, value):
        if not isinstance(value, (float, int)):
            raise TypeError('value of Float must be float, not %s.' % type(value))

    def __str__(self):
        return str(node.value)

class Str(_Constant):
    def __init__(self, value):
        _Constant.__init__(self, value, None, None)
        self.value = value

    def _type_check_value(self, value):
        if not isinstance(value, str):
            raise TypeError('value of Str must be str, not %s.' % type(value))

    def __str__(self):
        return str(node.value)

#-------------------------------------------------------------------------------
class _Operator(_Numeric): pass
    
#-------------------------------------------------------------------------------
class _BinaryOperator(_Operator):
    def __init__(self, left, right):
        self._type_check(left, right)
        self.left = left
        self.right = right

    def _type_check(self, left, right):
        if not isinstance(left, (_Numeric, bool, int, float, str)):
            raise TypeError('BinaryOperator does not support Type %s' % str(type(left)))
        if not isinstance(right, (_Numeric, bool, int, float, str)):
            raise TypeError('BinaryOperator does not support Type %s' % str(type(right)))

    def __str__(self):
        return ''.join(['(', str(self.left), ' ', op2mark(self.__class__.__name__), ' ',
                         str(self.right), ')'])

class _UnaryOperator(_Operator):
    def __init__(self, right):
        self._type_check(right)
        self.right = right
        
    def _type_check(self, right):
        if not isinstance(right, (_Numeric, bool, int, float, str)):
            raise TypeError('BinaryOperator does not support Type %s' % str(type(right)))

    def __str__(self):
        return ''.join(['(', op2mark(self.__class__.__name__), str(self.right), ')'])

#-------------------------------------------------------------------------------
# class names must be same the ones in pyverilog.vparser.ast
class Power(_BinaryOperator): pass
class Times(_BinaryOperator): pass
class Divide(_BinaryOperator): pass
class Mod(_BinaryOperator): pass

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

#-------------------------------------------------------------------------------
class _SpecialOperator(_Operator):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

#-------------------------------------------------------------------------------
class Pointer(_SpecialOperator):
    def __init__(self, var, pos):
        self.var = var
        self.pos = pos
        self.subst = []
        
    def __call__(self, r):
        return self.next(r)

    def next(self, r):
        return Subst(self, r)

    def add_subst(self, s):
        self.subst.append(s)
    
    def bit_length(self):
        if isinstance(var, _Variable) and var.length is not None:
            return self.var.bit_length()
        return 1
    
    def __str__(self):
        return ''.join([str(self.var), '[', str(self.pos), ']'])

class Slice(_SpecialOperator):
    def __init__(self, var, msb, lsb):
        self.var = var
        self.msb = msb
        self.lsb = lsb
        self.subst = []

    def __call__(self, r):
        return self.next(r)

    def next(self, r):
        return Subst(self, r)
    
    def add_subst(self, s):
        self.subst.append(s)
    
    def bit_length(self):
        return self.msb - self.lsb + 1
    
    def __str__(self):
        return ''.join([str(self.var), '[', str(self.msb), ':', str(self.lsb), ']'])

class Cat(_SpecialOperator):
    def __init__(self, *vars):
        self.vars = tuple(vars)
        self.subst = []
    
    def __call__(self, r):
        return self.next(r)

    def next(self, r):
        return Subst(self, r)

    def add_subst(self, s):
        self.subst.append(s)
    
    def bit_length(self):
        values = [ v.bit_length() for v in self.vars ]
        ret = values[0]
        for v in values[1:]:
            ret = ret + v
        return ret
    
    def __str__(self):
        ret = []
        ret.append('{')
        for v in self.vars:
            ret.append(str(v))
            ret.append(', ')
        ret.pop()
        ret.append('}')
        return ''.join(ret)
       
class Repeat(_SpecialOperator):
    def __init__(self, var, times):
        self.var = var
        self.times = times

    def bit_length(self):
        return self.var.bit_length() * self.times
        
    def __str__(self):
        return ''.join(['{', str(self.times), '{', str(self.var), '}}'])
       
#-------------------------------------------------------------------------------
class Cond(_SpecialOperator):
    def __init__(self, condition, true_value, false_value):
        self.condition = condition
        self.true_value = true_value
        self.false_value = false_value
        
    def bit_length(self):
        raise NotImplementedError('bit_length is not implemented on Cond.')
        
    def __str__(self):
        return ''.join(['(', str(self.condition), ')?', str(self.true_value), ' : ', str(self.false_value)])
       
#-------------------------------------------------------------------------------
class Sensitive(VeriloggenNode):
    def __init__(self, name):
        self.name = name

#-------------------------------------------------------------------------------
class Posedge(Sensitive): pass
class Negedge(Sensitive): pass

#-------------------------------------------------------------------------------
class SensitiveAll(Sensitive):
    def __init__(self):
        Sensitive.__init__('all')

#-------------------------------------------------------------------------------
class Subst(VeriloggenNode):
    def __init__(self, left, right, blk=False, ldelay=None, rdelay=None):
        self.left = left
        self.right = right
        self.blk = blk
        self.ldelay = ldelay
        self.rdelay = rdelay
        self.left.add_subst(self)

    def overwrite_right(self, right):
        self.right = right
        
    def __str__(self):
        return ''.join([str(self.left), ' <- ', str(self.right)])

#-------------------------------------------------------------------------------
class Always(VeriloggenNode):
    def __init__(self, *sensitivity):
        self.sensitivity = tuple(sensitivity)
        self.statement = None

    def __call__(self, *statement):
        return self.set_statement(*statement)

    def set_statement(self, *statement):
        if self.statement is not None:
            raise ValueError("Statement is already assigned.")
        self.statement = tuple(statement)
        return self
    
#-------------------------------------------------------------------------------
class Assign(VeriloggenNode):
    def __init__(self, statement):
        self.statement = statement

#-------------------------------------------------------------------------------
class Initial(VeriloggenNode):
    def __init__(self, *statement):
        self.statement = tuple(statement)

    def add(self, *statement):
        if self.statement is None:
            return self.set_statement(*statement)
        self.statement = tuple(self.statement + statement)
        return self

#-------------------------------------------------------------------------------
class If(VeriloggenNode):
    def __init__(self, condition):
        self.condition = condition
        self.true_statement = None
        self.false_statement = None

    def __call__(self, *args):
        if self.true_statement is None:
            return self.set_true_statement(*args)
        if self.false_statement is None:
            return self.set_false_statement(*args)
        raise ValueError("True statement and False statement are already assigned.")

    def set_true_statement(self, *statement):
        self.true_statement = tuple(statement)
        return self
    
    def set_false_statement(self, *statement):
        self.false_statement = tuple(statement)
        return self
    
    def Else(self, *statement):
        if self.false_statement is None:
            return self.set_false_statement(*statement)
        raise ValueError("False statement is already assigned.")
        
#-------------------------------------------------------------------------------
class For(VeriloggenNode):
    def __init__(self, pre, condition, post):
        self.pre = pre
        self.condition = condition
        self.post = post
        self.statement = None

    def __call__(self, *args):
        if self.statement is None:
            return self.set_statement(*args)
        raise ValueError("Statement body is already assigned.")

    def set_statement(self, *statement):
        self.statement = tuple(statement)
        return self

    def add(self, *statement):
        if self.statement is None:
            return self.set_statement(*statement)
        self.statement = tuple(self.statement + statement)
        return self

#-------------------------------------------------------------------------------
class While(VeriloggenNode):
    def __init__(self, condition):
        self.condition = condition
        self.statement = None

    def __call__(self, *args):
        if self.statement is None:
            return self.set_statement(*args)
        raise ValueError("Statement body is already assigned.")

    def set_statement(self, *statement):
        self.statement = tuple(statement)
        return self
    
    def add(self, *statement):
        if self.statement is None:
            return self.set_statement(*statement)
        self.statement = tuple(self.statement + statement)
        return self
    
#-------------------------------------------------------------------------------
class Case(VeriloggenNode):
    def __init__(self, comp):
        self.comp = comp
        self.statement = None
        self.last = False
        
    def __call__(self, *args):
        if self.statement is None:
            return self.set_statement(*args)
        raise ValueError("Case statement list is already assigned.")

    def _type_check_statement(self, *statement):
        for s in statement:
            if not isinstance(s, When):
                raise TypeError("Case statement requires When() object as statement list.")
            if self.last:
                raise ValueError("When() with None condition must be last.")
            if s.condition is None:
                self.last = True
    
    def set_statement(self, *statement):
        self._type_check_statement(*statement)
        self.statement = tuple(statement)
        return self

    def add(self, *statement):
        if self.statement is None:
            return self.set_statement(*statement)
        self._type_check_statement(*statement)
        self.statement = tuple(self.statement + statement)
        return self

class Casex(Case): pass
    
class When(VeriloggenNode) :
    def __init__(self, *condition):
        self._type_check_condition(*condition)
        self.condition = None if len(condition) == 0 or condition[0] is None else tuple(condition)
        self.statement = None

    def __call__(self, *args):
        if self.statement is None:
            return self.set_statement(*args)
        raise ValueError("Statement body is already assigned.")

    def _type_check_condition(self, *args):
        if len(args) == 0:
            return
        if len(args) == 1 and args[0] is None:
            return
        for i, a in enumerate(args):        
            if a is None:
                raise ValueError("None condition must not mixed in When() statement.")
            if isinstance(a, (_Numeric, bool, int, float, str)): continue
            raise TypeError("Condition must be _Numeric object, not '%s'" % str(type(a)))
    
    def _type_check_statement(self, *args):
        pass
    
    def set_statement(self, *statement):
        self._type_check_statement(*statement)
        self.statement = tuple(statement)
        return self
    
    def add(self, *statement):
        if self.statement is None:
            return self.set_statement(*statement)
        self._type_check_statement(*statement)
        self.statement = tuple(self.statement + statement)
        return self
    
#-------------------------------------------------------------------------------
class ScopeIndex(VeriloggenNode):
    def __init__(self, name, index):
        self.name = name
        self.index = index
        
class Scope(_Numeric):
    def __init__(self, *args):
        self.args = tuple(args)
        if not args:
            raise ValueError("Scope requires at least one argument.")

#-------------------------------------------------------------------------------
class SystemTask(_Numeric):
    def __init__(self, cmd, *args):
        self.cmd = cmd
        self.args = tuple(args)
        
def Systask(cmd, *args):
    return SingleStatement(SystemTask(cmd, *args))

#-------------------------------------------------------------------------------
class Event(VeriloggenNode):
    def __init__(self, *sensitivity):
        self.sensitivity = sensitivity

class Wait(VeriloggenNode):
    def __init__(self, condition):
        self.condition = condition
        self.statement = None

    def __call__(self, *statement):
        return self.set_statement(*statement)

    def set_statement(self, *statement):
        if self.statement is not None:
            raise ValueError("Statement is already assigned.")
        self.statement = tuple(statement)
        return self
        
class Forever(VeriloggenNode):
    def __init__(self, *statement):
        self.statement = tuple(statement)

class Delay(VeriloggenNode):
    def __init__(self, value):
        self.value = value

#-------------------------------------------------------------------------------
class SingleStatement(VeriloggenNode):
    def __init__(self, statement):
        self.statement = statement

