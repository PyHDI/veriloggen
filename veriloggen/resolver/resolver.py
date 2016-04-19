from __future__ import absolute_import
from __future__ import print_function
import os
import sys
from collections import OrderedDict

import veriloggen.core.vtypes as vtypes
import veriloggen.core.module as module

def get_width(node):
    if isinstance(node, int):
        return 32
    if isinstance(node, vtypes.AnyType):
        return 32
    ret = node.bit_length()
    if ret is None:
        return 32
    return ret

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
        if isinstance(node, vtypes._BinaryOperator):
            return self.visit__BinaryOperator(node)
        
        if isinstance(node, vtypes._UnaryOperator):
            return self.visit__UnaryOperator(node)

        if isinstance(node, vtypes._Variable):
            return self.visit__Variable(node)

        raise TypeError("Type %s is not supported." % str(type(node)))
    
    def visit_int(self, node):
        return node
    
    def visit_bool(self, node):
        return node
    
    def visit_float(self, node):
        return node
    
    def visit_str(self, node):
        return node
    
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

    def visit__Variable(self, node):
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
    
    #---------------------------------------------------------------------------
    def visit_Parameter(self, node):
        return self._visit_param(node)

    def visit_Localparam(self, node):
        return self._visit_param(node)

    #---------------------------------------------------------------------------
    def visit_AnyType(self, node):
        return self._visit_param(node)

    
#-------------------------------------------------------------------------------
def resolve_constant(m):
    const_dict = _get_const_dict(m)
    _resolve_module(m, const_dict)
    return m

#-------------------------------------------------------------------------------
def _get_const_dict(m):
    params = m.get_params()
    localparams = m.get_localparams()
    const_dict = _resolve_params(params, localparams)
    return const_dict

def _resolve_params(params, localparams):
    unresolved = OrderedDict()
    unresolved.update(params)
    unresolved.update(localparams)
    
    const_dict = OrderedDict()
    prev_size = len(unresolved) + 1
    
    while unresolved and len(unresolved) < prev_size:
        prev_size = len(unresolved)
        const_dict, unresolved = _resolve_params_iter(const_dict, unresolved)

    if unresolved:
        varlist = ', '.join(unresolved.keys())
        raise ValueError('Not all parameters could be resolved: %s' % varlist)

    return const_dict

def _resolve_params_iter(const_dict, unresolved):
    const_visitor = ConstantVisitor(const_dict)
    next_unresolved = OrderedDict()
    
    for name, param in unresolved.items():
        value = const_visitor.visit(param.value)
        
        if isinstance(value, vtypes.VeriloggenNode):
            next_unresolved[name] = param
            continue
        
        const_visitor.update_const(name, value)

    const_dict = const_visitor.get_const_dict()

    return const_dict, next_unresolved

#-------------------------------------------------------------------------------
def _resolve_module(m, const_dict):
    const_visitor = ConstantVisitor(const_dict)
    
    params = m.get_params()
    for param in params.values():
        if param.width is not None:
            param.width = const_visitor.visit(param.width)
        param.value = const_visitor.visit(param.value)

    localparams = m.get_localparams()
    for localparam in localparams.values():
        if localparam.width is not None:
            localparam.width = const_visitor.visit(localparam.width)
        localparam.value = const_visitor.visit(localparam.value)

    ports = m.get_ports()
    for port in ports.values():
        if port.width is not None:
            port.width = const_visitor.visit(port.width)

    vars = m.get_vars()
    for var in vars.values():
        if var.width is not None:
            var.width = const_visitor.visit(var.width)
