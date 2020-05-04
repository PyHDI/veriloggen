from __future__ import absolute_import
from __future__ import print_function
import collections
import veriloggen.core.module as module
import veriloggen.core.vtypes as vtypes
import veriloggen.verilog.from_verilog as from_verilog
from veriloggen.core.collect_visitor import CollectVisitor


class Submodule(vtypes.VeriloggenNode):
    """ Sub-module wrapper """

    def __init__(self, parent, child,
                 name=None, prefix=None,
                 arg_params=None, arg_ports=None,
                 as_io=None, as_wire=None, topmodule=None):

        self.parent = parent

        # child module definition as Verilog HDL source code text
        if isinstance(child, str):
            modules = from_verilog.read_verilog_module_str(child)
            if topmodule is None:
                child = list(modules.values())[0]
            else:
                child = modules[topmodule]

        self.child = child

        if name is None:
            name = child.name

        self.name = name

        if prefix is None:
            prefix = '_'.join((name, ''))

        self.prefix = prefix

        child_params = child.get_params()
        child_ports = child.get_ports()

        if arg_params is None:
            arg_params = []
        elif not isinstance(arg_params, (dict, list, tuple)):
            arg_params = [arg_params]

        if (isinstance(arg_params, (tuple, list)) and
            len(arg_params) >= 1 and
            (not isinstance(arg_params[0], (tuple, list)) or
             len(arg_params[0]) == 1)):  # nonamed argument
            arg_params = [(cport, pport)
                          for cport, pport in zip(child_params.keys(), arg_params)]

        if not isinstance(arg_params, dict):
            arg_params = collections.OrderedDict(arg_params)

        if arg_ports is None:
            arg_ports = []
        elif not isinstance(arg_ports, (dict, list, tuple)):
            arg_ports = [arg_ports]

        if (isinstance(arg_ports, (tuple, list)) and
            len(arg_ports) >= 1 and
            (not isinstance(arg_ports[0], (tuple, list)) or
             len(arg_ports[0]) == 1)):  # nonamed argument
            arg_ports = [(cport, pport)
                         for cport, pport in zip(child_ports.keys(), arg_ports)]

        if not isinstance(arg_ports, dict):
            arg_ports = collections.OrderedDict(arg_ports)

        if as_io is None:
            as_io = ()

        if not isinstance(as_io, (tuple, list)):
            as_io = (as_io,)

        if as_wire is None:
            as_wire = ()

        if not isinstance(as_wire, (tuple, list)):
            as_wire = (as_wire,)

        as_io = [v.name if not isinstance(v, str) else
                 v for v in as_io]
        as_wire = [v.name if not isinstance(v, str) else
                   v for v in as_wire]

        # collect used parameters and localparameters
        collect_visitor = CollectVisitor()

        for port in child_ports.values():
            collect_visitor.visit(port)

        used_params = collect_visitor.names

        # params
        new_params = collections.OrderedDict()

        if arg_params:
            new_params.update(
                parent.copy_params_as_localparams(child, self.prefix,
                                                  include=arg_params.keys(),
                                                  use_fullmatch=True))

        # localparams
        # used ones only
        new_localparams = collections.OrderedDict()
        if used_params:
            new_localparams.update(
                parent.copy_params_as_localparams(child, self.prefix,
                                                  include=used_params,
                                                  exclude=arg_params.keys(),
                                                  use_fullmatch=True))
            new_localparams.update(
                parent.copy_localparams(child, self.prefix, include=used_params,
                                        use_fullmatch=True))

        # overwrite the parameter value by parameter arg
        for key, param in arg_params.items():
            new_key = ''.join([self.prefix, key])
            new_param = new_params[new_key]
            new_param.value = param

        # ports
        new_ports = collections.OrderedDict()
        if as_io:
            new_ports.update(
                parent.copy_ports(child, self.prefix, include=as_io,
                                  use_fullmatch=True))

        exclude = []
        exclude.extend(arg_ports.keys())
        exclude.extend(as_io)
        exclude.extend(as_wire)

        new_ports.update(
            parent.copy_ports_as_vars(child, self.prefix, exclude=exclude,
                                      use_fullmatch=True))

        if as_wire:
            new_ports.update(
                parent.copy_ports_as_vars(child, self.prefix, include=as_wire,
                                          use_wire=True, use_fullmatch=True))

        # for instance args
        self.all_params = collections.OrderedDict()
        self.all_raw_params = collections.OrderedDict()

        for key in child_params.keys():
            new_key = ''.join((self.prefix, key))
            if new_key in new_params:
                self.all_params[key] = new_params[new_key]
                self.all_raw_params[new_key] = new_params[new_key]

        self.all_ports = collections.OrderedDict()
        self.all_raw_ports = collections.OrderedDict()

        for key in child_ports.keys():
            new_key = ''.join((self.prefix, key))
            if key in arg_ports:
                self.all_ports[key] = arg_ports[key]
                self.all_raw_ports[new_key] = arg_ports[key]
            elif new_key in new_ports:
                self.all_ports[key] = new_ports[new_key]
                self.all_raw_ports[new_key] = new_ports[new_key]

        # instance
        self.inst = parent.Instance(child, self.name,
                                    self.all_params, self.all_ports)

    def get_raw_inst_params(self):
        return self.all_raw_params

    def get_raw_inst_ports(self):
        return self.all_raw_ports

    def get_inst_params(self):
        return self.all_params

    def get_inst_ports(self):
        return self.all_ports

    def __getitem__(self, key):
        if key in self.all_params:
            return self.all_params[key]

        if key in self.all_ports:
            return self.all_ports[key]

        raise KeyError("'%s' submodule has no item '%s'" % (self.name, key))

    def __getattr__(self, attr):
        try:
            return vtypes.VeriloggenNode.__getattr__(self, attr)

        except AttributeError as e:

            if attr not in self.all_params and attr not in self.all_ports:
                raise e

            return self.__getitem__(attr)
