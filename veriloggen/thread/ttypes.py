from __future__ import absolute_import
from __future__ import print_function

import veriloggen.core.vtypes as vtypes
import veriloggen.types.ram as ram
import veriloggen.types.axi as axi
from veriloggen.seq.seq import Seq


class Shared(object):
    __intrinsics__ = ('read', 'write')

    def __init__(self, value):
        self._value = value
        self.seq = None

    @property
    def value(self):
        return self._value

    def read(self, fsm):
        return self._value

    def write(self, fsm, value, *part):
        if self.seq is None:
            self.seq = Seq(fsm.m, '_'.join(
                ['seq', self._value.name]), fsm.clk, fsm.rst)

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


class Mutex(object):
    __intrinsics__ = ('lock', 'try_lock', 'unlock')

    def __init__(self, m, name, clk, rst, width=32):

        self.m = m
        self.name = name
        self.clk = clk
        self.rst = rst
        self.width = width

        self.lock_reg = self.m.Reg(
            '_'.join(['', self.name, 'lock_reg']), initval=0)
        self.lock_id = self.m.Reg(
            '_'.join(['', self.name, 'lock_id']), self.width, initval=0)

        self.id_map = {}
        self.id_map_count = 0

    def lock(self, fsm):
        name = fsm.name
        new_lock_id = self._get_id(name)

        if new_lock_id > 2 ** self.width - 1:
            raise ValueError('too many lock IDs')

        # try
        try_state = fsm.current
        cond = vtypes.Ors(vtypes.Not(self.lock_reg),
                          self.lock_id == new_lock_id)
        fsm.If(cond)(
            self.lock_reg(1),
            self.lock_id(new_lock_id)
        )
        fsm.Then().goto_next()

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
        cond = vtypes.Or(vtypes.Not(self.lock_reg),
                         self.lock_id == new_lock_id)
        fsm.If(cond)(
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

        fsm.If(self.lock_id == new_lock_id)(
            self.lock_reg(0)
        )
        fsm.goto_next()

    def _get_id(self, name):
        if name not in self.id_map:
            self.id_map[name] = self.id_map_count
            self.id_map_count += 1

        return self.id_map[name]


class RAM(ram.SyncRAMManager):
    __intrinsics__ = ('read', 'write', 'dma_read', 'dma_write')

    def __init__(self, m, name, clk, rst,
                 datawidth=32, addrwidth=10, numports=1, axi=None):

        ram.SyncRAMManager.__init__(
            self, m, name, clk, rst, datawidth, addrwidth, numports)

        self.axi = axi

    def read(self, fsm, addr, port=0, unified=False):
        """ intrinsic read operation """

        if unified:
            return self._unified_read(fsm, addr, port)

        return self._shared_read(fsm, addr, port)

    def write(self, fsm, addr, wdata, port=0, unified=False):
        """ intrinsic write operation """

        if unified:
            return self._unified_write(fsm, addr, wdata, port)

        return self._shared_write(fsm, addr, wdata, port)

    def _shared_read(self, fsm, addr, port=0):
        """ intrinsic read operation using a shared Seq object """

        cond = fsm.state == fsm.current

        rdata, rvalid = ram.SyncRAMManager.read(self, port, addr, cond)
        rdata_reg = self.m.TmpReg(self.datawidth, initval=0)

        fsm.If(rvalid)(
            rdata_reg(rdata)
        )
        fsm.Then().goto_next()

        return rdata_reg

    def _shared_write(self, fsm, addr, wdata, port=0):
        """ intrinsic write operation using a shared Seq object """

        cond = fsm.state == fsm.current

        ram.SyncRAMManager.write(self, port, addr, wdata, cond)
        fsm.goto_next()

        return 0

    def _unified_read(self, fsm, addr, port=0):
        """ intrinsic read operation using the given FSM object """

        fsm(
            self.interfaces[port].addr(addr)
        )

        for _ in range(2):
            fsm.goto_next()

        rdata = self.m.TmpReg(self.datawidth, initval=0)

        fsm(
            rdata(self.interfaces[port].rdata)
        )
        fsm.goto_next()

        return rdata

    def _unified_write(self, fsm, addr, wdata, port=0):
        """ intrinsic write operation using the given FSM object """

        if self._write_disabled[port]:
            raise TypeError('Write disabled.')

        fsm(
            self.interfaces[port].addr(addr),
            self.interfaces[port].wdata(wdata),
            self.interfaces[port].wenable(1)
        )
        fsm.Delay(1)(
            self.interfaces[port].wenable(0)
        )
        fsm.goto_next()

        return 0

#    def dma_read(self, fsm, local_addr, global_addr, size, port=0, nonblocking=False):
#        if self.axi is None or not isinstance(self.axi, AXIM):
#            raise TypeError('AXIM interface is required')
#
#        cond = fsm.state == fsm.current
#
#        done = self.axi.dma_read(self, global_addr, local_addr, size, port)
#
#        if nonblocking:
#            fsm.goto_next()
#            return done
#
#        fsm.If(done).goto_next()
#        return 0
#
#    def dma_write(self, fsm, local_addr, global_addr, size, port=0, nonblocking=False):
#        if self.axi is None or not isinstance(self.axi, AXIM):
#            raise TypeError('AXIM interface is required')
#
#        cond = fsm.state == fsm.current
#
#        done = self.axi.dma_write(self, global_addr, local_addr, size, cond, port)
#
#        if nonblocking:
#            fsm.goto_next()
#            return done
#
#        fsm.If(done).goto_next()
#        return 0


class AXIM(axi.AxiMaster):
    __intrinsics__ = ('write_request', 'write_data',
                      'read_request', 'read_data')

    def __init__(self, m, name, clk, rst, datawidth=32, addrwidth=10):
        axi.AxiMaster.__init__(self, m, name, clk, rst, datawidth, addrwidth)


class AXIS(axi.AxiSlave):

    def __init__(self, m, name, clk, rst, datawidth=32, addrwidth=10):
        axi.AxiSlave.__init__(self, m, name, clk, rst, datawidth, addrwidth)
