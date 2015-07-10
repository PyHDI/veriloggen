import os
import sys
import collections

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import vtypes
import function

import to_verilog

class Module(object):
    """ Verilog Module class """
    def __init__(self, name=None):
        self.name = name if name is not None else self.__class__.__name__
        self.variable = collections.OrderedDict()
        self.io_variable = collections.OrderedDict()
        self.constant = collections.OrderedDict()
        self.global_constant = collections.OrderedDict()
        self.function = []
        self.assign = []
        self.always = []
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
    def Always(self, sensitivity, *statement):
        t = vtypes.Always(sensitivity, *statement)
        self.always.append(t)
        return t
    
    def Assign(self, statement):
        t = vtypes.Assign(statement)
        self.assign.append(t)
        return t

    #---------------------------------------------------------------------------
    def Function(self, name, width=1):
        t = function.Function(name, width)
        self.function.append(t)
        return t
        
    #---------------------------------------------------------------------------
    def Instance(self, module, instname, params, ports):
        t = vtypes.Instance(module, instname, params, ports)
        self.instance[instname] = t
        self.submodule[module.name] = module
        return t
    
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
        return to_verilog.to_verilog(self, filename)
