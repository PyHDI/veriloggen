from __future__ import absolute_import
from __future__ import print_function
import sys
import os
import collections

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from veriloggen import *

led_v = '''\
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
    modules = from_verilog.read_verilog_module_str(led_v)
    m = modules['blinkled']
    
    # change the module name
    m.name = 'modified_led'
    
    # add new statements
    enable = m.Input('enable')
    busy = m.Output('busy')

    old_statement = m.always[0].statement[0].false_statement
    m.always[0].statement[0].false_statement = If(enable)(*old_statement)
    m.Assign( busy(m.variable['count'] < 1023) )
    
    return m

if __name__ == '__main__':
    led = mkLed()
    verilog = led.to_verilog()
    print(verilog)
