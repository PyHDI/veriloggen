from __future__ import absolute_import
from __future__ import print_function

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import vtypes

class ResetVisitor(object):
    def generic_visit(self, node):
        raise TypeError("Type %s is not supported." % str(type(node)))
    
    def visit(self, node):
        if isinstance(node, vtypes._Variable):
            return self.visit__Variable(node)
        
        visitor = getattr(self, 'visit_' + node.__class__.__name__, self.generic_visit)
        return visitor(node)

    def visit__Variable(self, node):
        if node.initval is None:
            return None
        return vtypes.Subst(node, node.initval)

    def visit_Pointer(self, node):
        val = self.visit(node.var)
        if val is None:
            return None
        return vtypes.Subst(vtypes.Pointer(val.left, node.pos), 
                            vtypes.Pointer(val.right, node.pos))

    def visit_Slice(self, node):
        val = self.visit(node.var)
        if val is None:
            return None
        return vtypes.Subst(vtypes.Slice(val.left, node.msb, node.lsb),
                            vtypes.Slice(val.right, node.msb, node.lsb))

    def visit_Cat(self, node):
        left = []
        right = []
        for v in node.vars:
            val = self.visit(v)
            right = vtypes.IntX() if val is None else val.right
            left.append(v)
            right.append(right)
        return vtypes.Subst(vtypes.Cat(tuple(left)), vtypes.Cat(tuple(right)))
