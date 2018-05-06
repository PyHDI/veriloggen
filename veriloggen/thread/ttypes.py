from __future__ import absolute_import
from __future__ import print_function

import functools
import inspect
from collections import OrderedDict

import veriloggen.core.vtypes as vtypes
import veriloggen.types.util as util
from veriloggen.seq.seq import Seq


__intrinsics__ = ('intrinsic', 'statement', 'subst',
                  'display', 'write', 'finish', 'signed',
                  'embedded_code', 'embedded_numeric',
                  'set_parallel', 'unset_parallel')


def intrinsic(fsm, func, *args, **kwargs):
    """ function call as an intrinsic """
    func(fsm, *args, **kwargs)


class _verilog_meta(type):
    """ metaclass for verilog operator intrinsics """

    __verilog_classes__ = dict(inspect.getmembers(vtypes))
    __intrinsics__ = tuple(__verilog_classes__.keys())

    def __getattr__(self, key):
        if key in self.__verilog_classes__:
            cls = self.__verilog_classes__[key]

            @functools.wraps(cls)
            def wrapper(fsm, *args, **kwargs):
                return cls(*args, **kwargs)
            return wrapper

        raise NameError("name '%s' is not defined" % key)


_verilog = _verilog_meta('verilog', (object,),
                         {'__doc__': _verilog_meta.__doc__})


class verilog(_verilog):
    """ verilog operator intrinsics """
    pass


# for SingleStatement and EmbeddedCode
def statement(fsm, *values):
    for value in values:
        fsm(
            value
        )
    fsm.goto_next()


def subst(fsm, dst, src):
    statement(fsm, vtypes.Subst(dst, src))


def display(fsm, *args):
    statement(fsm, vtypes.Display(*args))


def write(fsm, *args):
    statement(fsm, vtypes.Write(*args))


def finish(fsm):
    statement(fsm, vtypes.Finish())


def signed(fsm, value):
    return vtypes.Signed(value)


def embedded_code(fsm, *codes):
    codes = [code.value if isinstance(code, vtypes.Str) else code
             for code in codes]
    code = '\n'.join(codes)
    statement(fsm, vtypes.EmbeddedCode(code))


def embedded_numeric(fsm, code):
    return vtypes.EmbeddedNumeric(code)


# parallel subst
def set_parallel(fsm):
    fsm.parallel = True


def unset_parallel(fsm):
    fsm.parallel = False
    fsm.goto_next()


def Lock(m, name, clk, rst, width=32):
    """ alias of Mutex class """
    return Mutex(m, name, clk, rst, width)


class Mutex(object):
    __intrinsics__ = ('lock', 'try_lock', 'unlock',
                      'acquire', 'release')

    def __init__(self, m, name, clk, rst, width=32):

        self.m = m
        self.name = name
        self.clk = clk
        self.rst = rst
        self.width = width

        self.seq = Seq(self.m, self.name, self.clk, self.rst)

        self.lock_reg = self.m.Reg(
            '_'.join(['', self.name, 'lock_reg']), initval=0)
        self.lock_id = self.m.Reg(
            '_'.join(['', self.name, 'lock_id']), self.width, initval=0)

        self.id_map = OrderedDict()
        self.id_map_count = 0

    def lock(self, fsm):
        name = fsm.name
        new_lock_id = self._get_id(name)

        if new_lock_id > 2 ** self.width - 1:
            raise ValueError('too many lock IDs')

        # try
        try_state = fsm.current

        state_cond = fsm.state == fsm.current
        try_cond = vtypes.Not(self.lock_reg)
        fsm_cond = vtypes.Ors(try_cond, self.lock_id == new_lock_id)

        self.seq.If(state_cond, try_cond)(
            self.lock_reg(1),
            self.lock_id(new_lock_id)
        )

        fsm.If(fsm_cond).goto_next()

        # verify
        cond = vtypes.Ands(self.lock_reg, self.lock_id == new_lock_id)
        fsm.If(vtypes.Not(cond)).goto(try_state)  # try again
        fsm.If(cond).goto_next()  # OK

        return 1

    def try_lock(self, fsm):
        name = fsm.name
        new_lock_id = self._get_id(name)

        if new_lock_id > 2 ** self.width - 1:
            raise ValueError('too many lock IDs')

        # try
        try_state = fsm.current

        state_cond = fsm.state == fsm.current
        try_cond = vtypes.Not(self.lock_reg)

        self.seq.If(state_cond, try_cond)(
            self.lock_reg(1),
            self.lock_id(new_lock_id)
        )

        fsm.goto_next()

        # verify
        cond = vtypes.And(self.lock_reg, self.lock_id == new_lock_id)
        result = self.m.TmpReg(initval=0)
        fsm(
            result(cond)
        )
        fsm.goto_next()

        return result

    def unlock(self, fsm):
        name = fsm.name
        new_lock_id = self._get_id(name)

        if new_lock_id > 2 ** self.width - 1:
            raise ValueError('too many lock IDs')

        state_cond = fsm.state == fsm.current

        self.seq.If(state_cond, self.lock_id == new_lock_id)(
            self.lock_reg(0)
        )

        fsm.goto_next()

        return 0

    def _get_id(self, name):
        if name not in self.id_map:
            self.id_map[name] = self.id_map_count
            self.id_map_count += 1

        return self.id_map[name]

    def acquire(self, fsm, blocking=True):
        """ alias of lock() """

        if not isinstance(blocking, (bool, int)):
            raise TypeError('blocking argument must be bool')

        if blocking:
            return self.lock(fsm)

        return self.try_lock(fsm)

    def release(self, fsm):
        """ alias of unlock() """

        return self.unlock(fsm)


class _MutexFunction(object):
    __intrinsics__ = ('lock', 'try_lock', 'unlock')

    def _check_mutex(self, fsm):
        if self.mutex is None:
            self.mutex = Mutex(self.m, '_'.join(
                ['', self.name, 'mutex']), self.clk, self.rst)

    def lock(self, fsm):
        self._check_mutex(fsm)
        return self.mutex.lock(fsm)

    def try_lock(self, fsm):
        self._check_mutex(fsm)
        return self.mutex.try_lock(fsm)

    def unlock(self, fsm):
        self._check_mutex(fsm)
        return self.mutex.unlock(fsm)


class Barrier(object):
    __intrinsics__ = ('wait', )

    def __init__(self, m, name, clk, rst, numparties):

        self.m = m
        self.name = name
        self.clk = clk
        self.rst = rst
        self.numparties = numparties
        self.width = util.log2(self.numparties) + 1

        self.seq = Seq(self.m, self.name, self.clk, self.rst)

        self.count = self.m.Reg(
            '_'.join(['', self.name, 'barrier_count']), self.width, initval=0)
        self.done = self.m.Reg(
            '_'.join(['', self.name, 'barrier_done']), initval=0)
        self.mutex = Mutex(self.m, '_'.join(
            ['', self.name, 'barrier_mutex']), self.clk, self.rst)

        # reset condition
        self.seq(
            self.done(0)
        )
        self.seq.If(self.count == self.numparties)(
            self.count(0),
            self.done(1)
        )

    def wait(self, fsm):

        self.mutex.lock(fsm)

        state_cond = fsm.state == fsm.current
        self.seq.If(state_cond)(
            self.count.inc()
        )
        fsm.goto_next()

        self.mutex.unlock(fsm)

        fsm.If(self.done).goto_next()

        return 0


class Shared(_MutexFunction):
    __intrinsics__ = ('read', 'write') + _MutexFunction.__intrinsics__

    def __init__(self, value):
        self._value = value
        self.seq = None
        self.mutex = None

    @property
    def value(self):
        return self._value

    def read(self, fsm):
        return self._value

    def write(self, fsm, value, *part):
        if self.seq is None:
            m = fsm.m
            clk = fsm.clk
            rst = fsm.rst
            name = self._value.name
            self.seq = Seq(m, '_'.join(['seq', name]), clk, rst)

        cond = fsm.state == fsm.current

        def getval(v, p):
            if isinstance(p, (tuple, list)):
                return v[p[0], p[1]]
            return v[p]

        if len(part) == 0:
            targ = self._value
        elif len(part) == 1:
            targ = getval(self._value, part[0])
        elif len(part) == 2:
            targ = getval(getval(self._value, part[0]), part[1])
        else:
            raise TypeError('unsupported type')

        self.seq.If(cond)(
            targ(value)
        )

        fsm.goto_next()
        return 0

    def _check_mutex(self, fsm):
        if self.mutex is None:
            m = fsm.m
            clk = fsm.clk
            rst = fsm.rst
            name = self._value.name
            self.mutex = Mutex(m, '_'.join(['', name, 'mutex']), clk, rst)
