from __future__ import absolute_import
from __future__ import print_function

import math
import functools

import veriloggen.core.vtypes as vtypes
import veriloggen.types.axi as axi
from veriloggen.fsm.fsm import FSM
from veriloggen.optimizer import try_optimize as optimize

from .axim import AXIM
from .axistreamin import AXIStreamIn, AXIStreamInFifo
from .axistreamout import AXIStreamOut, AXIStreamOutFifo

from .fifo import FIFO


class AXIM_for_AXIStreamIn(AXIM, axi.AxiMaster):

    def __init__(self, streamin, name,
                 waddr_id_width=0, wdata_id_width=0, wresp_id_width=0,
                 raddr_id_width=0, rdata_id_width=0,
                 waddr_user_width=2, wdata_user_width=0, wresp_user_width=0,
                 raddr_user_width=2, rdata_user_width=0,
                 waddr_burst_mode=axi.BURST_INCR, raddr_burst_mode=axi.BURST_INCR,
                 waddr_cache_mode=axi.AxCACHE_NONCOHERENT,
                 raddr_cache_mode=axi.AxCACHE_NONCOHERENT,
                 waddr_prot_mode=axi.AxPROT_NONCOHERENT,
                 raddr_prot_mode=axi.AxPROT_NONCOHERENT,
                 waddr_user_mode=axi.AxUSER_NONCOHERENT,
                 wdata_user_mode=axi.xUSER_DEFAULT,
                 raddr_user_mode=axi.AxUSER_NONCOHERENT,
                 noio=False,
                 use_global_base_addr=False,
                 req_fifo_addrwidth=3, fsm_as_module=False):

        if not isinstance(streamin, AXIStreamIn):
            raise TypeError('AXIStreamIn object is required.')

        if not streamin.noio:
            raise ValueError("noio mode of AXIStreamIn is required.")

        m = streamin.m
        clk = streamin.clk
        rst = streamin.rst
        datawidth = streamin.datawidth
        addrwidth = streamin.addrwidth

        axi.AxiMaster.__init__(self, m, name, clk, rst, datawidth, addrwidth,
                               waddr_id_width, wdata_id_width, wresp_id_width,
                               raddr_id_width, rdata_id_width,
                               waddr_user_width, wdata_user_width, wresp_user_width,
                               raddr_user_width, rdata_user_width,
                               waddr_burst_mode, raddr_burst_mode,
                               waddr_cache_mode, raddr_cache_mode,
                               waddr_prot_mode, raddr_prot_mode,
                               waddr_user_mode, wdata_user_mode,
                               raddr_user_mode,
                               noio, req_fifo_addrwidth)

        self.use_global_base_addr = use_global_base_addr
        self.req_fifo_addrwidth = req_fifo_addrwidth
        self.fsm_as_module = fsm_as_module

        self.mutex = None

        # Read
        self.read_start = self.m.Reg('_'.join(['', self.name, 'read_start']),
                                     initval=0)
        self.read_global_addr = self.m.Reg('_'.join(['', self.name, 'read_global_addr']),
                                           self.addrwidth, initval=0)
        self.read_global_size = self.m.Reg('_'.join(['', self.name, 'read_global_size']),
                                           self.addrwidth + 1, initval=0)

        self.read_req_fifo = FIFO(self.m, '_'.join(['', self.name, 'read_req_fifo']),
                                  self.clk, self.rst,
                                  datawidth=self.addrwidth + 1,
                                  addrwidth=self.req_fifo_addrwidth,
                                  sync=False)

        self.read_local_size_fifo = self.m.Wire('_'.join(['', self.name,
                                                          'read_local_size_fifo']),
                                                self.addrwidth + 1)

        self.read_local_size_fifo.assign(self.read_req_fifo.rdata)

        self.read_local_size_buf = self.m.Reg('_'.join(['', self.name,
                                                        'read_local_size_buf']),
                                              self.addrwidth + 1, initval=0)

        self.read_req_idle = self.m.Reg(
            '_'.join(['', self.name, 'read_req_idle']), initval=1)
        self.read_data_idle = self.m.Reg(
            '_'.join(['', self.name, 'read_data_idle']), initval=1)

        self.read_idle = self.m.Wire('_'.join(['', self.name, 'read_idle']))
        self.read_idle.assign(
            vtypes.Ands(vtypes.Not(self.read_start), self.read_req_idle,
                        self.read_req_fifo.empty, self.read_data_idle))

        self.seq(
            self.read_start(0)
        )

        self.read_req_fsm = None
        self.read_data_fsm = None

        if self.use_global_base_addr:
            self.global_base_addr = self.m.Reg('_'.join(['', self.name, 'global_base_addr']),
                                               self.addrwidth, initval=0)
        else:
            self.global_base_addr = None

        # No write
        self.disable_write()

        self.streamin = streamin
        streamout_name = '_'.join((streamin.name, 'out'))
        self.streamout = axi.AxiStreamOut(m, streamout_name, clk, rst,
                                          datawidth=streamin.datawidth,
                                          with_last=streamin.tdata.tlast is not None,
                                          with_strb=streamin.tdata.tstrb is not None,
                                          id_width=streamin.tdata.id_width,
                                          user_width=streamin.tdata.user_width,
                                          dest_width=streamin.tdata.dest_width,
                                          noio=streamin.noio)
        streamin.connect_stream(self.streamout)

    def dma_read(self, fsm, global_addr, size):
        raise NotImplementedError('Blocking dma_read is not supported. Use dma_read_async.')

    def dma_read_async(self, fsm, global_addr, size):

        return self._dma_read(fsm, global_addr, size)

    def dma_write(self, fsm, global_addr, size):
        raise NotImplementedError('Not supported.')

    def dma_write_async(self, fsm, global_addr, size):
        raise NotImplementedError('Not supported.')

    def dma_wait(self, fsm):
        return self.dma_wait_read(fsm)

    def _dma_read(self, fsm, global_addr, size):

        start = vtypes.Ands(fsm.here, self.read_req_idle)

        if not isinstance(self.datawidth, int):
            raise TypeError("axi.datawidth must be int, not '%s'" %
                            str(type(self.datawidth)))

        self._set_read_request(start, global_addr, size)
        self._synthesize_read_req_fsm()
        self._synthesize_read_data_fsm()

        fsm.If(self.read_req_idle).goto_next()

    def _set_read_request(self, start, global_addr, size):

        if self.use_global_base_addr:
            global_addr = global_addr + self.global_base_addr

        self.seq.If(start)(
            self.read_start(1),
            self.read_global_addr(self.mask_addr(global_addr)),
            self.read_global_size(size),
        )

    def _synthesize_read_req_fsm(self):

        if self.read_req_fsm is not None:
            return

        req_fsm = FSM(self.m, '_'.join(['', self.name, 'read_req_fsm']),
                      self.clk, self.rst, as_module=self.fsm_as_module)
        self.read_req_fsm = req_fsm

        cur_global_size = self.m.Reg('_'.join(['', self.name, 'read_cur_global_size']),
                                     self.addrwidth + 1, initval=0)
        cont = self.m.Reg('_'.join(['', self.name, 'read_cont']), initval=0)
        max_burstlen = 2 ** self.burst_size_width

        # Req state 0
        self.seq.If(req_fsm.here, self.read_start)(
            self.read_req_idle(0)
        )
        self.seq.If(self.read_start, self.read_req_fifo.almost_full)(
            self.read_start(1)
        )

        enq_cond = vtypes.Ands(req_fsm.here, self.read_start,
                               vtypes.Not(self.read_req_fifo.almost_full))
        _ = self.read_req_fifo.enq_rtl(self.read_global_size,
                                       cond=enq_cond)

        check_cond = vtypes.Ands(req_fsm.here, vtypes.Ors(self.read_start, cont),
                                 vtypes.Not(self.read_req_fifo.almost_full))
        self._check_4KB_boundary(req_fsm, max_burstlen,
                                 self.read_global_addr, cur_global_size, self.read_global_size,
                                 cond=check_cond)
        req_fsm.If(check_cond).goto_next()

        # Req state 1
        ack = self.read_request(self.read_global_addr, cur_global_size, cond=req_fsm)
        req_fsm.If(ack)(
            cont(1)
        )
        self.seq.If(req_fsm.here, ack)(
            self.read_global_addr.add(optimize(cur_global_size * (self.datawidth // 8)))
        )
        req_fsm.If(ack, self.read_global_size == 0)(
            cont(0)
        )
        self.seq.If(req_fsm.here, ack, self.read_global_size == 0)(
            self.read_req_idle(1)
        )
        req_fsm.If(ack).goto_init()

    def _synthesize_read_data_fsm(self):

        # Data FSM
        if self.read_data_fsm is not None:
            return

        data_fsm = FSM(self.m, '_'.join(['', self.name, 'read_data_fsm']),
                       self.clk, self.rst, as_module=self.fsm_as_module)
        self.read_data_fsm = data_fsm

        # Data state 0
        cond = vtypes.Ands(self.read_data_idle,
                           vtypes.Not(self.read_req_fifo.empty))
        self.seq.If(data_fsm.here, cond)(
            self.read_data_idle(0),
            self.read_local_size_buf(self.read_local_size_fifo),
        )
        deq_cond = vtypes.Ands(data_fsm.here, cond)
        _ = self.read_req_fifo.deq_rtl(cond=deq_cond)
        data_fsm.If(cond).goto_next()

        # Data state 1
        rready = vtypes.Ands(vtypes.Ors(self.streamin.tdata.tready,
                                        vtypes.Not(self.streamin.tdata.tvalid)),
                             self.read_local_size_buf > 0)
        _ = self.read_data(cond=rready)

        wlast = self.read_local_size_buf <= 1
        wcond = vtypes.Ands(self.rdata.rvalid, rready)
        # self.streamin.write_data(self.rdata.rdata, wlast, cond=wcond) ### ???
        self.streamout.write_data(self.rdata.rdata, wlast, cond=wcond)

        self.seq.If(data_fsm.here, self.rdata.rvalid, rready)(
            self.read_local_size_buf.dec()
        )

        data_fsm.If(wcond, wlast).goto_init()
        self.seq.If(data_fsm.here, wcond, wlast)(
            self.read_data_idle(1)
        )


class AXIM_for_AXIStreamOut(AXIM, axi.AxiMaster):

    def __init__(self, streamout, name,
                 waddr_id_width=0, wdata_id_width=0, wresp_id_width=0,
                 raddr_id_width=0, rdata_id_width=0,
                 waddr_user_width=2, wdata_user_width=0, wresp_user_width=0,
                 raddr_user_width=2, rdata_user_width=0,
                 waddr_burst_mode=axi.BURST_INCR, raddr_burst_mode=axi.BURST_INCR,
                 waddr_cache_mode=axi.AxCACHE_NONCOHERENT,
                 raddr_cache_mode=axi.AxCACHE_NONCOHERENT,
                 waddr_prot_mode=axi.AxPROT_NONCOHERENT,
                 raddr_prot_mode=axi.AxPROT_NONCOHERENT,
                 waddr_user_mode=axi.AxUSER_NONCOHERENT,
                 wdata_user_mode=axi.xUSER_DEFAULT,
                 raddr_user_mode=axi.AxUSER_NONCOHERENT,
                 noio=False,
                 use_global_base_addr=False,
                 req_fifo_addrwidth=3, fsm_as_module=False):

        if not isinstance(streamout, AXIStreamOut):
            raise TypeError('AXIStreamOut object is required.')

        if not streamout.noio:
            raise ValueError("noio mode of AXIStreamOut is required.")

        m = streamout.m
        clk = streamout.clk
        rst = streamout.rst
        datawidth = streamout.datawidth
        addrwidth = streamout.addrwidth

        axi.AxiMaster.__init__(self, m, name, clk, rst, datawidth, addrwidth,
                               waddr_id_width, wdata_id_width, wresp_id_width,
                               raddr_id_width, rdata_id_width,
                               waddr_user_width, wdata_user_width, wresp_user_width,
                               raddr_user_width, rdata_user_width,
                               waddr_burst_mode, raddr_burst_mode,
                               waddr_cache_mode, raddr_cache_mode,
                               waddr_prot_mode, raddr_prot_mode,
                               waddr_user_mode, wdata_user_mode,
                               raddr_user_mode,
                               noio, req_fifo_addrwidth)

        self.use_global_base_addr = use_global_base_addr
        self.req_fifo_addrwidth = req_fifo_addrwidth
        self.fsm_as_module = fsm_as_module

        self.mutex = None

        # Write
        self.write_start = self.m.Reg('_'.join(['', self.name, 'write_start']),
                                      initval=0)
        self.write_global_addr = self.m.Reg('_'.join(['', self.name, 'write_global_addr']),
                                            self.addrwidth, initval=0)
        self.write_global_size = self.m.Reg('_'.join(['', self.name, 'write_global_size']),
                                            self.addrwidth + 1, initval=0)

        self.write_req_fifo = FIFO(self.m, '_'.join(['', self.name, 'write_req_fifo']),
                                   self.clk, self.rst,
                                   datawidth=self.addrwidth + 1,
                                   addrwidth=self.req_fifo_addrwidth,
                                   sync=False)

        self.write_size_fifo = self.m.Wire('_'.join(['', self.name,
                                                     'write_size_fifo']),
                                           self.addrwidth + 1)
        self.write_size_fifo.assign(self.write_req_fifo.rdata)

        self.write_size_buf = self.m.Reg('_'.join(['', self.name,
                                                   'write_size_buf']),
                                         self.addrwidth + 1, initval=0)

        self.write_req_idle = self.m.Reg(
            '_'.join(['', self.name, 'write_req_idle']), initval=1)
        self.write_data_idle = self.m.Reg(
            '_'.join(['', self.name, 'write_data_idle']), initval=1)

        self.write_idle = self.m.Wire('_'.join(['', self.name, 'write_idle']))
        self.write_idle.assign(
            vtypes.Ands(vtypes.Not(self.write_start), self.write_req_idle,
                        self.write_req_fifo.empty, self.write_data_idle))

        self.seq(
            self.write_start(0)
        )

        self.write_req_fsm = None
        self.write_data_fsm = None

        if self.use_global_base_addr:
            self.global_base_addr = self.m.Reg('_'.join(['', self.name, 'global_base_addr']),
                                               self.addrwidth, initval=0)
        else:
            self.global_base_addr = None

        # No read
        self.disable_read()

        self.streamout = streamout
        streamin_name = '_'.join((streamout.name, 'in'))
        self.streamin = axi.AxiStreamIn(m, streamin_name, clk, rst,
                                        datawidth=streamout.datawidth,
                                        with_last=streamout.tdata.tlast is not None,
                                        with_strb=streamout.tdata.tstrb is not None,
                                        id_width=streamout.tdata.id_width,
                                        user_width=streamout.tdata.user_width,
                                        dest_width=streamout.tdata.dest_width,
                                        noio=streamout.noio)
        streamout.connect_stream(self.streamin)

    def dma_read(self, fsm, global_addr, size):
        raise NotImplementedError('Not supported.')

    def dma_read_async(self, fsm, global_addr, size):
        raise NotImplementedError('Not supported.')

    def dma_write(self, fsm, global_addr, size):
        raise NotImplementedError('Blocking dma_write is not supported. Use dma_write_async.')

    def dma_write_async(self, fsm, global_addr, size):

        return self._dma_write(fsm, global_addr, size)

    def _dma_write(self, fsm, global_addr, size):

        start = vtypes.Ands(fsm.here, self.write_req_idle)

        if not isinstance(self.datawidth, int):
            raise TypeError("axi.datawidth must be int, not '%s'" %
                            str(type(self.datawidth)))

        self._set_write_request(start, global_addr, size)
        self._synthesize_write_req_fsm()
        self._synthesize_write_data_fsm()

        fsm.If(self.write_req_idle).goto_next()

    def _set_write_request(self, start, global_addr, size):

        if self.use_global_base_addr:
            global_addr = global_addr + self.global_base_addr

        self.seq.If(start)(
            self.write_start(1),
            self.write_global_addr(self.mask_addr(global_addr)),
            self.write_global_size(size),
        )

    def _synthesize_write_req_fsm(self):

        if self.write_req_fsm is not None:
            return

        req_fsm = FSM(self.m, '_'.join(['', self.name, 'write_req_fsm']),
                      self.clk, self.rst, as_module=self.fsm_as_module)
        self.write_req_fsm = req_fsm

        cur_global_size = self.m.Reg('_'.join(['', self.name, 'write_cur_global_size']),
                                     self.addrwidth + 1, initval=0)
        cont = self.m.Reg('_'.join(['', self.name, 'write_cont']), initval=0)
        max_burstlen = 2 ** self.burst_size_width

        # Req state 0
        self.seq.If(req_fsm.here, self.write_start)(
            self.write_req_idle(0)
        )
        self.seq.If(self.write_start, self.write_req_fifo.almost_full)(
            self.write_start(1)
        )

        enq_cond = vtypes.Ands(req_fsm.here, self.write_start,
                               vtypes.Not(self.write_req_fifo.almost_full))
        _ = self.write_req_fifo.enq_rtl(self.write_global_size,
                                        cond=enq_cond)

        check_cond = vtypes.Ands(req_fsm.here, vtypes.Ors(self.write_start, cont),
                                 vtypes.Not(self.write_req_fifo.almost_full))
        self._check_4KB_boundary(req_fsm, max_burstlen,
                                 self.write_global_addr, cur_global_size, self.write_global_size,
                                 cond=check_cond)
        req_fsm.If(check_cond).goto_next()

        # Req state 1
        enq_cond = vtypes.Ands(req_fsm.here,
                               vtypes.Not(self.write_req_fifo.almost_full),
                               vtypes.Ors(self.waddr.awready, vtypes.Not(self.waddr.awvalid)),
                               self.write_acceptable())
        _ = self.write_req_fifo.enq_rtl(cur_global_size,
                                        cond=enq_cond)

        req_cond = vtypes.Ands(req_fsm.here,
                               vtypes.Not(self.write_req_fifo.almost_full),
                               self.write_acceptable())
        ack = self.write_request(self.write_global_addr, cur_global_size, cond=req_cond)
        req_fsm.If(enq_cond)(
            cont(1)
        )
        self.seq.If(req_fsm.here, enq_cond)(
            self.write_global_addr.add(optimize(cur_global_size * (self.datawidth // 8)))
        )
        req_fsm.If(enq_cond, self.write_global_size == 0)(
            cont(0)
        )
        self.seq.If(req_fsm.here, enq_cond, self.write_global_size == 0)(
            self.write_req_idle(1)
        )
        req_fsm.If(enq_cond).goto_init()

    def _synthesize_write_data_fsm(self):

        # Data FSM
        if self.write_data_fsm is not None:
            return

        data_fsm = FSM(self.m, '_'.join(['', self.name, 'write_data_fsm']),
                       self.clk, self.rst, as_module=self.fsm_as_module)
        self.write_data_fsm = data_fsm

        # Data state 0
        cond = vtypes.Ands(self.write_data_idle,
                           vtypes.Not(self.write_req_fifo.empty))
        count = self.m.TmpReg(self.addrwidth + 1, initval=0,
                              prefix='_'.join(['', self.name, 'write_count']))
        self.seq.If(data_fsm.here, cond)(
            self.write_data_idle(0),
            self.write_size_buf(0),
            count(self.write_size_fifo)
        )
        deq_cond = vtypes.Ands(data_fsm.here, cond)
        _ = self.write_req_fifo.deq_rtl(cond=deq_cond)
        data_fsm.If(cond).goto_next()

        # Data state 1
        cond = vtypes.Ands(vtypes.Not(self.write_req_fifo.empty),
                           self.write_size_buf == 0)
        self.seq.If(data_fsm.here, cond)(
            self.write_size_buf(self.write_size_fifo),
        )
        deq_cond = vtypes.Ands(data_fsm.here, cond)
        _ = self.write_req_fifo.deq_rtl(cond=deq_cond)

        rready = vtypes.Ands(vtypes.Ors(self.wdata.wready, vtypes.Not(self.wdata.wvalid)),
                             self.write_size_buf > 0)
        _ = self.streamin.read_data(cond=rready)

        wlast = self.write_size_buf <= 1
        wcond = vtypes.Ands(self.streamin.tdata.tvalid, rready)
        _ = self.write_data(self.streamin.tdata.tdata, wlast, cond=wcond)

        self.seq.If(data_fsm.here, self.streamin.tdata.tvalid, rready)(
            self.write_size_buf.dec(),
            count.dec()
        )

        data_fsm.If(wcond, count == 1).goto_init()
        self.seq.If(data_fsm.here, wcond, count == 1)(
            self.write_data_idle(1)
        )
