from __future__ import absolute_import
from __future__ import print_function
import os
import sys
import collections
import copy
import re

import veriloggen.core.vtypes as vtypes
import veriloggen.core.function as function
import veriloggen.core.task as task
import veriloggen.core.rename_visitor as rename_visitor

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
        if not isinstance(self.find_identifier(name), (vtypes.AnyType, vtypes.Wire)):
            raise ValueError("Object '%s' is already defined." % name)
        self.io_variable[name] = t
        self.items.append(t)
        return t
    
    def Output(self, name, width=None, length=None, signed=False, value=None):
        t = vtypes.Output(name, width, length, signed, value)
        if not isinstance(self.find_identifier(name), (vtypes.AnyType, vtypes.Wire, vtypes.Reg)):
            raise ValueError("Object '%s' is already defined." % name)
        self.io_variable[name] = t
        self.items.append(t)
        return t
    
    def OutputReg(self, name, width=None, length=None, signed=False, value=None, initval=None):
        t = vtypes.Output(name, width, length, signed, value)
        if not isinstance(self.find_identifier(name), vtypes.AnyType):
            raise ValueError("Object '%s' is already defined." % name)
        self.io_variable[name] = t
        self.items.append(t)
        t = vtypes.Reg(name, width, length, signed, value, initval)
        self.variable[name] = t
        self.items.append(t)
        return t
    
    def Inout(self, name, width=None, length=None, signed=False, value=None):
        t = vtypes.Inout(name, width, length, signed, value)
        if not isinstance(self.find_identifier(name), (vtypes.AnyType, vtypes.Wire)):
            raise ValueError("Object '%s' is already defined." % name)
        self.io_variable[name] = t
        self.items.append(t)
        return t

    def Wire(self, name, width=None, length=None, signed=False, value=None):
        t = vtypes.Wire(name, width, length, signed, value)
        if not isinstance(self.find_identifier(name),
                          (vtypes.AnyType, vtypes.Input, vtypes.Output)):
            raise ValueError("Object '%s' is already defined." % name)
        self.variable[name] = t
        self.items.append(t)
        return t
    
    def TmpWire(self, width=None, length=None, signed=False, value=None):
        name = '_'.join([self.tmp_prefix, str(self.tmp_count)])
        self.tmp_count += 1
        return self.Wire(name, width, length, signed, value)

    def Reg(self, name, width=None, length=None, signed=False, value=None, initval=None):
        t = vtypes.Reg(name, width, length, signed, value, initval)
        if not isinstance(self.find_identifier(name), (vtypes.AnyType, vtypes.Output)):
            raise ValueError("Object '%s' is already defined." % name)
        self.variable[name] = t
        self.items.append(t)
        return t
    
    def TmpReg(self, width=None, length=None, signed=False, value=None, initval=None):
        name = '_'.join([self.tmp_prefix, str(self.tmp_count)])
        self.tmp_count += 1
        return self.Reg(name, width, length, signed, value, initval)

    def Integer(self, name, width=None, length=None, signed=False, value=None, initval=None):
        t = vtypes.Integer(name, width, length, signed, value, initval)
        if not isinstance(self.find_identifier(name), vtypes.AnyType):
            raise ValueError("Object '%s' is already defined." % name)
        self.variable[name] = t
        self.items.append(t)
        return t
    
    def TmpInteger(self, width=None, length=None, signed=False, value=None, initval=None):
        name = '_'.join([self.tmp_prefix, str(self.tmp_count)])
        self.tmp_count += 1
        return self.Integer(name, width, length, signed, value, initval)

    def Real(self, name, width=None, length=None, signed=False, value=None, initval=None):
        t = vtypes.Real(name, width, length, signed, value, initval)
        if not isinstance(self.find_identifier(name), vtypes.AnyType):
            raise ValueError("Object '%s' is already defined." % name)
        self.variable[name] = t
        self.items.append(t)
        return t
    
    def TmpReal(self, width=None, length=None, signed=False, value=None, initval=None):
        name = '_'.join([self.tmp_prefix, str(self.tmp_count)])
        self.tmp_count += 1
        return self.Real(name, width, length, signed, value, initval)

    def Genvar(self, name, width=None, length=None, signed=False, value=None):
        t = vtypes.Genvar(name, width, length, signed, value)
        if not isinstance(self.find_identifier(name), vtypes.AnyType):
            raise ValueError("Object '%s' is already defined." % name)
        self.variable[name] = t
        self.items.append(t)
        return t
    
    def TmpGenvar(self, width=None, length=None, signed=False, value=None):
        name = '_'.join([self.tmp_prefix, str(self.tmp_count)])
        self.tmp_count += 1
        return self.Genvar(name, width, length, signed, value)

    def Parameter(self, name, value, width=None, signed=False, length=None):
        t = vtypes.Parameter(name, value, width, signed)
        if not isinstance(self.find_identifier(name), vtypes.AnyType):
            raise ValueError("Object '%s' is already defined." % name)
        self.global_constant[name] = t
        self.items.append(t)
        return t
    
    def Localparam(self, name, value, width=None, signed=False, length=None):
        t = vtypes.Localparam(name, value, width, signed)
        if not isinstance(self.find_identifier(name), vtypes.AnyType):
            raise ValueError("Object '%s' is already defined." % name)
        self.local_constant[name] = t
        self.items.append(t)
        return t

    def TmpLocalparam(self, value, width=None, signed=False, length=None):
        name = '_'.join([self.tmp_prefix, str(self.tmp_count)])
        self.tmp_count += 1
        return self.Localparam(name, value, width, signed, length)

    #---------------------------------------------------------------------------
    def InputLike(self, src, name=None, width=None, length=None, signed=None, value=None):
        if name is None: name = src.name
        if width is None: width = src.width
        #if length is None: length = src.length
        if length is None: length = None
        if signed is None: signed = src.signed
        if value is None: value = src.value
        return self.Input(name, width, length, signed, value)
        
    def OutputLike(self, src, name=None, width=None, length=None, signed=None, value=None):
        if name is None: name = src.name
        if width is None: width = src.width
        #if length is None: length = src.length
        if length is None: length = None
        if signed is None: signed = src.signed
        if value is None: value = src.value
        return self.Output(name, width, length, signed, value)
        
    def OutputRegLike(self, src, name=None, width=None, length=None, signed=None, value=None, initval=None):
        if name is None: name = src.name
        if width is None: width = src.width
        #if length is None: length = src.length
        if length is None: length = None
        if signed is None: signed = src.signed
        if value is None: value = src.value
        if initval is None: initval = src.initval
        return self.OutputReg(name, width, length, signed, value, initval)
        
    def InoutLike(self, src, name=None, width=None, length=None, signed=None, value=None):
        if name is None: name = src.name
        if width is None: width = src.width
        #if length is None: length = src.length
        if length is None: length = None
        if signed is None: signed = src.signed
        if value is None: value = src.value
        return self.Inout(name, width, length, signed, value)
        
    def WireLike(self, src, name=None, width=None, length=None, signed=None, value=None):
        if name is None: name = src.name
        if width is None: width = src.width
        if length is None: length = src.length
        if signed is None: signed = src.signed
        if value is None: value = src.value
        return self.Wire(name, width, length, signed, value)
        
    def TmpWireLike(self, src, width=None, length=None, signed=None, value=None):
        if width is None: width = src.width
        if length is None: length = src.length
        if signed is None: signed = src.signed
        if value is None: value = src.value
        return self.TmpWire(width, length, signed, value)
        
    def RegLike(self, src, name=None, width=None, length=None, signed=None, value=None, initval=None):
        if name is None: name = src.name
        if width is None: width = src.width
        if length is None: length = src.length
        if signed is None: signed = src.signed
        if value is None: value = src.value
        if initval is None: initval = src.initval
        return self.Reg(name, width, length, signed, value, initval)

    def TmpRegLike(self, src, width=None, length=None, signed=None, value=None, initval=None):
        if width is None: width = src.width
        if length is None: length = src.length
        if signed is None: signed = src.signed
        if value is None: value = src.value
        if initval is None: initval = src.initval
        return self.TmpReg(width, length, signed, value, initval)

    def IntegerLike(self, src, name=None, width=None, length=None, signed=None, value=None, initval=None):
        if name is None: name = src.name
        if width is None: width = src.width
        if length is None: length = src.length
        if signed is None: signed = src.signed
        if value is None: value = src.value
        if initval is None: initval = src.initval
        return self.Integer(name, width, length, signed, value, initval)

    def TmpIntegerLike(self, src, width=None, length=None, signed=None, value=None, initval=None):
        if width is None: width = src.width
        if length is None: length = src.length
        if signed is None: signed = src.signed
        if value is None: value = src.value
        if initval is None: initval = src.initval
        return self.TmpInteger(width, length, signed, value, initval)

    def RealLike(self, src, name=None, width=None, length=None, signed=None, value=None, initval=None):
        if name is None: name = src.name
        if width is None: width = src.width
        if length is None: length = src.length
        if signed is None: signed = src.signed
        if value is None: value = src.value
        if initval is None: initval = src.initval
        return self.Real(name, width, length, signed, value, initval)

    def TmpRealLike(self, src, width=None, length=None, signed=None, value=None, initval=None):
        if width is None: width = src.width
        if length is None: length = src.length
        if signed is None: signed = src.signed
        if value is None: value = src.value
        if initval is None: initval = src.initval
        return self.TmpReal(width, length, signed, value, initval)

    def GenvarLike(self, src, name=None, width=None, length=None, signed=None, value=None):
        if name is None: name = src.name
        if width is None: width = src.width
        #if length is None: length = src.length
        if length is None: length = None
        if signed is None: signed = src.signed
        if value is None: value = src.value
        return self.Genvar(name, width, length, signed, value)

    def TmpGenvarLike(self, src, width=None, length=None, signed=None, value=None):
        if width is None: width = src.width
        #if length is None: length = src.length
        if length is None: length = None
        if signed is None: signed = src.signed
        if value is None: value = src.value
        return self.TmpGenvar(width, length, signed, value)

    def ParameterLike(self, src, name=None, value=None, width=None, signed=False, length=None):
        if name is None: name = src.name
        if value is None: value = src.value
        if width is None: width = src.width
        if signed is None: signed = src.signed
        if length is None: length = src.length
        return self.Parameter(name, value, width, signed, length)
    
    def LocalparamLike(self, src, name=None, value=None, width=None, signed=False, length=None):
        if name is None: name = src.name
        if value is None: value = src.value
        if width is None: width = src.width
        if signed is None: signed = src.signed
        if length is None: length = src.length
        return self.Localparam(name, value, width, signed, length)
    
    def TmpLocalparamLike(self, src, value=None, width=None, signed=False, length=None):
        if value is None: value = src.value
        if width is None: width = src.width
        if signed is None: signed = src.signed
        if length is None: length = src.length
        return self.TmpLocalparam(value, width, signed, length)
    
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
        if not isinstance(self.find_identifier(name), vtypes.AnyType):
            raise ValueError("Object '%s' is already defined." % name)
        self.function[name] = t
        self.items.append(t)
        return t
        
    def Task(self, name, width=1):
        t = task.Task(name, width)
        if not isinstance(self.find_identifier(name), vtypes.AnyType):
            raise ValueError("Object '%s' is already defined." % name)
        self.task[name] = t
        self.items.append(t)
        return t
        
    #---------------------------------------------------------------------------
    def GenerateFor(self, pre, cond, post, scope=None):
        t = GenerateFor(self, pre, cond, post, scope)
        if scope is None:
            if None not in self.generate: self.generate[None] = []
            self.generate[None].append(t)
            return
        if not isinstance(self.find_identifier(scope), vtypes.AnyType):
            raise ValueError("Object '%s' is already defined." % scope)
        if scope in self.generate:
            raise ValueError("scope '%s' is already defined." % scope)
        self.generate[scope] = t
        self.items.append(t)
        return t
            
    def GenerateIf(self, cond, scope=None):
        t = GenerateIf(self, cond, scope)
        if scope is None:
            if None not in self.generate: self.generate[None] = []
            self.generate[None].append(t)
            return
        if not isinstance(self.find_identifier(scope), vtypes.AnyType):
            raise ValueError("Object '%s' is already defined." % scope)
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
        if not isinstance(self.find_identifier(instname), vtypes.AnyType):
            raise ValueError("Object '%s' is already defined." % instname)
        t = Instance(module, instname, params, ports)
        self.instance[instname] = t
        self.items.append(t)
        if isinstance(module, StubModule):
            return None
        if self.find_module(module.name) is not None:
            if self.submodule[module.name] != module:
                raise ValueError("Module '%s' is already defined." % module.name)
        else:
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
        return ret

    #---------------------------------------------------------------------------
    # User interface for accessing internal information
    #---------------------------------------------------------------------------
    def get_params(self):
        return self.global_constant
    
    def get_localparams(self):
        return self.local_constant
    
    def get_ports(self):
        return self.io_variable
    
    def get_vars(self):
        return self.variable
    
    #---------------------------------------------------------------------------
    def copy_params(self, src, prefix=None, postfix=None, exclude=None):
        if prefix is None: prefix = ''
        if postfix is None: postfix = ''
        if exclude is None: exclude = ()
        if isinstance(exclude, str): exclude = [ exclude ] 
        visitor = rename_visitor.RenameVisitor(prefix, postfix)
        ret = collections.OrderedDict()
        for key, obj in src.global_constant.items():
            skip = False
            for ex in exclude:
                if re.match(ex, key): skip = True
            if skip: continue
            copy_obj = copy.deepcopy(obj)
            copy_obj.name = ''.join([prefix, copy_obj.name, postfix])
            copy_obj.width = visitor.visit(copy_obj.width)
            self.add_object( copy_obj )
            ret[copy_obj.name] = copy_obj
        return ret
    
    def copy_localparams(self, src, prefix=None, postfix=None, exclude=None):
        if prefix is None: prefix = ''
        if postfix is None: postfix = ''
        if exclude is None: exclude = ()
        if isinstance(exclude, str): exclude = [ exclude ] 
        visitor = rename_visitor.RenameVisitor(prefix, postfix)
        ret = collections.OrderedDict()
        for key, obj in src.constant.items():
            skip = False
            for ex in exclude:
                if re.match(ex, key): skip = True
            if skip: continue
            copy_obj = copy.deepcopy(obj)
            copy_obj.name = ''.join([prefix, copy_obj.name, postfix])
            copy_obj.width = visitor.visit(copy_obj.width)
            self.add_object( copy_obj )
            ret[copy_obj.name] = copy_obj
        return ret
    
    def copy_ports(self, src, prefix=None, postfix=None, exclude=None):
        if prefix is None: prefix = ''
        if postfix is None: postfix = ''
        if exclude is None: exclude = ()
        if isinstance(exclude, str): exclude = [ exclude ] 
        visitor = rename_visitor.RenameVisitor(prefix, postfix)
        ret = collections.OrderedDict()
        for key, obj in src.io_variable.items():
            skip = False
            for ex in exclude:
                if re.match(ex, key): skip = True
            if skip: continue
            copy_obj = copy.deepcopy(obj)
            copy_obj.name = ''.join([prefix, copy_obj.name, postfix])
            copy_obj.width = visitor.visit(copy_obj.width)
            self.add_object( copy_obj )
            ret[copy_obj.name] = copy_obj
        return ret

    def copy_vars(self, src, prefix=None, postfix=None, exclude=None):
        if prefix is None: prefix = ''
        if postfix is None: postfix = ''
        if exclude is None: exclude = ()
        if isinstance(exclude, str): exclude = [ exclude ] 
        visitor = rename_visitor.RenameVisitor(prefix, postfix)
        ret = collections.OrderedDict()
        for key, obj in src.variable.items():
            skip = False
            for ex in exclude:
                if re.match(ex, key): skip = True
            if skip: continue
            copy_obj = copy.deepcopy(obj)
            copy_obj.name = ''.join([prefix, copy_obj.name, postfix])
            copy_obj.width = visitor.visit(copy_obj.width)
            self.add_object( copy_obj )
            ret[copy_obj.name] = copy_obj
        return ret

    def copy_sim_ports(self, src, prefix=None, postfix=None, exclude=None):
        if prefix is None: prefix = ''
        if postfix is None: postfix = ''
        if exclude is None: exclude = ()
        if isinstance(exclude, str): exclude = [ exclude ] 
        visitor = rename_visitor.RenameVisitor(prefix, postfix)
        ret = collections.OrderedDict()
        for key, obj in src.io_variable.items():
            skip = False
            for ex in exclude:
                if re.match(ex, key): skip = True
            if skip: continue
            copy_obj = self.get_opposite_variable(obj)(key, copy.deepcopy(obj.width))
            copy_obj.name = ''.join([prefix, copy_obj.name, postfix])
            copy_obj.width = visitor.visit(copy_obj.width)
            self.add_object( copy_obj )
            ret[copy_obj.name] = copy_obj
        return ret

    #---------------------------------------------------------------------------
    def connect_params(self, targ, prefix=None, postfix=None, exclude=None, strict=False):
        if prefix is None: prefix = ''
        if postfix is None: postfix = ''
        if exclude is None: exclude = ()
        if isinstance(exclude, str): exclude = [ exclude ] 
        ret = []
        for key, obj in targ.global_constant.items():
            skip = False
            for ex in exclude:
                if re.match(ex, key): skip = True
            if skip: continue
            my_key = ''.join([prefix, key, postfix])
            if strict and (my_key not in self.global_constant) and (my_key not in self.local_constant):
                raise IndexError("No such constant '%s' in module '%s'" % (key, self.name))
            if my_key in self.global_constant:
                ret.append( (key, self.global_constant[my_key]) )
            elif my_key in self.local_constant:
                ret.append( (key, self.local_constant[my_key]) )
        return ret
    
    def connect_ports(self, targ, prefix=None, postfix=None, exclude=None, strict=False):
        if prefix is None: prefix = ''
        if postfix is None: postfix = ''
        if exclude is None: exclude = ()
        if isinstance(exclude, str): exclude = [ exclude ] 
        ret = []
        for key, obj in targ.io_variable.items():
            skip = False
            for ex in exclude:
                if re.match(ex, key): skip = True
            if skip: continue
            my_key = ''.join([prefix, key, postfix])
            if strict and (my_key not in self.io_variable) and (my_key not in self.variable):
                raise IndexError("No such IO '%s' in module '%s'" % (key, self.name))
            if my_key in self.io_variable:
                ret.append( (key, self.io_variable[my_key]) )
            elif my_key in self.variable:
                ret.append( (key, self.variable[my_key]) )
        return ret
    
    #---------------------------------------------------------------------------
    # User interface for Verilog code generation
    #---------------------------------------------------------------------------
    def to_verilog(self, filename=None):
        import veriloggen.verilog.to_verilog as to_verilog
        obj = self.to_hook_resolved_obj()
        return to_verilog.write_verilog(obj, filename)

    def add_hook(self, method, args=None, kwargs=None):
        """ add a hooked method to 'to_verilog()' """
        self.hook.append( (method, args, kwargs) )

    #---------------------------------------------------------------------------
    def add_object(self, obj):
        self.items.append(obj)

        if isinstance(obj, vtypes.AnyType):
            self.io_variable[obj.name] = obj
            self.variable[obj.name] = obj
            self.global_constant[obj.name] = obj
            self.local_constant[obj.name] = obj
            return
        
        if isinstance(obj, (vtypes.Input, vtypes.Output, vtypes.Inout)):
            self.io_variable[obj.name] = obj
            return
            
        if isinstance(obj, (vtypes.Reg, vtypes.Wire)):
            self.variable[obj.name] = obj
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
        if name in self.generate: return self.generate[name]
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
    def get_opposite_variable(self, var, use_wire=False):
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

    #---------------------------------------------------------------------------
    def find_module(self, name):
        if name in self.submodule:
            return self.submodule[name]
        for gen in self.generate.values():
            if isinstance(gen, (tuple, list)):
                for g in gen:
                    r = g.find_module(name)
                    if r: return r
            else:
                r = gen.find_module(name)
                if r: return r
        for sub in self.submodule.values():
            r = sub.find_module(name)
            if r: return r
        return None

    def get_modules(self):
        modules = collections.OrderedDict()
        modules[self.name] = self
        for gen in self.generate.values():
            if isinstance(gen, (tuple, list)):
                for g in gen:
                    modules.update( g.get_modules() )
            else:
                modules.update( gen.get_modules() )
        for sub in self.submodule.values():
            modules.update( sub.get_modules() )
        return modules
    
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
        elif isinstance(params, dict):
            self.params = [ (k, v) for k, v in params.items() ]
        elif isinstance(params[0], (tuple, list)):
            self.params = params
        else:
            self.params = [ (None, p) for p in params ]
        if not ports:
            self.ports = ()
        elif isinstance(ports, dict):
            self.ports = [ (k, v) for k, v in ports.items() ]
        elif isinstance(ports[0], (tuple, list)):
            self.ports = ports
        else:
            self.ports = [ (None, p) for p in ports ]

    def _type_check_module(self, module):
        if not isinstance(module, (Module, StubModule)):
            raise TypeError("module of Instance must be Module or StubModule, not %s" %
                            type(module))
            
    def _type_check_params(self, params):
        if not isinstance(params, (tuple, list, dict)):
            raise TypeError("params of Instance require tuple, list, or dict, not %s." % type(params))
        
    def _type_check_ports(self, ports):
        if not isinstance(ports, (tuple, list, dict)):
            raise TypeError("ports of Instance require tuple, list, or dict, not %s." % type(ports))

#-------------------------------------------------------------------------------
class Generate(Module):
    """ Base class of generate statement """
    def __init__(self, m):
        Module.__init__(self)
        self.m = m
    
    def Input(self, name, width=None, length=None, signed=False, value=None):
        raise TypeError("Input port is not allowed in generate statement")
    
    def Output(self, name, width=None, length=None, signed=False, value=None):
        raise TypeError("Output port is not allowed in generate statement")
    
    def OutputReg(self, name, width=None, length=None, signed=False, value=None):
        raise TypeError("OutputReg port is not allowed in generate statement")
    
    def Inout(self, name, width=None, length=None, signed=False, value=None):
        raise TypeError("Inout port is not allowed in generate statement")

    def find_identifier(self, name):
        r = Module.find_identifier(self, name)
        if r:
            return r
        r = self.m.find_identifier(name)
        if r:
            return r
        return vtypes.AnyType(name)

    def get_modules(self):
        modules = collections.OrderedDict()
        for gen in self.generate.values():
            if isinstance(gen, (tuple, list)):
                for g in gen:
                    modules.update( g.get_modules() )
            else:
                modules.update( gen.get_modules() )
        for sub in self.submodule.values():
            modules.update( sub.get_modules() )
        return modules
    
    def _type_check_scope(self, scope):
        if scope is None: return
        if not isinstance(scope, str):
            raise TypeError("Scope name should be str, not %s." % type(scope))
        
#-------------------------------------------------------------------------------
class GenerateFor(Generate):
    def __init__(self, m, pre, cond, post, scope=None):
        Generate.__init__(self, m)
        self.pre = pre
        self.cond = cond
        self.post = post
        self.scope = scope
        self._type_check_scope(scope)

    def __getitem__(self, index):
        return vtypes.ScopeIndex(self.scope, index)

class GenerateIf(Generate):
    def __init__(self, m, cond, true_scope=None):
        Generate.__init__(self, m)
        self.cond = cond
        self.true_scope = true_scope
        self.Else = GenerateIfElse(m)
        self._type_check_scope(true_scope)

class GenerateIfElse(Generate):
    def __init__(self, m, false_scope=None):
        Generate.__init__(self, m)
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
