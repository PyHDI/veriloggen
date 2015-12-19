from __future__ import absolute_import
from __future__ import print_function
import sys
import os

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))

from veriloggen import *

def mkLed():
    m = Module('blinkled')
    width = m.Parameter('WIDTH', 8)
    num_inst = m.Parameter('NUM_INST', 4)
    clk = m.Input('CLK')
    rst = m.Input('RST')
    led = m.OutputReg('LED', width)
    count = m.Reg('count', 32)

    m.Always(Posedge(clk))(
        If(rst)(
            count(0)
        ).Else(
            If(count == 1023)(
                count(0)
            ).Else(
                count(count + 1)
            )
        ))

    # genvar i;
    i = m.Genvar('i')
    
    # generate for(i=0; i<NUM_INST; i=i+1) begin: gen_for;
    gen_for = m.GenerateFor(i(0), i<num_inst, i(i+1), scope='gen_for')
    gen_count = gen_for.Reg('gen_count', 32)
    
    # if(i==0) begin: gen_if_true // generate-if
    gen_if = gen_for.GenerateIf(i == 0, 'gen_if_true')
    gen_if.Always(Posedge(clk))(
        gen_count(count)
    )

    # end else begin // gen_if_false else
    gen_if = gen_if.Else('gen_if_false')
    gen_if_count = gen_if.Reg('gen_if_count', 32)
    gen_if.Always(Posedge(clk))(
        gen_count(Scope(gen_for[i-1], gen_count)),
        gen_if_count(gen_count),
    )
    # ... end endgenerate
    
    m.Always(Posedge(clk))(
        If(rst)(
            led(0)
        ).Else(
            If(Scope(gen_for[num_inst-1], gen_if, gen_if_count) == 1024 - 1)(
                led(led + 1)
            )))
    
    return m

if __name__ == '__main__':
    led = mkLed()
    verilog = led.to_verilog()
    print(verilog)
