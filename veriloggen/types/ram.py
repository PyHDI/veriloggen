from __future__ import absolute_import
from __future__ import print_function

import functools

import veriloggen.core.vtypes as vtypes
from veriloggen.core.module import Module
from veriloggen.seq.seq import Seq
from veriloggen.fsm.fsm import TmpFSM
from veriloggen.dataflow.dataflow import DataflowManager
from veriloggen.dataflow.dtypes import make_condition, read_multi
from veriloggen.dataflow.dtypes import _Numeric as df_numeric
from . import util


class RAMInterface(object):
    _I = 'Reg'
    _O = 'Wire'

    def __init__(self, m, name=None, datawidth=32, addrwidth=10,
                 itype=None, otype=None,
                 p_addr='addr', p_rdata='rdata',
                 p_wdata='wdata', p_wenable='wenable',
                 p_enable='enable',
                 with_enable=False, index=None):

        if itype is None:
            itype = self._I
        if otype is None:
            otype = self._O

        self.m = m

        name_addr = p_addr if name is None else '_'.join([name, p_addr])
        name_rdata = p_rdata if name is None else '_'.join([name, p_rdata])
        name_wdata = p_wdata if name is None else '_'.join([name, p_wdata])
        name_wenable = (
            p_wenable if name is None else '_'.join([name, p_wenable]))
        if with_enable:
            name_enable = (
                p_enable if name is None else '_'.join([name, p_enable]))

        if index is not None:
            name_addr = name_addr + str(index)
            name_rdata = name_rdata + str(index)
            name_wdata = name_wdata + str(index)
            name_wenable = name_wenable + str(index)
            if with_enable:
                name_enable = name_enable + str(index)

        self.addr = util.make_port(m, itype, name_addr, addrwidth, initval=0)
        self.rdata = util.make_port(m, otype, name_rdata, datawidth, initval=0)
        self.wdata = util.make_port(m, itype, name_wdata, datawidth, initval=0)
        self.wenable = util.make_port(m, itype, name_wenable, initval=0)
        if with_enable:
            self.enable = util.make_port(m, itype, name_enable, initval=0)

    def connect(self, targ):
        self.addr.connect(targ.addr)
        targ.rdata.connect(self.rdata)
        self.wdata.connect(targ.wdata)
        self.wenable.connect(targ.wenable)
        if hasattr(self, 'enable'):
            if hasattr(targ, 'enable'):
                self.enable.connect(targ.enable)
            else:
                self.enable.connect(1)
        else:
            if hasattr(targ, 'enable'):
                raise ValueError('no enable port')


class RAMSlaveInterface(RAMInterface):
    _I = 'Input'
    _O = 'Output'


class RAMMasterInterface(RAMInterface):
    _I = 'Output'
    _O = 'Input'


def mkRAMDefinition(name, datawidth=32, addrwidth=10, numports=2, sync=True, with_enable=False):
    m = Module(name)
    clk = m.Input('CLK')

    interfaces = []

    for i in range(numports):
        interface = RAMSlaveInterface(
            m, name + '_%d' % i, datawidth, addrwidth, with_enable=with_enable)
        if sync:
            interface.delay_addr = m.Reg(name + '_%d_daddr' % i, addrwidth)

        interfaces.append(interface)

    mem = m.Reg('mem', datawidth, length=2**addrwidth)

    for interface in interfaces:
        body = [
            vtypes.If(interface.wenable)(
                mem[interface.addr](interface.wdata)
            )]

        if sync:
            body.append(interface.delay_addr(interface.addr))

        if with_enable:
            body = vtypes.If(interface.enable)(*body)

        m.Always(vtypes.Posedge(clk))(
            body
        )

        if sync:
            m.Assign(interface.rdata(mem[interface.delay_addr]))
        else:
            m.Assign(interface.rdata(mem[interface.addr]))

    return m


class _RAM(object):

    def __init__(self, m, name, clk,
                 datawidth=32, addrwidth=10, numports=1, sync=True, with_enable=False):

        self.m = m
        self.name = name
        self.clk = clk
        self.with_enable = with_enable

        self.interfaces = [RAMInterface(m, name + '_%d' % i, datawidth, addrwidth,
                                        itype='Wire', otype='Wire', with_enable=with_enable)
                           for i in range(numports)]

        ram_def = mkRAMDefinition(
            name, datawidth, addrwidth, numports, sync, with_enable)

        self.m.Instance(ram_def, name,
                        params=(), ports=m.connect_ports(ram_def))

    def connect(self, port, addr, wdata, wenable, enable=None):
        self.m.Assign(self.interfaces[port].addr(addr))
        self.m.Assign(self.interfaces[port].wdata(wdata))
        self.m.Assign(self.interfaces[port].wenable(wenable))
        if self.with_enable:
            self.m.Assign(self.interfaces[port].enable(enable))

    def rdata(self, port):
        return self.interfaces[port].rdata


class SyncRAM(_RAM):

    def __init__(self, m, name, clk,
                 datawidth=32, addrwidth=10, numports=1, with_enable=False):
        _RAM.__init__(self, m, name, clk,
                      datawidth, addrwidth, numports, sync=True, with_enable=with_enable)


class AsyncRAM(_RAM):

    def __init__(self, m, name, clk,
                 datawidth=32, addrwidth=10, numports=1, with_enable=False):
        _RAM.__init__(self, m, name, clk,
                      datawidth, addrwidth, numports, sync=False)


#-------------------------------------------------------------------------
class SyncRAMManager(object):

    def __init__(self, m, name, clk, rst,
                 datawidth=32, addrwidth=10, numports=1,
                 nodataflow=False):

        self.m = m
        self.name = name
        self.clk = clk
        self.rst = rst
        self.datawidth = datawidth
        self.addrwidth = addrwidth
        self.numports = numports

        self.interfaces = [RAMInterface(m, name + '_%d' % i, datawidth, addrwidth)
                           for i in range(numports)]

        self.definition = mkRAMDefinition(name, datawidth, addrwidth, numports)

        self.inst = self.m.Instance(self.definition, 'inst_' + name,
                                    ports=m.connect_ports(self.definition))

        self.seq = Seq(m, name, clk, rst)

        if nodataflow:
            self.df = None
        else:
            self.df = DataflowManager(self.m, self.clk, self.rst)

        self._write_disabled = [False for i in range(numports)]
        self._port_disabled = [False for i in range(numports)]

    def __getitem__(self, index):
        return self.interfaces[index]

    def disable_write(self, port):
        self.seq(
            self.interfaces[port].wdata(0),
            self.interfaces[port].wenable(0)
        )
        self._write_disabled[port] = True

    def disable_port(self, port):
        self.seq(
            self.interfaces[port].addr(0),
        )
        self._port_disabled[port] = True

    def read(self, port, addr, cond=None):
        """ 
        @return data, valid
        """
        return self.read_data(port, addr, cond)

    def read_data(self, port, addr, cond=None):
        """ 
        @return data, valid
        """

        if cond is not None:
            self.seq.If(cond)

        self.seq(
            self.interfaces[port].addr(addr)
        )

        rdata = self.interfaces[port].rdata
        rvalid = self.m.TmpReg(initval=0)

        self.seq.Then().Delay(1)(
            rvalid(1)
        )

        self.seq.Then().Delay(2)(
            rvalid(0)
        )

        return rdata, rvalid

    def read_dataflow(self, port, addr, length=1,
                      stride=1, cond=None, point=0, signed=False):
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

        ext_cond = make_condition(cond)
        data_cond = make_condition(data_ack, last_ack)
        prev_data_cond = self.seq.Prev(data_cond, 1)

        data = self.m.TmpWireLike(self.interfaces[port].rdata)

        prev_data = self.seq.Prev(data, 1)
        data.assign(vtypes.Mux(prev_data_cond,
                               self.interfaces[port].rdata, prev_data))

        next_valid_on = self.m.TmpReg(initval=0)
        next_valid_off = self.m.TmpReg(initval=0)

        next_last = self.m.TmpReg(initval=0)
        last = self.m.TmpReg(initval=0)

        counter = self.m.TmpReg(length.bit_length() + 1, initval=0)

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
            self.interfaces[port].addr(addr),
            counter(length - 1),
            next_valid_on(1),
        )

        self.seq.If(data_cond, counter > 0)(
            self.interfaces[port].addr(self.interfaces[port].addr + stride),
            counter.dec(),
            next_valid_on(1),
            next_last(0)
        )

        self.seq.If(data_cond, counter == 1)(
            next_last(1)
        )

        df = self.df if self.df is not None else dataflow

        df_data = df.Variable(data, data_valid, data_ready,
                              width=self.datawidth, point=point, signed=signed)
        df_last = df.Variable(last, last_valid, last_ready, width=1)
        done = last

        return df_data, df_last, done

    def read_dataflow_pattern(self, port, addr, pattern,
                              cond=None, point=0, signed=False):
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

        ext_cond = make_condition(cond)
        data_cond = make_condition(data_ack, last_ack)
        prev_data_cond = self.seq.Prev(data_cond, 1)

        data = self.m.TmpWireLike(self.interfaces[port].rdata)

        prev_data = self.seq.Prev(data, 1)
        data.assign(vtypes.Mux(prev_data_cond,
                               self.interfaces[port].rdata, prev_data))

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

        count_list = [self.m.TmpReg(out_size.bit_length() + 1, initval=0)
                      for (out_size, out_stride) in pattern]

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
            self.interfaces[port].addr(addr),
            running(1),
            next_valid_on(1)
        )

        self.seq.If(data_cond, running)(
            self.interfaces[port].addr(next_addr),
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
                                    self.interfaces[port].addr + stride_value))

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

    def read_dataflow_multidim(self, port, addr, shape, order=None,
                               cond=None, point=0, signed=False):
        """ 
        @return data, last, done
        """

        if order is None:
            order = list(range(len(shape)))

        pattern = self._to_pattern(shape, order)
        return self.read_dataflow_pattern(port, addr, pattern,
                                          cond=cond, point=point, signed=signed)

    def write(self, port, addr, wdata, cond=None):
        """ 
        @return None
        """
        return self.write_data(port, addr, wdata, cond)

    def write_data(self, port, addr, wdata, cond=None):
        """ 
        @return None
        """

        if self._write_disabled[port]:
            raise TypeError('Write disabled.')

        if cond is not None:
            self.seq.If(cond)

        self.seq(
            self.interfaces[port].addr(addr),
            self.interfaces[port].wdata(wdata),
            self.interfaces[port].wenable(1)
        )

        self.seq.Then().Delay(1)(
            self.interfaces[port].wenable(0)
        )

    def write_dataflow(self, port, addr, data, length=1,
                       stride=1, cond=None, when=None):
        """ 
        @return done
        'data' and 'when' must be dataflow variables
        """

        if self._write_disabled[port]:
            raise TypeError('Write disabled.')

        counter = self.m.TmpReg(length.bit_length() + 1, initval=0)
        last = self.m.TmpReg(initval=0)

        ext_cond = make_condition(cond)
        data_cond = make_condition(counter > 0, vtypes.Not(last))

        if when is None or not isinstance(when, df_numeric):
            raw_data, raw_valid = data.read(cond=data_cond)
        else:
            data_list, raw_valid = read_multi(
                self.m, data, when, cond=data_cond)
            raw_data = data_list[0]
            when = data_list[1]

        when_cond = make_condition(when, ready=data_cond)
        if when_cond is not None:
            raw_valid = vtypes.Ands(when_cond, raw_valid)

        self.seq.If(ext_cond, counter == 0)(
            self.interfaces[port].addr(addr - stride),
            counter(length),
        )

        self.seq.If(raw_valid, counter > 0)(
            self.interfaces[port].addr(self.interfaces[port].addr + stride),
            self.interfaces[port].wdata(raw_data),
            self.interfaces[port].wenable(1),
            counter.dec()
        )

        self.seq.If(raw_valid, counter == 1)(
            last(1)
        )

        # de-assert
        self.seq.Delay(1)(
            self.interfaces[port].wenable(0),
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

        ext_cond = make_condition(cond)
        data_cond = make_condition(running, vtypes.Not(last))

        if when is None or not isinstance(when, df_numeric):
            raw_data, raw_valid = data.read(cond=data_cond)
        else:
            data_list, raw_valid = read_multi(
                self.m, data, when, cond=data_cond)
            raw_data = data_list[0]
            when = data_list[1]

        when_cond = make_condition(when, ready=data_cond)
        if when_cond is not None:
            raw_valid = vtypes.Ands(when_cond, raw_valid)

        offset_addr = self.m.TmpWire(self.addrwidth)
        offsets = [self.m.TmpReg(self.addrwidth, initval=0) for _ in pattern]

        offset_addr_value = addr
        for offset in offsets:
            offset_addr_value = offset + offset_addr_value
        offset_addr.assign(offset_addr_value)

        count_list = [self.m.TmpReg(out_size.bit_length() + 1, initval=0)
                      for (out_size, out_stride) in pattern]

        self.seq.If(ext_cond, vtypes.Not(running))(
            running(1)
        )

        self.seq.If(raw_valid, running)(
            self.interfaces[port].addr(offset_addr),
            self.interfaces[port].wdata(raw_data),
            self.interfaces[port].wenable(1)
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
            self.interfaces[port].wenable(0),
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
            order = list(range(len(shape)))

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
                                      shape[:p], basevalue) if p > 0 else basevalue
            pattern.append((size, stride))
        return pattern
