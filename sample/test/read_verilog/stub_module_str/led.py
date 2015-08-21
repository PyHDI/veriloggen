import sys
import os
import collections

from veriloggen import *

led_v = '''
module blinkled #
  (
   parameter WIDTH = 8
  )
  (
   input CLK, 
   input RST, 
   output reg [WIDTH-1:0] LED
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
'''

def mkLed():
    stubs = read_verilog_stubmodule_str(led_v)
    m = stubs['blinkled']
    return m

def mkTop():
    m = Module('top')
    width = m.Parameter('WIDTH', 8)
    clk = m.Input('CLK')
    rst = m.Input('RST')
    led = m.Output('LED', width)
    
    params = ( width, )
    ports = ( clk, rst, led )
    
    m.Instance(mkLed(), 'inst_blinkled', params, ports)

    return m

if __name__ == '__main__':
    top_module = mkTop()
    top_code = top_module.to_verilog()
    print(top_code)
