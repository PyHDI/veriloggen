from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import thread_fifo_try

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

  reg myfifo_enq;
  reg [32-1:0] myfifo_wdata;
  wire myfifo_full;
  wire myfifo_almost_full;
  reg myfifo_deq;
  wire [32-1:0] myfifo_rdata;
  wire myfifo_empty;
  wire myfifo_almost_empty;

  myfifo
  inst_myfifo
  (
    .CLK(CLK),
    .RST(RST),
    .myfifo_enq(myfifo_enq),
    .myfifo_wdata(myfifo_wdata),
    .myfifo_full(myfifo_full),
    .myfifo_almost_full(myfifo_almost_full),
    .myfifo_deq(myfifo_deq),
    .myfifo_rdata(myfifo_rdata),
    .myfifo_empty(myfifo_empty),
    .myfifo_almost_empty(myfifo_almost_empty)
  );

  reg [5-1:0] count_myfifo;
  reg [32-1:0] th_blink;
  localparam th_blink_init = 0;
  reg signed [32-1:0] _th_blink_times_0;
  reg signed [32-1:0] _th_blink_wdata_1;
  reg signed [32-1:0] _th_blink_ack_2;
  reg _myfifo_cond_0_1;
  reg _tmp_0;
  reg signed [32-1:0] _th_blink_sum_3;
  reg signed [32-1:0] _th_blink_rvalid_4;
  reg _tmp_1;
  reg _myfifo_cond_1_1;
  reg _myfifo_cond_2_1;
  reg _myfifo_cond_3_1;
  reg _myfifo_cond_3_2;
  reg signed [32-1:0] _tmp_2;
  reg _tmp_3;
  reg signed [32-1:0] _th_blink_rdata_5;

  always @(posedge CLK) begin
    if(RST) begin
      count_myfifo <= 0;
      myfifo_wdata <= 0;
      myfifo_enq <= 0;
      _myfifo_cond_0_1 <= 0;
      myfifo_deq <= 0;
      _myfifo_cond_1_1 <= 0;
      _tmp_1 <= 0;
      _myfifo_cond_2_1 <= 0;
      _myfifo_cond_3_1 <= 0;
      _myfifo_cond_3_2 <= 0;
    end else begin
      if(_myfifo_cond_3_2) begin
        _tmp_1 <= 0;
      end 
      if(_myfifo_cond_0_1) begin
        myfifo_enq <= 0;
      end 
      if(_myfifo_cond_1_1) begin
        _tmp_1 <= !myfifo_empty && myfifo_deq;
      end 
      if(_myfifo_cond_2_1) begin
        myfifo_deq <= 0;
      end 
      _myfifo_cond_3_2 <= _myfifo_cond_3_1;
      if(myfifo_enq && !myfifo_full && (myfifo_deq && !myfifo_empty)) begin
        count_myfifo <= count_myfifo;
      end else if(myfifo_enq && !myfifo_full) begin
        count_myfifo <= count_myfifo + 1;
      end else if(myfifo_deq && !myfifo_empty) begin
        count_myfifo <= count_myfifo - 1;
      end 
      if((th_blink == 4) && !myfifo_full) begin
        myfifo_wdata <= _th_blink_wdata_1;
      end 
      if((th_blink == 4) && !myfifo_full) begin
        myfifo_enq <= 1;
      end 
      _myfifo_cond_0_1 <= 1;
      if(th_blink == 14) begin
        myfifo_deq <= 1;
      end 
      _myfifo_cond_1_1 <= th_blink == 14;
      _myfifo_cond_2_1 <= 1;
      _myfifo_cond_3_1 <= 1;
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

  always @(posedge CLK) begin
    if(RST) begin
      th_blink <= th_blink_init;
      _th_blink_times_0 <= 0;
      _th_blink_wdata_1 <= 0;
      _th_blink_ack_2 <= 0;
      _tmp_0 <= 0;
      _th_blink_sum_3 <= 0;
      _th_blink_rvalid_4 <= 0;
      _tmp_2 <= 0;
      _tmp_3 <= 0;
      _th_blink_rdata_5 <= 0;
    end else begin
      case(th_blink)
        th_blink_init: begin
          _th_blink_times_0 <= 10;
          th_blink <= th_blink_1;
        end
        th_blink_1: begin
          _th_blink_wdata_1 <= 0;
          th_blink <= th_blink_2;
        end
        th_blink_2: begin
          _th_blink_ack_2 <= 1;
          th_blink <= th_blink_3;
        end
        th_blink_3: begin
          if(_th_blink_ack_2) begin
            th_blink <= th_blink_4;
          end else begin
            th_blink <= th_blink_11;
          end
        end
        th_blink_4: begin
          th_blink <= th_blink_5;
        end
        th_blink_5: begin
          _tmp_0 <= !myfifo_full && myfifo_enq;
          th_blink <= th_blink_6;
        end
        th_blink_6: begin
          _th_blink_ack_2 <= _tmp_0;
          th_blink <= th_blink_7;
        end
        th_blink_7: begin
          if(_th_blink_ack_2) begin
            th_blink <= th_blink_8;
          end else begin
            th_blink <= th_blink_9;
          end
        end
        th_blink_8: begin
          $display("wdata = %d", _th_blink_wdata_1);
          th_blink <= th_blink_9;
        end
        th_blink_9: begin
          _th_blink_wdata_1 <= _th_blink_wdata_1 + 1;
          th_blink <= th_blink_10;
        end
        th_blink_10: begin
          th_blink <= th_blink_3;
        end
        th_blink_11: begin
          _th_blink_sum_3 <= 0;
          th_blink <= th_blink_12;
        end
        th_blink_12: begin
          _th_blink_rvalid_4 <= 1;
          th_blink <= th_blink_13;
        end
        th_blink_13: begin
          if(_th_blink_rvalid_4) begin
            th_blink <= th_blink_14;
          end else begin
            th_blink <= th_blink_22;
          end
        end
        th_blink_14: begin
          th_blink <= th_blink_15;
        end
        th_blink_15: begin
          th_blink <= th_blink_16;
        end
        th_blink_16: begin
          _tmp_2 <= myfifo_rdata;
          _tmp_3 <= _tmp_1;
          th_blink <= th_blink_17;
        end
        th_blink_17: begin
          _th_blink_rdata_5 <= _tmp_2;
          _th_blink_rvalid_4 <= _tmp_3;
          th_blink <= th_blink_18;
        end
        th_blink_18: begin
          if(_th_blink_rvalid_4) begin
            th_blink <= th_blink_19;
          end else begin
            th_blink <= th_blink_21;
          end
        end
        th_blink_19: begin
          _th_blink_sum_3 <= _th_blink_sum_3 + _th_blink_rdata_5;
          th_blink <= th_blink_20;
        end
        th_blink_20: begin
          $display("rdata = %d", _th_blink_rdata_5);
          th_blink <= th_blink_21;
        end
        th_blink_21: begin
          th_blink <= th_blink_13;
        end
        th_blink_22: begin
          $display("sum = %d", _th_blink_sum_3);
          th_blink <= th_blink_23;
        end
      endcase
    end
  end


endmodule



module myfifo
(
  input CLK,
  input RST,
  input myfifo_enq,
  input [32-1:0] myfifo_wdata,
  output myfifo_full,
  output myfifo_almost_full,
  input myfifo_deq,
  output [32-1:0] myfifo_rdata,
  output myfifo_empty,
  output myfifo_almost_empty
);

  reg [32-1:0] mem [0:16-1];
  reg [4-1:0] head;
  reg [4-1:0] tail;
  wire is_empty;
  wire is_almost_empty;
  wire is_full;
  wire is_almost_full;
  assign is_empty = head == tail;
  assign is_almost_empty = head == (tail + 1 & 15);
  assign is_full = (head + 1 & 15) == tail;
  assign is_almost_full = (head + 2 & 15) == tail;
  reg [32-1:0] rdata_reg;
  assign myfifo_full = is_full;
  assign myfifo_almost_full = is_almost_full || is_full;
  assign myfifo_empty = is_empty;
  assign myfifo_almost_empty = is_almost_empty || is_empty;
  assign myfifo_rdata = rdata_reg;

  always @(posedge CLK) begin
    if(RST) begin
      head <= 0;
      rdata_reg <= 0;
      tail <= 0;
    end else begin
      if(myfifo_enq && !is_full) begin
        mem[head] <= myfifo_wdata;
        head <= head + 1;
      end 
      if(myfifo_deq && !is_empty) begin
        rdata_reg <= mem[tail];
        tail <= tail + 1;
      end 
    end
  end


endmodule
"""


def test():
    veriloggen.reset()
    test_module = thread_fifo_try.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
