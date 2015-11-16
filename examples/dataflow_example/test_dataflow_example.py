from __future__ import absolute_import
from __future__ import print_function
import dataflow_example
from veriloggen import *

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
  reg [32-1:0] c;
  wire [32-1:0] z;
  wire vz;
  reg rz;

  multadd
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
    .c(c),
    .z(z),
    .vz(vz),
    .rz(rz)
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
    c = 8;
    vx = 0;
    vy = 0;
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
          if(((_tmp_1 == 10) && ry)) begin
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
      if((vx && rx)) begin
        $display("x=%d", x);
      end 
      if((vy && ry)) begin
        $display("y=%d", y);
      end 
      if((vz && rz)) begin
        $display("z=%d", z);
      end 
    end 
  end

endmodule

module multadd
(
  input CLK,
  input RST,
  input [32-1:0] x,
  input vx,
  output rx,
  input [32-1:0] y,
  input vy,
  output ry,
  input [32-1:0] c,
  output [32-1:0] z,
  output vz,
  input rz
);

  assign rx = (_df_ready_0 || (!_df_valid_0));
  assign ry = (_df_ready_1 || (!_df_valid_1));
  reg [32-1:0] _df_data_0;
  reg _df_valid_0;
  wire _df_ready_0;
  assign _df_ready_0 = (_df_ready_2 || (!_df_valid_2));
  reg [32-1:0] _df_data_1;
  reg _df_valid_1;
  wire _df_ready_1;
  assign _df_ready_1 = (_df_ready_2 || (!_df_valid_2));
  reg [32-1:0] _df_data_2;
  reg _df_valid_2;
  wire _df_ready_2;
  assign _df_ready_2 = (_df_ready_3 || (!_df_valid_3));
  reg [32-1:0] _df_data_3;
  reg _df_valid_3;
  wire _df_ready_3;
  assign _df_ready_3 = rz;
  assign z = _df_data_3;
  assign vz = _df_valid_3;

  always @(posedge CLK) begin
    if(RST) begin
      _df_data_0 <= 0;
      _df_valid_0 <= 0;
      _df_data_1 <= 0;
      _df_valid_1 <= 0;
      _df_data_2 <= 0;
      _df_valid_2 <= 0;
      _df_data_3 <= 0;
      _df_valid_3 <= 0;
    end else begin
      if(((vx && rx) && (_df_ready_0 || (!_df_valid_0)))) begin
        _df_data_0 <= (x * c);
      end 
      if((_df_ready_0 || (!_df_valid_0))) begin
        _df_valid_0 <= (vx && rx);
      end 
      if(((vy && ry) && (_df_ready_1 || (!_df_valid_1)))) begin
        _df_data_1 <= y;
      end 
      if((_df_ready_1 || (!_df_valid_1))) begin
        _df_valid_1 <= (vy && ry);
      end 
      if((((_df_valid_0 && _df_ready_0) && (_df_valid_1 && _df_ready_1)) && (_df_ready_2 || (!_df_valid_2)))) begin
        _df_data_2 <= (_df_data_0 + _df_data_1);
      end 
      if((_df_ready_2 || (!_df_valid_2))) begin
        _df_valid_2 <= ((_df_valid_0 && _df_ready_0) && (_df_valid_1 && _df_ready_1));
      end 
      if(((_df_valid_2 && _df_ready_2) && (_df_ready_3 || (!_df_valid_3)))) begin
        _df_data_3 <= _df_data_2;
      end 
      if((_df_ready_3 || (!_df_valid_3))) begin
        _df_valid_3 <= (_df_valid_2 && _df_ready_2);
      end 
    end
  end

endmodule
"""

expected_rslt = """\
VCD info: dumpfile uut.vcd opened for output.
x=         1
y=         2
x=         2
y=         4
x=         3
y=         6
x=         4
y=         8
z=        10
x=         5
y=        10
z=        20
x=         6
y=        12
z=        30
x=         7
y=        14
z=        40
x=         8
y=        16
z=        50
x=         9
y=        18
z=        60
x=        10
y=        20
z=        70
z=        80
z=        90
z=       100
"""

def test():
    test_module = dataflow_example.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)

    sim = lib.simulation.Simulator(test_module)
    rslt = sim.run()

    assert(expected_rslt == rslt)
    
