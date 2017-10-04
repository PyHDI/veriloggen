from __future__ import absolute_import
from __future__ import print_function

import functools
import ast
import inspect
import textwrap
from collections import OrderedDict

from veriloggen.dataflow import *
from veriloggen.seq.seq import make_condition
from veriloggen.fsm.fsm import FSM
from veriloggen.seq.seq import Seq
import veriloggen.dataflow.dtypes as dtypes

from . import compiler
from . import thread


class Stream(thread.Thread):
    __intrinsics__ = ('run', 'join', 'done', 'reset', 'ret')

    def __init__(self, m, name, clk, rst, targ, datawidth=32, tid=None):
        thread.Thread.__init__(self, m, name, clk, rst, targ, datawidth, tid)

        self.df = DataflowManager(self.m, self.clk, self.rst)
        self.seq = Seq(self.m, self.name, self.clk, self.rst)

        self.start_cond = None
        self.running_reg = None
        self.running = None
        self.done_flags = []

    def start(self, *args, **kwargs):
        raise TypeError('Stream does not support start() method.')

    def extend(self, fsm, *args, **kwargs):
        raise TypeError('Stream does not support extend() method.')

    def reset(self, fsm):
        raise TypeError('Stream does not support reset() method.')

    def join(self, fsm):
        fsm.If(vtypes.Not(self.running)).goto_next()
        return 0

    def done(self, fsm):
        return vtypes.Not(self.running)

    def _synthesize_run_fsm(self, parent_fsm, args, kwargs, cond=None):

        # insert myself as a Stream object to arguments
        args = list(args)
        args.insert(0, self)
        args = tuple(args)

        start_flag = (parent_fsm.state == parent_fsm.current)

        if self.start_cond is None:
            self.start_cond = self.m.Reg(
                '_'.join(['', self.name, 'start_cond']), initval=0)

        if self.running_reg is None:
            self.running_reg = self.m.Reg(
                '_'.join(['', self.name, 'running_reg']), initval=0)

        if self.running is None:
            self.running = self.m.Wire(
                '_'.join(['', self.name, 'running']))

        if cond is not None:
            self.fsm.If(cond)

        self.fsm.If(start_flag)(
            self.start_cond(1)
        )

        self.fsm.If(start_flag)(
            self.running_reg(1)
        )

        functions = self._get_functions()

        cvisitor = compiler.CompileVisitor(self.m, self.name, self.clk, self.rst, self.fsm,
                                           functions, self.intrinsic_functions,
                                           self.intrinsic_methods,
                                           self.start_frame,
                                           datawidth=self.datawidth)

        text = textwrap.dedent(inspect.getsource(self.targ))
        tree = ast.parse(text).body[0]

        # stack a new scope frame
        cvisitor.pushScope(ftype='call')

        used_args = []

        # args
        args_code = []
        for pos, arginfo in enumerate(tree.args.args):
            argname = (arginfo.id
                       if isinstance(arginfo, ast.Name)  # python 2
                       else arginfo.arg)  # python 3

            # actual values can be assigned later in default value section
            args_code.append(argname)

            # regular args
            if pos < len(args):
                arg = args[pos]
                used_args.append(argname)

                if isinstance(arg, vtypes.numerical_types):  # pass by value
                    if argname not in self.args_dict:
                        name = compiler._tmp_name(
                            '_'.join(['', self.name, argname]))
                        v = self.m.Reg(name, self.datawidth,
                                       initval=0, signed=True)
                        cvisitor.scope.addVariable(argname, v)
                        self.args_dict[argname] = v
                    else:
                        v = self.args_dict[argname]

                    # binding
                    if cond is not None:
                        self.fsm.If(cond)

                    self.fsm.If(start_flag)(
                        v(arg)
                    )

                else:  # pass by reference
                    if argname not in self.args_dict:
                        cvisitor.scope.addVariable(argname, arg)
                        self.args_dict[argname] = arg
                    elif id(self.args_dict[argname]) == id(arg):
                        pass
                    else:
                        raise ValueError(
                            'same object must be passed for non-numeric argument')

        # variable length args
        if tree.args.vararg is None and len(args) > len(tree.args.args):
            raise TypeError('takes %d positional arguments but %d were given' %
                            (len(tree.args.args), len(args)))

        if tree.args.vararg is not None and not self.vararg_set:
            baseobj = tree.args.vararg
            argname = (baseobj.id
                       if isinstance(baseobj, ast.Name)  # python 2
                       else baseobj.arg)  # python 3
            cvisitor.scope.addVariable(argname, self.vararg_regs)

        varargname = argname

        if len(args) > len(tree.args.args):
            used_args.append(varargname)
            raise ValueError(
                'variable length argument is not supported in dynamic thread execution')

        # kwargs
        kwargs_code = []
        for argname, arg in sorted(kwargs.items(), key=lambda x: x[0]):
            if argname in used_args:
                raise TypeError(
                    "got multiple values for argument '%s'" % argname)

            used_args.append(argname)

            if isinstance(arg, vtypes.numerical_types):  # pass by value
                if argname not in self.args_dict:
                    name = compiler._tmp_name(
                        '_'.join(['', self.name, argname]))
                    v = self.m.Reg(name, self.datawidth,
                                   initval=0, signed=True)
                    cvisitor.scope.addVariable(argname, v)
                    self.args_dict[argname] = v
                else:
                    v = self.args_dict[argname]

                # binding
                if cond is not None:
                    self.fsm.If(cond)

                self.fsm.If(start_flag)(
                    v(arg)
                )

            else:  # pass by reference
                if argname not in self.args_dict:
                    cvisitor.scope.addVariable(argname, arg)
                    self.args_dict[argname] = arg
                elif id(self.args_dict[argname]) == id(arg):
                    pass
                else:
                    raise ValueError(
                        'same object must be passed for non-numeric argument')

            kwargs_code.append('{}={}'.format(key, key))

        # defaults
        defaults_size = len(tree.args.defaults)
        if defaults_size > 0:
            for arg, val in zip(tree.args.args[-defaults_size:], tree.args.defaults):
                argname = (arg.id if isinstance(arg, ast.Name)  # python 2
                           else arg.arg)  # python 3

                if argname not in self.args_dict:
                    name = compiler._tmp_name(
                        '_'.join(['', self.name, argname]))
                    v = self.m.Reg(name, self.datawidth,
                                   initval=0, signed=True)
                    cvisitor.scope.addVariable(argname, v)
                    self.args_dict[argname] = v
                else:
                    v = self.args_dict[argname]

                if argname not in used_args:
                    right = cvisitor.visit(val)

                    # binding
                    if cond is not None:
                        self.fsm.If(cond)

                    self.fsm.If(start_flag)(
                        v(right)
                    )

        # FSM management
        c = start_flag
        if cond is not None:
            c = vtypes.Land(c, cond)

        self.fsm.If(c).goto_next()
        parent_fsm.goto_next()
        parent_fsm.goto_next()
        parent_fsm.goto_next()

        # if already synthesized
        if self.end_state is not None:
            return self.return_value

        # call AST
        args_text = ', '.join(args_code + kwargs_code)
        call_code = ''.join([self.targ.__name__, '(', args_text, ')'])
        _call_ast = ast.parse(call_code)

        node = _call_ast.body[0].value

        call_args = []
        for arg in node.args:
            call_args.append(cvisitor.visit(arg))

        call_kwargs = OrderedDict()
        for key in node.keywords:
            call_kwargs[key.arg] = cvisitor.visit(key.value)

        self.return_value = self.targ(*call_args, **call_kwargs)

        # FSM management
        self.fsm(
            self.start_cond(0)
        )
        self.fsm.goto_next()
        self.fsm.goto_next()

        done = None
        for done_flag in self.done_flags:
            done = make_condition(done, done_flag)

        if done is not None:
            self.fsm.If(done)(
                self.running_reg(0)
            )
            self.fsm.If(done).goto_init()

            self.running.assign(vtypes.Ands(
                self.running_reg, vtypes.Not(done)))

        else:
            self.running.assign(0)

        # clean-up jump conditions
        cvisitor.clearBreak()
        cvisitor.clearContinue()
        cvisitor.clearReturn()
        cvisitor.clearReturnVariable()

        # return to the previous scope frame
        cvisitor.popScope()

        return self.return_value

    # stream control methods
    def read(self, obj, addr, size,
             stride=1, point=0, signed=True, port=0, with_last=False):

        done_flag = self.m.Reg(compiler._tmp_name('_'.join(['', self.name, 'done_flag'])),
                               initval=0)
        self.done_flags.append(done_flag)

        fsm = FSM(self.m, compiler._tmp_name('_'.join(['', self.name, 'fsm'])),
                  self.clk, self.rst)
        fsm.If(self.start_cond).goto_next()

        if hasattr(obj, 'read_dataflow_interleave'):
            rdata, rlast, done = obj.read_dataflow_interleave(port, addr, size,
                                                              stride=stride,
                                                              cond=fsm, point=point,
                                                              signed=signed)
        else:
            rdata, rlast, done = obj.read_dataflow(port, addr, size,
                                                   stride=stride,
                                                   cond=fsm, point=point,
                                                   signed=signed)

        fsm.goto_next()

        fsm.If(done)(
            done_flag(1)
        )
        fsm.If(done).goto_next()

        fsm.If(vtypes.Not(self.running))(
            done_flag(0)
        )
        fsm.If(vtypes.Not(self.running)).goto_init()

        if with_last:
            return rdata, rlast

        return rdata

    def read_pattern(self, obj, addr, pattern,
                     point=0, signed=True, port=0, with_last=False):

        done_flag = self.m.Reg(compiler._tmp_name('_'.join(['', self.name, 'done_flag'])),
                               initval=0)
        self.done_flags.append(done_flag)

        fsm = FSM(self.m, compiler._tmp_name('_'.join(['', self.name, 'fsm'])),
                  self.clk, self.rst)
        fsm.If(self.start_cond).goto_next()

        if hasattr(obj, 'read_dataflow_pattern_interleave'):
            rdata, rlast, done = obj.read_dataflow_pattern_interleave(port, addr, pattern,
                                                                      cond=fsm, point=point,
                                                                      signed=signed)
        else:
            rdata, rlast, done = obj.read_dataflow_pattern(port, addr, pattern,
                                                           cond=fsm, point=point,
                                                           signed=signed)

        fsm.goto_next()

        fsm.If(done)(
            done_flag(1)
        )
        fsm.If(done).goto_next()

        fsm.If(vtypes.Not(self.running))(
            done_flag(0)
        )
        fsm.If(vtypes.Not(self.running)).goto_init()

        if with_last:
            return rdata, rlast

        return rdata

    def read_multidim(self, obj, addr, shape, order=None,
                      point=0, signed=True, port=0, with_last=False):

        done_flag = self.m.Reg(compiler._tmp_name('_'.join(['', self.name, 'done_flag'])),
                               initval=0)
        self.done_flags.append(done_flag)

        fsm = FSM(self.m, compiler._tmp_name('_'.join(['', self.name, 'fsm'])),
                  self.clk, self.rst)
        fsm.If(self.start_cond).goto_next()

        if hasattr(obj, 'read_dataflow_multidim_interleave'):
            rdata, rlast, done = obj.read_dataflow_multidim_interleave(port, addr, shape,
                                                                       order=order,
                                                                       cond=fsm, point=point,
                                                                       signed=signed)
        else:
            rdata, rlast, done = obj.read_dataflow_multidim(port, addr, shape,
                                                            order=order,
                                                            cond=fsm, point=point,
                                                            signed=signed)

        fsm.goto_next()

        fsm.If(done)(
            done_flag(1)
        )
        fsm.If(done).goto_next()

        fsm.If(vtypes.Not(self.running))(
            done_flag(0)
        )
        fsm.If(vtypes.Not(self.running)).goto_init()

        if with_last:
            return rdata, rlast

        return rdata

    def read_reuse(self, obj, addr, size,
                   reuse_size=1, num_outputs=1,
                   stride=1, point=0, signed=True, port=0, with_last=False):

        done_flag = self.m.Reg(compiler._tmp_name('_'.join(['', self.name, 'done_flag'])),
                               initval=0)
        self.done_flags.append(done_flag)

        fsm = FSM(self.m, compiler._tmp_name('_'.join(['', self.name, 'fsm'])),
                  self.clk, self.rst)
        fsm.If(self.start_cond).goto_next()

        if hasattr(obj, 'read_dataflow_reuse_interleave'):
            ret = obj.read_dataflow_reuse_interleave(port, addr, size, stride=stride,
                                                     reuse_size=reuse_size,
                                                     num_outputs=num_outputs,
                                                     cond=fsm, point=point, signed=signed)
        else:
            ret = obj.read_dataflow_reuse(port, addr, size, stride=stride,
                                          reuse_size=reuse_size,
                                          num_outputs=num_outputs,
                                          cond=fsm, point=point, signed=signed)

        rdata = ret[:-2]
        done = ret[-1]
        rlast = ret[-2]

        fsm.goto_next()

        fsm.If(done)(
            done_flag(1)
        )
        fsm.If(done).goto_next()

        fsm.If(vtypes.Not(self.running))(
            done_flag(0)
        )
        fsm.If(vtypes.Not(self.running)).goto_init()

        if with_last:
            return tuple(rdata + [rlast])

        if len(rdata) == 1:
            rdata = rdata[0]
        else:
            rdata = tuple(rdata)

        return rdata

    def read_reuse_pattern(self, obj, addr, pattern,
                           reuse_size=1, num_outputs=1,
                           point=0, signed=True, port=0, with_last=False):

        done_flag = self.m.Reg(compiler._tmp_name('_'.join(['', self.name, 'done_flag'])),
                               initval=0)
        self.done_flags.append(done_flag)

        fsm = FSM(self.m, compiler._tmp_name('_'.join(['', self.name, 'fsm'])),
                  self.clk, self.rst)
        fsm.If(self.start_cond).goto_next()

        if hasattr(obj, 'read_dataflow_reuse_pattern_interleave'):
            ret = obj.read_dataflow_reuse_pattern_interleave(port, addr, pattern,
                                                             reuse_size, num_outputs,
                                                             cond=fsm, point=point,
                                                             signed=signed)
        else:
            ret = obj.read_dataflow_reuse_pattern(port, addr, pattern,
                                                  reuse_size, num_outputs,
                                                  cond=fsm, point=point,
                                                  signed=signed)

        rdata = ret[:-2]
        done = ret[-1]
        rlast = ret[-2]

        fsm.goto_next()

        fsm.If(done)(
            done_flag(1)
        )
        fsm.If(done).goto_next()

        fsm.If(vtypes.Not(self.running))(
            done_flag(0)
        )
        fsm.If(vtypes.Not(self.running)).goto_init()

        if with_last:
            return tuple(rdata + [rlast])

        if len(rdata) == 1:
            rdata = rdata[0]
        else:
            rdata = tuple(rdata)

        return rdata

    def read_reuse_multidim(self, obj, addr, shape, order=None,
                            reuse_size=1, num_outputs=1,
                            point=0, signed=True, port=0, with_last=False):

        done_flag = self.m.Reg(compiler._tmp_name('_'.join(['', self.name, 'done_flag'])),
                               initval=0)
        self.done_flags.append(done_flag)

        fsm = FSM(self.m, compiler._tmp_name('_'.join(['', self.name, 'fsm'])),
                  self.clk, self.rst)
        fsm.If(self.start_cond).goto_next()

        if hasattr(obj, 'read_dataflow_reuse_multidim_interleave'):
            ret = obj.read_dataflow_reuse_multidim_interleave(port, addr, shape,
                                                              order=order,
                                                              reuse_size=reuse_size,
                                                              num_outputs=num_outputs,
                                                              cond=fsm, point=point,
                                                              signed=signed)
        else:
            ret = obj.read_dataflow_reuse_multidim(port, addr, shape,
                                                   order=order,
                                                   reuse_size=reuse_size,
                                                   num_outputs=num_outputs,
                                                   cond=fsm, point=point,
                                                   signed=signed)

        rdata = ret[:-2]
        done = ret[-1]
        rlast = ret[-2]

        fsm.goto_next()

        fsm.If(done)(
            done_flag(1)
        )
        fsm.If(done).goto_next()

        fsm.If(vtypes.Not(self.running))(
            done_flag(0)
        )
        fsm.If(vtypes.Not(self.running)).goto_init()

        if with_last:
            return tuple(rdata + [rlast])

        if len(rdata) == 1:
            rdata = rdata[0]
        else:
            rdata = tuple(rdata)

        return rdata

    def write(self, obj, addr, size, value,
              stride=1, when=None, port=0):

        done_flag = self.m.Reg(compiler._tmp_name('_'.join(['', self.name, 'done_flag'])),
                               initval=0)
        self.done_flags.append(done_flag)

        fsm = FSM(self.m, compiler._tmp_name('_'.join(['', self.name, 'fsm'])),
                  self.clk, self.rst)
        fsm.If(self.start_cond).goto_next()

        if hasattr(obj, 'write_dataflow_interleave'):
            done = obj.write_dataflow_interleave(port, addr, value, size,
                                                 stride=stride, cond=fsm, when=when)
        else:
            done = obj.write_dataflow(port, addr, value, size,
                                      stride=stride, cond=fsm, when=when)

        fsm.goto_next()

        fsm.If(done)(
            done_flag(1)
        )
        fsm.If(done).goto_next()

        fsm.If(vtypes.Not(self.running))(
            done_flag(0)
        )
        fsm.If(vtypes.Not(self.running)).goto_init()

        return 0

    def write_pattern(self, obj, addr, value, pattern,
                      when=None, port=0):

        done_flag = self.m.Reg(compiler._tmp_name('_'.join(['', self.name, 'done_flag'])),
                               initval=0)
        self.done_flags.append(done_flag)

        fsm = FSM(self.m, compiler._tmp_name('_'.join(['', self.name, 'fsm'])),
                  self.clk, self.rst)
        fsm.If(self.start_cond).goto_next()

        if hasattr(obj, 'write_dataflow_pattern_interleave'):
            done = obj.write_dataflow_pattern_interleave(port, addr, value, pattern,
                                                         cond=fsm, when=when)
        else:
            done = obj.write_dataflow_pattern(port, addr, value, pattern,
                                              cond=fsm, when=when)

        fsm.goto_next()

        fsm.If(done)(
            done_flag(1)
        )
        fsm.If(done).goto_next()

        fsm.If(vtypes.Not(self.running))(
            done_flag(0)
        )
        fsm.If(vtypes.Not(self.running)).goto_init()

        return 0

    def write_multidim(self, obj, addr, value, shape, order=None,
                       when=None, port=0):

        done_flag = self.m.Reg(compiler._tmp_name('_'.join(['', self.name, 'done_flag'])),
                               initval=0)
        self.done_flags.append(done_flag)

        fsm = FSM(self.m, compiler._tmp_name('_'.join(['', self.name, 'fsm'])),
                  self.clk, self.rst)
        fsm.If(self.start_cond).goto_next()

        if hasattr(obj, 'write_dataflow_multidim_interleave'):
            done = obj.write_dataflow_multidim_interleave(port, addr, value, shape,
                                                          order=order, cond=fsm, when=when)
        else:
            done = obj.write_dataflow_multidim(port, addr, value, shape,
                                               order=order, cond=fsm, when=when)

        fsm.goto_next()

        fsm.If(done)(
            done_flag(1)
        )
        fsm.If(done).goto_next()

        fsm.If(vtypes.Not(self.running))(
            done_flag(0)
        )
        fsm.If(vtypes.Not(self.running)).goto_init()

        return 0

    def __getattr__(self, attr):
        try:
            return object.__getattr__(self, attr)

        except AttributeError as e:
            if attr.startswith('__') or attr not in dir(dtypes):
                raise e

            func = getattr(dtypes, attr)

            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                v = func(*args, **kwargs)
                if isinstance(v, (tuple, list)):
                    for item in v:
                        self._set_info(item)
                else:
                    self._set_info(v)
                return v

            return wrapper

    def _set_info(self, v):
        if isinstance(v, dtypes._Numeric):
            v._set_module(self.m)
            v._set_df(self.df)
            v._set_seq(self.seq)
