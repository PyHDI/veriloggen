from __future__ import absolute_import
from __future__ import print_function
import os
import sys
import copy
from collections import OrderedDict

import veriloggen.core.vtypes as vtypes
import veriloggen.core.module as module

def get_width(node):
    ret = node.bit_length()
    if isinstance(node, int) and ret < 32:
        return 32
    if ret is None or isinstance(node, vtypes.AnyType):
        return 32
    return ret

#-------------------------------------------------------------------------------
class _Visitor(object):
    def generic_visit(self, node):
        raise TypeError("Type %s is not supported." % str(type(node)))
        
    def visit(self, node):
        visitor = getattr(self, 'visit_' + node.__class__.__name__, self.generic_visit)
        return visitor(node)
    
class _CachedVisitor(_Visitor):
    def __init__(self):
        _Visitor.__init__(self)
        self.visited_node = {}

    def visit(self, node):
        # check the cache
        if node in self.visited_node:
            return self.visited_node[node]
        
        ret = self._visit(node)
        self.visited_node[node] = ret
        return ret
    
    def _visit(self, node):
        visitor = getattr(self, 'visit_' + node.__class__.__name__, self.generic_visit)
        return visitor(node)

class _CommonVisitor(_CachedVisitor):
    def generic_visit(self, node):
        if isinstance(node, vtypes._Variable):
            return self.visit__Variable(node)

        if isinstance(node, vtypes._Constant):
            return self.visit__Constant(node)

        if isinstance(node, vtypes._BinaryOperator):
            return self.visit__BinaryOperator(node)
        
        if isinstance(node, vtypes._UnaryOperator):
            return self.visit__UnaryOperator(node)

        #raise TypeError("Type %s is not supported." % str(type(node)))
        return node
    
    def visit__Variable(self, node):
        return node
    
    def visit__Constant(self, node):
        return node.value
    
    def visit__BinaryOperator(self, node):
        return node
        
    def visit__UnaryOperator(self, node):
        return node
        
#-------------------------------------------------------------------------------
class ConstantVisitor(_CommonVisitor):
    def __init__(self, const_dict):
        _CommonVisitor.__init__(self)
        self.const_dict = const_dict

    #---------------------------------------------------------------------------
    def get_const(self, name):
        if name not in self.const_dict:
            raise KeyError("No such constant: '%s'" % name)
        return self.const_dict[name]

    def has_const(self, name):
        return (name in self.const_dict)
        
    def update_const(self, name, value):
        self.const_dict[name] = value

    def get_const_dict(self):
        return self.const_dict

    #---------------------------------------------------------------------------
    def _visit_param(self, node):
        if self.has_const(node.name):
            value = self.get_const(node.name)
            return value
        # unresolved node
        return node
    
    def visit_Parameter(self, node):
        return self._visit_param(node)

    def visit_Localparam(self, node):
        return self._visit_param(node)

    def visit_AnyType(self, node):
        return self._visit_param(node)

    #---------------------------------------------------------------------------
    def visit__BinaryOperator(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        lwidth = self.visit(get_width(node.left))
        rwidth = self.visit(get_width(node.right))
        if (not isinstance(left, vtypes.VeriloggenNode) and
            not isinstance(right, vtypes.VeriloggenNode) and 
            not isinstance(lwidth, vtypes.VeriloggenNode) and
            not isinstance(rwidth, vtypes.VeriloggenNode)):
            return node.op(left, right, lwidth, rwidth)
        return node

    def visit__UnaryOperator(self, node):
        right = self.visit(node.right)
        rwidth = self.visit(get_width(node.right))
        if (not isinstance(right, vtypes.VeriloggenNode) and 
            not isinstance(rwidth, vtypes.VeriloggenNode)):
            return node.op(right, rwidth) 
        return node

    #---------------------------------------------------------------------------
    def visit_Pointer(self, node):
        var = self.visit(node.var)
        pos = self.visit(node.pos)
        if (not isinstance(var, vtypes.VeriloggenNode) and
            not isinstance(pos, vtypes.VeriloggenNode)):
            return node.op(var, pos)
        return node

    def visit_Slice(self, node):
        var = self.visit(node.var)
        msb = self.visit(node.msb)
        lsb = self.visit(node.lsb)
        if (not isinstance(var, vtypes.VeriloggenNode) and
            not isinstance(msb, vtypes.VeriloggenNode) and
            not isinstance(lsb, vtypes.VeriloggenNode)):
            return node.op(var, msb, lsb)
        return node

    def visit_Cat(self, node):
        vars = [ self.visit(var) for var in node.vars ]
        widths = [ self.visit(get_width(var)) for var in node.vars ]
        for var, width in zip(vars, widths):
            if isinstance(var, vtypes.VeriloggenNode):
                return node
            if isinstance(width, vtypes.VeriloggenNode):
                return node
        return node.op(vars, widths)

    def visit_Repeat(self, node):
        var = self.visit(node.var)
        width = self.visit(get_width(node.var))
        times = self.visit(node.times)
        if (not isinstance(var, vtypes.VeriloggenNode) and
            not isinstance(width, vtypes.VeriloggenNode) and
            not isinstance(times, vtypes.VeriloggenNode)):
            return node.op(var, width, times)
        return node

    def visit_Cond(self, node):
        condition = self.visit(node.condition)
        true_value = self.visit(node.true_value)
        false_value = self.visit(node.false_value)
        if (not isinstance(condition, vtypes.VeriloggenNode) and
            not isinstance(true_value, vtypes.VeriloggenNode) and
            not isinstance(false_value, vtypes.VeriloggenNode)):
            return node.op(condition, true_value, false_value)
        return node

#-------------------------------------------------------------------------------
class ReplaceVisitor(ConstantVisitor):
    def visit_tuple(self, node):
        return tuple([ self.visit(n) for n in node ])

    def visit_list(self, node):
        return [ self.visit(n) for n in node ]

    #---------------------------------------------------------------------------
    def visit__BinaryOperator(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        lwidth = self.visit(get_width(node.left))
        rwidth = self.visit(get_width(node.right))
        if (not isinstance(left, vtypes.VeriloggenNode) and
            not isinstance(right, vtypes.VeriloggenNode) and 
            not isinstance(lwidth, vtypes.VeriloggenNode) and
            not isinstance(rwidth, vtypes.VeriloggenNode)):
            return node.op(left, right, lwidth, rwidth)
        if not isinstance(left, vtypes.VeriloggenNode):
            node.left = left
        if not isinstance(right, vtypes.VeriloggenNode):
            node.right = right
        return node

    def visit__UnaryOperator(self, node):
        right = self.visit(node.right)
        rwidth = self.visit(get_width(node.right))
        if (not isinstance(right, vtypes.VeriloggenNode) and 
            not isinstance(rwidth, vtypes.VeriloggenNode)):
            return node.op(right, rwidth) 
        if not isinstance(right, vtypes.VeriloggenNode):
            node.right = right
        return node

    def visit_Pointer(self, node):
        var = self.visit(node.var)
        pos = self.visit(node.pos)
        if (not isinstance(var, vtypes.VeriloggenNode) and
            not isinstance(pos, vtypes.VeriloggenNode)):
            return node.op(var, pos)
        if not isinstance(var, vtypes.VeriloggenNode):
            node.var = var
        if not isinstance(pos, vtypes.VeriloggenNode):
            node.pos = pos
        return node

    def visit_Slice(self, node):
        var = self.visit(node.var)
        msb = self.visit(node.msb)
        lsb = self.visit(node.lsb)
        if (not isinstance(var, vtypes.VeriloggenNode) and
            not isinstance(msb, vtypes.VeriloggenNode) and
            not isinstance(lsb, vtypes.VeriloggenNode)):
            return node.op(var, msb, lsb)
        if not isinstance(var, vtypes.VeriloggenNode):
            node.var = var
        if not isinstance(msb, vtypes.VeriloggenNode):
            node.msb = msb
        if not isinstance(lsb, vtypes.VeriloggenNode):
            node.lsb = lsb
        return node

    def visit_Cat(self, node):
        vars = [ self.visit(var) for var in node.vars ]
        widths = [ self.visit(get_width(var)) for var in node.vars ]
        node.vars = vars
        for var, width in zip(vars, widths):
            if isinstance(var, vtypes.VeriloggenNode):
                return node
            if isinstance(width, vtypes.VeriloggenNode):
                return node
        return node.op(vars, widths)

    def visit_Repeat(self, node):
        var = self.visit(node.var)
        width = self.visit(get_width(node.var))
        times = self.visit(node.times)
        if (not isinstance(var, vtypes.VeriloggenNode) and
            not isinstance(width, vtypes.VeriloggenNode) and
            not isinstance(times, vtypes.VeriloggenNode)):
            return node.op(var, width, times)
        if not isinstance(var, vtypes.VeriloggenNode):
            node.var = var
        if not isinstance(times, vtypes.VeriloggenNode):
            node.times = times
        return node

    def visit_Cond(self, node):
        condition = self.visit(node.condition)
        true_value = self.visit(node.true_value)
        false_value = self.visit(node.false_value)
        if (not isinstance(condition, vtypes.VeriloggenNode) and
            not isinstance(true_value, vtypes.VeriloggenNode) and
            not isinstance(false_value, vtypes.VeriloggenNode)):
            return node.op(condition, true_value, false_value)
        if not isinstance(condition, vtypes.VeriloggenNode):
            node.condition = condition
        if not isinstance(true_value, vtypes.VeriloggenNode):
            node.true_value = true_value
        if not isinstance(false_value, vtypes.VeriloggenNode):
            node.false_value = false_value
        return node

    #---------------------------------------------------------------------------
    def visit_Posedge(self, node):
        name = self.visit(node.name)
        if not isinstance(name, vtypes.VeriloggenNode):
            node.name = name
        return node
    
    def visit_Negedge(self, node):
        name = self.visit(node.name)
        if not isinstance(name, vtypes.VeriloggenNode):
            node.name = name
        return node
    
    def visit_SensitiveAll(self, node):
        return node
    
    #---------------------------------------------------------------------------
    def visit_Subst(self, node):
        right = self.visit(node.right)
        ldelay = self.visit(node.ldelay) if node.ldelay is not None else None
        rdelay = self.visit(node.rdelay) if node.rdelay is not None else None
        if not isinstance(right, vtypes.VeriloggenNode):
            node.right = right
        if not isinstance(ldelay, vtypes.VeriloggenNode):
            node.ldelay = ldelay
        if not isinstance(rdelay, vtypes.VeriloggenNode):
            node.rdelay = rdelay
        return node

    #---------------------------------------------------------------------------
    def visit_If(self, node):
        condition = self.visit(node.condition)
        self.visit(node.true_statement)
        if node.false_statement is not None:
            self.visit(node.false_statement)
        if not isinstance(condition, vtypes.VeriloggenNode):
            node.condition = condition
        return node

    def visit_For(self, node):
        pre = self.visit(node.pre)
        condition = self.visit(node.condition)
        post = self.visit(node.post)
        self.visit(node.statement)
        if not isinstance(condition, vtypes.VeriloggenNode):
            node.condition = condition
        return node

    def visit_While(self, node):
        condition = self.visit(node.condition)
        self.visit(node.statement)
        if not isinstance(condition, vtypes.VeriloggenNode):
            node.condition = condition
        return node

    def visit_Case(self, node):
        comp = self.visit(node.comp)
        for s in node.statement:
            self.visit(s) 
        if not isinstance(comp, vtypes.VeriloggenNode):
            node.comp = comp
        return node

    def visit_Casex(self, node):
        comp = self.visit(node.comp)
        for s in node.statement:
            self.visit(s) 
        if not isinstance(comp, vtypes.VeriloggenNode):
            node.comp = comp
        return node

    def visit_When(self, node):
        condition = self.visit(node.condition)
        self.visit(node.statement)
        if not isinstance(condition, vtypes.VeriloggenNode):
            node.condition = condition
        return node

    def visit_ScopeIndex(self, node):
        self.visit(node.name)
        index = self.visit(node.index)
        if not isinstance(index, vtypes.VeriloggenNode):
            node.index = index
        return node
        
    def visit_Scope(self, node):
        args = [ self.visit(arg) for arg in node.args ]
        node.args = args
        return node
        
    def visit_SystemTask(self, node):
        args = [ self.visit(a) for a in node.args ]
        node.args = args
        return node
        
    def visit_Event(self, node):
        sensitivity = [ self.visit(s) for s in node.sensitivity ]
        node.sensitivity = sensitivity
        return node

    def visit_Forever(self, node):
        for s in node.statement:
            self.visit(s)
        return node
    
    def visit_Delay(self, node):
        delay = self.visit(node.delay)
        if not isinstance(delay, vtypes.VeriloggenNode):
            node.delay = delay
        return node

    def visit_SingleStatement(self, node):
        self.visit(node.statement)
        return node

    def visit_Function(self, node):
        return node

    def visit_FunctionCall(self, node):
        self.visit(node.func)
        args = [ self.visit(a) for a in node.args ]
        node.args = args
        return node
    
    def visit_Task(self, node):
        return node

    def visit_TaskCall(self, node):
        self.visit(node.func)
        args = [ self.visit(a) for a in node.args ]
        node.args = args
        return node

#-------------------------------------------------------------------------------
class ModuleReplaceVisitor(_CachedVisitor):
    tmp_count = 0
    
    def __init__(self, mod, const_dict=None, submodule=None):
        _CachedVisitor.__init__(self)
        
        if not isinstance(mod, module.Module) and not isinstance(mod, module.Generate):
            raise TypeError("Not supported object type: '%s'", str(type(mod)))
        
        if const_dict is None:
            const_dict = OrderedDict()

        if submodule is None:
            submodule = OrderedDict()

        self.mod = mod
        self.const_dict = const_dict
        self.submodule = submodule

        self.replace_visitor = None
    
    def resolve(self):
        self._update_const_dict()
        self.replace_visitor = ReplaceVisitor(self.const_dict)
        return self.visit(self.mod)

    def _update_const_dict(self):
        params = self.mod.get_params()
        localparams = self.mod.get_localparams()

        unresolved = OrderedDict()
        unresolved.update(params)
        unresolved.update(localparams)

        prev_size = len(unresolved) + 1
        
        while unresolved and len(unresolved) < prev_size:
            prev_size = len(unresolved)
            unresolved = self._update_const_dict_iter(unresolved)
            
        if unresolved:
            varlist = ', '.join(unresolved.keys())
            raise ValueError('Not all parameters could be resolved: %s' % varlist)

    def _update_const_dict_iter(self, unresolved):
        const_visitor = ConstantVisitor(self.const_dict)
        next_unresolved = OrderedDict()
        
        for name, param in unresolved.items():
            value = const_visitor.visit(param.value)
            
            if isinstance(value, vtypes.VeriloggenNode):
                next_unresolved[name] = param
                continue

            if name not in self.const_dict:
                const_visitor.update_const(name, value)
    
        self.const_dict = const_visitor.get_const_dict()
    
        return next_unresolved

    def visit_Module(self, node):
        params = node.get_params()
        for param in params.values():
            if param.width is not None:
                param.width = self.replace_visitor.visit(param.width)
            param.value = self.replace_visitor.visit(param.value)
            
        localparams = node.get_localparams()
        for localparam in localparams.values():
            if localparam.width is not None:
                localparam.width = self.replace_visitor.visit(localparam.width)
            localparam.value = self.replace_visitor.visit(localparam.value)

        ports = node.get_ports()
        for port in ports.values():
            if port.width is not None:
                 port.width = self.replace_visitor.visit(port.width)

        vars = node.get_vars()
        for var in vars.values():
            if var.width is not None:
                var.width = self.replace_visitor.visit(var.width)

        for asg in node.assign:
            self.visit(asg)

        for alw in node.always:
            self.visit(alw)

        for ini in node.initial:
            self.visit(ini)

        for ins in node.instance.values():
            self.visit(ins)

        return node

    def visit__Variable(self, node):
        width = self.replace_visitor.visit(node.width) if node.width is not None else None
        length = self.replace_visitor.visit(node.length) if node.length is not None else None
        initval = self.replace_visitor.visit(node.initval) if node.initval is not None else None
        if not isinstance(width, vtypes.VeriloggenNode):
            node.width = width
        if not isinstance(length, vtypes.VeriloggenNode):
            node.length = length
        if not isinstance(initval, vtypes.VeriloggenNode):
            node.initval = initval
        return node

    def visit_Always(self, node):
        sensitivity = self.replace_visitor.visit(node.sensitivity)
        self.replace_visitor.visit(node.statement)
        if not isinstance(sensitivity, vtypes.VeriloggenNode):
            node.sensitivity = sensitivity
        return node

    def visit_Assign(self, node):
        self.replace_visitor.visit(node.statement)
        return node

    def visit_Initial(self, node):
        for s in node.statement:
            self.replace_visitor.visit(s)
        return node

    def visit_Instance(self, node):
        params = [ (k, self.replace_visitor.visit(v)) for k, v in node.params ]
        ports = [ (k, self.replace_visitor.visit(v)) for k, v in node.ports ]
        node.params = params
        node.ports = ports

        inst_const_dict = OrderedDict()
        for k, v in params:
            inst_const_dict[k] = v

        if isinstance(node.module, (module.StubModule, str)):
            return node

        mod = copy.deepcopy(node.module)
        prev_name = mod.name
        new_name = prev_name

        while True:
            if new_name not in self.submodule:
                self.submodule[new_name] = mod
                self.mod.submodule[new_name] = mod
                mod.name = new_name
                break

            new_name = '_'.join([prev_name, 'copy', str(ModuleReplaceVisitor.tmp_count)])
            ModuleReplaceVisitor.tmp_count += 1
        
        mvisitor = ModuleReplaceVisitor(mod, inst_const_dict, self.submodule)
        mod = mvisitor.resolve()
        node.module = mod
        
        return node

    def visit_GenerateFor(self, node):
        pass

    def visit_GenerateIf(self, node):
        pass
    
#-------------------------------------------------------------------------------
def resolve(m, const_dict=None):
    mvisitor = ModuleReplaceVisitor(m, const_dict)
    return mvisitor.resolve()
