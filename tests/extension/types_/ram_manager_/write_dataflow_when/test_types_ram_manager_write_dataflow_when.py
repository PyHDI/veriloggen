from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import types_ram_manager_write_dataflow_when

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
  wire _tmp_all_valid_2;
  wire [32-1:0] _counter_data_3;
  wire _counter_valid_3;
  wire _counter_ready_3;
  assign _counter_ready_3 = (_tmp_0 > 0) && !_tmp_1 && _tmp_all_valid_2;
  wire [1-1:0] _eq_data_4;
  wire _eq_valid_4;
  wire _eq_ready_4;
  assign _eq_ready_4 = (_tmp_0 > 0) && !_tmp_1 && _tmp_all_valid_2;
  assign _tmp_all_valid_2 = _counter_valid_3 && _eq_valid_4;
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
      if(_eq_data_4 && (_counter_valid_3 && ((_tmp_0 > 0) && !_tmp_1 && _tmp_all_valid_2)) && (_tmp_0 > 0)) begin
        myram_0_addr <= myram_0_addr + 1;
        myram_0_wdata <= _counter_data_3;
        myram_0_wenable <= 1;
        _tmp_0 <= _tmp_0 - 1;
      end 
      if(_eq_data_4 && (_counter_valid_3 && ((_tmp_0 > 0) && !_tmp_1 && _tmp_all_valid_2)) && (_tmp_0 == 1)) begin
        _tmp_1 <= 1;
      end 
      _myram_cond_0_1 <= 1;
    end
  end

  reg [32-1:0] _counter_data_5;
  reg _counter_valid_5;
  wire _counter_ready_5;
  reg [32-1:0] _counter_data_6;
  reg _counter_valid_6;
  wire _counter_ready_6;
  reg [6-1:0] _counter_count_6;
  reg [1-1:0] _eq_data_7;
  reg _eq_valid_7;
  wire _eq_ready_7;
  assign _counter_ready_6 = (_eq_ready_7 || !_eq_valid_7) && _counter_valid_6;
  reg [32-1:0] __delay_data_8;
  reg __delay_valid_8;
  wire __delay_ready_8;
  assign _counter_ready_5 = (__delay_ready_8 || !__delay_valid_8) && _counter_valid_5;
  assign _eq_data_4 = _eq_data_7;
  assign _eq_valid_4 = _eq_valid_7;
  assign _eq_ready_7 = _eq_ready_4;
  assign _counter_data_3 = __delay_data_8;
  assign _counter_valid_3 = __delay_valid_8;
  assign __delay_ready_8 = _counter_ready_3;

  always @(posedge CLK) begin
    if(RST) begin
      _counter_data_5 <= -2'sd1;
      _counter_valid_5 <= 0;
      _counter_data_6 <= -2'sd1;
      _counter_count_6 <= 0;
      _counter_valid_6 <= 0;
      _eq_data_7 <= 0;
      _eq_valid_7 <= 0;
      __delay_data_8 <= 0;
      __delay_valid_8 <= 0;
    end else begin
      if((_counter_ready_5 || !_counter_valid_5) && 1 && 1) begin
        _counter_data_5 <= _counter_data_5 + 1;
      end 
      if(_counter_valid_5 && _counter_ready_5) begin
        _counter_valid_5 <= 0;
      end 
      if((_counter_ready_5 || !_counter_valid_5) && 1) begin
        _counter_valid_5 <= 1;
      end 
      if((_counter_ready_6 || !_counter_valid_6) && 1 && 1) begin
        _counter_data_6 <= _counter_data_6 + 1;
      end 
      if((_counter_ready_6 || !_counter_valid_6) && 1 && 1) begin
        _counter_count_6 <= (_counter_count_6 == 5'sd8 - 1)? 0 : _counter_count_6 + 1;
      end 
      if(_counter_valid_6 && _counter_ready_6) begin
        _counter_valid_6 <= 0;
      end 
      if((_counter_ready_6 || !_counter_valid_6) && 1) begin
        _counter_valid_6 <= 1;
      end 
      if((_counter_ready_6 || !_counter_valid_6) && 1 && 1 && (_counter_count_6 == 0)) begin
        _counter_data_6 <= -2'sd1 + 1;
      end 
      if((_eq_ready_7 || !_eq_valid_7) && _counter_ready_6 && _counter_valid_6) begin
        _eq_data_7 <= _counter_data_6 == 1'sd0;
      end 
      if(_eq_valid_7 && _eq_ready_7) begin
        _eq_valid_7 <= 0;
      end 
      if((_eq_ready_7 || !_eq_valid_7) && _counter_ready_6) begin
        _eq_valid_7 <= _counter_valid_6;
      end 
      if((__delay_ready_8 || !__delay_valid_8) && _counter_ready_5 && _counter_valid_5) begin
        __delay_data_8 <= _counter_data_5;
      end 
      if(__delay_valid_8 && __delay_ready_8) begin
        __delay_valid_8 <= 0;
      end 
      if((__delay_ready_8 || !__delay_valid_8) && _counter_ready_5) begin
        __delay_valid_8 <= _counter_valid_5;
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
    test_module = types_ram_manager_write_dataflow_when.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
