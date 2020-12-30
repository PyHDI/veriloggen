from __future__ import absolute_import
from __future__ import print_function


import os
from collections import OrderedDict

import veriloggen.core.vtypes as vtypes
from . import componentgen

TEMPLATE_DIR = os.path.dirname(os.path.abspath(__file__)) + '/template/'


def to_ipxact(m, ip_name=None, ip_ver='1.0',
              clk_ports=None, rst_ports=None, irq_ports=None):

    if ip_name is None:
        ip_name = m.name

    if clk_ports is None:
        clk_ports = {}

    if isinstance(clk_ports, (list, tuple)):
        clk_ports = OrderedDict(clk_ports)
        for name in clk_ports.keys():
            clk_ports[name] = list(clk_ports[name])

    if rst_ports is None:
        rst_ports = {}

    if isinstance(rst_ports, (list, tuple)):
        rst_ports = OrderedDict(rst_ports)

    if irq_ports is None:
        irq_ports = {}

    if isinstance(irq_ports, (list, tuple)):
        irq_ports = OrderedDict(irq_ports)

    dirname = ''.join([ip_name, '_v', ip_ver.replace('.', '_'), '/'])

    verilogname = ip_name + '.v'
    xmlname = 'component.xml'
    #xdcname = ip_name + '.xdc'
    #bdname = 'bd.tcl'
    xguiname = 'xgui.tcl'

    verilogpath = dirname + 'hdl/'
    xmlpath = dirname
    #xdcpath = dirname + 'data/'
    #bdpath = dirname + 'bd/'
    xguipath = dirname + 'xgui/'

    if not os.path.exists(dirname):
        os.mkdir(dirname)
    #if not os.path.exists(dirname + '/' + 'data'):
    #    os.mkdir(dirname + '/' + 'data')
    #if not os.path.exists(dirname + '/' + 'bd'):
    #    os.mkdir(dirname + '/' + 'bd')
    if not os.path.exists(dirname + '/' + 'xgui'):
        os.mkdir(dirname + '/' + 'xgui')
    if not os.path.exists(dirname + '/' + 'hdl'):
        os.mkdir(dirname + '/' + 'hdl')

    masterbus = m.masterbus if hasattr(m, 'masterbus') else []
    slavebus = m.slavebus if hasattr(m, 'slavebus') else []
    streaminbus = m.streaminbus if hasattr(m, 'streaminbus') else []
    streamoutbus = m.streamoutbus if hasattr(m, 'streamoutbus') else []
    bus_interfaces = masterbus + slavebus + streaminbus + streamoutbus

    for bus_interface in bus_interfaces:
        if (isinstance(bus_interface.clk, vtypes._Variable) and
                bus_interface.clk.module.is_input(bus_interface.clk.name)):
            clk = bus_interface.clk.name
        else:
            clk = None

        if (isinstance(bus_interface.rst, vtypes._Variable) and
                bus_interface.rst.module.is_input(bus_interface.rst.name)):
            rst = bus_interface.rst.name
        else:
            rst = None

        if clk is not None and clk not in clk_ports:
            clk_ports[clk] = []

        if clk is not None and rst is not None and rst not in clk_ports[clk]:
            clk_ports[clk].append(rst)

        if rst is not None and rst not in rst_ports:
            rst_ports[rst] = 'ACTIVE_HIGH'

    ext_ports = m.io_variable
    ext_params = m.global_constant

    # component.xml
    gen = componentgen.ComponentGen()
    xml_code = gen.generate(m,
                            ip_name,
                            bus_interfaces,
                            clk_ports,
                            rst_ports,
                            irq_ports,
                            ext_ports,
                            ext_params,
                            version=ip_ver)

    f = open(xmlpath + xmlname, 'w')
    f.write(xml_code)
    f.close()

    ## xdc
    #xdc_code = open(TEMPLATE_DIR + 'ipxact.xdc', 'r').read()

    #f = open(xdcpath + xdcname, 'w')
    #f.write(xdc_code)
    #f.close()

    ## bd
    #bd_code = open(TEMPLATE_DIR + 'bd.tcl', 'r').read()

    #f = open(bdpath + bdname, 'w')
    #f.write(bd_code)
    #f.close()

    # xgui file
    xgui_code = open(TEMPLATE_DIR + 'xgui_tcl.txt', 'r').read()

    f = open(xguipath + xguiname, 'w')
    f.write(xgui_code)
    f.close()

    # hdl file
    code = m.to_verilog()

    f = open(verilogpath + verilogname, 'w')
    f.write(code)
    f.close()
