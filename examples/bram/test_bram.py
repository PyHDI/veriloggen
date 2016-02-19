from __future__ import absolute_import
from __future__ import print_function
import bram

expected_verilog = """
module test
(

);

  reg CLK;
  reg RST;

  main
  uut
  (
    .CLK(CLK),
    .RST(RST)
  );


  initial begin
    $dumpfile("uut.vcd");
    $dumpvars(0, uut, CLK, RST);
  end


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
    #100000;
    $finish;
  end


endmodule



module main
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
      fsm <= fsm_init;
      count <= 0;
    end else begin
      case(fsm)
        fsm_init: begin
          bram_addr0 <= 0;
          bram_din0 <= 0;
          bram_we0 <= 0;
          bram_addr1 <= 0;
          bram_din1 <= 0;
          bram_we1 <= 0;
          fsm <= fsm_1;
        end
        fsm_1: begin
          bram_addr0 <= count + 0;
          bram_din0 <= count;
          bram_we0 <= 1;
          count <= count + 1;
          bram_addr1 <= count + 64;
          bram_din1 <= count;
          bram_we1 <= 1;
          count <= count + 1;
          if(count == 63) begin
            fsm <= fsm_2;
          end 
        end
      endcase
    end
  end


endmodule



module BRAM2
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
    test_module = bram.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
