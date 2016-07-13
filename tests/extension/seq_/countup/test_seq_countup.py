from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import seq_countup

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
def test():
    veriloggen.reset()
    test_module = seq_countup.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
