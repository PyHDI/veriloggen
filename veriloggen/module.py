import os
import sys
import collections

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import vtypes
import function
import task

import to_verilog

class Module(object):
    """ Verilog Module class """
    def __init__(self, name=None):
        self.name = name if name is not None else self.__class__.__name__
        self.variable = collections.OrderedDict()
        self.io_variable = collections.OrderedDict()
        self.constant = collections.OrderedDict()
        self.global_constant = collections.OrderedDict()
        self.function = collections.OrderedDict()
        self.task = collections.OrderedDict()
        self.assign = []
        self.always = []
        self.initial = []
        self.instance = collections.OrderedDict()
        self.submodule = {}

    #---------------------------------------------------------------------------
    def Input(self, name, width=None, length=None, signed=False, value=None):
        t = vtypes.Input(name, width, length, signed, value)
        self.io_variable[name] = t
        return t
    
    def Output(self, name, width=None, length=None, signed=False, value=None):
        t = vtypes.Output(name, width, length, signed, value)
        self.io_variable[name] = t
        return t
    
    def OutputReg(self, name, width=None, length=None, signed=False, value=None):
        t = vtypes.Output(name, width, length, signed, value)
        self.io_variable[name] = t
        t = vtypes.Reg(name, width, length, signed, value)
        self.variable[name] = t
        return t
    
    def Inout(self, name, width=None, length=None, signed=False, value=None):
        t = vtypes.Inout(name, width, length, signed, value)
        self.io_variable[name] = t
        return t

    def Wire(self, name, width=None, length=None, signed=False, value=None):
        t = vtypes.Wire(name, width, length, signed, value)
        self.variable[name] = t
        return t
    
    def Reg(self, name, width=None, length=None, signed=False, value=None):
        t = vtypes.Reg(name, width, length, signed, value)
        self.variable[name] = t
        return t
    
    def Integer(self, name, width=None, length=None, signed=False, value=None):
        t = vtypes.Integer(name, width, length, signed, value)
        self.variable[name] = t
        return t
    
    def Real(self, name, width=None, length=None, signed=False, value=None):
        t = vtypes.Real(name, width, length, signed, value)
        self.variable[name] = t
        return t
    
    def Genvar(self, name, width=None, length=None, signed=False, value=None):
        t = vtypes.Genvar(name, width, length, signed, value)
        self.variable[name] = t
        return t
    
    def Parameter(self, name, value, width=None, signed=False, length=None):
        t = vtypes.Parameter(name, value, width, signed)
        self.global_constant[name] = t
        return t
    
    def Localparam(self, name, value, width=None, signed=False, length=None):
        t = vtypes.Localparam(name, value, width, signed)
        self.constant[name] = t
        return t

    #---------------------------------------------------------------------------
    def Always(self, sensitivity):
        t = vtypes.Always(sensitivity)
        self.always.append(t)
        return t
    
    def Assign(self, statement):
        t = vtypes.Assign(statement)
        self.assign.append(t)
        return t

    def Initial(self, *statement):
        t = vtypes.Initial(*statement)
        self.initial.append(t)
    
    def Function(self, name, width=1):
        t = function.Function(name, width)
        self.function[name] = t
        return t
        
    def Task(self, name, width=1):
        t = task.Task(name, width)
        self.task[name] = t
        return t
        
    #---------------------------------------------------------------------------
    def Instance(self, module, instname, params, ports):
        if isinstance(module, str): module = StubModule(module)
        if not isinstance(module, (Module, StubModule, str)):
            raise TypeError('"module" of Instance must be Module, StubModule, or str, not %s'
                            % type(module))
        t = vtypes.Instance(module, instname, params, ports)
        self.instance[instname] = t
        if isinstance(module, StubModule):
            return None
        self.submodule[module.name] = module
        return t
    
    #---------------------------------------------------------------------------
    def add_object(self, obj):
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
            self.constant[obj.name] = obj
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

        raise TypeError("Object type '%s' is not supported." % str(type(obj)))
        
    #---------------------------------------------------------------------------
    def add_function(self, t):
        if not isinstance(t, function.Function):
            raise TypeError("add_function requires a Function, not %s" % type(t))
        name = t.name
        self.function[name] = t
        return t
            
    def add_task(self, t):
        if not isinstance(t, task.Task):
            raise TypeError("add_task requires a Task, not %s" % type(t))
        name = t.name
        self.task[name] = t
        return t
            
    #---------------------------------------------------------------------------
    def find_identifier(self, name):
        if name in self.variable: return self.variable[name]
        if name in self.io_variable: return self.io_variable[name]
        if name in self.constant: return self.constant[name]
        if name in self.global_constant: return self.global_constant[name]
        if name in self.function: return self.function[name]
        if name in self.task: return self.task[name]
        if name in self.instance: return self.instance[name]
        # raise KeyError("No such identifier in module '%s': '%s'" % (self.name, name))
        return vtypes.AnyType(name)
    
    #---------------------------------------------------------------------------
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

    def is_output(self, name):
        if name not in self.io_variable: return False
        if isinstance(self.io_variable[name], vtypes.Output): return True
        return False

    #---------------------------------------------------------------------------
    def get_io(self):
        return self.io_variable
    
    def get_io_name(self):
        return tuple(self.io_variable.keys())
    
    #---------------------------------------------------------------------------
    def to_verilog(self, filename=None):
        return to_verilog.write_verilog(self, filename)

#-------------------------------------------------------------------------------
class StubModule(Module):
    """ Verilog Module class """
    def __init__(self, name=None):
        self.name = name if name is not None else self.__class__.__name__

    def to_verilog(self, filename=None):
        return ''
