from __future__ import absolute_import
from __future__ import print_function

import veriloggen.core.vtypes as vtypes
import veriloggen.core.module as module
import veriloggen.types.bram as bram
from veriloggen.seq.seq import Seq


def CoramMemoryInterface(m, name=None, datawidth=32, addrwidth=10,
                         p_addr='ADDR', p_rdata='Q', p_wdata='D', p_wenable='WE',
                         index=None):

    return bram.BramInterface(
        m, name=name, datawidth=datawidth, addrwidth=addrwidth,
        p_addr=p_addr, p_rdata=p_rdata, p_wdata=p_wdata, p_wenable=p_wenable, index=index)


def CoramMemorySlaveInterface(m, name=None, datawidth=32, addrwidth=10,
                              p_addr='ADDR', p_rdata='Q', p_wdata='D', p_wenable='WE',
                              index=None):

    return bram.BramSlaveInterface(
        m, name=name, datawidth=datawidth, addrwidth=addrwidth,
        p_addr=p_addr, p_rdata=p_rdata, p_wdata=p_wdata, p_wenable=p_wenable, index=index)


def CoramMemoryMasterInterface(m, name=None, datawidth=32, addrwidth=10,
                               p_addr='ADDR', p_rdata='Q', p_wdata='D', p_wenable='WE',
                               index=None):

    return bram.BramMasterInterface(
        m, name=name, datawidth=datawidth, addrwidth=addrwidth,
        p_addr=p_addr, p_rdata=p_rdata, p_wdata=p_wdata, p_wenable=p_wenable, index=index)


def mkCoramMemoryDefinition(numports):
    name = 'CoramMemory%dP' % numports
    m = module.Module(name)

    coram_thread_name = m.Parameter('CORAM_THREAD_NAME', 'none')
    coram_id = m.Parameter('CORAM_ID', 0)
    coram_sub_id = m.Parameter('CORAM_SUB_ID', 0)
    coram_addr_len = m.Parameter('CORAM_ADDR_LEN', 10)
    coram_data_width = m.Parameter('CORAM_DATA_WIDTH', 32)

    clk = m.Input('CLK')

    interfaces = []

    for i in range(numports):
        index = i if numports > 1 else None
        interface = CoramMemorySlaveInterface(m, datawidth=coram_data_width,
                                              addrwidth=coram_addr_len, index=index)
        delay_addr_name = 'D_ADDR%d' % i if numports > 1 else 'D_ADDR'
        interface.delay_addr = m.Reg(delay_addr_name, coram_addr_len)
        interfaces.append(interface)

    mem = m.Reg('mem', coram_data_width, length=vtypes.Int(2)**coram_addr_len)

    for interface in interfaces:
        m.Always(vtypes.Posedge(clk))(
            vtypes.If(interface.wenable)(
                mem[interface.addr](interface.wdata)
            ),
            interface.delay_addr(interface.addr)
        )
        m.Assign(interface.rdata(mem[interface.delay_addr]))

    return m


#-------------------------------------------------------------------------
coram_memroy_definitions = {}
def get_coram_memory_definition(numports):
    if numports in coram_memroy_definitions:
        return coram_memroy_definitions[numports]
    coram_memroy_definitions[numports] = mkCoramMemoryDefinition(numports)
    return coram_memroy_definitions[numports]


#-------------------------------------------------------------------------
class CoramMemory(bram.Bram):

    def __init__(self, m, clk, rst,
                 thread_name, id, sub_id=None, datawidth=32, addrwidth=10, numports=1):

        self.m = m
        self.clk = clk
        self.rst = rst
        self.thread_name = thread_name
        self.id = id
        self.sub_id = sub_id
        self.name = '_'.join([thread_name, 'memory', str(id)])
        self.datawidth = datawidth
        self.addrwidth = addrwidth

        self.interfaces = []
        for i in range(numports):
            index = i if numports > 1 else None
            obj = CoramMemoryInterface(m, name=self.name,
                                       datawidth=datawidth, addrwidth=addrwidth, index=index)
            self.interfaces.append(obj)

        self.definition = get_coram_memory_definition(numports)

        params = []
        params.append(('CORAM_THREAD_NAME', self.thread_name))
        params.append(('CORAM_ID', self.id))
        if self.sub_id is not None:
            params.append(('CORAM_SUB_ID', self.sub_id))
        params.append(('CORAM_ADDR_LEN', self.addrwidth))
        params.append(('CORAM_DATA_WIDTH', self.datawidth))

        ports = []
        ports.append(('CLK', self.clk))
        ports.extend(m.connect_ports(self.definition, prefix=self.name + '_'))

        self.inst = self.m.Instance(
            self.definition, 'inst_' + self.name, params, ports)

        self.seq = Seq(m, self.name, clk, rst)
        #self.m.add_hook(self.seq.make_always)

        self._write_disabled = [False for i in range(numports)]
