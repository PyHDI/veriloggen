from __future__ import absolute_import
from __future__ import print_function
import types_bram_read_dataflow

expected_verilog = """
module test;

  reg CLK;
  reg RST;

  main
  uut
  (
    .CLK(CLK),
    .RST(RST)
  );


  initial begin
    $dumpfile("uut.vcd");
    $dumpvars(0, uut, CLK, RST);
  end


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
    #100000;
    $finish;
  end


endmodule



module main
(
  input CLK,
  input RST
);

  reg [14-1:0] mybram_0_addr;
  wire [32-1:0] mybram_0_rdata;
  reg [32-1:0] mybram_0_wdata;
  reg mybram_0_wenable;
  reg [14-1:0] mybram_1_addr;
  wire [32-1:0] mybram_1_rdata;
  reg [32-1:0] mybram_1_wdata;
  reg mybram_1_wenable;

  mybram
  inst_mybram
  (
    .CLK(CLK),
    .mybram_0_addr(mybram_0_addr),
    .mybram_0_rdata(mybram_0_rdata),
    .mybram_0_wdata(mybram_0_wdata),
    .mybram_0_wenable(mybram_0_wenable),
    .mybram_1_addr(mybram_1_addr),
    .mybram_1_rdata(mybram_1_rdata),
    .mybram_1_wdata(mybram_1_wdata),
    .mybram_1_wenable(mybram_1_wenable)
  );

  reg [32-1:0] fsm;
  localparam fsm_init = 0;
  reg [32-1:0] _tmp_data_0;
  reg _tmp_valid_0;
  wire _tmp_ready_0;
  assign _tmp_ready_0 = (_tmp_ready_1 || !_tmp_valid_1) && _tmp_valid_0;
  reg [32-1:0] _tmp_data_1;
  reg _tmp_valid_1;
  wire _tmp_ready_1;
  wire [32-1:0] value_data;
  wire value_valid;
  wire value_ready;
  assign value_data = _tmp_data_1;
  assign value_valid = _tmp_valid_1;
  assign _tmp_ready_1 = value_ready;
  reg [8-1:0] _tmp_2;
  reg _tmp_3;
  assign value_ready = (fsm == 0) && !_tmp_3;
  reg _mybram_cond_0_1;
  reg _tmp_4;
  reg _tmp_5;
  wire _tmp_6;
  wire _tmp_7;
  assign _tmp_6 = 1 && 1;
  assign _tmp_7 = 1 && 1;
  localparam _tmp_8 = 1;
  wire [_tmp_8-1:0] _tmp_9;
  assign _tmp_9 = (_tmp_6 || !_tmp_4) && (_tmp_7 || !_tmp_5);
  reg [_tmp_8-1:0] __tmp_9_1;
  wire [32-1:0] _tmp_10;
  reg [32-1:0] __tmp_10_1;
  assign _tmp_10 = (__tmp_9_1)? mybram_1_rdata : __tmp_10_1;
  reg [7-1:0] _tmp_11;
  reg _tmp_12;
  reg _tmp_13;
  reg _tmp_14;
  reg _tmp_15;
  wire [32-1:0] rdata_data;
  wire rdata_valid;
  assign rdata_data = _tmp_10;
  assign rdata_valid = _tmp_4;
  wire [1-1:0] rlast_data;
  wire rlast_valid;
  assign rlast_data = _tmp_15;
  assign rlast_valid = _tmp_5;
  reg [32-1:0] sum;
  reg _seq_cond_0_1;

  always @(posedge CLK) begin
    if(RST) begin
      mybram_1_wdata <= 0;
      mybram_1_wenable <= 0;
      mybram_0_addr <= 0;
      mybram_0_wdata <= 0;
      mybram_0_wenable <= 0;
      _tmp_2 <= 0;
      _tmp_3 <= 0;
      _mybram_cond_0_1 <= 0;
      __tmp_9_1 <= 0;
      __tmp_10_1 <= 0;
      _tmp_15 <= 0;
      _tmp_4 <= 0;
      _tmp_5 <= 0;
      _tmp_13 <= 0;
      _tmp_14 <= 0;
      _tmp_12 <= 0;
      mybram_1_addr <= 0;
      _tmp_11 <= 0;
    end else begin
      if(_mybram_cond_0_1) begin
        mybram_0_wenable <= 0;
        _tmp_3 <= 0;
      end 
      mybram_1_wdata <= 0;
      mybram_1_wenable <= 0;
      if(value_valid && ((fsm == 0) && !_tmp_3) && (_tmp_2 == 0)) begin
        mybram_0_addr <= 0;
        mybram_0_wdata <= value_data;
        mybram_0_wenable <= 1;
        _tmp_2 <= 63;
      end 
      if(value_valid && ((fsm == 0) && !_tmp_3) && (_tmp_2 > 0)) begin
        mybram_0_addr <= mybram_0_addr + 1;
        mybram_0_wdata <= value_data;
        mybram_0_wenable <= 1;
        _tmp_2 <= _tmp_2 - 1;
      end 
      if(value_valid && ((fsm == 0) && !_tmp_3) && (_tmp_2 == 1)) begin
        _tmp_3 <= 1;
      end 
      _mybram_cond_0_1 <= 1;
      __tmp_9_1 <= _tmp_9;
      __tmp_10_1 <= _tmp_10;
      if((_tmp_6 || !_tmp_4) && (_tmp_7 || !_tmp_5) && _tmp_13) begin
        _tmp_15 <= 0;
        _tmp_4 <= 0;
        _tmp_5 <= 0;
        _tmp_13 <= 0;
      end 
      if((_tmp_6 || !_tmp_4) && (_tmp_7 || !_tmp_5) && _tmp_12) begin
        _tmp_4 <= 1;
        _tmp_5 <= 1;
        _tmp_15 <= _tmp_14;
        _tmp_14 <= 0;
        _tmp_12 <= 0;
        _tmp_13 <= 1;
      end 
      if((_tmp_6 || !_tmp_4) && (_tmp_7 || !_tmp_5) && (fsm == 2) && (_tmp_11 == 0) && !_tmp_14 && !_tmp_15) begin
        mybram_1_addr <= 0;
        _tmp_11 <= 31;
        _tmp_12 <= 1;
      end 
      if((_tmp_6 || !_tmp_4) && (_tmp_7 || !_tmp_5) && (_tmp_11 > 0)) begin
        mybram_1_addr <= mybram_1_addr + 1;
        _tmp_11 <= _tmp_11 - 1;
        _tmp_12 <= 1;
        _tmp_14 <= 0;
      end 
      if((_tmp_6 || !_tmp_4) && (_tmp_7 || !_tmp_5) && (_tmp_11 == 1)) begin
        _tmp_14 <= 1;
      end 
    end
  end

  localparam fsm_1 = 1;
  localparam fsm_2 = 2;
  localparam fsm_3 = 3;

  always @(posedge CLK) begin
    if(RST) begin
      fsm <= fsm_init;
    end else begin
      case(fsm)
        fsm_init: begin
          if(_tmp_3) begin
            fsm <= fsm_1;
          end 
        end
        fsm_1: begin
          fsm <= fsm_2;
        end
        fsm_2: begin
          if(_tmp_15) begin
            fsm <= fsm_3;
          end 
        end
      endcase
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      _tmp_data_0 <= 1'd0;
      _tmp_valid_0 <= 0;
      _tmp_data_1 <= 0;
      _tmp_valid_1 <= 0;
    end else begin
      if((_tmp_ready_0 || !_tmp_valid_0) && 1 && 1) begin
        _tmp_data_0 <= _tmp_data_0 + 2'd1;
      end 
      if(_tmp_valid_0 && _tmp_ready_0) begin
        _tmp_valid_0 <= 0;
      end 
      if((_tmp_ready_0 || !_tmp_valid_0) && 1) begin
        _tmp_valid_0 <= 1;
      end 
      if((_tmp_ready_1 || !_tmp_valid_1) && _tmp_ready_0 && _tmp_valid_0) begin
        _tmp_data_1 <= _tmp_data_0 - 2'd1;
      end 
      if(_tmp_valid_1 && _tmp_ready_1) begin
        _tmp_valid_1 <= 0;
      end 
      if((_tmp_ready_1 || !_tmp_valid_1) && _tmp_ready_0) begin
        _tmp_valid_1 <= _tmp_valid_0;
      end 
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      sum <= 0;
      _seq_cond_0_1 <= 0;
    end else begin
      if(_seq_cond_0_1) begin
        $display("sum=%d expected_sum=%d", sum, 496);
      end 
      if(rdata_valid) begin
        sum <= sum + rdata_data;
      end 
      _seq_cond_0_1 <= rdata_valid && (rlast_data == 1);
    end
  end


endmodule



module mybram
(
  input CLK,
  input [14-1:0] mybram_0_addr,
  output [32-1:0] mybram_0_rdata,
  input [32-1:0] mybram_0_wdata,
  input mybram_0_wenable,
  input [14-1:0] mybram_1_addr,
  output [32-1:0] mybram_1_rdata,
  input [32-1:0] mybram_1_wdata,
  input mybram_1_wenable
);

  reg [14-1:0] mybram_0_daddr;
  reg [14-1:0] mybram_1_daddr;
  reg [32-1:0] mem [0:16384-1];

  always @(posedge CLK) begin
    if(mybram_0_wenable) begin
      mem[mybram_0_addr] <= mybram_0_wdata;
    end 
    mybram_0_daddr <= mybram_0_addr;
  end

  assign mybram_0_rdata = mem[mybram_0_daddr];

  always @(posedge CLK) begin
    if(mybram_1_wenable) begin
      mem[mybram_1_addr] <= mybram_1_wdata;
    end 
    mybram_1_daddr <= mybram_1_addr;
  end

  assign mybram_1_rdata = mem[mybram_1_daddr];

endmodule
"""


def test():
    test_module = types_bram_read_dataflow.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
