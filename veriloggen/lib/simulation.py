from __future__ import absolute_import
from __future__ import print_function
import os
import sys
import subprocess
import tempfile

import veriloggen.vtypes as vtypes
import veriloggen.module as module

def setup_waveform(m, *uuts):
    new_uuts = []
    for u in uuts:
        if isinstance(u, (tuple, list)):
            new_uuts.extend(u)
        elif isinstance(u, dict):
            new_uuts.extend(list(u.values()))
        else:
            new_uuts.append(u)
    uuts = new_uuts
    ret = m.Initial(
        vtypes.Systask('dumpfile', 'uut.vcd'),
        vtypes.Systask('dumpvars', 0, *uuts)
    )
    return ret

def setup_clock(m, clk, hperiod=5):
    ret = m.Initial(
        clk(0),
        vtypes.Forever(clk(vtypes.Not(clk), ldelay=hperiod))
    )
    return ret

def setup_reset(m, reset, *statement, **kwargs):
    period = kwargs['period'] if 'period' in kwargs else 100
    ret = m.Initial(
        reset(0),
        statement,
        vtypes.Delay(100),
        reset(1),
        vtypes.Delay(100),
        reset(0),
    )
    return ret

def next_clock(clk):
    return ( vtypes.Event(vtypes.Posedge(clk)), vtypes.Delay(1) )

def finish():
    return Systask('finish')

#-------------------------------------------------------------------------------
class Simulator(object):
    def __init__(self, *objs, **options):
        sim = 'iverilog' if 'sim' not in options else options['sim']
        wave = 'gtkwave' if 'wave' not in options else options['wave']
        files = None if 'files' not in options else options['files']
        self._type_check_sim(sim)
        self._type_check_wave(wave)
        self.objs = objs
        self.files = files
        self.sim = sim
        self.wave = wave

    def _type_check_sim(self, sim):
        if sim == 'iverilog' or sim == 'icarus':
            return
        if sim == 'vcs':
            raise NotImplementedError("Not implemented: '%s'" % sim)
        raise ValueError("Not supported simulator: '%s'" % sim)
        
    def _type_check_wave(self, wave):
        if wave == 'gtkwave':
            return 
        raise ValueError("Not supported waveform viewer: '%s'" % wave)
        
    def run(self, display=False, outputfile='a.out', include=None, define=None):
        if self.sim == 'iverilog' or self.sim == 'icarus':
            return self._run_iverilog(display, outputfile, include, define)
        raise NotImplementedError("Not implemented: '%s'" % self.sim)

    def _run_iverilog(self, display=False, outputfile='a.out', include=None, define=None):
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
                        cmd.append(''.join([ d[0], '=', str(d[1])]))
                else:
                    cmd.append(d)
                    
        cmd.append('-o')
        cmd.append(outputfile)

        # encoding: 'utf-8' ?
        encode = sys.getdefaultencoding()
        
        code = self._to_code()
        tmp = tempfile.NamedTemporaryFile()
        tmp.write(code.encode(encode))
        tmp.read()
        filename = tmp.name
        
        cmd.append(filename)

        # synthesis
        p = subprocess.Popen(' '.join(cmd), shell=True, stdout=subprocess.PIPE)
        syn_rslt = []
        while True:
            stdout_data = p.stdout.readline()
            syn_rslt.append(stdout_data.decode(encode))
            if display: print(stdout_data, end='')
            if not stdout_data: break
        p.wait()
        p.stdout.close()
        syn_rslt = ''.join(syn_rslt)

        # simulation
        p = subprocess.Popen('./' + outputfile, shell=True, stdout=subprocess.PIPE)
        sim_rslt = []
        while True:
            stdout_data = p.stdout.readline()
            sim_rslt.append(stdout_data.decode(encode))
            if display: print(stdout_data, end='')
            if not stdout_data: break
        p.wait()
        p.stdout.close()
        sim_rslt = ''.join(sim_rslt)

        # close temporal source code file
        tmp.close()
        
        return ''.join([syn_rslt, sim_rslt])

    def _to_code(self):
        code = []
        for obj in self.objs:
            if isinstance(obj, module.Module):
                code.append(obj.to_verilog())
                code.append('\n')
            if isinstance(obj, str):
                code.append(obj)
                code.append('\n')
        return ''.join(code)
    
    def view_waveform(self, filename='uut.vcd', background=False):
        return self._view_waveform_gtkwave(filename, background)

    def _view_waveform_gtkwave(self, filename='uut.vcd', background=False):
        cmd = []
        cmd.append('gtkwave')
        cmd.append('--giga')
        cmd.append(filename)
        if background:
            cmd.append('&')
        subprocess.call(' '.join(cmd), shell=True)
