from __future__ import absolute_import
from __future__ import print_function

import xml.dom.minidom
import datetime
import copy
import math

import veriloggen.core.vtypes as vtypes
from veriloggen.resolver import resolver
from . import axi


PORTLIST = ('AWID', 'AWADDR', 'AWLEN', 'AWSIZE', 'AWBURST', 'AWLOCK',
            'AWCACHE', 'AWPROT', 'AWQOS', 'AWUSER', 'AWVALID', 'AWREADY',
            'WDATA', 'WSTRB', 'WLAST', 'WUSER', 'WVALID', 'WREADY',
            'BID', 'BRESP', 'BUSER', 'BVALID', 'BREADY',
            'ARID', 'ARADDR', 'ARLEN', 'ARSIZE', 'ARBURST', 'ARLOCK',
            'ARCACHE', 'ARPROT', 'ARQOS', 'ARUSER', 'ARVALID', 'ARREADY',
            'RID', 'RDATA', 'RRESP', 'RLAST', 'RUSER', 'RVALID', 'RREADY')

PORTLITELIST = ('AWADDR', 'AWCACHE', 'AWPROT', 'AWVALID', 'AWREADY',
                'WDATA', 'WSTRB', 'WVALID', 'WREADY',
                'BRESP', 'BVALID', 'BREADY',
                'ARADDR', 'ARCACHE', 'ARPROT', 'ARVALID', 'ARREADY',
                'RDATA', 'RRESP', 'RVALID', 'RREADY')

PORTSTREAMLIST = ('TDATA', 'TVALID', 'TREADY', 'TLAST', 'TSTRB', 'TUSER', 'TID', 'TDEST')


class ComponentGen(object):
    def __init__(self):
        self.m = None
        self.ip_name = None
        self.bus_interfaces = None
        self.clk_ports = None
        self.rst_ports = None
        self.irq_ports = None
        self.ext_ports = None
        self.ext_params = None

        self.vendor = 'user.org'
        self.library = 'user'
        self.version = '1.0'

        self.doc = None
        self.top = None

        self.dependency_consumer = set()

    def generate(self, m, ip_name, bus_interfaces,
                 clk_ports, rst_ports, irq_ports,
                 ext_ports, ext_params,
                 vendor='user.org', library='user', version='1.0',
                 description='user description',
                 supported_families=('zynq', 'zynquplus')):

        self.m = m
        self.ip_name = ip_name
        self.bus_interfaces = bus_interfaces
        self.clk_ports = clk_ports
        self.rst_ports = rst_ports
        self.irq_ports = irq_ports
        self.ext_ports = ext_ports
        self.ext_params = ext_params

        self.resolved_m = resolver.resolve(copy.deepcopy(m))

        self.vendor = vendor
        self.library = library
        self.version = version

        if not supported_families:
            raise ValueError(
                'supported_families must be a list or tuple with valid names.')

        self.supported_families = supported_families

        impl = xml.dom.minidom.getDOMImplementation()
        self.doc = impl.createDocument('spirit', 'spirit:component', None)
        self.top = self.doc.documentElement

        self.setAttribute(self.top, 'xmlns:xilinx', "http://www.xilinx.com")
        self.setAttribute(self.top, 'xmlns:spirit',
                          "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009")
        self.setAttribute(self.top, 'xmlns:xsi',
                          "http://www.w3.org/2001/XMLSchema-instance")

        self.dependency_consumer = set()

        self.top.appendChild(self.mkVendor())
        self.top.appendChild(self.mkLibrary())
        self.top.appendChild(self.mkName(self.ip_name))
        self.top.appendChild(self.mkVersion())

        self.top.appendChild(self.mkBusInterfaces())

        r = self.mkAddressSpaces()
        if r:
            self.top.appendChild(r)

        r = self.mkMemoryMaps()
        if r:
            self.top.appendChild(r)

        self.top.appendChild(self.mkModel())
        self.top.appendChild(self.mkFileSets())
        self.top.appendChild(self.mkDescription(description))
        self.top.appendChild(self.mkParameters())
        self.top.appendChild(self.mkVendorExtensions())

        return self.doc.toprettyxml(indent='  ')

    def setAttribute(self, obj, name, text):
        obj.setAttribute(name, str(text))

    def setText(self, obj, text):
        textobj = self.doc.createTextNode(str(text))
        obj.appendChild(textobj)

    def mkVendor(self):
        vendor = self.doc.createElement('spirit:vendor')
        self.setText(vendor, self.vendor)
        return vendor

    def mkLibrary(self):
        library = self.doc.createElement('spirit:library')
        self.setText(library, self.library)
        return library

    def mkVersion(self):
        version = self.doc.createElement('spirit:version')
        self.setText(version, str(self.version))
        return version

    def mkName(self, v):
        name = self.doc.createElement('spirit:name')
        self.setText(name, v)
        return name

    def mkTextNode(self, n, v):
        name = self.doc.createElement(n)
        self.setText(name, v)
        return name

    def mkBusInterfaces(self):
        bus = self.doc.createElement('spirit:busInterfaces')

        for bus_interface in self.bus_interfaces:
            bus.appendChild(self.mkBusInterface(bus_interface))

        for rst_name, rst_polarity in self.rst_ports.items():
            bus.appendChild(self.mkBusInterfaceReset(rst_name, rst_polarity))

        for clk_name, assoc_rsts in self.clk_ports.items():
            bus.appendChild(self.mkBusInterfaceClock(clk_name, assoc_rsts))

        for irq_name, sensitivity in self.irq_ports.items():
            bus.appendChild(self.mkBusInterfaceInterrupt(irq_name, sensitivity))

        return bus

    def mkBusInterface(self, obj):
        name = obj.name
        datawidth = obj.datawidth

        interface = self.doc.createElement('spirit:busInterface')
        interface.appendChild(self.mkName(name))

        if is_master(obj):
            interface.appendChild(self.mkBusTypeMemory())
            interface.appendChild(self.mkAbstractionTypeMemory())
            interface.appendChild(self.mkMaster(name))
            interface.appendChild(self.mkPortMapsMemory(obj))
        elif is_slave(obj):
            interface.appendChild(self.mkBusTypeMemory())
            interface.appendChild(self.mkAbstractionTypeMemory())
            interface.appendChild(self.mkSlave(name))
            interface.appendChild(self.mkPortMapsMemory(obj))
        elif is_streamin(obj):
            interface.appendChild(self.mkBusTypeStream())
            interface.appendChild(self.mkAbstractionTypeStream())
            interface.appendChild(self.mkStreamIn(name))
            interface.appendChild(self.mkPortMapsStream(obj))
        elif is_streamout(obj):
            interface.appendChild(self.mkBusTypeStream())
            interface.appendChild(self.mkAbstractionTypeStream())
            interface.appendChild(self.mkStreamOut(name))
            interface.appendChild(self.mkPortMapsStream(obj))
        else:
            raise TypeError("Unsupported type: '%s'" % str(type(obj)))

        return interface

    def mkBusTypeMemory(self):
        bustype = self.doc.createElement('spirit:busType')
        self.setAttribute(bustype, 'spirit:vendor', "xilinx.com")
        self.setAttribute(bustype, 'spirit:library', "interface")
        self.setAttribute(bustype, 'spirit:name', "aximm")
        self.setAttribute(bustype, 'spirit:version', "1.0")
        return bustype

    def mkAbstractionTypeMemory(self):
        abstractiontype = self.doc.createElement('spirit:abstractionType')
        self.setAttribute(abstractiontype, 'spirit:vendor', "xilinx.com")
        self.setAttribute(abstractiontype, 'spirit:library', "interface")
        self.setAttribute(abstractiontype, 'spirit:name', "aximm_rtl")
        self.setAttribute(abstractiontype, 'spirit:version', "1.0")
        return abstractiontype

    def mkBusTypeStream(self):
        bustype = self.doc.createElement('spirit:busType')
        self.setAttribute(bustype, 'spirit:vendor', "xilinx.com")
        self.setAttribute(bustype, 'spirit:library', "interface")
        self.setAttribute(bustype, 'spirit:name', "axis")
        self.setAttribute(bustype, 'spirit:version', "1.0")
        return bustype

    def mkAbstractionTypeStream(self):
        abstractiontype = self.doc.createElement('spirit:abstractionType')
        self.setAttribute(abstractiontype, 'spirit:vendor', "xilinx.com")
        self.setAttribute(abstractiontype, 'spirit:library', "interface")
        self.setAttribute(abstractiontype, 'spirit:name', "axis_rtl")
        self.setAttribute(abstractiontype, 'spirit:version', "1.0")
        return abstractiontype

    def mkMaster(self, name):
        master = self.doc.createElement('spirit:master')
        addressspaceref = self.doc.createElement('spirit:addressSpaceRef')
        self.setAttribute(addressspaceref, 'spirit:addressSpaceRef', name)
        master.appendChild(addressspaceref)
        return master

    def mkSlave(self, name):
        slave = self.doc.createElement('spirit:slave')
        memorymapref = self.doc.createElement('spirit:memoryMapRef')
        self.setAttribute(memorymapref, 'spirit:memoryMapRef', name)
        slave.appendChild(memorymapref)
        return slave

    def mkStreamIn(self, name):
        streamin = self.doc.createElement('spirit:slave')
        return streamin

    def mkStreamOut(self, name):
        streamout = self.doc.createElement('spirit:master')
        return streamout

    def mkPortMapsMemory(self, obj):
        lite = is_lite(obj)
        portmaps = self.doc.createElement('spirit:portMaps')
        portlist = list(PORTLITELIST if lite else PORTLIST)

        if not lite and obj.waddr.awid is None:
            portlist.remove('AWID')
        if not lite and obj.waddr.awuser is None:
            portlist.remove('AWUSER')
        if not lite and obj.wdata.wuser is None:
            portlist.remove('WUSER')
        if not lite and obj.wresp.bid is None:
            portlist.remove('BID')
        if not lite and obj.wresp.buser is None:
            portlist.remove('BUSER')
        if not lite and obj.raddr.arid is None:
            portlist.remove('ARID')
        if not lite and obj.raddr.aruser is None:
            portlist.remove('ARUSER')
        if not lite and obj.rdata.rid is None:
            portlist.remove('RID')
        if not lite and obj.rdata.ruser is None:
            portlist.remove('RUSER')

        for port in portlist:
            portmaps.appendChild(self.mkPortMapMemory(obj, port))

        return portmaps

    def mkPortMapsStream(self, obj):
        portmaps = self.doc.createElement('spirit:portMaps')
        portlist = list(PORTSTREAMLIST)

        if obj.tdata.tlast is None:
            portlist.remove('TLAST')
        if obj.tdata.tstrb is None:
            portlist.remove('TSTRB')
        if obj.tdata.tuser is None:
            portlist.remove('TUSER')
        if obj.tdata.tid is None:
            portlist.remove('TID')
        if obj.tdata.tdest is None:
            portlist.remove('TDEST')

        for port in portlist:
            portmaps.appendChild(self.mkPortMapStream(obj, port))

        return portmaps

    def mkPortMapMemory(self, obj, attr):
        portmap = self.doc.createElement('spirit:portMap')
        portmap.appendChild(self.mkLogicalPort(attr))
        portmap.appendChild(self.mkPhysicalPortMemory(obj, attr))
        return portmap

    def mkPortMapStream(self, obj, attr):
        portmap = self.doc.createElement('spirit:portMap')
        portmap.appendChild(self.mkLogicalPort(attr))
        portmap.appendChild(self.mkPhysicalPortStream(obj, attr))
        return portmap

    def mkLogicalPort(self, attr):
        logicalport = self.doc.createElement('spirit:logicalPort')
        logicalport.appendChild(self.mkName(attr))
        return logicalport

    def mkPhysicalPortMemory(self, obj, attr):
        if hasattr(obj.waddr, attr.lower()):
            name = getattr(obj.waddr, attr.lower()).name
        elif hasattr(obj.wdata, attr.lower()):
            name = getattr(obj.wdata, attr.lower()).name
        elif hasattr(obj.wresp, attr.lower()):
            name = getattr(obj.wresp, attr.lower()).name
        elif hasattr(obj.raddr, attr.lower()):
            name = getattr(obj.raddr, attr.lower()).name
        elif hasattr(obj.rdata, attr.lower()):
            name = getattr(obj.rdata, attr.lower()).name
        else:
            raise NameError("No such attribute '%s' in object '%s'" %
                            (attr.lower(), obj))

        physicalport = self.doc.createElement('spirit:physicalPort')
        physicalport.appendChild(self.mkName(name))
        return physicalport

    def mkPhysicalPortStream(self, obj, attr):
        if hasattr(obj.tdata, attr.lower()):
            name = getattr(obj.tdata, attr.lower()).name
        else:
            raise NameError("No such attribute '%s' in object '%s'" %
                            (attr.lower(), obj))

        physicalport = self.doc.createElement('spirit:physicalPort')
        physicalport.appendChild(self.mkName(name))
        return physicalport

    def mkBusInterfaceClock(self, name, rsts):
        interface = self.doc.createElement('spirit:busInterface')
        interface.appendChild(self.mkName(name))
        interface.appendChild(self.mkBusTypeClock())
        interface.appendChild(self.mkAbstractionTypeClock())
        interface.appendChild(self.mkSlaveClock())
        interface.appendChild(self.mkPortMapsClock(name))
        interface.appendChild(self.mkBusParametersClock(name, rsts))
        return interface

    def mkBusTypeClock(self):
        bustype = self.doc.createElement('spirit:busType')
        self.setAttribute(bustype, 'spirit:vendor', "xilinx.com")
        self.setAttribute(bustype, 'spirit:library', "signal")
        self.setAttribute(bustype, 'spirit:name', "clock")
        self.setAttribute(bustype, 'spirit:version', "1.0")
        return bustype

    def mkAbstractionTypeClock(self):
        abstractiontype = self.doc.createElement('spirit:abstractionType')
        self.setAttribute(abstractiontype, 'spirit:vendor', "xilinx.com")
        self.setAttribute(abstractiontype, 'spirit:library', "signal")
        self.setAttribute(abstractiontype, 'spirit:name', "clock_rtl")
        self.setAttribute(abstractiontype, 'spirit:version', "1.0")
        return abstractiontype

    def mkSlaveClock(self):
        slave = self.doc.createElement('spirit:slave')
        return slave

    def mkPortMapsClock(self, name):
        portmaps = self.doc.createElement('spirit:portMaps')
        portmaps.appendChild(self.mkPortMapClock(name))
        return portmaps

    def mkPortMapClock(self, name):
        portmap = self.doc.createElement('spirit:portMap')
        portmap.appendChild(self.mkLogicalPort('CLK'))
        portmap.appendChild(self.mkPhysicalPortClock(name))
        return portmap

    def mkPhysicalPortClock(self, name):
        physicalport = self.doc.createElement('spirit:physicalPort')
        physicalport.appendChild(self.mkName(name))
        return physicalport

    def mkBusParametersClock(self, name, rsts):
        parameters = self.doc.createElement('spirit:parameters')
        parameters.appendChild(self.mkBusParameterAssocBusIf(name))
        parameters.appendChild(self.mkBusParameterAssocReset(name, rsts))
        return parameters

    def mkBusParameterAssocBusIf(self, name):
        parameter = self.doc.createElement('spirit:parameter')
        parameter.appendChild(self.mkName('ASSOCIATED_BUSIF'))
        value = self.doc.createElement('spirit:value')

        bus_name_list = []
        for bus_interface in self.bus_interfaces:
            if (isinstance(bus_interface.clk, vtypes._Variable) and
                bus_interface.clk.module.is_input(bus_interface.clk.name) and
                    bus_interface.clk.name == name):
                bus_name_list.append(bus_interface.name)

        bus_names = ':'.join(bus_name_list)

        self.setAttribute(value, 'spirit:id', "BUSIFPARAM_VALUE."
                          + name + ".ASSOCIATED_BUSIF")
        self.setText(value, bus_names)
        parameter.appendChild(value)
        return parameter

    def mkBusParameterAssocReset(self, name, rsts):
        parameter = self.doc.createElement('spirit:parameter')
        parameter.appendChild(self.mkName('ASSOCIATED_RESET'))
        value = self.doc.createElement('spirit:value')

        rst_names = ':'.join(rsts)

        self.setAttribute(value, 'spirit:id', "BUSIFPARAM_VALUE."
                          + name + ".ASSOCIATED_RESET")
        self.setText(value, rst_names)
        parameter.appendChild(value)
        return parameter

    def mkBusInterfaceReset(self, name, polarity):
        interface = self.doc.createElement('spirit:busInterface')
        interface.appendChild(self.mkName(name))
        interface.appendChild(self.mkBusTypeReset())
        interface.appendChild(self.mkAbstractionTypeReset())
        interface.appendChild(self.mkSlaveReset())
        interface.appendChild(self.mkPortMapsReset(name))
        interface.appendChild(self.mkBusParametersReset(name, polarity))
        return interface

    def mkBusTypeReset(self):
        bustype = self.doc.createElement('spirit:busType')
        self.setAttribute(bustype, 'spirit:vendor', "xilinx.com")
        self.setAttribute(bustype, 'spirit:library', "signal")
        self.setAttribute(bustype, 'spirit:name', "reset")
        self.setAttribute(bustype, 'spirit:version', "1.0")
        return bustype

    def mkAbstractionTypeReset(self):
        abstractiontype = self.doc.createElement('spirit:abstractionType')
        self.setAttribute(abstractiontype, 'spirit:vendor', "xilinx.com")
        self.setAttribute(abstractiontype, 'spirit:library', "signal")
        self.setAttribute(abstractiontype, 'spirit:name', "reset_rtl")
        self.setAttribute(abstractiontype, 'spirit:version', "1.0")
        return abstractiontype

    def mkSlaveReset(self):
        slave = self.doc.createElement('spirit:slave')
        return slave

    def mkPortMapsReset(self, name):
        portmaps = self.doc.createElement('spirit:portMaps')
        portmaps.appendChild(self.mkPortMapReset(name))
        return portmaps

    def mkPortMapReset(self, name):
        portmap = self.doc.createElement('spirit:portMap')
        portmap.appendChild(self.mkLogicalPort('RST'))
        portmap.appendChild(self.mkPhysicalPortReset(name))
        return portmap

    def mkPhysicalPortReset(self, name):
        physicalport = self.doc.createElement('spirit:physicalPort')
        physicalport.appendChild(self.mkName(name))
        return physicalport

    def mkBusParametersReset(self, name, polarity):
        parameters = self.doc.createElement('spirit:parameters')
        parameters.appendChild(self.mkBusParameterPolarity(name, polarity))
        return parameters

    def mkBusParameterPolarity(self, name, polarity):
        parameter = self.doc.createElement('spirit:parameter')
        parameter.appendChild(self.mkName('POLARITY'))
        value = self.doc.createElement('spirit:value')
        self.setAttribute(value, 'spirit:id', "BUSIFPARAM_VALUE."
                          + name + ".POLARITY")
        self.setText(value, polarity)
        parameter.appendChild(value)
        return parameter

    def mkBusInterfaceInterrupt(self, name, sensitivity):
        interface = self.doc.createElement('spirit:busInterface')
        interface.appendChild(self.mkName(name))
        interface.appendChild(self.mkBusTypeInterrupt())
        interface.appendChild(self.mkAbstractionTypeInterrupt())
        interface.appendChild(self.mkMasterInterrupt())
        interface.appendChild(self.mkPortMapsInterrupt(name))
        interface.appendChild(self.mkBusParametersInterrupt(name, sensitivity))
        return interface

    def mkBusTypeInterrupt(self):
        bustype = self.doc.createElement('spirit:busType')
        self.setAttribute(bustype, 'spirit:vendor', "xilinx.com")
        self.setAttribute(bustype, 'spirit:library', "signal")
        self.setAttribute(bustype, 'spirit:name', "interrupt")
        self.setAttribute(bustype, 'spirit:version', "1.0")
        return bustype

    def mkAbstractionTypeInterrupt(self):
        abstractiontype = self.doc.createElement('spirit:abstractionType')
        self.setAttribute(abstractiontype, 'spirit:vendor', "xilinx.com")
        self.setAttribute(abstractiontype, 'spirit:library', "signal")
        self.setAttribute(abstractiontype, 'spirit:name', "interrupt_rtl")
        self.setAttribute(abstractiontype, 'spirit:version', "1.0")
        return abstractiontype

    def mkMasterInterrupt(self):
        master = self.doc.createElement('spirit:master')
        return master

    def mkPortMapsInterrupt(self, name):
        portmaps = self.doc.createElement('spirit:portMaps')
        portmaps.appendChild(self.mkPortMapInterrupt(name))
        return portmaps

    def mkPortMapInterrupt(self, name):
        portmap = self.doc.createElement('spirit:portMap')
        portmap.appendChild(self.mkLogicalPort('INTERRUPT'))
        portmap.appendChild(self.mkPhysicalPortInterrupt(name))
        return portmap

    def mkPhysicalPortInterrupt(self, name):
        physicalport = self.doc.createElement('spirit:physicalPort')
        physicalport.appendChild(self.mkName(name))
        return physicalport

    def mkBusParametersInterrupt(self, name, sensitivity):
        parameters = self.doc.createElement('spirit:parameters')
        parameters.appendChild(self.mkBusParameterSensitivity(name, sensitivity))
        return parameters

    def mkBusParameterSensitivity(self, name, sensitivity):
        parameter = self.doc.createElement('spirit:parameter')
        parameter.appendChild(self.mkName('SENSITIVITY'))
        value = self.doc.createElement('spirit:value')
        self.setAttribute(value, 'spirit:id', "BUSIFPARAM_VALUE."
                          + name.upper() + ".SENSITIVITY")
        self.setText(value, sensitivity)
        parameter.appendChild(value)
        return parameter

    def mkAddressSpaces(self):
        isempty = True
        spaces = self.doc.createElement('spirit:addressSpaces')
        for bus_interface in self.bus_interfaces:
            if isinstance(bus_interface, (axi.AxiLiteMaster, axi.AxiMaster)):
                spaces.appendChild(self.mkAddressSpace(bus_interface))
                isempty = False
        if isempty:
            return None
        return spaces

    def mkAddressSpace(self, obj):
        name = obj.name

        space = self.doc.createElement('spirit:addressSpace')
        space.appendChild(self.mkName(name))

        range = self.doc.createElement('spirit:range')
        self.setAttribute(range, 'spirit:format', "long")
        range_value = 2 ** self.resolved_m[obj.name + '_awaddr'].width
        self.setText(range, range_value)
        space.appendChild(range)

        width = self.doc.createElement('spirit:width')
        self.setAttribute(width, 'spirit:format', "long")
        width_value = self.resolved_m[obj.name + '_wdata'].width
        self.setText(width, width_value)
        space.appendChild(width)

        return space

    def mkMemoryMaps(self):
        isempty = True
        maps = self.doc.createElement('spirit:memoryMaps')
        for bus_interface in self.bus_interfaces:
            if isinstance(bus_interface, (axi.AxiLiteSlave, axi.AxiSlave)):
                maps.appendChild(self.mkMemoryMap(bus_interface))
                isempty = False
        if isempty:
            return None
        return maps

    def mkMemoryMap(self, obj):
        name = obj.name
        map = self.doc.createElement('spirit:memoryMap')
        map.appendChild(self.mkName(name))

        addressblock = self.doc.createElement('spirit:addressBlock')
        addressblock.appendChild(self.mkName(name + '_reg'))

        baseaddr = self.doc.createElement('spirit:baseAddress')
        self.setAttribute(baseaddr, 'spirit:format', "long")
        self.setText(baseaddr, 0)
        addressblock.appendChild(baseaddr)

        range = self.doc.createElement('spirit:range')
        self.setAttribute(range, 'spirit:format', "long")

        if hasattr(obj, 'register') and isinstance(obj.register, (tuple, list)):
            map_range = 2 ** int(math.ceil(math.log(max(len(obj.register), 4096), 2)))
        else:
            map_range = 2 ** self.resolved_m[obj.name + '_awaddr'].width

        self.setText(range, map_range)
        addressblock.appendChild(range)

        width = self.doc.createElement('spirit:width')
        self.setAttribute(width, 'spirit:format', "long")
        self.setText(width, obj.datawidth)
        addressblock.appendChild(width)

        usage = self.doc.createElement('spirit:usage')
        self.setText(usage, 'register')
        addressblock.appendChild(usage)

        map.appendChild(addressblock)

        return map

    def mkModel(self):
        model = self.doc.createElement('spirit:model')
        model.appendChild(self.mkViews())
        model.appendChild(self.mkPorts())
        return model

    def mkViews(self):
        views = self.doc.createElement('spirit:views')
        views.appendChild(self.mkView('xilinx_verilogsynthesis',
                                      'Verilog Synthesis',
                                      'verilogSource:vivado.xilinx.com:synthesis',
                                      'verilog',
                                      self.ip_name,
                                      'xilinx_verilogsynthesis_view_fileset'))
        views.appendChild(self.mkView('xilinx_verilogbehavioralsimulation',
                                      'Verilog Simulation',
                                      'verilogSource:vivado.xilinx.com:simulation',
                                      'verilog',
                                      self.ip_name,
                                      'xilinx_verilogbehavioralsimulation_view_fileset'))
        views.appendChild(self.mkView('xilinx_xpgui',
                                      'UI Layout',
                                      ':vivado.xilinx.com:xgui.ui',
                                      None,
                                      None,
                                      'xilinx_xpgui_view_fileset'))
        return views

    def mkView(self, name, displayname, envidentifier, language, modelname, localname):
        view = self.doc.createElement('spirit:view')
        view.appendChild(self.mkName(name))
        view.appendChild(self.mkTextNode('spirit:displayName', displayname))
        view.appendChild(self.mkTextNode('spirit:envIdentifier', envidentifier))

        if language is not None:
            view.appendChild(self.mkTextNode('spirit:language', language))

        if modelname is not None:
            view.appendChild(self.mkTextNode('spirit:modelName', modelname))

        filesetref = self.doc.createElement('spirit:fileSetRef')
        filesetref.appendChild(self.mkTextNode('spirit:localName', localname))
        view.appendChild(filesetref)

        return view

    def mkPorts(self):
        ports = self.doc.createElement('spirit:ports')

        for portname, port in self.ext_ports.items():
            ports.appendChild(self.mkPortSignal(port))

        return ports

    def mkPortSignal(self, var):
        name = var.name
        direction = ('in' if isinstance(var, vtypes.Input) else
                     'out' if isinstance(var, vtypes.Output) else
                     'inout')

        width = self.resolved_m[name].width
        h = width - 1 if width is not None else None
        l = 0 if h is not None else None

        return self.mkPortEntry(name, direction,
                                None, h, None, l)

    def mkPortEntry(self, name, direction,
                    lvar, lvalue, rvar, rvalue,
                    withdriver=False,
                    extensionvar=None, extensionvalue='true'):

        port = self.doc.createElement('spirit:port')
        port.appendChild(self.mkName(name))
        port.appendChild(self.mkWire(direction, lvar, lvalue, rvar, rvalue, withdriver))

        if extensionvar is not None:
            port.appendChild(
                self.mkPortVendorExtensions(name, extensionvar, extensionvalue))

        return port

    def mkWire(self, direction, lvar, lvalue, rvar, rvalue, withdriver=False):
        wire = self.doc.createElement('spirit:wire')
        wire.appendChild(self.mkDirection(direction))

        if not (lvalue is None and rvalue is None):
            wire.appendChild(self.mkVector(lvar, lvalue, rvar, rvalue))

        wire.appendChild(self.mkWireTypeDefs('wire'))

        if withdriver:
            wire.appendChild(self.mkDriver())

        return wire

    def mkDirection(self, direction):
        return self.mkTextNode('spirit:direction', direction)

    def mkVector(self, lvar, lvalue, rvar, rvalue):
        vector = self.doc.createElement('spirit:vector')

        left = self.doc.createElement('spirit:left')
        self.setAttribute(left, 'spirit:format', "long")

        if lvar is not None:
            self.setAttribute(left, 'spirit:resolve', 'dependent')
            self.setAttribute(left, 'spirit:dependency', lvar)

        self.setText(left, lvalue)
        vector.appendChild(left)

        right = self.doc.createElement('spirit:right')
        self.setAttribute(right, 'spirit:format', "long")

        if rvar is not None:
            self.setAttribute(right, 'spirit:resolve', 'dependent')
            self.setAttribute(right, 'spirit:dependency', rvar)

        self.setText(right, rvalue)
        vector.appendChild(right)

        return vector

    def mkWireTypeDefs(self, wiretype):
        wiretypedefs = self.doc.createElement('spirit:wireTypeDefs')
        wiretypedefs.appendChild(self.mkWireTypeDef(wiretype))
        return wiretypedefs

    def mkWireTypeDef(self, wiretype):
        wiretypedef = self.doc.createElement('spirit:wireTypeDef')
        wiretypedef.appendChild(self.mkTextNode('spirit:typeName', wiretype))
        wiretypedef.appendChild(
            self.mkTextNode('spirit:viewNameRef', 'xilinx_verilogsynthesis'))
        wiretypedef.appendChild(
            self.mkTextNode('spirit:viewNameRef', 'xilinx_verilogbehavioralsimulation'))
        return wiretypedef

    def mkDriver(self):
        driver = self.doc.createElement('spirit:driver')
        driver.appendChild(self.mkTextNode('spirit:defaultValue', 0))
        return driver

    def mkPortVendorExtensions(self, name, var, value='true'):
        extensions = self.doc.createElement('spirit:vendorExtensions')
        portinfo = self.doc.createElement('xilinx:portInfo')
        enablement = self.doc.createElement('xilinx:enablement')

        isEnabled = self.doc.createElement('xilinx:isEnabled')
        self.setAttribute(isEnabled, 'xilinx:resolve', "dependent")
        self.setAttribute(isEnabled, 'xilinx:id', 'PORT_ENABLEMENT.' + name)
        self.setAttribute(isEnabled, 'xilinx:dependency',
                          "spirit:decode(id('MODELPARAM_VALUE." + var.name + "')) >0")
        self.setText(isEnabled, value)
        enablement.appendChild(isEnabled)

        portinfo.appendChild(enablement)
        extensions.appendChild(portinfo)
        return extensions

    def mkFileSets(self):
        filesets = self.doc.createElement('spirit:fileSets')

        source = self.doc.createElement('spirit:fileSet')
        source.appendChild(self.mkName("xilinx_verilogsynthesis_view_fileset"))
        source.appendChild(self.mkFileSet('hdl/' + self.ip_name + '.v',
                                          'verilogSource'))
        filesets.appendChild(source)

        sim = self.doc.createElement('spirit:fileSet')
        sim.appendChild(self.mkName(
            "xilinx_verilogbehavioralsimulation_view_fileset"))
        sim.appendChild(self.mkFileSet('hdl/' + self.ip_name + '.v',
                                       'verilogSource'))
        filesets.appendChild(sim)

        xguitcl = self.doc.createElement('spirit:fileSet')
        xguitcl.appendChild(self.mkName("xilinx_xpgui_view_fileset"))
        xguitcl.appendChild(self.mkFileSet('xgui/xgui.tcl',
                                           'tclSource', 'XGUI_VERSION_2'))
        filesets.appendChild(xguitcl)

        return filesets

    def mkFileSet(self, name, filetype=None, *userfiletypes):
        fileset = self.doc.createElement('spirit:file')
        fileset.appendChild(self.mkName(name))
        if filetype is not None:
            fileset.appendChild(self.mkTextNode('spirit:fileType', filetype))
        for u in userfiletypes:
            fileset.appendChild(self.mkTextNode('spirit:userFileType', u))
        return fileset

    def mkDescription(self, description):
        return self.mkTextNode('spirit:description', description)

    def mkParameters(self):
        parameters = self.doc.createElement('spirit:parameters')

        compname = self.doc.createElement('spirit:parameter')
        compname.appendChild(self.mkName('Component_Name'))
        value = self.doc.createElement('spirit:value')
        self.setAttribute(value, 'spirit:resolve', 'user')
        self.setAttribute(value, 'spirit:id',
                          "PARAM_VALUE." + 'Component_Name')
        self.setAttribute(value, 'spirit:order', 1)
        self.setText(value, self.ip_name + '_v' + self.version.replace('.', '_'))
        compname.appendChild(value)
        parameters.appendChild(compname)

        return parameters

    def mkVendorExtensions(self):
        extensions = self.doc.createElement('spirit:vendorExtensions')
        extensions.appendChild(self.mkCoreExtensions())
        packageinfo = self.doc.createElement('xilinx:packagingInfo')
        packageinfo.appendChild(self.mkTextNode(
            'xilinx:xilinxVersion', '2018.3'))
        extensions.appendChild(packageinfo)
        return extensions

    def mkCoreExtensions(self):
        coreextensions = self.doc.createElement('xilinx:coreExtensions')
        supported = self.doc.createElement('xilinx:supportedFamilies')

        for name in self.supported_families:
            family = self.doc.createElement('xilinx:family')
            self.setAttribute(family, 'xilinx:lifeCycle', 'Production')
            self.setText(family, name)
            supported.appendChild(family)

        coreextensions.appendChild(supported)

        taxonomies = self.doc.createElement('xilinx:taxonomies')
        taxonomies.appendChild(self.mkTextNode('xilinx:taxonomy', '/UserIP'))
        coreextensions.appendChild(taxonomies)

        coreextensions.appendChild(
            self.mkTextNode('xilinx:displayName',
                            (self.ip_name + '_v' + self.version.replace('.', '_'))))

        coreextensions.appendChild(self.mkTextNode('xilinx:coreRevision', 1))

        now = datetime.datetime.now()
        dt = now.strftime("%Y-%m-%dT%H:%M:%SZ")  # '2015-03-08T02:16:15Z'
        coreextensions.appendChild(self.mkTextNode('xilinx:coreCreationDateTime', dt))

        return coreextensions


def is_master(obj):
    return isinstance(obj, (axi.AxiMaster, axi.AxiLiteMaster))


def is_slave(obj):
    return isinstance(obj, (axi.AxiSlave, axi.AxiLiteSlave))


def is_streamin(obj):
    return isinstance(obj, axi.AxiStreamIn)


def is_streamout(obj):
    return isinstance(obj, axi.AxiStreamOut)


def is_lite(obj):
    return isinstance(obj, (axi.AxiLiteMaster, axi.AxiLiteSlave))
