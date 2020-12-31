from __future__ import absolute_import
from __future__ import print_function

import functools
import math

import veriloggen.core.vtypes as vtypes
import veriloggen.dataflow.dtypes as dtypes
import veriloggen.types.fixed as fxd
import veriloggen.types.util as util

from veriloggen.seq.seq import Seq, TmpSeq, make_condition
from veriloggen.fsm.fsm import TmpFSM
from veriloggen.types.ram import RAMInterface, mkRAMDefinition
from veriloggen.dataflow.dataflow import DataflowManager
from veriloggen.dataflow.dtypes import _Numeric as df_numeric

from .ttypes import _MutexFunction


class RAM(_MutexFunction):
    __intrinsics__ = ('read', 'write') + _MutexFunction.__intrinsics__

    def __init__(self, m, name, clk, rst,
                 datawidth=32, addrwidth=10, numports=1,
                 initvals=None, nocheck_initvals=False,
                 ram_style=None, nodataflow=False, external_ports=None):

        self.m = m
        self.name = name
        self.clk = clk
        self.rst = rst

        self.datawidth = datawidth
        self.addrwidth = addrwidth
        self.numports = numports

        if external_ports is None:
            external_ports = ()

        self.interfaces = []

        for i in range(numports):
            if i in external_ports:
                interface = RAMInterface(m, name + '_%d' % i, datawidth, addrwidth,
                                         itype='Input', otype='Output', with_enable=True)
            else:
                interface = RAMInterface(m, name + '_%d' % i, datawidth, addrwidth,
                                         itype='Wire', otype='Wire', with_enable=True)

            self.interfaces.append(interface)

        for interface in self.interfaces:
            interface.wdata.no_write_check = True

        self.definition = mkRAMDefinition(
            name, datawidth, addrwidth, numports, initvals,
            with_enable=True,
            nocheck_initvals=nocheck_initvals,
            ram_style=ram_style)

        self.inst = self.m.Instance(self.definition, 'inst_' + name,
                                    ports=m.connect_ports(self.definition))

        self.seq = Seq(m, name, clk, rst)
        if nodataflow:
            self.df = None
        else:
            self.df = DataflowManager(self.m, self.clk, self.rst)

        self._write_disabled = [False for i in range(numports)]
        self._port_disabled = [False for i in range(numports)]

        self.mutex = None

    def __getitem__(self, index):
        return self.interfaces[index]

    def _id(self):
        return id(self)

    @property
    def length(self):
        if isinstance(self.addrwidth, int):
            return 2 ** self.addrwidth
        return vtypes.Int(2) ** self.addrwidth

    def disable_write(self, port):
        self.interfaces[port].wdata.connect(0)
        self.interfaces[port].wenable.connect(0)
        self._write_disabled[port] = True

    def disable_port(self, port):
        self.interfaces[port].addr.connect(0)
        self.interfaces[port].enable.connect(0)
        self._port_disabled[port] = True

    def connect_rtl(self, port, addr, wdata=None, wenable=None, rdata=None, enable=None):
        """ connect native signals to the internal RAM interface """

        self.interfaces[port].addr.connect(addr)
        if wdata is not None:
            self.interfaces[port].wdata.connect(wdata)
        if wenable is not None:
            self.interfaces[port].wenable.connect(wenable)
        if rdata is not None:
            rdata.connect(self.interfaces[port].rdata)

        if enable is not None:
            if hasattr(self.interfaces[port], 'enable'):
                self.interfaces[port].enable.connect(enable)
            else:
                raise ValueError("RAM '%s' has no enable port.")

        elif hasattr(self.interfaces[port], 'enable'):
            raise ValueError('enable must be assigned.')

    def read_rtl(self, addr, port=0, cond=None):
        """
        @return data, valid
        """

        cond = make_condition(cond)

        if cond is not None:
            enable = cond
        else:
            enable = vtypes.Int(1, 1)

        util.add_mux(self.interfaces[port].addr, enable, addr)
        util.add_enable_cond(self.interfaces[port].enable, enable, vtypes.Int(1, 1))

        rdata = self.interfaces[port].rdata
        rvalid = self.seq.Prev(enable, 1)

        return rdata, rvalid

    def write_rtl(self, addr, wdata, port=0, cond=None):
        """
        @return None
        """
        if self._write_disabled[port]:
            raise TypeError('Write disabled.')

        cond = make_condition(cond)

        if cond is not None:
            enable = cond
        else:
            enable = vtypes.Int(1, 1)

        util.add_mux(self.interfaces[port].addr, enable, addr)
        util.add_mux(self.interfaces[port].wdata, enable, wdata)
        util.add_enable_cond(self.interfaces[port].wenable, enable, vtypes.Int(1, 1))
        util.add_enable_cond(self.interfaces[port].enable, enable, vtypes.Int(1, 1))

    def read(self, fsm, addr, port=0):
        """ intrinsic read operation using a shared Seq object """

        port = vtypes.to_int(port)
        cond = fsm.state == fsm.current

        rdata, rvalid = self.read_rtl(addr, port, cond)
        rdata_reg = self.m.TmpReg(self.datawidth, initval=0, signed=True)

        fsm.If(rvalid)(
            rdata_reg(rdata)
        )
        fsm.Then().goto_next()

        return rdata_reg

    def write(self, fsm, addr, wdata, port=0, cond=None):
        """ intrinsic write operation using a shared Seq object """

        port = vtypes.to_int(port)

        if cond is None:
            cond = fsm.state == fsm.current
        else:
            cond = vtypes.Ands(cond, fsm.state == fsm.current)

        self.write_rtl(addr, wdata, port, cond)
        fsm.goto_next()

        return 0

    def read_dataflow(self, port, addr, length=1,
                      stride=1, cond=None, point=0, signed=True):
        """ 
        @return data, last, done
        """

        data_valid = self.m.TmpReg(initval=0)
        last_valid = self.m.TmpReg(initval=0)
        data_ready = self.m.TmpWire()
        last_ready = self.m.TmpWire()
        data_ready.assign(1)
        last_ready.assign(1)

        data_ack = vtypes.Ors(data_ready, vtypes.Not(data_valid))
        last_ack = vtypes.Ors(last_ready, vtypes.Not(last_valid))

        ext_cond = dtypes.make_condition(cond)
        data_cond = dtypes.make_condition(data_ack, last_ack)

        data = self.m.TmpWireLike(self.interfaces[port].rdata, signed=True)

        data.assign(self.interfaces[port].rdata)

        next_valid_on = self.m.TmpReg(initval=0)
        next_valid_off = self.m.TmpReg(initval=0)

        next_last = self.m.TmpReg(initval=0)
        last = self.m.TmpReg(initval=0)

        counter = self.m.TmpReg(vtypes.get_width(length), initval=0)

        read_addr = self.m.TmpRegLike(self.interfaces[port].addr, initval=0)

        read_cond = next_valid_on
        read_enable = vtypes.Ands(data_cond, next_valid_on)
        util.add_mux(self.interfaces[port].addr, read_cond, read_addr)
        util.add_enable_cond(self.interfaces[port].enable, read_enable, vtypes.Int(1, 1))

        self.seq.If(data_cond, next_valid_off)(
            last(0),
            data_valid(0),
            last_valid(0),
            next_valid_off(0)
        )

        self.seq.If(data_cond, next_valid_on)(
            data_valid(1),
            last_valid(1),
            last(next_last),
            next_last(0),
            next_valid_on(0),
            next_valid_off(1)
        )

        self.seq.If(ext_cond, counter == 0,
                    vtypes.Not(next_last), vtypes.Not(last))(
            read_addr(addr),
            counter(length - 1),
            next_valid_on(1),
            next_last(length == 1)
        )

        self.seq.If(data_cond, counter > 0)(
            read_addr(read_addr + stride),
            counter.dec(),
            next_valid_on(1),
            next_last(0)
        )

        self.seq.If(data_cond, counter == 1)(
            next_last(1)
        )

        df_data = self.df.Variable(data, data_valid, data_ready,
                                   width=self.datawidth, point=point, signed=signed)
        df_last = self.df.Variable(
            last, last_valid, last_ready, width=1, signed=False)
        done = last

        return df_data, df_last, done

    def read_dataflow_pattern(self, port, addr, pattern,
                              cond=None, point=0, signed=True):
        """ 
        @return data, last, done
        """

        if not isinstance(pattern, (tuple, list)):
            raise TypeError('pattern must be list or tuple.')

        if not pattern:
            raise ValueError(
                'pattern must have one (size, stride) pair at least.')

        if not isinstance(pattern[0], (tuple, list)):
            pattern = (pattern,)

        data_valid = self.m.TmpReg(initval=0)
        last_valid = self.m.TmpReg(initval=0)
        data_ready = self.m.TmpWire()
        last_ready = self.m.TmpWire()
        data_ready.assign(1)
        last_ready.assign(1)

        data_ack = vtypes.Ors(data_ready, vtypes.Not(data_valid))
        last_ack = vtypes.Ors(last_ready, vtypes.Not(last_valid))

        ext_cond = dtypes.make_condition(cond)
        data_cond = dtypes.make_condition(data_ack, last_ack)

        data = self.m.TmpWireLike(self.interfaces[port].rdata, signed=True)

        data.assign(self.interfaces[port].rdata)

        next_valid_on = self.m.TmpReg(initval=0)
        next_valid_off = self.m.TmpReg(initval=0)

        next_last = self.m.TmpReg(initval=0)
        last = self.m.TmpReg(initval=0)

        running = self.m.TmpReg(initval=0)

        next_addr = self.m.TmpWire(self.addrwidth)
        offset_addr = self.m.TmpWire(self.addrwidth)
        offsets = [self.m.TmpReg(self.addrwidth, initval=0)
                   for _ in pattern[1:]]

        offset_addr_value = addr
        for offset in offsets:
            offset_addr_value = offset + offset_addr_value
        offset_addr.assign(offset_addr_value)

        offsets.insert(0, None)

        count_list = [self.m.TmpReg(vtypes.get_width(out_size), initval=0)
                      for (out_size, out_stride) in pattern]

        read_addr = self.m.TmpRegLike(self.interfaces[port].addr, initval=0)

        read_cond = next_valid_on
        read_enable = vtypes.Ands(data_cond, next_valid_on)
        util.add_mux(self.interfaces[port].addr, read_cond, read_addr)
        util.add_enable_cond(self.interfaces[port].enable, read_enable, vtypes.Int(1, 1))

        self.seq.If(data_cond, next_valid_off)(
            last(0),
            data_valid(0),
            last_valid(0),
            next_valid_off(0)
        )

        self.seq.If(data_cond, next_valid_on)(
            data_valid(1),
            last_valid(1),
            last(next_last),
            next_last(0),
            next_valid_on(0),
            next_valid_off(1)
        )

        self.seq.If(ext_cond, vtypes.Not(running),
                    vtypes.Not(next_last), vtypes.Not(last))(
            read_addr(addr),
            running(1),
            next_valid_on(1)
        )

        self.seq.If(data_cond, running)(
            read_addr(next_addr),
            next_valid_on(1),
            next_last(0)
        )

        update_count = None
        update_offset = None
        update_addr = None
        last_one = None
        stride_value = None
        carry = None

        for offset, count, (out_size, out_stride) in zip(offsets, count_list, pattern):
            self.seq.If(ext_cond, vtypes.Not(running),
                        vtypes.Not(next_last), vtypes.Not(last))(
                count(out_size - 1)
            )
            self.seq.If(data_cond, running, update_count)(
                count.dec()
            )
            self.seq.If(data_cond, running, update_count, count == 0)(
                count(out_size - 1)
            )

            if offset is not None:
                self.seq.If(ext_cond, vtypes.Not(running),
                            vtypes.Not(next_last), vtypes.Not(last))(
                    offset(0)
                )
                self.seq.If(data_cond, running, update_offset, vtypes.Not(carry))(
                    offset(offset + out_stride)
                )
                self.seq.If(data_cond, running, update_offset, count == 0)(
                    offset(0)
                )

            if update_count is None:
                update_count = count == 0
            else:
                update_count = vtypes.Ands(update_count, count == 0)

            if update_offset is None:
                update_offset = vtypes.Mux(out_size == 1, 1, count == 1)
            else:
                update_offset = vtypes.Ands(update_offset, count == carry)

            if update_addr is None:
                update_addr = count == 0
            else:
                update_addr = vtypes.Mux(carry, count == 0, update_addr)

            if last_one is None:
                last_one = count == 0
            else:
                last_one = vtypes.Ands(last_one, count == 0)

            if stride_value is None:
                stride_value = out_stride
            else:
                stride_value = vtypes.Mux(carry, out_stride, stride_value)

            if carry is None:
                carry = out_size == 1
            else:
                carry = vtypes.Ands(carry, out_size == 1)

        next_addr.assign(vtypes.Mux(update_addr, offset_addr,
                                    read_addr + stride_value))

        self.seq.If(data_cond, running, last_one)(
            running(0),
            next_last(1)
        )

        df_data = self.df.Variable(data, data_valid, data_ready,
                                   width=self.datawidth, point=point, signed=signed)
        df_last = self.df.Variable(
            last, last_valid, last_ready, width=1, signed=False)
        done = last

        return df_data, df_last, done

    def read_dataflow_multidim(self, port, addr, shape, order=None,
                               cond=None, point=0, signed=True):
        """ 
        @return data, last, done
        """

        if order is None:
            order = list(reversed(range(len(shape))))

        pattern = self._to_pattern(shape, order)
        return self.read_dataflow_pattern(port, addr, pattern,
                                          cond=cond, point=point, signed=signed)

    def read_dataflow_reuse(self, port, addr, length=1,
                            stride=1,
                            reuse_size=1, num_outputs=1,
                            cond=None, point=0, signed=True):
        """ 
        @return data, last, done
        """

        if not isinstance(num_outputs, int):
            raise TypeError('num_outputs must be int')

        data_valid = [self.m.TmpReg(initval=0) for _ in range(num_outputs)]
        last_valid = self.m.TmpReg(initval=0)
        data_ready = [self.m.TmpWire() for _ in range(num_outputs)]
        last_ready = self.m.TmpWire()

        for r in data_ready:
            r.assign(1)
        last_ready.assign(1)

        data_ack = vtypes.Ands(*[vtypes.Ors(r, vtypes.Not(v))
                                 for v, r in zip(data_valid, data_ready)])
        last_ack = vtypes.Ors(last_ready, vtypes.Not(last_valid))

        ext_cond = dtypes.make_condition(cond)
        data_cond = dtypes.make_condition(data_ack, last_ack)

        counter = self.m.TmpReg(vtypes.get_width(length), initval=0)

        last = self.m.TmpReg(initval=0)
        reuse_data = [self.m.TmpReg(self.datawidth, initval=0, signed=True)
                      for _ in range(num_outputs)]
        next_reuse_data = [self.m.TmpReg(self.datawidth, initval=0, signed=True)
                           for _ in range(num_outputs)]

        reuse_count = self.m.TmpReg(vtypes.get_width(reuse_size), initval=0)
        fill_reuse_count = self.m.TmpReg(initval=0)
        fetch_done = self.m.TmpReg(initval=0)

        fsm = TmpFSM(self.m, self.clk, self.rst)

        read_addr = self.m.TmpRegLike(self.interfaces[port].addr, initval=0)

        # initial state
        fsm.If(ext_cond)(
            read_addr(addr),
            fetch_done(0),
            counter(length)
        )
        fsm.If(ext_cond, length > 0).goto_next()

        read_cond = vtypes.Ands(fsm.here, ext_cond)
        read_enable = vtypes.Ands(fsm.here, ext_cond)
        util.add_mux(self.interfaces[port].addr, read_cond, read_addr)
        util.add_enable_cond(self.interfaces[port].enable, read_enable, vtypes.Int(1, 1))

        # initial prefetch state
        for n in next_reuse_data:
            fsm(
                read_addr(read_addr + stride),
                counter(vtypes.Mux(counter > 0, counter - 1, counter))
            )
            fsm.Delay(1)(
                n(self.interfaces[port].rdata)
            )

            read_cond = fsm.here
            read_enable = fsm.here
            util.add_mux(self.interfaces[port].addr, read_cond, read_addr)
            util.add_enable_cond(self.interfaces[port].enable, read_enable, vtypes.Int(1, 1))

            fsm.goto_next()

        fsm.goto_next()
        fsm.goto_next()

        # initial update state
        for n, r in zip(next_reuse_data, reuse_data):
            fsm(
                r(n)
            )

        fsm(
            fill_reuse_count(1),
            fetch_done(counter == 0)
        )
        fsm.Delay(1)(
            fill_reuse_count(0)
        )

        fsm.goto_next()

        # prefetch state
        read_start_state = fsm.current

        for n in next_reuse_data:
            fsm(
                read_addr(read_addr + stride),
                counter(vtypes.Mux(counter > 0, counter - 1, counter))
            )
            fsm.Delay(1)(
                n(self.interfaces[port].rdata)
            )

            read_cond = fsm.here
            read_enable = fsm.here
            util.add_mux(self.interfaces[port].addr, read_cond, read_addr)
            util.add_enable_cond(self.interfaces[port].enable, read_enable, vtypes.Int(1, 1))

            fsm.goto_next()

        fsm.goto_next()
        fsm.goto_next()

        # update state
        for n, r in zip(next_reuse_data, reuse_data):
            fsm.If(data_cond, reuse_count == 0)(
                r(n)
            )

        fsm.If(data_cond, reuse_count == 0)(
            fill_reuse_count(vtypes.Not(fetch_done)),
            fetch_done(counter == 0)
        )
        fsm.Delay(1)(
            fill_reuse_count(0)
        )

        # next -> prefetch state or initial state
        fsm.If(data_cond, reuse_count == 0, counter == 0).goto_init()
        fsm.If(data_cond, reuse_count == 0, counter > 0).goto(read_start_state)

        # output signal control
        self.seq.If(data_cond, last_valid)(
            last(0),
            [d(0) for d in data_valid],
            last_valid(0)
        )

        self.seq.If(fill_reuse_count)(
            reuse_count(reuse_size)
        )

        self.seq.If(data_cond, reuse_count > 0)(
            reuse_count.dec(),
            [d(1) for d in data_valid],
            last_valid(1),
            last(0)
        )

        self.seq.If(data_cond, reuse_count == 1, fetch_done)(
            last(1)
        )

        df_last = self.df.Variable(
            last, last_valid, last_ready, width=1, signed=False)
        done = last

        df_reuse_data = [self.df.Variable(d, v, r,
                                          width=self.datawidth, point=point, signed=signed)
                         for d, v, r in zip(reuse_data, data_valid, data_ready)]

        return tuple(df_reuse_data + [df_last, done])

    def read_dataflow_reuse_pattern(self, port, addr, pattern,
                                    reuse_size=1, num_outputs=1,
                                    cond=None, point=0, signed=True):
        """ 
        @return data, last, done
        """

        if not isinstance(pattern, (tuple, list)):
            raise TypeError('pattern must be list or tuple.')

        if not pattern:
            raise ValueError(
                'pattern must have one (size, stride) pair at least.')

        if not isinstance(pattern[0], (tuple, list)):
            pattern = (pattern,)

        if not isinstance(num_outputs, int):
            raise TypeError('num_outputs must be int')

        data_valid = [self.m.TmpReg(initval=0) for _ in range(num_outputs)]
        last_valid = self.m.TmpReg(initval=0)
        data_ready = [self.m.TmpWire() for _ in range(num_outputs)]
        last_ready = self.m.TmpWire()

        for r in data_ready:
            r.assign(1)
        last_ready.assign(1)

        data_ack = vtypes.Ands(*[vtypes.Ors(r, vtypes.Not(v))
                                 for v, r in zip(data_valid, data_ready)])
        last_ack = vtypes.Ors(last_ready, vtypes.Not(last_valid))

        ext_cond = dtypes.make_condition(cond)
        data_cond = dtypes.make_condition(data_ack, last_ack)

        next_addr = self.m.TmpWire(self.addrwidth)
        offset_addr = self.m.TmpWire(self.addrwidth)
        offsets = [self.m.TmpReg(self.addrwidth, initval=0)
                   for _ in pattern[1:]]

        offset_addr_value = addr
        for offset in offsets:
            offset_addr_value = offset + offset_addr_value
        offset_addr.assign(offset_addr_value)

        offsets.insert(0, None)

        count_list = [self.m.TmpReg(vtypes.get_width(out_size), initval=0)
                      for (out_size, out_stride) in pattern]

        last = self.m.TmpReg(initval=0)
        reuse_data = [self.m.TmpReg(self.datawidth, initval=0, signed=True)
                      for _ in range(num_outputs)]
        next_reuse_data = [self.m.TmpReg(self.datawidth, initval=0, signed=True)
                           for _ in range(num_outputs)]

        reuse_count = self.m.TmpReg(vtypes.get_width(reuse_size), initval=0)
        fill_reuse_count = self.m.TmpReg(initval=0)

        prefetch_done = self.m.TmpReg(initval=0)
        fetch_done = self.m.TmpReg(initval=0)

        update_addr = None
        stride_value = None
        carry = None

        for offset, count, (out_size, out_stride) in zip(offsets, count_list, pattern):
            if update_addr is None:
                update_addr = count == 0
            else:
                update_addr = vtypes.Mux(carry, count == 0, update_addr)

            if stride_value is None:
                stride_value = out_stride
            else:
                stride_value = vtypes.Mux(carry, out_stride, stride_value)

            if carry is None:
                carry = out_size == 1
            else:
                carry = vtypes.Ands(carry, out_size == 1)

        read_addr = self.m.TmpRegLike(self.interfaces[port].addr, initval=0)
        next_addr.assign(vtypes.Mux(update_addr, offset_addr,
                                    read_addr + stride_value))

        fsm = TmpFSM(self.m, self.clk, self.rst)

        # initial state
        fsm.If(ext_cond)(
            read_.addr(addr),
            prefetch_done(0),
            fetch_done(0)
        )

        read_cond = vtypes.Ands(fsm.here, ext_cond)
        read_enable = vtypes.Ands(fsm.here, ext_cond)
        util.add_mux(self.interfaces[port].addr, read_cond, read_addr)
        util.add_enable_cond(self.interfaces[port].enable, read_enable, vtypes.Int(1, 1))

        first = True
        for offset, count, (out_size, out_stride) in zip(offsets, count_list, pattern):
            fsm.If(ext_cond)(
                count(out_size) if first else count(out_size - 1),
            )
            if offset is not None:
                fsm.If(ext_cond)(
                    offset(0)
                )
            first = False

        fsm.If(ext_cond).goto_next()

        # initial prefetch state
        for n in next_reuse_data:
            update_count = None
            update_offset = None
            last_one = None
            carry = None

            for offset, count, (out_size, out_stride) in zip(offsets, count_list, pattern):
                fsm.If(update_count)(
                    count.dec()
                )
                fsm.If(update_count, count == 0)(
                    count(out_size - 1)
                )
                fsm(
                    read_addr(next_addr)
                )
                fsm.Delay(1)(
                    n(self.interfaces[port].rdata)
                )

                if offset is not None:
                    fsm.If(update_offset, vtypes.Not(carry))(
                        offset(offset + out_stride)
                    )
                    fsm.If(update_offset, count == 0)(
                        offset(0)
                    )

                read_cond = fsm.here
                read_enable = fsm.here
                util.add_mux(self.interfaces[port].addr, read_cond, read_addr)
                util.add_enable_cond(self.interfaces[port].enable, read_enable, vtypes.Int(1, 1))

                if update_count is None:
                    update_count = count == 0
                else:
                    update_count = vtypes.Ands(update_count, count == 0)

                if update_offset is None:
                    update_offset = vtypes.Mux(out_size == 1, 1, count == 1)
                else:
                    update_offset = vtypes.Ands(update_offset, count == carry)

                if last_one is None:
                    last_one = count == 0
                else:
                    last_one = vtypes.Ands(last_one, count == 0)

                if carry is None:
                    carry = out_size == 1
                else:
                    carry = vtypes.Ands(carry, out_size == 1)

            fsm.goto_next()

            fsm.If(last_one)(
                prefetch_done(1)
            )

        fsm.goto_next()
        fsm.goto_next()

        # initial update state
        for r, n in zip(reuse_data, next_reuse_data):
            fsm(
                r(n)
            )

        fsm(
            fetch_done(prefetch_done),
            fill_reuse_count(vtypes.Not(fetch_done))
        )
        fsm.Delay(1)(
            fill_reuse_count(0)
        )

        fsm.goto_next()

        # prefetch state
        read_start_state = fsm.current

        for n in next_reuse_data:
            update_count = None
            update_offset = None
            last_one = None
            carry = None

            for offset, count, (out_size, out_stride) in zip(offsets, count_list, pattern):
                fsm.If(update_count)(
                    count.dec()
                )
                fsm.If(update_count, count == 0)(
                    count(out_size - 1)
                )
                fsm(
                    read_addr(next_addr)
                )
                fsm.Delay(1)(
                    n(self.interfaces[port].rdata)
                )

                read_cond = fsm.here
                read_enable = fsm.here
                util.add_mux(self.interfaces[port].addr, read_cond, read_addr)
                util.add_enable_cond(self.interfaces[port].enable, read_enable, vtypes.Int(1, 1))

                if offset is not None:
                    fsm.If(update_offset, vtypes.Not(carry))(
                        offset(offset + out_stride)
                    )
                    fsm.If(update_offset, count == 0)(
                        offset(0)
                    )

                if update_count is None:
                    update_count = count == 0
                else:
                    update_count = vtypes.Ands(update_count, count == 0)

                if update_offset is None:
                    update_offset = vtypes.Mux(out_size == 1, 1, count == 1)
                else:
                    update_offset = vtypes.Ands(update_offset, count == carry)

                if last_one is None:
                    last_one = count == 0
                else:
                    last_one = vtypes.Ands(last_one, count == 0)

                if carry is None:
                    carry = out_size == 1
                else:
                    carry = vtypes.Ands(carry, out_size == 1)

            fsm.goto_next()

            fsm.If(last_one)(
                prefetch_done(1)
            )

        fsm.goto_next()
        fsm.goto_next()

        # update state
        for r, n in zip(reuse_data, next_reuse_data):
            fsm.If(data_cond, reuse_count == 0)(
                r(n)
            )

        fsm.If(data_cond, reuse_count == 0)(
            fetch_done(prefetch_done),
            fill_reuse_count(vtypes.Not(fetch_done))
        )
        fsm.Delay(1)(
            fill_reuse_count(0)
        )

        # next -> prefetch state or initial state
        fsm.If(data_cond, reuse_count == 0,
               fetch_done).goto_init()
        fsm.If(data_cond, reuse_count == 0,
               vtypes.Not(fetch_done)).goto(read_start_state)

        # output signal control
        self.seq.If(data_cond, last_valid)(
            last(0),
            [d(0) for d in data_valid],
            last_valid(0)
        )

        self.seq.If(fill_reuse_count)(
            reuse_count(reuse_size)
        )

        self.seq.If(data_cond, reuse_count > 0)(
            reuse_count.dec(),
            [d(1) for d in data_valid],
            last_valid(1),
            last(0)
        )

        self.seq.If(data_cond, reuse_count == 1, fetch_done)(
            last(1)
        )

        df_last = self.df.Variable(
            last, last_valid, last_ready, width=1, signed=False)
        done = last

        df_reuse_data = [self.df.Variable(d, v, r,
                                          width=self.datawidth, point=point, signed=signed)
                         for d, v, r in zip(reuse_data, data_valid, data_ready)]

        return tuple(df_reuse_data + [df_last, done])

    def read_dataflow_reuse_multidim(self, port, addr, shape, order=None,
                                     reuse_size=1, num_outputs=1,
                                     cond=None, point=0, signed=True):
        """ 
        @return data, last, done
        """

        if order is None:
            order = list(reversed(range(len(shape))))

        pattern = self._to_pattern(shape, order)
        return self.read_dataflow_reuse_pattern(port, addr, pattern,
                                                reuse_size, num_outputs,
                                                cond=cond, point=point, signed=signed)

    def write_dataflow(self, port, addr, data, length=1,
                       stride=1, cond=None, when=None):
        """ 
        @return done
        'data' and 'when' must be dataflow variables
        """

        if self._write_disabled[port]:
            raise TypeError('Write disabled.')

        counter = self.m.TmpReg(vtypes.get_width(length), initval=0)
        last = self.m.TmpReg(initval=0)

        ext_cond = dtypes.make_condition(cond)
        data_cond = dtypes.make_condition(counter > 0, vtypes.Not(last))

        if when is None or not isinstance(when, df_numeric):
            raw_data, raw_valid = data.read(cond=data_cond)
        else:
            data_list, raw_valid = dtypes.read_multi(
                self.m, data, when, cond=data_cond)
            raw_data = data_list[0]
            when = data_list[1]

        when_cond = dtypes.make_condition(when, ready=data_cond)
        if when_cond is not None:
            raw_valid = vtypes.Ands(when_cond, raw_valid)

        write_addr = self.m.TmpRegLike(self.interfaces[port].addr, initval=0)
        write_data = self.m.TmpRegLike(self.interfaces[port].wdata, initval=0)
        write_enable = self.m.TmpRegLike(self.interfaces[port].wenable, initval=0)

        util.add_mux(self.interfaces[port].addr, write_enable, write_addr)
        util.add_mux(self.interfaces[port].wdata, write_enable, write_data)
        util.add_enable_cond(self.interfaces[port].wenable, write_enable, vtypes.Int(1, 1))
        util.add_enable_cond(self.interfaces[port].enable, write_enable, vtypes.Int(1, 1))

        self.seq.If(ext_cond, counter == 0)(
            write_addr(addr - stride),
            counter(length),
        )

        self.seq.If(raw_valid, counter > 0)(
            write_addr(write_addr + stride),
            write_data(raw_data),
            write_enable(1),
            counter.dec()
        )

        self.seq.If(raw_valid, counter == 1)(
            last(1)
        )

        # de-assert
        self.seq.Delay(1)(
            write_enable(0),
            last(0)
        )

        done = last

        return done

    def write_dataflow_pattern(self, port, addr, data, pattern,
                               cond=None, when=None):
        """ 
        @return done
        'data' and 'when' must be dataflow variables
        """

        if self._write_disabled[port]:
            raise TypeError('Write disabled.')

        if not isinstance(pattern, (tuple, list)):
            raise TypeError('pattern must be list or tuple.')

        if not pattern:
            raise ValueError(
                'pattern must have one (size, stride) pair at least.')

        if not isinstance(pattern[0], (tuple, list)):
            pattern = (pattern,)

        last = self.m.TmpReg(initval=0)

        running = self.m.TmpReg(initval=0)

        ext_cond = dtypes.make_condition(cond)
        data_cond = dtypes.make_condition(running, vtypes.Not(last))

        if when is None or not isinstance(when, df_numeric):
            raw_data, raw_valid = data.read(cond=data_cond)
        else:
            data_list, raw_valid = dtypes.read_multi(
                self.m, data, when, cond=data_cond)
            raw_data = data_list[0]
            when = data_list[1]

        when_cond = dtypes.make_condition(when, ready=data_cond)
        if when_cond is not None:
            raw_valid = vtypes.Ands(when_cond, raw_valid)

        offset_addr = self.m.TmpWire(self.addrwidth)
        offsets = [self.m.TmpReg(self.addrwidth, initval=0) for _ in pattern]

        offset_addr_value = addr
        for offset in offsets:
            offset_addr_value = offset + offset_addr_value
        offset_addr.assign(offset_addr_value)

        count_list = [self.m.TmpReg(vtypes.get_width(out_size), initval=0)
                      for (out_size, out_stride) in pattern]

        self.seq.If(ext_cond, vtypes.Not(running))(
            running(1)
        )

        write_addr = self.m.TmpRegLike(self.interfaces[port].addr, initval=0)
        write_data = self.m.TmpRegLike(self.interfaces[port].wdata, initval=0)
        write_enable = self.m.TmpRegLike(self.interfaces[port].wenable, initval=0)

        util.add_mux(self.interfaces[port].addr, write_enable, write_addr)
        util.add_mux(self.interfaces[port].wdata, write_enable, write_data)
        util.add_enable_cond(self.interfaces[port].wenable, write_enable, vtypes.Int(1, 1))
        util.add_enable_cond(self.interfaces[port].enable, write_enable, vtypes.Int(1, 1))

        self.seq.If(raw_valid, running)(
            write_addr(offset_addr),
            write_data(raw_data),
            write_enable(1)
        )

        update_count = None
        last_one = None

        for offset, count, (out_size, out_stride) in zip(offsets, count_list, pattern):
            self.seq.If(ext_cond, vtypes.Not(running))(
                count(out_size - 1),
                offset(0)
            )
            self.seq.If(raw_valid, running, update_count)(
                count.dec(),
                offset(offset + out_stride)
            )
            self.seq.If(raw_valid, running, update_count, count == 0)(
                count(out_size - 1),
                offset(0)
            )

            if update_count is None:
                update_count = count == 0
            else:
                update_count = vtypes.Ands(update_count, count == 0)

            if last_one is None:
                last_one = count == 0
            else:
                last_one = vtypes.Ands(last_one, count == 0)

        self.seq.If(raw_valid, last_one)(
            running(0),
            last(1)
        )

        # de-assert
        self.seq.Delay(1)(
            write_enable(0),
            last(0)
        )

        done = last

        return done

    def write_dataflow_multidim(self, port, addr, data, shape, order=None,
                                cond=None, when=None):
        """ 
        @return done
        'data' and 'when' must be dataflow variables
        """

        if order is None:
            order = list(reversed(range(len(shape))))

        pattern = self._to_pattern(shape, order)
        return self.write_dataflow_pattern(port, addr, data, pattern,
                                           cond=cond, when=when)

    def _to_pattern(self, shape, order):
        pattern = []
        for p in order:
            if not isinstance(p, int):
                raise TypeError(
                    "Values of 'order' must be 'int', not %s" % str(type(p)))
            size = shape[p]
            basevalue = 1 if isinstance(size, int) else vtypes.Int(1)
            stride = functools.reduce(lambda x, y: x * y,
                                      shape[p + 1:], basevalue)
            pattern.append((size, stride))
        return pattern


class FixedRAM(RAM):

    def __init__(self, m, name, clk, rst,
                 datawidth=32, addrwidth=10, numports=1, point=0,
                 initvals=None, nocheck_initvals=False, noconvert_initvals=False,
                 ram_style=None, nodataflow=False, external_ports=None):

        if initvals is not None and not noconvert_initvals:
            initvals = [fxd.to_fixed(initval, point) for initval in initvals]

        RAM.__init__(self, m, name, clk, rst,
                     datawidth, addrwidth, numports,
                     initvals, nocheck_initvals, ram_style, nodataflow, external_ports)

        self.point = point

    def read(self, fsm, addr, port=0, raw=False):
        raw_value = RAM.read(self, fsm, addr, port)
        if raw:
            return raw_value
        return fxd.reinterpret_cast_to_fixed(raw_value, self.point)

    def write(self, fsm, addr, wdata, port=0, cond=None, raw=False):
        if raw:
            fixed_wdata = wdata
        else:
            fixed_wdata = fxd.write_adjust(wdata, self.point)

        return RAM.write(self, fsm, addr, fixed_wdata, port, cond)


def extract_rams(rams):
    ret = []

    for ram in rams:
        if isinstance(ram, MultibankRAM):
            ret.extend(extract_rams(ram.rams))
        else:
            ret.append(ram)

    return ret


class MultibankRAM(object):
    __intrinsics__ = (
        'read', 'write',
        'read_bank', 'write_bank',
        'dma_read_bank', 'dma_read_bank_async',
        'dma_write_bank', 'dma_write_bank_async',
        'dma_read_block', 'dma_read_block_async',
        'dma_write_block', 'dma_write_block_async') + _MutexFunction.__intrinsics__

    def __init__(self, m, name, clk, rst,
                 datawidth=32, addrwidth=10, numports=1, numbanks=2,
                 ram_style=None, external_ports=None):

        if numbanks < 2:
            raise ValueError('numbanks must be 2 or more')

        self.m = m
        self.name = name
        self.clk = clk
        self.rst = rst
        self.orig_datawidth = datawidth
        self.datawidth = datawidth * numbanks
        self.addrwidth = addrwidth
        self.numports = numports
        self.numbanks = numbanks
        self.shift = util.log2(self.numbanks)
        self.rams = [RAM(m, '_'.join([name, '%d' % i]),
                         clk, rst, datawidth, addrwidth, numports,
                         ram_style=ram_style, external_ports=external_ports)
                     for i in range(numbanks)]
        self.keep_hierarchy = False
        self.seq = None

        self.df = DataflowManager(self.m, self.clk, self.rst)

        # key: (axi._id(), port, ram_method_name)
        self.cache_dma_reqs = {}

        self.mutex = None

    def __getitem__(self, index):
        return self.rams[index]

    def _id(self):
        _ids = [ram._id() for ram in self.rams]
        return tuple(_ids)

    @property
    def length(self):
        if isinstance(self.addrwidth, int):
            return (2 ** self.addrwidth) * self.numbanks
        return (vtypes.Int(2) ** self.addrwidth) * self.numbanks

    def disable_write(self, port):
        for ram in self.rams:
            ram.seq(
                ram.interfaces[port].wdata(0),
                ram.interfaces[port].wenable(0)
            )
            ram._write_disabled[port] = True

    def connect_rtl(self, port, addr, wdata=None, wenable=None, rdata=None, enable=None):
        """ connect native signals to the internal RAM interface """

        if enable is not None:
            for ram in self.rams:
                if not hasattr(ram.interfaces[port], 'enable'):
                    raise ValueError("RAM '%s' has no enable port.")

        else:
            for ram in self.rams:
                if hasattr(ram.interfaces[port], 'enable'):
                    raise ValueError('enable must be assigned.')

        if math.log(self.numbanks, 2) % 1.0 != 0.0:
            raise ValueError('numbanks must be power-of-2')

        if self.seq is None:
            self.seq = Seq(self.m, self.name, self.clk, self.rst)

        bank = self.m.TmpWire(self.shift)
        bank.assign(addr)
        addr = addr >> self.shift

        rdata_list = []
        for i, ram in enumerate(self.rams):
            ram.interfaces[port].addr.connect(addr)

            if wdata is not None:
                ram.interfaces[port].wdata.connect(wdata)

            bank_wenable = vtypes.Ands(wenable, bank == i)
            if wenable is not None:
                ram.interfaces[port].wenable.connect(bank_wenable)

            rdata_list.append(ram.interfaces[port].rdata)
            bank_enable = vtypes.Ands(enable, bank == i)
            if enable is not None:
                ram.interfaces[port].enable.connect(bank_enable)

        bank_reg = self.seq.Prev(bank, 1, initval=0)
        pat = [(bank_reg == i, rdata_list[i])
               for i, ram in enumerate(self.rams)]
        pat.append((None, 0))

        rdata_wire = self.m.TmpWire(self.orig_datawidth, signed=True)
        rdata_wire.assign(vtypes.PatternMux(pat))

        if rdata is not None:
            rdata.connect(rdata_wire)

    def read_rtl(self, addr, port=0, cond=None):
        """
        @return data, valid
        """
        if math.log(self.numbanks, 2) % 1.0 != 0.0:
            raise ValueError('numbanks must be power-of-2')

        if self.seq is None:
            self.seq = Seq(self.m, self.name, self.clk, self.rst)

        rdata_list = []
        rvalid_list = []

        bank = self.m.TmpWire(self.shift)
        bank.assign(addr)
        addr = addr >> self.shift

        bank_reg = self.seq.Prev(bank, 1, initval=0)

        for ram in self.rams:
            rdata, rvalid = ram.read_rtl(addr, port, cond)
            rdata_list.append(rdata)
            rvalid_list.append(rvalid)

        rdata_wire = self.m.TmpWire(self.orig_datawidth, signed=True)
        rvalid_wire = self.m.TmpWire()

        pat = [(bank_reg == i, rdata_list[i])
               for i, ram in enumerate(self.rams)]
        pat.append((None, 0))

        rdata_wire.assign(vtypes.PatternMux(pat))
        rvalid_wire.assign(rvalid_list[0])

        return rdata_wire, rvalid_wire

    def write_rtl(self, addr, data, port=0, cond=None):
        """
        @return None
        """
        if math.log(self.numbanks, 2) % 1.0 != 0.0:
            raise ValueError('numbanks must be power-of-2')

        bank = self.m.TmpWire(self.shift)
        bank.assign(addr)
        addr = addr >> self.shift

        for i, ram in enumerate(self.rams):
            bank_cond = vtypes.Ands(cond, bank == i)
            ram.write_rtl(addr, data, port, bank_cond)

        return 0

    def _read_recursive(self, ram, port, addr, cond):
        if isinstance(ram, MultibankRAM):
            if math.log(ram.numbanks, 2) % 1.0 != 0.0:
                raise ValueError('numbanks must be power-of-2')

            rdata_list = []
            rvalid_list = []
            bank = self.m.TmpWire(ram.shift)
            bank.assign(addr)
            addr = addr >> ram.shift

            for sub in ram.rams:
                rdata, rvalid = self._read_recursive(sub, port, addr, cond)
                rdata_list.append(rdata)
                rvalid_list.append(rvalid)

            rdata_wire = self.m.TmpWire(ram.orig_datawidth, signed=True)

            patterns = [(bank == i, rdata)
                        for i, rdata in enumerate(rdata_list)]
            patterns.append((None, 0))
            rdata_wire.assign(vtypes.PatternMux(*patterns))

            return rdata_wire, rvalid_list[0]

        rdata, rvalid = ram.read_rtl(addr, port, cond)
        return rdata, rvalid

    def read(self, fsm, addr, port=0):
        if math.log(self.numbanks, 2) % 1.0 != 0.0:
            raise ValueError('numbanks must be power-of-2')

        port = vtypes.to_int(port)
        cond = fsm.state == fsm.current

        rdata_list = []
        rvalid_list = []

        bank = self.m.TmpWire(self.shift)
        bank.assign(addr)
        addr = addr >> self.shift

        for ram in self.rams:
            rdata, rvalid = self._read_recursive(ram, port, addr, cond)
            rdata_list.append(rdata)
            rvalid_list.append(rvalid)

        rdata_reg = self.m.TmpReg(self.orig_datawidth, initval=0, signed=True)

        for i, ram in enumerate(self.rams):
            fsm.If(rvalid_list[i], bank == i)(
                rdata_reg(rdata_list[i])
            )

        fsm.If(vtypes.Ors(*rvalid_list)).goto_next()

        return rdata_reg

    def _write_recursive(self, ram, port, addr, wdata, cond=None):
        if isinstance(ram, MultibankRAM):
            if math.log(ram.numbanks, 2) % 1.0 != 0.0:
                raise ValueError('numbanks must be power-of-2')

            bank = self.m.TmpWire(ram.shift)
            bank.assign(addr)
            addr = addr >> ram.shift

            for i, sub in enumerate(ram.rams):
                bank_cond = vtypes.Ands(cond, bank == i)
                self._write_recursive(sub, port, addr, wdata, bank_cond)

            return

        ram.write_rtl(addr, wdata, port, cond)

    def write(self, fsm, addr, wdata, port=0, cond=None):
        if math.log(self.numbanks, 2) % 1.0 != 0.0:
            raise ValueError('numbanks must be power-of-2')

        if cond is None:
            cond = fsm.state == fsm.current
        else:
            cond = vtypes.Ands(cond, fsm.state == fsm.current)

        bank = self.m.TmpWire(self.shift)
        bank.assign(addr)
        addr = addr >> self.shift

        for i, ram in enumerate(self.rams):
            bank_cond = vtypes.Ands(cond, bank == i)
            self._write_recursive(ram, port, addr, wdata, bank_cond)

        fsm.goto_next()

        return 0

    def read_bank(self, fsm, bank, addr, port=0):
        port = vtypes.to_int(port)
        cond = fsm.state == fsm.current

        rdata_list = []
        rvalid_list = []
        for ram in self.rams:
            rdata, rvalid = self._read_recursive(ram, port, addr, cond)
            rdata_list.append(rdata)
            rvalid_list.append(rvalid)

        rdata_reg = self.m.TmpReg(self.orig_datawidth, initval=0, signed=True)

        for i, ram in enumerate(self.rams):
            fsm.If(rvalid_list[i], bank == i)(
                rdata_reg(rdata_list[i])
            )

        fsm.If(vtypes.Ors(*rvalid_list)).goto_next()

        return rdata_reg

    def write_bank(self, fsm, bank, addr, wdata, port=0, cond=None):
        if cond is None:
            cond = fsm.state == fsm.current
        else:
            cond = vtypes.Ands(cond, fsm.state == fsm.current)

        for i, ram in enumerate(self.rams):
            bank_cond = vtypes.Ands(cond, bank == i)
            self._write_recursive(ram, port, addr, wdata, bank_cond)

        fsm.goto_next()

        return 0

    def dma_read_bank(self, fsm, bank, bus, local_addr, global_addr, size,
                      local_stride=1, port=0):

        if bus.enable_async:
            bus.dma_wait_read(fsm)

        self._dma_read_bank(fsm, bank, bus, local_addr, global_addr, size,
                            local_stride, port)

        bus.dma_wait_read(fsm)

    def dma_read_bank_async(self, fsm, bank, bus, local_addr, global_addr, size,
                            local_stride=1, port=0):

        if not bus.enable_async:
            raise ValueError(
                "Async mode is disabled. Set 'True' to AXIM.enable_async.")

        bus.dma_wait_read(fsm)

        self._dma_read_bank(fsm, bank, bus, local_addr, global_addr, size,
                            local_stride, port)

    def _dma_read_bank(self, fsm, bank, bus, local_addr, global_addr, size,
                       local_stride=1, port=0):
        check = fsm.current
        fsm.set_index(check + 1)

        starts = []
        ends = []
        for i, ram in enumerate(self.rams):
            starts.append(fsm.current)
            bus._dma_read(fsm, ram, local_addr, global_addr, size,
                          local_stride, port)
            ends.append(fsm.current)
            fsm.set_index(fsm.current + 1)

        fin = fsm.current

        for i, (s, e) in enumerate(zip(starts, ends)):
            fsm.goto_from(check, s, cond=bank == i)
            fsm.goto_from(e, fin)

    def dma_write_bank(self, fsm, bank, bus, local_addr, global_addr, size,
                       local_stride=1, port=0):

        if bus.enable_async:
            bus.dma_wait_write(fsm)

        self._dma_write_bank(fsm, bank, bus, local_addr, global_addr, size,
                             local_stride, port)

        bus.dma_wait_write(fsm)

    def dma_write_bank_async(self, fsm, bank, bus, local_addr, global_addr, size,
                             local_stride=1, port=0):

        if not bus.enable_async:
            raise ValueError(
                "Async mode is disabled. Set 'True' to AXIM.enable_async.")

        bus.dma_wait_write(fsm)

        self._dma_write_bank(fsm, bank, bus, local_addr, global_addr, size,
                             local_stride, port)

    def _dma_write_bank(self, fsm, bank, bus, local_addr, global_addr, size,
                        local_stride=1, port=0):
        check = fsm.current
        fsm.set_index(check + 1)

        starts = []
        ends = []
        for i, ram in enumerate(self.rams):
            starts.append(fsm.current)
            bus._dma_write(fsm, ram, local_addr, global_addr, size,
                           local_stride, port)
            ends.append(fsm.current)
            fsm.set_index(fsm.current + 1)

        fin = fsm.current

        for i, (s, e) in enumerate(zip(starts, ends)):
            fsm.goto_from(check, s, cond=bank == i)
            fsm.goto_from(e, fin)

    def dma_read_block(self, fsm, bus, local_addr, global_addr, size,
                       block_size=1, local_stride=1, port=0):

        if bus.enable_async:
            bus.dma_wait_read(fsm)

        self._dma_read_block(fsm, bus, local_addr, global_addr, size,
                             block_size, local_stride, port)

        bus.dma_wait_read(fsm)

    def dma_read_block_async(self, fsm, bus, local_addr, global_addr, size,
                             block_size=1, local_stride=1, port=0):

        if not bus.enable_async:
            raise ValueError(
                "Async mode is disabled. Set 'True' to AXIM.enable_async.")

        bus.dma_wait_read(fsm)

        self._dma_read_block(fsm, bus, local_addr, global_addr, size,
                             block_size, local_stride, port)

    def _dma_read_block(self, fsm, bus, local_addr, global_addr, size,
                        block_size=1, local_stride=1, port=0):

        cache_key = (id(bus), port)

        if cache_key in self.cache_dma_reqs:
            info = self.cache_dma_reqs[cache_key]
            seq = info[0]
            req_block_size = info[1]
        else:
            seq = TmpSeq(bus.m, bus.clk, bus.rst)
            req_block_size = self.m.TmpReg(self.addrwidth, initval=0,
                                           prefix='req_block_size')
            info = (seq, req_block_size)
            self.cache_dma_reqs[cache_key] = info

        set_req = bus._set_flag(fsm, prefix='set_req')
        seq.If(set_req)(
            req_block_size(block_size)
        )

        ram_method = functools.partial(self.write_dataflow_block,
                                       block_size=req_block_size)

        bus._dma_read(fsm, self, local_addr, global_addr, size,
                      local_stride, port, ram_method)

    def dma_write_block(self, fsm, bus, local_addr, global_addr, size,
                        block_size=1, local_stride=1, port=0):

        if bus.enable_async:
            bus.dma_wait_write(fsm)

        self._dma_write_block(fsm, bus, local_addr, global_addr, size,
                              block_size, local_stride, port)

        bus.dma_wait_write(fsm)

    def dma_write_block_async(self, fsm, bus, local_addr, global_addr, size,
                              block_size=1, local_stride=1, port=0):

        if not bus.enable_async:
            raise ValueError(
                "Async mode is disabled. Set 'True' to AXIM.enable_async.")

        bus.dma_wait_write(fsm)

        self._dma_write_block(fsm, bus, local_addr, global_addr, size,
                              block_size, local_stride, port)

    def _dma_write_block(self, fsm, bus, local_addr, global_addr, size,
                         block_size=1, local_stride=1, port=0):

        cache_key = (id(bus), port)

        if cache_key in self.cache_dma_reqs:
            info = self.cache_dma_reqs[cache_key]
            seq = info[0]
            req_block_size = info[1]
        else:
            seq = TmpSeq(bus.m, bus.clk, bus.rst)
            req_block_size = self.m.TmpReg(self.addrwidth, initval=0,
                                           prefix='req_block_size')
            info = (seq, req_block_size)
            self.cache_dma_reqs[cache_key] = info

        set_req = bus._set_flag(fsm, prefix='set_req')
        seq.If(set_req)(
            req_block_size(block_size)
        )

        ram_method = functools.partial(self.read_dataflow_block,
                                       block_size=req_block_size)

        bus._dma_write(fsm, self, local_addr, global_addr, size,
                       local_stride, port, ram_method)

    def read_dataflow(self, port, addr, length=1,
                      stride=1, cond=None, point=0, signed=True):
        """ 
        @return data, last, done
        """

        data_list = []
        last_list = []
        done_list = []
        for ram in self.rams:
            data, last, done = ram.read_dataflow(
                port, addr, length, stride, cond, point, signed)
            data_list.insert(0, data)
            last_list.insert(0, last)
            done_list.insert(0, done)

        merged_data = dtypes.Cat(*data_list)
        merged_last = last_list[-1]
        merged_done = done_list[-1]

        return merged_data, merged_last, merged_done

    def read_dataflow_interleave(self, port, addr, length=1,
                                 stride=1, cond=None, point=0, signed=True):
        """ 
        @return data, last, done
        """

        if self.seq is None:
            self.seq = Seq(self.m, self.name, self.clk, self.rst)

        data_valid = self.m.TmpReg(initval=0)
        last_valid = self.m.TmpReg(initval=0)
        data_ready = self.m.TmpWire()
        last_ready = self.m.TmpWire()
        data_ready.assign(1)
        last_ready.assign(1)

        data_ack = vtypes.Ors(data_ready, vtypes.Not(data_valid))
        last_ack = vtypes.Ors(last_ready, vtypes.Not(last_valid))

        ext_cond = dtypes.make_condition(cond)
        data_cond = dtypes.make_condition(data_ack, last_ack)
        prev_data_cond = self.seq.Prev(data_cond, 1)

        data_list = [self.m.TmpWireLike(ram.interfaces[port].rdata, signed=True)
                     for ram in self.rams]

        for data, ram in zip(data_list, self.rams):
            data.assign(ram.interfaces[port].rdata)

        log_numbanks = util.log2(self.numbanks)
        reg_addr = self.m.TmpReg(self.addrwidth + log_numbanks, initval=0)
        next_addr = self.m.TmpWire(self.addrwidth + log_numbanks)
        next_addr.assign(reg_addr + stride)
        ram_addr_list = [self.m.TmpWire(ram.addrwidth) for ram in self.rams]
        for ram_addr in ram_addr_list:
            ram_addr.assign(next_addr >> log_numbanks)

        bank_sel = self.m.TmpWire(log_numbanks)
        bank_sel.assign(reg_addr[0:log_numbanks])
        reg_bank_sel = self.m.TmpReg(log_numbanks, initval=0)
        prev_reg_bank_sel = self.seq.Prev(reg_bank_sel, 1)
        self.seq.If(data_cond)(
            reg_bank_sel(bank_sel)
        )

        cur_bank_sel = vtypes.Mux(prev_data_cond, reg_bank_sel, prev_reg_bank_sel)
        patterns = [(cur_bank_sel == i, data)
                    for i, data in enumerate(data_list)]
        patterns.append((None, 0))

        data = self.m.TmpWire(self.orig_datawidth, signed=True)
        data.assign(vtypes.PatternMux(*patterns))

        next_valid_on = self.m.TmpReg(initval=0)
        next_valid_off = self.m.TmpReg(initval=0)

        next_last = self.m.TmpReg(initval=0)
        last = self.m.TmpReg(initval=0)

        counter = self.m.TmpReg(vtypes.get_width(length), initval=0)

        read_addr_list = [self.m.TmpRegLike(ram.interfaces[port].addr, initval=0)
                          for ram in self.rams]

        read_cond = next_valid_on
        read_enable = vtypes.Ands(data_cond, next_valid_on)
        for ram, read_addr in zip(self.rams, read_addr_list):
            util.add_mux(ram.interfaces[port].addr, read_cond, read_addr)
            util.add_enable_cond(ram.interfaces[port].enable, read_enable, vtypes.Int(1, 1))

        self.seq.If(data_cond, next_valid_off)(
            last(0),
            data_valid(0),
            last_valid(0),
            next_valid_off(0)
        )

        self.seq.If(data_cond, next_valid_on)(
            data_valid(1),
            last_valid(1),
            last(next_last),
            next_last(0),
            next_valid_on(0),
            next_valid_off(1)
        )

        self.seq.If(ext_cond, counter == 0,
                    vtypes.Not(next_last), vtypes.Not(last))(
            reg_addr(addr),
            counter(length - 1),
            next_valid_on(1),
            next_last(length == 1)
        )

        for read_addr in read_addr_list:
            self.seq.If(ext_cond, counter == 0,
                        vtypes.Not(next_last), vtypes.Not(last))(
                read_addr(addr >> log_numbanks)
            )

        self.seq.If(data_cond, counter > 0)(
            reg_addr(reg_addr + stride),
            counter.dec(),
            next_valid_on(1),
            next_last(0)
        )

        for read_addr, ram_addr in zip(read_addr_list, ram_addr_list):
            self.seq.If(data_cond, counter > 0)(
                read_addr(ram_addr)
            )

        self.seq.If(data_cond, counter == 1)(
            next_last(1)
        )

        df = self.df if self.df is not None else dataflow

        df_data = df.Variable(data, data_valid, data_ready,
                              width=self.orig_datawidth, point=point, signed=signed)
        df_last = df.Variable(last, last_valid, last_ready, width=1)
        done = last

        return df_data, df_last, done

    def read_dataflow_pattern_interleave(self, port, addr, pattern,
                                         cond=None, point=0, signed=True):
        """ 
        @return data, last, done
        """

        if self.seq is None:
            self.seq = Seq(self.m, self.name, self.clk, self.rst)

        if not isinstance(pattern, (tuple, list)):
            raise TypeError('pattern must be list or tuple.')

        if not pattern:
            raise ValueError(
                'pattern must have one (size, stride) pair at least.')

        if not isinstance(pattern[0], (tuple, list)):
            pattern = (pattern,)

        data_valid = self.m.TmpReg(initval=0)
        last_valid = self.m.TmpReg(initval=0)
        data_ready = self.m.TmpWire()
        last_ready = self.m.TmpWire()
        data_ready.assign(1)
        last_ready.assign(1)

        data_ack = vtypes.Ors(data_ready, vtypes.Not(data_valid))
        last_ack = vtypes.Ors(last_ready, vtypes.Not(last_valid))

        ext_cond = dtypes.make_condition(cond)
        data_cond = dtypes.make_condition(data_ack, last_ack)
        prev_data_cond = self.seq.Prev(data_cond, 1)

        data_list = [self.m.TmpWireLike(ram.interfaces[port].rdata, signed=True)
                     for ram in self.rams]

        for data, ram in zip(data_list, self.rams):
            data.assign(ram.interfaces[port].rdata)

        log_numbanks = util.log2(self.numbanks)
        reg_addr = self.m.TmpReg(self.addrwidth + log_numbanks, initval=0)

        bank_sel = self.m.TmpWire(log_numbanks)
        bank_sel.assign(reg_addr[0:log_numbanks])
        reg_bank_sel = self.m.TmpReg(log_numbanks, initval=0)
        prev_reg_bank_sel = self.seq.Prev(reg_bank_sel, 1)
        self.seq.If(data_cond)(
            reg_bank_sel(bank_sel)
        )

        cur_bank_sel = vtypes.Mux(prev_data_cond, reg_bank_sel, prev_reg_bank_sel)
        patterns = [(cur_bank_sel == i, data)
                    for i, data in enumerate(data_list)]
        patterns.append((None, 0))

        data = self.m.TmpWire(self.orig_datawidth, signed=True)
        data.assign(vtypes.PatternMux(*patterns))

        next_valid_on = self.m.TmpReg(initval=0)
        next_valid_off = self.m.TmpReg(initval=0)

        next_last = self.m.TmpReg(initval=0)
        last = self.m.TmpReg(initval=0)

        running = self.m.TmpReg(initval=0)

        next_addr = self.m.TmpWire(self.addrwidth + log_numbanks)
        offset_addr = self.m.TmpWire(self.addrwidth + log_numbanks)
        offsets = [self.m.TmpReg(self.addrwidth + log_numbanks, initval=0)
                   for _ in pattern[1:]]

        ram_addr_list = [self.m.TmpWire(ram.addrwidth) for ram in self.rams]
        for ram_addr in ram_addr_list:
            ram_addr.assign(next_addr >> log_numbanks)

        offset_addr_value = addr
        for offset in offsets:
            offset_addr_value = offset + offset_addr_value
        offset_addr.assign(offset_addr_value)

        offsets.insert(0, None)

        count_list = [self.m.TmpReg(vtypes.get_width(out_size), initval=0)
                      for (out_size, out_stride) in pattern]

        read_addr_list = [self.m.TmpRegLike(ram.interfaces[port].addr, initval=0)
                          for ram in self.rams]

        read_cond = next_valid_on
        read_enable = vtypes.Ands(data_cond, next_valid_on)
        for ram, read_addr in zip(self.rams, read_addr_list):
            util.add_mux(ram.interfaces[port].addr, read_cond, read_addr)
            util.add_enable_cond(ram.interfaces[port].enable, read_enable, vtypes.Int(1, 1))

        self.seq.If(data_cond, next_valid_off)(
            last(0),
            data_valid(0),
            last_valid(0),
            next_valid_off(0)
        )

        self.seq.If(data_cond, next_valid_on)(
            data_valid(1),
            last_valid(1),
            last(next_last),
            next_last(0),
            next_valid_on(0),
            next_valid_off(1)
        )

        self.seq.If(ext_cond, vtypes.Not(running),
                    vtypes.Not(next_last), vtypes.Not(last))(
            reg_addr(addr),
            running(1),
            next_valid_on(1)
        )

        for read_addr in read_addr_list:
            self.seq.If(ext_cond, vtypes.Not(running),
                        vtypes.Not(next_last), vtypes.Not(last))(
                read_addr(addr >> log_numbanks)
            )

        self.seq.If(data_cond, running)(
            reg_addr(next_addr),
            next_valid_on(1),
            next_last(0)
        )

        for read_addr, ram_addr in zip(read_addr_list, ram_addr_list):
            self.seq.If(data_cond, running)(
                ram.interfaces[port].addr(ram_addr)
            )

        update_count = None
        update_offset = None
        update_addr = None
        last_one = None
        stride_value = None
        carry = None

        for offset, count, (out_size, out_stride) in zip(offsets, count_list, pattern):
            self.seq.If(ext_cond, vtypes.Not(running),
                        vtypes.Not(next_last), vtypes.Not(last))(
                count(out_size - 1)
            )
            self.seq.If(data_cond, running, update_count)(
                count.dec()
            )
            self.seq.If(data_cond, running, update_count, count == 0)(
                count(out_size - 1)
            )

            if offset is not None:
                self.seq.If(ext_cond, vtypes.Not(running),
                            vtypes.Not(next_last), vtypes.Not(last))(
                    offset(0)
                )
                self.seq.If(data_cond, running, update_offset, vtypes.Not(carry))(
                    offset(offset + out_stride)
                )
                self.seq.If(data_cond, running, update_offset, count == 0)(
                    offset(0)
                )

            if update_count is None:
                update_count = count == 0
            else:
                update_count = vtypes.Ands(update_count, count == 0)

            if update_offset is None:
                update_offset = vtypes.Mux(out_size == 1, 1, count == 1)
            else:
                update_offset = vtypes.Ands(update_offset, count == carry)

            if update_addr is None:
                update_addr = count == 0
            else:
                update_addr = vtypes.Mux(carry, count == 0, update_addr)

            if last_one is None:
                last_one = count == 0
            else:
                last_one = vtypes.Ands(last_one, count == 0)

            if stride_value is None:
                stride_value = out_stride
            else:
                stride_value = vtypes.Mux(carry, out_stride, stride_value)

            if carry is None:
                carry = out_size == 1
            else:
                carry = vtypes.Ands(carry, out_size == 1)

        next_addr.assign(vtypes.Mux(update_addr, offset_addr,
                                    reg_addr + stride_value))

        self.seq.If(data_cond, running, last_one)(
            running(0),
            next_last(1)
        )

        df = self.df if self.df is not None else dataflow

        df_data = df.Variable(data, data_valid, data_ready,
                              width=self.datawidth, point=point, signed=signed)
        df_last = df.Variable(last, last_valid, last_ready, width=1)
        done = last

        return df_data, df_last, done

    def read_dataflow_multidim_interleave(self, port, addr, shape, order=None,
                                          cond=None, point=0, signed=True):
        """ 
        @return data, last, done
        """
        if order is None:
            order = list(reversed(range(len(shape))))

        pattern = self._to_pattern(shape, order)
        return self.read_dataflow_pattern_interleave(port, addr, pattern,
                                                     cond=cond, point=point, signed=signed)

    def read_dataflow_block(self, port, addr, length=1, block_size=1,
                            stride=1, cond=None, point=0, signed=True):
        """ 
        @return data, last, done
        """

        if self.keep_hierarchy and isinstance(self.rams[0], MultibankRAM):
            return self._read_dataflow_block_nested(port, addr, length, block_size,
                                                    stride, cond, point, signed)

        if self.seq is None:
            self.seq = Seq(self.m, self.name, self.clk, self.rst)

        data_valid = self.m.TmpReg(initval=0)
        last_valid = self.m.TmpReg(initval=0)
        data_ready = self.m.TmpWire()
        last_ready = self.m.TmpWire()
        data_ready.assign(1)
        last_ready.assign(1)

        data_ack = vtypes.Ors(data_ready, vtypes.Not(data_valid))
        last_ack = vtypes.Ors(last_ready, vtypes.Not(last_valid))

        ext_cond = dtypes.make_condition(cond)
        data_cond = dtypes.make_condition(data_ack, last_ack)
        prev_data_cond = self.seq.Prev(data_cond, 1)

        data_list = [self.m.TmpWireLike(ram.interfaces[port].rdata, signed=True)
                     for ram in self.rams]

        for data, ram in zip(data_list, self.rams):
            data.assign(ram.interfaces[port].rdata)

        log_numbanks = util.log2(self.numbanks)

        reg_addr_list = [self.m.TmpReg(self.addrwidth, initval=0)
                         for ram in self.rams]

        next_addr_list = [self.m.TmpWire(self.addrwidth)
                          for ram in self.rams]
        for next_addr, reg_addr in zip(next_addr_list, reg_addr_list):
            next_addr.assign(reg_addr + stride)

        ram_addr_list = [self.m.TmpWire(ram.addrwidth)
                         for ram in self.rams]
        for ram_addr, next_addr in zip(ram_addr_list, next_addr_list):
            ram_addr.assign(next_addr)

        bank_sel = self.m.TmpReg(log_numbanks, initval=0)
        reg_bank_sel = self.m.TmpReg(log_numbanks, initval=0)
        prev_reg_bank_sel = self.seq.Prev(reg_bank_sel, 1)
        self.seq.If(data_cond)(
            reg_bank_sel(bank_sel)
        )

        cur_bank_sel = vtypes.Mux(prev_data_cond, reg_bank_sel, prev_reg_bank_sel)
        patterns = [(cur_bank_sel == i, data)
                    for i, data in enumerate(data_list)]
        patterns.append((None, 0))

        data = self.m.TmpWire(self.orig_datawidth, signed=True)
        data.assign(vtypes.PatternMux(*patterns))

        next_valid_on = self.m.TmpReg(initval=0)
        next_valid_off = self.m.TmpReg(initval=0)

        next_last = self.m.TmpReg(initval=0)
        last = self.m.TmpReg(initval=0)

        block_counter = self.m.TmpReg(vtypes.get_width(block_size), initval=0)
        counter = self.m.TmpReg(vtypes.get_width(length), initval=0)

        read_addr_list = [self.m.TmpRegLike(ram.interfaces[port].addr, initval=0)
                          for ram in self.rams]

        read_cond = next_valid_on
        read_enable = vtypes.Ands(data_cond, next_valid_on)
        for ram, read_addr in zip(self.rams, read_addr_list):
            util.add_mux(ram.interfaces[port].addr, read_cond, read_addr)
            util.add_enable_cond(ram.interfaces[port].enable, read_enable, vtypes.Int(1, 1))

        self.seq.If(data_cond, next_valid_off)(
            last(0),
            data_valid(0),
            last_valid(0),
            next_valid_off(0)
        )

        self.seq.If(data_cond, next_valid_on)(
            data_valid(1),
            last_valid(1),
            last(next_last),
            next_last(0),
            next_valid_on(0),
            next_valid_off(1)
        )

        self.seq.If(ext_cond, counter == 0,
                    vtypes.Not(next_last), vtypes.Not(last))(
            bank_sel(0),
            reg_bank_sel(0),
            block_counter(block_size - 1),
            counter(length - 1),
            next_valid_on(1),
            next_last(length == 1)
        )

        for reg_addr in reg_addr_list:
            self.seq.If(ext_cond, counter == 0,
                        vtypes.Not(next_last), vtypes.Not(last))(
                reg_addr(addr)
            )

        for read_addr in read_addr_list:
            self.seq.If(ext_cond, counter == 0,
                        vtypes.Not(next_last), vtypes.Not(last))(
                read_addr(addr)
            )

        self.seq.If(data_cond, counter > 0)(
            block_counter.dec(),
            counter.dec(),
            next_valid_on(1),
            next_last(0)
        )

        self.seq.If(data_cond, counter > 0, block_counter == 0)(
            block_counter(block_size - 1),
            bank_sel.inc()
        )

        self.seq.If(data_cond, counter > 0, block_counter == 0,
                    bank_sel == self.numbanks - 1)(
            bank_sel(0)
        )

        for i, (reg_addr, next_addr) in enumerate(zip(reg_addr_list, next_addr_list)):
            self.seq.If(data_cond, counter > 0, bank_sel == i)(
                reg_addr(next_addr)
            )

        for i, (read_addr, ram_addr) in enumerate(zip(read_addr_list, ram_addr_list)):
            self.seq.If(data_cond, counter > 0, bank_sel == i)(
                read_addr(ram_addr)
            )

        self.seq.If(data_cond, counter == 1)(
            next_last(1)
        )

        df = self.df if self.df is not None else dataflow

        df_data = df.Variable(data, data_valid, data_ready,
                              width=self.orig_datawidth, point=point, signed=signed)
        df_last = df.Variable(last, last_valid, last_ready, width=1)
        done = last

        return df_data, df_last, done

    def _read_dataflow_block_nested(self, port, addr, length=1, block_size=1,
                                    stride=1, cond=None, point=0, signed=True):
        """ 
        @return data, last, done
        """

        len_rams = 0
        for ram in self.rams:
            if not isinstance(ram, MultibankRAM):
                raise TypeError('All sub-bank RAMs must be MultibankRAM.')
            if len_rams == 0:
                len_rams = len(ram.rams)
            elif len_rams != len(ram.rams):
                raise ValueError(
                    'All sub-bank RAMs must have the same number of RAMs.')

        rams = [[] for i in range(len_rams)]

        for ram in self.rams:
            for i, sub in enumerate(ram.rams):
                rams[i].append(sub)

        rams = [to_multibank_ram(ram_list, keep_hierarchy=True)
                for ram_list in rams]

        data_list = []
        last_list = []
        done_list = []
        for ram in rams:
            data, last, done = ram.read_dataflow_block(
                port, addr, length, block_size, stride, cond, point, signed)
            data_list.insert(0, data)
            last_list.insert(0, last)
            done_list.insert(0, done)

        merged_data = dtypes.Cat(*data_list)
        merged_last = last_list[-1]
        merged_done = done_list[-1]

        return merged_data, merged_last, merged_done

    def write_dataflow(self, port, addr, data, length=1,
                       stride=1, cond=None, when=None):
        """ 
        @return done
        """

        done_list = []
        lsb = 0
        msb = 0
        for ram in self.rams:
            msb = msb + ram.datawidth
            bank_data = dtypes.Slice(data, msb - 1, lsb)
            done = ram.write_dataflow(
                port, addr, bank_data, length, stride, cond, when)
            done_list.append(done)
            lsb = msb

        merged_done = done_list[0]
        return merged_done

    def write_dataflow_interleave(self, port, addr, data, length=1,
                                  stride=1, cond=None, when=None):
        """ 
        @return done
        'data' and 'when' must be dataflow variables
        """

        if self.seq is None:
            self.seq = Seq(self.m, self.name, self.clk, self.rst)

        for ram in self.rams:
            if ram._write_disabled[port]:
                raise TypeError('Write disabled.')

        counter = self.m.TmpReg(vtypes.get_width(length), initval=0)
        last = self.m.TmpReg(initval=0)

        ext_cond = dtypes.make_condition(cond)
        data_cond = dtypes.make_condition(counter > 0, vtypes.Not(last))

        if when is None or not isinstance(when, dtypes._Numeric):
            raw_data, raw_valid = data.read(cond=data_cond)
        else:
            data_list, raw_valid = dtypes.read_multi(
                self.m, data, when, cond=data_cond)
            raw_data = data_list[0]
            when = data_list[1]

        when_cond = dtypes.make_condition(when, ready=data_cond)
        if when_cond is not None:
            raw_valid = vtypes.Ands(when_cond, raw_valid)

        log_numbanks = util.log2(self.numbanks)
        reg_addr = self.m.TmpReg(self.addrwidth + log_numbanks, initval=0)
        next_addr = self.m.TmpWire(self.addrwidth + log_numbanks)
        next_addr.assign(reg_addr + stride)
        ram_addr_list = [self.m.TmpWire(ram.addrwidth) for ram in self.rams]
        for ram_addr in ram_addr_list:
            ram_addr.assign(next_addr >> log_numbanks)

        bank_sel = self.m.TmpWire(log_numbanks)
        bank_sel.assign(next_addr)

        write_addr_list = [self.m.TmpRegLike(ram.interfaces[port].addr, initval=0)
                           for ram in self.rams]
        write_data_list = [self.m.TmpRegLike(ram.interfaces[port].wdata, initval=0)
                           for ram in self.rams]
        write_enable_list = [self.m.TmpRegLike(ram.interfaces[port].enable, initval=0)
                             for ram in self.rams]

        for ram, write_addr, write_data, write_enable in zip(self.rams, write_addr_list,
                                                             write_data_list, write_enable_list):
            util.add_mux(ram.interfaces[port].addr, write_enable, write_addr)
            util.add_mux(ram.interfaces[port].wdata, write_enable, write_data)
            util.add_enable_cond(ram.interfaces[port].wenable, write_enable, vtypes.Int(1, 1))
            util.add_enable_cond(ram.interfaces[port].enable, write_enable, vtypes.Int(1, 1))

        self.seq.If(ext_cond, counter == 0)(
            reg_addr(addr - stride),
            counter(length),
        )

        self.seq.If(raw_valid, counter > 0)(
            reg_addr(next_addr),
            counter.dec()
        )

        for i, (write_addr, write_data,
                write_enable, ram_addr) in enumerate(zip(write_addr_list, write_data_list,
                                                         write_enable_list, ram_addr_list)):
            self.seq.If(raw_valid, counter > 0)(
                write_addr(ram_addr),
                write_data(raw_data),
                write_enable(bank_sel == i)
            )

        self.seq.If(raw_valid, counter == 1)(
            last(1)
        )

        # de-assert
        self.seq.Delay(1)(
            last(0)
        )

        for write_enable in write_enable_list:
            self.seq.Delay(1)(
                write_enable(0)
            )

        done = last

        return done

    def write_dataflow_pattern_interleave(self, port, addr, data, pattern,
                                          cond=None, when=None):
        """ 
        @return done
        'data' and 'when' must be dataflow variables
        """

        if self.seq is None:
            self.seq = Seq(self.m, self.name, self.clk, self.rst)

        for ram in self.rams:
            if ram._write_disabled[port]:
                raise TypeError('Write disabled.')

        if not isinstance(pattern, (tuple, list)):
            raise TypeError('pattern must be list or tuple.')

        if not pattern:
            raise ValueError(
                'pattern must have one (size, stride) pair at least.')

        if not isinstance(pattern[0], (tuple, list)):
            pattern = (pattern,)

        last = self.m.TmpReg(initval=0)

        running = self.m.TmpReg(initval=0)

        ext_cond = dtypes.make_condition(cond)
        data_cond = dtypes.make_condition(running, vtypes.Not(last))

        if when is None or not isinstance(when, dtypes._Numeric):
            raw_data, raw_valid = data.read(cond=data_cond)
        else:
            data_list, raw_valid = dtypes.read_multi(
                self.m, data, when, cond=data_cond)
            raw_data = data_list[0]
            when = data_list[1]

        when_cond = dtypes.make_condition(when, ready=data_cond)
        if when_cond is not None:
            raw_valid = vtypes.Ands(when_cond, raw_valid)

        offset_addr = self.m.TmpWire(self.addrwidth)
        offsets = [self.m.TmpReg(self.addrwidth, initval=0) for _ in pattern]

        offset_addr_value = addr
        for offset in offsets:
            offset_addr_value = offset + offset_addr_value
        offset_addr.assign(offset_addr_value)

        log_numbanks = util.log2(self.numbanks)
        ram_addr_list = [self.m.TmpWire(ram.addrwidth) for ram in self.rams]
        for ram_addr in ram_addr_list:
            ram_addr.assign(offset_addr >> log_numbanks)

        bank_sel = self.m.TmpWire(log_numbanks)
        bank_sel.assign(offset_addr)

        count_list = [self.m.TmpReg(vtypes.get_width(out_size), initval=0)
                      for (out_size, out_stride) in pattern]

        write_addr_list = [self.m.TmpRegLike(ram.interfaces[port].addr, initval=0)
                           for ram in self.rams]
        write_data_list = [self.m.TmpRegLike(ram.interfaces[port].wdata, initval=0)
                           for ram in self.rams]
        write_enable_list = [self.m.TmpRegLike(ram.interfaces[port].enable, initval=0)
                             for ram in self.rams]

        for ram, write_addr, write_data, write_enable in zip(self.rams, write_addr_list,
                                                             write_data_list, write_enable_list):
            util.add_mux(ram.interfaces[port].addr, write_enable, write_addr)
            util.add_mux(ram.interfaces[port].wdata, write_enable, write_data)
            util.add_enable_cond(ram.interfaces[port].wenable, write_enable, vtypes.Int(1, 1))
            util.add_enable_cond(ram.interfaces[port].enable, write_enable, vtypes.Int(1, 1))

        self.seq.If(ext_cond, vtypes.Not(running))(
            running(1)
        )

        for i, (write_addr, write_data,
                write_enable, ram_addr) in enumerate(zip(write_addr_list, write_data_list,
                                                         write_enable_list, ram_addr_list)):
            self.seq.If(raw_valid, running)(
                write_addr(ram_addr),
                write_data(raw_data),
                write_enable(bank_sel == i)
            )

        update_count = None
        last_one = None

        for offset, count, (out_size, out_stride) in zip(offsets, count_list, pattern):
            self.seq.If(ext_cond, vtypes.Not(running))(
                count(out_size - 1),
                offset(0)
            )
            self.seq.If(raw_valid, running, update_count)(
                count.dec(),
                offset(offset + out_stride)
            )
            self.seq.If(raw_valid, running, update_count, count == 0)(
                count(out_size - 1),
                offset(0)
            )

            if update_count is None:
                update_count = count == 0
            else:
                update_count = vtypes.Ands(update_count, count == 0)

            if last_one is None:
                last_one = count == 0
            else:
                last_one = vtypes.Ands(last_one, count == 0)

        self.seq.If(raw_valid, last_one)(
            running(0),
            last(1)
        )

        # de-assert
        self.seq.Delay(1)(
            last(0)
        )

        for write_enable in write_enable_list:
            self.seq.Delay(1)(
                write_enable(0)
            )

        done = last

        return done

    def write_dataflow_multidim_interleave(self, port, addr, data, shape, order=None,
                                           cond=None, when=None):
        """ 
        @return done
        'data' and 'when' must be dataflow variables
        """
        if order is None:
            order = list(reversed(range(len(shape))))

        pattern = self._to_pattern(shape, order)
        return self.write_dataflow_pattern_interleave(port, addr, data, pattern,
                                                      cond=cond, when=when)

    def write_dataflow_bcast(self, port, addr, data, length=1,
                             stride=1, cond=None, when=None):
        """ 
        @return done
        """

        done_list = []
        for ram in self.rams:
            done = ram.write_dataflow(
                port, addr, data, length, stride, cond, when)
            done_list.append(done)

        merged_done = done_list[0]
        return merged_done

    def write_dataflow_pattern_bcast(self, port, addr, data, pattern,
                                     cond=None, when=None):
        """ 
        @return done
        'data' and 'when' must be dataflow variables
        """

        done_list = []
        for ram in self.rams:
            done = ram.write_dataflow_pattern(
                port, addr, data, pattern, cond, when)
            done_list.append(done)

        merged_done = done_list[0]
        return merged_done

    def write_dataflow_multidim_bcast(self, port, addr, data, shape, order=None,
                                      cond=None, when=None):
        """ 
        @return done
        'data' and 'when' must be dataflow variables
        """
        if order is None:
            order = list(reversed(range(len(shape))))

        pattern = self._to_pattern(shape, order)
        return self.write_dataflow_pattern_bcast(port, addr, data, pattern,
                                                 cond=cond, when=when)

    def write_dataflow_block(self, port, addr, data, length=1, block_size=1,
                             stride=1, cond=None, when=None):
        """ 
        @return done
        'data' and 'when' must be dataflow variables
        """

        if self.keep_hierarchy and isinstance(self.rams[0], MultibankRAM):
            return self._write_dataflow_block_nested(port, addr, data, length, block_size,
                                                     stride, cond, when)

        if self.seq is None:
            self.seq = Seq(self.m, self.name, self.clk, self.rst)

        for ram in self.rams:
            if ram._write_disabled[port]:
                raise TypeError('Write disabled.')

        block_counter = self.m.TmpReg(vtypes.get_width(block_size), initval=0)
        counter = self.m.TmpReg(vtypes.get_width(length), initval=0)
        last = self.m.TmpReg(initval=0)

        ext_cond = dtypes.make_condition(cond)
        data_cond = dtypes.make_condition(counter > 0, vtypes.Not(last))

        if when is None or not isinstance(when, dtypes._Numeric):
            raw_data, raw_valid = data.read(cond=data_cond)
        else:
            data_list, raw_valid = dtypes.read_multi(
                self.m, data, when, cond=data_cond)
            raw_data = data_list[0]
            when = data_list[1]

        when_cond = dtypes.make_condition(when, ready=data_cond)
        if when_cond is not None:
            raw_valid = vtypes.Ands(when_cond, raw_valid)

        log_numbanks = util.log2(self.numbanks)

        reg_addr_list = [self.m.TmpReg(self.addrwidth, initval=0)
                         for ram in self.rams]

        next_addr_list = [self.m.TmpWire(self.addrwidth)
                          for ram in self.rams]
        for next_addr, reg_addr in zip(next_addr_list, reg_addr_list):
            next_addr.assign(reg_addr + stride)

        ram_addr_list = [self.m.TmpWire(ram.addrwidth)
                         for ram in self.rams]
        for ram_addr, next_addr in zip(ram_addr_list, next_addr_list):
            ram_addr.assign(next_addr)

        bank_sel = self.m.TmpReg(log_numbanks, initval=0)

        write_addr_list = [self.m.TmpRegLike(ram.interfaces[port].addr, initval=0)
                           for ram in self.rams]
        write_data_list = [self.m.TmpRegLike(ram.interfaces[port].wdata, initval=0)
                           for ram in self.rams]
        write_enable_list = [self.m.TmpRegLike(ram.interfaces[port].enable, initval=0)
                             for ram in self.rams]

        for ram, write_addr, write_data, write_enable in zip(self.rams, write_addr_list,
                                                             write_data_list, write_enable_list):
            util.add_mux(ram.interfaces[port].addr, write_enable, write_addr)
            util.add_mux(ram.interfaces[port].wdata, write_enable, write_data)
            util.add_enable_cond(ram.interfaces[port].wenable, write_enable, vtypes.Int(1, 1))
            util.add_enable_cond(ram.interfaces[port].enable, write_enable, vtypes.Int(1, 1))

        self.seq.If(ext_cond, counter == 0)(
            bank_sel(0),
            block_counter(block_size - 1),
            counter(length),
        )

        for reg_addr in reg_addr_list:
            self.seq.If(ext_cond, counter == 0)(
                reg_addr(addr - stride)
            )

        self.seq.If(raw_valid, counter > 0)(
            block_counter.dec(),
            counter.dec()
        )

        self.seq.If(raw_valid, counter > 0, block_counter == 0)(
            block_counter(block_size - 1),
            bank_sel.inc()
        )

        self.seq.If(raw_valid, counter > 0, block_counter == 0,
                    bank_sel == self.numbanks - 1)(
            bank_sel(0)
        )

        for i, (reg_addr, next_addr) in enumerate(zip(reg_addr_list, next_addr_list)):
            self.seq.If(raw_valid, counter > 0, bank_sel == i)(
                reg_addr(next_addr)
            )

        for i, (write_addr, write_data,
                write_enable, ram_addr) in enumerate(zip(write_addr_list, write_data_list,
                                                         write_enable_list, ram_addr_list)):
            self.seq.If(raw_valid, counter > 0)(
                write_addr(ram_addr),
                write_data(raw_data),
                write_enable(bank_sel == i)
            )

        self.seq.If(raw_valid, counter == 1)(
            last(1)
        )

        # de-assert
        self.seq.Delay(1)(
            last(0)
        )

        for write_enable in write_enable_list:
            self.seq.Delay(1)(
                write_enable(0)
            )

        done = last

        return done

    def _write_dataflow_block_nested(self, port, addr, data, length=1, block_size=1,
                                     stride=1, cond=None, when=None):
        """ 
        @return done
        'data' and 'when' must be dataflow variables
        """

        len_rams = 0
        for ram in self.rams:
            if not isinstance(ram, MultibankRAM):
                raise TypeError('All sub-bank RAMs must be MultibankRAM.')
            if len_rams == 0:
                len_rams = len(ram.rams)
            elif len_rams != len(ram.rams):
                raise ValueError(
                    'All sub-bank RAMs must have the same number of RAMs.')

        rams = [[] for i in range(len_rams)]

        for ram in self.rams:
            for i, sub in enumerate(ram.rams):
                rams[i].append(sub)

        rams = [to_multibank_ram(ram_list, keep_hierarchy=True)
                for ram_list in rams]

        done_list = []
        lsb = 0
        msb = 0
        for ram in rams:
            msb = msb + ram.orig_datawidth
            bank_data = dtypes.Slice(data, msb - 1, lsb)
            done = ram.write_dataflow_block(
                port, addr, bank_data, length, block_size, stride, cond, when)
            done_list.append(done)
            lsb = msb

        merged_done = done_list[0]
        return merged_done


class _PackedMultibankRAM(MultibankRAM):
    def __init__(self, src=None, name=None, keep_hierarchy=False):

        if not isinstance(src, (tuple, list)):
            src = [src]

        if not keep_hierarchy:
            src = extract_rams(src)

        if len(src) < 2:
            raise ValueError('numbanks must be 2 or more')

        max_datawidth = 0
        for ram in src:
            max_datawidth = max(max_datawidth, ram.datawidth)

        max_addrwidth = 0
        for ram in src:
            max_addrwidth = max(max_addrwidth, ram.addrwidth)

        max_numports = src[0].numports
        for ram in src[1:]:
            if max_numports != ram.numports:
                raise ValueError('numports must be same')

        self.m = src[0].m
        self.name = ('_'.join([ram.name for ram in src])
                     if name is None else name)
        self.clk = src[0].clk
        self.rst = src[0].rst
        self.orig_datawidth = max_datawidth
        self.datawidth = max_datawidth * len(src)
        self.addrwidth = max_addrwidth
        self.numports = max_numports
        self.numbanks = len(src)
        self.shift = util.log2(self.numbanks)
        self.rams = src
        self.keep_hierarchy = keep_hierarchy
        self.seq = None

        for ram in self.rams:
            if ram.seq is not None:
                self.seq = ram.seq
                break

        self.df = DataflowManager(self.m, self.clk, self.rst)

        # key: (axi._id(), port, ram_method_name)
        self.cache_dma_reqs = {}

        self.mutex = None


multibank_ram_cache = {}


def to_multibank_ram(rams, name=None, keep_hierarchy=False):
    ids = tuple([ram._id() for ram in rams])

    if ids in multibank_ram_cache:
        return multibank_ram_cache[ids]

    ram = _PackedMultibankRAM(rams, name, keep_hierarchy)
    multibank_ram_cache[ids] = ram

    return ram
