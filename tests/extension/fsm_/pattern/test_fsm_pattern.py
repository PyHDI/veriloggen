from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import fsm_pattern

expected_verilog = """
module test;

  reg CLK;
  reg RST;
  wire [8-1:0] LED;

  blinkled
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



module blinkled
(
  input CLK,
  input RST,
  output reg [8-1:0] LED
);

  reg [32-1:0] _tmp_0;
  reg [32-1:0] fsm;
  localparam fsm_init = 0;
  localparam fsm_1 = 1;
  localparam fsm_2 = 2;
  localparam fsm_3 = 3;
  localparam fsm_4 = 4;
  localparam fsm_5 = 5;
  localparam fsm_6 = 6;

  always @(posedge CLK) begin
    if(RST) begin
      fsm <= fsm_init;
      LED <= 0;
      _tmp_0 <= 0;
    end else begin
      case(fsm)
        fsm_init: begin
          LED <= 0;
          fsm <= fsm_1;
        end
        fsm_1: begin
          _tmp_0 <= 0;
          fsm <= fsm_2;
        end
        fsm_2: begin
          if(_tmp_0 < 127) begin
            _tmp_0 <= _tmp_0 + 1;
          end 
          if(_tmp_0 == 127) begin
            fsm <= fsm_3;
          end 
        end
        fsm_3: begin
          _tmp_0 <= 0;
          fsm <= fsm_4;
        end
        fsm_4: begin
          if(_tmp_0 < 255) begin
            _tmp_0 <= _tmp_0 + 1;
          end 
          if(_tmp_0 == 255) begin
            fsm <= fsm_5;
          end 
        end
        fsm_5: begin
          LED <= LED + 1;
          fsm <= fsm_6;
        end
        fsm_6: begin
          fsm <= fsm_init;
        end
      endcase
    end
  end


endmodule
"""


def test():
    veriloggen.reset()
    test_module = fsm_pattern.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
