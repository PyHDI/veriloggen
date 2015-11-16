from __future__ import absolute_import
from __future__ import print_function
import simulation_example
from veriloggen import *

expected_verilog = """
module test #
(
  parameter INTERVAL = 16
);

  reg CLK;
  reg RST;
  wire [(8 - 1):0] LED;

  blinkled
  #(
    .INTERVAL(INTERVAL)
  )
  uut
  (
    .CLK(CLK),
    .RST(RST),
    .LED(LED)
  );


  initial begin
    CLK = 0;
    forever begin
      #5 CLK = (!CLK);
    end
  end

  initial begin
    RST = 0;
    #100;
    RST = 1;
    #100;
    RST = 0;
    #1000;
    $finish;
  end
endmodule

module blinkled #
(
  parameter INTERVAL = 16
)
(
  input CLK,
  input RST,
  output reg [(8 - 1):0] LED
);

  reg [(32 - 1):0] count;

  always @(posedge CLK) begin
    if(RST) begin
      count <= 0;
      LED <= 0;
    end else begin
      $display("LED:%d count:%d", LED, count);
      if((count < (INTERVAL - 1))) begin
        count <= (count + 1);
      end 
      if((count == (INTERVAL - 1))) begin
        count <= 0;
      end 
      if((count == (INTERVAL - 1))) begin
        LED <= (LED + 1);
      end 
    end
  end
endmodule
"""

expected_rslt = """\
LED:  x count:         x
LED:  x count:         x
LED:  x count:         x
LED:  x count:         x
LED:  x count:         x
LED:  x count:         x
LED:  x count:         x
LED:  x count:         x
LED:  x count:         x
LED:  x count:         x
LED:  0 count:         0
LED:  0 count:         1
LED:  0 count:         2
LED:  0 count:         3
LED:  0 count:         4
LED:  0 count:         5
LED:  0 count:         6
LED:  0 count:         7
LED:  0 count:         8
LED:  0 count:         9
LED:  0 count:        10
LED:  0 count:        11
LED:  0 count:        12
LED:  0 count:        13
LED:  0 count:        14
LED:  0 count:        15
LED:  1 count:         0
LED:  1 count:         1
LED:  1 count:         2
LED:  1 count:         3
LED:  1 count:         4
LED:  1 count:         5
LED:  1 count:         6
LED:  1 count:         7
LED:  1 count:         8
LED:  1 count:         9
LED:  1 count:        10
LED:  1 count:        11
LED:  1 count:        12
LED:  1 count:        13
LED:  1 count:        14
LED:  1 count:        15
LED:  2 count:         0
LED:  2 count:         1
LED:  2 count:         2
LED:  2 count:         3
LED:  2 count:         4
LED:  2 count:         5
LED:  2 count:         6
LED:  2 count:         7
LED:  2 count:         8
LED:  2 count:         9
LED:  2 count:        10
LED:  2 count:        11
LED:  2 count:        12
LED:  2 count:        13
LED:  2 count:        14
LED:  2 count:        15
LED:  3 count:         0
LED:  3 count:         1
LED:  3 count:         2
LED:  3 count:         3
LED:  3 count:         4
LED:  3 count:         5
LED:  3 count:         6
LED:  3 count:         7
LED:  3 count:         8
LED:  3 count:         9
LED:  3 count:        10
LED:  3 count:        11
LED:  3 count:        12
LED:  3 count:        13
LED:  3 count:        14
LED:  3 count:        15
LED:  4 count:         0
LED:  4 count:         1
LED:  4 count:         2
LED:  4 count:         3
LED:  4 count:         4
LED:  4 count:         5
LED:  4 count:         6
LED:  4 count:         7
LED:  4 count:         8
LED:  4 count:         9
LED:  4 count:        10
LED:  4 count:        11
LED:  4 count:        12
LED:  4 count:        13
LED:  4 count:        14
LED:  4 count:        15
LED:  5 count:         0
LED:  5 count:         1
LED:  5 count:         2
LED:  5 count:         3
LED:  5 count:         4
LED:  5 count:         5
LED:  5 count:         6
LED:  5 count:         7
LED:  5 count:         8
LED:  5 count:         9
LED:  5 count:        10
LED:  5 count:        11
LED:  5 count:        12
LED:  5 count:        13
LED:  5 count:        14
LED:  5 count:        15
LED:  6 count:         0
LED:  6 count:         1
LED:  6 count:         2
LED:  6 count:         3
"""

def test():
    test_module = simulation_example.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)

    sim = lib.simulation.Simulator(test_module)
    rslt = sim.run()

    assert(expected_rslt == rslt)
    
