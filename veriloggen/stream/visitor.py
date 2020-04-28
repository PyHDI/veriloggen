from __future__ import absolute_import
from __future__ import print_function

from . import stypes


class _Visitor(object):

    def __init__(self):
        self.visited_node = set()
        self.result_cache = {}

    def generic_visit(self, node):
        raise TypeError("Type '%s' is not supported." % str(type(node)))

    def visit(self, node):
        if node in self.result_cache:
            return self.result_cache[node]

        if node in self.visited_node:
            raise ValueError("Loop detected.")

        self.visited_node.add(node)

        rslt = self._visit(node)
        self.result_cache[node] = rslt
        return rslt

    def _visit(self, node):
        if isinstance(node, stypes.Substream):
            return self.visit_Substream(node)

        if isinstance(node, stypes.RingBuffer):
            return self.visit_RingBuffer(node)

        if isinstance(node, stypes._RingBufferOutput):
            return self.visit__RingBufferOutput(node)

        if isinstance(node, stypes.Scratchpad):
            return self.visit_Scratchpad(node)

        if isinstance(node, stypes._ScratchpadOutput):
            return self.visit__ScratchpadOutput(node)

        if isinstance(node, stypes._Accumulator):
            return self.visit__Accumulator(node)

        if isinstance(node, stypes._BinaryOperator):
            return self.visit__BinaryOperator(node)

        if isinstance(node, stypes._UnaryOperator):
            return self.visit__UnaryOperator(node)

        if isinstance(node, stypes._SpecialOperator):
            return self.visit__SpecialOperator(node)

        if isinstance(node, stypes._ParameterVariable):
            return self.visit__ParameterVariable(node)

        if isinstance(node, stypes._Variable):
            return self.visit__Variable(node)

        if isinstance(node, stypes._Constant):
            return self.visit__Constant(node)

        visitor = getattr(
            self, 'visit_' + node.__class__.__name__, self.generic_visit)
        return visitor(node)

    def visit__BinaryOperator(self, node):
        raise NotImplementedError()

    def visit__UnaryOperator(self, node):
        raise NotImplementedError()

    def visit__SpecialOperator(self, node):
        raise NotImplementedError()

    def visit__Accumulator(self, node):
        raise NotImplementedError()

    def visit_Substream(self, node):
        raise NotImplementedError()

    def visit_RingBuffer(self, node):
        raise NotImplementedError()

    def visit__RingBufferOutput(self, node):
        raise NotImplementedError()

    def visit_Scratchpad(self, node):
        raise NotImplementedError()

    def visit__ScratchpadOutput(self, node):
        raise NotImplementedError()

    def visit__ParameterVariable(self, node):
        raise NotImplementedError()

    def visit__Variable(self, node):
        raise NotImplementedError()

    def visit__Constant(self, node):
        raise NotImplementedError()


class InputVisitor(_Visitor):

    def visit__BinaryOperator(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        return left | right

    def visit__UnaryOperator(self, node):
        right = self.visit(node.right)
        return right

    def visit__SpecialOperator(self, node):
        ret = set()
        for var in node.args:
            var = self.visit(var)
            ret.update(var)
        return ret

    def visit__Accumulator(self, node):
        right = self.visit(node.right)
        size = self.visit(node.size) if node.size is not None else set()
        initval = (self.visit(node.initval)
                   if node.initval is not None else set())
        dependency = (self.visit(node.dependency)
                      if node.dependency is not None else set())
        enable = self.visit(node.enable) if node.enable is not None else set()
        reset = self.visit(node.reset) if node.reset is not None else set()
        return right | size | initval | dependency | enable | reset

    def visit_Substream(self, node):
        return self.visit__SpecialOperator(node)

    def visit_RingBuffer(self, node):
        right = self.visit(node.right)
        enable = self.visit(node.enable) if node.enable is not None else set()
        reset = self.visit(node.reset) if node.reset is not None else set()
        return right | enable | reset

    def visit__RingBufferOutput(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        enable = self.visit(node.enable) if node.enable is not None else set()
        reset = self.visit(node.reset) if node.reset is not None else set()
        return left | right | enable | reset

    def visit_Scratchpad(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        enable = self.visit(node.enable) if node.enable is not None else set()
        reset = self.visit(node.reset) if node.reset is not None else set()
        return left | right | enable | reset

    def visit__ScratchpadOutput(self, node):
        return self.visit__BinaryOperator(node)

    def visit__ParameterVariable(self, node):
        return set([node])

    def visit__Variable(self, node):
        if isinstance(node.input_data, stypes._Numeric):
            return self.visit(node.input_data)
        return set([node])

    def visit__Constant(self, node):
        return set()


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

    def visit__SpecialOperator(self, node):
        ret = set()
        for var in node.args:
            var = self.visit(var)
            ret.update(var)
        mine = set([node]) if node._has_output() else set()
        return ret | mine

    def visit__Accumulator(self, node):
        right = self.visit(node.right)
        size = self.visit(node.size) if node.size is not None else set()
        initval = (self.visit(node.initval)
                   if node.initval is not None else set())
        dependency = (self.visit(node.dependency)
                      if node.dependency is not None else set())
        enable = self.visit(node.enable) if node.enable is not None else set()
        #reset = self.visit(node.reset) if node.reset is not None else set()
        reset = set()
        mine = set([node]) if node._has_output() else set()
        return right | size | initval | dependency | enable | reset | mine

    def visit_Substream(self, node):
        return self.visit__SpecialOperator(node)

    def visit_RingBuffer(self, node):
        right = self.visit(node.right)
        enable = self.visit(node.enable) if node.enable is not None else set()
        #reset = self.visit(node.reset) if node.reset is not None else set()
        reset = set()
        mine = set([node]) if node._has_output() else set()
        return right | enable | reset | mine

    def visit__RingBufferOutput(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        enable = self.visit(node.enable) if node.enable is not None else set()
        #reset = self.visit(node.reset) if node.reset is not None else set()
        reset = set()
        mine = set([node]) if node._has_output() else set()
        return left | right | enable | reset | mine

    def visit_Scratchpad(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        enable = self.visit(node.enable) if node.enable is not None else set()
        #reset = self.visit(node.reset) if node.reset is not None else set()
        reset = set()
        mine = set([node]) if node._has_output() else set()
        return left | right | enable | reset | mine

    def visit__ScratchpadOutput(self, node):
        return self.visit__BinaryOperator(node)

    def visit__ParameterVariable(self, node):
        mine = set([node]) if node._has_output() else set()
        return mine

    def visit__Variable(self, node):
        if isinstance(node.input_data, stypes._Numeric):
            return self.visit(node.input_data)
        mine = set([node]) if node._has_output() else set()
        return mine

    def visit__Constant(self, node):
        mine = set([node]) if node._has_output() else set()
        return mine


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

    def visit__SpecialOperator(self, node):
        ret = set()
        for var in node.args:
            var = self.visit(var)
            ret.update(var)
        mine = set([node])
        return ret | mine

    def visit__Accumulator(self, node):
        right = self.visit(node.right)
        size = self.visit(node.size) if node.size is not None else set()
        initval = (self.visit(node.initval)
                   if node.initval is not None else set())
        dependency = (self.visit(node.dependency)
                      if node.dependency is not None else set())
        enable = self.visit(node.enable) if node.enable is not None else set()
        reset = self.visit(node.reset) if node.reset is not None else set()
        mine = set([node])
        return right | size | initval | dependency | enable | reset | mine

    def visit_Substream(self, node):
        return self.visit__SpecialOperator(node)

    def visit_RingBuffer(self, node):
        right = self.visit(node.right)
        enable = self.visit(node.enable) if node.enable is not None else set()
        reset = self.visit(node.reset) if node.reset is not None else set()
        mine = set([node])
        return right | enable | reset | mine

    def visit__RingBufferOutput(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        enable = self.visit(node.enable) if node.enable is not None else set()
        reset = self.visit(node.reset) if node.reset is not None else set()
        mine = set([node])
        return left | right | enable | reset | mine

    def visit_Scratchpad(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        enable = self.visit(node.enable) if node.enable is not None else set()
        reset = self.visit(node.reset) if node.reset is not None else set()
        mine = set([node])
        return left | right | enable | reset | mine

    def visit__ScratchpadOutput(self, node):
        return self.visit__BinaryOperator(node)

    def visit__ParameterVariable(self, node):
        return set()

    def visit__Variable(self, node):
        if isinstance(node.input_data, stypes._Numeric):
            return self.visit(node.input_data)
        return set()

    def visit__Constant(self, node):
        return set()


class AllVisitor(OperatorVisitor):

    def visit__ParameterVariable(self, node):
        return set([node])

    def visit__Variable(self, node):
        if isinstance(node.input_data, stypes._Numeric):
            return self.visit(node.input_data)
        return set([node])

    def visit__Constant(self, node):
        return set([node])
