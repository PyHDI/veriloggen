from __future__ import absolute_import
from __future__ import print_function

import os
import veriloggen
import thread_ram_style


expected_verilog = """
module test;

  reg CLK;
  reg RST;

  blinkled
  uut
  (
    .CLK(CLK),
    .RST(RST)
  );


  initial begin
    CLK = 0;
    forever begin
      #5 CLK = !CLK;
    end
  end


  initial begin
    RST = 0;
    #100;
    RST = 1;
    #100;
    RST = 0;
    #10000;
    $finish;
  end


endmodule



module blinkled
(
  input CLK,
  input RST
);

  wire [10-1:0] myram_0_addr;
  wire [32-1:0] myram_0_rdata;
  wire [32-1:0] myram_0_wdata;
  wire myram_0_wenable;
  wire myram_0_enable;

  myram
  inst_myram
  (
    .CLK(CLK),
    .myram_0_addr(myram_0_addr),
    .myram_0_rdata(myram_0_rdata),
    .myram_0_wdata(myram_0_wdata),
    .myram_0_wenable(myram_0_wenable),
    .myram_0_enable(myram_0_enable)
  );

  reg [32-1:0] th_blink;
  localparam th_blink_init = 0;
  reg signed [32-1:0] _th_blink_times_0;
  reg signed [32-1:0] _th_blink_all_ok_1;
  reg signed [32-1:0] _th_blink_write_sum_2;
  reg signed [32-1:0] _th_blink_i_3;
  reg signed [32-1:0] _th_blink_wdata_4;
  assign myram_0_wdata = (th_blink == 6)? _th_blink_wdata_4 : 'hx;
  assign myram_0_wenable = (th_blink == 6)? 1'd1 : 0;
  reg signed [32-1:0] _th_blink_read_sum_5;
  assign myram_0_addr = (th_blink == 13)? _th_blink_i_3 : 
                        (th_blink == 6)? _th_blink_i_3 : 'hx;
  assign myram_0_enable = (th_blink == 13)? 1'd1 : 
                          (th_blink == 6)? 1'd1 : 0;
  localparam _tmp_0 = 1;
  wire [_tmp_0-1:0] _tmp_1;
  assign _tmp_1 = th_blink == 13;
  reg [_tmp_0-1:0] __tmp_1_1;
  reg signed [32-1:0] read_rdata_2;
  reg signed [32-1:0] _th_blink_rdata_6;

  always @(posedge CLK) begin
    if(RST) begin
      __tmp_1_1 <= 0;
    end else begin
      __tmp_1_1 <= _tmp_1;
    end
  end

  localparam th_blink_1 = 1;
  localparam th_blink_2 = 2;
  localparam th_blink_3 = 3;
  localparam th_blink_4 = 4;
  localparam th_blink_5 = 5;
  localparam th_blink_6 = 6;
  localparam th_blink_7 = 7;
  localparam th_blink_8 = 8;
  localparam th_blink_9 = 9;
  localparam th_blink_10 = 10;
  localparam th_blink_11 = 11;
  localparam th_blink_12 = 12;
  localparam th_blink_13 = 13;
  localparam th_blink_14 = 14;
  localparam th_blink_15 = 15;
  localparam th_blink_16 = 16;
  localparam th_blink_17 = 17;
  localparam th_blink_18 = 18;
  localparam th_blink_19 = 19;
  localparam th_blink_20 = 20;
  localparam th_blink_21 = 21;
  localparam th_blink_22 = 22;
  localparam th_blink_23 = 23;
  localparam th_blink_24 = 24;
  localparam th_blink_25 = 25;
  localparam th_blink_26 = 26;
  localparam th_blink_27 = 27;

  always @(posedge CLK) begin
    if(RST) begin
      th_blink <= th_blink_init;
      _th_blink_times_0 <= 0;
      _th_blink_all_ok_1 <= 0;
      _th_blink_write_sum_2 <= 0;
      _th_blink_i_3 <= 0;
      _th_blink_wdata_4 <= 0;
      _th_blink_read_sum_5 <= 0;
      read_rdata_2 <= 0;
      _th_blink_rdata_6 <= 0;
    end else begin
      case(th_blink)
        th_blink_init: begin
          _th_blink_times_0 <= 10;
          th_blink <= th_blink_1;
        end
        th_blink_1: begin
          _th_blink_all_ok_1 <= 1;
          th_blink <= th_blink_2;
        end
        th_blink_2: begin
          _th_blink_write_sum_2 <= 0;
          th_blink <= th_blink_3;
        end
        th_blink_3: begin
          _th_blink_i_3 <= 0;
          th_blink <= th_blink_4;
        end
        th_blink_4: begin
          if(_th_blink_i_3 < _th_blink_times_0) begin
            th_blink <= th_blink_5;
          end else begin
            th_blink <= th_blink_10;
          end
        end
        th_blink_5: begin
          _th_blink_wdata_4 <= _th_blink_i_3;
          th_blink <= th_blink_6;
        end
        th_blink_6: begin
          th_blink <= th_blink_7;
        end
        th_blink_7: begin
          _th_blink_write_sum_2 <= _th_blink_write_sum_2 + _th_blink_wdata_4;
          th_blink <= th_blink_8;
        end
        th_blink_8: begin
          $display("wdata = %d", _th_blink_wdata_4);
          th_blink <= th_blink_9;
        end
        th_blink_9: begin
          _th_blink_i_3 <= _th_blink_i_3 + 1;
          th_blink <= th_blink_4;
        end
        th_blink_10: begin
          _th_blink_read_sum_5 <= 0;
          th_blink <= th_blink_11;
        end
        th_blink_11: begin
          _th_blink_i_3 <= 0;
          th_blink <= th_blink_12;
        end
        th_blink_12: begin
          if(_th_blink_i_3 < _th_blink_times_0) begin
            th_blink <= th_blink_13;
          end else begin
            th_blink <= th_blink_20;
          end
        end
        th_blink_13: begin
          if(__tmp_1_1) begin
            read_rdata_2 <= myram_0_rdata;
          end 
          if(__tmp_1_1) begin
            th_blink <= th_blink_14;
          end 
        end
        th_blink_14: begin
          _th_blink_rdata_6 <= read_rdata_2;
          th_blink <= th_blink_15;
        end
        th_blink_15: begin
          _th_blink_read_sum_5 <= _th_blink_read_sum_5 + _th_blink_rdata_6;
          th_blink <= th_blink_16;
        end
        th_blink_16: begin
          $display("rdata = %d", _th_blink_rdata_6);
          th_blink <= th_blink_17;
        end
        th_blink_17: begin
          if(_th_blink_rdata_6 !== _th_blink_i_3) begin
            th_blink <= th_blink_18;
          end else begin
            th_blink <= th_blink_19;
          end
        end
        th_blink_18: begin
          _th_blink_all_ok_1 <= 0;
          th_blink <= th_blink_19;
        end
        th_blink_19: begin
          _th_blink_i_3 <= _th_blink_i_3 + 1;
          th_blink <= th_blink_12;
        end
        th_blink_20: begin
          $display("read_sum = %d", _th_blink_read_sum_5);
          th_blink <= th_blink_21;
        end
        th_blink_21: begin
          if(_th_blink_read_sum_5 !== _th_blink_write_sum_2) begin
            th_blink <= th_blink_22;
          end else begin
            th_blink <= th_blink_23;
          end
        end
        th_blink_22: begin
          _th_blink_all_ok_1 <= 0;
          th_blink <= th_blink_23;
        end
        th_blink_23: begin
          if(_th_blink_all_ok_1) begin
            th_blink <= th_blink_24;
          end else begin
            th_blink <= th_blink_26;
          end
        end
        th_blink_24: begin
          $display("# verify: PASSED");
          th_blink <= th_blink_25;
        end
        th_blink_25: begin
          th_blink <= th_blink_27;
        end
        th_blink_26: begin
          $display("# verify: FAILED");
          th_blink <= th_blink_27;
        end
      endcase
    end
  end


endmodule



module myram
(
  input CLK,
  input [10-1:0] myram_0_addr,
  output [32-1:0] myram_0_rdata,
  input [32-1:0] myram_0_wdata,
  input myram_0_wenable,
  input myram_0_enable
);

  reg [32-1:0] myram_0_rdata_out;
  assign myram_0_rdata = myram_0_rdata_out;
  (* ram_style = "block" *)
  reg [32-1:0] mem [0:1024-1];

  always @(posedge CLK) begin
    if(myram_0_enable) begin
      if(myram_0_wenable) begin
        mem[myram_0_addr] <= myram_0_wdata;
        myram_0_rdata_out <= myram_0_wdata;
      end else begin
        myram_0_rdata_out <= mem[myram_0_addr];
      end
    end 
  end


endmodule
"""


def test(request):
    veriloggen.reset()

    simtype = request.config.getoption('--sim')

    rslt = thread_ram_style.run(filename=None, simtype=simtype,
                                outputfile=os.path.splitext(os.path.basename(__file__))[0] + '.out')

    verify_rslt = rslt.splitlines()[-1]
    assert(verify_rslt == '# verify: PASSED')

    veriloggen.reset()

    test_module = thread_ram_style.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator

    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
