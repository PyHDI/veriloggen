from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import thread_multibank_ram_style

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
    #20000;
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
  reg signed [32-1:0] _th_blink_i_1;
  reg signed [32-1:0] _th_blink_wdata_2;
  wire [2-1:0] _tmp_0;
  assign _tmp_0 = _th_blink_i_1;
  reg _myram_0_cond_0_1;
  reg _myram_1_cond_0_1;
  reg _myram_2_cond_0_1;
  reg _myram_3_cond_0_1;
  reg signed [32-1:0] _th_blink_sum_3;
  wire [2-1:0] _tmp_1;
  assign _tmp_1 = _th_blink_i_1;
  reg _tmp_2;
  reg _myram_0_cond_1_1;
  reg _myram_0_cond_2_1;
  reg _myram_0_cond_2_2;
  reg _tmp_3;
  reg _myram_1_cond_1_1;
  reg _myram_1_cond_2_1;
  reg _myram_1_cond_2_2;
  reg _tmp_4;
  reg _myram_2_cond_1_1;
  reg _myram_2_cond_2_1;
  reg _myram_2_cond_2_2;
  reg _tmp_5;
  reg _myram_3_cond_1_1;
  reg _myram_3_cond_2_1;
  reg _myram_3_cond_2_2;
  reg signed [32-1:0] _tmp_6;
  reg signed [32-1:0] _th_blink_rdata_4;

  always @(posedge CLK) begin
    if(RST) begin
      myram_0_0_addr <= 0;
      myram_0_0_wdata <= 0;
      myram_0_0_wenable <= 0;
      _myram_0_cond_0_1 <= 0;
      _myram_0_cond_1_1 <= 0;
      _tmp_2 <= 0;
      _myram_0_cond_2_1 <= 0;
      _myram_0_cond_2_2 <= 0;
    end else begin
      if(_myram_0_cond_2_2) begin
        _tmp_2 <= 0;
      end 
      if(_myram_0_cond_0_1) begin
        myram_0_0_wenable <= 0;
      end 
      if(_myram_0_cond_1_1) begin
        _tmp_2 <= 1;
      end 
      _myram_0_cond_2_2 <= _myram_0_cond_2_1;
      if((th_blink == 4) && (_tmp_0 == 0)) begin
        myram_0_0_addr <= _th_blink_i_1 >> 2;
        myram_0_0_wdata <= _th_blink_wdata_2;
        myram_0_0_wenable <= 1;
      end 
      _myram_0_cond_0_1 <= (th_blink == 4) && (_tmp_0 == 0);
      if(th_blink == 10) begin
        myram_0_0_addr <= _th_blink_i_1 >> 2;
      end 
      _myram_0_cond_1_1 <= th_blink == 10;
      _myram_0_cond_2_1 <= th_blink == 10;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      myram_1_0_addr <= 0;
      myram_1_0_wdata <= 0;
      myram_1_0_wenable <= 0;
      _myram_1_cond_0_1 <= 0;
      _myram_1_cond_1_1 <= 0;
      _tmp_3 <= 0;
      _myram_1_cond_2_1 <= 0;
      _myram_1_cond_2_2 <= 0;
    end else begin
      if(_myram_1_cond_2_2) begin
        _tmp_3 <= 0;
      end 
      if(_myram_1_cond_0_1) begin
        myram_1_0_wenable <= 0;
      end 
      if(_myram_1_cond_1_1) begin
        _tmp_3 <= 1;
      end 
      _myram_1_cond_2_2 <= _myram_1_cond_2_1;
      if((th_blink == 4) && (_tmp_0 == 1)) begin
        myram_1_0_addr <= _th_blink_i_1 >> 2;
        myram_1_0_wdata <= _th_blink_wdata_2;
        myram_1_0_wenable <= 1;
      end 
      _myram_1_cond_0_1 <= (th_blink == 4) && (_tmp_0 == 1);
      if(th_blink == 10) begin
        myram_1_0_addr <= _th_blink_i_1 >> 2;
      end 
      _myram_1_cond_1_1 <= th_blink == 10;
      _myram_1_cond_2_1 <= th_blink == 10;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      myram_2_0_addr <= 0;
      myram_2_0_wdata <= 0;
      myram_2_0_wenable <= 0;
      _myram_2_cond_0_1 <= 0;
      _myram_2_cond_1_1 <= 0;
      _tmp_4 <= 0;
      _myram_2_cond_2_1 <= 0;
      _myram_2_cond_2_2 <= 0;
    end else begin
      if(_myram_2_cond_2_2) begin
        _tmp_4 <= 0;
      end 
      if(_myram_2_cond_0_1) begin
        myram_2_0_wenable <= 0;
      end 
      if(_myram_2_cond_1_1) begin
        _tmp_4 <= 1;
      end 
      _myram_2_cond_2_2 <= _myram_2_cond_2_1;
      if((th_blink == 4) && (_tmp_0 == 2)) begin
        myram_2_0_addr <= _th_blink_i_1 >> 2;
        myram_2_0_wdata <= _th_blink_wdata_2;
        myram_2_0_wenable <= 1;
      end 
      _myram_2_cond_0_1 <= (th_blink == 4) && (_tmp_0 == 2);
      if(th_blink == 10) begin
        myram_2_0_addr <= _th_blink_i_1 >> 2;
      end 
      _myram_2_cond_1_1 <= th_blink == 10;
      _myram_2_cond_2_1 <= th_blink == 10;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      myram_3_0_addr <= 0;
      myram_3_0_wdata <= 0;
      myram_3_0_wenable <= 0;
      _myram_3_cond_0_1 <= 0;
      _myram_3_cond_1_1 <= 0;
      _tmp_5 <= 0;
      _myram_3_cond_2_1 <= 0;
      _myram_3_cond_2_2 <= 0;
    end else begin
      if(_myram_3_cond_2_2) begin
        _tmp_5 <= 0;
      end 
      if(_myram_3_cond_0_1) begin
        myram_3_0_wenable <= 0;
      end 
      if(_myram_3_cond_1_1) begin
        _tmp_5 <= 1;
      end 
      _myram_3_cond_2_2 <= _myram_3_cond_2_1;
      if((th_blink == 4) && (_tmp_0 == 3)) begin
        myram_3_0_addr <= _th_blink_i_1 >> 2;
        myram_3_0_wdata <= _th_blink_wdata_2;
        myram_3_0_wenable <= 1;
      end 
      _myram_3_cond_0_1 <= (th_blink == 4) && (_tmp_0 == 3);
      if(th_blink == 10) begin
        myram_3_0_addr <= _th_blink_i_1 >> 2;
      end 
      _myram_3_cond_1_1 <= th_blink == 10;
      _myram_3_cond_2_1 <= th_blink == 10;
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

  always @(posedge CLK) begin
    if(RST) begin
      th_blink <= th_blink_init;
      _th_blink_times_0 <= 0;
      _th_blink_i_1 <= 0;
      _th_blink_wdata_2 <= 0;
      _th_blink_sum_3 <= 0;
      _tmp_6 <= 0;
      _th_blink_rdata_4 <= 0;
    end else begin
      case(th_blink)
        th_blink_init: begin
          _th_blink_times_0 <= 10;
          th_blink <= th_blink_1;
        end
        th_blink_1: begin
          _th_blink_i_1 <= 0;
          th_blink <= th_blink_2;
        end
        th_blink_2: begin
          if(_th_blink_i_1 < (_th_blink_times_0 << 2)) begin
            th_blink <= th_blink_3;
          end else begin
            th_blink <= th_blink_7;
          end
        end
        th_blink_3: begin
          _th_blink_wdata_2 <= _th_blink_i_1;
          th_blink <= th_blink_4;
        end
        th_blink_4: begin
          th_blink <= th_blink_5;
        end
        th_blink_5: begin
          $display("wdata = %d", _th_blink_wdata_2);
          th_blink <= th_blink_6;
        end
        th_blink_6: begin
          _th_blink_i_1 <= _th_blink_i_1 + 1;
          th_blink <= th_blink_2;
        end
        th_blink_7: begin
          _th_blink_sum_3 <= 0;
          th_blink <= th_blink_8;
        end
        th_blink_8: begin
          _th_blink_i_1 <= 0;
          th_blink <= th_blink_9;
        end
        th_blink_9: begin
          if(_th_blink_i_1 < (_th_blink_times_0 << 2)) begin
            th_blink <= th_blink_10;
          end else begin
            th_blink <= th_blink_15;
          end
        end
        th_blink_10: begin
          if(_tmp_2 && (_tmp_1 == 0)) begin
            _tmp_6 <= myram_0_0_rdata;
          end 
          if(_tmp_3 && (_tmp_1 == 1)) begin
            _tmp_6 <= myram_1_0_rdata;
          end 
          if(_tmp_4 && (_tmp_1 == 2)) begin
            _tmp_6 <= myram_2_0_rdata;
          end 
          if(_tmp_5 && (_tmp_1 == 3)) begin
            _tmp_6 <= myram_3_0_rdata;
          end 
          if(_tmp_2) begin
            th_blink <= th_blink_11;
          end 
        end
        th_blink_11: begin
          _th_blink_rdata_4 <= _tmp_6;
          th_blink <= th_blink_12;
        end
        th_blink_12: begin
          _th_blink_sum_3 <= _th_blink_sum_3 + _th_blink_rdata_4;
          th_blink <= th_blink_13;
        end
        th_blink_13: begin
          $display("rdata = %d", _th_blink_rdata_4);
          th_blink <= th_blink_14;
        end
        th_blink_14: begin
          _th_blink_i_1 <= _th_blink_i_1 + 1;
          th_blink <= th_blink_9;
        end
        th_blink_15: begin
          $display("sum = %d", _th_blink_sum_3);
          th_blink <= th_blink_16;
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
  (* ram_style = "block" *)
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
  (* ram_style = "block" *)
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
  (* ram_style = "block" *)
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
  (* ram_style = "block" *)
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
    test_module = thread_multibank_ram_style.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
