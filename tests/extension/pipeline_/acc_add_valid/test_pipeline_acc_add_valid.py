from __future__ import absolute_import
from __future__ import print_function
import pipeline_acc_add_valid

expected_verilog = """
module test;
  reg CLK;
  reg RST;
  reg [32-1:0] x;
  reg vx;
  wire [32-1:0] y;
  wire vy;
  reg prst;

  blinkled
  uut
  (
    .CLK(CLK),
    .RST(RST),
    .x(x),
    .vx(vx),
    .y(y),
    .vy(vy),
    .prst(prst)
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
    prst = 0;
    x = 0;
    vx = 0;
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

  always @(posedge CLK) begin
    if(RST) begin
      xfsm <= xfsm_init;
      _tmp_0 <= 0;
    end else begin
      case(xfsm)
        xfsm_init: begin
          vx <= 0;
          if(reset_done) begin
            xfsm <= xfsm_1;
          end 
        end
        xfsm_1: begin
          vx <= 1;
          x <= (x + 1);
          _tmp_0 <= (_tmp_0 + 1);
          if((_tmp_0 == 10)) begin
            xfsm <= xfsm_2;
          end 
        end
        xfsm_2: begin
          vx <= 0;
        end
      endcase
    end
  end

  always @(posedge CLK) begin
    if(reset_done) begin
      if(vx) begin
        $display("x=%d", x);
      end 
      if(vy) begin
        $display("y=%d", y);
      end 
    end 
  end

endmodule

module blinkled
(
  input CLK,
  input RST,
  input [32-1:0] x,
  input vx,
  output [32-1:0] y,
  output vy,
  input prst
);

  reg [32-1:0] _df_data_0;
  reg _df_valid_0;
  assign y = _df_data_0;
  assign vy = _df_valid_0;

  always @(posedge CLK) begin
    if(RST) begin
      _df_data_0 <= 0;
      _df_valid_0 <= 0;
    end else begin
      if(vx) begin
        _df_data_0 <= _df_data_0 + x;
      end 
      _df_valid_0 <= vx;
      if(prst) begin
        _df_data_0 <= 0;
      end 
      if(prst) begin
        _df_valid_0 <= 0;
      end 
    end
  end

endmodule
"""

def test():
    test_module = pipeline_acc_add_valid.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
