from __future__ import absolute_import
from __future__ import print_function

import os
import sys

import veriloggen.core.vtypes as vtypes


class ResetVisitor(object):

    def generic_visit(self, node):
        raise TypeError("Type %s is not supported." % str(type(node)))

    def visit(self, node):
        if isinstance(node, vtypes._Variable):
            return self.visit__Variable(node)

        visitor = getattr(
            self, 'visit_' + node.__class__.__name__, self.generic_visit)
        return visitor(node)

    def visit__Variable(self, node):
        if node.initval is None:
            return None
        return vtypes.Subst(node, node.initval)

    def visit_Pointer(self, node):
        val = self.visit(node.var)
        if val is None:
            return None
        left = vtypes.Pointer(val.left, node.pos)
        if not isinstance(val.right, (vtypes._Variable, vtypes.Scope)):
            if isinstance(val.right, (int, bool)):
                val_right = vtypes.Int(val.right)
            elif isinstance(val.right, float):
                val_right = vtypes.Float(val.right)
            else:
                raise TypeError("unsupported value type: %s" % str(val.right))
            right = (val_right >> node.pos) & 0x1
        else:
            right = vtypes.Pointer(val.right, node.pos)
        return vtypes.Subst(left, right)

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
