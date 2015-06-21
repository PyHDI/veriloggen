import os
import sys
import collections

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import vtypes
import toverilog

class Module(object):
    def __init__(self, name):
        self.name = name
        self.variable = collections.OrderedDict()
        self.io_variable = collections.OrderedDict()
        self.constant = collections.OrderedDict()
        self.global_constant = collections.OrderedDict()
        self.assign = []
        self.always = []
        self.instance = collections.OrderedDict()

    def isReg(self, name):
        if name not in self.variable: return False
        if isinstance(self.variable[name], vtypes.Reg): return True
        return False
        
    def isWire(self, name):
        if name not in self.variable and name not in self.io_variable: return False
        if name in self.variable and isinstance(self.variable[name], vtypes.Wire): return True
        if name in self.variable and isinstance(self.variable[name], vtypes.Reg): return False
        if name in self.io_variable: return True
        return False

    def isOutput(self, name):
        if name not in self.io_variable: return False
        if isinstance(self.io_variable[name], vtypes.Output): return True
        return False
    
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
    
    def Parameter(self, name, value, width=None, signed=False, length=None):
        t = vtypes.Parameter(name, value, width, signed)
        self.global_constant[name] = t
        return t
    
    def Localparam(self, name, value, width=None, signed=False, length=None):
        t = vtypes.Localparam(name, value, width, signed)
        self.constant[name] = t
        return t

    #---------------------------------------------------------------------------
    def Always(self, sensitivity, statement):
        t = vtypes.Always(sensitivity, statement)
        self.always.append(t)
        return t
    
    def Assign(self, left, right):
        t = vtypes.Assign(left, right)
        self.assign.append(t)
        return t

    def Instance(self, module, instname, params, ports):
        t = vtypes.Instance(module, instname, params, ports)
        self.instance[instname] = t
        return t
    
    #---------------------------------------------------------------------------
    def toVerilog(self):
        return toverilog.toVerilog(self)

    def getIO(self):
        return self.io_variable
    
    def getIOname(self):
        return tuple(self.io_variable.keys())
