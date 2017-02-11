from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import thread_call_embedded_function

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
    $dumpfile("uut.vcd");
    $dumpvars(0, uut);
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
    #10000;
    $finish;
  end


endmodule



module blinkled
(
  input CLK,
  input RST
);

  reg [8-1:0] data;
  reg enable;
  wire ready;
  assign ready = 1;
  reg [32-1:0] fsm;
  localparam fsm_init = 0;
  reg [32-1:0] _thread_fsm_times_0;
  reg [32-1:0] _thread_fsm_i_1;
  localparam fsm_1 = 1;
  localparam fsm_2 = 2;
  localparam fsm_3 = 3;
  localparam fsm_4 = 4;
  localparam fsm_5 = 5;
  localparam fsm_6 = 6;
  localparam fsm_7 = 7;

  always @(posedge CLK) begin
    if(RST) begin
      fsm <= fsm_init;
      data <= 0;
      enable <= 0;
    end else begin
      case(fsm)
        fsm_init: begin
          _thread_fsm_times_0 <= 10;
          fsm <= fsm_1;
        end
        fsm_1: begin
          _thread_fsm_i_1 <= 0;
          fsm <= fsm_2;
        end
        fsm_2: begin
          if(_thread_fsm_i_1 < _thread_fsm_times_0) begin
            fsm <= fsm_3;
          end else begin
            fsm <= fsm_7;
          end
        end
        fsm_3: begin
          data <= _thread_fsm_i_1;
          enable <= 1;
          fsm <= fsm_4;
        end
        fsm_4: begin
          enable <= 0;
          fsm <= fsm_5;
        end
        fsm_5: begin
          if(ready) begin
            fsm <= fsm_6;
          end 
        end
        fsm_6: begin
          _thread_fsm_i_1 <= _thread_fsm_i_1 + 1;
          fsm <= fsm_2;
        end
      endcase
    end
  end


endmodule
"""


def test():
    veriloggen.reset()
    test_module = thread_call_embedded_function.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
