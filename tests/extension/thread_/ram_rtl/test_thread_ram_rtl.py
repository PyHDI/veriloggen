from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import thread_ram_rtl

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

  myram
  inst_myram
  (
    .CLK(CLK),
    .myram_0_addr(myram_0_addr),
    .myram_0_rdata(myram_0_rdata),
    .myram_0_wdata(myram_0_wdata),
    .myram_0_wenable(myram_0_wenable)
  );

  reg write_done;
  reg [10-1:0] write_addr;
  reg [10-1:0] read_addr;
  reg [32-1:0] sum;
  reg [32-1:0] fsm;
  localparam fsm_init = 0;
  reg _myram_cond_0_1;
  reg _tmp_0;
  reg _myram_cond_1_1;
  reg _myram_cond_2_1;
  reg _myram_cond_2_2;
  reg _tmp_1;
  reg _myram_cond_3_1;
  reg _myram_cond_4_1;
  reg _myram_cond_4_2;
  reg [32-1:0] th_blink;
  localparam th_blink_init = 0;
  reg signed [32-1:0] _th_blink_times_0;
  reg signed [32-1:0] _th_blink_i_1;
  reg signed [32-1:0] _th_blink_wdata_2;
  reg _myram_cond_5_1;

  always @(posedge CLK) begin
    if(RST) begin
      myram_0_addr <= 0;
      myram_0_wdata <= 0;
      myram_0_wenable <= 0;
      _myram_cond_0_1 <= 0;
      _myram_cond_1_1 <= 0;
      _tmp_0 <= 0;
      _myram_cond_2_1 <= 0;
      _myram_cond_2_2 <= 0;
      _myram_cond_3_1 <= 0;
      _tmp_1 <= 0;
      _myram_cond_4_1 <= 0;
      _myram_cond_4_2 <= 0;
      _myram_cond_5_1 <= 0;
    end else begin
      if(_myram_cond_2_2) begin
        _tmp_0 <= 0;
      end 
      if(_myram_cond_4_2) begin
        _tmp_1 <= 0;
      end 
      if(_myram_cond_0_1) begin
        myram_0_wenable <= 0;
      end 
      if(_myram_cond_1_1) begin
        _tmp_0 <= 1;
      end 
      _myram_cond_2_2 <= _myram_cond_2_1;
      if(_myram_cond_3_1) begin
        _tmp_1 <= 1;
      end 
      _myram_cond_4_2 <= _myram_cond_4_1;
      if(_myram_cond_5_1) begin
        myram_0_wenable <= 0;
      end 
      if(fsm == 1) begin
        myram_0_addr <= write_addr;
        myram_0_wdata <= write_addr;
        myram_0_wenable <= 1;
      end 
      _myram_cond_0_1 <= fsm == 1;
      if(fsm == 2) begin
        myram_0_addr <= read_addr;
      end 
      _myram_cond_1_1 <= fsm == 2;
      _myram_cond_2_1 <= fsm == 2;
      if(fsm == 3) begin
        myram_0_addr <= read_addr;
      end 
      _myram_cond_3_1 <= fsm == 3;
      _myram_cond_4_1 <= fsm == 3;
      if(th_blink == 5) begin
        myram_0_addr <= _th_blink_i_1;
        myram_0_wdata <= _th_blink_wdata_2;
        myram_0_wenable <= 1;
      end 
      _myram_cond_5_1 <= th_blink == 5;
    end
  end

  localparam fsm_1 = 1;
  localparam fsm_2 = 2;
  localparam fsm_3 = 3;
  localparam fsm_4 = 4;
  localparam fsm_5 = 5;
  localparam fsm_6 = 6;
  localparam fsm_7 = 7;

  always @(posedge CLK) begin
    if(RST) begin
      fsm <= fsm_init;
      write_addr <= 0;
      read_addr <= 0;
      sum <= 0;
    end else begin
      case(fsm)
        fsm_init: begin
          if(write_done) begin
            fsm <= fsm_1;
          end 
        end
        fsm_1: begin
          write_addr <= write_addr + 1;
          $display("wdata =  %d", write_addr);
          if(write_addr == 9) begin
            fsm <= fsm_2;
          end 
        end
        fsm_2: begin
          fsm <= fsm_3;
        end
        fsm_3: begin
          read_addr <= read_addr + 1;
          if(_tmp_1) begin
            $display("rdata =  %d", myram_0_rdata);
            sum <= sum + myram_0_rdata;
          end 
          if(read_addr == 9) begin
            fsm <= fsm_4;
          end 
        end
        fsm_4: begin
          if(_tmp_1) begin
            $display("rdata =  %d", myram_0_rdata);
            sum <= sum + myram_0_rdata;
          end 
          fsm <= fsm_5;
        end
        fsm_5: begin
          if(_tmp_1) begin
            $display("rdata =  %d", myram_0_rdata);
            sum <= sum + myram_0_rdata;
          end 
          fsm <= fsm_6;
        end
        fsm_6: begin
          $display("sum =  %d", sum);
          fsm <= fsm_7;
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
  input myram_0_wenable
);

  reg [10-1:0] myram_0_daddr;
  reg [32-1:0] mem [0:1024-1];

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
    test_module = thread_ram_rtl.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
