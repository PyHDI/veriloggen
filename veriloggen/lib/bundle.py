from __future__ import absolute_import
from __future__ import print_function
import os
import sys
import re

import veriloggen.vtypes as vtypes
from veriloggen.module import Module

class Bundle(vtypes.VeriloggenNode):
    def __init__(self, m, prefix='', postfix=''):
        if not isinstance(m, Module):
            raise TypeError("module should be an instance of Module.")
        self.module = m
        self.prefix = prefix
        self.postfix = postfix

    #---------------------------------------------------------------------------
    def get_name(self, name):
        return self.prefix + name + self.postfix

    def get_basename(self, name):
        return re.sub(r'' + self.postfix + '$', '', name.replace(self.prefix, '', 1))

    #---------------------------------------------------------------------------
    def Input(self, name, width=1, length=None, signed=False, value=None):
        new_name = self.get_name(name)
        return self.module.Input(name, width, length, signed, value)
        
    def Output(self, name, width=1, length=None, signed=False, value=None):
        new_name = self.get_name(name)
        return self.module.Output(name, width, length, signed, value)
        
    def OutputReg(self, name, width=1, length=None, signed=False, value=None):
        new_name = self.get_name(name)
        return self.module.OutputReg(name, width, length, signed, value)
        
    def Inout(self, name, width=1, length=None, signed=False, value=None):
        new_name = self.get_name(name)
        return self.module.Inout(name, width, length, signed, value)
        
    def Reg(self, name, width=1, length=None, signed=False, value=None):
        new_name = self.get_name(name)
        return self.module.Reg(name, width, length, signed, value)
        
    def Wire(self, name, width=1, length=None, signed=False, value=None):
        new_name = self.get_name(name)
        return self.module.Wire(name, width, length, signed, value)
        
    def Parameter(self, name, value, width=None, signed=False):
        new_name = self.get_name(name)
        return self.module.Parameter(name, value, width, signed)
        
    def Localparam(self, name, value, width=None, signed=False):
        new_name = self.get_name(name)
        return self.module.Localparam(name, value, width, signed)
        
    #---------------------------------------------------------------------------
    def connect_all_ports(self, prefix='', postfix=''):
        instances = sorted(dir(self))
        inputs = [ s for s in instances if isinstance(getattr(self, s), vtypes.Input) ]
        outputs = [ s for s in instances if isinstance(getattr(self, s), vtypes.Output) ]
        inouts = [ s for s in instances if isinstance(getattr(self, s), vtypes.Inout) ]
        regs = [ s for s in instances if isinstance(getattr(self, s), vtypes.Reg) ]
        wires = [ s for s in instances if isinstance(getattr(self, s), vtypes.Wire) ]
        ret = []
        for p in inputs:
            name = prefix + self.get_basename(getattr(self, p).name) + postfix
            ret.append( (name, getattr(self, p)) )
        for p in outputs:
            name = prefix + self.get_basename(getattr(self, p).name) + postfix
            ret.append( (name, getattr(self, p)) )
        for p in inouts:
            name = prefix + self.get_basename(getattr(self, p).name) + postfix
            ret.append( (name, getattr(self, p)) )
        for p in regs:
            name = prefix + self.get_basename(getattr(self, p).name) + postfix
            ret.append( (name, getattr(self, p)) )
        for p in wires:
            name = prefix + self.get_basename(getattr(self, p).name) + postfix
            ret.append( (name, getattr(self, p)) )
        return tuple(ret)

    #---------------------------------------------------------------------------
    def connect_all_parameters(self, prefix='', postfix=''):
        instances = sorted(dir(self))
        parameters = [ s for s in instances if isinstance(getattr(self, s), vtypes.Parameter) ]
        localparams = [ s for s in instances if isinstance(getattr(self, s), vtypes.Localparam) ]
        ret = []
        for p in parameters:
            name = prefix + self.get_basename(getattr(self, p).name) + postfix
            ret.append( (name, getattr(self, p)) )
        for p in localparams:
            name = prefix + self.get_basename(getattr(self, p).name) + postfix
            ret.append( (name, getattr(self, p)) )
        return tuple(ret)
    
    def get_ports(self):
        return ([ getattr(self, s) for s in dir(self) if isinstance(getattr(self, s), vtypes.Input) ] +
                [ getattr(self, s) for s in dir(self) if isinstance(getattr(self, s), vtypes.Output) ] +
                [ getattr(self, s) for s in dir(self) if isinstance(getattr(self, s), vtypes.Inout) ] +
                [ getattr(self, s) for s in dir(self) if isinstance(getattr(self, s), vtypes.Reg) ] +
                [ getattr(self, s) for s in dir(self) if isinstance(getattr(self, s), vtypes.Wire) ])
        
    def get_parameters(self):
        return ([ getattr(self, s) for s in dir(self) if isinstance(getattr(self, s), vtypes.Parameter) ] +
                [ getattr(self, s) for s in dir(self) if isinstance(getattr(self, s), vtypes.Localparam) ])
