from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import seq_countup_cat

expected_verilog = """
module test #
(
  parameter INTERVAL = 16
)
(

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

  reg [4-1:0] count0;
  reg [4-1:0] count1;
  localparam [4-1:0] _tmp_0 = (0 >> 0) & { 4{ 1'd1 } };

  always @(posedge CLK) begin
    if(RST) begin
      { count0, count1[3:0] } <= { 4'd0, _tmp_0 };
      LED <= 0;
    end else begin
      $display("LED:%d count0:%d count1:%d", LED, count0, count1);
      if({ count0, count1 } < INTERVAL - 1) begin
        { count0, count1[3:0] } <= { count0, count1 } + 1;
      end 
      if({ count0, count1 } == INTERVAL - 1) begin
        { count0, count1[3:0] } <= 0;
      end 
      if({ count0, count1 } == INTERVAL - 1) begin
        LED <= LED + 1;
      end 
    end
  end


endmodule
"""


def test():
    veriloggen.reset()
    test_module = seq_countup_cat.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
