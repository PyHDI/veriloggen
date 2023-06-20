from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import pipeline_draw_graph

expected_verilog = """
module test
(
);

  reg CLK;
  reg RST;
  reg [32-1:0] x;
  reg vx;
  wire rx;
  reg [32-1:0] y;
  reg vy;
  wire ry;
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
    $dumpfile("pipeline_draw_graph.vcd");
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
    y = 0;
    vx = 0;
    vy = 0;
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
            x <= x + 1;
          end 
          if(rx) begin
            _tmp_0 <= _tmp_0 + 1;
          end 
          if((_tmp_0 == 10) && rx) begin
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

  always @(posedge CLK) begin
    if(RST) begin
      yfsm <= yfsm_init;
      _tmp_1 <= 0;
    end else begin
      case(yfsm)
        yfsm_init: begin
          vy <= 0;
          if(reset_done) begin
            yfsm <= yfsm_1;
          end 
        end
        yfsm_1: begin
          vy <= 1;
          if(ry) begin
            y <= y + 2;
          end 
          if(ry) begin
            _tmp_1 <= _tmp_1 + 1;
          end 
          if((_tmp_1 == 10) && ry) begin
            yfsm <= yfsm_2;
          end 
        end
        yfsm_2: begin
          vy <= 0;
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
  input [32-1:0] y,
  input vy,
  output ry,
  output [32-1:0] z,
  output vz,
  input rz
);

  reg [32-1:0] _df_data_0;
  reg _df_valid_0;
  wire _df_ready_0;
  assign rx = (_df_ready_0 || !_df_valid_0) && (vx && vy);
  assign ry = (_df_ready_0 || !_df_valid_0) && (vx && vy);
  assign z = _df_data_0;
  assign vz = _df_valid_0;
  assign _df_ready_0 = rz;

  always @(posedge CLK) begin
    if(RST) begin
      _df_data_0 <= 0;
      _df_valid_0 <= 0;
    end else begin
      if(vx && vy && (rx && ry) && (_df_ready_0 || !_df_valid_0)) begin
        _df_data_0 <= x + y;
      end 
      if(_df_valid_0 && _df_ready_0) begin
        _df_valid_0 <= 0;
      end 
      if(rx && ry && (_df_ready_0 || !_df_valid_0)) begin
        _df_valid_0 <= vx && vy;
      end 
    end
  end

endmodule
"""


def test():
    veriloggen.reset()
    test_module = pipeline_draw_graph.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
