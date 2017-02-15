from __future__ import absolute_import
from __future__ import print_function
import os
import sys
import ast
import inspect
import textwrap
from collections import OrderedDict

import veriloggen.core.vtypes as vtypes
from veriloggen.fsm.fsm import FSM

from . import compiler


def reset():
    compiler._tmp_count = 0


class Thread(vtypes.VeriloggenNode):
    __intrinsics__ = ('run', 'join', 'busy')

    def __init__(self, m, clk, rst, name, targ, datawidth=32):

        self.m = m
        self.clk = clk
        self.rst = rst
        self.name = name
        self.targ = targ
        self.datawidth = datawidth

        self.function_lib = OrderedDict()
        self.intrinsic_functions = OrderedDict()
        self.intrinsic_methods = OrderedDict()

        self.fsm = None
        self.is_child = False
        self.start_state = None
        self.end_state = None

        self.local_objects = {}

    def start(self, *args, **kwargs):
        """ build up a new FSM based on the arguments """

        if self.is_child:
            raise ValueError('already started as a child thread.')

        if self.end_state is not None:
            raise ValueError('already started.')

        frame = inspect.currentframe()
        _locals = frame.f_back.f_locals

        self.local_objects = OrderedDict()
        for key, value in _locals.items():
            self.local_objects[key] = value

        self.fsm = FSM(self.m, self.name, self.clk, self.rst)

        self.start_state = self.fsm.current
        self._synthesize_fsm(self.fsm, args, kwargs)
        self.end_state = self.fsm.current

        return self.fsm

    def extend(self, fsm, *args, **kwargs):
        """ extend a given thread FSM """

        frame = inspect.currentframe()
        _locals = frame.f_back.f_locals

        self.local_objects = OrderedDict()
        for key, value in _locals.items():
            self.local_objects[key] = value

        self._synthesize_fsm(fsm, args, kwargs)

        return fsm

    def run(self, fsm, *args, **kwargs):
        """ start as a child thread """

        if not self.is_child and self.end_state is not None:
            raise ValueError('already started.')

        self.fsm = FSM(self.m, self.name, self.clk, self.rst)
        self.is_child = True

        if self.start_state is None:
            self.start_state = self.fsm.current

        start_flag = (fsm.state == fsm.current)
        self.fsm.goto_from(self.start_state, self.start_state + 1, start_flag)

        self.fsm._set_index(self.start_state + 1)

        if self.end_state is not None:
            return 0

        self._synthesize_fsm(self.fsm, args, kwargs)

        if self.end_state is None:
            self.end_state = self.fsm.current

        return 0

    def join(self, fsm):
        if self.end_state is None:
            raise ValueError('not started')

        end_flag = (self.fsm.state == self.end_state)
        fsm.If(end_flag).goto_next()

        return 0

    def busy(self, fsm):
        if self.end_state is None:
            raise ValueError('not started')

        end_flag = (self.fsm.state == self.end_state)

        return end_flag

    def add_function(self, func):
        name = func.__name__
        if name in self.function_lib:
            raise ValueError(
                'Function {} is already defined'.format(name))
        self.function_lib[name] = func
        return func

    def add_intrinsics(self, *funcs):
        for func in funcs:
            self.intrinsic(func)

    def add_intrinsic_method_prefix(self, obj, prefix):
        funcs = [method for name, method in inspect.getmembers(obj, inspect.ismethod)
                 if name.startswith(prefix)]
        self.add_intrinsics(*funcs)

    def intrinsic(self, func):
        if inspect.isfunction(func):
            return self._add_intrinsic_function(func)
        if inspect.ismethod(func):
            return self._add_intrinsic_method(func)
        raise TypeError("'%s' object is not supported" % str(type(func)))

    def _add_intrinsic_function(self, func):
        name = func.__name__
        if name in self.intrinsic_functions:
            raise ValueError(
                'Intrinsic function {} is already defined'.format(name))
        self.intrinsic_functions[name] = func
        return func

    def _add_intrinsic_method(self, func):
        name = str(func)
        if name in self.intrinsic_methods:
            raise ValueError(
                'Intrinsic method {} is already defined'.format(name))
        self.intrinsic_methods[name] = func
        return func

    def _synthesize_fsm(self, fsm, args, kwargs):

        functions = self._get_functions()

        local_objects = {}
        for key, value in self.local_objects.items():
            local_objects[key] = value

        cvisitor = compiler.CompileVisitor(self.m, self.name, self.clk, self.rst, fsm,
                                           functions, self.intrinsic_functions,
                                           self.intrinsic_methods, local_objects,
                                           datawidth=self.datawidth)

        text = textwrap.dedent(inspect.getsource(self.targ))
        tree = ast.parse(text).body[0]

        # stack a new scope frame
        cvisitor.pushScope(ftype='call')

        # args -> scope variable
        args_code = []
        for pos, arg in enumerate(args):
            baseobj = tree.args.args[pos]
            argname = (baseobj.id
                       if isinstance(baseobj, ast.Name)  # python 2
                       else baseobj.arg)  # python 3
            cvisitor.scope.addVariable(argname, arg)
            args_code.append(argname)

        # kwargs -> scope variable
        kwargs_code = []
        for key, val in sorted(kwargs.items(), key=lambda x: x[0]):
            cvisitor.scope.addVariable(key, val)
            kwargs_code.append('{}={}'.format(key, key))

        # call AST
        args_text = ', '.join(args_code + kwargs_code)
        call_code = ''.join([self.targ.__name__, '(', args_text, ')'])
        _call_ast = ast.parse(call_code)

        # start visit
        cvisitor.visit(_call_ast)

        # clean-up jump conditions
        cvisitor.clearBreak()
        cvisitor.clearContinue()
        cvisitor.clearReturn()
        cvisitor.clearReturnVariable()

        # return to the previous scope frame
        cvisitor.popScope()

    def _get_functions(self):
        codes = []

        for func_name, func in self.function_lib.items():
            codes.append(textwrap.dedent(inspect.getsource(func)))

        if self.targ.__name__ not in self.function_lib:
            codes.append(textwrap.dedent(inspect.getsource(self.targ)))

        text = '\n'.join(codes)
        _ast = ast.parse(text)

        functionvisitor = compiler.FunctionVisitor()
        functionvisitor.visit(_ast)
        functions = functionvisitor.getFunctions()

        return functions
