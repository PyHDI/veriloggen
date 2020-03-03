from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import stream_sra_round

expected_verilog = """
module test
(

);

  reg CLK;
  reg RST;
  reg signed [32-1:0] xdata;
  reg signed [32-1:0] ydata;
  wire signed [32-1:0] zdata;

  main
  uut
  (
    .CLK(CLK),
    .RST(RST),
    .xdata(xdata),
    .ydata(ydata),
    .zdata(zdata)
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
    xdata = -128;
    ydata = 1;
    #100;
    RST = 1;
    #100;
    RST = 0;
    #1000;
    reset_done = 1;
    @(posedge CLK);
    #1;
    #100000;
    $finish;
  end

  reg [32-1:0] send_fsm;
  localparam send_fsm_init = 0;
  reg [32-1:0] send_count;
  reg [32-1:0] recv_fsm;
  localparam recv_fsm_init = 0;
  reg [32-1:0] recv_count;
  localparam send_fsm_1 = 1;
  localparam send_fsm_2 = 2;
  localparam send_fsm_3 = 3;
  localparam send_fsm_4 = 4;
  localparam send_fsm_5 = 5;
  localparam send_fsm_6 = 6;
  localparam send_fsm_7 = 7;
  localparam send_fsm_8 = 8;
  localparam send_fsm_9 = 9;
  localparam send_fsm_10 = 10;
  localparam send_fsm_11 = 11;
  localparam send_fsm_12 = 12;
  localparam send_fsm_13 = 13;
  localparam send_fsm_14 = 14;
  localparam send_fsm_15 = 15;
  localparam send_fsm_16 = 16;
  localparam send_fsm_17 = 17;

  always @(posedge CLK) begin
    if(RST) begin
      send_fsm <= send_fsm_init;
      send_count <= -128;
    end else begin
      case(send_fsm)
        send_fsm_init: begin
          if(reset_done) begin
            send_fsm <= send_fsm_1;
          end 
        end
        send_fsm_1: begin
          xdata <= -128;
          ydata <= 0;
          send_count <= -128;
          send_fsm <= send_fsm_2;
        end
        send_fsm_2: begin
          xdata <= xdata + 1;
          $display("xdata=%d", xdata);
          $display("ydata=%d", ydata);
          send_count <= send_count + 1;
          if(send_count == 127) begin
            send_fsm <= send_fsm_3;
          end 
        end
        send_fsm_3: begin
          xdata <= -128;
          ydata <= 1;
          send_count <= -128;
          send_fsm <= send_fsm_4;
        end
        send_fsm_4: begin
          xdata <= xdata + 1;
          $display("xdata=%d", xdata);
          $display("ydata=%d", ydata);
          send_count <= send_count + 1;
          if(send_count == 127) begin
            send_fsm <= send_fsm_5;
          end 
        end
        send_fsm_5: begin
          xdata <= -128;
          ydata <= 2;
          send_count <= -128;
          send_fsm <= send_fsm_6;
        end
        send_fsm_6: begin
          xdata <= xdata + 1;
          $display("xdata=%d", xdata);
          $display("ydata=%d", ydata);
          send_count <= send_count + 1;
          if(send_count == 127) begin
            send_fsm <= send_fsm_7;
          end 
        end
        send_fsm_7: begin
          xdata <= -128;
          ydata <= 3;
          send_count <= -128;
          send_fsm <= send_fsm_8;
        end
        send_fsm_8: begin
          xdata <= xdata + 1;
          $display("xdata=%d", xdata);
          $display("ydata=%d", ydata);
          send_count <= send_count + 1;
          if(send_count == 127) begin
            send_fsm <= send_fsm_9;
          end 
        end
        send_fsm_9: begin
          xdata <= -128;
          ydata <= 4;
          send_count <= -128;
          send_fsm <= send_fsm_10;
        end
        send_fsm_10: begin
          xdata <= xdata + 1;
          $display("xdata=%d", xdata);
          $display("ydata=%d", ydata);
          send_count <= send_count + 1;
          if(send_count == 127) begin
            send_fsm <= send_fsm_11;
          end 
        end
        send_fsm_11: begin
          xdata <= -128;
          ydata <= 5;
          send_count <= -128;
          send_fsm <= send_fsm_12;
        end
        send_fsm_12: begin
          xdata <= xdata + 1;
          $display("xdata=%d", xdata);
          $display("ydata=%d", ydata);
          send_count <= send_count + 1;
          if(send_count == 127) begin
            send_fsm <= send_fsm_13;
          end 
        end
        send_fsm_13: begin
          xdata <= -128;
          ydata <= 6;
          send_count <= -128;
          send_fsm <= send_fsm_14;
        end
        send_fsm_14: begin
          xdata <= xdata + 1;
          $display("xdata=%d", xdata);
          $display("ydata=%d", ydata);
          send_count <= send_count + 1;
          if(send_count == 127) begin
            send_fsm <= send_fsm_15;
          end 
        end
        send_fsm_15: begin
          xdata <= -128;
          ydata <= 7;
          send_count <= -128;
          send_fsm <= send_fsm_16;
        end
        send_fsm_16: begin
          xdata <= xdata + 1;
          $display("xdata=%d", xdata);
          $display("ydata=%d", ydata);
          send_count <= send_count + 1;
          if(send_count == 127) begin
            send_fsm <= send_fsm_17;
          end 
        end
      endcase
    end
  end

  localparam recv_fsm_1 = 1;
  localparam recv_fsm_2 = 2;
  localparam recv_fsm_3 = 3;
  localparam recv_fsm_4 = 4;
  localparam recv_fsm_5 = 5;
  localparam recv_fsm_6 = 6;
  localparam recv_fsm_7 = 7;
  localparam recv_fsm_8 = 8;
  localparam recv_fsm_9 = 9;
  localparam recv_fsm_10 = 10;
  localparam recv_fsm_11 = 11;
  localparam recv_fsm_12 = 12;
  localparam recv_fsm_13 = 13;
  localparam recv_fsm_14 = 14;
  localparam recv_fsm_15 = 15;
  localparam recv_fsm_16 = 16;
  localparam recv_fsm_17 = 17;

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
          recv_count <= -128;
          recv_fsm <= recv_fsm_2;
        end
        recv_fsm_2: begin
          $display("zdata=%d", zdata);
          recv_count <= recv_count + 1;
          if(recv_count == 137) begin
            recv_fsm <= recv_fsm_3;
          end 
        end
        recv_fsm_3: begin
          recv_count <= -128;
          recv_fsm <= recv_fsm_4;
        end
        recv_fsm_4: begin
          $display("zdata=%d", zdata);
          recv_count <= recv_count + 1;
          if(recv_count == 137) begin
            recv_fsm <= recv_fsm_5;
          end 
        end
        recv_fsm_5: begin
          recv_count <= -128;
          recv_fsm <= recv_fsm_6;
        end
        recv_fsm_6: begin
          $display("zdata=%d", zdata);
          recv_count <= recv_count + 1;
          if(recv_count == 137) begin
            recv_fsm <= recv_fsm_7;
          end 
        end
        recv_fsm_7: begin
          recv_count <= -128;
          recv_fsm <= recv_fsm_8;
        end
        recv_fsm_8: begin
          $display("zdata=%d", zdata);
          recv_count <= recv_count + 1;
          if(recv_count == 137) begin
            recv_fsm <= recv_fsm_9;
          end 
        end
        recv_fsm_9: begin
          recv_count <= -128;
          recv_fsm <= recv_fsm_10;
        end
        recv_fsm_10: begin
          $display("zdata=%d", zdata);
          recv_count <= recv_count + 1;
          if(recv_count == 137) begin
            recv_fsm <= recv_fsm_11;
          end 
        end
        recv_fsm_11: begin
          recv_count <= -128;
          recv_fsm <= recv_fsm_12;
        end
        recv_fsm_12: begin
          $display("zdata=%d", zdata);
          recv_count <= recv_count + 1;
          if(recv_count == 137) begin
            recv_fsm <= recv_fsm_13;
          end 
        end
        recv_fsm_13: begin
          recv_count <= -128;
          recv_fsm <= recv_fsm_14;
        end
        recv_fsm_14: begin
          $display("zdata=%d", zdata);
          recv_count <= recv_count + 1;
          if(recv_count == 137) begin
            recv_fsm <= recv_fsm_15;
          end 
        end
        recv_fsm_15: begin
          recv_count <= -128;
          recv_fsm <= recv_fsm_16;
        end
        recv_fsm_16: begin
          $display("zdata=%d", zdata);
          recv_count <= recv_count + 1;
          if(recv_count == 137) begin
            recv_fsm <= recv_fsm_17;
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
  output signed [32-1:0] zdata
);

  reg [1-1:0] _pointer_data_2;
  reg [3-1:0] _slice_data_7;
  reg [1-1:0] _eq_data_23;
  reg signed [32-1:0] __delay_data_25;
  reg signed [32-1:0] __delay_data_28;
  reg [3-1:0] _minus_data_8;
  reg signed [32-1:0] __delay_data_26;
  reg signed [32-1:0] __delay_data_29;
  reg [1-1:0] __delay_data_33;
  reg [1-1:0] __delay_data_39;
  reg signed [10-1:0] _sll_data_10;
  reg signed [32-1:0] __delay_data_27;
  reg signed [32-1:0] __delay_data_30;
  reg [1-1:0] __delay_data_34;
  reg [1-1:0] __delay_data_40;
  reg signed [32-1:0] _plus_data_16;
  reg signed [32-1:0] __delay_data_31;
  reg [1-1:0] __delay_data_35;
  reg [1-1:0] __delay_data_41;
  reg signed [32-1:0] __delay_data_45;
  reg signed [32-1:0] _minus_data_17;
  reg [32-1:0] _srl_data_20;
  reg signed [32-1:0] __delay_data_32;
  reg [1-1:0] __delay_data_36;
  reg [1-1:0] __delay_data_42;
  reg signed [32-1:0] __delay_data_46;
  reg signed [32-1:0] _sra_data_19;
  reg [1-1:0] __delay_data_37;
  reg [32-1:0] __delay_data_38;
  reg [1-1:0] __delay_data_43;
  reg signed [32-1:0] __delay_data_47;
  reg signed [32-1:0] _cond_data_21;
  reg [1-1:0] __delay_data_44;
  reg signed [32-1:0] __delay_data_48;
  reg signed [32-1:0] _cond_data_24;
  assign zdata = _cond_data_24;

  always @(posedge CLK) begin
    if(RST) begin
      _pointer_data_2 <= 0;
      _slice_data_7 <= 0;
      _eq_data_23 <= 0;
      __delay_data_25 <= 0;
      __delay_data_28 <= 0;
      _minus_data_8 <= 0;
      __delay_data_26 <= 0;
      __delay_data_29 <= 0;
      __delay_data_33 <= 0;
      __delay_data_39 <= 0;
      _sll_data_10 <= 0;
      __delay_data_27 <= 0;
      __delay_data_30 <= 0;
      __delay_data_34 <= 0;
      __delay_data_40 <= 0;
      _plus_data_16 <= 0;
      __delay_data_31 <= 0;
      __delay_data_35 <= 0;
      __delay_data_41 <= 0;
      __delay_data_45 <= 0;
      _minus_data_17 <= 0;
      _srl_data_20 <= 0;
      __delay_data_32 <= 0;
      __delay_data_36 <= 0;
      __delay_data_42 <= 0;
      __delay_data_46 <= 0;
      _sra_data_19 <= 0;
      __delay_data_37 <= 0;
      __delay_data_38 <= 0;
      __delay_data_43 <= 0;
      __delay_data_47 <= 0;
      _cond_data_21 <= 0;
      __delay_data_44 <= 0;
      __delay_data_48 <= 0;
      _cond_data_24 <= 0;
    end else begin
      _pointer_data_2 <= xdata[6'sd31];
      _slice_data_7 <= ydata[3'd2:1'd0];
      _eq_data_23 <= ydata == 1'sd0;
      __delay_data_25 <= xdata;
      __delay_data_28 <= ydata;
      _minus_data_8 <= _slice_data_7 - 2'sd1;
      __delay_data_26 <= __delay_data_25;
      __delay_data_29 <= __delay_data_28;
      __delay_data_33 <= _pointer_data_2;
      __delay_data_39 <= _eq_data_23;
      _sll_data_10 <= 2'sd1 << _minus_data_8;
      __delay_data_27 <= __delay_data_26;
      __delay_data_30 <= __delay_data_29;
      __delay_data_34 <= __delay_data_33;
      __delay_data_40 <= __delay_data_39;
      _plus_data_16 <= __delay_data_27 + _sll_data_10;
      __delay_data_31 <= __delay_data_30;
      __delay_data_35 <= __delay_data_34;
      __delay_data_41 <= __delay_data_40;
      __delay_data_45 <= __delay_data_27;
      _minus_data_17 <= _plus_data_16 - 2'sd1;
      _srl_data_20 <= _plus_data_16 >> __delay_data_31;
      __delay_data_32 <= __delay_data_31;
      __delay_data_36 <= __delay_data_35;
      __delay_data_42 <= __delay_data_41;
      __delay_data_46 <= __delay_data_45;
      _sra_data_19 <= _minus_data_17 >>> __delay_data_32;
      __delay_data_37 <= __delay_data_36;
      __delay_data_38 <= _srl_data_20;
      __delay_data_43 <= __delay_data_42;
      __delay_data_47 <= __delay_data_46;
      _cond_data_21 <= (__delay_data_37)? _sra_data_19 : __delay_data_38;
      __delay_data_44 <= __delay_data_43;
      __delay_data_48 <= __delay_data_47;
      _cond_data_24 <= (__delay_data_44)? __delay_data_48 : _cond_data_21;
    end
  end


endmodule
"""


def test():
    veriloggen.reset()
    test_module = stream_sra_round.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
