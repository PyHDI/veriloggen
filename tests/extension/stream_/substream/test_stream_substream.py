from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import stream_substream

expected_verilog = """
module test;

  reg CLK;
  reg RST;
  reg signed [32-1:0] xdata;
  reg signed [32-1:0] ydata;
  reg signed [32-1:0] edata;
  wire signed [32-1:0] zdata;
  wire [1-1:0] vdata;

  main
  uut
  (
    .CLK(CLK),
    .RST(RST),
    .xdata(xdata),
    .ydata(ydata),
    .edata(edata),
    .zdata(zdata),
    .vdata(vdata)
  );

  reg reset_done;

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
    ydata = 0;
    edata = 0;
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

  reg [32-1:0] send_fsm;
  localparam send_fsm_init = 0;
  reg [32-1:0] send_count;
  reg [32-1:0] _d1_send_fsm;
  reg _send_fsm_cond_1_0_1;
  reg _send_fsm_cond_2_1_1;
  reg [32-1:0] recv_fsm;
  localparam recv_fsm_init = 0;
  reg [32-1:0] recv_count;
  localparam send_fsm_1 = 1;
  localparam send_fsm_2 = 2;
  localparam send_fsm_3 = 3;

  always @(posedge CLK) begin
    if(RST) begin
      send_fsm <= send_fsm_init;
      _d1_send_fsm <= send_fsm_init;
      send_count <= 0;
      _send_fsm_cond_1_0_1 <= 0;
      _send_fsm_cond_2_1_1 <= 0;
    end else begin
      _d1_send_fsm <= send_fsm;
      case(_d1_send_fsm)
        send_fsm_1: begin
          if(_send_fsm_cond_1_0_1) begin
            $display("xdata=%d", xdata);
            $display("ydata=%d", ydata);
          end 
        end
        send_fsm_2: begin
          if(_send_fsm_cond_2_1_1) begin
            $display("xdata=%d", xdata);
            $display("ydata=%d", ydata);
          end 
        end
      endcase
      case(send_fsm)
        send_fsm_init: begin
          if(reset_done) begin
            send_fsm <= send_fsm_1;
          end 
        end
        send_fsm_1: begin
          xdata <= 0;
          ydata <= 0;
          edata <= 1;
          send_count <= send_count + 1;
          _send_fsm_cond_1_0_1 <= 1;
          send_fsm <= send_fsm_2;
        end
        send_fsm_2: begin
          xdata <= xdata + 1;
          ydata <= ydata + 2;
          edata <= 1;
          send_count <= send_count + 1;
          _send_fsm_cond_2_1_1 <= 1;
          if(send_count == 64) begin
            send_fsm <= send_fsm_3;
          end 
        end
        send_fsm_3: begin
          edata <= 0;
        end
      endcase
    end
  end

  localparam recv_fsm_1 = 1;
  localparam recv_fsm_2 = 2;

  always @(posedge CLK) begin
    if(RST) begin
      recv_fsm <= recv_fsm_init;
      recv_count <= 0;
    end else begin
      case(recv_fsm)
        recv_fsm_init: begin
          if(reset_done) begin
            recv_fsm <= recv_fsm_1;
          end 
        end
        recv_fsm_1: begin
          if(vdata) begin
            $display("zdata=%d", zdata);
            recv_count <= recv_count + 1;
          end 
          if(recv_count == 8) begin
            recv_fsm <= recv_fsm_2;
          end 
        end
      endcase
    end
  end


endmodule



module main
(
  input CLK,
  input RST,
  input signed [32-1:0] xdata,
  input signed [32-1:0] ydata,
  input signed [32-1:0] edata,
  output signed [32-1:0] zdata,
  output [1-1:0] vdata
);

  wire signed [32-1:0] adata;
  wire signed [32-1:0] bdata;
  wire signed [64-1:0] _times_mul_odata_2;
  reg signed [64-1:0] _times_mul_odata_reg_2;
  wire signed [32-1:0] _times_data_2;
  assign _times_data_2 = _times_mul_odata_reg_2;
  wire _times_mul_update_2;
  assign _times_mul_update_2 = 1'd1;

  multiplier_0
  _times_mul_2
  (
    .CLK(CLK),
    .update(_times_mul_update_2),
    .a(adata),
    .b(bdata),
    .c(_times_mul_odata_2)
  );

  wire signed [32-1:0] cdata;
  assign cdata = _times_data_2;
  reg signed [32-1:0] _plus_data_6;
  reg signed [32-1:0] _plus_data_8;
  reg signed [32-1:0] __delay_data_20__variable_5;
  reg signed [32-1:0] __variable_wdata_0;
  assign adata = __variable_wdata_0;
  reg signed [32-1:0] __variable_wdata_1;
  assign bdata = __variable_wdata_1;
  reg signed [32-1:0] __delay_data_21__delay_20__variable_5;
  reg signed [32-1:0] __delay_data_22__delay_21__delay_20__variable_5;
  reg signed [32-1:0] __delay_data_23__delay_22__delay_21__delay_20__variable_5;
  reg signed [32-1:0] __delay_data_24__delay_23__delay_22__delay_21____variable_5;
  wire signed [32-1:0] __substreamoutput_data_11;
  assign __substreamoutput_data_11 = cdata;
  reg signed [32-1:0] _reduceadd_data_12;
  reg [6-1:0] _reduceadd_count_12;
  reg _reduceadd_prev_count_max_12;
  wire _reduceadd_reset_cond_12;
  assign _reduceadd_reset_cond_12 = _reduceadd_prev_count_max_12;
  wire [6-1:0] _reduceadd_current_count_12;
  assign _reduceadd_current_count_12 = (_reduceadd_reset_cond_12)? 0 : _reduceadd_count_12;
  wire signed [32-1:0] _reduceadd_current_data_12;
  assign _reduceadd_current_data_12 = (_reduceadd_reset_cond_12)? 1'sd0 : _reduceadd_data_12;
  reg [1-1:0] _pulse_data_15;
  reg [6-1:0] _pulse_count_15;
  reg _pulse_prev_count_max_15;
  wire _pulse_reset_cond_15;
  assign _pulse_reset_cond_15 = _pulse_prev_count_max_15;
  wire [6-1:0] _pulse_current_count_15;
  assign _pulse_current_count_15 = (_pulse_reset_cond_15)? 0 : _pulse_count_15;
  wire [1-1:0] _pulse_current_data_15;
  assign _pulse_current_data_15 = (_pulse_reset_cond_15)? 1'sd0 : _pulse_data_15;
  reg signed [32-1:0] _plus_data_18;
  reg [1-1:0] __delay_data_25_pulse_15;
  assign zdata = _plus_data_18;
  assign vdata = __delay_data_25_pulse_15;

  always @(posedge CLK) begin
    if(RST) begin
      _times_mul_odata_reg_2 <= 0;
      __variable_wdata_0 <= 0;
      __variable_wdata_1 <= 0;
    end else begin
      _times_mul_odata_reg_2 <= _times_mul_odata_2;
      __variable_wdata_0 <= _plus_data_6;
      __variable_wdata_1 <= _plus_data_8;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      _plus_data_6 <= 0;
      _plus_data_8 <= 0;
      __delay_data_20__variable_5 <= 0;
      __delay_data_21__delay_20__variable_5 <= 0;
      __delay_data_22__delay_21__delay_20__variable_5 <= 0;
      __delay_data_23__delay_22__delay_21__delay_20__variable_5 <= 0;
      __delay_data_24__delay_23__delay_22__delay_21____variable_5 <= 0;
      _reduceadd_count_12 <= 0;
      _reduceadd_prev_count_max_12 <= 0;
      _reduceadd_data_12 <= 1'sd0;
      _pulse_count_15 <= 0;
      _pulse_prev_count_max_15 <= 0;
      _pulse_data_15 <= 1'sd0;
      _plus_data_18 <= 0;
      __delay_data_25_pulse_15 <= 0;
    end else begin
      _plus_data_6 <= xdata + 2'sd1;
      _plus_data_8 <= ydata + 3'sd2;
      __delay_data_20__variable_5 <= edata;
      __delay_data_21__delay_20__variable_5 <= __delay_data_20__variable_5;
      __delay_data_22__delay_21__delay_20__variable_5 <= __delay_data_21__delay_20__variable_5;
      __delay_data_23__delay_22__delay_21__delay_20__variable_5 <= __delay_data_22__delay_21__delay_20__variable_5;
      __delay_data_24__delay_23__delay_22__delay_21____variable_5 <= __delay_data_23__delay_22__delay_21__delay_20__variable_5;
      if(__delay_data_24__delay_23__delay_22__delay_21____variable_5) begin
        _reduceadd_count_12 <= (_reduceadd_current_count_12 >= 5'sd8 - 1)? 0 : _reduceadd_current_count_12 + 1;
      end 
      if(__delay_data_24__delay_23__delay_22__delay_21____variable_5) begin
        _reduceadd_prev_count_max_12 <= _reduceadd_current_count_12 >= 5'sd8 - 1;
      end 
      if(__delay_data_24__delay_23__delay_22__delay_21____variable_5) begin
        _reduceadd_data_12 <= _reduceadd_current_data_12 + __substreamoutput_data_11;
      end 
      if(__delay_data_24__delay_23__delay_22__delay_21____variable_5) begin
        _pulse_count_15 <= (_pulse_current_count_15 >= 5'sd8 - 1)? 0 : _pulse_current_count_15 + 1;
      end 
      if(__delay_data_24__delay_23__delay_22__delay_21____variable_5) begin
        _pulse_prev_count_max_15 <= _pulse_current_count_15 >= 5'sd8 - 1;
      end 
      if(__delay_data_24__delay_23__delay_22__delay_21____variable_5) begin
        _pulse_data_15 <= _pulse_current_count_15 >= 5'sd8 - 1;
      end 
      _plus_data_18 <= _reduceadd_data_12 + 11'sd1000;
      __delay_data_25_pulse_15 <= _pulse_data_15;
    end
  end


endmodule



module multiplier_0
(
  input CLK,
  input update,
  input [32-1:0] a,
  input [32-1:0] b,
  output [64-1:0] c
);


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

  reg signed [32-1:0] _a;
  reg signed [32-1:0] _b;
  wire signed [64-1:0] _mul;
  reg signed [64-1:0] _pipe_mul0;
  assign _mul = _a * _b;
  assign c = _pipe_mul0;

  always @(posedge CLK) begin
    if(update) begin
      _a <= a;
      _b <= b;
      _pipe_mul0 <= _mul;
    end 
  end


endmodule
"""


def test():
    veriloggen.reset()
    test_module = stream_substream.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
