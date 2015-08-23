from __future__ import absolute_import
from __future__ import print_function

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

#-------------------------------------------------------------------------------
class _Variable(_Numeric):
    def __init__(self, name, width=1, length=None, signed=False, value=None, initvalue=None):
        self.name = name
        self.width = width
        self.length = length
        self.signed = signed
        self.value = value
        self.initvalue = initvalue
    
    def __call__(self, r):
        return self.next(r)

    def next(self, r):
        return Subst(self, r)
    
    def connect(self, prefix='', postfix=''):
        return ( prefix + self.name + postfix, self )
        
#-------------------------------------------------------------------------------
class Input(_Variable): pass
class Output(_Variable): pass
class Inout(_Variable): pass
class Tri(_Variable): pass
class Reg(_Variable): pass
class Wire(_Variable): pass
class Integer(_Variable): pass
class Real(_Variable): pass
class Genvar(_Variable): pass

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
        self.type_check_value(value)
        self.type_check_width(width)
        self.type_check_base(base)
    def type_check_value(self, value): pass
    def type_check_width(self, width): pass
    def type_check_base(self, base): pass

class Int(_Constant):
    def __init__(self, value, width=None, base=None, signed=False):
        _Constant.__init__(self, value, width, base)
        self.value = value
        self.width = width
        self.base = base
        self.signed = False

    def type_check_value(self, value):
        if not isinstance(value, int):
            raise TypeError('value of Int must be int, not %s.' % type(value))

    def type_check_width(self, width):
        if width is None: return
        if not isinstance(width, int):
            raise TypeError('width of Int must be int, not %s.' % type(width))

    def type_check_base(self, base):
        if base is None: return 
        if not isinstance(base, int):
            raise TypeError('base of Int must be int, not %s.' % type(base))

class Float(_Constant):
    def __init__(self, value):
        _Constant.__init__(self, value, None, None)
        self.value = value

    def type_check_value(self, value):
        if not isinstance(value, (float, int)):
            raise TypeError('value of Float must be float, not %s.' % type(value))

class Str(_Constant):
    def __init__(self, value):
        _Constant.__init__(self, value, None, None)
        self.value = value

    def type_check_value(self, value):
        if not isinstance(value, str):
            raise TypeError('value of Str must be str, not %s.' % type(value))

#-------------------------------------------------------------------------------
class _Operator(_Numeric): pass
    
#-------------------------------------------------------------------------------
class _BinaryOperator(_Operator):
    def __init__(self, left, right):
        self.left = left
        self.right = right

class _UnaryOperator(_Operator):
    def __init__(self, right):
        self.right = right
        
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
        
    def __call__(self, r):
        return self.next(r)

    def next(self, r):
        return Subst(self, r)
    
class Slice(_SpecialOperator):
    def __init__(self, var, msb, lsb):
        self.var = var
        self.msb = msb
        self.lsb = lsb

    def __call__(self, r):
        return self.next(r)

    def next(self, r):
        return Subst(self, r)
    
class Cat(_SpecialOperator):
    def __init__(self, *vars):
        self.vars = vars
    
    def __call__(self, r):
        return self.next(r)

    def next(self, r):
        return Subst(self, r)
    
class Repeat(_SpecialOperator):
    def __init__(self, var, times):
        self.var = var
        self.times = times

#-------------------------------------------------------------------------------
class Cond(_SpecialOperator):
    def __init__(self, condition, true_value, false_value):
        self.condition = condition
        self.true_value = true_value
        self.false_value = false_value
        
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

#-------------------------------------------------------------------------------
class Always(VeriloggenNode):
    def __init__(self, sensitivity):
        self.sensitivity = sensitivity
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
        self.statement = statement

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
        self.statement = tuple(list(self.statement).extend(*statement))
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
        self.statement = tuple(list(self.statement).extend(*statement))
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

    def type_check_statement(self, *statement):
        for s in statement:
            if not isinstance(s, When):
                raise TypeError("Case statement requires When() object as statement list.")
            if self.last:
                raise ValueError("When() with None condition must be last.")
            if s.condition is None:
                self.last = True
    
    def set_statement(self, *statement):
        self.type_check_statement(*statement)
        self.statement = tuple(statement)
        return self

    def add(self, *statement):
        if self.statement is None:
            return self.set_statement(*statement)
        self.type_check_statement(*statement)
        self.statement = tuple(list(self.statement).extend(*statement))
        return self

class Casex(Case): pass
    
class When(VeriloggenNode) :
    def __init__(self, *condition):
        self.type_check_condition(*condition)
        self.condition = None if len(condition) == 0 or condition[0] is None else condition
        self.statement = None

    def __call__(self, *args):
        if self.statement is None:
            return self.set_statement(*args)
        raise ValueError("Statement body is already assigned.")

    def type_check_condition(self, *args):
        if len(args) == 0:
            return
        if len(args) == 1 and args[0] is None:
            return
        for i, a in enumerate(args):        
            if a is None:
                raise ValueError("None condition must not mixed in When() statement.")
            if isinstance(a, (_Numeric, int, float, str)): continue
            raise TypeError("Condition must be _Numeric object, not '%s'" % str(type(a)))
    
    def type_check_statement(self, *args):
        pass
    
    def set_statement(self, *statement):
        self.type_check_statement(*statement)
        self.statement = tuple(statement)
        return self
    
    def add(self, *statement):
        if self.statement is None:
            return self.set_statement(*statement)
        self.type_check_statement(*statement)
        self.statement = tuple(list(self.statement).extend(*statement))
        return self
    
#-------------------------------------------------------------------------------
class ScopeIndex(VeriloggenNode):
    def __init__(self, name, index):
        self.name = name
        self.index = index
        
class Scope(_Numeric):
    def __init__(self, *args):
        self.args = args
        if not args:
            raise ValueError("Scope requires at least one argument.")

#-------------------------------------------------------------------------------
class SystemTask(_Numeric):
    def __init__(self, cmd, *args):
        self.cmd = cmd
        self.args = args
        
def SystemStatement(cmd, *args):
    return SingleStatement(SystemTask(cmd, *args))

#-------------------------------------------------------------------------------
class SingleStatement(VeriloggenNode):
    def __init__(self, statement):
        self.statement = statement

#-------------------------------------------------------------------------------
class Event(VeriloggenNode):
    def __init__(self, sensitivity):
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
        self.statement = statement

class Delay(VeriloggenNode):
    def __init__(self, value):
        self.value = value
