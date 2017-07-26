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

    def read_sequential(self, obj, addr, size,
                        point=0, signed=False, port=0, with_last=False):

        return self.read(obj, addr, size,
                         stride=1, point=point, signed=signed, port=port,
                         with_last=with_last)

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

    def write_sequential(self, obj, addr, size, value,
                         when=None, port=0):

        return self.write(obj, addr, size, value,
                          when=when, port=port)

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

        done = obj.write_dataflow(port, addr, value, size,
                                  stride=stride, cond=fsm, when=when)

        fsm.goto_next()

        fsm.If(done)(
            flag(1)
        )

        fsm.If(done).goto_init()

        return 0

    def read_multidim(self, obj, addr, shape,
                      point=0, signed=False, port=0, with_last=False):

        if not isinstance(shape, (tuple, list)):
            raise TypeError('shape must be list or tuple.')

        if not shape:
            raise ValueError(
                'shape must have one (size, stride) pair at least.')

        if not isinstance(shape[0], (tuple, list)):
            shape = (shape,)

        flag = self.m.Reg(compiler._tmp_name('_'.join(['', self.name, 'flag'])),
                          initval=0)
        self.done_flags.append(flag)

        req_addr = self.m.Wire(
            compiler._tmp_name('_'.join(['', self.name, 'req_addr'])), obj.addrwidth)

        addr_offset = [
            self.m.Reg(compiler._tmp_name('_'.join(['', self.name, 'offset_%d' % i])),
                       obj.addrwidth, initval=0)
            for i, (out_size, out_stride) in enumerate(shape[1:])]

        req_addr_value = addr
        for offset in addr_offset:
            req_addr_value = offset + req_addr_value
        req_addr.assign(req_addr_value)

        fsm = FSM(self.m, compiler._tmp_name('_'.join(['', self.name, 'fsm'])),
                  self.clk, self.rst)
        fsm.If(self.start_cond)(
            flag(0),
            [offset(0) for offset in addr_offset]
        )
        fsm.If(self.start_cond).goto_next()

        # send state
        size, stride = shape[0]
        if stride is None:
            stride = 1

        count_list = [self.m.Reg(compiler._tmp_name('_'.join(['', self.name, 'count_%d' % i])),
                                 out_size.bit_length() + 1, initval=0)
                      for i, (out_size, out_stride) in enumerate(shape[1:])]

        repeat_state = fsm.current

        rdata, rlast, done = obj.read_dataflow(port, req_addr, size, stride=stride,
                                               cond=fsm, point=point, signed=signed)

        fsm.goto_next()

        # wait state
        cond_list = []
        prev_cond = None

        for offset, count, (out_size, out_stride) in zip(addr_offset, count_list, shape[1:]):
            if prev_cond is None:
                fsm.If(done)(
                    count.inc(),
                    offset(offset + out_stride)
                )
                fsm.If(done, count == out_size - 1)(
                    count(0),
                    offset(0)
                )
            else:
                fsm.If(done, prev_cond)(
                    count.inc(),
                    offset(offset + out_stride)
                )
                fsm.If(done, prev_cond, count == out_size - 1)(
                    count(0),
                    offset(0)
                )

            cond_list.append(count == out_size - 1)
            prev_cond = vtypes.Ands(*cond_list)

        fin_cond = vtypes.Ands(*cond_list) if cond_list else None

        if fin_cond is not None:
            # repeat condition (default)
            fsm.If(done).goto(repeat_state)
            # finish condition
            fsm.If(done, fin_cond)(
                flag(1)
            )
            fsm.If(done, fin_cond).goto_init()

        else:
            # finish condition
            fsm.If(done)(
                flag(1)
            )
            fsm.If(done).goto_init()

        if with_last:
            return rdata, rlast

        return rdata

    def write_multidim(self, obj, addr, shape, value,
                       when=None, port=0):

        if not isinstance(shape, (tuple, list)):
            raise TypeError('shape must be list or tuple.')

        if not shape:
            raise ValueError(
                'shape must have one (size, stride) pair at least.')

        if not isinstance(shape[0], (tuple, list)):
            shape = (shape,)

        flag = self.m.Reg(compiler._tmp_name('_'.join(['', self.name, 'flag'])),
                          initval=0)
        self.done_flags.append(flag)

        req_addr = self.m.Wire(
            compiler._tmp_name('_'.join(['', self.name, 'req_addr'])), obj.addrwidth)

        addr_offset = [
            self.m.Reg(compiler._tmp_name('_'.join(['', self.name, 'offset_%d' % i])),
                       obj.addrwidth, initval=0)
            for i, (out_size, out_stride) in enumerate(shape[1:])]

        req_addr_value = addr
        for offset in addr_offset:
            req_addr_value = offset + req_addr_value
        req_addr.assign(req_addr_value)

        fsm = FSM(self.m, compiler._tmp_name('_'.join(['', self.name, 'fsm'])),
                  self.clk, self.rst)
        fsm.If(self.start_cond)(
            flag(0),
            [offset(0) for offset in addr_offset]
        )
        fsm.If(self.start_cond).goto_next()

        # send state
        size, stride = shape[0]
        if stride is None:
            stride = 1

        count_list = [self.m.Reg(compiler._tmp_name('_'.join(['', self.name, 'count_%d' % i])),
                                 out_size.bit_length() + 1, initval=0)
                      for i, (out_size, out_stride) in enumerate(shape[1:])]

        repeat_state = fsm.current

        done = obj.write_dataflow(port, req_addr, value, size, stride=stride,
                                  cond=fsm, when=when)

        fsm.goto_next()

        # wait state
        cond_list = []
        prev_cond = None

        for offset, count, (out_size, out_stride) in zip(addr_offset, count_list, shape[1:]):
            if prev_cond is None:
                fsm.If(done)(
                    count.inc(),
                    offset(offset + out_stride)
                )
                fsm.If(done, count == out_size - 1)(
                    count(0),
                    offset(0)
                )
            else:
                fsm.If(done, prev_cond)(
                    count.inc(),
                    offset(offset + out_stride)
                )
                fsm.If(done, prev_cond, count == out_size - 1)(
                    count(0),
                    offset(0)
                )

            cond_list.append(count == out_size - 1)
            prev_cond = vtypes.Ands(*cond_list)

        fin_cond = vtypes.Ands(*cond_list) if cond_list else None

        if fin_cond is not None:
            # repeat condition (default)
            fsm.If(done).goto(repeat_state)
            # finish condition
            fsm.If(done, fin_cond)(
                flag(1)
            )
            fsm.If(done, fin_cond).goto_init()

        else:
            # finish condition
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
