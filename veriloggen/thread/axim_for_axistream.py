from __future__ import absolute_import
from __future__ import print_function

from .axim import AXIM
from .axistreamin import AXIStreamIn, AXIStreamInFifo
from .axistreamout import AXIStreamOut, AXIStreamOutFifo


class AXIM_for_AXIStreamIn(AXIM):

    def __init__(self, streamin, name,
                 waddr_id_width=0, wdata_id_width=0, wresp_id_width=0,
                 raddr_id_width=0, rdata_id_width=0,
                 waddr_user_width=2, wdata_user_width=0, wresp_user_width=0,
                 raddr_user_width=2, rdata_user_width=0,
                 waddr_burst_mode=axi.BURST_INCR, raddr_burst_mode=axi.BURST_INCR,
                 waddr_cache_mode=axi.AxCACHE_NONCOHERENT, raddr_cache_mode=axi.AxCACHE_NONCOHERENT,
                 waddr_prot_mode=axi.AxPROT_NONCOHERENT, raddr_prot_mode=axi.AxPROT_NONCOHERENT,
                 waddr_user_mode=axi.AxUSER_NONCOHERENT, wdata_user_mode=axi.xUSER_DEFAULT,
                 raddr_user_mode=axi.AxUSER_NONCOHERENT,
                 noio=False,
                 enable_async=True, use_global_base_addr=False,
                 num_cmd_delay=0, num_data_delay=0,
                 op_sel_width=8, fsm_as_module=False):

        if not isinstance(streamin, AXIStreamIn):
            raise TypeError('AXIStreamIn object is required.')

        if not streamin.noio:
            raise ValueError("noio mode of AXIStreamIn is required.")

        m = streamin.m
        clk = streamin.clk
        rst = streamin.rst
        datawidth = streamin.datawidth
        addrwidth = streamin.addrwidth

        AXIM.__init__(self, m, name, clk, rst, datawidth, addrwidth,
                      waddr_id_width, wdata_id_width, wresp_id_width,
                      raddr_id_width, rdata_id_width,
                      waddr_user_width, wdata_user_width, wresp_user_width,
                      raddr_user_width, rdata_user_width,
                      waddr_burst_mode, raddr_burst_mode,
                      waddr_cache_mode, raddr_cache_mode,
                      waddr_prot_mode, raddr_prot_mode,
                      waddr_user_mode, wdata_user_mode,
                      raddr_user_mode,
                      noio,
                      enable_async, use_global_base_addr,
                      num_cmd_delay, num_data_delay,
                      op_sel_width, fsm_as_module)

        self.streamin = streamin
        self.streamin.connect_master_rdata(self)

        self.disable_write()

    def dma_read(self, fsm, global_addr, size):
        raise NotImplementedError('Blocking dma_read is not supported. Use dma_read_async.')

    def dma_read_async(self, fsm, global_addr, size):

        if not self.enable_async:
            raise ValueError(
                "Async mode is disabled. Set 'True' to AXIM.enable_async.")

        self.dma_wait_read(fsm)

        return self._dma_read(fsm, global_addr, size)

    def _dma_read(self, fsm, global_addr, size):

        start = self._set_flag(fsm)

        for _ in range(self.num_cmd_delay + 1):
            fsm.goto_next()

        self._set_read_request(start, global_addr, size)
        self._synthesize_read_fsm()

        fsm.goto_next()

    def _set_read_request(self, start, global_addr, size):

        op_id = 1

        if op_id in self.read_reqs:
            (read_start, read_op_sel,
             read_global_addr_in,
             read_size_in) = self.read_reqs[op_id]

            self.seq.If(start)(
                read_start(1),
                read_op_sel(op_id),
                read_global_addr_in(global_addr),
                read_size_in(size),
            )

            return

        read_start = self.m.Reg(
            '_'.join(['', self.name, self.streamin.name, 'read_start']),
            initval=0)
        read_op_sel = self.m.Reg(
            '_'.join(['', self.name, self.streamin.name, 'read_op_sel']),
            self.op_sel_width, initval=0)
        read_global_addr = self.m.Reg(
            '_'.join(['', self.name, self.streamin.name, 'read_global_addr']),
            self.addrwidth, initval=0)
        read_size = self.m.Reg(
            '_'.join(['', self.name, self.streamin.name, 'read_size']),
            self.addrwidth + 1, initval=0)

        self.seq(
            read_start(0)
        )
        self.seq.If(start)(
            read_start(1),
            read_op_sel(op_id),
            read_global_addr(global_addr),
            read_size(size),
        )

        self.read_reqs[op_id] = (read_start, read_op_sel,
                                 read_global_addr,
                                 read_size)

        if self.num_cmd_delay > 0:
            read_start = self.seq.Prev(read_start, self.num_cmd_delay)
            read_op_sel = self.seq.Prev(read_op_sel, self.num_cmd_delay)
            read_global_addr = self.seq.Prev(
                read_global_addr, self.num_cmd_delay)
            read_size = self.seq.Prev(read_size, self.num_cmd_delay)

        self.seq.If(read_start)(
            self.read_idle(0)
        )

        self.seq.If(read_start)(
            self.read_start(1),
            self.read_op_sel(read_op_sel),
            self.read_global_addr(read_global_addr),
            self.read_size(read_size),
        )

    def _synthesize_read_fsm(self):

        op_id = 1

        if op_id in self.read_ops:
            """ already synthesized op """
            return

        if self.read_fsm is not None:
            """ new op """
            self.read_ops.append(op_id)
            return

        """ new op and fsm """
        fsm = FSM(self.m, '_'.join(['', self.name, 'read_fsm']),
                  self.clk, self.rst, as_module=self.fsm_as_module)
        self.read_fsm = fsm

        self.read_ops.append(op_id)

        cur_global_addr = self.m.Reg('_'.join(['', self.name, 'read_cur_global_addr']),
                                     self.addrwidth, initval=0)
        cur_size = self.m.Reg('_'.join(['', self.name, 'read_cur_size']),
                              self.addrwidth + 1, initval=0)
        rest_size = self.m.Reg('_'.join(['', self.name, 'read_rest_size']),
                               self.addrwidth + 1, initval=0)
        max_burstlen = 2 ** self.burst_size_width

        # state 0
        if not self.use_global_base_addr:
            gaddr = self.read_global_addr
        else:
            gaddr = self.read_global_addr + self.global_base_addr

        fsm.If(self.read_start)(
            cur_global_addr(self.mask_addr(gaddr)),
            rest_size(self.read_size)
        )
        fsm.If(self.read_start).goto_next()

        # state 1
        check_state = fsm.current
        self._check_4KB_boundary(fsm, max_burstlen,
                                 cur_global_addr, cur_size, rest_size)

        # state 2
        ack = self.read_request(cur_global_addr, cur_size, cond=fsm)
        fsm.If(ack).goto_next()

        accept = vtypes.Ands(self.raddr.arvalid, self.raddr.arready)
        fsm.If(accept)(
            cur_global_addr.add(optimize(cur_size * (self.datawidth // 8)))
        )
        fsm.If(accept, rest_size > 0).goto(check_state)
        fsm.If(accept, rest_size == 0).goto_next()

        for _ in range(self.num_data_delay):
            fsm.goto_next()

        # state 3
        set_idle = self._set_flag(fsm)
        self.seq.If(set_idle)(
            self.read_idle(1)
        )

        fsm.goto_init()


class AXIM_for_AXIStreamOut(AXIM):

    def __init__(self, streamout, name,
                 waddr_id_width=0, wdata_id_width=0, wresp_id_width=0,
                 raddr_id_width=0, rdata_id_width=0,
                 waddr_user_width=2, wdata_user_width=0, wresp_user_width=0,
                 raddr_user_width=2, rdata_user_width=0,
                 waddr_burst_mode=axi.BURST_INCR, raddr_burst_mode=axi.BURST_INCR,
                 waddr_cache_mode=axi.AxCACHE_NONCOHERENT, raddr_cache_mode=axi.AxCACHE_NONCOHERENT,
                 waddr_prot_mode=axi.AxPROT_NONCOHERENT, raddr_prot_mode=axi.AxPROT_NONCOHERENT,
                 waddr_user_mode=axi.AxUSER_NONCOHERENT, wdata_user_mode=axi.xUSER_DEFAULT,
                 raddr_user_mode=axi.AxUSER_NONCOHERENT,
                 noio=False,
                 enable_async=True, use_global_base_addr=False,
                 num_cmd_delay=0, num_data_delay=0,
                 op_sel_width=8, fsm_as_module=False):

        if not isinstance(streamout, AXIStreamOut):
            raise TypeError('AXIStreamOut object is required.')

        if not streamout.noio:
            raise ValueError("noio mode of AXIStreamOut is required.")

        m = streamout.m
        clk = streamout.clk
        rst = streamout.rst
        datawidth = streamout.datawidth
        addrwidth = streamout.addrwidth

        AXIM.__init__(self, m, name, clk, rst, datawidth, addrwidth,
                      waddr_id_width, wdata_id_width, wresp_id_width,
                      raddr_id_width, rdata_id_width,
                      waddr_user_width, wdata_user_width, wresp_user_width,
                      raddr_user_width, rdata_user_width,
                      waddr_burst_mode, raddr_burst_mode,
                      waddr_cache_mode, raddr_cache_mode,
                      waddr_prot_mode, raddr_prot_mode,
                      waddr_user_mode, wdata_user_mode,
                      raddr_user_mode,
                      noio,
                      enable_async, use_global_base_addr,
                      num_cmd_delay, num_data_delay,
                      op_sel_width, fsm_as_module)

        self.streamout = streamout
        self.in_streamout = AXIStreamIn(streamout.m, streamout.name + '_in', streamout.clk, streamout.rst,
                                        streamout.datawidth, streamout.addrwidth,
                                        streamout.tdata.tlast is not None,
                                        streamout.tdata.id_width, streamout.tdata.user_width, streamout.tdata.dest_width,
                                        True,
                                        streamout.enable_async,
                                        streamout.num_cmd_delay, streamout.num_data_delay,
                                        streamout.op_sel_width, streamout.fsm_as_module)
        self.in_streamout.connect_stream(self.streamout)

        self.disable_read()

    def dma_write(self, fsm, global_addr, size):
        raise NotImplementedError('Blocking dma_write is not supported. Use dma_write_async.')

    def dma_write_async(self, fsm, global_addr, size):

        if not self.enable_async:
            raise ValueError(
                "Async mode is disabled. Set 'True' to AXIM.enable_async.")

        self.dma_wait_write(fsm)

        return self._dma_write(fsm, global_addr, size)

    def _dma_write(self, fsm, global_addr, size):

        start = self._set_flag(fsm)

        for _ in range(self.num_cmd_delay + 1):
            fsm.goto_next()

        self._set_write_request(start, global_addr, size)
        self._synthesize_write_fsm()

        fsm.goto_next()

    def _set_write_request(self, start, global_addr, size):

        op_id = 1

        if op_id in self.write_reqs:
            (write_start, write_op_sel,
             write_global_addr_in,
             write_size_in) = self.write_reqs[op_id]

            self.seq.If(start)(
                write_start(1),
                write_op_sel(op_id),
                write_global_addr_in(global_addr),
                write_size_in(size),
            )

            return

        write_start = self.m.Reg(
            '_'.join(['', self.name, self.streamout.name, 'write_start']),
            initval=0)
        write_op_sel = self.m.Reg(
            '_'.join(['', self.name, self.streamout.name, 'write_op_sel']),
            self.op_sel_width, initval=0)
        write_global_addr = self.m.Reg(
            '_'.join(['', self.name, self.streamout.name, 'write_global_addr']),
            self.addrwidth, initval=0)
        write_size = self.m.Reg(
            '_'.join(['', self.name, self.streamout.name, 'write_size']),
            self.addrwidth + 1, initval=0)

        self.seq(
            write_start(0)
        )
        self.seq.If(start)(
            write_start(1),
            write_op_sel(op_id),
            write_global_addr(global_addr),
            write_size(size),
        )

        self.write_reqs[op_id] = (write_start, write_op_sel,
                                  write_global_addr,
                                  write_size)

        if self.num_cmd_delay > 0:
            write_start = self.seq.Prev(write_start, self.num_cmd_delay)
            write_op_sel = self.seq.Prev(write_op_sel, self.num_cmd_delay)
            write_global_addr = self.seq.Prev(
                write_global_addr, self.num_cmd_delay)
            write_size = self.seq.Prev(write_size, self.num_cmd_delay)

        self.seq.If(write_start)(
            self.write_idle(0)
        )

        self.seq.If(write_start)(
            self.write_start(1),
            self.write_op_sel(write_op_sel),
            self.write_global_addr(write_global_addr),
            self.write_size(write_size),
        )

    def _synthesize_write_fsm(self):

        op_id = 1

        if op_id in self.write_ops:
            """ already synthesized op """
            return

        if self.write_fsm is not None:
            """ new op """
            self.write_ops.append(op_id)
            return

        """ new op and fsm """
        fsm = FSM(self.m, '_'.join(['', self.name, 'write_fsm']),
                  self.clk, self.rst, as_module=self.fsm_as_module)
        self.write_fsm = fsm

        self.write_ops.append(op_id)

        cur_global_addr = self.m.Reg('_'.join(['', self.name, 'write_cur_global_addr']),
                                     self.addrwidth, initval=0)
        cur_size = self.m.Reg('_'.join(['', self.name, 'write_cur_size']),
                              self.addrwidth + 1, initval=0)
        rest_size = self.m.Reg('_'.join(['', self.name, 'write_rest_size']),
                               self.addrwidth + 1, initval=0)
        max_burstlen = 2 ** self.burst_size_width

        # state 0
        if not self.use_global_base_addr:
            gaddr = self.write_global_addr
        else:
            gaddr = self.write_global_addr + self.global_base_addr

        fsm.If(self.write_start)(
            cur_global_addr(self.mask_addr(gaddr)),
            rest_size(self.write_size)
        )
        fsm.If(self.write_start).goto_next()

        # state 1
        check_state = fsm.current
        self._check_4KB_boundary(fsm, max_burstlen,
                                 cur_global_addr, cur_size, rest_size)

        # state 2
        ack, counter = self.write_request_counter(cur_global_addr, cur_size, cond=fsm)
        self.write_data_counter = counter
        fsm.If(ack).goto_next()

        # state 3
        cond = fsm.here
        data, last, _id, user, dest, done = self.in_streamout.read_dataflow(cond=cond)
        done_out = self.write_dataflow(data, counter, cond=cond)
        self.write_data_done.assign(done_out)

        fsm.If(self.write_data_done)(
            cur_global_addr.add(optimize(cur_size * (self.datawidth // 8)))
        )
        fsm.If(self.write_data_done, rest_size > 0).goto(check_state)
        fsm.If(self.write_data_done, rest_size == 0).goto_next()

        # state 4
        set_idle = self._set_flag(fsm)
        self.seq.If(set_idle)(
            self.write_idle(1)
        )

        fsm.goto_init()


class AXIM2(AXIM_for_AXIStreamIn):

    def __init__(self, m, name, clk, rst, datawidth=32, addrwidth=32,
                 waddr_id_width=0, wdata_id_width=0, wresp_id_width=0,
                 raddr_id_width=0, rdata_id_width=0,
                 waddr_user_width=2, wdata_user_width=0, wresp_user_width=0,
                 raddr_user_width=2, rdata_user_width=0,
                 waddr_burst_mode=axi.BURST_INCR, raddr_burst_mode=axi.BURST_INCR,
                 waddr_cache_mode=axi.AxCACHE_NONCOHERENT, raddr_cache_mode=axi.AxCACHE_NONCOHERENT,
                 waddr_prot_mode=axi.AxPROT_NONCOHERENT, raddr_prot_mode=axi.AxPROT_NONCOHERENT,
                 waddr_user_mode=axi.AxUSER_NONCOHERENT, wdata_user_mode=axi.xUSER_DEFAULT,
                 raddr_user_mode=axi.AxUSER_NONCOHERENT,
                 noio=False,
                 enable_async=True, use_global_base_addr=False,
                 num_cmd_delay=0, num_data_delay=0,
                 op_sel_width=8, fsm_as_module=False):

        streamin = AXIStreamIn(m, '_'.join(['', name, 'streamin']), clk, rst, datawidth, addrwidth,
                               with_last=True,
                               id_width=rdata_id_width, user_width=rdata_user_width, dest_width=0,
                               noio=True,
                               enable_async=enable_async,
                               num_cmd_delay=num_cmd_delay, num_data_delay=num_data_delay,
                               op_sel_width=op_sel_width, fsm_as_module=fsm_as_module)

        AXIM.__init__(self, m, name, clk, rst, datawidth, addrwidth,
                      waddr_id_width, wdata_id_width, wresp_id_width,
                      raddr_id_width, rdata_id_width,
                      waddr_user_width, wdata_user_width, wresp_user_width,
                      raddr_user_width, rdata_user_width,
                      waddr_burst_mode, raddr_burst_mode,
                      waddr_cache_mode, raddr_cache_mode,
                      waddr_prot_mode, raddr_prot_mode,
                      waddr_user_mode, wdata_user_mode,
                      raddr_user_mode,
                      noio,
                      enable_async, use_global_base_addr,
                      num_cmd_delay, num_data_delay,
                      op_sel_width, fsm_as_module)

        self.streamin = streamin
        self.streamin.connect_master_rdata(self)

    def dma_read(self, fsm, ram, local_addr, global_addr, size,
                 local_stride=1, port=0, ram_method=None):

        if ram_method is None:
            ram_method = getattr(ram, 'write_dataflow')

        ram_method_name = (ram_method.func.__name__
                           if isinstance(ram_method, functools.partial) else
                           ram_method.__name__)
        ram_datawidth = (ram.datawidth if ram_method is None else
                         ram.orig_datawidth if 'bcast' in ram_method_name else
                         ram.orig_datawidth if 'block' in ram_method_name else
                         ram.datawidth)

        if ram_datawidth == self.datawidth:
            dma_size = size
        elif ram_datawidth > self.datawidth:
            pack_size = ram_datawidth // self.datawidth
            dma_size = (size << int(math.log(pack_size, 2))
                        if math.log(pack_size, 2) % 1.0 == 0.0 else
                        size * pack_size)
        else:
            pack_size = self.datawidth // ram_datawidth
            shamt = int(math.log(pack_size, 2))
            res = vtypes.Mux(
                vtypes.And(size, 2 ** shamt - 1) > 0, 1, 0)
            dma_size = (size >> shamt) + res

        AXIM_for_AXIStreamIn.dma_read_async(self, fsm, global_addr, dma_size)
        self.streamin.write_ram(fsm, ram, local_addr, size,
                                local_stride, port, ram_method)

    def dma_read_async(self, fsm, ram, local_addr, global_addr, size,
                       local_stride=1, port=0, ram_method=None):

        if ram_method is None:
            ram_method = getattr(ram, 'write_dataflow')

        ram_method_name = (ram_method.func.__name__
                           if isinstance(ram_method, functools.partial) else
                           ram_method.__name__)
        ram_datawidth = (ram.datawidth if ram_method is None else
                         ram.orig_datawidth if 'bcast' in ram_method_name else
                         ram.orig_datawidth if 'block' in ram_method_name else
                         ram.datawidth)

        if ram_datawidth == self.datawidth:
            dma_size = size
        elif ram_datawidth > self.datawidth:
            pack_size = ram_datawidth // self.datawidth
            dma_size = (size << int(math.log(pack_size, 2))
                        if math.log(pack_size, 2) % 1.0 == 0.0 else
                        size * pack_size)
        else:
            pack_size = self.datawidth // ram_datawidth
            shamt = int(math.log(pack_size, 2))
            res = vtypes.Mux(
                vtypes.And(size, 2 ** shamt - 1) > 0, 1, 0)
            dma_size = (size >> shamt) + res

        AXIM_for_AXIStreamIn.dma_read_async(self, fsm, global_addr, dma_size)
        self.streamin.write_ram_async(fsm, ram, local_addr, size,
                                      local_stride, port, ram_method)
