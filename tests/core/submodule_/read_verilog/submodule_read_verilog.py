from __future__ import absolute_import
from __future__ import print_function
import sys
import os
import collections

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))

from veriloggen import *

verilog_blinkled = """
module blinkled #
(
  parameter WIDTH = 8
)
(
  input CLK,
  input RST,
  output reg [WIDTH-1:0] LED,
  output [WIDTH-1:0] dummy_out0,
  output [WIDTH-1:0] dummy_out1,
  output [WIDTH-1:0] dummy_out2,
  input [WIDTH-1:0] dummy_in0,
  input [WIDTH-1:0] dummy_in1,
  input [WIDTH-1:0] dummy_in2
);

  reg [32-1:0] count;

  always @(posedge CLK) begin
    if(RST) begin
      count <= 0;
    end else begin
      if(count == 1023) begin
        count <= 0;
      end else begin
        count <= count + 1;
      end
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      LED <= 0;
    end else begin
      if(count == 1023) begin
        LED <= LED + 1;
      end 
    end
  end


endmodule
"""


def mkTop():
    m = Module('top')
    width = m.Parameter('WIDTH', 8)
    clk = m.Input('CLK')
    rst = m.Input('RST')
    led = m.Output('LED', width)

    sub = Submodule(m, verilog_blinkled, 'inst_blinkled',
                    arg_params=(('WIDTH', width),),
                    arg_ports=(('LED', led), ('CLK', clk), ('RST', rst)),
                    as_io=('dummy_out0', 'dummy_in0'), as_wire=('dummy_out1', 'dummy_in1'))

    return m

if __name__ == '__main__':
    top = mkTop()
    verilog = top.to_verilog('tmp.v')
    print(verilog)
