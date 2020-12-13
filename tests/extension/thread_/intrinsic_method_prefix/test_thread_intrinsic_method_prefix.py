from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import thread_intrinsic_method_prefix

expected_verilog = """
module test;

  reg CLK;
  reg RST;

  blinkled
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
    #10000;
    $finish;
  end


endmodule



module blinkled
(
  input CLK,
  input RST
);

  reg [8-1:0] _tmp_0;
  reg _tmp_1;
  wire _tmp_2;
  assign _tmp_2 = 1;
  reg [32-1:0] th_blink;
  localparam th_blink_init = 0;
  reg signed [32-1:0] _th_blink_times_0;
  reg signed [32-1:0] _th_blink_i_1;
  reg signed [32-1:0] _th_blink_data_2;
  localparam th_blink_1 = 1;
  localparam th_blink_2 = 2;
  localparam th_blink_3 = 3;
  localparam th_blink_4 = 4;
  localparam th_blink_5 = 5;
  localparam th_blink_6 = 6;
  localparam th_blink_7 = 7;
  localparam th_blink_8 = 8;

  always @(posedge CLK) begin
    if(RST) begin
      th_blink <= th_blink_init;
      _th_blink_times_0 <= 0;
      _th_blink_i_1 <= 0;
      _th_blink_data_2 <= 0;
      _tmp_0 <= 0;
      _tmp_1 <= 0;
    end else begin
      case(th_blink)
        th_blink_init: begin
          _th_blink_times_0 <= 10;
          th_blink <= th_blink_1;
        end
        th_blink_1: begin
          _th_blink_i_1 <= 0;
          th_blink <= th_blink_2;
        end
        th_blink_2: begin
          if(_th_blink_i_1 < _th_blink_times_0) begin
            th_blink <= th_blink_3;
          end else begin
            th_blink <= th_blink_8;
          end
        end
        th_blink_3: begin
          _th_blink_data_2 <= _th_blink_i_1 + 100;
          th_blink <= th_blink_4;
        end
        th_blink_4: begin
          _tmp_0 <= _th_blink_data_2;
          _tmp_1 <= 1;
          $display("data = %d", _th_blink_data_2);
          th_blink <= th_blink_5;
        end
        th_blink_5: begin
          _tmp_1 <= 0;
          th_blink <= th_blink_6;
        end
        th_blink_6: begin
          if(_tmp_2) begin
            th_blink <= th_blink_7;
          end 
        end
        th_blink_7: begin
          _th_blink_i_1 <= _th_blink_i_1 + 1;
          th_blink <= th_blink_2;
        end
      endcase
    end
  end


endmodule
"""


def test():
    veriloggen.reset()
    test_module = thread_intrinsic_method_prefix.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
