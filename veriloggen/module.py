from __future__ import absolute_import
from __future__ import print_function
import os
import sys
import collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import vtypes
import function
import task
import to_verilog

#-------------------------------------------------------------------------------
class Module(vtypes.VeriloggenNode):
    """ Verilog Module class """
    def __init__(self, name=None):
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
    
    def OutputReg(self, name, width=None, length=None, signed=False, value=None):
        t = vtypes.Output(name, width, length, signed, value)
        self.io_variable[name] = t
        self.items.append(t)
        t = vtypes.Reg(name, width, length, signed, value)
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
    
    def Reg(self, name, width=None, length=None, signed=False, value=None):
        t = vtypes.Reg(name, width, length, signed, value)
        self.variable[name] = t
        self.items.append(t)
        return t
    
    def Integer(self, name, width=None, length=None, signed=False, value=None):
        t = vtypes.Integer(name, width, length, signed, value)
        self.variable[name] = t
        self.items.append(t)
        return t
    
    def Real(self, name, width=None, length=None, signed=False, value=None):
        t = vtypes.Real(name, width, length, signed, value)
        self.variable[name] = t
        self.items.append(t)
        return t
    
    def Genvar(self, name, width=None, length=None, signed=False, value=None):
        t = vtypes.Genvar(name, width, length, signed, value)
        self.variable[name] = t
        self.items.append(t)
        return t
    
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
    def Instance(self, module, instname, params, ports):
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
    def to_verilog(self, filename=None):
        return to_verilog.write_verilog(self, filename)

#-------------------------------------------------------------------------------
class StubModule(vtypes.VeriloggenNode):
    """ Verilog Module class """
    def __init__(self, name=None):
        self.name = name if name is not None else self.__class__.__name__

    def to_verilog(self, filename=None):
        return ''

#-------------------------------------------------------------------------------
class Instance(vtypes.VeriloggenNode):
    def __init__(self, module, instname, params, ports):
        self.type_check_params(params)
        self.type_check_ports(ports)
        self.module = module
        self.instname = instname
        if isinstance(params[0], (tuple, list)):
            self.params = params
        else:
            self.params = [ (None, p) for p in params ]
        if isinstance(ports[0], (tuple, list)):
            self.ports = ports
        else:
            self.ports = [ (None, p) for p in ports ]

    def type_check_module(self, module):
        if not isinstance(module, (Module, StubModule)):
            raise TypeError("module of Instance must be Module or StubModule, not %s" %
                            type(module))
            
    def type_check_params(self, params):
        if not isinstance(params, (tuple, list)):
            raise TypeError("params of Instance require tuple, not %s." % type(params))
        
    def type_check_ports(self, ports):
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

    def type_check_scope(self, scope):
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
        self.type_check_scope(scope)

    def __getitem__(self, index):
        return vtypes.ScopeIndex(self.scope, index)

class GenerateIf(Generate):
    def __init__(self, cond, true_scope=None):
        Generate.__init__(self)
        self.cond = cond
        self.true_scope = true_scope
        self.Else = GenerateIfElse()
        self.type_check_scope(true_scope)

class GenerateIfElse(Generate):
    def __init__(self, false_scope=None):
        Generate.__init__(self)
        self.false_scope = false_scope
        self.type_check_scope(false_scope)

    def __call__(self, false_scope):
        self.false_scope = false_scope
        return self
