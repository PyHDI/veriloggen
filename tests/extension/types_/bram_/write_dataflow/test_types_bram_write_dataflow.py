from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import types_bram_write_dataflow

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
    end
  end

  localparam fsm_1 = 1;
  localparam fsm_2 = 2;

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
        $display("sum=%d expected_sum=%d", sum, 2016);
      end 
      if(mybram_0_wenable) begin
        sum <= sum + mybram_0_wdata;
      end 
      _seq_cond_0_1 <= mybram_0_wenable && (mybram_0_addr == 63);
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
    veriloggen.reset()
    test_module = types_bram_write_dataflow.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
