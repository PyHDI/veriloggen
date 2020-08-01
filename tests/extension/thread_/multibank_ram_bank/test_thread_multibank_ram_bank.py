from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import thread_multibank_ram_bank

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

  reg [10-1:0] myram_0_0_addr;
  wire [32-1:0] myram_0_0_rdata;
  reg [32-1:0] myram_0_0_wdata;
  reg myram_0_0_wenable;

  myram_0
  inst_myram_0
  (
    .CLK(CLK),
    .myram_0_0_addr(myram_0_0_addr),
    .myram_0_0_rdata(myram_0_0_rdata),
    .myram_0_0_wdata(myram_0_0_wdata),
    .myram_0_0_wenable(myram_0_0_wenable)
  );

  reg [10-1:0] myram_1_0_addr;
  wire [32-1:0] myram_1_0_rdata;
  reg [32-1:0] myram_1_0_wdata;
  reg myram_1_0_wenable;

  myram_1
  inst_myram_1
  (
    .CLK(CLK),
    .myram_1_0_addr(myram_1_0_addr),
    .myram_1_0_rdata(myram_1_0_rdata),
    .myram_1_0_wdata(myram_1_0_wdata),
    .myram_1_0_wenable(myram_1_0_wenable)
  );

  reg [10-1:0] myram_2_0_addr;
  wire [32-1:0] myram_2_0_rdata;
  reg [32-1:0] myram_2_0_wdata;
  reg myram_2_0_wenable;

  myram_2
  inst_myram_2
  (
    .CLK(CLK),
    .myram_2_0_addr(myram_2_0_addr),
    .myram_2_0_rdata(myram_2_0_rdata),
    .myram_2_0_wdata(myram_2_0_wdata),
    .myram_2_0_wenable(myram_2_0_wenable)
  );

  reg [10-1:0] myram_3_0_addr;
  wire [32-1:0] myram_3_0_rdata;
  reg [32-1:0] myram_3_0_wdata;
  reg myram_3_0_wenable;

  myram_3
  inst_myram_3
  (
    .CLK(CLK),
    .myram_3_0_addr(myram_3_0_addr),
    .myram_3_0_rdata(myram_3_0_rdata),
    .myram_3_0_wdata(myram_3_0_wdata),
    .myram_3_0_wenable(myram_3_0_wenable)
  );

  reg [32-1:0] th_blink;
  localparam th_blink_init = 0;
  reg signed [32-1:0] _th_blink_times_0;
  reg signed [32-1:0] _th_blink_wdata_1;
  reg signed [32-1:0] _th_blink_i_2;
  reg signed [32-1:0] _th_blink_b_3;
  reg _myram_0_cond_0_1;
  reg _myram_1_cond_0_1;
  reg _myram_2_cond_0_1;
  reg _myram_3_cond_0_1;
  reg signed [32-1:0] _th_blink_sum_4;
  reg _tmp_0;
  reg _myram_0_cond_1_1;
  reg _myram_0_cond_2_1;
  reg _myram_0_cond_2_2;
  reg _tmp_1;
  reg _myram_1_cond_1_1;
  reg _myram_1_cond_2_1;
  reg _myram_1_cond_2_2;
  reg _tmp_2;
  reg _myram_2_cond_1_1;
  reg _myram_2_cond_2_1;
  reg _myram_2_cond_2_2;
  reg _tmp_3;
  reg _myram_3_cond_1_1;
  reg _myram_3_cond_2_1;
  reg _myram_3_cond_2_2;
  reg signed [32-1:0] _tmp_4;
  reg signed [32-1:0] _th_blink_rdata_5;

  always @(posedge CLK) begin
    if(RST) begin
      myram_0_0_addr <= 0;
      myram_0_0_wdata <= 0;
      myram_0_0_wenable <= 0;
      _myram_0_cond_0_1 <= 0;
      _myram_0_cond_1_1 <= 0;
      _tmp_0 <= 0;
      _myram_0_cond_2_1 <= 0;
      _myram_0_cond_2_2 <= 0;
    end else begin
      if(_myram_0_cond_2_2) begin
        _tmp_0 <= 0;
      end 
      if(_myram_0_cond_0_1) begin
        myram_0_0_wenable <= 0;
      end 
      if(_myram_0_cond_1_1) begin
        _tmp_0 <= 1;
      end 
      _myram_0_cond_2_2 <= _myram_0_cond_2_1;
      if((th_blink == 6) && (_th_blink_b_3 == 0)) begin
        myram_0_0_addr <= _th_blink_i_2;
        myram_0_0_wdata <= _th_blink_wdata_1;
        myram_0_0_wenable <= 1;
      end 
      _myram_0_cond_0_1 <= (th_blink == 6) && (_th_blink_b_3 == 0);
      if(th_blink == 16) begin
        myram_0_0_addr <= _th_blink_i_2;
      end 
      _myram_0_cond_1_1 <= th_blink == 16;
      _myram_0_cond_2_1 <= th_blink == 16;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      myram_1_0_addr <= 0;
      myram_1_0_wdata <= 0;
      myram_1_0_wenable <= 0;
      _myram_1_cond_0_1 <= 0;
      _myram_1_cond_1_1 <= 0;
      _tmp_1 <= 0;
      _myram_1_cond_2_1 <= 0;
      _myram_1_cond_2_2 <= 0;
    end else begin
      if(_myram_1_cond_2_2) begin
        _tmp_1 <= 0;
      end 
      if(_myram_1_cond_0_1) begin
        myram_1_0_wenable <= 0;
      end 
      if(_myram_1_cond_1_1) begin
        _tmp_1 <= 1;
      end 
      _myram_1_cond_2_2 <= _myram_1_cond_2_1;
      if((th_blink == 6) && (_th_blink_b_3 == 1)) begin
        myram_1_0_addr <= _th_blink_i_2;
        myram_1_0_wdata <= _th_blink_wdata_1;
        myram_1_0_wenable <= 1;
      end 
      _myram_1_cond_0_1 <= (th_blink == 6) && (_th_blink_b_3 == 1);
      if(th_blink == 16) begin
        myram_1_0_addr <= _th_blink_i_2;
      end 
      _myram_1_cond_1_1 <= th_blink == 16;
      _myram_1_cond_2_1 <= th_blink == 16;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      myram_2_0_addr <= 0;
      myram_2_0_wdata <= 0;
      myram_2_0_wenable <= 0;
      _myram_2_cond_0_1 <= 0;
      _myram_2_cond_1_1 <= 0;
      _tmp_2 <= 0;
      _myram_2_cond_2_1 <= 0;
      _myram_2_cond_2_2 <= 0;
    end else begin
      if(_myram_2_cond_2_2) begin
        _tmp_2 <= 0;
      end 
      if(_myram_2_cond_0_1) begin
        myram_2_0_wenable <= 0;
      end 
      if(_myram_2_cond_1_1) begin
        _tmp_2 <= 1;
      end 
      _myram_2_cond_2_2 <= _myram_2_cond_2_1;
      if((th_blink == 6) && (_th_blink_b_3 == 2)) begin
        myram_2_0_addr <= _th_blink_i_2;
        myram_2_0_wdata <= _th_blink_wdata_1;
        myram_2_0_wenable <= 1;
      end 
      _myram_2_cond_0_1 <= (th_blink == 6) && (_th_blink_b_3 == 2);
      if(th_blink == 16) begin
        myram_2_0_addr <= _th_blink_i_2;
      end 
      _myram_2_cond_1_1 <= th_blink == 16;
      _myram_2_cond_2_1 <= th_blink == 16;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      myram_3_0_addr <= 0;
      myram_3_0_wdata <= 0;
      myram_3_0_wenable <= 0;
      _myram_3_cond_0_1 <= 0;
      _myram_3_cond_1_1 <= 0;
      _tmp_3 <= 0;
      _myram_3_cond_2_1 <= 0;
      _myram_3_cond_2_2 <= 0;
    end else begin
      if(_myram_3_cond_2_2) begin
        _tmp_3 <= 0;
      end 
      if(_myram_3_cond_0_1) begin
        myram_3_0_wenable <= 0;
      end 
      if(_myram_3_cond_1_1) begin
        _tmp_3 <= 1;
      end 
      _myram_3_cond_2_2 <= _myram_3_cond_2_1;
      if((th_blink == 6) && (_th_blink_b_3 == 3)) begin
        myram_3_0_addr <= _th_blink_i_2;
        myram_3_0_wdata <= _th_blink_wdata_1;
        myram_3_0_wenable <= 1;
      end 
      _myram_3_cond_0_1 <= (th_blink == 6) && (_th_blink_b_3 == 3);
      if(th_blink == 16) begin
        myram_3_0_addr <= _th_blink_i_2;
      end 
      _myram_3_cond_1_1 <= th_blink == 16;
      _myram_3_cond_2_1 <= th_blink == 16;
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
      _th_blink_i_2 <= 0;
      _th_blink_b_3 <= 0;
      _th_blink_sum_4 <= 0;
      _tmp_4 <= 0;
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
          _th_blink_i_2 <= 0;
          th_blink <= th_blink_3;
        end
        th_blink_3: begin
          if(_th_blink_i_2 < _th_blink_times_0) begin
            th_blink <= th_blink_4;
          end else begin
            th_blink <= th_blink_11;
          end
        end
        th_blink_4: begin
          _th_blink_b_3 <= 0;
          th_blink <= th_blink_5;
        end
        th_blink_5: begin
          if(_th_blink_b_3 < 4) begin
            th_blink <= th_blink_6;
          end else begin
            th_blink <= th_blink_10;
          end
        end
        th_blink_6: begin
          th_blink <= th_blink_7;
        end
        th_blink_7: begin
          $display("bank:%d wdata = %d", _th_blink_b_3, _th_blink_wdata_1);
          th_blink <= th_blink_8;
        end
        th_blink_8: begin
          _th_blink_wdata_1 <= _th_blink_wdata_1 + 1;
          th_blink <= th_blink_9;
        end
        th_blink_9: begin
          _th_blink_b_3 <= _th_blink_b_3 + 1;
          th_blink <= th_blink_5;
        end
        th_blink_10: begin
          _th_blink_i_2 <= _th_blink_i_2 + 1;
          th_blink <= th_blink_3;
        end
        th_blink_11: begin
          _th_blink_sum_4 <= 0;
          th_blink <= th_blink_12;
        end
        th_blink_12: begin
          _th_blink_i_2 <= 0;
          th_blink <= th_blink_13;
        end
        th_blink_13: begin
          if(_th_blink_i_2 < _th_blink_times_0) begin
            th_blink <= th_blink_14;
          end else begin
            th_blink <= th_blink_22;
          end
        end
        th_blink_14: begin
          _th_blink_b_3 <= 0;
          th_blink <= th_blink_15;
        end
        th_blink_15: begin
          if(_th_blink_b_3 < 4) begin
            th_blink <= th_blink_16;
          end else begin
            th_blink <= th_blink_21;
          end
        end
        th_blink_16: begin
          if(_tmp_0 && (_th_blink_b_3 == 0)) begin
            _tmp_4 <= myram_0_0_rdata;
          end 
          if(_tmp_1 && (_th_blink_b_3 == 1)) begin
            _tmp_4 <= myram_1_0_rdata;
          end 
          if(_tmp_2 && (_th_blink_b_3 == 2)) begin
            _tmp_4 <= myram_2_0_rdata;
          end 
          if(_tmp_3 && (_th_blink_b_3 == 3)) begin
            _tmp_4 <= myram_3_0_rdata;
          end 
          if(_tmp_0) begin
            th_blink <= th_blink_17;
          end 
        end
        th_blink_17: begin
          _th_blink_rdata_5 <= _tmp_4;
          th_blink <= th_blink_18;
        end
        th_blink_18: begin
          _th_blink_sum_4 <= _th_blink_sum_4 + _th_blink_rdata_5;
          th_blink <= th_blink_19;
        end
        th_blink_19: begin
          $display("bank:%d rdata = %d", _th_blink_b_3, _th_blink_rdata_5);
          th_blink <= th_blink_20;
        end
        th_blink_20: begin
          _th_blink_b_3 <= _th_blink_b_3 + 1;
          th_blink <= th_blink_15;
        end
        th_blink_21: begin
          _th_blink_i_2 <= _th_blink_i_2 + 1;
          th_blink <= th_blink_13;
        end
        th_blink_22: begin
          $display("sum = %d", _th_blink_sum_4);
          th_blink <= th_blink_23;
        end
      endcase
    end
  end


endmodule



module myram_0
(
  input CLK,
  input [10-1:0] myram_0_0_addr,
  output [32-1:0] myram_0_0_rdata,
  input [32-1:0] myram_0_0_wdata,
  input myram_0_0_wenable
);

  reg [10-1:0] myram_0_0_daddr;
  reg [32-1:0] mem [0:1024-1];

  always @(posedge CLK) begin
    if(myram_0_0_wenable) begin
      mem[myram_0_0_addr] <= myram_0_0_wdata;
    end 
    myram_0_0_daddr <= myram_0_0_addr;
  end

  assign myram_0_0_rdata = mem[myram_0_0_daddr];

endmodule



module myram_1
(
  input CLK,
  input [10-1:0] myram_1_0_addr,
  output [32-1:0] myram_1_0_rdata,
  input [32-1:0] myram_1_0_wdata,
  input myram_1_0_wenable
);

  reg [10-1:0] myram_1_0_daddr;
  reg [32-1:0] mem [0:1024-1];

  always @(posedge CLK) begin
    if(myram_1_0_wenable) begin
      mem[myram_1_0_addr] <= myram_1_0_wdata;
    end 
    myram_1_0_daddr <= myram_1_0_addr;
  end

  assign myram_1_0_rdata = mem[myram_1_0_daddr];

endmodule



module myram_2
(
  input CLK,
  input [10-1:0] myram_2_0_addr,
  output [32-1:0] myram_2_0_rdata,
  input [32-1:0] myram_2_0_wdata,
  input myram_2_0_wenable
);

  reg [10-1:0] myram_2_0_daddr;
  reg [32-1:0] mem [0:1024-1];

  always @(posedge CLK) begin
    if(myram_2_0_wenable) begin
      mem[myram_2_0_addr] <= myram_2_0_wdata;
    end 
    myram_2_0_daddr <= myram_2_0_addr;
  end

  assign myram_2_0_rdata = mem[myram_2_0_daddr];

endmodule



module myram_3
(
  input CLK,
  input [10-1:0] myram_3_0_addr,
  output [32-1:0] myram_3_0_rdata,
  input [32-1:0] myram_3_0_wdata,
  input myram_3_0_wenable
);

  reg [10-1:0] myram_3_0_daddr;
  reg [32-1:0] mem [0:1024-1];

  always @(posedge CLK) begin
    if(myram_3_0_wenable) begin
      mem[myram_3_0_addr] <= myram_3_0_wdata;
    end 
    myram_3_0_daddr <= myram_3_0_addr;
  end

  assign myram_3_0_rdata = mem[myram_3_0_daddr];

endmodule
"""


def test():
    veriloggen.reset()
    test_module = thread_multibank_ram_bank.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
