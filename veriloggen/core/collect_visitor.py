from __future__ import absolute_import
from __future__ import print_function

import os
import sys
import copy

import veriloggen.core.vtypes as vtypes


class CollectVisitor(object):

    def __init__(self):
        self.names = set()

    def generic_visit(self, node):
        raise TypeError("Type %s is not supported." % str(type(node)))

    def visit(self, node):
        if node is None:
            return None
        if isinstance(node, vtypes._Variable):
            return self.visit__Variable(node)
        if isinstance(node, vtypes._BinaryOperator):
            return self.visit__BinaryOperator(node)
        if isinstance(node, vtypes._UnaryOperator):
            return self.visit__UnaryOperator(node)

        visitor = getattr(
            self, 'visit_' + node.__class__.__name__, self.generic_visit)
        return visitor(node)

    def visit_Int(self, node):
        return

    def visit_Float(self, node):
        return

    def visit_Str(self, node):
        return

    def visit_bool(self, node):
        return

    def visit_int(self, node):
        return

    def visit_str(self, node):
        return

    def visit_float(self, node):
        return

    def visit__Variable(self, node):
        self.names.add(node.name)

        self.visit(node.width)
        if hasattr(node, 'initval'):
            self.visit(node.initval)

    def visit_Pointer(self, node):
        self.visit(node.var)
        self.visit(node.pos)

    def visit_Slice(self, node):
        self.visit(node.var)
        self.visit(node.msb)
        self.visit(node.lsb)

    def visit_Cat(self, node):
        for var in node.vars:
            self.visit(var)

    def visit_Repeat(self, node):
        self.visit(node.var)
        self.visit(node.times)

    def visit_Cond(self, node):
        self.visit(node.condition)
        self.visit(node.true_value)
        self.visit(node.false_value)

    def visit__BinaryOperator(self, node):
        self.visit(node.left)
        self.visit(node.right)

    def visit__UnaryOperator(self, node):
        self.visit(node.right)

    def visit_EmbeddedNumeric(self, node):
        return
