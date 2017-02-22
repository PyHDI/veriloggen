from __future__ import absolute_import
from __future__ import print_function
import os
import sys

import veriloggen.core.vtypes as vtypes
from veriloggen.fsm.fsm import FSM

from .thread import Thread


class ThreadPool(vtypes.VeriloggenNode):
    __intrinsics__ = ('run', 'join', 'done', 'reset', 'ret')

    def __init__(self, m, clk, rst, name, targ, numthreads, datawidth=32):
        self.m = m
        self.clk = clk
        self.rst = rst
        self.name = name
        self.targ = targ
        self.numthreads = numthreads
        self.datawidth = datawidth
        self.threads = [Thread(m, clk, rst, '_'.join([name, str(i)]), targ,
                               datawidth=datawidth, tid=i)
                        for i in range(numthreads)]

        self.start = self.m.Reg(
            '_'.join(['', self.name, 'start']), self.numthreads, initval=0)

    def start(self, tid, *args, **kwargs):
        return self.threads[tid].start(*args, **kwargs)

    def extend(self, tid, fsm, *args, **kwargs):
        return self.threads[tid].extend(fsm, *args, **kwargs)

    def run(self, fsm, tid, *args, **kwargs):
        """ start as a child thread """

        fsm(
            self.start[tid](1)
        )
        fsm.goto_next()

        for thread in self.threads:
            start_cond = self.start[thread.tid]

            if not thread.is_child and thread.end_state is not None:
                raise ValueError('thread %d already started' % thread.tid)

            if thread.fsm is None:
                thread.fsm = FSM(thread.m, thread.name, thread.clk, thread.rst)

            thread.is_child = True

            if thread.start_state is not None:
                thread.fsm._set_index(thread.start_state)
            else:
                thread.start_state = thread.fsm.current

        fsm_start = fsm.current

        for thread in self.threads:
            start_cond = self.start[thread.tid]

            fsm._set_index(fsm_start)

            thread._synthesize_run_fsm(fsm, args, kwargs, cond=start_cond)

            if thread.end_state is None:
                thread.end_state = thread.fsm.current

        fsm(
            self.start[tid](0)
        )
        fsm.goto_next()

        return 0

    def join(self, fsm, tid):
        """ wait for the completion """

        patterns = []
        for thread in self.threads:
            if thread.end_state is None:
                raise ValueError('thread %d not started' % thread.tid)
            end_flag = (thread.fsm.state == thread.end_state)
            patterns.append(((tid == thread.tid), end_flag))

        patterns.append((None, 0))
        cond = vtypes.PatternMux(*patterns)
        fsm.If(cond).goto_next()

        return 0

    def done(self, fsm, tid):
        """ check whethe the thread is running """

        patterns = []
        for thread in self.threads:
            if thread.end_state is None:
                raise ValueError('thread %d not started' % thread.tid)
            end_flag = (thread.fsm.state == thread.end_state)
            patterns.append(((tid == thread.tid), end_flag))

        patterns.append((None, 0))
        cond = vtypes.PatternMux(*patterns)

        return cond

    def reset(self, fsm, tid):
        """ reset the FSM counter to the initial state """

        for thread in self.threads:
            if thread.end_state is None:
                raise ValueError('thread %d not started' % thread.tid)

        for thread in self.threads:
            reset_flag = vtypes.Land(
                (fsm.state == fsm.current), (tid == thread.tid))

            thread.fsm._set_index(thread.end_state)

            if thread.called is not None:
                thread.fsm.If(reset_flag)(
                    thread.called(0)
                )

            thread.fsm.goto_from(
                thread.end_state, thread.start_state, reset_flag)
            thread._set_index(thread.start_state)

        return 0

    def ret(self, fsm, tid):
        """ return value """

        patterns = []
        for thread in self.threads:
            if thread.end_state is None:
                raise ValueError('thread %d not started' % thread.tid)
            patterns.append(((tid == thread.tid), thread.return_value))

        patterns.append((None, vtypes.IntX()))
        ret = vtypes.PatternMux(*patterns)

        return ret
