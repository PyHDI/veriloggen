from __future__ import absolute_import
from __future__ import print_function
import dataflow_single_add

expected_verilog = """
module test;
  reg CLK;
  reg RST;
  reg [32-1:0] x;
  wire [32-1:0] y;

  blinkled
  uut
  (
    .CLK(CLK),
    .RST(RST),
    .x(x),
    .y(y)
  );

  reg reset_done;

  initial begin
    $dumpfile("uut.vcd");
    $dumpvars(0, uut);
  end

  initial begin
    CLK = 0;
    forever begin
      #5 CLK = (!CLK);
    end
  end

  initial begin
    RST = 0;
    reset_done = 0;
    x = 0;
    #100;
    RST = 1;
    #100;
    RST = 0;
    #1000;
    reset_done = 1;
    @(posedge CLK);
    #1;
    #10000;
    $finish;
  end

  reg [32-1:0] _tmp_0;
  reg [32-1:0] xfsm;
  localparam xfsm_init = 0;
  localparam xfsm_1 = 1;
  localparam xfsm_2 = 2;
  localparam xfsm_3 = 3;
  localparam xfsm_4 = 4;
  localparam xfsm_5 = 5;
  localparam xfsm_6 = 6;
  localparam xfsm_7 = 7;

  always @(posedge CLK) begin
    if(RST) begin
      xfsm <= xfsm_init;
      _tmp_0 <= 0;
    end else begin
      case(xfsm)
        xfsm_init: begin
          if(reset_done) begin
            xfsm <= xfsm_1;
          end 
        end
        xfsm_1: begin
          x <= x + 1;
          _tmp_0 <= _tmp_0 + 1;
          if(_tmp_0 == 10) begin
            xfsm <= xfsm_2;
          end 
        end
        xfsm_2: begin
          x <= 0;
          xfsm <= xfsm_3;
        end
        xfsm_3: begin
          xfsm <= xfsm_4;
        end
        xfsm_4: begin
          xfsm <= xfsm_5;
        end
        xfsm_5: begin
          xfsm <= xfsm_6;
        end
        xfsm_6: begin
          xfsm <= xfsm_7;
        end
        xfsm_7: begin
          $finish;
        end
      endcase
    end
  end

  always @(posedge CLK) begin
    if(reset_done) begin
      $display("x=%d", x);
      $display("y=%d", y);
    end 
  end

endmodule

module blinkled
(
  input CLK,
  input RST,
  input [32-1:0] x,
  output [32-1:0] y
);

  reg [32-1:0] _df_data_0;
  reg [32-1:0] _df_data_1;
  reg [32-1:0] _df_data_2;
  reg [32-1:0] _df_data_3;
  reg [32-1:0] _df_data_4;
  assign y = _df_data_4;

  always @(posedge CLK) begin
    if(RST) begin
      _df_data_0 <= 0;
      _df_data_1 <= 0;
      _df_data_2 <= 0;
      _df_data_3 <= 0;
      _df_data_4 <= 0;
    end else begin
      _df_data_0 <= x;
      _df_data_1 <= _df_data_0;
      _df_data_2 <= (_df_data_0 + _df_data_1);
      _df_data_3 <= x;
      _df_data_4 <= (_df_data_2 + _df_data_3);
    end
  end

endmodule
"""

def test():
    test_module = dataflow_single_add.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
