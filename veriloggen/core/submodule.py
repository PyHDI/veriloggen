from __future__ import absolute_import
from __future__ import print_function
import collections
import veriloggen.core.module as module
import veriloggen.core.vtypes as vtypes


class Submodule(vtypes.VeriloggenNode):
    """ Sub-module wrapper """

    def __init__(self, parent, child,
                 name=None, prefix=None,
                 arg_params=None, arg_ports=None,
                 as_io=None, as_wire=None):

        self.parent = parent
        self.child = child

        if name is None:
            name = '_'.join(('inst', child.name))
        self.name = name

        if prefix is None:
            prefix = ''
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
        if as_wire is None:
            as_wire = ()

        as_io = [v.name if not isinstance(v, str) else
                 v for v in as_io]
        as_wire = [v.name if not isinstance(v, str) else
                   v for v in as_wire]

        # params
        new_params = collections.OrderedDict()

        param_exclude = []
        param_exclude.extend(arg_params.keys())
        new_params.update(parent.copy_params(
            child, self.prefix, exclude=param_exclude, rename_exclude=param_exclude))

        self.all_params = collections.OrderedDict()
        self.all_raw_params = collections.OrderedDict()

        for key in child_params.keys():
            new_key = ''.join((self.prefix, key))
            if key in arg_params:
                self.all_params[key] = arg_params[key]
                self.all_raw_params[new_key] = arg_params[key]
            elif new_key in new_params:
                self.all_params[key] = new_params[new_key]
                self.all_raw_params[new_key] = new_params[new_key]

        # ports
        new_ports = collections.OrderedDict()
        if as_io:
            new_ports.update(parent.copy_ports(
                child, self.prefix, include=as_io,
                rename_exclude=param_exclude))

        exclude = []
        exclude.extend(arg_ports.keys())
        exclude.extend(as_io)
        exclude.extend(as_wire)

        new_ports.update(parent.copy_ports_as_vars(
            child, self.prefix, exclude=exclude,
            rename_exclude=param_exclude))

        if as_wire:
            new_ports.update(parent.copy_ports_as_vars(
                child, self.prefix, include=as_wire,
                rename_exclude=param_exclude, use_wire=True))

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
        self.inst = parent.Instance(
            child, self.name, self.all_params, self.all_ports)

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
