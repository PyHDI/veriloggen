import sys
import os

from veriloggen import *

# external function definition
def get_ext():
    ext = Function('ext_inc', 32)
    ext_v = ext.Input('v', 32)
    ext_o = ext.Input('o', 32)
    ext_tmp = ext.Reg('tmp', 32)
    ext.Body(
        ext_tmp(ext_v + ext_o),
        ext(ext_tmp)
    )
    return ext
    
def mkLed():
    m = Module('blinkled')
    width = m.Parameter('WIDTH', 8)
    clk = m.Input('CLK')
    rst = m.Input('RST')
    led = m.OutputReg('LED', width)
    count = m.Reg('count', 32)

    inc = m.Function('inc', width)
    inc_v = inc.Input('v', width)
    inc_o = inc.Input('o', width)
    inc_tmp = inc.Reg('tmp', width)
    inc.Body(
        inc_tmp(inc_v + inc_o),
        inc(inc_tmp)
    )

    # import an external function definition
    m.add_function(get_ext())
    
    m.Always(Posedge(clk))(
        If(rst)(
            count(0)
        ).Else(
            If(count == 1023)(
                count(0)
            ).Else(
                #count( FunctionCall(inc.name, count, 1) + 1 - 1 )
                count( inc.call(count, 1) + 1 - 1 )
            )
        ))
    
    m.Always(Posedge(clk))(
        If(rst)(
            led(1)
        ).Else(
            If(count == 1024 - 1)(
                led[0](led[width-1]),
                led[width-1:1](led[width-2:0])
            )
        ))

    return m

if __name__ == '__main__':
    led_module = mkLed()
    led_code = led_module.to_verilog()
    print(led_code)
