from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import dataflow_reduceadd_valid

expected_verilog = """

module test
(

);

  reg CLK;
  reg RST;
  reg [32-1:0] xdata;
  reg xvalid;
  wire xready;
  wire [32-1:0] zdata;
  wire zvalid;
  reg zready;
  wire [1-1:0] vdata;
  wire vvalid;
  reg vready;

  main
  uut
  (
    .CLK(CLK),
    .RST(RST),
    .xdata(xdata),
    .xvalid(xvalid),
    .xready(xready),
    .zdata(zdata),
    .zvalid(zvalid),
    .zready(zready),
    .vdata(vdata),
    .vvalid(vvalid),
    .vready(vready)
  );

  reg reset_done;

  initial begin
    $dumpfile("dataflow_reduceadd_valid.vcd");
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
    xdata = 0;
    xvalid = 0;
    zready = 0;
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

  reg [32-1:0] xfsm;
  localparam xfsm_init = 0;
  reg [32-1:0] _tmp_0;
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
          xvalid <= 0;
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
          xvalid <= 1;
          xfsm <= xfsm_12;
        end
        xfsm_12: begin
          if(xready) begin
            xdata <= xdata + 1;
          end 
          if(xready) begin
            _tmp_0 <= _tmp_0 + 1;
          end 
          if((_tmp_0 == 5) && xready) begin
            xvalid <= 0;
          end 
          if((_tmp_0 == 5) && xready) begin
            xfsm <= xfsm_13;
          end 
        end
        xfsm_13: begin
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
          xvalid <= 1;
          if(xready) begin
            xdata <= xdata + 1;
          end 
          if(xready) begin
            _tmp_0 <= _tmp_0 + 1;
          end 
          if((_tmp_0 == 100) && xready) begin
            xvalid <= 0;
          end 
          if((_tmp_0 == 100) && xready) begin
            xfsm <= xfsm_24;
          end 
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

  always @(posedge CLK) begin
    if(RST) begin
      zfsm <= zfsm_init;
    end else begin
      case(zfsm)
        zfsm_init: begin
          zready <= 0;
          if(reset_done) begin
            zfsm <= zfsm_1;
          end 
        end
        zfsm_1: begin
          zfsm <= zfsm_2;
        end
        zfsm_2: begin
          if(zvalid && vvalid) begin
            zready <= 1;
          end 
          if(zvalid && vvalid) begin
            zfsm <= zfsm_3;
          end 
        end
        zfsm_3: begin
          zready <= 0;
          zfsm <= zfsm_4;
        end
        zfsm_4: begin
          zready <= 0;
          zfsm <= zfsm_5;
        end
        zfsm_5: begin
          zready <= 0;
          zfsm <= zfsm_6;
        end
        zfsm_6: begin
          zready <= 0;
          zfsm <= zfsm_7;
        end
        zfsm_7: begin
          zready <= 0;
          zfsm <= zfsm_8;
        end
        zfsm_8: begin
          zfsm <= zfsm_2;
        end
      endcase
    end
  end

  reg [32-1:0] vfsm;
  localparam vfsm_init = 0;
  localparam vfsm_1 = 1;
  localparam vfsm_2 = 2;
  localparam vfsm_3 = 3;
  localparam vfsm_4 = 4;
  localparam vfsm_5 = 5;
  localparam vfsm_6 = 6;
  localparam vfsm_7 = 7;
  localparam vfsm_8 = 8;

  always @(posedge CLK) begin
    if(RST) begin
      vfsm <= vfsm_init;
    end else begin
      case(vfsm)
        vfsm_init: begin
          vready <= 0;
          if(reset_done) begin
            vfsm <= vfsm_1;
          end 
        end
        vfsm_1: begin
          vfsm <= vfsm_2;
        end
        vfsm_2: begin
          if(zvalid && vvalid) begin
            vready <= 1;
          end 
          if(zvalid && vvalid) begin
            vfsm <= vfsm_3;
          end 
        end
        vfsm_3: begin
          vready <= 0;
          vfsm <= vfsm_4;
        end
        vfsm_4: begin
          vready <= 0;
          vfsm <= vfsm_5;
        end
        vfsm_5: begin
          vready <= 0;
          vfsm <= vfsm_6;
        end
        vfsm_6: begin
          vready <= 0;
          vfsm <= vfsm_7;
        end
        vfsm_7: begin
          vready <= 0;
          vfsm <= vfsm_8;
        end
        vfsm_8: begin
          vfsm <= vfsm_2;
        end
      endcase
    end
  end


  always @(posedge CLK) begin
    if(reset_done) begin
      if(xvalid && xready) begin
        $display("xdata=%d", xdata);
      end 
      if(zvalid && zready) begin
        $display("zdata=%d", zdata);
      end 
      if(vvalid && vready) begin
        $display("vdata=%d", vdata);
      end 
    end 
  end


endmodule



module main
(
  input CLK,
  input RST,
  input [32-1:0] xdata,
  input xvalid,
  output xready,
  output [32-1:0] zdata,
  output zvalid,
  input zready,
  output [1-1:0] vdata,
  output vvalid,
  input vready
);

  wire [32-1:0] _dataflow_times_data_1;
  wire _dataflow_times_valid_1;
  wire _dataflow_times_ready_1;
  wire [64-1:0] _dataflow_times_mul_odata_1;
  reg [64-1:0] _dataflow_times_mul_odata_reg_1;
  assign _dataflow_times_data_1 = _dataflow_times_mul_odata_reg_1;
  wire _dataflow_times_mul_ovalid_1;
  reg _dataflow_times_mul_valid_reg_1;
  assign _dataflow_times_valid_1 = _dataflow_times_mul_valid_reg_1;
  wire _dataflow_times_mul_enable_1;
  wire _dataflow_times_mul_update_1;
  assign _dataflow_times_mul_enable_1 = (_dataflow_times_ready_1 || !_dataflow_times_valid_1) && (xready && xready) && (xvalid && xvalid);
  assign _dataflow_times_mul_update_1 = _dataflow_times_ready_1 || !_dataflow_times_valid_1;

  multiplier_0
  _dataflow_times_mul_1
  (
    .CLK(CLK),
    .RST(RST),
    .update(_dataflow_times_mul_update_1),
    .enable(_dataflow_times_mul_enable_1),
    .valid(_dataflow_times_mul_ovalid_1),
    .a(xdata),
    .b(xdata),
    .c(_dataflow_times_mul_odata_1)
  );

  assign xready = (_dataflow_times_ready_1 || !_dataflow_times_valid_1) && (xvalid && xvalid) && ((_dataflow_times_ready_1 || !_dataflow_times_valid_1) && (xvalid && xvalid));
  reg [32-1:0] _dataflow_reduceadd_data_4;
  reg _dataflow_reduceadd_valid_4;
  wire _dataflow_reduceadd_ready_4;
  reg [5-1:0] _dataflow_reduceadd_count_4;
  reg [1-1:0] _dataflow_pulse_data_7;
  reg _dataflow_pulse_valid_7;
  wire _dataflow_pulse_ready_7;
  reg [5-1:0] _dataflow_pulse_count_7;
  assign _dataflow_times_ready_1 = (_dataflow_reduceadd_ready_4 || !_dataflow_reduceadd_valid_4) && _dataflow_times_valid_1 && ((_dataflow_pulse_ready_7 || !_dataflow_pulse_valid_7) && _dataflow_times_valid_1);
  assign zdata = _dataflow_reduceadd_data_4;
  assign zvalid = _dataflow_reduceadd_valid_4;
  assign _dataflow_reduceadd_ready_4 = zready;
  assign vdata = _dataflow_pulse_data_7;
  assign vvalid = _dataflow_pulse_valid_7;
  assign _dataflow_pulse_ready_7 = vready;

  always @(posedge CLK) begin
    if(RST) begin
      _dataflow_times_mul_odata_reg_1 <= 0;
      _dataflow_times_mul_valid_reg_1 <= 0;
      _dataflow_reduceadd_data_4 <= 1'sd0;
      _dataflow_reduceadd_count_4 <= 0;
      _dataflow_reduceadd_valid_4 <= 0;
      _dataflow_pulse_data_7 <= 1'sd0;
      _dataflow_pulse_count_7 <= 0;
      _dataflow_pulse_valid_7 <= 0;
    end else begin
      if(_dataflow_times_ready_1 || !_dataflow_times_valid_1) begin
        _dataflow_times_mul_odata_reg_1 <= _dataflow_times_mul_odata_1;
      end 
      if(_dataflow_times_ready_1 || !_dataflow_times_valid_1) begin
        _dataflow_times_mul_valid_reg_1 <= _dataflow_times_mul_ovalid_1;
      end 
      if((_dataflow_reduceadd_ready_4 || !_dataflow_reduceadd_valid_4) && _dataflow_times_ready_1 && _dataflow_times_valid_1) begin
        _dataflow_reduceadd_data_4 <= _dataflow_reduceadd_data_4 + _dataflow_times_data_1;
      end 
      if((_dataflow_reduceadd_ready_4 || !_dataflow_reduceadd_valid_4) && _dataflow_times_ready_1 && _dataflow_times_valid_1) begin
        _dataflow_reduceadd_count_4 <= (_dataflow_reduceadd_count_4 == 4'sd4 - 1)? 0 : _dataflow_reduceadd_count_4 + 1;
      end 
      if(_dataflow_reduceadd_valid_4 && _dataflow_reduceadd_ready_4) begin
        _dataflow_reduceadd_valid_4 <= 0;
      end 
      if((_dataflow_reduceadd_ready_4 || !_dataflow_reduceadd_valid_4) && _dataflow_times_ready_1) begin
        _dataflow_reduceadd_valid_4 <= _dataflow_times_valid_1;
      end 
      if((_dataflow_reduceadd_ready_4 || !_dataflow_reduceadd_valid_4) && _dataflow_times_ready_1 && _dataflow_times_valid_1 && (_dataflow_reduceadd_count_4 == 0)) begin
        _dataflow_reduceadd_data_4 <= 1'sd0 + _dataflow_times_data_1;
      end 
      if((_dataflow_pulse_ready_7 || !_dataflow_pulse_valid_7) && _dataflow_times_ready_1 && _dataflow_times_valid_1) begin
        _dataflow_pulse_data_7 <= _dataflow_pulse_count_7 == 4'sd4 - 1;
      end 
      if((_dataflow_pulse_ready_7 || !_dataflow_pulse_valid_7) && _dataflow_times_ready_1 && _dataflow_times_valid_1) begin
        _dataflow_pulse_count_7 <= (_dataflow_pulse_count_7 == 4'sd4 - 1)? 0 : _dataflow_pulse_count_7 + 1;
      end 
      if(_dataflow_pulse_valid_7 && _dataflow_pulse_ready_7) begin
        _dataflow_pulse_valid_7 <= 0;
      end 
      if((_dataflow_pulse_ready_7 || !_dataflow_pulse_valid_7) && _dataflow_times_ready_1) begin
        _dataflow_pulse_valid_7 <= _dataflow_times_valid_1;
      end 
      if((_dataflow_pulse_ready_7 || !_dataflow_pulse_valid_7) && _dataflow_times_ready_1 && _dataflow_times_valid_1 && (_dataflow_pulse_count_7 == 0)) begin
        _dataflow_pulse_data_7 <= _dataflow_pulse_count_7 == 4'sd4 - 1;
      end 
    end
  end


endmodule



module multiplier_0
(
  input CLK,
  input RST,
  input update,
  input enable,
  output valid,
  input [32-1:0] a,
  input [32-1:0] b,
  output [64-1:0] c
);

  reg valid_reg0;
  reg valid_reg1;
  reg valid_reg2;
  reg valid_reg3;
  reg valid_reg4;
  reg valid_reg5;
  assign valid = valid_reg5;

  always @(posedge CLK) begin
    if(RST) begin
      valid_reg0 <= 0;
      valid_reg1 <= 0;
      valid_reg2 <= 0;
      valid_reg3 <= 0;
      valid_reg4 <= 0;
      valid_reg5 <= 0;
    end else begin
      if(update) begin
        valid_reg0 <= enable;
        valid_reg1 <= valid_reg0;
        valid_reg2 <= valid_reg1;
        valid_reg3 <= valid_reg2;
        valid_reg4 <= valid_reg3;
        valid_reg5 <= valid_reg4;
      end 
    end
  end


  multiplier_core_0
  mult
  (
    .CLK(CLK),
    .update(update),
    .a(a),
    .b(b),
    .c(c)
  );


endmodule



module multiplier_core_0
(
  input CLK,
  input update,
  input [32-1:0] a,
  input [32-1:0] b,
  output [64-1:0] c
);

  reg [32-1:0] _a;
  reg [32-1:0] _b;
  wire signed [64-1:0] _mul;
  reg signed [64-1:0] _pipe_mul0;
  reg signed [64-1:0] _pipe_mul1;
  reg signed [64-1:0] _pipe_mul2;
  reg signed [64-1:0] _pipe_mul3;
  reg signed [64-1:0] _pipe_mul4;
  assign _mul = $signed({ 1'd0, _a }) * $signed({ 1'd0, _b });
  assign c = _pipe_mul4;

  always @(posedge CLK) begin
    if(update) begin
      _a <= a;
      _b <= b;
      _pipe_mul0 <= _mul;
      _pipe_mul1 <= _pipe_mul0;
      _pipe_mul2 <= _pipe_mul1;
      _pipe_mul3 <= _pipe_mul2;
      _pipe_mul4 <= _pipe_mul3;
    end 
  end


endmodule

"""


def test():
    veriloggen.reset()
    test_module = dataflow_reduceadd_valid.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
