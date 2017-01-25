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

from .scope import ScopeName, ScopeFrameList, ScopeFrame
from .operator import getVeriloggenOp
from .optimizer import optimize

_tmp_count = 0


def reset():
    global _tmp_count
    _tmp_count = 0


def _tmp_name(prefix='_tmp_thread'):
    global _tmp_count
    v = _tmp_count
    _tmp_count += 1
    ret = '_'.join([prefix, str(v)])
    return ret


class ThreadGenerator(vtypes.VeriloggenNode):

    def __init__(self, m, clk, rst, datawidth=32):
        self.m = m
        self.clk = clk
        self.rst = rst
        self.datawidth = datawidth
        self.func_lib = OrderedDict()

    def add(self, func):
        name = func.__name__
        if name in self.func_lib:
            raise ValueError(
                'function {} is already defined in ThreadGenerator.'.format(name))
        self.func_lib[name] = func
        return func

    def generate_fsm(self, name, targ, *args, **kwargs):
        frame = inspect.currentframe()
        _locals = frame.f_back.f_locals
        _globals = frame.f_back.f_globals
        local_objects = OrderedDict()
        global_objects = OrderedDict()

        for key, value in _locals.items():
            if isinstance(value, vtypes.VeriloggenNode):
                local_objects[key] = value

        for key, value in _globals.items():
            if isinstance(value, vtypes.VeriloggenNode):
                global_objects[key] = value

        codes = []

        for func_name, func in self.func_lib.items():
            codes.append(textwrap.dedent(inspect.getsource(func)))

        if targ.__name__ not in self.func_lib:
            codes.append(textwrap.dedent(inspect.getsource(targ)))

        text = '\n'.join(codes)
        _ast = ast.parse(text)

        functionvisitor = FunctionVisitor()
        functionvisitor.visit(_ast)
        functions = functionvisitor.getFunctions()

        compilevisitor = CompileVisitor(self.m, name, self.clk, self.rst,
                                        functions, local_objects, global_objects,
                                        self.datawidth)

        # function argument
        args_code = []
        for i, arg in enumerate(args):
            argkey = '__arg_%d' % i
            local_objects[argkey] = arg
            args_code.append(argkey)

        kwargs_code = []
        i = 0
        for k, v in sorted(kwargs.items(), key=lambda x: x[0]):
            argkey = '__kwarg_%d' % i
            local_objects[argkey] = v
            kwargs_code.append('{}={}'.format(k, argkey))
            i += 1

        args_text = ', '.join(args_code + kwargs_code)
        call_code = ''.join([targ.__name__, '(', args_text, ')'])

        _call_ast = ast.parse(call_code)
        compilevisitor.visit(_call_ast)

        return compilevisitor.fsm


class FunctionVisitor(ast.NodeVisitor):

    def __init__(self):
        self.functions = {}

    def getFunctions(self):
        return self.functions

    def visit_FunctionDef(self, node):
        self.functions[node.name] = node


class CompileVisitor(ast.NodeVisitor):

    def __init__(self, m, name, clk, rst,
                 functions, local_objects, global_objects, datawidth=32):

        self.m = m
        self.name = name
        self.clk = clk
        self.rst = rst

        self.functions = functions
        self.local_objects = local_objects
        self.global_objects = global_objects
        self.datawidth = datawidth

        self.scope = ScopeFrameList()
        self.fsm = FSM(self.m, self.name, self.clk, self.rst)
        self.loop_info = OrderedDict()

        for func in functions.values():
            self.scope.addFunction(func)

    #-------------------------------------------------------------------------
    def visit_Import(self, node):
        raise TypeError("{} is not supported.".format(type(node)))

    def visit_ImportFrom(self, node):
        raise TypeError("{} is not supported.".format(type(node)))

    def visit_ClassDef(self, node):
        raise TypeError("{} is not supported.".format(type(node)))

    #-------------------------------------------------------------------------
    def visit_FunctionDef(self, node):
        self.scope.addFunction(node)

    def visit_Assign(self, node):
        if self.skip():
            return
        right = self.visit(node.value)
        left = self.visit(node.targets[0])
        self.setBind(left, right)
        self.setFsm()
        self.incFsmCount()

    def visit_AugAssign(self, node):
        if self.skip():
            return
        right = self.visit(node.value)
        left = self.visit(node.target)
        op = getVeriloggenOp(node.op)
        if op is None:
            raise TypeError("Unsupported BinOp: %s" % str(node.op))
        rslt = op(left, right)
        self.setBind(left, rslt)
        self.setFsm()
        self.incFsmCount()

    def visit_IfExp(self, node):
        test = self.visit(node.test)  # if condition
        body = self.visit(node.body)
        orelse = self.visit(node.orelse)
        rslt = vtypes.Cond(test, body, orelse)
        return rslt

    def visit_If(self, node):
        if self.skip():
            return
        test = self.visit(node.test)  # if condition

        cur_count = self.getFsmCount()
        self.incFsmCount()
        true_count = self.getFsmCount()

        self.pushScope()

        for b in node.body:  # true statement
            self.visit(b)

        self.popScope()

        mid_count = self.getFsmCount()

        if len(node.orelse) == 0:
            self.setFsm(cur_count, true_count, test, mid_count)
            return

        self.incFsmCount()
        false_count = self.getFsmCount()

        self.pushScope()

        for b in node.orelse:  # false statement
            self.visit(b)

        self.popScope()

        end_count = self.getFsmCount()
        self.setFsm(cur_count, true_count, test, false_count)
        self.setFsm(mid_count, end_count)

    def visit_While(self, node):
        if self.skip():
            return

        # loop condition
        test = self.visit(node.test)

        begin_count = self.getFsmCount()
        self.incFsmCount()
        body_begin_count = self.getFsmCount()

        self.pushScope()

        for b in node.body:
            self.visit(b)

        self.popScope()

        body_end_count = self.getFsmCount()
        self.incFsmCount()
        loop_exit_count = self.getFsmCount()

        self.setFsm(begin_count, body_begin_count, test, loop_exit_count)
        self.setFsm(body_end_count, begin_count)

        unresolved_break = self.getUnresolvedBreak()
        for b in unresolved_break:
            self.setFsm(b, loop_exit_count)

        unresolved_continue = self.getUnresolvedContinue()
        for c in unresolved_continue:
            self.setFsm(c, begin_count)

        self.clearBreak()
        self.clearContinue()

        self.setFsmLoop(begin_count, body_end_count)

    def visit_For(self, node):
        if self.skip():
            return
        if (isinstance(node.iter, ast.Call) and
            isinstance(node.iter.func, ast.Name) and
                node.iter.func.id == 'range'):
            # typical for-loop

            if len(node.iter.args) == 0:
                raise TypeError()
            begin_node = (vtypes.Int(0)
                          if len(node.iter.args) == 1
                          else self.visit(node.iter.args[0]))

            end_node = (self.visit(node.iter.args[0])
                        if len(node.iter.args) == 1
                        else self.visit(node.iter.args[1]))

            step_node = (vtypes.Int(1)
                         if len(node.iter.args) < 3
                         else self.visit(node.iter.args[2]))

            iter_node = self.visit(node.target)
            cond_node = vtypes.LessThan(iter_node, end_node)
            update_node = vtypes.Plus(iter_node, step_node)

            self.pushScope()

            # initialize
            self.setBind(iter_node, begin_node)
            self.setFsm()
            self.incFsmCount()

            # condition check
            check_count = self.getFsmCount()
            self.incFsmCount()
            body_begin_count = self.getFsmCount()

            for b in node.body:
                self.visit(b)

            self.popScope()

            body_end_count = self.getFsmCount()

            # update
            self.setBind(iter_node, update_node)
            self.incFsmCount()
            loop_exit_count = self.getFsmCount()

            self.setFsm(body_end_count, check_count)
            self.setFsm(check_count, body_begin_count,
                        cond_node, loop_exit_count)

            unresolved_break = self.getUnresolvedBreak()
            for b in unresolved_break:
                self.setFsm(b, loop_exit_count)

            unresolved_continue = self.getUnresolvedContinue()
            for c in unresolved_continue:
                self.setFsm(c, body_end_count)

            self.clearBreak()
            self.clearContinue()

            self.setFsmLoop(check_count, body_end_count, iter_node, step_node)

    #--------------------------------------------------------------------------
    def visit_Call(self, node):
        if self.skip():
            return

        if isinstance(node.func, ast.Name):
            return self._call_Name(node)

        if isinstance(node.func, ast.Attribute):
            return self._call_Attribute(node)

        raise NameError("function '%s' is not defined" % name)

    def _call_Name(self, node):
        name = node.func.id

        # system task
        if name == 'print':  # display
            return self._call_Name_print(node)
        if name == 'int':
            return self._call_Name_int(node)

        # function call
        return self._call_Name_function(node, name)

    def _call_Name_print(self, node):
        # prepare the argument values
        argvalues = []
        formatstring_list = []
        for arg in node.args:
            if isinstance(arg, ast.BinOp) and isinstance(arg.op, ast.Mod) and isinstance(arg.left, ast.Str):
                # format string in print statement
                values, form = self._print_binop_mod(arg)
                argvalues.extend(values)
                formatstring_list.append(form)
                formatstring_list.append(" ")
            elif isinstance(arg, ast.Tuple):
                for e in arg.elts:
                    value = self.visit(e)
                    if isinstance(value, vtypes.Str):
                        formatstring_list.append(value.value)
                        formatstring_list.append(" ")
                    else:
                        argvalues.append(value)
                        formatstring_list.append("%d")
                        formatstring_list.append(" ")
            else:
                value = self.visit(arg)
                if isinstance(value, vtypes.Str):
                    formatstring_list.append(value.value)
                    formatstring_list.append(" ")
                else:
                    argvalues.append(value)
                    formatstring_list.append("%d")
                    formatstring_list.append(" ")

        formatstring_list = formatstring_list[:-1]

        args = []
        args.append(vtypes.Str(''.join(formatstring_list)))
        args.extend(argvalues)

        left = None
        right = vtypes.SystemTask('display', *args)
        self.setBind(left, right)

        self.setFsm()
        self.incFsmCount()

        return right

    def _print_binop_mod(self, arg):
        values = []
        if isinstance(arg.right, ast.Tuple) or isinstance(arg.right, ast.List):
            for e in arg.right.elts:
                values.append(self.visit(e))
        else:
            values.append(self.visit(arg.right))
        form = arg.left.s
        return values, form

    def _call_Name_int(self, node):
        if len(node.args) > 1:
            raise TypeError("Too much arguments for 'int()'")
        argvalues = []
        for arg in node.args:
            argvalues.append(self.visit(arg))
        return argvalues[0]

    def _call_Name_function(self, node, name):
        tree = self.getFunction(name)
        if tree is None:
            raise NameError("function '%s' is not defined" % name)

        # prepare the argument values
        args = []
        keywords = []
        for arg in node.args:
            args.append(self.visit(arg))
        for key in node.keywords:
            keywords.append(self.visit(key.value))

        # stack a new scope frame
        self.pushScope(ftype='call')

        # node.args -> variable and binding
        for pos, arg in enumerate(node.args):
            baseobj = tree.args.args[pos]
            argname = (baseobj.id
                       if isinstance(baseobj, ast.Name)  # python 2
                       else baseobj.arg)  # python 3
            left = self.getVariable(argname, store=True)
            right = args[pos]
            self.setBind(left, right)

        # kwargs
        for pos, key in enumerate(node.keywords):
            left = self.getVariable(key.arg, store=True)
            right = keywords[pos]
            self.setBind(left, right)

        # default values of kwargs
        kwargs_size = len(tree.args.defaults)
        if kwargs_size > 0:
            for arg, val in zip(tree.args.args[-kwargs_size:], tree.args.defaults):
                argname = (arg.id if isinstance(arg, ast.Name)  # python 2
                           else arg.arg)  # python 3
                var = self.scope.searchVariable(argname, store=True)
                # not defined yet
                if var is None:
                    left = self.getVariable(argname, store=True)
                    right = self.visit(val)
                    self.setBind(left, right)

        self.setFsm()
        self.incFsmCount()

        # visit the function definition
        ret = self.__visit_FunctionDef(tree)

        # fsm jump by return statement
        end_count = self.getFsmCount()
        unresolved_return = self.getUnresolvedReturn()
        for ret_count, value in unresolved_return:
            self.setFsm(ret_count, end_count)

        # clean-up jump conditions
        self.clearBreak()
        self.clearContinue()
        self.clearReturn()
        self.clearReturnVariable()

        # return to the previous scope frame
        self.popScope()

        return ret

    def __visit_FunctionDef(self, node):
        self.generic_visit(node)
        retvar = self.getReturnVariable()
        if retvar is not None:
            return retvar
        return vtypes.Int(0)

    def _call_Attribute(self, node):
        attr_value = self.visit(node.func.value)
        raise NotImplementedError('%s' % str(ast.dump(node.func)))

    #--------------------------------------------------------------------------
    def visit_Nonlocal(self, node):
        for name in node.names:
            self.addNonlocal(name)

    def visit_Global(self, node):
        for name in node.names:
            self.addGlobal(name)

    def visit_Pass(self, node):
        pass

    def visit_Break(self, node):
        self.addBreak()
        self.incFsmCount()

    def visit_Continue(self, node):
        self.addContinue()
        self.incFsmCount()

    def visit_Return(self, node):
        if node.value is None:
            self.addReturn(None)
            self.incFsmCount()
            return None

        retvar = self.getReturnVariable()
        if retvar is not None:
            left = retvar
            right = self.visit(node.value)
            self.setBind(left, right)
            self.addReturn(right)
            self.incFsmCount()
            return left

        tmp = self.getTmpVariable()
        self.setReturnVariable(tmp)
        left = tmp
        right = self.visit(node.value)
        self.setBind(left, right)
        self.addReturn(right)
        self.incFsmCount()
        return left

    def visit_Num(self, node):
        if isinstance(node.n, int):
            return vtypes.Int(node.n)
        return vtypes.Constant(node.n)

    def visit_Str(self, node):
        return vtypes.Str(node.s)

    def visit_UnaryOp(self, node):
        op = getVeriloggenOp(node.op)
        value = self.visit(node.operand)
        rslt = op(value)
        return self.optimize(rslt)

    def visit_BoolOp(self, node):
        op = getVeriloggenOp(node.op)
        if op is None:
            raise TypeError("Unsupported BinOp: %s" % str(node.op))
        rslt = self.visit(node.values[0])
        for v in node.values[1:]:
            rslt = op(rslt, self.visit(v))
        return self.optimize(rslt)

    def visit_BinOp(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        op = getVeriloggenOp(node.op)
        if op is None:
            raise TypeError("Unsupported BinOp: %s" % str(node.op))
        if isinstance(left, vtypes.Str) or isinstance(right, vtypes.Str):
            if op == vtypes.Plus:
                return self._string_operation_plus(left, right)
            raise TypeError("Can not generate a corresponding node")
        rslt = op(left, right)
        return self.optimize(rslt)

    def _string_operation_plus(self, left, right):
        if not isinstance(left, vtypes.Str) or not isinstance(right, vtypes.Str):
            raise TypeError("'+' operation requires two string arguments")
        return vtypes.Str(left.value + right.value)

    def visit_Compare(self, node):
        left = self.visit(node.left)
        ops = [getVeriloggenOp(op) for op in node.ops]
        comparators = [self.visit(comp) for comp in node.comparators]
        rslts = []
        for i, op in enumerate(ops):
            if i == 0:
                rslts.append(op(left, comparators[i]))
            else:
                rslts.append(op(comparators[i - 1], comparators[i]))
        if len(rslts) == 1:
            return rslts[0]
        ret = None
        for r in rslts:
            if ret:
                ret = vtypes.Land(ret, r)
            else:
                ret = r
        return ret

    def visit_NameConstant(self, node):
        # for Python 3.4
        if node.value == True:
            return vtypes.Int(1)
        if node.value == False:
            return vtypes.Int(0)
        if node.value == None:
            return vtypes.Int(0)
        raise TypeError("%s in NameConst.value is not supported." %
                        str(node.value))

    def visit_Name(self, node):
        # for Python 3.3 or older
        if node.id == 'True':
            return vtypes.Int(1)
        if node.id == 'False':
            return vtypes.Int(0)
        if node.id == 'None':
            return vtypes.Int(0)

        store = isinstance(node.ctx, ast.Store)
        name = self.getVariable(node.id, store)
        return name

    def visit_Print(self, node):
        # for Python 2.x
        # prepare the argument values
        argvalues = []
        formatstring_list = []
        for arg in node.values:
            if isinstance(arg, ast.BinOp) and isinstance(arg.op, ast.Mod) and isinstance(arg.left, ast.Str):
                # format string in print statement
                values, form = self._print_binop_mod(arg)
                argvalues.extend(values)
                formatstring_list.append(form)
                formatstring_list.append(" ")
            elif isinstance(arg, ast.Tuple):
                for e in arg.elts:
                    value = self.visit(e)
                    if isinstance(value, vtypes.Str):
                        formatstring_list.append(value.value)
                        formatstring_list.append(" ")
                    else:
                        argvalues.append(value)
                        formatstring_list.append("%d")
                        formatstring_list.append(" ")
            else:
                value = self.visit(arg)
                if isinstance(value, vtypes.Str):
                    formatstring_list.append(value.value)
                    formatstring_list.append(" ")
                else:
                    argvalues.append(value)
                    formatstring_list.append("%d")
                    formatstring_list.append(" ")

        formatstring_list = formatstring_list[:-1]

        args = []
        args.append(vtypes.Str(''.join(formatstring_list)))
        args.extend(argvalues)

        left = None
        right = vtypes.SystemTask('display', *args)
        self.setBind(left, right)

        self.setFsm()
        self.incFsmCount()

        return right

    def visit_Attribute(self, node):
        value = self.visit(node.value)
        attr = node.attr
        if isinstance(value, vtypes._Variable) and attr == 'value':
            return value
        raise TypeError('attribute access is not supported')

    #-------------------------------------------------------------------------
    def skip(self):
        val = self.hasBreak() or self.hasContinue() or self.hasReturn()
        return val

    def makeVariable(self, name, width=None):
        signame = _tmp_name('_'.join(['_thread', self.name, name]))
        if width is None:
            width = self.datawidth
        return self.m.Reg(signame, width)

    def getVariable(self, name, store=False):
        var = self.scope.searchVariable(name, store)
        if var is None:
            if not store:
                if name in self.local_objects:
                    return self.local_objects[name]
                if name in self.global_objects:
                    return self.global_objects[name]
                raise NameError("name '%s' is not defined" % name)
            var = self.makeVariable(name)
            self.scope.addVariable(name, var)
            var = self.scope.searchVariable(name)
        return var

    def getTmpVariable(self):
        name = _tmp_name('tmp')
        var = self.getVariable(name)
        return var

    def addNonlocal(self, name):
        self.scope.addNonlocal(name)

    def addGlobal(self, name):
        self.scope.addGlobal(name)

    def getFunction(self, name):
        func = self.scope.searchFunction(name)
        if func is None:
            raise NameError("function '%s' is not defined" % name)
        return func

    def setBind(self, var, value, cond=None):
        opt_value = self.optimize(value) if var is not None else value
        opt_cond = (self.optimize(cond)
                    if cond is not None and var is not None
                    else None)
        subst = (vtypes.SingleStatement(opt_value)
                 if var is None else var(opt_value))
        self.fsm._add_statement([subst], cond=opt_cond)

        state = self.getFsmCount()
        vname = var.name if var is not None else None
        self.scope.addBind(state, vname, value, cond)

    #-------------------------------------------------------------------------
    def optimize(self, node):
        return optimize(node)

    #-------------------------------------------------------------------------
    def setFsm(self, src=None, dst=None, cond=None, else_dst=None):
        if src is None:
            src = self.fsm.current
        if dst is None:
            dst = src + 1
        self.fsm.goto_from(src, dst, cond, else_dst)

    def incFsmCount(self):
        self.fsm.inc()

    def getFsmCount(self):
        return self.fsm.current

    #-------------------------------------------------------------------------
    def setFsmLoop(self, begin, end, iter_node=None, step_node=None):
        self.loop_info[(begin, end)] = (iter_node, step_node)

    def getFsmLoops(self):
        return self.loop_info

    def getFsmCandidateLoops(self, pos):
        candidates = [(b, e) for (b, e), (inode, unode)
                      in self.loop_info.items() if b <= pos and pos <= e]
        return candidates

    #-------------------------------------------------------------------------
    def getCurrentScope(self):
        return self.scope.getCurrent()

    def pushScope(self, name=None, ftype=None):
        self.scope.pushScopeFrame(name, ftype)

    def popScope(self):
        self.scope.popScopeFrame()

    #-------------------------------------------------------------------------
    def addBreak(self):
        count = self.getFsmCount()
        self.scope.addBreak(count)

    def addContinue(self):
        count = self.getFsmCount()
        self.scope.addContinue(count)

    def addReturn(self, value):
        count = self.getFsmCount()
        self.scope.addReturn(count, value)

    def hasBreak(self):
        return self.scope.hasBreak()

    def hasContinue(self):
        return self.scope.hasContinue()

    def hasReturn(self):
        return self.scope.hasReturn()

    def getUnresolvedBreak(self):
        return self.scope.getUnresolvedBreak()

    def getUnresolvedContinue(self):
        return self.scope.getUnresolvedContinue()

    def getUnresolvedReturn(self):
        return self.scope.getUnresolvedReturn()

    def setReturnVariable(self, var):
        self.scope.setReturnVariable(var)

    def getReturnVariable(self):
        return self.scope.getReturnVariable()

    def clearBreak(self):
        self.scope.clearBreak()

    def clearContinue(self):
        self.scope.clearContinue()

    def clearReturn(self):
        self.scope.clearReturn()

    def clearReturnVariable(self):
        self.scope.clearReturnVariable()
