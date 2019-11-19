from __future__ import absolute_import
from __future__ import print_function
import os
import sys
import subprocess
import tempfile
import collections
from jinja2 import Environment, FileSystemLoader
try:
    from math import gcd
except:
    from fractions import gcd

import veriloggen.core.vtypes as vtypes
import veriloggen.core.module as module
import veriloggen.core.submodule as submodule


def setup_waveform(m, *uuts, **kwargs):
    new_uuts = []
    for uut in uuts:
        if isinstance(uut, (tuple, list)):
            for u in uut:
                if isinstance(u, vtypes._Variable) and u.dims is not None:
                    continue
                new_uuts.append(u)
        elif isinstance(uut, dict):
            _uut = list(uut.values())
            for u in _uut:
                if isinstance(u, vtypes._Variable) and u.dims is not None:
                    continue
                new_uuts.append(u)
        elif isinstance(uut, submodule.Submodule):
            new_uuts.append(uut.inst)
        else:
            if isinstance(uut, vtypes._Variable) and uut.dims is not None:
                continue
            new_uuts.append(uut)

    dumpfile = kwargs['dumpfile'] if 'dumpfile' in kwargs else 'uut.vcd'

    uuts = new_uuts
    ret = m.Initial(
        vtypes.Systask('dumpfile', dumpfile),
        vtypes.Systask('dumpvars', 0, *uuts)
    )

    # for verilator
    m.verilator_dumpfile = dumpfile

    return ret


def setup_clock(m, clk, hperiod=5):
    ret = m.Initial(
        clk(0),
        vtypes.Forever(clk(vtypes.Not(clk), ldelay=hperiod))
    )

    # for verilator
    if not hasattr(m, 'verilator_clock'):
        m.verilator_clock = collections.OrderedDict()

    m.verilator_clock[clk] = hperiod

    return ret


def setup_reset(m, reset, *statement, **kwargs):
    period = kwargs['period'] if 'period' in kwargs else 100
    polarity = kwargs['polarity'] if 'polarity' in kwargs else 'high'
    positive = 'high' in polarity.lower()

    ret = m.Initial(
        reset(not positive),
        statement,
        vtypes.Delay(period),
        reset(positive),
        vtypes.Delay(period),
        reset(not positive),
    )

    # for verilator
    if not hasattr(m, 'verilator_reset'):
        m.verilator_reset = collections.OrderedDict()

    m.verilator_reset[reset] = (period, positive)

    if not hasattr(m, 'verilator_reset_statements'):
        m.verilator_reset_statements = collections.OrderedDict()

    if reset not in m.verilator_reset_statements:
        m.verilator_reset_statements[reset] = []

    m.verilator_reset_statements[reset].extend(statement)

    return ret


def next_clock(clk):
    return (vtypes.Event(vtypes.Posedge(clk)), vtypes.Delay(1))


def finish():
    return vtypes.Systask('finish')


def _to_code(objs):
    code = []
    for obj in objs:
        if isinstance(obj, module.Module):
            code.append(obj.to_verilog())
            code.append('\n')
        if isinstance(obj, str):
            code.append(obj)
            code.append('\n')
    return ''.join(code)


def run_iverilog(objs, display=False, top=None, outputfile=None,
                 include=None, define=None, libdir=None):

    if not isinstance(objs, (tuple, list)):
        objs = [objs]

    if top is None:
        top = objs[0]

    top_name = top.name if isinstance(top, module.Module) else top

    if outputfile is None:
        outputfile = 'a.out'

    cmd = []
    cmd.append('iverilog')
    if include:
        for inc in include:
            cmd.append('-I')
            cmd.append(inc)

    if define:
        for d in define:
            cmd.append('-D')
            if isinstance(d, (tuple, list)):
                if d[1] is None:
                    cmd.append(d[0])
                else:
                    cmd.append(''.join([d[0], '=', str(d[1])]))
            else:
                cmd.append(d)

    if libdir:
        for l in libdir:
            cmd.append('-y')
            cmd.append(l)

    cmd.append('-s')
    cmd.append(top_name)

    cmd.append('-o')
    cmd.append(outputfile)

    # encoding: 'utf-8' ?
    encoding = sys.getdefaultencoding()

    code = _to_code(objs)

    if os.name == 'nt':
        fd, path = tempfile.mkstemp()
        os.close(fd)
        tmp = open(path, 'w+b')
    else:
        tmp = tempfile.NamedTemporaryFile()

    tmp.write(code.encode(encoding))
    tmp.read()
    filename = tmp.name

    cmd.append(filename)

    # synthesis
    syn_rslt = _exec(' '.join(cmd), encoding, display)

    # simulation
    cmd = []
    cmd.append('vvp')
    cmd.append(outputfile)
    sim_rslt = _exec(' '.join(cmd), encoding, display)

    # close temporal source code file
    tmp.close()

    if os.name == 'nt':
        os.remove(path)

    return ''.join([syn_rslt, sim_rslt])


def run_vcs(objs, display=False, top=None, outputfile=None,
            include=None, define=None, libdir=None,
            full64=False, notimingcheck=True):

    if not isinstance(objs, (tuple, list)):
        objs = [objs]

    if top is None:
        top = objs[0]

    top_name = top.name if isinstance(top, module.Module) else top

    if outputfile is None:
        outputfile = 'simv'

    cmd = []
    cmd.append('vcs')
    cmd.append('-v2005')

    if full64:
        cmd.append('-full64')

    if notimingcheck:
        cmd.append('+notimingcheck')

    if include:
        for inc in include:
            cmd.append('+incdir+')
            cmd.append(inc)

    if define:
        for d in define:
            cmd.append('+define+')
            if isinstance(d, (tuple, list)):
                if d[1] is None:
                    cmd.append(d[0])
                else:
                    cmd.append(''.join([d[0], '=', str(d[1])]))
            else:
                cmd.append(d)

    if libdir:
        for l in libdir:
            cmd.append('-y')
            cmd.append(l)

    cmd.append('-o')
    cmd.append(outputfile)

    # encoding: 'utf-8' ?
    encoding = sys.getdefaultencoding()

    code = _to_code(objs)

    if os.name == 'nt':
        fd, path = tempfile.mkstemp()
        os.close(fd)
        tmp = open(path, 'w+b')
    else:
        tmp = tempfile.NamedTemporaryFile()

    tmp.write(code.encode(encoding))
    tmp.read()
    filename = tmp.name

    cmd.append(filename)

    # synthesis
    syn_rslt = _exec(' '.join(cmd), encoding, display)

    # simulation
    cmd = []

    if os.name == 'nt':
        cmd.append(outputfile)
    else:
        cmd.append('./' + outputfile)

    sim_rslt = _exec(' '.join(cmd), encoding, display)

    # close temporal source code file
    tmp.close()

    if os.name == 'nt':
        os.remove(path)

    return ''.join([syn_rslt, sim_rslt])


def run_modelsim(objs, display=False, top=None, outputfile=None,
                 include=None, define=None, libdir=None):

    if not isinstance(objs, (tuple, list)):
        objs = [objs]

    if top is None:
        top = objs[0]

    top_name = top.name if isinstance(top, module.Module) else top

    if outputfile is None:
        outputfile = 'a.out'

    cmd = []
    cmd.append('vlib work ; vmap work ; vlog')

    if include:
        for inc in include:
            cmd.append('-I')
            cmd.append(inc)

    if define:
        for d in define:
            cmd.append('-D')
            if isinstance(d, (tuple, list)):
                if d[1] is None:
                    cmd.append(d[0])
                else:
                    cmd.append(''.join([d[0], '=', str(d[1])]))
            else:
                cmd.append(d)

    if libdir:
        for l in libdir:
            cmd.append('-y')
            cmd.append(l)

    # encoding: 'utf-8' ?
    encoding = sys.getdefaultencoding()

    code = _to_code(objs)

    if os.name == 'nt':
        fd, path = tempfile.mkstemp()
        os.close(fd)
        tmp = open(path, 'w+b')
    else:
        tmp = tempfile.NamedTemporaryFile()

    tmp.write(code.encode(encoding))
    tmp.read()
    filename = tmp.name

    cmd.append(filename)

    # synthesis
    syn_rslt = _exec(' '.join(cmd), encoding, display)

    # simulation
    cmd = []
    cmd.append('vsim -c')
    cmd.append(top)
    cmd.append('-do \"run -all\"')
    sim_rslt = _exec(' '.join(cmd), encoding, display)

    # close temporal source code file
    tmp.close()

    if os.name == 'nt':
        os.remove(path)

    return ''.join([syn_rslt, sim_rslt])


def to_verilator_code(top, objs):
    code = []

    if hasattr(top, 'verilator_clock'):
        clks = top.verilator_clock
    else:
        clks = {}

    if hasattr(top, 'verilator_reset'):
        rsts = top.verilator_reset
    else:
        rsts = {}

    if hasattr(top, 'verilator_reset_statements'):
        inits_list = top.verilator_reset_statements
        inits = collections.OrderedDict()
        for init in inits_list:
            if isinstance(init, vtypes.Subst):
                inits[init.left] = init.right
    else:
        inits = {}

    new_clks = collections.OrderedDict()
    for clk, values in clks.items():
        new_clk = top.InputLike(clk, name='io_' + clk.name)
        clk.connect(new_clk)
        new_clks[new_clk] = values

    top.verilator_new_clock = new_clks

    new_rsts = collections.OrderedDict()
    for rst, values in rsts.items():
        new_rst = top.InputLike(rst, name='io_' + rst.name)
        rst.connect(new_rst)
        new_rsts[new_rst] = values

    top.verilator_new_reset = new_rsts

    for obj in objs:
        if isinstance(obj, module.Module):
            code.append(obj.to_verilog(for_verilator=True))
            code.append('\n')
        if isinstance(obj, str):
            code.append(obj)
            code.append('\n')
    return ''.join(code)


def to_verilator_cpp(top, verilog_prefix, sim_time=0):
    template_path = os.path.dirname(os.path.abspath(__file__))
    env = Environment(loader=FileSystemLoader(template_path))
    env.globals['zip'] = zip

    if hasattr(top, 'verilator_dumpfile'):
        dumpfile = top.verilator_dumpfile
    else:
        dumpfile = None

    clks = top.verilator_new_clock
    rsts = top.verilator_new_reset

    if hasattr(top, 'verilator_reset_statements'):
        inits_list = top.verilator_reset_statements
        inits = collections.OrderedDict()
        for init in inits_list:
            if isinstance(init, vtypes.Subst):
                inits[init.left] = init.right
    else:
        inits = {}

    ios = top.get_ports()
    inputs = [io_var for io_var in ios.values()
              if isinstance(io_var, vtypes.Input) and
              (io_var not in clks) and (io_var not in rsts)]

    time_step = None

    for hperiod in clks.values():
        if time_step is None:
            time_step = hperiod
        else:
            time_step = gcd(time_step, hperiod)

    for period, positive in rsts.values():
        if time_step is None:
            time_step = period
        else:
            time_step = gcd(time_step, period)

    if time_step is None:
        time_step = 1

    template_dict = {
        'verilog_prefix': verilog_prefix,
        'sim_time': sim_time,
        'time_step': time_step,
        'dumpfile': dumpfile,
        'clks': clks,
        'rsts': rsts,
        'inits': inits,
        'inputs': inputs,
    }

    template = env.get_template('verilator_template.cpp')
    code = template.render(template_dict)
    return code


def run_verilator(objs, display=False, top=None, outputfile=None,
                  include=None, define=None, libdir=None,
                  sim_time=0, options=None):

    if not isinstance(objs, (tuple, list)):
        objs = [objs]

    if top is None:
        top = objs[0]

    top_name = top.name if isinstance(top, module.Module) else top

    if not isinstance(top, module.Module):
        for obj in objs:
            if obj.name == top_name:
                top = obj
                break

    if not isinstance(top, module.Module):
        raise ValueError('top module must be specified.')

    if outputfile is None:
        outputfile = 'obj_dir'

    cmd = []
    cmd.append('verilator')
    cmd.append('--cc')

    if options is not None:
        if isinstance(options, (tuple, list)):
            options = (options,)
        cmd.append(options)

    if hasattr(top, 'verilator_dumpfile'):
        cmd.append('--trace')
        cmd.append('--trace-underscore')

    # cmd.append('-Wall')
    cmd.append('-Wno-lint')

    if include:
        for inc in include:
            cmd.append('+incdir+')
            cmd.append(inc)

    if define:
        for d in define:
            cmd.append('+define+')
            if isinstance(d, (tuple, list)):
                if d[1] is None:
                    cmd.append(d[0])
                else:
                    cmd.append(''.join([d[0], '=', str(d[1])]))
            else:
                cmd.append(d)

    if libdir:
        for l in libdir:
            cmd.append('-y')
            cmd.append(l)

    cmd.append('--Mdir')
    cmd.append(outputfile)

    verilog_prefix = 'out'
    verilog_name = verilog_prefix + '.v'
    verilog_path = outputfile + '/' + verilog_name
    cmd.append(verilog_path)

    cpp_prefix = 'sim_%s' % top_name
    cpp_name = cpp_prefix + '.cpp'
    cpp_path = outputfile + '/' + cpp_name
    cmd.append('--exe')
    cmd.append(cpp_path)

    to_verilator(top, objs,
                 sim_time, outputfile, verilog_prefix, cpp_prefix)

    # for clk in top.verilator_clock.keys():
    #    cmd.append('--clk')
    #    cmd.append(clk.name)

    # for clk in top.verilator_new_clock.keys():
    #    cmd.append('--clk')
    #    cmd.append(clk.name)

    # encoding: 'utf-8' ?
    encoding = sys.getdefaultencoding()

    # synthesis
    syn_rslt = _exec(' '.join(cmd), encoding, display)

    # make
    make = ['make -C', outputfile, '-j -f',
            'V' + verilog_prefix + '.mk', 'V' + verilog_prefix]
    make_rslt = _exec(' '.join(make), encoding, display)

    # simulation
    cmd = []

    if os.name == 'nt':
        cmd.append(outputfile + '/' + 'V' + verilog_prefix)
    else:
        cmd.append('./' + outputfile + '/' + 'V' + verilog_prefix)

    sim_rslt = _exec(' '.join(cmd), encoding, display)

    # return ''.join([syn_rslt, make_rslt, sim_rslt])
    return sim_rslt


def to_verilator(top, objs,
                 sim_time=0, outputdir='obj_dir',
                 verilog_prefix='out', cpp_prefix='sim'):

    if not os.path.exists(outputdir):
        os.mkdir(outputdir)

    verilog_name = verilog_prefix + '.v'
    verilog_path = outputdir + '/' + verilog_name

    verilog_code = to_verilator_code(top, objs)
    verilog = open(verilog_path, 'w')
    verilog.write(verilog_code)
    verilog.close()

    cpp_name = cpp_prefix + '.cpp'
    cpp_path = outputdir + '/' + cpp_name

    cpp_code = to_verilator_cpp(top, verilog_prefix, sim_time)
    cpp = open(cpp_path, 'w')
    cpp.write(cpp_code)
    cpp.close()


def view_waveform_gtkwave(filename='uut.vcd', background=False):
    cmd = []
    cmd.append('gtkwave')
    cmd.append('--giga')
    cmd.append(filename)
    if background:
        cmd.append('&')
    subprocess.call(' '.join(cmd), shell=True)


class Simulator(object):
    """ obsoleted class """

    def __init__(self, *objs, **options):
        if not objs:
            raise ValueError('no target object')

        sim = 'iverilog' if 'sim' not in options else options['sim'].lower()
        wave = 'gtkwave' if 'wave' not in options else options['wave'].lower()

        # for VCS
        full64 = False if 'full64' not in options else options['full64']
        notimingcheck = True if 'notimingcheck' not in options else options['notimingcheck']

        self.objs = objs
        self.sim = sim
        self.wave = wave

        self.full64 = full64
        self.notimingcheck = notimingcheck

    def run(self, display=False, top=None, outputfile=None,
            include=None, define=None, libdir=None,
            sim_time=0, options=None):

        if include is not None and not isinstance(include, (tuple, list)):
            include = (include,)

        if define is not None and not isinstance(define, (tuple, list)):
            define = (define,)

        if libdir is not None and not isinstance(libdir, (tuple, list)):
            libdir = (libdir,)

        if self.sim == 'iverilog' or self.sim == 'icarus':
            return run_iverilog(self.objs,
                                display, top, outputfile, include, define, libdir)

        if self.sim == 'vcs':
            return run_vcs(self.objs,
                           display, top, outputfile, include, define, libdir,
                           full64=self.full64, notimingcheck=self.notimingcheck)

        if self.sim == 'modelsim' or self.sim == 'vsim':
            return run_modelsim(self.objs,
                                display, top, include, define, libdir)

        if self.sim == 'verilator':
            return run_verilator(self.objs,
                                 display, top, outputfile, include, define, libdir,
                                 sim_time=sim_time, options=options)

        raise NotImplementedError("not supported simulator: '%s'" % self.sim)

    def view_waveform(self, filename='uut.vcd', background=False):
        if self.wave == 'gtkwave':
            return view_waveform_gtkwave(filename, background)

        raise NotImplementedError(
            "not supported waveform viewer: '%s'" % self.wave)


def _exec(cmd, encoding, display=False):
    if display:
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        rslt = []

        while True:
            stdout_data = p.stdout.readline()
            out = stdout_data.decode(encoding)
            rslt.append(out)
            print(out, end='')
            if not stdout_data:
                break

        p.wait()
        p.stdout.close()
        rslt = ''.join(rslt)

    else:
        b = subprocess.check_output(cmd, shell=True)
        rslt = b.decode(encoding)

    return rslt
