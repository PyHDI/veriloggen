from __future__ import absolute_import
from __future__ import print_function
import pipeline_multi_output

expected_verilog = """
module test;
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
  wire [32-1:0] a;
  wire va;
  reg ra;

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
    .rz(rz),
    .a(a),
    .va(va),
    .ra(ra)
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
    y = 0;
    vx = 0;
    vy = 0;
    rz = 0;
    ra = 0;
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
  reg [32-1:0] _tmp_3;
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
            y <= (y + 2);
          end 
          if(ry) begin
            _tmp_1 <= (_tmp_1 + 1);
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

  reg [32-1:0] afsm;
  localparam afsm_init = 0;
  localparam afsm_1 = 1;
  localparam afsm_2 = 2;
  localparam afsm_3 = 3;
  localparam afsm_4 = 4;
  localparam afsm_5 = 5;
  localparam afsm_6 = 6;
  localparam afsm_7 = 7;
  localparam afsm_8 = 8;
  localparam afsm_9 = 9;
  localparam afsm_10 = 10;
  localparam afsm_11 = 11;
  localparam afsm_12 = 12;
  localparam afsm_13 = 13;
  localparam afsm_14 = 14;
  localparam afsm_15 = 15;
  localparam afsm_16 = 16;
  localparam afsm_17 = 17;
  localparam afsm_18 = 18;
  localparam afsm_19 = 19;
  localparam afsm_20 = 20;
  localparam afsm_21 = 21;
  localparam afsm_22 = 22;
  localparam afsm_23 = 23;

  always @(posedge CLK) begin
    if(RST) begin
      afsm <= afsm_init;
    end else begin
      case(afsm)
        afsm_init: begin
          ra <= 0;
          if(reset_done) begin
            afsm <= afsm_1;
          end 
        end
        afsm_1: begin
          afsm <= afsm_2;
        end
        afsm_2: begin
          if(va) begin
            ra <= 1;
          end 
          if(va) begin
            afsm <= afsm_3;
          end 
        end
        afsm_3: begin
          ra <= 0;
          afsm <= afsm_4;
        end
        afsm_4: begin
          ra <= 0;
          afsm <= afsm_5;
        end
        afsm_5: begin
          ra <= 0;
          afsm <= afsm_6;
        end
        afsm_6: begin
          ra <= 0;
          afsm <= afsm_7;
        end
        afsm_7: begin
          ra <= 0;
          afsm <= afsm_8;
        end
        afsm_8: begin
          ra <= 0;
          afsm <= afsm_9;
        end
        afsm_9: begin
          ra <= 0;
          afsm <= afsm_10;
        end
        afsm_10: begin
          ra <= 0;
          afsm <= afsm_11;
        end
        afsm_11: begin
          ra <= 0;
          afsm <= afsm_12;
        end
        afsm_12: begin
          ra <= 0;
          afsm <= afsm_13;
        end
        afsm_13: begin
          ra <= 0;
          afsm <= afsm_14;
        end
        afsm_14: begin
          ra <= 0;
          afsm <= afsm_15;
        end
        afsm_15: begin
          ra <= 0;
          afsm <= afsm_16;
        end
        afsm_16: begin
          ra <= 0;
          afsm <= afsm_17;
        end
        afsm_17: begin
          ra <= 0;
          afsm <= afsm_18;
        end
        afsm_18: begin
          ra <= 0;
          afsm <= afsm_19;
        end
        afsm_19: begin
          ra <= 0;
          afsm <= afsm_20;
        end
        afsm_20: begin
          ra <= 0;
          afsm <= afsm_21;
        end
        afsm_21: begin
          ra <= 0;
          afsm <= afsm_22;
        end
        afsm_22: begin
          ra <= 0;
          afsm <= afsm_23;
        end
        afsm_23: begin
          afsm <= afsm_2;
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
      if(va && ra) begin
        $display("a=%d", a);
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
  input rz,
  output [32-1:0] a,
  output va,
  input ra
);

  assign rx = ((_df_ready_0 || (!_df_valid_0)) && (_df_ready_1 || (!_df_valid_1)));
  assign ry = ((_df_ready_0 || (!_df_valid_0)) && (_df_ready_1 || (!_df_valid_1)));
  reg [32-1:0] _df_data_0;
  reg _df_valid_0;
  wire _df_ready_0;
  assign _df_ready_0 = rz;
  reg [32-1:0] _df_data_1;
  reg _df_valid_1;
  wire _df_ready_1;
  assign _df_ready_1 = ra;
  assign z = _df_data_0;
  assign vz = _df_valid_0;
  assign a = _df_data_1;
  assign va = _df_valid_1;

  always @(posedge CLK) begin
    if(RST) begin
      _df_data_0 <= 0;
      _df_valid_0 <= 0;
      _df_data_1 <= 0;
      _df_valid_1 <= 0;
    end else begin
      if((((vx && rx) && (vy && ry)) && (_df_ready_0 || (!_df_valid_0)))) begin
        _df_data_0 <= (x + y);
      end 
      if((_df_ready_0 || (!_df_valid_0))) begin
        _df_valid_0 <= ((vx && rx) && (vy && ry));
      end 
      if((((vy && ry) && (vx && rx)) && (_df_ready_1 || (!_df_valid_1)))) begin
        _df_data_1 <= (y - x);
      end 
      if((_df_ready_1 || (!_df_valid_1))) begin
        _df_valid_1 <= ((vy && ry) && (vx && rx));
      end 
    end
  end

endmodule
"""

def test():
    test_module = pipeline_multi_output.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
