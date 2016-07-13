from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import seq_countup_if_elif_delayed

expected_verilog = """
module test #
(
  parameter INTERVAL = 32
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
  parameter INTERVAL = 32
)
(
  input CLK,
  input RST,
  output reg [8-1:0] LED
);

  reg [32-1:0] count;
  reg _tmp_0;
  reg test0;
  reg _seq_cond_0_1;
  reg _seq_cond_1_1;
  reg _seq_cond_1_2;
  reg test1;
  reg _seq_cond_2_1;
  reg _seq_cond_3_1;
  reg _seq_cond_3_2;

  always @(posedge CLK) begin
    if(RST) begin
      count <= 0;
      LED <= 0;
      _seq_cond_0_1 <= 0;
      test0 <= 0;
      _seq_cond_1_1 <= 0;
      _seq_cond_1_2 <= 0;
      test1 <= 0;
      _seq_cond_2_1 <= 0;
      _seq_cond_3_1 <= 0;
      _seq_cond_3_2 <= 0;
    end else begin
      if(_seq_cond_1_2) begin
        test0 <= 0;
      end 
      if(_seq_cond_3_2) begin
        test1 <= 1;
      end 
      if(_seq_cond_0_1) begin
        test0 <= 1;
      end 
      _seq_cond_1_2 <= _seq_cond_1_1;
      if(_seq_cond_2_1) begin
        test1 <= 0;
      end 
      _seq_cond_3_2 <= _seq_cond_3_1;
      $display("LED:%d count:%d", LED, count);
      if(count < INTERVAL - 1) begin
        count <= count + 1;
      end else begin
        count <= 0;
        LED <= LED + 1;
      end
      _seq_cond_0_1 <= count == 9;
      _seq_cond_1_1 <= !(count == 9) && (count == 10);
      if(!(count == 9) && !(count == 10) && (count == 15)) begin
        test0 <= 1;
      end 
      if(count == 12) begin
        test1 <= 1;
      end 
      _seq_cond_2_1 <= !(count == 12) && (count == 13);
      _seq_cond_3_1 <= !(count == 12) && !(count == 13) && (count == 14);
    end
  end


endmodule
"""

def test():
    veriloggen.reset()
    test_module = seq_countup_if_elif_delayed.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
