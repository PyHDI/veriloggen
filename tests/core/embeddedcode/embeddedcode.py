from __future__ import absolute_import
from __future__ import print_function
import sys
import os

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

from veriloggen import *


def mkLed():
    m = Module('blinkled')
    clk = m.Input('CLK')
    rst = m.Input('RST')
    led = m.OutputReg('LED', 8, initval=0)

    code = m.EmbeddedCode("""
// Embedded code
reg [31:0] count;
always @(posedge CLK) begin
  if(RST) begin
    count <= 0;
    LED <= 0;
  end else begin
    if(count == 1024 - 1) begin
      count <= 0;
      LED <= LED + 1;
    end else begin
      count <= count + 1;
    end 
  end
end
""")

    return m

if __name__ == '__main__':
    led = mkLed()
    verilog = led.to_verilog()
    print(verilog)
