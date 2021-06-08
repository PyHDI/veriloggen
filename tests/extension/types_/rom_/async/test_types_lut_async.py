from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import types_rom_async

expected_verilog = """
module test;

  reg CLK;
  reg RST;

  main
  uut
  (
    .CLK(CLK),
    .RST(RST)
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
    #100000;
    $finish;
  end


endmodule



module main
(
  input CLK,
  input RST
);

  reg [4-1:0] addr;
  wire [4-1:0] myrom_addr;
  assign myrom_addr = addr;
  wire [8-1:0] myrom_val;

  myrom
  myrom
  (
    .addr(myrom_addr),
    .val(myrom_val)
  );


  always @(posedge CLK) begin
    if(RST) begin
      addr <= 0;
    end else begin
      addr <= addr + 1;
      $display("addr=%d rdata=%d", addr, myrom_val);
    end
  end


endmodule



module myrom
(
  input [4-1:0] addr,
  output reg [8-1:0] val
);


  always @(*) begin
    case(addr)
      0: begin
        val = 0;
      end
      1: begin
        val = 1;
      end
      2: begin
        val = 4;
      end
      3: begin
        val = 9;
      end
      4: begin
        val = 16;
      end
      5: begin
        val = 25;
      end
      6: begin
        val = 36;
      end
      7: begin
        val = 49;
      end
      8: begin
        val = 64;
      end
      9: begin
        val = 81;
      end
      10: begin
        val = 100;
      end
      11: begin
        val = 121;
      end
      12: begin
        val = 144;
      end
      13: begin
        val = 169;
      end
      14: begin
        val = 196;
      end
      15: begin
        val = 225;
      end
    endcase
  end


endmodule
"""


def test():
    veriloggen.reset()
    test_module = types_rom_async.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
