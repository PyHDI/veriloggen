from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import seq_countup_if_then

expected_verilog = """
module test #
(
  parameter INTERVAL = 16
);

  reg CLK;
  reg RST;
  wire [8-1:0] LED;

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
      #5 CLK = !CLK;
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
  output reg [8-1:0] LED
);

  reg [32-1:0] count;
  reg _tmp_0;
  reg updated;
  reg _seq_cond_0_1;
  reg _seq_cond_1_1;
  reg _seq_cond_1_2;

  always @(posedge CLK) begin
    if(RST) begin
      count <= 0;
      LED <= 0;
      _seq_cond_0_1 <= 0;
      updated <= 0;
      _seq_cond_1_1 <= 0;
      _seq_cond_1_2 <= 0;
    end else begin
      if(_seq_cond_1_2) begin
        updated <= 0;
      end 
      if(_seq_cond_0_1) begin
        updated <= 1;
      end 
      _seq_cond_1_2 <= _seq_cond_1_1;
      $display("LED:%d count:%d", LED, count);
      if(count < INTERVAL - 1) begin
        count <= count + 1;
      end else begin
        count <= 0;
        LED <= LED + 1;
      end
      _seq_cond_0_1 <= !(count < INTERVAL - 1);
      _seq_cond_1_1 <= !(count < INTERVAL - 1);
    end
  end


endmodule
"""

def test():
    veriloggen.reset()
    test_module = seq_countup_if_then.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
