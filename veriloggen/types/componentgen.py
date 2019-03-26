from __future__ import absolute_import
from __future__ import print_function

import xml.dom.minidom
import datetime
import copy

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

PORTLITELIST = ('AWADDR', 'AWPROT', 'AWVALID', 'AWREADY',
                'WDATA', 'WSTRB', 'WVALID', 'WREADY',
                'BRESP', 'BVALID', 'BREADY',
                'ARADDR', 'ARPROT', 'ARVALID', 'ARREADY',
                'RDATA', 'RRESP', 'RVALID', 'RREADY')


class ComponentGen(object):
    def __init__(self):
        self.m = None
        self.ip_name = None
        self.bus_interfaces = None
        self.clk_ports = None
        self.rst_ports = None
        self.ext_ports = None
        self.ext_params = None

        self.vendor = 'user'
        self.library = 'user'
        self.version = '1.0'

        self.doc = None
        self.top = None

        self.dependency_consumer = set()

    def generate(self, m, ip_name, bus_interfaces,
                 clk_ports, rst_ports,
                 ext_ports, ext_params,
                 vendor='user', library='user', version='1.0',
                 description='user description'):

        self.m = m
        self.ip_name = ip_name
        self.bus_interfaces = bus_interfaces
        self.clk_ports = clk_ports
        self.rst_ports = rst_ports
        self.ext_ports = ext_ports
        self.ext_params = ext_params

        self.resolved_m = resolver.resolve(copy.deepcopy(m))

        self.vendor = vendor
        self.library = library
        self.version = version

        impl = xml.dom.minidom.getDOMImplementation()
        self.doc = impl.createDocument('spirit', 'spirit:component', None)
        self.top = self.doc.documentElement

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
#        self.top.appendChild(self.mkChoices())
        self.top.appendChild(self.mkFileSets())
        self.top.appendChild(self.mkDescription(description))
        self.top.appendChild(self.mkParameters())
        self.top.appendChild(self.mkVendorExtensions())

        return self.doc.toprettyxml(indent='  ')

    def setAttribute(self, obj, name, text):
        attrobj = self.doc.createAttribute(name)
        attrobj.value = str(text)
        obj.setAttributeNode(attrobj)

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

        for clk_name, assoc_rsts in self.clk_ports.items():
            bus.appendChild(self.mkBusInterfaceClock(clk_name, assoc_rsts))

        for rst_name, rst_polarity in self.rst_ports.items():
            bus.appendChild(self.mkBusInterfaceReset(rst_name, rst_polarity))

        return bus

    def mkBusInterface(self, obj):
        master = is_master(obj)
        name = obj.name
        datawidth = obj.datawidth
        interface = self.doc.createElement('spirit:busInterface')
        interface.appendChild(self.mkName(name))
        interface.appendChild(self.mkBusType())
        interface.appendChild(self.mkAbstractionType())
        if master:
            interface.appendChild(self.mkMaster(name))
        else:
            interface.appendChild(self.mkSlave(name))
        interface.appendChild(self.mkPortMaps(obj))
        interface.appendChild(self.mkBusParameters(name, datawidth, master))
        return interface

    def mkBusType(self):
        bustype = self.doc.createElement('spirit:busType')
        self.setAttribute(bustype, 'spirit:vendor', "xilinx.com")
        self.setAttribute(bustype, 'spirit:library', "interface")
        self.setAttribute(bustype, 'spirit:name', "aximm")
        self.setAttribute(bustype, 'spirit:version', "1.0")
        return bustype

    def mkAbstractionType(self):
        abstractiontype = self.doc.createElement('spirit:abstractionType')
        self.setAttribute(abstractiontype, 'spirit:vendor', "xilinx.com")
        self.setAttribute(abstractiontype, 'spirit:library', "interface")
        self.setAttribute(abstractiontype, 'spirit:name', "aximm_rtl")
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

    def mkPortMaps(self, obj):
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
            portmaps.appendChild(self.mkPortMap(obj, port))

        return portmaps

    def mkPortMap(self, obj, attr):
        portmap = self.doc.createElement('spirit:portMap')
        portmap.appendChild(self.mkLogicalPort(attr))
        portmap.appendChild(self.mkPhysicalPort(obj, attr))
        return portmap

    def mkLogicalPort(self, attr):
        logicalport = self.doc.createElement('spirit:logicalPort')
        logicalport.appendChild(self.mkName(attr))
        return logicalport

    def mkPhysicalPort(self, obj, attr):
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

    def mkBusParameters(self, name, addrwidth, datawidth):
        parameters = self.doc.createElement('spirit:parameters')
        parameters.appendChild(self.mkBusParameterAddrWidth(name, addrwidth))
        parameters.appendChild(self.mkBusParameterDataWidth(name, datawidth))
        parameters.appendChild(self.mkBusParameterSupportsNarrowBurst(name, 0))
        return parameters

    def mkBusParameterAddrWidth(self, name, num):
        parameter = self.doc.createElement('spirit:parameter')
        parameter.appendChild(self.mkName('ADDR_WIDTH'))
        value = self.doc.createElement('spirit:value')
        self.setAttribute(value, 'spirit:id', "BUSIFPARAM_VALUE." + name + ".ADDR_WIDTH")
        self.setText(value, num)
        parameter.appendChild(value)
        return parameter

    def mkBusParameterDataWidth(self, name, num):
        parameter = self.doc.createElement('spirit:parameter')
        parameter.appendChild(self.mkName('DATA_WIDTH'))
        value = self.doc.createElement('spirit:value')
        self.setAttribute(value, 'spirit:id', "BUSIFPARAM_VALUE." + name + ".DATA_WIDTH")
        self.setText(value, num)
        parameter.appendChild(value)
        return parameter

    def mkBusParameterSupportsNarrowBurst(self, name, num):
        parameter = self.doc.createElement('spirit:parameter')
        parameter.appendChild(self.mkName('SUPPORTS_NARROW_BURST'))
        value = self.doc.createElement('spirit:value')
        self.setAttribute(value, 'spirit:id', "BUSIFPARAM_VALUE." + name + ".SUPPORTS_NARROW_BURST")
        self.setText(value, num)
        parameter.appendChild(value)
        return parameter

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

        if not isinstance(obj.addrwidth, int):
            self.setAttribute(range, 'spirit:resolve', "dependent")
            dep = "'MODELPARAM_VALUE." + name + "_ADDR_WIDTH'"
            self.dependency_consumer.add(dep)
            self.setAttribute(range, 'spirit:dependency',
                              ("pow(2,(spirit:decode(id(" + dep + ")) - 1) + 1)"))
            self.setAttribute(range, 'spirit:minimum', "0")
            self.setAttribute(range, 'spirit:maximum', str(vtypes.Int(2) ** obj.addrwidth))
        else:
            self.setAttribute(range, 'spirit:resolve', "immediate")

        range_value = 2 ** self.resolved_m[obj.name + '_awaddr'].width
        self.setText(range, range_value)
        space.appendChild(range)

        width = self.doc.createElement('spirit:width')
        self.setAttribute(width, 'spirit:format', "long")

        if not isinstance(obj.datawidth, int):
            self.setAttribute(width, 'spirit:resolve', "dependent")
            dep = "'MODELPARAM_VALUE." + name + "_DATA_WIDTH'"
            self.dependency_consumer.add(dep)
            self.setAttribute(width, 'spirit:dependency',
                              ("(spirit:decode(id(" + dep + ")) - 1) + 1"))

        width_value = self.resolved_m[obj.name + '_wdata'].width
        self.setText(width, width_value)
        space.appendChild(width)

        space.appendChild(self.mkAddressSpaceParameters(name))
        return space

    def mkAddressSpaceParameters(self, name):
        parameters = self.doc.createElement('spirit:parameters')
        parameters.appendChild(self.mkAddressSpaceParameterPreferredUsage(name))
        return parameters

    def mkAddressSpaceParameterPreferredUsage(self, name):
        base = self.doc.createElement('spirit:parameter')
        base.appendChild(self.mkName('PREFERRED_USAGE'))
        value = self.doc.createElement('spirit:value')
        self.setAttribute(value, 'spirit:id',
                          "ADDRSPACEPARAM_VALUE." + name + ".PREFERRED_USAGE")
        self.setText(value, 'MEMORY')
        base.appendChild(value)
        return base

    def mkMemoryMaps(self):
        isempty = True
        maps = self.doc.createElement('spirit:memoryMaps')
        for bus_interface in self.bus_interfaces:
            if not isinstance(bus_interface, (axi.AxiLiteMaster, axi.AxiMaster)):
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
        addressblock.appendChild(self.mkName(name + '_REG'))

        baseaddr = self.doc.createElement('spirit:baseAddress')
        self.setAttribute(baseaddr, 'spirit:format', "long")
        self.setText(baseaddr, 0)
        addressblock.appendChild(baseaddr)

        range = self.doc.createElement('spirit:range')
        self.setAttribute(range, 'spirit:format', "long")
        self.setAttribute(range, 'spirit:resolve', "generated")
        map_range = 65536
        self.setText(range, map_range)
        addressblock.appendChild(range)

        width = self.doc.createElement('spirit:width')
        self.setAttribute(width, 'spirit:format', "long")
        self.setText(width, obj.datawidth)
        addressblock.appendChild(width)

        usage = self.doc.createElement('spirit:usage')
        self.setText(usage, 'register')
        addressblock.appendChild(usage)

        addressblock.appendChild(self.mkMemoryMapParameters(name))

        reg = self.mkMemoryMapRegister(obj)
        if reg:
            addressblock.appendChild(reg)

        map.appendChild(addressblock)

        return map

    def mkMemoryMapParameters(self, name):
        parameters = self.doc.createElement('spirit:parameters')
        parameters.appendChild(self.mkMemoryMapParameterBase(name))
        parameters.appendChild(self.mkMemoryMapParameterHigh(name))
        return parameters

    def mkMemoryMapParameterBase(self, name):
        base = self.doc.createElement('spirit:parameter')
        base.appendChild(self.mkName('OFFSET_BASE_PARAM'))
        value = self.doc.createElement('spirit:value')
        self.setAttribute(value, 'spirit:id',
                          "ADDRBLOCKPARAM_VALUE." + name + "_REG.OFFSET_BASE_PARAM")
        self.setText(value, 'C_' + name + '_BASEADDR')
        base.appendChild(value)
        return base

    def mkMemoryMapParameterHigh(self, name):
        high = self.doc.createElement('spirit:parameter')
        high.appendChild(self.mkName('OFFSET_HIGH_PARAM'))
        value = self.doc.createElement('spirit:value')
        self.setAttribute(value, 'spirit:id',
                          "ADDRBLOCKPARAM_VALUE." + name + "_REG.OFFSET_HIGH_PARAM")
        self.setText(value, 'C_' + name + '_HIGHADDR')
        high.appendChild(value)
        return high

    def mkMemoryMapRegister(self, obj):
        if hasattr(obj, 'register') and isinstance(obj.register, (tuple, list)):
            length = len(obj.register)
        else:
            length = None

        if length is None:
            return None

        name = obj.name

        register = self.doc.createElement('spirit:register')
        register.appendChild(self.mkName(name + '_control_reg'))
        register.appendChild(self.mkTextNode('spirit:displayName', name + '_control_reg'))
        register.appendChild(self.mkTextNode('spirit:displayName', name + '_control_reg'))

        offset = self.doc.createElement('spirit:addressOffset')
        self.setText(offset, 0)
        register.appendChild(offset)

        size = self.doc.createElement('spirit:size')
        self.setAttribute(size, 'spirit:format', "long")
        self.setText(size, length)
        register.appendChild(size)

        register.appendChild(self.mkTextNode('spirit:access', 'read-write'))

        reset = self.doc.createElement('spirit:reset')
        value = self.doc.createElement('spirit:value')
        self.setAttribute(value, 'spirit:format', "long")
        self.setText(value, 0)
        reset.appendChild(value)
        register.appendChild(reset)

        for i in range(length):
            field = self.doc.createElement('spirit:field')
            field.appendChild(self.mkName(name + '_control_reg%d' % i))
            field.appendChild(self.mkTextNode('spirit:description', name + '_control_reg%d' % i))
            field.appendChild(self.mkTextNode('spirit:bitOffset', 0))
            field.appendChild(self.mkTextNode('spirit:access', 'read-write'))
            register.appendChild(field)

        return register

    def mkModel(self):
        model = self.doc.createElement('spirit:model')
        model.appendChild(self.mkViews())
        model.appendChild(self.mkPorts())
#        model.appendChild(self.mkModelParameters())
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
#        views.appendChild(self.mkView('xilinx_softwaredriver'
#                                      'Software Driver',
#                                      'Verilog Simulation',
#                                      ':vivado.xilinx.com:sw.driver',
#                                      None,
#                                      None,
#                                      'xilinx_softwaredriver_view_fileset'))
        views.appendChild(self.mkView('xilinx_xpgui',
                                      'UI Layout',
                                      ':vivado.xilinx.com:xgui.ui',
                                      None,
                                      None,
                                      'xilinx_xpgui_view_fileset'))
        views.appendChild(self.mkView('bd_tcl',
                                      'Block Diagram',
                                      ':vivado.xilinx.com:block.diagram',
                                      None,
                                      None,
                                      'bd_tcl_view_fileset'))
        return views

    def mkView(self, name, displayname, envidentifier, language, modelname, localname):
        view = self.doc.createElement('spirit:view')
        view.appendChild(self.mkName(name))
        view.appendChild(self.mkTextNode('spirit:displayName', displayname))
        view.appendChild(self.mkTextNode(
            'spirit:envIdentifier', envidentifier))

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

        for bus_interface in self.bus_interfaces:
            for p in self.mkPortBus(bus_interface):
                ports.appendChild(p)

        for portname, port in self.ext_ports.items():
            ports.appendChild(self.mkPortSignal(port))

        return ports

    def mkPortBus(self, obj):
        lite = is_lite(obj)
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

        ret = []
        for port in portlist:
            ret.append(self.mkPortBusSignal(obj, port))

        return ret

    def mkPortBusSignal(self, obj, attr):
        base = obj.name

        if hasattr(obj.waddr, attr.lower()):
            name = getattr(obj.waddr, attr.lower()).name
            var = obj.m[name]
        elif hasattr(obj.wdata, attr.lower()):
            name = getattr(obj.wdata, attr.lower()).name
            var = obj.m[name]
        elif hasattr(obj.wresp, attr.lower()):
            name = getattr(obj.wresp, attr.lower()).name
            var = obj.m[name]
        elif hasattr(obj.raddr, attr.lower()):
            name = getattr(obj.raddr, attr.lower()).name
            var = obj.m[name]
        elif hasattr(obj.rdata, attr.lower()):
            name = getattr(obj.rdata, attr.lower()).name
            var = obj.m[name]
        else:
            raise NameError("No such attribute '%s' in object '%s'" %
                            (attr.lower(), obj))

        direction = ('in' if obj.m.is_input(name) else
                     'out' if obj.m.is_output(name) else
                     'inout')

        width = self.resolved_m[name].width
        h = width - 1 if width is not None else None
        l = 0 if h is not None else None

        return self.mkPortEntry(name, direction,
                                None, h, None, l)

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

#    def mkModelParameters(self):
#        modelparameters = self.doc.createElement('spirit:modelParameters')
#        order = 2
#
#        for paramname, param in self.ext_params.items():
#            p = self.doc.createElement('spirit:modelParameter')
#            p.appendChild(self.mkName(paramname))
#            p.appendChild(self.mkTextNode('spirit:displayName', paramname))
#            p.appendChild(self.mkTextNode('spirit:description', paramname))
#            value = self.doc.createElement('spirit:value')
#            if isinstance(param, vtypes.Integer):
#                self.setAttribute(value, 'spirit:format', 'long')
#            self.setAttribute(value, 'spirit:resolve', 'generated')
#            self.setAttribute(value, 'spirit:id',
#                              "MODELPARAM_VALUE." + paramname)
#            self.setText(value, paramlvalue)
#            p.appendChild(value)
#            modelparameters.appendChild(p)
#
#        return modelparameters

#    def mkModelParameterBus(self, obj, order):
#        lite = is_lite(obj)
#        ret = []
#        name = obj.name
#
#        if not lite:
#            idwidth = self.doc.createElement('spirit:modelParameter')
#            self.setAttribute(idwidth, 'spirit:dataType', "integer")
#            idwidth.appendChild(self.mkName("C_" + name + "_ID_WIDTH"))
#            idwidth.appendChild(self.mkTextNode(
#                'spirit:displayName', "C_" + name + "_ID_WIDTH"))
#            idwidth.appendChild(self.mkTextNode(
#                'spirit:description', "C_" + name + "_ID_WIDTH"))
#            value = self.doc.createElement('spirit:value')
#            self.setAttribute(value, 'spirit:format', 'long')
#            self.setAttribute(value, 'spirit:resolve', 'dependent')
#            self.setAttribute(value, 'spirit:id',
#                              "MODELPARAM_VALUE.C_" + name + "_ID_WIDTH")
#            self.setAttribute(value, 'spirit:dependency',
#                              ("((spirit:decode(id('PARAM_VALUE.C_" + name +
#                               "_ID_WIDTH')) <= 0 ) + (spirit:decode(id('PARAM_VALUE.C_"
#                               + name + "_ID_WIDTH'))))"))
#            self.setAttribute(value, 'spirit:order', order)
#            self.setAttribute(value, 'spirit:minimum', "0")
#            self.setAttribute(value, 'spirit:maximum', "32")
#            self.setAttribute(value, 'spirit:rangeType', "long")
#            self.setText(value, 1)
#            idwidth.appendChild(value)
#            ret.append(idwidth)
#            order += 1
#
#        addrwidth = self.doc.createElement('spirit:modelParameter')
#        self.setAttribute(addrwidth, 'spirit:dataType', "integer")
#        addrwidth.appendChild(self.mkName("C_" + name + "_ADDR_WIDTH"))
#        addrwidth.appendChild(self.mkTextNode(
#            'spirit:displayName', "C_" + name + "_ADDR_WIDTH"))
#        addrwidth.appendChild(self.mkTextNode(
#            'spirit:description', "C_" + name + "_ADDR_WIDTH"))
#        value = self.doc.createElement('spirit:value')
#        self.setAttribute(value, 'spirit:format', 'long')
#        self.setAttribute(value, 'spirit:resolve', 'generated')
#        self.setAttribute(value, 'spirit:id',
#                          "MODELPARAM_VALUE.C_" + name + "_ADDR_WIDTH")
#        self.setAttribute(value, 'spirit:order', order)
#        self.setAttribute(value, 'spirit:rangeType', "long")
#        self.setText(value, obj.addrwidth)
#        addrwidth.appendChild(value)
#        ret.append(addrwidth)
#        order += 1
#
#        datawidth = self.doc.createElement('spirit:modelParameter')
#        self.setAttribute(datawidth, 'spirit:dataType', "integer")
#        datawidth.appendChild(self.mkName("C_" + name + "_DATA_WIDTH"))
#        datawidth.appendChild(self.mkTextNode(
#            'spirit:displayName', "C_" + name + "_DATA_WIDTH"))
#        datawidth.appendChild(self.mkTextNode(
#            'spirit:description', "C_" + name + "_DATA_WIDTH"))
#        value = self.doc.createElement('spirit:value')
#        self.setAttribute(value, 'spirit:format', 'long')
#        self.setAttribute(value, 'spirit:resolve', 'generated')
#        self.setAttribute(value, 'spirit:id',
#                          "MODELPARAM_VALUE.C_" + name + "_DATA_WIDTH")
#        self.setAttribute(value, 'spirit:order', order)
#        self.setAttribute(value, 'spirit:rangeType', "long")
#        self.setText(value, obj.datawidth)
#        datawidth.appendChild(value)
#        ret.append(datawidth)
#        order += 1
#
#        if not lite:
#            awuserwidth = self.doc.createElement('spirit:modelParameter')
#            self.setAttribute(awuserwidth, 'spirit:dataType', "integer")
#            awuserwidth.appendChild(self.mkName("C_" + name + "_AWUSER_WIDTH"))
#            awuserwidth.appendChild(self.mkTextNode(
#                'spirit:displayName', "C_" + name + "_AWUSER_WIDTH"))
#            awuserwidth.appendChild(self.mkTextNode(
#                'spirit:description', "C_" + name + "_AWUSER_WIDTH"))
#            value = self.doc.createElement('spirit:value')
#            self.setAttribute(value, 'spirit:format', 'long')
#            self.setAttribute(value, 'spirit:resolve', 'dependent')
#            self.setAttribute(value, 'spirit:id',
#                              "MODELPARAM_VALUE.C_" + name + "_AWUSER_WIDTH")
#            self.setAttribute(value, 'spirit:dependency',
#                              ("((spirit:decode(id('PARAM_VALUE.C_" + name +
#                               "_AWUSER_WIDTH')) <= 0 ) + (spirit:decode(id('PARAM_VALUE.C_"
#                               + name + "_AWUSER_WIDTH'))))"))
#            self.setAttribute(value, 'spirit:order', order)
#            self.setAttribute(value, 'spirit:minimum', "0")
#            self.setAttribute(value, 'spirit:maximum', "1024")
#            self.setAttribute(value, 'spirit:rangeType', "long")
#            self.setText(value, 1)
#            awuserwidth.appendChild(value)
#            ret.append(awuserwidth)
#            order += 1
#
#        if not lite:
#            aruserwidth = self.doc.createElement('spirit:modelParameter')
#            self.setAttribute(aruserwidth, 'spirit:dataType', "integer")
#            aruserwidth.appendChild(self.mkName("C_" + name + "_ARUSER_WIDTH"))
#            aruserwidth.appendChild(self.mkTextNode(
#                'spirit:displayName', "C_" + name + "_ARUSER_WIDTH"))
#            aruserwidth.appendChild(self.mkTextNode(
#                'spirit:description', "C_" + name + "_ARUSER_WIDTH"))
#            value = self.doc.createElement('spirit:value')
#            self.setAttribute(value, 'spirit:format', 'long')
#            self.setAttribute(value, 'spirit:resolve', 'dependent')
#            self.setAttribute(value, 'spirit:id',
#                              "MODELPARAM_VALUE.C_" + name + "_ARUSER_WIDTH")
#            self.setAttribute(value, 'spirit:dependency',
#                              ("((spirit:decode(id('PARAM_VALUE.C_" + name +
#                               "_ARUSER_WIDTH')) <= 0 ) + (spirit:decode(id('PARAM_VALUE.C_"
#                               + name + "_ARUSER_WIDTH'))))"))
#            self.setAttribute(value, 'spirit:order', order)
#            self.setAttribute(value, 'spirit:minimum', "0")
#            self.setAttribute(value, 'spirit:maximum', "1024")
#            self.setAttribute(value, 'spirit:rangeType', "long")
#            self.setText(value, 1)
#            aruserwidth.appendChild(value)
#            ret.append(aruserwidth)
#            order += 1
#
#        if not lite:
#            wuserwidth = self.doc.createElement('spirit:modelParameter')
#            self.setAttribute(wuserwidth, 'spirit:dataType', "integer")
#            wuserwidth.appendChild(self.mkName("C_" + name + "_WUSER_WIDTH"))
#            wuserwidth.appendChild(self.mkTextNode(
#                'spirit:displayName', "C_" + name + "_WUSER_WIDTH"))
#            wuserwidth.appendChild(self.mkTextNode(
#                'spirit:description', "C_" + name + "_WUSER_WIDTH"))
#            value = self.doc.createElement('spirit:value')
#            self.setAttribute(value, 'spirit:format', 'long')
#            self.setAttribute(value, 'spirit:resolve', 'dependent')
#            self.setAttribute(value, 'spirit:id',
#                              "MODELPARAM_VALUE.C_" + name + "_WUSER_WIDTH")
#            self.setAttribute(value, 'spirit:dependency',
#                              ("((spirit:decode(id('PARAM_VALUE.C_" + name +
#                               "_WUSER_WIDTH')) <= 0 ) + (spirit:decode(id('PARAM_VALUE.C_"
#                               + name + "_WUSER_WIDTH'))))"))
#            self.setAttribute(value, 'spirit:order', order)
#            self.setAttribute(value, 'spirit:minimum', "0")
#            self.setAttribute(value, 'spirit:maximum', "1024")
#            self.setAttribute(value, 'spirit:rangeType', "long")
#            self.setText(value, 1)
#            wuserwidth.appendChild(value)
#            ret.append(wuserwidth)
#            order += 1
#
#        if not lite:
#            ruserwidth = self.doc.createElement('spirit:modelParameter')
#            self.setAttribute(ruserwidth, 'spirit:dataType', "integer")
#            ruserwidth.appendChild(self.mkName("C_" + name + "_RUSER_WIDTH"))
#            ruserwidth.appendChild(self.mkTextNode(
#                'spirit:displayName', "C_" + name + "_RUSER_WIDTH"))
#            ruserwidth.appendChild(self.mkTextNode(
#                'spirit:description', "C_" + name + "_RUSER_WIDTH"))
#            value = self.doc.createElement('spirit:value')
#            self.setAttribute(value, 'spirit:format', 'long')
#            self.setAttribute(value, 'spirit:resolve', 'dependent')
#            self.setAttribute(value, 'spirit:id',
#                              "MODELPARAM_VALUE.C_" + name + "_RUSER_WIDTH")
#            self.setAttribute(value, 'spirit:dependency',
#                              ("((spirit:decode(id('PARAM_VALUE.C_" + name +
#                               "_RUSER_WIDTH')) <= 0 ) + (spirit:decode(id('PARAM_VALUE.C_"
#                               + name + "_RUSER_WIDTH'))))"))
#            self.setAttribute(value, 'spirit:order', order)
#            self.setAttribute(value, 'spirit:minimum', "0")
#            self.setAttribute(value, 'spirit:maximum', "1024")
#            self.setAttribute(value, 'spirit:rangeType', "long")
#            self.setText(value, 1)
#            ruserwidth.appendChild(value)
#            ret.append(ruserwidth)
#            order += 1
#
#        if not lite:
#            buserwidth = self.doc.createElement('spirit:modelParameter')
#            self.setAttribute(buserwidth, 'spirit:dataType', "integer")
#            buserwidth.appendChild(self.mkName("C_" + name + "_BUSER_WIDTH"))
#            buserwidth.appendChild(self.mkTextNode(
#                'spirit:displayName', "C_" + name + "_BUSER_WIDTH"))
#            buserwidth.appendChild(self.mkTextNode(
#                'spirit:description', "C_" + name + "_BUSER_WIDTH"))
#            value = self.doc.createElement('spirit:value')
#            self.setAttribute(value, 'spirit:format', 'long')
#            self.setAttribute(value, 'spirit:resolve', 'dependent')
#            self.setAttribute(value, 'spirit:id',
#                              "MODELPARAM_VALUE.C_" + name + "_BUSER_WIDTH")
#            self.setAttribute(value, 'spirit:dependency',
#                              ("((spirit:decode(id('PARAM_VALUE.C_" + name +
#                               "_BUSER_WIDTH')) <= 0 ) + (spirit:decode(id('PARAM_VALUE.C_"
#                               + name + "_BUSER_WIDTH'))))"))
#            self.setAttribute(value, 'spirit:order', order)
#            self.setAttribute(value, 'spirit:minimum', "0")
#            self.setAttribute(value, 'spirit:maximum', "1024")
#            self.setAttribute(value, 'spirit:rangeType', "long")
#            self.setText(value, 1)
#            buserwidth.appendChild(value)
#            ret.append(buserwidth)
#            order += 1
#
#        return order, ret

#    def mkChoices(self):
#        choices = self.doc.createElement('spirit:choices')
#        choices.appendChild(self.mkChoice(
#            'choices_0', (32, 64, 128, 256, 512)))
#
#        choices_1 = self.doc.createElement('spirit:choice')
#        choices_1.appendChild(self.mkName('choices_1'))
#        choices_1_true = self.doc.createElement('spirit:enumeration')
#        self.setAttribute(choices_1_true, 'spirit:text', 'true')
#        self.setText(choices_1_true, 1)
#        choices_1_false = self.doc.createElement('spirit:enumeration')
#        self.setAttribute(choices_1_false, 'spirit:text', 'false')
#        self.setText(choices_1_false, 0)
#        choices_1.appendChild(choices_1_true)
#        choices_1.appendChild(choices_1_false)
#        choices.appendChild(choices_1)
#
#        choices.appendChild(self.mkChoice(
#            'choices_2', (32, 64, 128, 256, 512)))
#
#        choices_3 = self.doc.createElement('spirit:choice')
#        choices_3.appendChild(self.mkName('choices_3'))
#        choices_3_true = self.doc.createElement('spirit:enumeration')
#        self.setAttribute(choices_3_true, 'spirit:text', 'true')
#        self.setText(choices_3_true, 1)
#        choices_3_false = self.doc.createElement('spirit:enumeration')
#        self.setAttribute(choices_3_false, 'spirit:text', 'false')
#        self.setText(choices_3_false, 0)
#        choices_3.appendChild(choices_3_true)
#        choices_3.appendChild(choices_3_false)
#        choices.appendChild(choices_3)
#
#        choices.appendChild(self.mkChoice(
#            'choices_4', (1, 2, 4, 8, 16, 32, 64, 128, 256, 512)))
#        choices.appendChild(self.mkChoice(
#            'choices_5', (1, 2, 4, 8, 16, 32, 64, 128, 256, 512)))
#
#        return choices

#    def mkChoice(self, name, arg):
#        choice = self.doc.createElement('spirit:choice')
#        choice.appendChild(self.mkName(name))
#        for a in arg:
#            choice.appendChild(self.mkTextNode('spirit:enumeration', a))
#        return choice

    def mkFileSets(self):
        filesets = self.doc.createElement('spirit:fileSets')
        source = self.doc.createElement('spirit:fileSet')
        source.appendChild(self.mkName("xilinx_verilogsynthesis_view_fileset"))
        source.appendChild(self.mkFileSet('hdl/verilog/' + self.ip_name + '.v',
                                          'verilogSource'))
        filesets.appendChild(source)

        sim = self.doc.createElement('spirit:fileSet')
        sim.appendChild(self.mkName(
            "xilinx_verilogbehavioralsimulation_view_fileset"))
        sim.appendChild(self.mkFileSet('hdl/verilog/' + self.ip_name + '.v',
                                       'verilogSource'))
        sim.appendChild(self.mkFileSet('test/test_' + self.ip_name + '.v',
                                       'verilogSource'))
        filesets.appendChild(sim)

        xguitcl = self.doc.createElement('spirit:fileSet')
        xguitcl.appendChild(self.mkName("xilinx_xpgui_view_fileset"))
        xguitcl.appendChild(self.mkFileSet('xgui/xgui.tcl',
                                           'tclSource', 'XGUI_VERSION_2'))
        filesets.appendChild(xguitcl)

        bdtcl = self.doc.createElement('spirit:fileSet')
        bdtcl.appendChild(self.mkName("bd_tcl_view_fileset"))
        bdtcl.appendChild(self.mkFileSet('bd/bd.tcl', 'tclSource'))
        filesets.appendChild(bdtcl)

        xdc = self.doc.createElement('spirit:fileSet')
        xdc.appendChild(self.mkName(
            "xilinx_synthesisconstraints_view_fileset"))
        xdc.appendChild(self.mkFileSet('data/' + self.ip_name + '.xdc',
                                       None, 'xdc'))
        filesets.appendChild(xdc)

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

#        order = 2
#        for memory in self.bus_interfaces:
#            order, rslt = self.mkParameter(memory, order)
#            for p in rslt:
#                parameters.appendChild(p)
#
#        for paramname, paramlvalue, paramtype in self.ext_params:
#            p = self.doc.createElement('spirit:parameter')
#            p.appendChild(self.mkName(paramname))
#            p.appendChild(self.mkTextNode('spirit:displayName', paramname))
#            p.appendChild(self.mkTextNode('spirit:description', paramname))
#            value = self.doc.createElement('spirit:value')
#            if paramtype == 'integer':
#                self.setAttribute(value, 'spirit:format', 'long')
#            self.setAttribute(value, 'spirit:resolve', 'user')
#            self.setAttribute(value, 'spirit:id', "PARAM_VALUE." + paramname)
#            self.setText(value, paramlvalue)
#            p.appendChild(value)
#            parameters.appendChild(p)

        return parameters

#    def mkParameter(self, obj, order):
#        lite = is_lite(obj)
#        ret = []
#        name = obj.name
#
#        if not lite:
#            idwidth = self.doc.createElement('spirit:parameter')
#            idwidth.appendChild(self.mkName("C_" + name + "_ID_WIDTH"))
#            idwidth.appendChild(self.mkTextNode(
#                'spirit:displayName', "C_" + name + "_ID_WIDTH"))
#            idwidth.appendChild(self.mkTextNode(
#                'spirit:description', "C_" + name + "_ID_WIDTH"))
#            value = self.doc.createElement('spirit:value')
#            self.setAttribute(value, 'spirit:format', 'long')
#            self.setAttribute(value, 'spirit:resolve', 'user')
#            self.setAttribute(value, 'spirit:id',
#                              "PARAM_VALUE.C_" + name + "_ID_WIDTH")
#            self.setAttribute(value, 'spirit:dependency',
#                              ("((spirit:decode(id('PARAM_VALUE.C_" + name +
#                               "_ID_WIDTH')) <= 0 ) + (spirit:decode(id('PARAM_VALUE.C_"
#                               + name + "_ID_WIDTH'))))"))
#            self.setAttribute(value, 'spirit:order', order)
#            self.setAttribute(value, 'spirit:minimum', "0")
#            self.setAttribute(value, 'spirit:maximum', "32")
#            self.setAttribute(value, 'spirit:rangeType', "long")
#            self.setText(value, 1)
#            idwidth.appendChild(value)
#            ret.append(idwidth)
#            order += 1
#
#        addrwidth = self.doc.createElement('spirit:parameter')
#        addrwidth.appendChild(self.mkName("C_" + name + "_ADDR_WIDTH"))
#        addrwidth.appendChild(self.mkTextNode(
#            'spirit:displayName', "C_" + name + "_ADDR_WIDTH"))
#        addrwidth.appendChild(self.mkTextNode(
#            'spirit:description', "C_" + name + "_ADDR_WIDTH"))
#        value = self.doc.createElement('spirit:value')
#        self.setAttribute(value, 'spirit:format', 'long')
#        self.setAttribute(value, 'spirit:resolve', 'user')
#        self.setAttribute(value, 'spirit:id',
#                          "PARAM_VALUE.C_" + name + "_ADDR_WIDTH")
#        self.setAttribute(value, 'spirit:order', order)
#        self.setAttribute(value, 'spirit:rangeType', "long")
#        self.setText(value, obj.addrwidth)
#        addrwidth.appendChild(value)
#        extensions = self.doc.createElement('spirit:vendorExtensions')
#        parameterinfo = self.doc.createElement('xilinx:parameterInfo')
#        enablement = self.doc.createElement('xilinx:enablement')
#        enablement.appendChild(self.mkTextNode('xilinx:isEnabled', 'false'))
#        parameterinfo.appendChild(enablement)
#        extensions.appendChild(parameterinfo)
#        addrwidth.appendChild(extensions)
#        ret.append(addrwidth)
#        order += 1
#
#        datawidth = self.doc.createElement('spirit:parameter')
#        datawidth.appendChild(self.mkName("C_" + name + "_DATA_WIDTH"))
#        datawidth.appendChild(self.mkTextNode(
#            'spirit:displayName', "C_" + name + "_DATA_WIDTH"))
#        datawidth.appendChild(self.mkTextNode(
#            'spirit:description', "C_" + name + "_DATA_WIDTH"))
#        value = self.doc.createElement('spirit:value')
#        self.setAttribute(value, 'spirit:format', 'long')
#        self.setAttribute(value, 'spirit:resolve', 'user')
#        self.setAttribute(value, 'spirit:id',
#                          "PARAM_VALUE.C_" + name + "_DATA_WIDTH")
#        self.setAttribute(value, 'spirit:order', order)
#        self.setAttribute(value, 'spirit:rangeType', "long")
#        self.setText(value, obj.datawidth)
#        datawidth.appendChild(value)
#        extensions = self.doc.createElement('spirit:vendorExtensions')
#        parameterinfo = self.doc.createElement('xilinx:parameterInfo')
#        enablement = self.doc.createElement('xilinx:enablement')
#        enablement.appendChild(self.mkTextNode('xilinx:isEnabled', 'false'))
#        parameterinfo.appendChild(enablement)
#        extensions.appendChild(parameterinfo)
#        datawidth.appendChild(extensions)
#        ret.append(datawidth)
#        order += 1
#
#        if not lite:
#            awuserwidth = self.doc.createElement('spirit:parameter')
#            awuserwidth.appendChild(self.mkName("C_" + name + "_AWUSER_WIDTH"))
#            awuserwidth.appendChild(self.mkTextNode(
#                'spirit:displayName', "C_" + name + "_AWUSER_WIDTH"))
#            awuserwidth.appendChild(self.mkTextNode(
#                'spirit:description', "C_" + name + "_AWUSER_WIDTH"))
#            value = self.doc.createElement('spirit:value')
#            self.setAttribute(value, 'spirit:format', 'long')
#            self.setAttribute(value, 'spirit:resolve', 'dependent')
#            self.setAttribute(value, 'spirit:id',
#                              "PARAM_VALUE.C_" + name + "_AWUSER_WIDTH")
#            self.setAttribute(value, 'spirit:dependency',
#                              ("((spirit:decode(id('PARAM_VALUE.C_" + name +
#                               "_AWUSER_WIDTH')) <= 0 ) + (spirit:decode(id('PARAM_VALUE.C_"
#                               + name + "_AWUSER_WIDTH'))))"))
#            self.setAttribute(value, 'spirit:order', order)
#            self.setAttribute(value, 'spirit:minimum', "0")
#            self.setAttribute(value, 'spirit:maximum', "1024")
#            self.setAttribute(value, 'spirit:rangeType', "long")
#            self.setText(value, 0)
#            awuserwidth.appendChild(value)
#            ret.append(awuserwidth)
#            order += 1
#
#        if not lite:
#            aruserwidth = self.doc.createElement('spirit:parameter')
#            aruserwidth.appendChild(self.mkName("C_" + name + "_ARUSER_WIDTH"))
#            aruserwidth.appendChild(self.mkTextNode(
#                'spirit:displayName', "C_" + name + "_ARUSER_WIDTH"))
#            aruserwidth.appendChild(self.mkTextNode(
#                'spirit:description', "C_" + name + "_ARUSER_WIDTH"))
#            value = self.doc.createElement('spirit:value')
#            self.setAttribute(value, 'spirit:format', 'long')
#            self.setAttribute(value, 'spirit:resolve', 'dependent')
#            self.setAttribute(value, 'spirit:id',
#                              "PARAM_VALUE.C_" + name + "_ARUSER_WIDTH")
#            self.setAttribute(value, 'spirit:dependency',
#                              ("((spirit:decode(id('PARAM_VALUE.C_" + name +
#                               "_ARUSER_WIDTH')) <= 0 ) + (spirit:decode(id('PARAM_VALUE.C_"
#                               + name + "_ARUSER_WIDTH'))))"))
#            self.setAttribute(value, 'spirit:order', order)
#            self.setAttribute(value, 'spirit:minimum', "0")
#            self.setAttribute(value, 'spirit:maximum', "1024")
#            self.setAttribute(value, 'spirit:rangeType', "long")
#            self.setText(value, 0)
#            aruserwidth.appendChild(value)
#            ret.append(aruserwidth)
#            order += 1
#
#        if not lite:
#            wuserwidth = self.doc.createElement('spirit:parameter')
#            wuserwidth.appendChild(self.mkName("C_" + name + "_WUSER_WIDTH"))
#            wuserwidth.appendChild(self.mkTextNode(
#                'spirit:displayName', "C_" + name + "_WUSER_WIDTH"))
#            wuserwidth.appendChild(self.mkTextNode(
#                'spirit:description', "C_" + name + "_WUSER_WIDTH"))
#            value = self.doc.createElement('spirit:value')
#            self.setAttribute(value, 'spirit:format', 'long')
#            self.setAttribute(value, 'spirit:resolve', 'dependent')
#            self.setAttribute(value, 'spirit:id',
#                              "PARAM_VALUE.C_" + name + "_WUSER_WIDTH")
#            self.setAttribute(value, 'spirit:dependency',
#                              ("((spirit:decode(id('PARAM_VALUE.C_" + name +
#                               "_WUSER_WIDTH')) <= 0 ) + (spirit:decode(id('PARAM_VALUE.C_"
#                               + name + "_WUSER_WIDTH'))))"))
#            self.setAttribute(value, 'spirit:order', order)
#            self.setAttribute(value, 'spirit:minimum', "0")
#            self.setAttribute(value, 'spirit:maximum', "1024")
#            self.setAttribute(value, 'spirit:rangeType', "long")
#            self.setText(value, 0)
#            wuserwidth.appendChild(value)
#            ret.append(wuserwidth)
#            order += 1
#
#        if not lite:
#            ruserwidth = self.doc.createElement('spirit:parameter')
#            ruserwidth.appendChild(self.mkName("C_" + name + "_RUSER_WIDTH"))
#            ruserwidth.appendChild(self.mkTextNode(
#                'spirit:displayName', "C_" + name + "_RUSER_WIDTH"))
#            ruserwidth.appendChild(self.mkTextNode(
#                'spirit:description', "C_" + name + "_RUSER_WIDTH"))
#            value = self.doc.createElement('spirit:value')
#            self.setAttribute(value, 'spirit:format', 'long')
#            self.setAttribute(value, 'spirit:resolve', 'dependent')
#            self.setAttribute(value, 'spirit:id',
#                              "PARAM_VALUE.C_" + name + "_RUSER_WIDTH")
#            self.setAttribute(value, 'spirit:dependency',
#                              ("((spirit:decode(id('PARAM_VALUE.C_" + name +
#                               "_RUSER_WIDTH')) <= 0 ) + (spirit:decode(id('PARAM_VALUE.C_"
#                               + name + "_RUSER_WIDTH'))))"))
#            self.setAttribute(value, 'spirit:order', order)
#            self.setAttribute(value, 'spirit:minimum', "0")
#            self.setAttribute(value, 'spirit:maximum', "1024")
#            self.setAttribute(value, 'spirit:rangeType', "long")
#            self.setText(value, 0)
#            ruserwidth.appendChild(value)
#            ret.append(ruserwidth)
#            order += 1
#
#        if not lite:
#            buserwidth = self.doc.createElement('spirit:parameter')
#            buserwidth.appendChild(self.mkName("C_" + name + "_BUSER_WIDTH"))
#            buserwidth.appendChild(self.mkTextNode(
#                'spirit:displayName', "C_" + name + "_BUSER_WIDTH"))
#            buserwidth.appendChild(self.mkTextNode(
#                'spirit:description', "C_" + name + "_BUSER_WIDTH"))
#            value = self.doc.createElement('spirit:value')
#            self.setAttribute(value, 'spirit:format', 'long')
#            self.setAttribute(value, 'spirit:resolve', 'dependent')
#            self.setAttribute(value, 'spirit:id',
#                              "PARAM_VALUE.C_" + name + "_BUSER_WIDTH")
#            self.setAttribute(value, 'spirit:dependency',
#                              ("((spirit:decode(id('PARAM_VALUE.C_" + name +
#                               "_BUSER_WIDTH')) <= 0 ) + (spirit:decode(id('PARAM_VALUE.C_"
#                               + name + "_BUSER_WIDTH'))))"))
#            self.setAttribute(value, 'spirit:order', order)
#            self.setAttribute(value, 'spirit:minimum', "0")
#            self.setAttribute(value, 'spirit:maximum', "1024")
#            self.setAttribute(value, 'spirit:rangeType', "long")
#            self.setText(value, 0)
#            buserwidth.appendChild(value)
#            ret.append(buserwidth)
#            order += 1
#
#        return order, ret

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

        # Zynq
        family = self.doc.createElement('xilinx:family')
        self.setAttribute(family, 'xilinx:lifeCycle', 'Production')
        self.setText(family, 'zynq')
        supported.appendChild(family)

        # Zynq Ultrascale+
        family = self.doc.createElement('xilinx:family')
        self.setAttribute(family, 'xilinx:lifeCycle', 'Production')
        self.setText(family, 'zynquplus')
        supported.appendChild(family)

        coreextensions.appendChild(supported)
        taxonomies = self.doc.createElement('xilinx:taxonomies')
        taxonomies.appendChild(self.mkTextNode('xilinx:taxonomy', 'AXI_Peripheral'))
        coreextensions.appendChild(taxonomies)
        coreextensions.appendChild(
            self.mkTextNode('xilinx:displayName',
                            (self.ip_name + '_v' + self.version.replace('.', '_'))))

#        coreextensions.appendChild(self.mkTextNode('xilinx:coreRevison', 1))
#        now = datetime.datetime.now()
#        dt = now.strftime("%Y-%m-%d") # '2015-03-08T02:16:15Z'
#        coreextensions.appendChild(self.mkTextNode('xilinx:coreCreationDateTime', dt))

        return coreextensions


def is_master(obj):
    return isinstance(obj, (axi.AxiMaster, axi.AxiLiteMaster))


def is_lite(obj):
    return isinstance(obj, (axi.AxiLiteMaster, axi.AxiLiteSlave))
