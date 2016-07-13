from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import resolver_bram

expected_verilog = """
module main #
(
  parameter DATA_WIDTH = 32,
  parameter ADDR_WIDTH = 14
)
(
  input CLK,
  input RST
);

  reg [14-1:0] bram_addr0;
  reg [32-1:0] bram_din0;
  reg bram_we0;
  wire [32-1:0] bram_dout0;
  reg [14-1:0] bram_addr1;
  reg [32-1:0] bram_din1;
  reg bram_we1;
  wire [32-1:0] bram_dout1;

  BRAM2
  #(
    .DATA_WIDTH(32),
    .ADDR_WIDTH(14)
  )
  bram_inst
  (
    .CLK(CLK),
    .ADDR0(bram_addr0),
    .DIN0(bram_din0),
    .WE0(bram_we0),
    .DOUT0(bram_dout0),
    .ADDR1(bram_addr1),
    .DIN1(bram_din1),
    .WE1(bram_we1),
    .DOUT1(bram_dout1)
  );

  reg [32-1:0] fsm;
  localparam fsm_init = 0;
  reg [32-1:0] count;
  localparam fsm_1 = 1;
  localparam fsm_2 = 2;

  always @(posedge CLK) begin
    if(RST) begin
      fsm <= 0;
      count <= 0;
    end else begin
      case(fsm)
        0: begin
          bram_addr0 <= 0;
          bram_din0 <= 0;
          bram_we0 <= 0;
          bram_addr1 <= 0;
          bram_din1 <= 0;
          bram_we1 <= 0;
          fsm <= 1;
        end
        1: begin
          bram_addr0 <= count + 0;
          bram_din0 <= count;
          bram_we0 <= 1;
          count <= count + 1;
          bram_addr1 <= count + 64;
          bram_din1 <= count;
          bram_we1 <= 1;
          count <= count + 1;
          if(count == 63) begin
            fsm <= 2;
          end 
        end
      endcase
    end
  end


endmodule



module BRAM2 #
(
  parameter DATA_WIDTH = 32,
  parameter ADDR_WIDTH = 14
)
(
  input CLK,
  input [14-1:0] ADDR0,
  input [32-1:0] DIN0,
  input WE0,
  output [32-1:0] DOUT0,
  input [14-1:0] ADDR1,
  input [32-1:0] DIN1,
  input WE1,
  output [32-1:0] DOUT1
);

  reg [14-1:0] delay_ADDR0;
  reg [14-1:0] delay_ADDR1;
  reg [32-1:0] mem [0:16384-1];

  always @(posedge CLK) begin
    if(WE0) begin
      mem[ADDR0] <= DIN0;
    end 
    delay_ADDR0 <= ADDR0;
  end

  assign DOUT0 = mem[delay_ADDR0];

  always @(posedge CLK) begin
    if(WE1) begin
      mem[ADDR1] <= DIN1;
    end 
    delay_ADDR1 <= ADDR1;
  end

  assign DOUT1 = mem[delay_ADDR1];

endmodule
"""

def test():
    veriloggen.reset()
    test_module = resolver_bram.mkOrig()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
