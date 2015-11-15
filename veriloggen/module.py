from __future__ import absolute_import
from __future__ import print_function
import os
import sys
import collections
import copy

import veriloggen.vtypes as vtypes
import veriloggen.function as function
import veriloggen.task as task

#-------------------------------------------------------------------------------
class Module(vtypes.VeriloggenNode):
    """ Verilog Module class """
    def __init__(self, name=None, tmp_prefix='_tmp'):
        self.name = name if name is not None else self.__class__.__name__
        self.io_variable = collections.OrderedDict()
        self.variable = collections.OrderedDict()
        self.global_constant = collections.OrderedDict()
        self.local_constant = collections.OrderedDict()
        self.function = collections.OrderedDict()
        self.task = collections.OrderedDict()
        self.assign = []
        self.always = []
        self.initial = []
        self.instance = collections.OrderedDict()
        self.submodule = collections.OrderedDict()
        self.generate = collections.OrderedDict()
        self.items = []
        self.tmp_prefix = tmp_prefix
        self.tmp_count = 0
        self.hook = []
        
    #---------------------------------------------------------------------------
    # User interface for variables
    #---------------------------------------------------------------------------
    def Input(self, name, width=None, length=None, signed=False, value=None):
        t = vtypes.Input(name, width, length, signed, value)
        self.io_variable[name] = t
        self.items.append(t)
        return t
    
    def Output(self, name, width=None, length=None, signed=False, value=None):
        t = vtypes.Output(name, width, length, signed, value)
        self.io_variable[name] = t
        self.items.append(t)
        return t
    
    def OutputReg(self, name, width=None, length=None, signed=False, value=None, initval=None):
        t = vtypes.Output(name, width, length, signed, value)
        self.io_variable[name] = t
        self.items.append(t)
        t = vtypes.Reg(name, width, length, signed, value, initval)
        self.variable[name] = t
        self.items.append(t)
        return t
    
    def Inout(self, name, width=None, length=None, signed=False, value=None):
        t = vtypes.Inout(name, width, length, signed, value)
        self.io_variable[name] = t
        self.items.append(t)
        return t

    def Wire(self, name, width=None, length=None, signed=False, value=None):
        t = vtypes.Wire(name, width, length, signed, value)
        self.variable[name] = t
        self.items.append(t)
        return t
    
    def TmpWire(self, width=None, length=None, signed=False, value=None):
        name = '_'.join([self.tmp_prefix, str(self.tmp_count)])
        self.tmp_count += 1
        return self.Wire(name, width, length, signed, value)

    def Reg(self, name, width=None, length=None, signed=False, value=None, initval=None):
        t = vtypes.Reg(name, width, length, signed, value, initval)
        self.variable[name] = t
        self.items.append(t)
        return t
    
    def TmpReg(self, width=None, length=None, signed=False, value=None, initval=None):
        name = '_'.join([self.tmp_prefix, str(self.tmp_count)])
        self.tmp_count += 1
        return self.Reg(name, width, length, signed, value, initval)

    def Integer(self, name, width=None, length=None, signed=False, value=None, initval=None):
        t = vtypes.Integer(name, width, length, signed, value, initval)
        self.variable[name] = t
        self.items.append(t)
        return t
    
    def TmpInteger(self, width=None, length=None, signed=False, value=None, initval=None):
        name = '_'.join([self.tmp_prefix, str(self.tmp_count)])
        self.tmp_count += 1
        return self.Integer(name, width, length, signed, value, initval)

    def Real(self, name, width=None, length=None, signed=False, value=None, initval=None):
        t = vtypes.Real(name, width, length, signed, value, initval)
        self.variable[name] = t
        self.items.append(t)
        return t
    
    def TmpReal(self, width=None, length=None, signed=False, value=None, initval=None):
        name = '_'.join([self.tmp_prefix, str(self.tmp_count)])
        self.tmp_count += 1
        return self.Real(name, width, length, signed, value, initval)

    def Genvar(self, name, width=None, length=None, signed=False, value=None):
        t = vtypes.Genvar(name, width, length, signed, value)
        self.variable[name] = t
        self.items.append(t)
        return t
    
    def TmpGenvar(self, width=None, length=None, signed=False, value=None):
        name = '_'.join([self.tmp_prefix, str(self.tmp_count)])
        self.tmp_count += 1
        return self.Genvar(name, width, length, signed, value)

    def Parameter(self, name, value, width=None, signed=False, length=None):
        t = vtypes.Parameter(name, value, width, signed)
        self.global_constant[name] = t
        self.items.append(t)
        return t
    
    def Localparam(self, name, value, width=None, signed=False, length=None):
        t = vtypes.Localparam(name, value, width, signed)
        self.local_constant[name] = t
        self.items.append(t)
        return t

    def TmpLocalparam(self, value, width=None, signed=False, length=None):
        name = '_'.join([self.tmp_prefix, str(self.tmp_count)])
        self.tmp_count += 1
        return self.Localparam(name, value, width, signed, length)

    #---------------------------------------------------------------------------
    # User interface for control statements
    #---------------------------------------------------------------------------
    def Always(self, *sensitivity):
        t = vtypes.Always(*sensitivity)
        self.always.append(t)
        self.items.append(t)
        return t
    
    def Assign(self, statement):
        t = vtypes.Assign(statement)
        self.assign.append(t)
        self.items.append(t)
        return t

    def Initial(self, *statement):
        t = vtypes.Initial(*statement)
        self.initial.append(t)
        self.items.append(t)
        return t
    
    def Function(self, name, width=1):
        t = function.Function(name, width)
        self.function[name] = t
        self.items.append(t)
        return t
        
    def Task(self, name, width=1):
        t = task.Task(name, width)
        self.task[name] = t
        self.items.append(t)
        return t
        
    #---------------------------------------------------------------------------
    def GenerateFor(self, pre, cond, post, scope=None):
        t = GenerateFor(pre, cond, post, scope)
        if scope is None:
            if None not in self.generate: self.generate[None] = []
            self.generate[None].append(t)
            return
        if scope in self.generate:
            raise ValueError("scope '%s' is already defined." % scope)
        self.generate[scope] = t
        self.items.append(t)
        return t
            
    def GenerateIf(self, cond, scope=None):
        t = GenerateIf(cond, scope)
        if scope is None:
            if None not in self.generate: self.generate[None] = []
            self.generate[None].append(t)
            return
        if scope in self.generate:
            raise ValueError("scope '%s' is already defined." % scope)
        self.generate[scope] = t
        self.items.append(t)
        return t
            
    #---------------------------------------------------------------------------
    def Instance(self, module, instname, params=None, ports=None):
        if isinstance(module, str): module = StubModule(module)
        if not isinstance(module, (Module, StubModule, str)):
            raise TypeError('"module" of Instance must be Module, StubModule, or str, not %s'
                            % type(module))
        t = Instance(module, instname, params, ports)
        self.instance[instname] = t
        self.items.append(t)
        if isinstance(module, StubModule):
            return None
        self.submodule[module.name] = module
        return t
    
    #---------------------------------------------------------------------------
    # User intarface for reset assignments
    #---------------------------------------------------------------------------
    def make_reset(self):
        ret = []
        for vname, var in self.variable.items():
            r = var.reset()
            if r: ret.append(r)
        return tuple(ret)

    #---------------------------------------------------------------------------
    # User interface for accessing internal information
    #---------------------------------------------------------------------------
    def get_params(self):
        return list(self.global_constant.values())
    
    def get_localparams(self):
        return list(self.constant.values())
    
    def get_ports(self):
        return list(self.io_variable.values())
    
    def get_vars(self):
        return list(self.variable.values())
    
    #---------------------------------------------------------------------------
    def copy_params(self, src):
        ret = collections.OrderedDict()
        for key, obj in src.global_constant.items():
            copy_obj = copy.deepcopy(obj)
            self.add_object( copy_obj )
            ret[key] = copy_obj
        return ret
    
    def copy_localparams(self, src):
        ret = collections.OrderedDict()
        for key, obj in src.constant.items():
            copy_obj = copy.deepcopy(obj)
            self.add_object( copy_obj )
            ret[key] = copy_obj
        return ret
    
    def copy_ports(self, src):
        ret = collections.OrderedDict()
        for key, obj in src.io_variable.items():
            copy_obj = copy.deepcopy(obj)
            self.add_object( copy_obj )
            ret[key] = copy_obj
        return ret

    def copy_vars(self, src):
        ret = collections.OrderedDict()
        for key, obj in src.variable.items():
            copy_obj = copy.deepcopy(obj)
            self.add_object( copy_obj )
            ret[key] = copy_obj
        return ret

    def copy_sim_ports(self, src):
        ret = collections.OrderedDict()
        for key, obj in src.io_variable.items():
            copy_obj = self.get_corresponding_variable(obj)(key, copy.deepcopy(obj.width))
            self.add_object( copy_obj )
            ret[key] = copy_obj
        return ret

    #---------------------------------------------------------------------------
    def connect_params(self, targ, strict=False):
        ret = []
        for key, obj in targ.global_constant.items():
            if strict and (key not in self.global_constant) and (key not in self.constant):
                raise IndexError("No such constant '%s' in module '%s'" % (key, self.name))
            if key in self.global_constant:
                ret.append( (key, self.global_constant[key]) )
            elif key in self.constant:
                ret.append( (key, self.constant[key]) )
        return tuple(ret)
    
    def connect_ports(self, targ, strict=False):
        ret = []
        for key, obj in targ.io_variable.items():
            if strict and (key not in self.io_variable) and (key not in self.variable):
                raise IndexError("No such IO '%s' in module '%s'" % (key, self.name))
            if key in self.io_variable:
                ret.append( (key, self.io_variable[key]) )
            elif key in self.variable:
                ret.append( (key, self.variable[key]) )
        return tuple(ret)
    
    #---------------------------------------------------------------------------
    # User interface for Verilog code generation
    #---------------------------------------------------------------------------
    def to_verilog(self, filename=None):
        import veriloggen.to_verilog as to_verilog
        obj = self.to_hook_resolved_obj()
        return to_verilog.write_verilog(obj, filename)

    def add_hook(self, method, args=None, kwargs=None):
        """ add a hooked method to 'to_verilog()' """
        self.hook.append( (method, args, kwargs) )

    #---------------------------------------------------------------------------
    # Internal methods
    #---------------------------------------------------------------------------
    def add_object(self, obj):
        self.items.append(obj)
        
        if isinstance(obj, (vtypes.Input, vtypes.Output, vtypes.Inout)):
            self.io_variable[obj.name] = obj
            # no return here
            
        if isinstance(obj, (vtypes.Reg, vtypes.Wire)):
            self.variable[obj.name] = obj
            return
        
        if isinstance(obj, (vtypes.Input, vtypes.Output, vtypes.Inout)):
            return
            
        if isinstance(obj, (vtypes.Integer, vtypes.Real, vtypes.Genvar)):
            self.variable[obj.name] = obj
            return
        
        if isinstance(obj, vtypes.Parameter):
            self.global_constant[obj.name] = obj
            return
        
        if isinstance(obj, vtypes.Localparam):
            self.local_constant[obj.name] = obj
            return

        if isinstance(obj, function.Function):
            self.function[obj.name] = obj
            return

        if isinstance(obj, task.Task):
            self.task[obj.name] = obj
            return

        if isinstance(obj, vtypes.Assign):
            self.assign.append(obj)
            return

        if isinstance(obj, vtypes.Always):
            self.always.append(obj)
            return

        if isinstance(obj, vtypes.Initial):
            self.initial.append(obj)
            return

        if isinstance(obj, GenerateFor):
            if obj.scope is None:
                if None not in self.generate: self.generate[None] = []
                self.generate[None].append(obj)
                return
            self.generate[obj.scope] = obj
            return

        if isinstance(obj, GenerateIf):
            if obj.true_scope is None:
                if None not in self.generate: self.generate[None] = []
                self.generate[None].append(obj)
                return
            self.generate[obj.true_scope] = obj
            return

        if isinstance(obj, Instance):
            if isinstance(obj.module, Module):
                self.instance[obj.module.name] = obj
                self.submodule[obj.module.name] = obj.module
            elif isinstance(obj.module, str):
                self.instance[obj.module] = obj
            return

        raise TypeError("Object type '%s' is not supported." % str(type(obj)))
        
    #---------------------------------------------------------------------------
    def add_function(self, t):
        if not isinstance(t, function.Function):
            raise TypeError("add_function requires a Function, not %s" % type(t))
        name = t.name
        self.function[name] = t
        self.items.append(t)
        return t
            
    def add_task(self, t):
        if not isinstance(t, task.Task):
            raise TypeError("add_task requires a Task, not %s" % type(t))
        name = t.name
        self.task[name] = t
        self.items.append(t)
        return t
            
    #---------------------------------------------------------------------------
    def find_identifier(self, name):
        if name in self.variable: return self.variable[name]
        if name in self.io_variable: return self.io_variable[name]
        if name in self.local_constant: return self.local_constant[name]
        if name in self.global_constant: return self.global_constant[name]
        if name in self.function: return self.function[name]
        if name in self.task: return self.task[name]
        if name in self.instance: return self.instance[name]
        # raise KeyError("No such identifier in module '%s': '%s'" % (self.name, name))
        return vtypes.AnyType(name)
    
    #---------------------------------------------------------------------------
    def is_input(self, name):
        if name not in self.io_variable: return False
        if isinstance(self.io_variable[name], vtypes.Input): return True
        return False

    def is_output(self, name):
        if name not in self.io_variable: return False
        if isinstance(self.io_variable[name], vtypes.Output): return True
        return False

    def is_inout(self, name):
        if name not in self.io_variable: return False
        if isinstance(self.io_variable[name], vtypes.Inout): return True
        return False

    def is_reg(self, name):
        if name not in self.variable: return False
        if isinstance(self.variable[name], vtypes.Reg): return True
        return False
        
    def is_wire(self, name):
        if name not in self.variable and name not in self.io_variable: return False
        if name in self.variable and isinstance(self.variable[name], vtypes.Wire): return True
        if name in self.variable and isinstance(self.variable[name], vtypes.Reg): return False
        if name in self.io_variable: return True
        return False

    #---------------------------------------------------------------------------
    def get_corresponding_variable(self, var, use_wire=False):
        if isinstance(var, vtypes.Input):
            if use_wire: return vtypes.Wire
            return vtypes.Reg
        if isinstance(var, vtypes.Output):
            return vtypes.Wire
        if isinstance(var, vtypes.Inout):
            return vtypes.Wire
        raise TypeError('No corresponding IO type for %s' % str(type(var)))

    #---------------------------------------------------------------------------
    def to_hook_resolved_obj(self):
        # if there is no hooked method, object copy is not required.
        if not self.has_hook():
            return self
        copied = copy.deepcopy(self)
        copied.resolve_hook()
        return copied
        
    def resolve_hook(self):
        for method, args, kwargs in self.hook:
            if args is None: args = ()
            if kwargs is None: kwargs = {}
            method(*args, **kwargs)
            
        for sub in self.submodule.values():
            sub.resolve_hook()

    def has_hook(self):
        if self.hook: return True
        for sub in self.submodule.values():
            if sub.has_hook(): return True
        return False

#-------------------------------------------------------------------------------
class StubModule(vtypes.VeriloggenNode):
    """ Verilog Module class """
    def __init__(self, name=None):
        self.name = name if name is not None else self.__class__.__name__

    def to_verilog(self, filename=None):
        return ''

#-------------------------------------------------------------------------------
class Instance(vtypes.VeriloggenNode):
    def __init__(self, module, instname, params=None, ports=None):
        if params is None: params = ()
        if ports is None: ports = ()
        self._type_check_params(params)
        self._type_check_ports(ports)
        self.module = module
        self.instname = instname
        if not params:
            self.params = ()
        elif isinstance(params[0], (tuple, list)):
            self.params = params
        else:
            self.params = [ (None, p) for p in params ]
        if not ports:
            self.ports = ()
        elif isinstance(ports[0], (tuple, list)):
            self.ports = ports
        else:
            self.ports = [ (None, p) for p in ports ]

    def _type_check_module(self, module):
        if not isinstance(module, (Module, StubModule)):
            raise TypeError("module of Instance must be Module or StubModule, not %s" %
                            type(module))
            
    def _type_check_params(self, params):
        if not isinstance(params, (tuple, list)):
            raise TypeError("params of Instance require tuple, not %s." % type(params))
        
    def _type_check_ports(self, ports):
        if not isinstance(ports, (tuple, list)):
            raise TypeError("ports of Instance require tuple, not %s." % type(ports))

#-------------------------------------------------------------------------------
class Generate(Module):
    """ Base class of generate statement """
    def __init__(self):
        Module.__init__(self)
    
    def Input(self, name, width=None, length=None, signed=False, value=None):
        raise TypeError("Input port is not allowed in generate statement")
    
    def Output(self, name, width=None, length=None, signed=False, value=None):
        raise TypeError("Output port is not allowed in generate statement")
    
    def OutputReg(self, name, width=None, length=None, signed=False, value=None):
        raise TypeError("OutputReg port is not allowed in generate statement")
    
    def Inout(self, name, width=None, length=None, signed=False, value=None):
        raise TypeError("Inout port is not allowed in generate statement")

    def _type_check_scope(self, scope):
        if scope is None: return
        if not isinstance(scope, str):
            raise TypeError("Scope name should be str, not %s." % type(scope))
        
#-------------------------------------------------------------------------------
class GenerateFor(Generate):
    def __init__(self, pre, cond, post, scope=None):
        Generate.__init__(self)
        self.pre = pre
        self.cond = cond
        self.post = post
        self.scope = scope
        self._type_check_scope(scope)

    def __getitem__(self, index):
        return vtypes.ScopeIndex(self.scope, index)

class GenerateIf(Generate):
    def __init__(self, cond, true_scope=None):
        Generate.__init__(self)
        self.cond = cond
        self.true_scope = true_scope
        self.Else = GenerateIfElse()
        self._type_check_scope(true_scope)

class GenerateIfElse(Generate):
    def __init__(self, false_scope=None):
        Generate.__init__(self)
        self.false_scope = false_scope
        self._type_check_scope(false_scope)

    def __call__(self, false_scope):
        self.false_scope = false_scope
        return self

#-------------------------------------------------------------------------------
def connect_same_name(*args):
    ret = []
    for arg in args:
        if isinstance(arg, (list, tuple)):
            ret.extend([ (a.name, a) for a in arg ])
        elif isinstance(arg, vtypes._Variable):
            ret.append( (arg.name, arg) )
        else:
            raise TypeError('connect_same_name supports Variables, lists and tuples of them.')
    return ret
