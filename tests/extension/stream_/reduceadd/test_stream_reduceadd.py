from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import stream_reduceadd

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

  reg signed [32-1:0] _plus_data_3;
  reg signed [32-1:0] __delay_data_10__variable_2;
  reg signed [32-1:0] _reduceadd_data_4;
  reg [6-1:0] _reduceadd_count_4;
  reg _reduceadd_prev_count_max_4;
  wire _reduceadd_reset_cond_4;
  assign _reduceadd_reset_cond_4 = _reduceadd_prev_count_max_4;
  wire [6-1:0] _reduceadd_current_count_4;
  assign _reduceadd_current_count_4 = (_reduceadd_reset_cond_4)? 0 : _reduceadd_count_4;
  wire signed [32-1:0] _reduceadd_current_data_4;
  assign _reduceadd_current_data_4 = (_reduceadd_reset_cond_4)? 1'sd0 : _reduceadd_data_4;
  reg [1-1:0] _pulse_data_7;
  reg [6-1:0] _pulse_count_7;
  reg _pulse_prev_count_max_7;
  wire _pulse_reset_cond_7;
  assign _pulse_reset_cond_7 = _pulse_prev_count_max_7;
  wire [6-1:0] _pulse_current_count_7;
  assign _pulse_current_count_7 = (_pulse_reset_cond_7)? 0 : _pulse_count_7;
  wire [1-1:0] _pulse_current_data_7;
  assign _pulse_current_data_7 = (_pulse_reset_cond_7)? 1'sd0 : _pulse_data_7;
  assign zdata = _reduceadd_data_4;
  assign vdata = _pulse_data_7;

  always @(posedge CLK) begin
    if(RST) begin
      _plus_data_3 <= 0;
      __delay_data_10__variable_2 <= 0;
      _reduceadd_count_4 <= 0;
      _reduceadd_prev_count_max_4 <= 0;
      _reduceadd_data_4 <= 1'sd0;
      _pulse_count_7 <= 0;
      _pulse_prev_count_max_7 <= 0;
      _pulse_data_7 <= 1'sd0;
    end else begin
      _plus_data_3 <= xdata + ydata;
      __delay_data_10__variable_2 <= edata;
      if(__delay_data_10__variable_2) begin
        _reduceadd_count_4 <= (_reduceadd_current_count_4 >= 5'sd8 - 1)? 0 : _reduceadd_current_count_4 + 1;
      end 
      if(__delay_data_10__variable_2) begin
        _reduceadd_prev_count_max_4 <= _reduceadd_current_count_4 >= 5'sd8 - 1;
      end 
      if(__delay_data_10__variable_2) begin
        _reduceadd_data_4 <= _reduceadd_current_data_4 + _plus_data_3;
      end 
      if(__delay_data_10__variable_2) begin
        _pulse_count_7 <= (_pulse_current_count_7 >= 5'sd8 - 1)? 0 : _pulse_current_count_7 + 1;
      end 
      if(__delay_data_10__variable_2) begin
        _pulse_prev_count_max_7 <= _pulse_current_count_7 >= 5'sd8 - 1;
      end 
      if(__delay_data_10__variable_2) begin
        _pulse_data_7 <= _pulse_current_count_7 >= 5'sd8 - 1;
      end 
    end
  end


endmodule
"""


def test():
    veriloggen.reset()
    test_module = stream_reduceadd.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
