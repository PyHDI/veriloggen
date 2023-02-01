from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import pipeline_unbalanced_output

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
  wire [32-1:0] z;
  wire vz;
  reg rz;

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
    .z(z),
    .vz(vz),
    .rz(rz)
  );

  reg reset_done;

  initial begin
    $dumpfile("pipeline_unbalanced_output.vcd");
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
    ry = 0;
    rz = 0;
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
  reg [32-1:0] _tmp_2;
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
          if(rx) begin
            x <= x + 1;
          end 
          if(rx) begin
            _tmp_0 <= _tmp_0 + 1;
          end 
          if((_tmp_0 == 5) && rx) begin
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
          if(rx) begin
            x <= x + 1;
          end 
          if(rx) begin
            _tmp_0 <= _tmp_0 + 1;
          end 
          if((_tmp_0 == 10) && rx) begin
            xfsm <= xfsm_24;
          end 
        end
        xfsm_24: begin
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
          yfsm <= yfsm_2;
        end
      endcase
    end
  end

  reg [32-1:0] zfsm;
  localparam zfsm_init = 0;
  localparam zfsm_1 = 1;
  localparam zfsm_2 = 2;
  localparam zfsm_3 = 3;
  localparam zfsm_4 = 4;
  localparam zfsm_5 = 5;
  localparam zfsm_6 = 6;
  localparam zfsm_7 = 7;
  localparam zfsm_8 = 8;
  localparam zfsm_9 = 9;
  localparam zfsm_10 = 10;
  localparam zfsm_11 = 11;
  localparam zfsm_12 = 12;
  localparam zfsm_13 = 13;
  localparam zfsm_14 = 14;
  localparam zfsm_15 = 15;
  localparam zfsm_16 = 16;
  localparam zfsm_17 = 17;
  localparam zfsm_18 = 18;
  localparam zfsm_19 = 19;
  localparam zfsm_20 = 20;
  localparam zfsm_21 = 21;
  localparam zfsm_22 = 22;
  localparam zfsm_23 = 23;

  always @(posedge CLK) begin
    if(RST) begin
      zfsm <= zfsm_init;
    end else begin
      case(zfsm)
        zfsm_init: begin
          rz <= 0;
          if(reset_done) begin
            zfsm <= zfsm_1;
          end 
        end
        zfsm_1: begin
          zfsm <= zfsm_2;
        end
        zfsm_2: begin
          if(vz) begin
            rz <= 1;
          end 
          if(vz) begin
            zfsm <= zfsm_3;
          end 
        end
        zfsm_3: begin
          rz <= 0;
          zfsm <= zfsm_4;
        end
        zfsm_4: begin
          rz <= 0;
          zfsm <= zfsm_5;
        end
        zfsm_5: begin
          rz <= 0;
          zfsm <= zfsm_6;
        end
        zfsm_6: begin
          rz <= 0;
          zfsm <= zfsm_7;
        end
        zfsm_7: begin
          rz <= 0;
          zfsm <= zfsm_8;
        end
        zfsm_8: begin
          rz <= 0;
          zfsm <= zfsm_9;
        end
        zfsm_9: begin
          rz <= 0;
          zfsm <= zfsm_10;
        end
        zfsm_10: begin
          rz <= 0;
          zfsm <= zfsm_11;
        end
        zfsm_11: begin
          rz <= 0;
          zfsm <= zfsm_12;
        end
        zfsm_12: begin
          rz <= 0;
          zfsm <= zfsm_13;
        end
        zfsm_13: begin
          rz <= 0;
          zfsm <= zfsm_14;
        end
        zfsm_14: begin
          rz <= 0;
          zfsm <= zfsm_15;
        end
        zfsm_15: begin
          rz <= 0;
          zfsm <= zfsm_16;
        end
        zfsm_16: begin
          rz <= 0;
          zfsm <= zfsm_17;
        end
        zfsm_17: begin
          rz <= 0;
          zfsm <= zfsm_18;
        end
        zfsm_18: begin
          rz <= 0;
          zfsm <= zfsm_19;
        end
        zfsm_19: begin
          rz <= 0;
          zfsm <= zfsm_20;
        end
        zfsm_20: begin
          rz <= 0;
          zfsm <= zfsm_21;
        end
        zfsm_21: begin
          rz <= 0;
          zfsm <= zfsm_22;
        end
        zfsm_22: begin
          rz <= 0;
          zfsm <= zfsm_23;
        end
        zfsm_23: begin
          zfsm <= zfsm_2;
        end
      endcase
    end
  end


  always @(posedge CLK) begin
    if(reset_done) begin
      if(vx && rx) begin
        $display("x=%d", x);
      end 
      if(vy && ry) begin
        $display("y=%d", y);
      end 
      if(vz && rz) begin
        $display("z=%d", z);
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
  output [32-1:0] z,
  output vz,
  input rz
);

  reg [32-1:0] _df_data_0;
  reg _df_valid_0;
  wire _df_ready_0;
  assign rx = (_df_ready_0 || !_df_valid_0) && vx;
  reg [32-1:0] _df_data_1;
  reg _df_valid_1;
  wire _df_ready_1;
  reg [32-1:0] _df_data_2;
  reg _df_valid_2;
  wire _df_ready_2;
  assign _df_ready_0 = (_df_ready_1 || !_df_valid_1) && _df_valid_0 && ((_df_ready_2 || !_df_valid_2) && _df_valid_0);
  assign y = _df_data_2;
  assign vy = _df_valid_2;
  assign _df_ready_2 = ry;
  assign z = _df_data_1;
  assign vz = _df_valid_1;
  assign _df_ready_1 = rz;

  always @(posedge CLK) begin
    if(RST) begin
      _df_data_0 <= 0;
      _df_valid_0 <= 0;
      _df_data_1 <= 0;
      _df_valid_1 <= 0;
      _df_data_2 <= 0;
      _df_valid_2 <= 0;
    end else begin
      if(vx && rx && (_df_ready_0 || !_df_valid_0)) begin
        _df_data_0 <= x + 1;
      end 
      if(_df_valid_0 && _df_ready_0) begin
        _df_valid_0 <= 0;
      end 
      if(rx && (_df_ready_0 || !_df_valid_0)) begin
        _df_valid_0 <= vx;
      end 
      if(_df_valid_0 && _df_ready_0 && (_df_ready_1 || !_df_valid_1)) begin
        _df_data_1 <= _df_data_0 + 1;
      end 
      if(_df_valid_1 && _df_ready_1) begin
        _df_valid_1 <= 0;
      end 
      if(_df_ready_0 && (_df_ready_1 || !_df_valid_1)) begin
        _df_valid_1 <= _df_valid_0;
      end 
      if(_df_valid_0 && _df_ready_0 && (_df_ready_2 || !_df_valid_2)) begin
        _df_data_2 <= _df_data_0;
      end 
      if(_df_valid_2 && _df_ready_2) begin
        _df_valid_2 <= 0;
      end 
      if(_df_ready_0 && (_df_ready_2 || !_df_valid_2)) begin
        _df_valid_2 <= _df_valid_0;
      end 
    end
  end


endmodule
"""

def test():
    veriloggen.reset()
    test_module = pipeline_unbalanced_output.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
