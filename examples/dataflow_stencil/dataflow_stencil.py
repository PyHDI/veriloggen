from __future__ import absolute_import
from __future__ import print_function
import sys
import os
import math
from functools import reduce

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from veriloggen import *
import veriloggen.dataflow as dataflow
import veriloggen.types.ram as ram
import veriloggen.types.fixed as fixed

def stencil(coe, data):
    data = map(lambda x,y: x*y, data, coe)
    rslt = reduce(lambda x,y: x+y, data)
    return rslt
    
def mkStencilPipeline2D(coe=None, size=3, width=32, point=16):
    # size-port stream inputs
    iports = [ dataflow.Variable('idata%d'%i, valid='ivalid%d'%i,
                                 width=width, point=point, signed=True)
               for i in range(size) ]

    if coe is None:
        coe = [ [ dataflow.Constant(1.0/(1.0*size*size), point=point) for i in range(size) ]
                for j in range(size) ]
        
    # source data
    data = [ [ d.prev(j) for j in range(size) ] for d in iports ]
    
    # from 2D list to 1D list
    data_list = []
    coe_list = []
    for d, c in zip(data, coe):
        data_list.extend(d)
        coe_list.extend(c)

    # computation by calling standard method
    rslt = stencil(coe_list, data_list)
    
    rslt.output('odata', valid='ovalid')
    
    df = dataflow.Dataflow(rslt)
    m = df.to_module('stencil_pipeline_2d')

    #try:
    #    df.draw_graph()
    #except:
    #    print('Dataflow graph could not be generated.', file=sys.stderr)

    return m

def mkStencil(n=16, size=3, datawidth=32, point=16, coe_test=False):
    m = Module('stencil')

    addrwidth = int(math.log(n, 2))

    clk = m.Input('CLK')
    rst = m.Input('RST')

    start = m.Input('start')
    busy = m.OutputReg('busy', initval=0)
    
    done = m.TmpReg(initval=0)

    # external RAM I/F
    ext_src_rams = [ ram.RAMSlaveInterface(m, 'ext_src_ram%d' % i,
                                              datawidth=datawidth, addrwidth=addrwidth)
                      for i in range(size) ]
    ext_dst_ram = ram.RAMSlaveInterface(m, 'ext_dst_ram',
                                           datawidth=datawidth, addrwidth=addrwidth)
    
    # RAM
    addrwidth = int(math.log(n, 2)) * 2
    
    src_rams = [ ram.SyncRAMManager(m, 'src_ram%d' % i, clk, rst,
                                    datawidth=datawidth, addrwidth=addrwidth, numports=2)
                  for i in range(size) ]
                            
    dst_ram = ram.SyncRAMManager(m, 'dst_ram', clk, rst,
                                 datawidth=datawidth, addrwidth=addrwidth, numports=2)

    # connect RAM I/Fs
    for src_ram, ext_src_ram in zip(src_rams, ext_src_rams):
        src_ram[1].connect(ext_src_ram)

    dst_ram[1].connect(ext_dst_ram)

    # read FSM
    read_fsm = FSM(m, 'read_fsm', clk, rst)
    read_count = m.Reg('read_count', 32, initval=0)
    read_addr = m.Reg('read_addr', 32, initval=0)


    read_fsm(
        read_addr(0),
        read_count(0),
        busy(0)
    )

    read_fsm.If(start)(
        busy(1)
    )

    read_fsm.Then().goto_next()

    read_fsm(
        read_addr.inc(),
        read_count.inc()
    )
        
    idata = []
    ivalid = []
    for i, src_ram in enumerate(src_rams):
        src_ram.disable_write(0)
        rdata, rvalid = src_ram.read(0, read_addr, read_fsm)
        idata.append(rdata)
        ivalid.append(rvalid)

    read_fsm.If(read_count == n - 1)(
        read_addr(0),
        read_count(0)
    )

    read_fsm.Then().goto_next()

    read_fsm.If(done)(
        busy(0)
    )

    read_fsm.Then().goto_init()

    read_fsm.make_always()


    # instance
    odata = m.Wire('odata', datawidth)
    ovalid = m.Wire('ovalid')
    
    ports = []
    ports.append( ('CLK', clk) )
    ports.append( ('RST', rst) )    
    
    for i, (d, v) in enumerate(zip(idata, ivalid)):
        ports.append( ('idata%d' % i, d) )
        ports.append( ('ivalid%d' % i, v) )

    ports.append( ('odata', odata) )
    ports.append( ('ovalid', ovalid) )

    coe = None
    if coe_test:
        coe = [ [ dataflow.Constant(1, point=point) for i in range(size) ]
                for j in range(size) ]
        point = 0
        
    st = mkStencilPipeline2D(size=3, width=datawidth, point=point, coe=coe)
    m.Instance(st, 'inst_stencil', ports=ports)

    skip_offset = int(math.floor(size/2))
    
    # write FSM
    write_fsm = FSM(m, 'write_fsm', clk, rst)
    write_count = m.Reg('write_count', 32, initval=0)
    write_addr = m.Reg('write_addr', 32, initval=skip_offset)

    write_fsm(
        done(0)
    )
    
    write_fsm.If(Ands(ovalid, write_count > skip_offset))(
        write_addr.inc()
    )
    
    dst_ram.write(0, write_addr, odata, write_fsm.then)
    
    write_fsm.If(ovalid)(
        write_count.inc(),
    )
    
    write_fsm.If(write_count == n)(
        write_count(0),
        write_addr(skip_offset),
        done(1)
    )
    write_fsm.Then().goto_init()

    write_fsm.make_always()

    return m

def mkTest(n=16, size=3, datawidth=32, point=16, coe_test=False):
    if coe_test:
        point = 0
    
    m = Module('test')

    addrwidth = int(math.log(n, 2))

    main = mkStencil(n, size, datawidth, point, coe_test)

    params = m.copy_params(main)
    ports = m.copy_sim_ports(main)
    
    clk = ports['CLK']
    rst = ports['RST']

    start = ports['start']
    busy = ports['busy']
    
    uut = m.Instance(main, 'uut',
                     params=m.connect_params(main),
                     ports=m.connect_ports(main))

    reset_done = m.Reg('reset_done', initval=0)
    reset_stmt = []
    reset_stmt.append( reset_done(0) )
    reset_stmt.append( start(0) )

    
    # src RAM
    for i in range(3):
        addr = ports['ext_src_ram%d_addr' % i]
        rdata = ports['ext_src_ram%d_rdata' % i]
        wdata = ports['ext_src_ram%d_wdata' % i]
        wenable = ports['ext_src_ram%d_wenable' % i]
        reset_stmt.append(addr(0))
        reset_stmt.append(wdata(0))
        reset_stmt.append(wenable(0))

    # dst RAM
    addr = ports['ext_dst_ram_addr']
    rdata = ports['ext_dst_ram_rdata']
    wdata = ports['ext_dst_ram_wdata']
    wenable = ports['ext_dst_ram_wenable']
    reset_stmt.append(addr(2))
    reset_stmt.append(wdata(0))
    reset_stmt.append(wenable(0))
    

    simulation.setup_waveform(m, uut)
    simulation.setup_clock(m, clk, hperiod=5)
    init = simulation.setup_reset(m, rst, reset_stmt, period=100)

    nclk = simulation.next_clock

    init.add(
        Delay(1000),
        reset_done(1),
        nclk(clk),
        Delay(100000),
        Systask('finish'),
    )

    fsm = FSM(m, 'fsm', clk, rst)
    
    fsm.goto_next(cond=reset_done)

    for i in range(3):
        addr = ports['ext_src_ram%d_addr' % i]
        fsm.add( addr(-1) )

    fsm.goto_next()

    for i in range(3):
        addr = ports['ext_src_ram%d_addr' % i]
        rdata = ports['ext_src_ram%d_rdata' % i]
        wdata = ports['ext_src_ram%d_wdata' % i]
        wenable = ports['ext_src_ram%d_wenable' % i]
        next_addr = (addr+1) % (n*n)
        fsm.add( addr.inc() )
        fsm.add( wdata(fixed.FixedConst(90, point)) )
        fsm.add( wenable(1) )
        fsm.add( wenable(0), cond=AndList(wenable, addr==2**addrwidth-1) )

    fsm.goto_next(cond=AndList(wenable, ports['ext_src_ram0_addr']==2**addrwidth-1))
    
    fsm.goto_next(cond=Not(busy))
    
    fsm.add( start(1) )
    fsm.add( start(0), delay=1 )
    fsm.goto_next()
    
    fsm.goto_next(cond=busy)

    fsm.goto_next(cond=Not(busy))

    fsm.add( Systask('finish') )

    fsm.make_always()

    return m

if __name__ == '__main__':
    n = 16
    #test = mkTest(n, coe_test=True)
    test = mkTest(n)
    verilog = test.to_verilog('tmp.v')
    #print(verilog)

    # run simulator (Icarus Verilog)
    sim = simulation.Simulator(test)
    rslt = sim.run()
    print(rslt)
