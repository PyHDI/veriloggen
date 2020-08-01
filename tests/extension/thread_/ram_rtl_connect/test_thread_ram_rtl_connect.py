from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import thread_ram_rtl_connect

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

  reg [10-1:0] myram_0_addr;
  wire [32-1:0] myram_0_rdata;
  reg [32-1:0] myram_0_wdata;
  reg myram_0_wenable;
  reg [10-1:0] myram_1_addr;
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

  reg write_done;
  reg [10-1:0] addr;
  reg [32-1:0] wdata;
  reg wenable;
  wire [32-1:0] rdata;
  reg [32-1:0] sum;
  reg [32-1:0] fsm;
  localparam fsm_init = 0;
  reg [32-1:0] _d1_fsm;
  reg _fsm_cond_2_0_1;
  reg [32-1:0] _d2_fsm;
  reg _fsm_cond_4_1_1;
  reg _fsm_cond_4_1_2;
  wire [10-1:0] _tmp_0;
  assign _tmp_0 = addr;

  always @(*) begin
    myram_1_addr = _tmp_0;
  end

  wire [32-1:0] _tmp_1;
  assign _tmp_1 = wdata;

  always @(*) begin
    myram_1_wdata = _tmp_1;
  end

  wire _tmp_2;
  assign _tmp_2 = wenable;

  always @(*) begin
    myram_1_wenable = _tmp_2;
  end

  assign rdata = myram_1_rdata;
  reg [32-1:0] th_blink;
  localparam th_blink_init = 0;
  reg signed [32-1:0] _th_blink_times_0;
  reg signed [32-1:0] _th_blink_i_1;
  reg signed [32-1:0] _th_blink_wdata_2;
  reg _myram_cond_0_1;

  always @(posedge CLK) begin
    if(RST) begin
      myram_0_addr <= 0;
      myram_0_wdata <= 0;
      myram_0_wenable <= 0;
      _myram_cond_0_1 <= 0;
    end else begin
      if(_myram_cond_0_1) begin
        myram_0_wenable <= 0;
      end 
      if(th_blink == 5) begin
        myram_0_addr <= _th_blink_i_1;
        myram_0_wdata <= _th_blink_wdata_2;
        myram_0_wenable <= 1;
      end 
      _myram_cond_0_1 <= th_blink == 5;
    end
  end

  localparam fsm_1 = 1;
  localparam fsm_2 = 2;
  localparam fsm_3 = 3;
  localparam fsm_4 = 4;
  localparam fsm_5 = 5;
  localparam fsm_6 = 6;
  localparam fsm_7 = 7;
  localparam fsm_8 = 8;

  always @(posedge CLK) begin
    if(RST) begin
      fsm <= fsm_init;
      _d1_fsm <= fsm_init;
      _d2_fsm <= fsm_init;
      addr <= 0;
      wdata <= 0;
      wenable <= 0;
      _fsm_cond_2_0_1 <= 0;
      _fsm_cond_4_1_1 <= 0;
      _fsm_cond_4_1_2 <= 0;
      sum <= 0;
    end else begin
      _d1_fsm <= fsm;
      _d2_fsm <= _d1_fsm;
      case(_d2_fsm)
        fsm_4: begin
          if(_fsm_cond_4_1_2) begin
            sum <= sum + rdata;
            $display("rdata =  %d", rdata);
          end 
        end
      endcase
      case(_d1_fsm)
        fsm_2: begin
          if(_fsm_cond_2_0_1) begin
            $display("wdata =  %d", wdata);
            wenable <= 0;
          end 
        end
        fsm_4: begin
          _fsm_cond_4_1_2 <= _fsm_cond_4_1_1;
        end
      endcase
      case(fsm)
        fsm_init: begin
          if(write_done) begin
            fsm <= fsm_1;
          end 
        end
        fsm_1: begin
          addr <= -1;
          wdata <= -1;
          wenable <= 0;
          fsm <= fsm_2;
        end
        fsm_2: begin
          addr <= addr + 1;
          wdata <= wdata + 1;
          wenable <= 1;
          _fsm_cond_2_0_1 <= 1;
          if(addr == 8) begin
            fsm <= fsm_3;
          end 
        end
        fsm_3: begin
          addr <= -1;
          wenable <= 0;
          fsm <= fsm_4;
        end
        fsm_4: begin
          addr <= addr + 1;
          _fsm_cond_4_1_1 <= 1;
          if(addr == 8) begin
            fsm <= fsm_5;
          end 
        end
        fsm_5: begin
          fsm <= fsm_6;
        end
        fsm_6: begin
          fsm <= fsm_7;
        end
        fsm_7: begin
          $display("sum =  %d", sum);
          fsm <= fsm_8;
        end
      endcase
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

  always @(posedge CLK) begin
    if(RST) begin
      th_blink <= th_blink_init;
      _th_blink_times_0 <= 0;
      write_done <= 0;
      _th_blink_i_1 <= 0;
      _th_blink_wdata_2 <= 0;
    end else begin
      case(th_blink)
        th_blink_init: begin
          _th_blink_times_0 <= 10;
          th_blink <= th_blink_1;
        end
        th_blink_1: begin
          write_done <= 0;
          th_blink <= th_blink_2;
        end
        th_blink_2: begin
          _th_blink_i_1 <= 0;
          th_blink <= th_blink_3;
        end
        th_blink_3: begin
          if(_th_blink_i_1 < _th_blink_times_0) begin
            th_blink <= th_blink_4;
          end else begin
            th_blink <= th_blink_8;
          end
        end
        th_blink_4: begin
          _th_blink_wdata_2 <= _th_blink_i_1 + 100;
          th_blink <= th_blink_5;
        end
        th_blink_5: begin
          th_blink <= th_blink_6;
        end
        th_blink_6: begin
          $display("wdata = %d", _th_blink_wdata_2);
          th_blink <= th_blink_7;
        end
        th_blink_7: begin
          _th_blink_i_1 <= _th_blink_i_1 + 1;
          th_blink <= th_blink_3;
        end
        th_blink_8: begin
          write_done <= 1;
          th_blink <= th_blink_9;
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
  input [10-1:0] myram_1_addr,
  output [32-1:0] myram_1_rdata,
  input [32-1:0] myram_1_wdata,
  input myram_1_wenable
);

  reg [10-1:0] myram_0_daddr;
  reg [10-1:0] myram_1_daddr;
  reg [32-1:0] mem [0:1024-1];

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
    test_module = thread_ram_rtl_connect.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
