from __future__ import absolute_import
from __future__ import print_function

from collections import OrderedDict
from tempfile import NamedTemporaryFile

import ipgen.ipgen

import veriloggen.core.vtypes as vtypes
import veriloggen.core.module as module
from . import axi


def to_ipcore(m, ipname=None, topname=None,
              clkname='CLK', rstname='RST', iftype='axi',
              simaddrwidth=20, simcode=None, simmemimg=None,
              silent=False):

    if topname is None:
        topname = '_'.join(['top', m.name])

    if ipname is None:
        ipname = '_'.join([m.name, 'ip'])

    top = generate_top(m, topname, clkname, rstname)
    verilog = top.to_verilog()

    run_ipgen(topname, ipname, verilog,
              iftype, simaddrwidth, simcode, simmemimg,
              silent)


def run_ipgen(topname, ipname, verilog,
              iftype='axi', simaddrwidth=20, simcode=None, simmemimg=None,
              silent=False):

    # memory image
    if simmemimg is None:
        size = 2 ** simaddrwidth
        wordsize = 4
        file_memimg = NamedTemporaryFile('w+')
        axi.AxiMemoryModel._make_img(file_memimg.name, size, wordsize)
        file_memimg.read()
        file_memimg_name = file_memimg.name
    else:
        file_memimg = None
        file_memimg_name = simmemimg

    # source code
    file_source = NamedTemporaryFile('w+')
    file_source.write(verilog)
    file_source.read()

    # usertest
    file_simcode = None
    if simcode is not None:
        file_simcode = NamedTemporaryFile('w+')
        file_simcode.write(simcode)
        file_simcode.read()

    # configuration
    topmodule = topname
    userlogic_filelist = [file_source.name]
    include = []
    define = []
    usertest = file_simcode.name if file_simcode is not None else None
    memimg = file_memimg_name
    skip_not_found = False
    ignore_protocol_error = False

    configs = {
        'signal_width': 32,
        'ext_addrwidth': 32,
        'ext_datawidth': 256,
        'single_clock': True,
        'if_type': iftype,
        'output': 'tmp.v',
        'sim_addrwidth': simaddrwidth,
        'hperiod_ulogic': 5,
        'hperiod_bus': 5,
    }

    builder = ipgen.ipgen.SystemBuilder()
    builder.build(configs,
                  topmodule,
                  ipname,
                  userlogic_filelist,

                  include=include,
                  define=define,
                  usertest=usertest,
                  memimg=memimg,

                  skip_not_found=skip_not_found,
                  ignore_protocol_error=ignore_protocol_error,
                  silent=silent)

    if file_memimg is not None:
        file_memimg.close()

    file_source.close()

    if file_simcode:
        file_simcode.close()


def generate_top(m, name, clkname='CLK', rstname='RST'):

    if not isinstance(m, module.Module):
        raise TypeError("'m' must be Module, not %s" % str(type(m)))

    masterbus = m.masterbus if hasattr(m, 'masterbus') else ()
    slavebus = m.slavebus if hasattr(m, 'slavebus') else ()

    include_names = [master.name for master in masterbus]
    include_names += [slave.name for slave in slavebus]

    top = module.Module(name)

    params = top.copy_params(m)
    ports = top.copy_ports(m, exclude=tuple(include_names))
    bus_ports = top.copy_sim_ports(
        m, include=tuple(include_names), use_wire=True)

    body = top.Instance(m, 'inst_' + m.name,
                        params=top.connect_params(m), ports=top.connect_ports(m))

    clk = ports[clkname]
    rst = ports[rstname]

    _id_count = 0

    for master in masterbus:
        port_list = OrderedDict([(k, v) for k, v in top.get_vars().items()
                                 if k.startswith(master.name)])
        name = master.name
        _id = _id_count
        _id_count += 1
        addr_width = port_list[master.name + '_awaddr'].width
        data_width = port_list[master.name + '_wdata'].width

        mod = ipgen_master_lite_memory() if master.lite else ipgen_master_memory()
        inst_params = (('NAME', name), ('ID', _id),
                       ('ADDR_WIDTH', addr_width), ('DATA_WIDTH', data_width))
        inst_ports = [('CLK', clk), ('RST', rst)]
        inst_ports += top.connect_ports(mod, prefix=name + '_')
        top.Instance(mod, 'inst_' + name, params=inst_params, ports=inst_ports)

    for slave in slavebus:
        port_list = OrderedDict([(k, v) for k, v in top.get_vars().items()
                                 if k.startswith(slave.name)])
        name = slave.name
        _id = _id_count
        _id_count += 1
        addr_width = port_list[slave.name + '_awaddr'].width
        data_width = port_list[slave.name + '_wdata'].width

        mod = ipgen_slave_lite_memory() if slave.lite else ipgen_slave_memory()
        inst_params = (('NAME', name), ('ID', _id),
                       ('ADDR_WIDTH', addr_width), ('DATA_WIDTH', data_width))
        inst_ports = [('CLK', clk), ('RST', rst)]
        inst_ports += top.connect_ports(mod, prefix=name + '_')
        top.Instance(mod, 'inst_' + name, params=inst_params, ports=inst_ports)

    return top


def mk_ipgen_master_memory():
    m = module.Module('ipgen_master_memory')

    name = m.Parameter('NAME', 'undefined')
    _id = m.Parameter('ID', 0)
    addr_width = m.Parameter('ADDR_WIDTH', 32)
    data_width = m.Parameter('DATA_WIDTH', 32)

    clk = m.Input('CLK')
    rst = m.Input('RST')

    awvalid = m.Input('awvalid')
    awaddr = m.Input('awaddr', addr_width)
    awlen = m.Input('awlen', 8)
    awready = m.Output('awready')

    wdata = m.Input('wdata', data_width)
    wstrb = m.Input('wstrb', data_width / 8)
    wlast = m.Input('wlast')
    wvalid = m.Input('wvalid')
    wready = m.Output('wready')

    arvalid = m.Input('arvalid')
    araddr = m.Input('araddr', addr_width)
    arlen = m.Input('arlen', 8)
    arready = m.Output('arready')

    rdata = m.Output('rdata', data_width)
    rlast = m.Output('rlast')
    rvalid = m.Output('rvalid')
    rready = m.Input('rready')

    return m


def mk_ipgen_slave_memory():
    m = module.Module('ipgen_slave_memory')

    name = m.Parameter('NAME', 'undefined')
    _id = m.Parameter('ID', 0)
    addr_width = m.Parameter('ADDR_WIDTH', 32)
    data_width = m.Parameter('DATA_WIDTH', 32)

    clk = m.Input('CLK')
    rst = m.Input('RST')

    awvalid = m.Output('awvalid')
    awaddr = m.Output('awaddr', addr_width)
    awlen = m.Output('awlen', 8)
    awready = m.Input('awready')

    wdata = m.Output('wdata', data_width)
    wstrb = m.Output('wstrb', data_width / 8)
    wlast = m.Output('wlast')
    wvalid = m.Output('wvalid')
    wready = m.Input('wready')

    arvalid = m.Output('arvalid')
    araddr = m.Output('araddr', addr_width)
    arlen = m.Output('arlen', 8)
    arready = m.Input('arready')

    rdata = m.Input('rdata', data_width)
    rlast = m.Input('rlast')
    rvalid = m.Input('rvalid')
    rready = m.Output('rready')

    return m


def mk_ipgen_master_lite_memory():
    m = module.Module('ipgen_master_lite_memory')

    name = m.Parameter('NAME', 'undefined')
    _id = m.Parameter('ID', 0)
    addr_width = m.Parameter('ADDR_WIDTH', 32)
    data_width = m.Parameter('DATA_WIDTH', 32)

    clk = m.Input('CLK')
    rst = m.Input('RST')

    awvalid = m.Input('awvalid')
    awaddr = m.Input('awaddr', addr_width)
    awready = m.Output('awready')

    wdata = m.Input('wdata', data_width)
    wstrb = m.Input('wstrb', data_width / 8)
    wvalid = m.Input('wvalid')
    wready = m.Output('wready')

    arvalid = m.Input('arvalid')
    araddr = m.Input('araddr', addr_width)
    arready = m.Output('arready')

    rdata = m.Output('rdata', data_width)
    rvalid = m.Output('rvalid')
    rready = m.Input('rready')

    return m


def mk_ipgen_slave_lite_memory():
    m = module.Module('ipgen_slave_lite_memory')

    name = m.Parameter('NAME', 'undefined')
    _id = m.Parameter('ID', 0)
    addr_width = m.Parameter('ADDR_WIDTH', 32)
    data_width = m.Parameter('DATA_WIDTH', 32)

    clk = m.Input('CLK')
    rst = m.Input('RST')

    awvalid = m.Output('awvalid')
    awaddr = m.Output('awaddr', addr_width)
    awready = m.Input('awready')

    wdata = m.Output('wdata', data_width)
    wstrb = m.Output('wstrb', data_width / 8)
    wvalid = m.Output('wvalid')
    wready = m.Input('wready')

    arvalid = m.Output('arvalid')
    araddr = m.Output('araddr', addr_width)
    arready = m.Input('arready')

    rdata = m.Input('rdata', data_width)
    rvalid = m.Input('rvalid')
    rready = m.Output('rready')

    return m


_master_memory = None
_slave_memory = None
_master_lite_memory = None
_slave_lite_memory = None


def ipgen_master_memory():
    global _master_memory
    if _master_memory is None:
        _master_memory = mk_ipgen_master_memory()
    return _master_memory


def ipgen_slave_memory():
    global _slave_memory
    if _slave_memory is None:
        _slave_memory = mk_ipgen_slave_memory()
    return _slave_memory


def ipgen_master_lite_memory():
    global _master_lite_memory
    if _master_lite_memory is None:
        _master_lite_memory = mk_ipgen_master_lite_memory()
    return _master_lite_memory


def ipgen_slave_lite_memory():
    global _slave_lite_memory
    if _slave_lite_memory is None:
        _slave_lite_memory = mk_ipgen_slave_lite_memory()
    return _slave_lite_memory
