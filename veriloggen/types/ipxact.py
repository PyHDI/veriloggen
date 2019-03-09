from __future__ import absolute_import
from __future__ import print_function


import os
from collections import OrderedDict

import veriloggen.core.vtypes as vtypes
from . import componentgen

TEMPLATE_DIR = os.path.dirname(os.path.abspath(__file__)) + '/template/'


def to_ipxact(m, ip_name=None, ip_ver='v1_00_a',
              clk_ports=None, rst_ports=None):

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

    dirname = ''.join([ip_name, '_', ip_ver, '/'])

    verilogname = ip_name + '.v'
    xmlname = 'component.xml'
    xdcname = ip_name + '.xdc'
    bdname = 'bd.tcl'
    xguiname = 'xgui.tcl'

    verilogpath = dirname + 'hdl/verilog/'
    xmlpath = dirname
    xdcpath = dirname + 'data/'
    bdpath = dirname + 'bd/'
    xguipath = dirname + 'xgui/'

    if not os.path.exists(dirname):
        os.mkdir(dirname)
    if not os.path.exists(dirname + '/' + 'data'):
        os.mkdir(dirname + '/' + 'data')
    if not os.path.exists(dirname + '/' + 'bd'):
        os.mkdir(dirname + '/' + 'bd')
    if not os.path.exists(dirname + '/' + 'xgui'):
        os.mkdir(dirname + '/' + 'xgui')
    if not os.path.exists(dirname + '/' + 'hdl'):
        os.mkdir(dirname + '/' + 'hdl')
    if not os.path.exists(dirname + '/' + 'hdl/verilog'):
        os.mkdir(dirname + '/' + 'hdl/verilog')

    masterbus = m.masterbus if hasattr(m, 'masterbus') else []
    slavebus = m.slavebus if hasattr(m, 'slavebus') else []
    bus_interfaces = masterbus + slavebus

    for bus_interface in bus_interfaces:
        clk = bus_interface.clk.name if isinstance(bus_interface.clk, vtypes.Input) else None
        rst = bus_interface.rst.name if isinstance(bus_interface.rst, vtypes.Input) else None

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
                            ext_ports,
                            ext_params)

    f = open(xmlpath + xmlname, 'w')
    f.write(xml_code)
    f.close()

    # xdc
    xdc_code = open(TEMPLATE_DIR + 'ipxact.xdc', 'r').read()

    f = open(xdcpath + xdcname, 'w')
    f.write(xdc_code)
    f.close()

    # bd
    bd_code = open(TEMPLATE_DIR + 'bd.tcl', 'r').read()

    f = open(bdpath + bdname, 'w')
    f.write(bd_code)
    f.close()

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
