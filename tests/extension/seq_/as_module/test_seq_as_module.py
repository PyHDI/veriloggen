from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import seq_as_module


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

  reg [32-1:0] count;
  wire [32-1:0] _count_0;
  wire [32-1:0] _tmp_1;
  assign _tmp_1 = _count_0;

  always @(*) begin
    count = _tmp_1;
  end

  wire [8-1:0] _LED_2;
  wire [8-1:0] _tmp_3;
  assign _tmp_3 = _LED_2;

  always @(*) begin
    LED = _tmp_3;
  end

  localparam _seq_in_INTERVAL = INTERVAL;
  wire _seqCLK;
  wire _seqRST;
  wire [8-1:0] _seq_in_LED;
  wire [32-1:0] _seq_in_count;
  wire [32-1:0] _seqcount;
  wire [8-1:0] _seqLED;

  seq
  #(
    ._in_INTERVAL(_seq_in_INTERVAL)
  )
  inst_seq
  (
    .CLK(CLK),
    .RST(RST),
    ._in_LED(LED),
    ._in_count(count),
    .count(_count_0),
    .LED(_LED_2)
  );


endmodule



module seq #
(
  parameter _in_INTERVAL = 16
)
(
  input CLK,
  input RST,
  input [8-1:0] _in_LED,
  input [32-1:0] _in_count,
  output reg [32-1:0] count,
  output reg [8-1:0] LED
);


  always @(posedge CLK) begin
    if(RST) begin
      count <= 0;
      LED <= 0;
    end else begin
      $display("LED:%d count:%d", _in_LED, _in_count);
      if(_in_count < _in_INTERVAL - 1) begin
        count <= _in_count + 1;
      end 
      if(_in_count == _in_INTERVAL - 1) begin
        count <= 0;
      end 
      if(_in_count == _in_INTERVAL - 1) begin
        LED <= _in_LED + 1;
      end 
    end
  end


endmodule
"""

def test():
    veriloggen.reset()
    test_module = seq_as_module.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
