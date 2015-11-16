from __future__ import absolute_import
from __future__ import print_function
import lib_dataflow_acc_add_validready

expected_verilog = """
module test;
  reg CLK;
  reg RST;
  reg [32-1:0] x;
  reg vx;
  wire rx;
  wire [32-1:0] y;
  wire vy;
  reg ry;
  reg prst;

  blinkled
  uut
  (
    .CLK(CLK),
    .RST(RST),
    .x(x),
    .vx(vx),
    .rx(rx),
    .y(y),
    .vy(vy),
    .ry(ry),
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
    ry = 0;
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
  reg [32-1:0] _tmp_1;
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
          if(rx) begin
            x <= (x + 1);
          end 
          if(rx) begin
            _tmp_0 <= (_tmp_0 + 1);
          end 
          if(((_tmp_0 == 10) && rx)) begin
            xfsm <= xfsm_2;
          end 
        end
        xfsm_2: begin
          vx <= 0;
        end
      endcase
    end
  end

  reg [32-1:0] yfsm;
  localparam yfsm_init = 0;
  localparam yfsm_1 = 1;
  localparam yfsm_2 = 2;
  localparam yfsm_3 = 3;
  localparam yfsm_4 = 4;
  localparam yfsm_5 = 5;
  localparam yfsm_6 = 6;
  localparam yfsm_7 = 7;
  localparam yfsm_8 = 8;
  localparam yfsm_9 = 9;
  localparam yfsm_10 = 10;
  localparam yfsm_11 = 11;
  localparam yfsm_12 = 12;
  localparam yfsm_13 = 13;

  always @(posedge CLK) begin
    if(RST) begin
      yfsm <= yfsm_init;
    end else begin
      case(yfsm)
        yfsm_init: begin
          ry <= 0;
          if(reset_done) begin
            yfsm <= yfsm_1;
          end 
        end
        yfsm_1: begin
          yfsm <= yfsm_2;
        end
        yfsm_2: begin
          if(vy) begin
            ry <= 1;
          end 
          if(vy) begin
            yfsm <= yfsm_3;
          end 
        end
        yfsm_3: begin
          ry <= 0;
          yfsm <= yfsm_4;
        end
        yfsm_4: begin
          ry <= 0;
          yfsm <= yfsm_5;
        end
        yfsm_5: begin
          ry <= 0;
          yfsm <= yfsm_6;
        end
        yfsm_6: begin
          ry <= 0;
          yfsm <= yfsm_7;
        end
        yfsm_7: begin
          ry <= 0;
          yfsm <= yfsm_8;
        end
        yfsm_8: begin
          ry <= 0;
          yfsm <= yfsm_9;
        end
        yfsm_9: begin
          ry <= 0;
          yfsm <= yfsm_10;
        end
        yfsm_10: begin
          ry <= 0;
          yfsm <= yfsm_11;
        end
        yfsm_11: begin
          ry <= 0;
          yfsm <= yfsm_12;
        end
        yfsm_12: begin
          ry <= 0;
          yfsm <= yfsm_13;
        end
        yfsm_13: begin
          yfsm <= yfsm_2;
        end
      endcase
    end
  end


  always @(posedge CLK) begin
    if(reset_done) begin
      if((vx && rx)) begin
        $display("x=%d", x);
      end 
      if((vy && ry)) begin
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
  output rx,
  output [32-1:0] y,
  output vy,
  input ry,
  input prst
);

  assign rx = (_df_ready_0 || (!_df_valid_0));
  reg [32-1:0] _df_data_0;
  reg _df_valid_0;
  wire _df_ready_0;
  assign _df_ready_0 = (_df_ready_1 || (!_df_valid_1));
  reg [32-1:0] _df_data_1;
  reg _df_valid_1;
  wire _df_ready_1;
  assign _df_ready_1 = ry;
  assign y = _df_data_1;
  assign vy = _df_valid_1;

  always @(posedge CLK) begin
    if(RST) begin
      _df_data_0 <= 0;
      _df_valid_0 <= 0;
      _df_data_1 <= 0;
      _df_valid_1 <= 0;
    end else begin
      if(((vx && rx) && (_df_ready_0 || (!_df_valid_0)))) begin
        _df_data_0 <= (_df_data_0 + x);
      end 
      if((_df_ready_0 || (!_df_valid_0))) begin
        _df_valid_0 <= (vx && rx);
      end 
      if(prst) begin
        _df_data_0 <= 0;
      end 
      if(prst) begin
        _df_valid_0 <= 0;
      end 
      if(((_df_valid_0 && _df_ready_0) && (_df_ready_1 || (!_df_valid_1)))) begin
        _df_data_1 <= _df_data_0;
      end 
      if((_df_ready_1 || (!_df_valid_1))) begin
        _df_valid_1 <= (_df_valid_0 && _df_ready_0);
      end 
    end
  end

endmodule
"""

def test():
    test_module = lib_dataflow_acc_add_validready.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
