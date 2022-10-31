from __future__ import absolute_import
from __future__ import print_function

import os
import veriloggen
import thread_multibank_ram_style


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
    #20000;
    $finish;
  end


endmodule



module blinkled
(
  input CLK,
  input RST
);

  wire [10-1:0] myram_0_0_addr;
  wire [32-1:0] myram_0_0_rdata;
  wire [32-1:0] myram_0_0_wdata;
  wire myram_0_0_wenable;
  wire myram_0_0_enable;

  myram_0
  inst_myram_0
  (
    .CLK(CLK),
    .myram_0_0_addr(myram_0_0_addr),
    .myram_0_0_rdata(myram_0_0_rdata),
    .myram_0_0_wdata(myram_0_0_wdata),
    .myram_0_0_wenable(myram_0_0_wenable),
    .myram_0_0_enable(myram_0_0_enable)
  );

  wire [10-1:0] myram_1_0_addr;
  wire [32-1:0] myram_1_0_rdata;
  wire [32-1:0] myram_1_0_wdata;
  wire myram_1_0_wenable;
  wire myram_1_0_enable;

  myram_1
  inst_myram_1
  (
    .CLK(CLK),
    .myram_1_0_addr(myram_1_0_addr),
    .myram_1_0_rdata(myram_1_0_rdata),
    .myram_1_0_wdata(myram_1_0_wdata),
    .myram_1_0_wenable(myram_1_0_wenable),
    .myram_1_0_enable(myram_1_0_enable)
  );

  wire [10-1:0] myram_2_0_addr;
  wire [32-1:0] myram_2_0_rdata;
  wire [32-1:0] myram_2_0_wdata;
  wire myram_2_0_wenable;
  wire myram_2_0_enable;

  myram_2
  inst_myram_2
  (
    .CLK(CLK),
    .myram_2_0_addr(myram_2_0_addr),
    .myram_2_0_rdata(myram_2_0_rdata),
    .myram_2_0_wdata(myram_2_0_wdata),
    .myram_2_0_wenable(myram_2_0_wenable),
    .myram_2_0_enable(myram_2_0_enable)
  );

  wire [10-1:0] myram_3_0_addr;
  wire [32-1:0] myram_3_0_rdata;
  wire [32-1:0] myram_3_0_wdata;
  wire myram_3_0_wenable;
  wire myram_3_0_enable;

  myram_3
  inst_myram_3
  (
    .CLK(CLK),
    .myram_3_0_addr(myram_3_0_addr),
    .myram_3_0_rdata(myram_3_0_rdata),
    .myram_3_0_wdata(myram_3_0_wdata),
    .myram_3_0_wenable(myram_3_0_wenable),
    .myram_3_0_enable(myram_3_0_enable)
  );

  reg [32-1:0] th_blink;
  localparam th_blink_init = 0;
  reg signed [32-1:0] _th_blink_times_0;
  reg signed [32-1:0] _th_blink_all_ok_1;
  reg signed [32-1:0] _th_blink_write_sum_2;
  reg signed [32-1:0] _th_blink_i_3;
  reg signed [32-1:0] _th_blink_wdata_4;
  wire [2-1:0] write_rtl_bank_0;
  assign write_rtl_bank_0 = _th_blink_i_3;
  assign myram_0_0_wdata = ((th_blink == 6) && (write_rtl_bank_0 == 0))? _th_blink_wdata_4 : 'hx;
  assign myram_0_0_wenable = ((th_blink == 6) && (write_rtl_bank_0 == 0))? 1'd1 : 0;
  assign myram_1_0_wdata = ((th_blink == 6) && (write_rtl_bank_0 == 1))? _th_blink_wdata_4 : 'hx;
  assign myram_1_0_wenable = ((th_blink == 6) && (write_rtl_bank_0 == 1))? 1'd1 : 0;
  assign myram_2_0_wdata = ((th_blink == 6) && (write_rtl_bank_0 == 2))? _th_blink_wdata_4 : 'hx;
  assign myram_2_0_wenable = ((th_blink == 6) && (write_rtl_bank_0 == 2))? 1'd1 : 0;
  assign myram_3_0_wdata = ((th_blink == 6) && (write_rtl_bank_0 == 3))? _th_blink_wdata_4 : 'hx;
  assign myram_3_0_wenable = ((th_blink == 6) && (write_rtl_bank_0 == 3))? 1'd1 : 0;
  reg signed [32-1:0] _th_blink_read_sum_5;
  wire [2-1:0] read_rtl_bank_1;
  assign read_rtl_bank_1 = _th_blink_i_3;
  reg [2-1:0] _tmp_2;
  assign myram_0_0_addr = (th_blink == 13)? _th_blink_i_3 >> 2 : 
                          ((th_blink == 6) && (write_rtl_bank_0 == 0))? _th_blink_i_3 >> 2 : 'hx;
  assign myram_0_0_enable = (th_blink == 13)? 1'd1 : 
                            ((th_blink == 6) && (write_rtl_bank_0 == 0))? 1'd1 : 0;
  localparam _tmp_3 = 1;
  wire [_tmp_3-1:0] _tmp_4;
  assign _tmp_4 = th_blink == 13;
  reg [_tmp_3-1:0] __tmp_4_1;
  assign myram_1_0_addr = (th_blink == 13)? _th_blink_i_3 >> 2 : 
                          ((th_blink == 6) && (write_rtl_bank_0 == 1))? _th_blink_i_3 >> 2 : 'hx;
  assign myram_1_0_enable = (th_blink == 13)? 1'd1 : 
                            ((th_blink == 6) && (write_rtl_bank_0 == 1))? 1'd1 : 0;
  localparam _tmp_5 = 1;
  wire [_tmp_5-1:0] _tmp_6;
  assign _tmp_6 = th_blink == 13;
  reg [_tmp_5-1:0] __tmp_6_1;
  assign myram_2_0_addr = (th_blink == 13)? _th_blink_i_3 >> 2 : 
                          ((th_blink == 6) && (write_rtl_bank_0 == 2))? _th_blink_i_3 >> 2 : 'hx;
  assign myram_2_0_enable = (th_blink == 13)? 1'd1 : 
                            ((th_blink == 6) && (write_rtl_bank_0 == 2))? 1'd1 : 0;
  localparam _tmp_7 = 1;
  wire [_tmp_7-1:0] _tmp_8;
  assign _tmp_8 = th_blink == 13;
  reg [_tmp_7-1:0] __tmp_8_1;
  assign myram_3_0_addr = (th_blink == 13)? _th_blink_i_3 >> 2 : 
                          ((th_blink == 6) && (write_rtl_bank_0 == 3))? _th_blink_i_3 >> 2 : 'hx;
  assign myram_3_0_enable = (th_blink == 13)? 1'd1 : 
                            ((th_blink == 6) && (write_rtl_bank_0 == 3))? 1'd1 : 0;
  localparam _tmp_9 = 1;
  wire [_tmp_9-1:0] _tmp_10;
  assign _tmp_10 = th_blink == 13;
  reg [_tmp_9-1:0] __tmp_10_1;
  wire signed [32-1:0] read_rtl_rdata_11;
  wire read_rtl_rvalid_12;
  assign read_rtl_rdata_11 = (_tmp_2 == 0)? myram_0_0_rdata : 
                             (_tmp_2 == 1)? myram_1_0_rdata : 
                             (_tmp_2 == 2)? myram_2_0_rdata : 
                             (_tmp_2 == 3)? myram_3_0_rdata : 0;
  assign read_rtl_rvalid_12 = __tmp_4_1;
  reg signed [32-1:0] read_rdata_13;
  reg signed [32-1:0] _th_blink_rdata_6;

  always @(posedge CLK) begin
    if(RST) begin
      __tmp_4_1 <= 0;
    end else begin
      __tmp_4_1 <= _tmp_4;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      __tmp_6_1 <= 0;
    end else begin
      __tmp_6_1 <= _tmp_6;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      __tmp_8_1 <= 0;
    end else begin
      __tmp_8_1 <= _tmp_8;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      __tmp_10_1 <= 0;
    end else begin
      __tmp_10_1 <= _tmp_10;
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

  always @(posedge CLK) begin
    if(RST) begin
      th_blink <= th_blink_init;
      _th_blink_times_0 <= 0;
      _th_blink_all_ok_1 <= 0;
      _th_blink_write_sum_2 <= 0;
      _th_blink_i_3 <= 0;
      _th_blink_wdata_4 <= 0;
      _th_blink_read_sum_5 <= 0;
      read_rdata_13 <= 0;
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
          if(_th_blink_i_3 < (_th_blink_times_0 << 2)) begin
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
          if(_th_blink_i_3 < (_th_blink_times_0 << 2)) begin
            th_blink <= th_blink_13;
          end else begin
            th_blink <= th_blink_18;
          end
        end
        th_blink_13: begin
          if(read_rtl_rvalid_12) begin
            read_rdata_13 <= read_rtl_rdata_11;
          end 
          if(read_rtl_rvalid_12) begin
            th_blink <= th_blink_14;
          end 
        end
        th_blink_14: begin
          _th_blink_rdata_6 <= read_rdata_13;
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
          _th_blink_i_3 <= _th_blink_i_3 + 1;
          th_blink <= th_blink_12;
        end
        th_blink_18: begin
          $display("read_sum = %d", _th_blink_read_sum_5);
          th_blink <= th_blink_19;
        end
        th_blink_19: begin
          if(_th_blink_read_sum_5 !== _th_blink_write_sum_2) begin
            th_blink <= th_blink_20;
          end else begin
            th_blink <= th_blink_21;
          end
        end
        th_blink_20: begin
          _th_blink_all_ok_1 <= 0;
          th_blink <= th_blink_21;
        end
        th_blink_21: begin
          if(_th_blink_all_ok_1) begin
            th_blink <= th_blink_22;
          end else begin
            th_blink <= th_blink_24;
          end
        end
        th_blink_22: begin
          $display("# verify: PASSED");
          th_blink <= th_blink_23;
        end
        th_blink_23: begin
          th_blink <= th_blink_25;
        end
        th_blink_24: begin
          $display("# verify: FAILED");
          th_blink <= th_blink_25;
        end
      endcase
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      _tmp_2 <= 0;
    end else begin
      if(th_blink == 13) begin
        _tmp_2 <= read_rtl_bank_1;
      end 
    end
  end


endmodule



module myram_0
(
  input CLK,
  input [10-1:0] myram_0_0_addr,
  output [32-1:0] myram_0_0_rdata,
  input [32-1:0] myram_0_0_wdata,
  input myram_0_0_wenable,
  input myram_0_0_enable
);

  reg [32-1:0] myram_0_0_rdata_out;
  assign myram_0_0_rdata = myram_0_0_rdata_out;
  (* ram_style = "block" *)
  reg [32-1:0] mem [0:1024-1];

  always @(posedge CLK) begin
    if(myram_0_0_enable) begin
      if(myram_0_0_wenable) begin
        mem[myram_0_0_addr] <= myram_0_0_wdata;
        myram_0_0_rdata_out <= myram_0_0_wdata;
      end else begin
        myram_0_0_rdata_out <= mem[myram_0_0_addr];
      end
    end 
  end


endmodule



module myram_1
(
  input CLK,
  input [10-1:0] myram_1_0_addr,
  output [32-1:0] myram_1_0_rdata,
  input [32-1:0] myram_1_0_wdata,
  input myram_1_0_wenable,
  input myram_1_0_enable
);

  reg [32-1:0] myram_1_0_rdata_out;
  assign myram_1_0_rdata = myram_1_0_rdata_out;
  (* ram_style = "block" *)
  reg [32-1:0] mem [0:1024-1];

  always @(posedge CLK) begin
    if(myram_1_0_enable) begin
      if(myram_1_0_wenable) begin
        mem[myram_1_0_addr] <= myram_1_0_wdata;
        myram_1_0_rdata_out <= myram_1_0_wdata;
      end else begin
        myram_1_0_rdata_out <= mem[myram_1_0_addr];
      end
    end 
  end


endmodule



module myram_2
(
  input CLK,
  input [10-1:0] myram_2_0_addr,
  output [32-1:0] myram_2_0_rdata,
  input [32-1:0] myram_2_0_wdata,
  input myram_2_0_wenable,
  input myram_2_0_enable
);

  reg [32-1:0] myram_2_0_rdata_out;
  assign myram_2_0_rdata = myram_2_0_rdata_out;
  (* ram_style = "block" *)
  reg [32-1:0] mem [0:1024-1];

  always @(posedge CLK) begin
    if(myram_2_0_enable) begin
      if(myram_2_0_wenable) begin
        mem[myram_2_0_addr] <= myram_2_0_wdata;
        myram_2_0_rdata_out <= myram_2_0_wdata;
      end else begin
        myram_2_0_rdata_out <= mem[myram_2_0_addr];
      end
    end 
  end


endmodule



module myram_3
(
  input CLK,
  input [10-1:0] myram_3_0_addr,
  output [32-1:0] myram_3_0_rdata,
  input [32-1:0] myram_3_0_wdata,
  input myram_3_0_wenable,
  input myram_3_0_enable
);

  reg [32-1:0] myram_3_0_rdata_out;
  assign myram_3_0_rdata = myram_3_0_rdata_out;
  (* ram_style = "block" *)
  reg [32-1:0] mem [0:1024-1];

  always @(posedge CLK) begin
    if(myram_3_0_enable) begin
      if(myram_3_0_wenable) begin
        mem[myram_3_0_addr] <= myram_3_0_wdata;
        myram_3_0_rdata_out <= myram_3_0_wdata;
      end else begin
        myram_3_0_rdata_out <= mem[myram_3_0_addr];
      end
    end 
  end


endmodule
"""


def test(request):
    veriloggen.reset()

    simtype = request.config.getoption('--sim')

    rslt = thread_multibank_ram_style.run(filename=None, simtype=simtype,
                                          outputfile=os.path.splitext(os.path.basename(__file__))[0] + '.out')

    verify_rslt = rslt.splitlines()[-1]
    assert(verify_rslt == '# verify: PASSED')

    veriloggen.reset()

    test_module = thread_multibank_ram_style.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator

    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
