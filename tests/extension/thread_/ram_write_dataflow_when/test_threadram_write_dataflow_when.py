from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import thread_ram_write_dataflow_when

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

  reg [14-1:0] myram_0_addr;
  wire [32-1:0] myram_0_rdata;
  reg [32-1:0] myram_0_wdata;
  reg myram_0_wenable;

  myram
  inst_myram
  (
    .CLK(CLK),
    .myram_0_addr(myram_0_addr),
    .myram_0_rdata(myram_0_rdata),
    .myram_0_wdata(myram_0_wdata),
    .myram_0_wenable(myram_0_wenable)
  );

  reg [32-1:0] fsm;
  localparam fsm_init = 0;
  reg [7-1:0] _tmp_0;
  reg _tmp_1;
  wire _dataflow_tmp_all_valid_2;
  wire [32-1:0] _dataflow_counter_odata_1;
  wire _dataflow_counter_ovalid_1;
  wire _dataflow_counter_oready_1;
  assign _dataflow_counter_oready_1 = (_tmp_0 > 0) && !_tmp_1 && _dataflow_tmp_all_valid_2;
  wire [1-1:0] _dataflow_eq_odata_7;
  wire _dataflow_eq_ovalid_7;
  wire _dataflow_eq_oready_7;
  assign _dataflow_eq_oready_7 = (_tmp_0 > 0) && !_tmp_1 && _dataflow_tmp_all_valid_2;
  assign _dataflow_tmp_all_valid_2 = _dataflow_counter_ovalid_1 && _dataflow_eq_ovalid_7;
  reg _myram_cond_0_1;

  always @(posedge CLK) begin
    if(RST) begin
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
      if((fsm == 0) && (_tmp_0 == 0)) begin
        myram_0_addr <= -1;
        _tmp_0 <= 32;
      end 
      if(_dataflow_eq_odata_7 && (_dataflow_counter_ovalid_1 && ((_tmp_0 > 0) && !_tmp_1 && _dataflow_tmp_all_valid_2)) && (_tmp_0 > 0)) begin
        myram_0_addr <= myram_0_addr + 1;
        myram_0_wdata <= _dataflow_counter_odata_1;
        myram_0_wenable <= 1;
        _tmp_0 <= _tmp_0 - 1;
      end 
      if(_dataflow_eq_odata_7 && (_dataflow_counter_ovalid_1 && ((_tmp_0 > 0) && !_tmp_1 && _dataflow_tmp_all_valid_2)) && (_tmp_0 == 1)) begin
        _tmp_1 <= 1;
      end 
      _myram_cond_0_1 <= 1;
    end
  end

  reg [32-1:0] _dataflow_counter_data_1;
  reg _dataflow_counter_valid_1;
  wire _dataflow_counter_ready_1;
  reg [32-1:0] _dataflow_counter_data_5;
  reg _dataflow_counter_valid_5;
  wire _dataflow_counter_ready_5;
  reg [6-1:0] _dataflow_counter_count_5;
  reg [1-1:0] _dataflow_eq_data_7;
  reg _dataflow_eq_valid_7;
  wire _dataflow_eq_ready_7;
  assign _dataflow_counter_ready_5 = (_dataflow_eq_ready_7 || !_dataflow_eq_valid_7) && _dataflow_counter_valid_5;
  reg [32-1:0] _dataflow__delay_data_9;
  reg _dataflow__delay_valid_9;
  wire _dataflow__delay_ready_9;
  assign _dataflow_counter_ready_1 = (_dataflow__delay_ready_9 || !_dataflow__delay_valid_9) && _dataflow_counter_valid_1;
  assign _dataflow_eq_odata_7 = _dataflow_eq_data_7;
  assign _dataflow_eq_ovalid_7 = _dataflow_eq_valid_7;
  assign _dataflow_eq_ready_7 = _dataflow_eq_oready_7;
  assign _dataflow_counter_odata_1 = _dataflow__delay_data_9;
  assign _dataflow_counter_ovalid_1 = _dataflow__delay_valid_9;
  assign _dataflow__delay_ready_9 = _dataflow_counter_oready_1;

  always @(posedge CLK) begin
    if(RST) begin
      _dataflow_counter_data_1 <= -2'sd1;
      _dataflow_counter_valid_1 <= 0;
      _dataflow_counter_data_5 <= -2'sd1;
      _dataflow_counter_count_5 <= 0;
      _dataflow_counter_valid_5 <= 0;
      _dataflow_eq_data_7 <= 0;
      _dataflow_eq_valid_7 <= 0;
      _dataflow__delay_data_9 <= 0;
      _dataflow__delay_valid_9 <= 0;
    end else begin
      if((_dataflow_counter_ready_1 || !_dataflow_counter_valid_1) && 1 && 1) begin
        _dataflow_counter_data_1 <= _dataflow_counter_data_1 + 1;
      end 
      if(_dataflow_counter_valid_1 && _dataflow_counter_ready_1) begin
        _dataflow_counter_valid_1 <= 0;
      end 
      if((_dataflow_counter_ready_1 || !_dataflow_counter_valid_1) && 1) begin
        _dataflow_counter_valid_1 <= 1;
      end 
      if((_dataflow_counter_ready_5 || !_dataflow_counter_valid_5) && 1 && 1) begin
        _dataflow_counter_data_5 <= _dataflow_counter_data_5 + 1;
      end 
      if((_dataflow_counter_ready_5 || !_dataflow_counter_valid_5) && 1 && 1) begin
        _dataflow_counter_count_5 <= (_dataflow_counter_count_5 == 5'sd8 - 1)? 0 : _dataflow_counter_count_5 + 1;
      end 
      if(_dataflow_counter_valid_5 && _dataflow_counter_ready_5) begin
        _dataflow_counter_valid_5 <= 0;
      end 
      if((_dataflow_counter_ready_5 || !_dataflow_counter_valid_5) && 1) begin
        _dataflow_counter_valid_5 <= 1;
      end 
      if((_dataflow_counter_ready_5 || !_dataflow_counter_valid_5) && 1 && 1 && (_dataflow_counter_count_5 == 0)) begin
        _dataflow_counter_data_5 <= -2'sd1 + 1;
      end 
      if((_dataflow_eq_ready_7 || !_dataflow_eq_valid_7) && _dataflow_counter_ready_5 && _dataflow_counter_valid_5) begin
        _dataflow_eq_data_7 <= _dataflow_counter_data_5 == 1'sd0;
      end 
      if(_dataflow_eq_valid_7 && _dataflow_eq_ready_7) begin
        _dataflow_eq_valid_7 <= 0;
      end 
      if((_dataflow_eq_ready_7 || !_dataflow_eq_valid_7) && _dataflow_counter_ready_5) begin
        _dataflow_eq_valid_7 <= _dataflow_counter_valid_5;
      end 
      if((_dataflow__delay_ready_9 || !_dataflow__delay_valid_9) && _dataflow_counter_ready_1 && _dataflow_counter_valid_1) begin
        _dataflow__delay_data_9 <= _dataflow_counter_data_1;
      end 
      if(_dataflow__delay_valid_9 && _dataflow__delay_ready_9) begin
        _dataflow__delay_valid_9 <= 0;
      end 
      if((_dataflow__delay_ready_9 || !_dataflow__delay_valid_9) && _dataflow_counter_ready_1) begin
        _dataflow__delay_valid_9 <= _dataflow_counter_valid_1;
      end 
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
          fsm <= fsm_1;
        end
        fsm_1: begin
          if(_tmp_1) begin
            fsm <= fsm_2;
          end 
        end
      endcase
    end
  end


  always @(posedge CLK) begin
    if(myram_0_wenable) begin
      $display("[%d] <- %d", myram_0_addr, myram_0_wdata);
    end 
  end


endmodule



module myram
(
  input CLK,
  input [14-1:0] myram_0_addr,
  output [32-1:0] myram_0_rdata,
  input [32-1:0] myram_0_wdata,
  input myram_0_wenable
);

  reg [14-1:0] myram_0_daddr;
  reg [32-1:0] mem [0:16384-1];

  always @(posedge CLK) begin
    if(myram_0_wenable) begin
      mem[myram_0_addr] <= myram_0_wdata;
    end 
    myram_0_daddr <= myram_0_addr;
  end

  assign myram_0_rdata = mem[myram_0_daddr];

endmodule
"""


def test():
    veriloggen.reset()
    test_module = thread_ram_write_dataflow_when.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
