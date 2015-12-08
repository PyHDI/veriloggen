from __future__ import absolute_import
from __future__ import print_function
import pipeline_single_add_valid

expected_verilog = """
module test;

  reg CLK;
  reg RST;
  reg [32-1:0] x;
  reg vx;
  wire [32-1:0] y;
  wire vy;

  blinkled
  uut
  (
    .CLK(CLK),
    .RST(RST),
    .x(x),
    .vx(vx),
    .y(y),
    .vy(vy)
  );

  reg reset_done;

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
    reset_done = 0;
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
  localparam xfsm_3 = 3;
  localparam xfsm_4 = 4;
  localparam xfsm_5 = 5;
  localparam xfsm_6 = 6;
  localparam xfsm_7 = 7;
  localparam xfsm_8 = 8;
  localparam xfsm_9 = 9;
  localparam xfsm_10 = 10;
  localparam xfsm_11 = 11;
  localparam xfsm_12 = 12;
  localparam xfsm_13 = 13;
  localparam xfsm_14 = 14;
  localparam xfsm_15 = 15;
  localparam xfsm_16 = 16;
  localparam xfsm_17 = 17;
  localparam xfsm_18 = 18;
  localparam xfsm_19 = 19;
  localparam xfsm_20 = 20;
  localparam xfsm_21 = 21;
  localparam xfsm_22 = 22;
  localparam xfsm_23 = 23;
  localparam xfsm_24 = 24;

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
          xfsm <= xfsm_2;
        end
        xfsm_2: begin
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
          xfsm <= xfsm_8;
        end
        xfsm_8: begin
          xfsm <= xfsm_9;
        end
        xfsm_9: begin
          xfsm <= xfsm_10;
        end
        xfsm_10: begin
          xfsm <= xfsm_11;
        end
        xfsm_11: begin
          vx <= 1;
          xfsm <= xfsm_12;
        end
        xfsm_12: begin
          x <= x + 1;
          _tmp_0 <= _tmp_0 + 1;
          if(_tmp_0 == 5) begin
            xfsm <= xfsm_13;
          end 
        end
        xfsm_13: begin
          vx <= 0;
          xfsm <= xfsm_14;
        end
        xfsm_14: begin
          xfsm <= xfsm_15;
        end
        xfsm_15: begin
          xfsm <= xfsm_16;
        end
        xfsm_16: begin
          xfsm <= xfsm_17;
        end
        xfsm_17: begin
          xfsm <= xfsm_18;
        end
        xfsm_18: begin
          xfsm <= xfsm_19;
        end
        xfsm_19: begin
          xfsm <= xfsm_20;
        end
        xfsm_20: begin
          xfsm <= xfsm_21;
        end
        xfsm_21: begin
          xfsm <= xfsm_22;
        end
        xfsm_22: begin
          xfsm <= xfsm_23;
        end
        xfsm_23: begin
          vx <= 1;
          x <= x + 1;
          _tmp_0 <= _tmp_0 + 1;
          if(_tmp_0 == 10) begin
            xfsm <= xfsm_24;
          end 
        end
        xfsm_24: begin
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
  output vy
);

  reg [32-1:0] _df_data_0;
  reg [32-1:0] _df_data_1;
  reg [32-1:0] _df_data_2;
  reg _df_valid_2;
  reg [32-1:0] _df_data_3;
  reg _df_valid_3;
  reg [32-1:0] _df_data_4;
  reg _df_valid_4;
  assign y = _df_data_4;
  assign vy = _df_valid_4;

  always @(posedge CLK) begin
    if(RST) begin
      _df_data_0 <= 0;
      _df_data_1 <= 0;
      _df_data_2 <= 0;
      _df_valid_2 <= 0;
      _df_data_3 <= 0;
      _df_valid_3 <= 0;
      _df_data_4 <= 0;
      _df_valid_4 <= 0;
    end else begin
      if(vx) begin
        _df_data_0 <= x;
      end 
      if(vx) begin
        _df_data_1 <= _df_data_0;
      end 
      if(vx && vx) begin
        _df_data_2 <= _df_data_0 + _df_data_1;
      end 
      _df_valid_2 <= vx && vx;
      if(vx) begin
        _df_data_3 <= x;
      end 
      _df_valid_3 <= vx;
      if(_df_valid_2 && _df_valid_3) begin
        _df_data_4 <= _df_data_2 + _df_data_3;
      end 
      _df_valid_4 <= _df_valid_2 && _df_valid_3;
    end
  end

endmodule
"""

def test():
    test_module = pipeline_single_add_valid.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
