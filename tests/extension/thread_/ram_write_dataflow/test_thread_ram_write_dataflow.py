from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import thread_ram_write_dataflow

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

  reg [14-1:0] myram_0_addr;
  wire [32-1:0] myram_0_rdata;
  reg [32-1:0] myram_0_wdata;
  reg myram_0_wenable;
  reg [14-1:0] myram_1_addr;
  wire [32-1:0] myram_1_rdata;
  reg [32-1:0] myram_1_wdata;
  reg myram_1_wenable;

  myram
  inst_myram
  (
    .CLK(CLK),
    .myram_0_addr(myram_0_addr),
    .myram_0_rdata(myram_0_rdata),
    .myram_0_wdata(myram_0_wdata),
    .myram_0_wenable(myram_0_wenable),
    .myram_1_addr(myram_1_addr),
    .myram_1_rdata(myram_1_rdata),
    .myram_1_wdata(myram_1_wdata),
    .myram_1_wenable(myram_1_wenable)
  );

  reg [32-1:0] fsm;
  localparam fsm_init = 0;
  reg [8-1:0] _tmp_0;
  reg _tmp_1;
  wire [32-1:0] _dataflow_minus_odata_4;
  wire _dataflow_minus_ovalid_4;
  wire _dataflow_minus_oready_4;
  assign _dataflow_minus_oready_4 = (_tmp_0 > 0) && !_tmp_1;
  reg _myram_cond_0_1;
  reg [32-1:0] sum;
  reg _seq_cond_0_1;
  reg _seq_cond_0_2;

  always @(posedge CLK) begin
    if(RST) begin
      myram_1_wdata <= 0;
      myram_1_wenable <= 0;
      myram_0_addr <= 0;
      _tmp_0 <= 0;
      myram_0_wdata <= 0;
      myram_0_wenable <= 0;
      _tmp_1 <= 0;
      _myram_cond_0_1 <= 0;
    end else begin
      if(_myram_cond_0_1) begin
        myram_0_wenable <= 0;
        _tmp_1 <= 0;
      end 
      myram_1_wdata <= 0;
      myram_1_wenable <= 0;
      if((fsm == 1) && (_tmp_0 == 0)) begin
        myram_0_addr <= -1;
        _tmp_0 <= 64;
      end 
      if(_dataflow_minus_ovalid_4 && ((_tmp_0 > 0) && !_tmp_1) && (_tmp_0 > 0)) begin
        myram_0_addr <= myram_0_addr + 1;
        myram_0_wdata <= _dataflow_minus_odata_4;
        myram_0_wenable <= 1;
        _tmp_0 <= _tmp_0 - 1;
      end 
      if(_dataflow_minus_ovalid_4 && ((_tmp_0 > 0) && !_tmp_1) && (_tmp_0 == 1)) begin
        _tmp_1 <= 1;
      end 
      _myram_cond_0_1 <= 1;
    end
  end

  reg [32-1:0] _dataflow_counter_data_2;
  reg _dataflow_counter_valid_2;
  wire _dataflow_counter_ready_2;
  reg [9-1:0] _dataflow_counter_count_2;
  reg [32-1:0] _dataflow_minus_data_4;
  reg _dataflow_minus_valid_4;
  wire _dataflow_minus_ready_4;
  assign _dataflow_counter_ready_2 = (_dataflow_minus_ready_4 || !_dataflow_minus_valid_4) && _dataflow_counter_valid_2;
  assign _dataflow_minus_odata_4 = _dataflow_minus_data_4;
  assign _dataflow_minus_ovalid_4 = _dataflow_minus_valid_4;
  assign _dataflow_minus_ready_4 = _dataflow_minus_oready_4;

  always @(posedge CLK) begin
    if(RST) begin
      _dataflow_counter_data_2 <= -2'sd1;
      _dataflow_counter_count_2 <= 0;
      _dataflow_counter_valid_2 <= 0;
      _dataflow_minus_data_4 <= 0;
      _dataflow_minus_valid_4 <= 0;
    end else begin
      if((_dataflow_counter_ready_2 || !_dataflow_counter_valid_2) && 1 && 1) begin
        _dataflow_counter_data_2 <= _dataflow_counter_data_2 + 1;
      end 
      if((_dataflow_counter_ready_2 || !_dataflow_counter_valid_2) && 1 && 1) begin
        _dataflow_counter_count_2 <= (_dataflow_counter_count_2 == 8'sd64 - 1)? 0 : _dataflow_counter_count_2 + 1;
      end 
      if(_dataflow_counter_valid_2 && _dataflow_counter_ready_2) begin
        _dataflow_counter_valid_2 <= 0;
      end 
      if((_dataflow_counter_ready_2 || !_dataflow_counter_valid_2) && 1) begin
        _dataflow_counter_valid_2 <= 1;
      end 
      if((_dataflow_counter_ready_2 || !_dataflow_counter_valid_2) && 1 && 1 && (_dataflow_counter_count_2 == 0)) begin
        _dataflow_counter_data_2 <= -2'sd1 + 1;
      end 
      if((_dataflow_minus_ready_4 || !_dataflow_minus_valid_4) && _dataflow_counter_ready_2 && _dataflow_counter_valid_2) begin
        _dataflow_minus_data_4 <= _dataflow_counter_data_2 - 2'sd1;
      end 
      if(_dataflow_minus_valid_4 && _dataflow_minus_ready_4) begin
        _dataflow_minus_valid_4 <= 0;
      end 
      if((_dataflow_minus_ready_4 || !_dataflow_minus_valid_4) && _dataflow_counter_ready_2) begin
        _dataflow_minus_valid_4 <= _dataflow_counter_valid_2;
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
          fsm <= fsm_1;
        end
        fsm_1: begin
          fsm <= fsm_2;
        end
        fsm_2: begin
          if(_tmp_1) begin
            fsm <= fsm_3;
          end 
        end
      endcase
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      sum <= 0;
      _seq_cond_0_1 <= 0;
      _seq_cond_0_2 <= 0;
    end else begin
      if(_seq_cond_0_2) begin
        $display("sum=%d expected_sum=%d", sum, 1952);
      end 
      _seq_cond_0_2 <= _seq_cond_0_1;
      if(myram_0_wenable) begin
        sum <= sum + myram_0_wdata;
      end 
      _seq_cond_0_1 <= myram_0_wenable && (myram_0_addr == 63);
    end
  end


endmodule



module myram
(
  input CLK,
  input [14-1:0] myram_0_addr,
  output [32-1:0] myram_0_rdata,
  input [32-1:0] myram_0_wdata,
  input myram_0_wenable,
  input [14-1:0] myram_1_addr,
  output [32-1:0] myram_1_rdata,
  input [32-1:0] myram_1_wdata,
  input myram_1_wenable
);

  reg [14-1:0] myram_0_daddr;
  reg [14-1:0] myram_1_daddr;
  reg [32-1:0] mem [0:16384-1];

  always @(posedge CLK) begin
    if(myram_0_wenable) begin
      mem[myram_0_addr] <= myram_0_wdata;
    end 
    myram_0_daddr <= myram_0_addr;
  end

  assign myram_0_rdata = mem[myram_0_daddr];

  always @(posedge CLK) begin
    if(myram_1_wenable) begin
      mem[myram_1_addr] <= myram_1_wdata;
    end 
    myram_1_daddr <= myram_1_addr;
  end

  assign myram_1_rdata = mem[myram_1_daddr];

endmodule
"""


def test():
    veriloggen.reset()
    test_module = thread_ram_write_dataflow.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
