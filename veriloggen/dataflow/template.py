from __future__ import absolute_import
from __future__ import print_function

import veriloggen.core.vtypes as vtypes
import veriloggen.core.module as module

def mkMultiplierCore(datawidth=32, depth=6):
    m = module.Module('multiplier_core')
    datawidth = m.Parameter('datawidth', datawidth)
    depth = m.Parameter('depth', depth)
    clk = m.Input('CLK')
    update = m.Input('update')
    a = m.Input('a', datawidth)
    b = m.Input('b', datawidth)
    c = m.Output('c', datawidth*2)
    rslt = m.Wire('rslt', datawidth*2)
    mem = m.Reg('mem', datawidth*2, depth)
    m.Assign( rslt(a * b) )
    m.Assign( c(mem[depth-1]) )
    i = m.Integer('i')
    m.Always(vtypes.Posedge(clk))(
        vtypes.If(update)(
            mem[0](rslt),
            vtypes.For(i(1), i<depth, i.inc())(
                mem[i](mem[i-1])
            )))
    return m

def mkMultiplier(datawidth=32, depth=6):
    if datawidth < 0: raise ValueError("datawidth must be greater than 0.")
    if depth < 0: raise ValueError("depth must be greater than 0.")
    
    mult = mkMultiplierCore(datawidth, depth)
    m = module.Module('multiplier')
    datawidth = m.Parameter('datawidth', datawidth)
    depth = m.Parameter('depth', depth)
    clk = m.Input('CLK')
    rst = m.Input('RST')
    update = m.Input('update')
    enable = m.Input('enable')
    valid = m.Output('valid')
    a = m.Input('a', datawidth)
    b = m.Input('b', datawidth)
    c = m.Output('c', datawidth)
    _c = m.Wire('_c', datawidth*2)
    valid_reg = m.Reg('valid_reg', depth, initval=0)
    m.Assign(c(_c[datawidth-1:0]))
    m.Assign( valid(valid_reg[depth-1]) )
    i = m.Integer('i')
    m.Always(vtypes.Posedge(clk))(
        vtypes.If(rst)(
            valid_reg(0)
        ).Else(
            vtypes.If(update)(
                valid_reg[0](enable),
                vtypes.For(i(1), i<depth, i.inc())(
                    valid_reg[i](valid_reg[i-1])
                ))))
    ports = [ ('CLK', clk), ('update', update), ('a', a), ('b', b), ('c', _c) ]
    m.Instance(mult, 'mult', m.connect_params(mult), ports)
    return m

# global multiplier definition
multiplier = mkMultiplier()
