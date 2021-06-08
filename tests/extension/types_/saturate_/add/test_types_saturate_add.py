from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import types_saturate_add

expected_verilog = """
module test;

  reg uut_CLK;
  reg uut_RST;
  wire [8-1:0] uut_LED;

  blinkled
  uut
  (
    .CLK(uut_CLK),
    .RST(uut_RST),
    .LED(uut_LED)
  );


  initial begin
    uut_CLK = 0;
    forever begin
      #5 uut_CLK = !uut_CLK;
    end
  end


  initial begin
    uut_RST = 0;
    #100;
    uut_RST = 1;
    #100;
    uut_RST = 0;
    #100000;
    $finish;
  end


endmodule



module blinkled
(
  input CLK,
  input RST,
  output reg [8-1:0] LED
);

  reg [10-1:0] count;

  always @(posedge CLK) begin
    if(RST) begin
      count <= 0;
      LED <= 0;
    end else begin
      count <= (count + 1 > 1023)? 1023 : count + 1;
      if(count == 1023) begin
        LED <= (LED + 'sd1 > 255)? 255 : LED + 'sd1;
      end 
      $display("LED:%d count:%d", LED, count);
    end
  end


endmodule
"""


def test():
    veriloggen.reset()
    test_module = types_saturate_add.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
