from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import seq_as_module_array


expected_verilog = """
module test #
(
  parameter INTERVAL = 8,
  parameter LENGTH = 8
);

  reg CLK;
  reg RST;
  wire [8-1:0] LED;

  blinkled
  #(
    .INTERVAL(INTERVAL),
    .LENGTH(LENGTH)
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
  parameter INTERVAL = 8,
  parameter LENGTH = 8
)
(
  input CLK,
  input RST,
  output reg [8-1:0] LED
);

  reg [32-1:0] count;
  reg [32-1:0] array [0:LENGTH-1];
  wire [32*LENGTH-1:0] _seq_array_0;
  genvar i_1;

  generate for(i_1=0; i_1<LENGTH; i_1=i_1+1) begin
    assign _seq_array_0[(i_1+1)*32-1:i_1*32] = array[i_1];
  end
  endgenerate

  wire [32-1:0] _seq_count_2;

  always @(*) begin
    count = _seq_count_2;
  end

  wire [8-1:0] _seq_LED_3;

  always @(*) begin
    LED = _seq_LED_3;
  end

  localparam _seq_INTERVAL = INTERVAL;
  localparam _seq_LENGTH = LENGTH;

  seq
  #(
    .INTERVAL(_seq_INTERVAL),
    .LENGTH(_seq_LENGTH)
  )
  inst_seq
  (
    .CLK(CLK),
    .RST(RST),
    .i_LED(LED),
    .i_count(count),
    .i_array_line(_seq_array_0),
    .count(_seq_count_2),
    .LED(_seq_LED_3)
  );


endmodule



module seq #
(
  parameter INTERVAL = 8,
  parameter LENGTH = 8
)
(
  input CLK,
  input RST,
  input [8-1:0] i_LED,
  input [32-1:0] i_count,
  input [LENGTH*32-1:0] i_array_line,
  output reg [32-1:0] count,
  output reg [8-1:0] LED
);

  wire [32-1:0] i_array [0:LENGTH-1];
  genvar i_0;

  generate for(i_0=0; i_0<LENGTH; i_0=i_0+1) begin
    assign i_array[i_0] = i_array_line[(i_0+1)*32-1:i_0*32];
  end
  endgenerate


  always @(posedge CLK) begin
    if(RST) begin
      count <= 0;
      LED <= 0;
    end else begin
      $display("LED:%d count:%d", i_LED, i_count);
      if(i_count < INTERVAL - 1) begin
        count <= i_count + 1 + i_array[i_count];
      end 
      if(i_count == INTERVAL - 1) begin
        count <= 0;
      end 
      if(i_count == INTERVAL - 1) begin
        LED <= i_LED + 1;
      end 
    end
  end


endmodule
"""


def test():
    veriloggen.reset()
    test_module = seq_as_module_array.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
