from __future__ import absolute_import
from __future__ import print_function

import functools

from veriloggen.dataflow import *
from veriloggen.seq.seq import make_condition
from veriloggen.fsm.fsm import FSM
from veriloggen.seq.seq import Seq
import veriloggen.dataflow.dtypes as dtypes

from . import compiler


class Stream(vtypes.VeriloggenNode):
    __intrinsics__ = ('run', 'join', 'done')

    def __init__(self, m, name, clk, rst, func):
        self.m = m
        self.name = name
        self.clk = clk
        self.rst = rst
        self.func = func

        self.df = DataflowManager(self.m, self.clk, self.rst)
        self.seq = Seq(self.m, 'name', self.clk, self.rst)
        self.start_cond = None
        self.done_flags = []

    def run(self, fsm, *args, **kwargs):
        self.start_cond = fsm.state == fsm.current
        self.func(self, *args)

        fsm.goto_next()

        return 0

    def join(self, fsm):
        done = None

        for flag in self.done_flags:
            done = make_condition(done, flag)

        fsm.If(done).goto_next()
        return 0

    def done(self, fsm):
        done = None

        for flag in self.done_flags:
            done = make_condition(done, flag)

        return done

    def read(self, obj, addr, size,
             stride=1, point=0, signed=False, port=0, with_last=False):

        flag = self.m.Reg(compiler._tmp_name('_'.join(['', self.name, 'flag'])),
                          initval=0)
        self.done_flags.append(flag)

        fsm = FSM(self.m, compiler._tmp_name('_'.join(['', self.name, 'fsm'])),
                  self.clk, self.rst)
        fsm.If(self.start_cond)(
            flag(0)
        )
        fsm.If(self.start_cond).goto_next()

        if hasattr(obj, 'read_dataflow_interleave'):
            rdata, rlast, done = obj.read_dataflow_interleave(port, addr, size, stride=stride,
                                                              cond=fsm, point=point, signed=signed)
        else:
            rdata, rlast, done = obj.read_dataflow(port, addr, size, stride=stride,
                                                   cond=fsm, point=point, signed=signed)

        fsm.goto_next()

        fsm.If(done)(
            flag(1)
        )

        fsm.If(done).goto_init()

        if with_last:
            return rdata, rlast

        return rdata

    def read_sequential(self, obj, addr, size,
                        point=0, signed=False, port=0, with_last=False):

        return self.read(obj, addr, size,
                         stride=1, point=point, signed=signed, port=port,
                         with_last=with_last)

    def read_pattern(self, obj, addr, pattern,
                     point=0, signed=False, port=0, with_last=False):

        flag = self.m.Reg(compiler._tmp_name('_'.join(['', self.name, 'flag'])),
                          initval=0)
        self.done_flags.append(flag)

        fsm = FSM(self.m, compiler._tmp_name('_'.join(['', self.name, 'fsm'])),
                  self.clk, self.rst)
        fsm.If(self.start_cond)(
            flag(0)
        )
        fsm.If(self.start_cond).goto_next()

        if hasattr(obj, 'read_dataflow_pattern_interleave'):
            rdata, rlast, done = obj.read_dataflow_pattern_interleave(port, addr, pattern,
                                                                      cond=fsm, point=point, signed=signed)
        else:
            rdata, rlast, done = obj.read_dataflow_pattern(port, addr, pattern,
                                                           cond=fsm, point=point, signed=signed)

        fsm.goto_next()

        fsm.If(done)(
            flag(1)
        )

        fsm.If(done).goto_init()

        if with_last:
            return rdata, rlast

        return rdata

    def read_multidim(self, obj, addr, shape, order=None,
                      point=0, signed=False, port=0, with_last=False):

        flag = self.m.Reg(compiler._tmp_name('_'.join(['', self.name, 'flag'])),
                          initval=0)
        self.done_flags.append(flag)

        fsm = FSM(self.m, compiler._tmp_name('_'.join(['', self.name, 'fsm'])),
                  self.clk, self.rst)
        fsm.If(self.start_cond)(
            flag(0)
        )
        fsm.If(self.start_cond).goto_next()

        if hasattr(obj, 'read_dataflow_multidim_interleave'):
            rdata, rlast, done = obj.read_dataflow_multidim_interleave(port, addr, shape, order=order,
                                                                       cond=fsm, point=point, signed=signed)
        else:
            rdata, rlast, done = obj.read_dataflow_multidim(port, addr, shape, order=order,
                                                            cond=fsm, point=point, signed=signed)

        fsm.goto_next()

        fsm.If(done)(
            flag(1)
        )

        fsm.If(done).goto_init()

        if with_last:
            return rdata, rlast

        return rdata

    def write(self, obj, addr, size, value,
              stride=1, when=None, port=0):

        flag = self.m.Reg(compiler._tmp_name('_'.join(['', self.name, 'flag'])),
                          initval=0)
        self.done_flags.append(flag)

        fsm = FSM(self.m, compiler._tmp_name('_'.join(['', self.name, 'fsm'])),
                  self.clk, self.rst)
        fsm.If(self.start_cond)(
            flag(0)
        )
        fsm.If(self.start_cond).goto_next()

        if hasattr(obj, 'write_dataflow_interleave'):
            done = obj.write_dataflow_interleave(port, addr, value, size,
                                                 stride=stride, cond=fsm, when=when)
        else:
            done = obj.write_dataflow(port, addr, value, size,
                                      stride=stride, cond=fsm, when=when)

        fsm.goto_next()

        fsm.If(done)(
            flag(1)
        )

        fsm.If(done).goto_init()

        return 0

    def write_sequential(self, obj, addr, size, value,
                         when=None, port=0):

        return self.write(obj, addr, size, value,
                          when=when, port=port)

    def write_pattern(self, obj, addr, value, pattern,
                      when=None, port=0):

        flag = self.m.Reg(compiler._tmp_name('_'.join(['', self.name, 'flag'])),
                          initval=0)
        self.done_flags.append(flag)

        fsm = FSM(self.m, compiler._tmp_name('_'.join(['', self.name, 'fsm'])),
                  self.clk, self.rst)
        fsm.If(self.start_cond)(
            flag(0)
        )
        fsm.If(self.start_cond).goto_next()

        if hasattr(obj, 'write_dataflow_pattern_interleave'):
            done = obj.write_dataflow_pattern_interleave(port, addr, value, pattern,
                                                         cond=fsm, when=when)
        else:
            done = obj.write_dataflow_pattern(port, addr, value, pattern,
                                              cond=fsm, when=when)

        fsm.goto_next()

        fsm.If(done)(
            flag(1)
        )

        fsm.If(done).goto_init()

        return 0

    def write_multidim(self, obj, addr, value, shape, order=None,
                       when=None, port=0):

        flag = self.m.Reg(compiler._tmp_name('_'.join(['', self.name, 'flag'])),
                          initval=0)
        self.done_flags.append(flag)

        fsm = FSM(self.m, compiler._tmp_name('_'.join(['', self.name, 'fsm'])),
                  self.clk, self.rst)
        fsm.If(self.start_cond)(
            flag(0)
        )
        fsm.If(self.start_cond).goto_next()

        if hasattr(obj, 'write_dataflow_multidim_interleave'):
            done = obj.write_dataflow_multidim_interleave(port, addr, value, shape, order=order,
                                                          cond=fsm, when=when)
        else:
            done = obj.write_dataflow_multidim(port, addr, value, shape, order=order,
                                               cond=fsm, when=when)

        fsm.goto_next()

        fsm.If(done)(
            flag(1)
        )

        fsm.If(done).goto_init()

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
