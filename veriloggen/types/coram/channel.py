from __future__ import absolute_import
from __future__ import print_function

import veriloggen.core.vtypes as vtypes
import veriloggen.core.module as module
import veriloggen.types.fifo as fifo
from veriloggen.seq.seq import Seq


def CoramChannelWriteInterface(m, name=None, datawidth=32,
                               p_enq='ENQ', p_wdata='D',
                               p_full='FULL', p_almost_full='ALM_FULL'):
    return fifo.FifoWriteInterface(
        m, name=name, datawidth=datawidth,
        p_enq=p_enq, p_wdata=p_wdata, p_full=p_full, p_almost_full=p_almost_full)


def CoramChannelReadInterface(m, name=None, datawidth=32,
                              p_deq='DEQ', p_rdata='Q',
                              p_empty='EMPTY', p_almost_empty='ALM_EMPTY'):
    return fifo.FifoReadInterface(
        m, name=name, datawidth=datawidth,
        p_deq=p_deq, p_rdata=p_rdata, p_empty=p_empty, p_almost_empty=p_almost_empty)


def CoramChannelWriteMasterInterface(m, name=None, datawidth=32,
                                     p_enq='ENQ', p_wdata='D',
                                     p_full='FULL', p_almost_full='ALM_FULL'):
    return fifo.FifoWriteMasterInterface(
        m, name=name, datawidth=datawidth,
        p_enq=p_enq, p_wdata=p_wdata, p_full=p_full, p_almost_full=p_almost_full)


def CoramChannelReadMasterInterface(m, name=None, datawidth=32,
                                    p_deq='DEQ', p_rdata='Q',
                                    p_empty='EMPTY', p_almost_empty='ALM_EMPTY'):
    return fifo.FifoReadMasterInterface(
        m, name=name, datawidth=datawidth,
        p_deq=p_deq, p_rdata=p_rdata, p_empty=p_empty, p_almost_empty=p_almost_empty)


def CoramChannelWriteSlaveInterface(m, name=None, datawidth=32,
                                    p_enq='ENQ', p_wdata='D',
                                    p_full='FULL', p_almost_full='ALM_FULL'):
    return fifo.FifoWriteSlaveInterface(
        m, name=name, datawidth=datawidth,
        p_enq=p_enq, p_wdata=p_wdata, p_full=p_full, p_almost_full=p_almost_full)


def CoramChannelReadSlaveInterface(m, name=None, datawidth=32,
                                   p_deq='DEQ', p_rdata='Q',
                                   p_empty='EMPTY', p_almost_empty='ALM_EMPTY'):
    return fifo.FifoReadSlaveInterface(
        m, name=name, datawidth=datawidth,
        p_deq=p_deq, p_rdata=p_rdata, p_empty=p_empty, p_almost_empty=p_almost_empty)


def mkCoramChannelDefinition():
    name = 'CoramChannel'
    m = module.Module(name)

    coram_thread_name = m.Parameter('CORAM_THREAD_NAME', 'none')
    coram_thread_id = m.Parameter('CORAM_THREAD_ID', 0)
    coram_id = m.Parameter('CORAM_ID', 0)
    coram_sub_id = m.Parameter('CORAM_SUB_ID', 0)
    coram_addr_len = m.Parameter('CORAM_ADDR_LEN', 10)
    coram_data_width = m.Parameter('CORAM_DATA_WIDTH', 32)

    clk = m.Input('CLK')
    rst = m.Input('RST')

    wif = CoramChannelWriteSlaveInterface(m, datawidth=coram_data_width)
    rif = CoramChannelReadSlaveInterface(m, datawidth=coram_data_width)

    wif.full.assign(0)
    wif.almost_full.assign(0)
    rif.rdata.assign(1)
    rif.empty.assign(0)
    rif.almost_empty.assign(0)

    return m


coram_channel_definition = None


def get_coram_channel_definition():
    global coram_channel_definition
    if coram_channel_definition is None:
        coram_channel_definition = mkCoramChannelDefinition()
    return coram_channel_definition


class CoramChannel(fifo.Fifo):

    def __init__(self, m, clk, rst,
                 thread_name, thread_id, id, sub_id=None,
                 datawidth=32, addrwidth=4):

        self.m = m
        self.clk = clk
        self.rst = rst
        self.thread_name = thread_name
        self.thread_id = thread_id
        self.id = id
        self.sub_id = sub_id
        self.name = '_'.join([thread_name, 'channel', str(id)])
        self.datawidth = datawidth
        self.addrwidth = addrwidth
        self.wif = CoramChannelWriteInterface(self.m, self.name, datawidth)
        self.rif = CoramChannelReadInterface(self.m, self.name, datawidth)
        self.definition = get_coram_channel_definition()

        params = []
        params.append(('CORAM_THREAD_NAME', self.thread_name))
        params.append(('CORAM_THREAD_ID', self.thread_id))
        params.append(('CORAM_ID', self.id))
        if self.sub_id is not None:
            params.append(('CORAM_SUB_ID', self.sub_id))
        params.append(('CORAM_ADDR_LEN', self.addrwidth))
        params.append(('CORAM_DATA_WIDTH', self.datawidth))

        ports = []
        ports.append(('CLK', self.clk))
        ports.append(('RST', self.rst))
        ports.extend(m.connect_ports(self.definition, prefix=self.name + '_'))

        self.inst = self.m.Instance(
            self.definition, 'inst_' + self.name, params, ports)

        self.seq = Seq(m, self.name, clk, rst)

        self._max_size = (2 ** self.addrwidth - 1 if isinstance(self.addrwidth, int) else
                          vtypes.Int(2) ** self.addrwidth - 1)

        self._count = 0

        self._enq_disabled = False
        self._deq_disabled = False
