from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import resolver_nested_module

expected_verilog = """
module blinkled #
(
  parameter TOP_WIDTH = 16,
  parameter TOP_INC = 1
)
(
  input CLK,
  input RST,
  output [16-1:0] LED0,
  output [16-1:0] LED1
);


  sub_blinkled
  #(
    .WIDTH(16),
    .INC(2)
  )
  inst_sub_blinkled_0
  (
    .CLK(CLK),
    .RST(RST),
    .LED(LED0)
  );


  sub_blinkled_copy_0
  #(
    .WIDTH(16),
    .INC(3)
  )
  inst_sub_blinkled_1
  (
    .CLK(CLK),
    .RST(RST),
    .LED(LED1)
  );


endmodule



module sub_blinkled #
(
  parameter WIDTH = 8,
  parameter INC = 1
)
(
  input CLK,
  input RST,
  output reg [16-1:0] LED
);

  reg [26-1:0] count;

  always @(posedge CLK) begin
    if(RST) begin
      count <= 0;
    end else begin
      if(count == 1023) begin
        count <= 0;
      end else begin
        count <= count + 2;
      end
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      LED <= 0;
    end else begin
      if(count == 1023) begin
        LED <= LED + 2;
      end 
    end
  end


endmodule



module sub_blinkled_copy_0 #
(
  parameter WIDTH = 8,
  parameter INC = 1
)
(
  input CLK,
  input RST,
  output reg [16-1:0] LED
);

  reg [26-1:0] count;

  always @(posedge CLK) begin
    if(RST) begin
      count <= 0;
    end else begin
      if(count == 1023) begin
        count <= 0;
      end else begin
        count <= count + 3;
      end
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      LED <= 0;
    end else begin
      if(count == 1023) begin
        LED <= LED + 3;
      end 
    end
  end


endmodule
"""

def test():
    veriloggen.reset()
    test_module = resolver_nested_module.mkLed()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
