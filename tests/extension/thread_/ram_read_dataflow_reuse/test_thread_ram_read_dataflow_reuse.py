from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import thread_ram_read_dataflow_reuse

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
  wire [32-1:0] _dataflow_counter_odata_1;
  wire _dataflow_counter_ovalid_1;
  wire _dataflow_counter_oready_1;
  assign _dataflow_counter_oready_1 = (_tmp_0 > 0) && !_tmp_1;
  reg _myram_cond_0_1;
  reg _tmp_2;
  reg _tmp_3;
  reg _tmp_4;
  wire _tmp_5;
  wire _tmp_6;
  wire _tmp_7;
  reg [7-1:0] _tmp_8;
  reg _tmp_9;
  reg signed [32-1:0] _tmp_10;
  reg signed [32-1:0] _tmp_11;
  reg signed [32-1:0] _tmp_12;
  reg signed [32-1:0] _tmp_13;
  reg [4-1:0] _tmp_14;
  reg _tmp_15;
  reg _tmp_16;
  reg [32-1:0] _tmp_fsm_0;
  localparam _tmp_fsm_0_init = 0;
  reg [32-1:0] _d1__tmp_fsm_0;
  reg [32-1:0] _d2__tmp_fsm_0;
  reg __tmp_fsm_0_cond_1_0_1;
  reg __tmp_fsm_0_cond_1_0_2;
  reg __tmp_fsm_0_cond_2_1_1;
  reg __tmp_fsm_0_cond_2_1_2;
  reg __tmp_fsm_0_cond_5_2_1;
  reg __tmp_fsm_0_cond_6_3_1;
  reg __tmp_fsm_0_cond_6_3_2;
  reg __tmp_fsm_0_cond_7_4_1;
  reg __tmp_fsm_0_cond_7_4_2;
  reg __tmp_fsm_0_cond_10_5_1;
  wire signed [32-1:0] _dataflow__variable_odata_4;
  wire _dataflow__variable_ovalid_4;
  wire _dataflow__variable_oready_4;
  assign _dataflow__variable_oready_4 = 1;
  wire signed [32-1:0] _dataflow__variable_odata_5;
  wire _dataflow__variable_ovalid_5;
  wire _dataflow__variable_oready_5;
  assign _dataflow__variable_oready_5 = 1;
  wire [1-1:0] _dataflow__variable_odata_3;
  wire _dataflow__variable_ovalid_3;
  wire _dataflow__variable_oready_3;
  assign _dataflow__variable_oready_3 = 1;
  reg [32-1:0] sum0;
  reg [32-1:0] sum1;
  reg _seq_cond_0_1;

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
      _tmp_9 <= 0;
      _tmp_2 <= 0;
      _tmp_3 <= 0;
      _tmp_4 <= 0;
      _tmp_14 <= 0;
    end else begin
      if(_myram_cond_0_1) begin
        myram_0_wenable <= 0;
        _tmp_1 <= 0;
      end 
      myram_1_wdata <= 0;
      myram_1_wenable <= 0;
      if((fsm == 0) && (_tmp_0 == 0)) begin
        myram_0_addr <= -1;
        _tmp_0 <= 64;
      end 
      if(_dataflow_counter_ovalid_1 && ((_tmp_0 > 0) && !_tmp_1) && (_tmp_0 > 0)) begin
        myram_0_addr <= myram_0_addr + 1;
        myram_0_wdata <= _dataflow_counter_odata_1;
        myram_0_wenable <= 1;
        _tmp_0 <= _tmp_0 - 1;
      end 
      if(_dataflow_counter_ovalid_1 && ((_tmp_0 > 0) && !_tmp_1) && (_tmp_0 == 1)) begin
        _tmp_1 <= 1;
      end 
      _myram_cond_0_1 <= 1;
      if((_tmp_5 || !_tmp_2) && (_tmp_6 || !_tmp_3) && (_tmp_7 || !_tmp_4) && _tmp_4) begin
        _tmp_9 <= 0;
        _tmp_2 <= 0;
        _tmp_3 <= 0;
        _tmp_4 <= 0;
      end 
      if(_tmp_15) begin
        _tmp_14 <= 4;
      end 
      if((_tmp_5 || !_tmp_2) && (_tmp_6 || !_tmp_3) && (_tmp_7 || !_tmp_4) && (_tmp_14 > 0)) begin
        _tmp_14 <= _tmp_14 - 1;
        _tmp_2 <= 1;
        _tmp_3 <= 1;
        _tmp_4 <= 1;
        _tmp_9 <= 0;
      end 
      if((_tmp_5 || !_tmp_2) && (_tmp_6 || !_tmp_3) && (_tmp_7 || !_tmp_4) && (_tmp_14 == 1) && _tmp_16) begin
        _tmp_9 <= 1;
      end 
    end
  end

  assign _dataflow__variable_odata_3 = _tmp_9;
  assign _dataflow__variable_ovalid_3 = _tmp_4;
  assign _tmp_7 = 1 && _dataflow__variable_oready_3;
  assign _dataflow__variable_odata_4 = _tmp_10;
  assign _dataflow__variable_ovalid_4 = _tmp_2;
  assign _tmp_5 = 1 && _dataflow__variable_oready_4;
  assign _dataflow__variable_odata_5 = _tmp_11;
  assign _dataflow__variable_ovalid_5 = _tmp_3;
  assign _tmp_6 = 1 && _dataflow__variable_oready_5;
  reg [32-1:0] _dataflow_counter_data_1;
  reg _dataflow_counter_valid_1;
  wire _dataflow_counter_ready_1;
  assign _dataflow_counter_odata_1 = _dataflow_counter_data_1;
  assign _dataflow_counter_ovalid_1 = _dataflow_counter_valid_1;
  assign _dataflow_counter_ready_1 = _dataflow_counter_oready_1;

  always @(posedge CLK) begin
    if(RST) begin
      _dataflow_counter_data_1 <= -2'sd1;
      _dataflow_counter_valid_1 <= 0;
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
    end
  end

  localparam fsm_1 = 1;
  localparam fsm_2 = 2;
  localparam fsm_3 = 3;
  localparam fsm_4 = 4;
  localparam fsm_5 = 5;

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
        fsm_2: begin
          fsm <= fsm_3;
        end
        fsm_3: begin
          fsm <= fsm_4;
        end
        fsm_4: begin
          if(_tmp_9) begin
            fsm <= fsm_5;
          end 
        end
      endcase
    end
  end

  localparam _tmp_fsm_0_1 = 1;
  localparam _tmp_fsm_0_2 = 2;
  localparam _tmp_fsm_0_3 = 3;
  localparam _tmp_fsm_0_4 = 4;
  localparam _tmp_fsm_0_5 = 5;
  localparam _tmp_fsm_0_6 = 6;
  localparam _tmp_fsm_0_7 = 7;
  localparam _tmp_fsm_0_8 = 8;
  localparam _tmp_fsm_0_9 = 9;
  localparam _tmp_fsm_0_10 = 10;

  always @(posedge CLK) begin
    if(RST) begin
      _tmp_fsm_0 <= _tmp_fsm_0_init;
      _d1__tmp_fsm_0 <= _tmp_fsm_0_init;
      _d2__tmp_fsm_0 <= _tmp_fsm_0_init;
      myram_1_addr <= 0;
      _tmp_16 <= 0;
      _tmp_8 <= 0;
      __tmp_fsm_0_cond_1_0_1 <= 0;
      __tmp_fsm_0_cond_1_0_2 <= 0;
      _tmp_12 <= 0;
      __tmp_fsm_0_cond_2_1_1 <= 0;
      __tmp_fsm_0_cond_2_1_2 <= 0;
      _tmp_13 <= 0;
      _tmp_10 <= 0;
      _tmp_11 <= 0;
      _tmp_15 <= 0;
      __tmp_fsm_0_cond_5_2_1 <= 0;
      __tmp_fsm_0_cond_6_3_1 <= 0;
      __tmp_fsm_0_cond_6_3_2 <= 0;
      __tmp_fsm_0_cond_7_4_1 <= 0;
      __tmp_fsm_0_cond_7_4_2 <= 0;
      __tmp_fsm_0_cond_10_5_1 <= 0;
    end else begin
      _d1__tmp_fsm_0 <= _tmp_fsm_0;
      _d2__tmp_fsm_0 <= _d1__tmp_fsm_0;
      case(_d2__tmp_fsm_0)
        _tmp_fsm_0_1: begin
          if(__tmp_fsm_0_cond_1_0_2) begin
            _tmp_12 <= myram_1_rdata;
          end 
        end
        _tmp_fsm_0_2: begin
          if(__tmp_fsm_0_cond_2_1_2) begin
            _tmp_13 <= myram_1_rdata;
          end 
        end
        _tmp_fsm_0_6: begin
          if(__tmp_fsm_0_cond_6_3_2) begin
            _tmp_12 <= myram_1_rdata;
          end 
        end
        _tmp_fsm_0_7: begin
          if(__tmp_fsm_0_cond_7_4_2) begin
            _tmp_13 <= myram_1_rdata;
          end 
        end
      endcase
      case(_d1__tmp_fsm_0)
        _tmp_fsm_0_1: begin
          __tmp_fsm_0_cond_1_0_2 <= __tmp_fsm_0_cond_1_0_1;
        end
        _tmp_fsm_0_2: begin
          __tmp_fsm_0_cond_2_1_2 <= __tmp_fsm_0_cond_2_1_1;
        end
        _tmp_fsm_0_5: begin
          if(__tmp_fsm_0_cond_5_2_1) begin
            _tmp_15 <= 0;
          end 
        end
        _tmp_fsm_0_6: begin
          __tmp_fsm_0_cond_6_3_2 <= __tmp_fsm_0_cond_6_3_1;
        end
        _tmp_fsm_0_7: begin
          __tmp_fsm_0_cond_7_4_2 <= __tmp_fsm_0_cond_7_4_1;
        end
        _tmp_fsm_0_10: begin
          if(__tmp_fsm_0_cond_10_5_1) begin
            _tmp_15 <= 0;
          end 
        end
      endcase
      case(_tmp_fsm_0)
        _tmp_fsm_0_init: begin
          if(fsm == 3) begin
            myram_1_addr <= -1;
            _tmp_16 <= 0;
            _tmp_8 <= 32;
          end 
          if((fsm == 3) && 1) begin
            _tmp_fsm_0 <= _tmp_fsm_0_1;
          end 
        end
        _tmp_fsm_0_1: begin
          myram_1_addr <= myram_1_addr + 1;
          _tmp_8 <= (_tmp_8 > 0)? _tmp_8 - 1 : _tmp_8;
          __tmp_fsm_0_cond_1_0_1 <= 1;
          _tmp_fsm_0 <= _tmp_fsm_0_2;
        end
        _tmp_fsm_0_2: begin
          myram_1_addr <= myram_1_addr + 1;
          _tmp_8 <= (_tmp_8 > 0)? _tmp_8 - 1 : _tmp_8;
          __tmp_fsm_0_cond_2_1_1 <= 1;
          _tmp_fsm_0 <= _tmp_fsm_0_3;
        end
        _tmp_fsm_0_3: begin
          _tmp_fsm_0 <= _tmp_fsm_0_4;
        end
        _tmp_fsm_0_4: begin
          _tmp_fsm_0 <= _tmp_fsm_0_5;
        end
        _tmp_fsm_0_5: begin
          _tmp_10 <= _tmp_12;
          _tmp_11 <= _tmp_13;
          _tmp_15 <= 1;
          _tmp_16 <= _tmp_8 == 0;
          __tmp_fsm_0_cond_5_2_1 <= 1;
          _tmp_fsm_0 <= _tmp_fsm_0_6;
        end
        _tmp_fsm_0_6: begin
          myram_1_addr <= myram_1_addr + 1;
          _tmp_8 <= (_tmp_8 > 0)? _tmp_8 - 1 : _tmp_8;
          __tmp_fsm_0_cond_6_3_1 <= 1;
          _tmp_fsm_0 <= _tmp_fsm_0_7;
        end
        _tmp_fsm_0_7: begin
          myram_1_addr <= myram_1_addr + 1;
          _tmp_8 <= (_tmp_8 > 0)? _tmp_8 - 1 : _tmp_8;
          __tmp_fsm_0_cond_7_4_1 <= 1;
          _tmp_fsm_0 <= _tmp_fsm_0_8;
        end
        _tmp_fsm_0_8: begin
          _tmp_fsm_0 <= _tmp_fsm_0_9;
        end
        _tmp_fsm_0_9: begin
          _tmp_fsm_0 <= _tmp_fsm_0_10;
        end
        _tmp_fsm_0_10: begin
          if((_tmp_5 || !_tmp_2) && (_tmp_6 || !_tmp_3) && (_tmp_7 || !_tmp_4) && (_tmp_14 == 0)) begin
            _tmp_10 <= _tmp_12;
          end 
          if((_tmp_5 || !_tmp_2) && (_tmp_6 || !_tmp_3) && (_tmp_7 || !_tmp_4) && (_tmp_14 == 0)) begin
            _tmp_11 <= _tmp_13;
          end 
          if((_tmp_5 || !_tmp_2) && (_tmp_6 || !_tmp_3) && (_tmp_7 || !_tmp_4) && (_tmp_14 == 0)) begin
            _tmp_15 <= !_tmp_16;
            _tmp_16 <= _tmp_8 == 0;
          end 
          __tmp_fsm_0_cond_10_5_1 <= 1;
          if((_tmp_5 || !_tmp_2) && (_tmp_6 || !_tmp_3) && (_tmp_7 || !_tmp_4) && (_tmp_14 == 0) && (_tmp_8 == 0)) begin
            _tmp_fsm_0 <= _tmp_fsm_0_init;
          end 
          if((_tmp_5 || !_tmp_2) && (_tmp_6 || !_tmp_3) && (_tmp_7 || !_tmp_4) && (_tmp_14 == 0) && (_tmp_8 > 0)) begin
            _tmp_fsm_0 <= _tmp_fsm_0_6;
          end 
        end
      endcase
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      sum0 <= 0;
      sum1 <= 0;
      _seq_cond_0_1 <= 0;
    end else begin
      if(_seq_cond_0_1) begin
        $display("sum=%d expected_sum=%d", (sum0 + sum1), 1984);
      end 
      if(_dataflow__variable_ovalid_4) begin
        sum0 <= sum0 + _dataflow__variable_odata_4;
        $display("rdata0_data=%d", _dataflow__variable_odata_4);
      end 
      if(_dataflow__variable_ovalid_5) begin
        sum1 <= sum1 + _dataflow__variable_odata_5;
        $display("rdata1_data=%d", _dataflow__variable_odata_5);
      end 
      _seq_cond_0_1 <= _dataflow__variable_ovalid_5 && (_dataflow__variable_odata_3 == 1);
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
    test_module = thread_ram_read_dataflow_reuse.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
