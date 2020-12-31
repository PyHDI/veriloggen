from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import like

expected_verilog = """
module blinkled #
 (
  parameter WIDTH = 8,
  parameter [32-1:0] WIDTH1 = 8
 )
 (
  input CLK, 
  input RST, 
  output reg [WIDTH-1:0] LED,
  output reg [32-1:0] count,
  output [32-1:0] input_count,
  output [32-1:0] output_count
 );

  localparam [32-1:0] WIDTH2 = 8;
  localparam [32-1:0] _tmp_0 = 8;

  wire [32-1:0] wire_count;
  reg [32-1:0] reg_count;
  wire [32-1:0] _tmp_1;
  reg [32-1:0] _tmp_2;

  assign wire_count = input_count;
  assign output_count = reg_count;

  always @(posedge CLK) begin
    if(RST) begin
      reg_count <= 8;
    end else begin
      reg_count <= wire_count;
    end
  end

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
"""


def test():
    veriloggen.reset()
    test_module = like.mkLed()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
