from __future__ import absolute_import
from __future__ import print_function

import veriloggen.types.ram as ram


class RAM(ram.SyncRAMManager):
    __intrinsics__ = ('read', 'write')

    def __init__(self, m, name, clk, rst, datawidth=32, addrwidth=10, numports=1):
        ram.SyncRAMManager.__init__(
            self, m, name, clk, rst, datawidth, addrwidth, numports)

    def read(self, fsm, addr, port=0):
        """ thread intrinsic for read operation """

        cond = fsm.state == fsm.current

        rdata, rvalid = ram.SyncRAMManager.read(self, port, addr, cond)
        fsm.goto_next()
        fsm.goto_next()
        
        val = self.m.TmpReg(self.datawidth, initval=0)
        fsm(
            val(rdata)
        )
        fsm.goto_next()

        return val

    def write(self, fsm, addr, wdata, port=0):
        """ thread intrinsic for write operation """

        cond = fsm.state == fsm.current

        ram.SyncRAMManager.write(self, port, addr, wdata, cond)
        fsm.goto_next()

        return 0
