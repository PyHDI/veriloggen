from __future__ import absolute_import
from __future__ import print_function

from . import dtypes

#-------------------------------------------------------------------------------
class _Visitor(object):
    def generic_visit(self, node):
        raise TypeError("Type '%s' is not supported." % str(type(node)))
    
    def visit(self, node):
        if isinstance(node, dtypes._BinaryOperator):
            return self.visit__BinaryOperator(node)

        if isinstance(node, dtypes._UnaryOperator):
            return self.visit__UnaryOperator(node)

        if isinstance(node, dtypes._Variable):
            return self.visit__Variable(node)

        if isinstance(node, dtypes._Constant):
            return self.visit__Constant(node)

        visitor = getattr(self, 'visit_' + node.__class__.__name__, self.generic_visit)
        return visitor(node)

    def visit__BinaryOperator(self, node):
        raise NotImplementedError()

    def visit__UnaryOperator(self, node):
        raise NotImplementedError()
    
    def visit__Variable(self, node):
        raise NotImplementedError()
        
    def visit__Constant(self, node):
        raise NotImplementedError()

    def visit_Pointer(self, node):
        raise NotImplementedError()
    
    def visit_Slice(self, node):
        raise NotImplementedError()
    
    def visit_Cat(self, node):
        raise NotImplementedError()
    
    def visit_Repeat(self, node):
        raise NotImplementedError()
    
    def visit_Cond(self, node):
        raise NotImplementedError()

#-------------------------------------------------------------------------------    
class InputVisitor(_Visitor):
    def visit__BinaryOperator(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        return left | right

    def visit__UnaryOperator(self, node):
        right = self.visit(node.right)
        return right
    
    def visit__Variable(self, node):
        return set([node])
        
    def visit__Constant(self, node):
        return set()

    def visit_Pointer(self, node):
        var = self.visit(node.var)
        pos = self.visit(node.pos)
        return var | pos
    
    def visit_Slice(self, node):
        var = self.visit(node.var)
        msb = self.visit(node.msb)
        lsb = self.visit(node.lsb)
        return var | msb | lsb
    
    def visit_Cat(self, node):
        ret = set()
        for var in node.vars:
            var = self.visit(node.var)
            ret.update(var)
        return ret
    
    def visit_Repeat(self, node):
        var = self.visit(node.var)
        times = self.visit(node.times)
        return var | times
    
    def visit_Cond(self, node):
        condition = self.visit(node.condition)
        true_value = self.visit(node.true_value)
        false_value = self.visit(node.false_value)
        return condition | true_value | false_value
    
#-------------------------------------------------------------------------------    
class OutputVisitor(_Visitor):
    def visit__BinaryOperator(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        mine = set([node]) if node._has_output() else set()
        return left | right | mine

    def visit__UnaryOperator(self, node):
        right = self.visit(node.right)
        mine = set([node]) if node._has_output() else set()
        return right | mine
    
    def visit__Variable(self, node):
        mine = set([node]) if node._has_output() else set()
        return mine
        
    def visit__Constant(self, node):
        mine = set([node]) if node._has_output() else set()
        return mine

    def visit_Pointer(self, node):
        var = self.visit(node.var)
        pos = self.visit(node.pos)
        mine = set([node]) if node._has_output() else set()
        return var | pos | mine
    
    def visit_Slice(self, node):
        var = self.visit(node.var)
        msb = self.visit(node.msb)
        lsb = self.visit(node.lsb)
        mine = set([node]) if node._has_output() else set()
        return var | msb | lsb | mine
    
    def visit_Cat(self, node):
        ret = set()
        for var in node.vars:
            var = self.visit(node.var)
            ret.update(var)
        mine = set([node]) if node._has_output() else set()
        return ret | mine
    
    def visit_Repeat(self, node):
        var = self.visit(node.var)
        times = self.visit(node.times)
        mine = set([node]) if node._has_output() else set()
        return var | times | mine
    
    def visit_Cond(self, node):
        condition = self.visit(node.condition)
        true_value = self.visit(node.true_value)
        false_value = self.visit(node.false_value)
        mine = set([node]) if node._has_output() else set()
        return condition | true_value | false_value | mine

#-------------------------------------------------------------------------------    
class OperatorVisitor(_Visitor):
    def visit__BinaryOperator(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        mine = set([node])
        return left | right | mine

    def visit__UnaryOperator(self, node):
        right = self.visit(node.right)
        mine = set([node])
        return right | mine
    
    def visit__Variable(self, node):
        return set()
        
    def visit__Constant(self, node):
        return set()

    def visit_Pointer(self, node):
        var = self.visit(node.var)
        pos = self.visit(node.pos)
        mine = set([node])
        return var | pos | mine
    
    def visit_Slice(self, node):
        var = self.visit(node.var)
        msb = self.visit(node.msb)
        lsb = self.visit(node.lsb)
        mine = set([node])
        return var | msb | lsb | mine
    
    def visit_Cat(self, node):
        ret = set()
        for var in node.vars:
            var = self.visit(node.var)
            ret.update(var)
        mine = set([node])
        return ret | mine
    
    def visit_Repeat(self, node):
        var = self.visit(node.var)
        times = self.visit(node.times)
        mine = set([node])
        return var | times | mine
    
    def visit_Cond(self, node):
        condition = self.visit(node.condition)
        true_value = self.visit(node.true_value)
        false_value = self.visit(node.false_value)
        mine = set([node])
        return condition | true_value | false_value | mine

class AllVisitor(OperatorVisitor):
    def visit__Variable(self, node):
        return set([node])
        
    def visit__Constant(self, node):
        return set([node])
