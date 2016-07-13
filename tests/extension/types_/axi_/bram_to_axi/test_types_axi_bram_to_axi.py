from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import types_axi_bram_to_axi

expected_verilog = """
module test;

  reg CLK;
  reg RST;
  wire [32-1:0] myaxi_awaddr;
  wire [8-1:0] myaxi_awlen;
  wire myaxi_awvalid;
  reg myaxi_awready;
  wire [32-1:0] myaxi_wdata;
  wire [4-1:0] myaxi_wstrb;
  wire myaxi_wlast;
  wire myaxi_wvalid;
  reg myaxi_wready;
  wire [32-1:0] myaxi_araddr;
  wire [8-1:0] myaxi_arlen;
  wire myaxi_arvalid;
  reg myaxi_arready;
  reg [32-1:0] myaxi_rdata;
  reg myaxi_rlast;
  reg myaxi_rvalid;
  wire myaxi_rready;
  reg [32-1:0] waddr;
  localparam waddr_init = 0;
  reg [32-1:0] _awlen;
  reg [32-1:0] raddr;
  localparam raddr_init = 0;
  reg [32-1:0] _arlen;
  reg [32-1:0] _d1_raddr;
  reg _raddr_cond_3_0_1;
  localparam raddr_1 = 1;
  localparam raddr_2 = 2;
  localparam raddr_3 = 3;
  localparam raddr_4 = 4;
  localparam raddr_5 = 5;
  localparam raddr_6 = 6;
  localparam raddr_7 = 7;
  localparam raddr_8 = 8;
  localparam raddr_9 = 9;
  localparam raddr_10 = 10;

  always @(posedge CLK) begin
    if(RST) begin
      raddr <= raddr_init;
      _d1_raddr <= raddr_init;
      _arlen <= 0;
      _raddr_cond_3_0_1 <= 0;
    end else begin
      _d1_raddr <= raddr;
      case(_d1_raddr)
        raddr_3: begin
          if(_raddr_cond_3_0_1) begin
            myaxi_rvalid <= 0;
            myaxi_rlast <= 0;
          end 
        end
      endcase
      case(raddr)
        raddr_init: begin
          myaxi_arready <= 0;
          myaxi_rdata <= -1;
          myaxi_rvalid <= 0;
          myaxi_rlast <= 0;
          if(myaxi_arvalid) begin
            raddr <= raddr_1;
          end 
        end
        raddr_1: begin
          if(myaxi_arvalid) begin
            myaxi_arready <= 1;
            myaxi_rdata <= myaxi_araddr - 1;
          end 
          raddr <= raddr_2;
        end
        raddr_2: begin
          myaxi_arready <= 0;
          _arlen <= myaxi_arlen;
          raddr <= raddr_3;
        end
        raddr_3: begin
          if((myaxi_rready || !myaxi_rvalid) && !myaxi_rlast) begin
            myaxi_rdata <= myaxi_rdata + 1;
            myaxi_rvalid <= 1;
            myaxi_rlast <= 0;
            _arlen <= _arlen - 1;
          end 
          if((myaxi_rready || !myaxi_rvalid) && !myaxi_rlast && (_arlen == 0)) begin
            myaxi_rlast <= 1;
          end 
          _raddr_cond_3_0_1 <= 1;
          raddr <= raddr_4;
        end
        raddr_4: begin
          if(myaxi_rvalid && !myaxi_rready) begin
            myaxi_rvalid <= myaxi_rvalid;
            myaxi_rlast <= myaxi_rlast;
          end 
          if(myaxi_rvalid && myaxi_rready) begin
            raddr <= raddr_5;
          end 
        end
        raddr_5: begin
          raddr <= raddr_6;
        end
        raddr_6: begin
          raddr <= raddr_7;
        end
        raddr_7: begin
          raddr <= raddr_8;
        end
        raddr_8: begin
          if((_arlen + 1 & 255) != 0) begin
            raddr <= raddr_3;
          end 
          if((_arlen + 1 & 255) == 0) begin
            raddr <= raddr_9;
          end 
        end
        raddr_9: begin
          raddr <= raddr_10;
        end
        raddr_10: begin
          raddr <= raddr_init;
        end
      endcase
    end
  end


  main
  uut
  (
    .CLK(CLK),
    .RST(RST),
    .myaxi_awaddr(myaxi_awaddr),
    .myaxi_awlen(myaxi_awlen),
    .myaxi_awvalid(myaxi_awvalid),
    .myaxi_awready(myaxi_awready),
    .myaxi_wdata(myaxi_wdata),
    .myaxi_wstrb(myaxi_wstrb),
    .myaxi_wlast(myaxi_wlast),
    .myaxi_wvalid(myaxi_wvalid),
    .myaxi_wready(myaxi_wready),
    .myaxi_araddr(myaxi_araddr),
    .myaxi_arlen(myaxi_arlen),
    .myaxi_arvalid(myaxi_arvalid),
    .myaxi_arready(myaxi_arready),
    .myaxi_rdata(myaxi_rdata),
    .myaxi_rlast(myaxi_rlast),
    .myaxi_rvalid(myaxi_rvalid),
    .myaxi_rready(myaxi_rready)
  );


  initial begin
    $dumpfile("uut.vcd");
    $dumpvars(0, uut, CLK, RST, myaxi_awaddr, myaxi_awlen, myaxi_awvalid, myaxi_awready, myaxi_wdata, myaxi_wstrb, myaxi_wlast, myaxi_wvalid, myaxi_wready, myaxi_araddr, myaxi_arlen, myaxi_arvalid, myaxi_arready, myaxi_rdata, myaxi_rlast, myaxi_rvalid, myaxi_rready, waddr, _awlen, raddr, _arlen, _d1_raddr, _raddr_cond_3_0_1);
  end


  initial begin
    CLK = 0;
    forever begin
      #5 CLK = !CLK;
    end
  end


  initial begin
    RST = 0;
    waddr = waddr_init;
    _awlen = 0;
    raddr = raddr_init;
    _arlen = 0;
    _d1_raddr = raddr_init;
    _raddr_cond_3_0_1 = 0;
    #100;
    RST = 1;
    #100;
    RST = 0;
    #100000;
    $finish;
  end

  localparam waddr_1 = 1;
  localparam waddr_2 = 2;
  localparam waddr_3 = 3;
  localparam waddr_4 = 4;
  localparam waddr_5 = 5;
  localparam waddr_6 = 6;
  localparam waddr_7 = 7;
  localparam waddr_8 = 8;

  always @(posedge CLK) begin
    if(RST) begin
      waddr <= waddr_init;
      _awlen <= 0;
    end else begin
      case(waddr)
        waddr_init: begin
          myaxi_awready <= 0;
          myaxi_wready <= 0;
          _awlen <= 0;
          if(myaxi_awvalid) begin
            waddr <= waddr_1;
          end 
        end
        waddr_1: begin
          if(myaxi_awvalid) begin
            myaxi_awready <= 1;
          end 
          waddr <= waddr_2;
        end
        waddr_2: begin
          myaxi_awready <= 0;
          _awlen <= myaxi_awlen;
          waddr <= waddr_3;
        end
        waddr_3: begin
          myaxi_wready <= 0;
          if(myaxi_wvalid) begin
            waddr <= waddr_4;
          end 
        end
        waddr_4: begin
          if(myaxi_wvalid) begin
            myaxi_wready <= 1;
          end 
          waddr <= waddr_5;
        end
        waddr_5: begin
          myaxi_wready <= 0;
          waddr <= waddr_6;
        end
        waddr_6: begin
          waddr <= waddr_7;
        end
        waddr_7: begin
          waddr <= waddr_8;
        end
        waddr_8: begin
          _awlen <= _awlen - 1;
          waddr <= waddr_3;
          if(_awlen == 0) begin
            waddr <= waddr_init;
          end 
        end
      endcase
    end
  end


endmodule



module main
(
  input CLK,
  input RST,
  output reg [32-1:0] myaxi_awaddr,
  output reg [8-1:0] myaxi_awlen,
  output reg myaxi_awvalid,
  input myaxi_awready,
  output reg [32-1:0] myaxi_wdata,
  output reg [4-1:0] myaxi_wstrb,
  output reg myaxi_wlast,
  output reg myaxi_wvalid,
  input myaxi_wready,
  output reg [32-1:0] myaxi_araddr,
  output reg [8-1:0] myaxi_arlen,
  output reg myaxi_arvalid,
  input myaxi_arready,
  input [32-1:0] myaxi_rdata,
  input myaxi_rlast,
  input myaxi_rvalid,
  output myaxi_rready
);

  reg [10-1:0] mybram_0_addr;
  wire [32-1:0] mybram_0_rdata;
  reg [32-1:0] mybram_0_wdata;
  reg mybram_0_wenable;

  mybram
  inst_mybram
  (
    .CLK(CLK),
    .mybram_0_addr(mybram_0_addr),
    .mybram_0_rdata(mybram_0_rdata),
    .mybram_0_wdata(mybram_0_wdata),
    .mybram_0_wenable(mybram_0_wenable)
  );

  reg [32-1:0] fsm;
  localparam fsm_init = 0;
  reg [8-1:0] _tmp_0;
  reg _myaxi_cond_0_1;
  wire _tmp_1;
  wire _tmp_2;
  assign _tmp_1 = 1 && ((_tmp_ready_22 || !_tmp_valid_22) && (myaxi_rvalid && myaxi_rvalid));
  assign _tmp_2 = 1 && ((_tmp_ready_22 || !_tmp_valid_22) && (myaxi_rvalid && myaxi_rvalid));
  assign myaxi_rready = _tmp_1 && _tmp_2;
  reg [8-1:0] _tmp_3;
  reg _tmp_4;
  wire [32-1:0] _tmp_data_5;
  wire _tmp_valid_5;
  wire _tmp_ready_5;
  assign _tmp_ready_5 = (fsm == 1) && !_tmp_4;
  reg _mybram_cond_0_1;
  reg [8-1:0] _tmp_6;
  reg _myaxi_cond_1_1;
  reg _tmp_7;
  reg _tmp_8;
  wire _tmp_9;
  wire _tmp_10;
  assign _tmp_9 = 1 && _tmp_ready_20;
  assign _tmp_10 = 1;
  localparam _tmp_11 = 1;
  wire [_tmp_11-1:0] _tmp_12;
  assign _tmp_12 = (_tmp_9 || !_tmp_7) && (_tmp_10 || !_tmp_8);
  reg [_tmp_11-1:0] __tmp_12_1;
  wire [32-1:0] _tmp_13;
  reg [32-1:0] __tmp_13_1;
  assign _tmp_13 = (__tmp_12_1)? mybram_0_rdata : __tmp_13_1;
  reg [8-1:0] _tmp_14;
  reg _tmp_15;
  reg _tmp_16;
  reg _tmp_17;
  reg _tmp_18;
  reg _tmp_19;
  wire [32-1:0] _tmp_data_20;
  wire _tmp_valid_20;
  wire _tmp_ready_20;
  assign _tmp_ready_20 = myaxi_wready || !myaxi_wvalid;
  reg _myaxi_cond_2_1;
  reg [32-1:0] sum;
  reg _seq_cond_0_1;

  always @(posedge CLK) begin
    if(RST) begin
      myaxi_araddr <= 0;
      myaxi_arlen <= 0;
      myaxi_arvalid <= 0;
      _tmp_0 <= 0;
      _myaxi_cond_0_1 <= 0;
      myaxi_awaddr <= 0;
      myaxi_awlen <= 0;
      myaxi_awvalid <= 0;
      _tmp_6 <= 0;
      _myaxi_cond_1_1 <= 0;
      myaxi_wdata <= 0;
      myaxi_wvalid <= 0;
      myaxi_wlast <= 0;
      myaxi_wstrb <= 0;
      _tmp_19 <= 0;
      _myaxi_cond_2_1 <= 0;
    end else begin
      if(_myaxi_cond_0_1) begin
        myaxi_arvalid <= 0;
      end 
      if(_myaxi_cond_1_1) begin
        myaxi_awvalid <= 0;
      end 
      if(_myaxi_cond_2_1) begin
        myaxi_wvalid <= 0;
        myaxi_wlast <= 0;
        _tmp_19 <= 0;
      end 
      if((fsm == 0) && ((myaxi_arready || !myaxi_arvalid) && (_tmp_0 == 0))) begin
        myaxi_araddr <= 1024;
        myaxi_arlen <= 63;
        myaxi_arvalid <= 1;
        _tmp_0 <= 64;
      end 
      _myaxi_cond_0_1 <= 1;
      if(myaxi_arvalid && !myaxi_arready) begin
        myaxi_arvalid <= myaxi_arvalid;
      end 
      if(myaxi_rready && myaxi_rvalid && (_tmp_0 > 0)) begin
        _tmp_0 <= _tmp_0 - 1;
      end 
      if((fsm == 2) && ((myaxi_awready || !myaxi_awvalid) && (_tmp_6 == 0))) begin
        myaxi_awaddr <= 1024;
        myaxi_awlen <= 63;
        myaxi_awvalid <= 1;
        _tmp_6 <= 64;
      end 
      if((fsm == 2) && ((myaxi_awready || !myaxi_awvalid) && (_tmp_6 == 0)) && 0) begin
        myaxi_awvalid <= 0;
      end 
      _myaxi_cond_1_1 <= 1;
      if(myaxi_awvalid && !myaxi_awready) begin
        myaxi_awvalid <= myaxi_awvalid;
      end 
      if(_tmp_valid_20 && (myaxi_wready || !myaxi_wvalid) && ((myaxi_wready || !myaxi_wvalid) && (_tmp_6 > 0))) begin
        myaxi_wdata <= _tmp_data_20;
        myaxi_wvalid <= 1;
        myaxi_wlast <= 0;
        myaxi_wstrb <= { 4{ 1'd1 } };
        _tmp_6 <= _tmp_6 - 1;
      end 
      if(_tmp_valid_20 && (myaxi_wready || !myaxi_wvalid) && ((myaxi_wready || !myaxi_wvalid) && (_tmp_6 > 0)) && (_tmp_6 == 1)) begin
        myaxi_wlast <= 1;
        _tmp_19 <= 1;
      end 
      _myaxi_cond_2_1 <= 1;
      if(myaxi_wvalid && !myaxi_wready) begin
        myaxi_wvalid <= myaxi_wvalid;
        myaxi_wlast <= myaxi_wlast;
        _tmp_19 <= _tmp_19;
      end 
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      mybram_0_addr <= 0;
      mybram_0_wdata <= 0;
      mybram_0_wenable <= 0;
      _tmp_3 <= 0;
      _tmp_4 <= 0;
      _mybram_cond_0_1 <= 0;
      __tmp_12_1 <= 0;
      __tmp_13_1 <= 0;
      _tmp_18 <= 0;
      _tmp_7 <= 0;
      _tmp_8 <= 0;
      _tmp_16 <= 0;
      _tmp_17 <= 0;
      _tmp_15 <= 0;
      _tmp_14 <= 0;
    end else begin
      if(_mybram_cond_0_1) begin
        mybram_0_wenable <= 0;
        _tmp_4 <= 0;
      end 
      if(_tmp_valid_5 && ((fsm == 1) && !_tmp_4) && (_tmp_3 == 0)) begin
        mybram_0_addr <= 0;
        mybram_0_wdata <= _tmp_data_5;
        mybram_0_wenable <= 1;
        _tmp_3 <= 63;
      end 
      if(_tmp_valid_5 && ((fsm == 1) && !_tmp_4) && (_tmp_3 > 0)) begin
        mybram_0_addr <= mybram_0_addr + 1;
        mybram_0_wdata <= _tmp_data_5;
        mybram_0_wenable <= 1;
        _tmp_3 <= _tmp_3 - 1;
      end 
      if(_tmp_valid_5 && ((fsm == 1) && !_tmp_4) && (_tmp_3 == 1)) begin
        _tmp_4 <= 1;
      end 
      _mybram_cond_0_1 <= 1;
      __tmp_12_1 <= _tmp_12;
      __tmp_13_1 <= _tmp_13;
      if((_tmp_9 || !_tmp_7) && (_tmp_10 || !_tmp_8) && _tmp_16) begin
        _tmp_18 <= 0;
        _tmp_7 <= 0;
        _tmp_8 <= 0;
        _tmp_16 <= 0;
      end 
      if((_tmp_9 || !_tmp_7) && (_tmp_10 || !_tmp_8) && _tmp_15) begin
        _tmp_7 <= 1;
        _tmp_8 <= 1;
        _tmp_18 <= _tmp_17;
        _tmp_17 <= 0;
        _tmp_15 <= 0;
        _tmp_16 <= 1;
      end 
      if((_tmp_9 || !_tmp_7) && (_tmp_10 || !_tmp_8) && (fsm == 3) && (_tmp_14 == 0) && !_tmp_17 && !_tmp_18) begin
        mybram_0_addr <= 0;
        _tmp_14 <= 63;
        _tmp_15 <= 1;
      end 
      if((_tmp_9 || !_tmp_7) && (_tmp_10 || !_tmp_8) && (_tmp_14 > 0)) begin
        mybram_0_addr <= mybram_0_addr + 1;
        _tmp_14 <= _tmp_14 - 1;
        _tmp_15 <= 1;
        _tmp_17 <= 0;
      end 
      if((_tmp_9 || !_tmp_7) && (_tmp_10 || !_tmp_8) && (_tmp_14 == 1)) begin
        _tmp_17 <= 1;
      end 
    end
  end

  assign _tmp_data_20 = _tmp_13;
  assign _tmp_valid_20 = _tmp_7;
  reg [1-1:0] _tmp_data_21;
  reg [32-1:0] _tmp_data_22;
  reg _tmp_valid_22;
  wire _tmp_ready_22;
  assign _tmp_data_5 = _tmp_data_22;
  assign _tmp_valid_5 = _tmp_valid_22;
  assign _tmp_ready_22 = _tmp_ready_5;

  always @(posedge CLK) begin
    if(RST) begin
      _tmp_data_21 <= 0;
      _tmp_data_22 <= 1'd0;
      _tmp_valid_22 <= 0;
    end else begin
      if(myaxi_rvalid && _tmp_2) begin
        _tmp_data_21 <= myaxi_rlast;
      end 
      if((_tmp_ready_22 || !_tmp_valid_22) && (_tmp_1 && _tmp_2) && (myaxi_rvalid && myaxi_rvalid)) begin
        _tmp_data_22 <= _tmp_data_22 + myaxi_rdata;
      end 
      if(_tmp_valid_22 && _tmp_ready_22) begin
        _tmp_valid_22 <= 0;
      end 
      if((_tmp_ready_22 || !_tmp_valid_22) && (_tmp_1 && _tmp_2)) begin
        _tmp_valid_22 <= myaxi_rvalid && myaxi_rvalid;
      end 
      if((_tmp_ready_22 || !_tmp_valid_22) && (_tmp_1 && _tmp_2) && (myaxi_rvalid && myaxi_rvalid) && _tmp_data_21) begin
        _tmp_data_22 <= 1'd0 + myaxi_rdata;
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
          if(myaxi_arready || !myaxi_arvalid) begin
            fsm <= fsm_1;
          end 
        end
        fsm_1: begin
          if(_tmp_4) begin
            fsm <= fsm_2;
          end 
        end
        fsm_2: begin
          if(myaxi_awready || !myaxi_awvalid) begin
            fsm <= fsm_3;
          end 
        end
        fsm_3: begin
          if(_tmp_18) begin
            fsm <= fsm_4;
          end 
        end
        fsm_4: begin
          if(_tmp_19) begin
            fsm <= fsm_5;
          end 
        end
      endcase
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      sum <= 0;
      _seq_cond_0_1 <= 0;
    end else begin
      if(_seq_cond_0_1) begin
        $display("sum=%d expected_sum=%d", sum, 2173600);
      end 
      if(myaxi_wvalid && myaxi_wready) begin
        sum <= sum + myaxi_wdata;
      end 
      _seq_cond_0_1 <= myaxi_wvalid && myaxi_wready && myaxi_wlast;
    end
  end


endmodule



module mybram
(
  input CLK,
  input [10-1:0] mybram_0_addr,
  output [32-1:0] mybram_0_rdata,
  input [32-1:0] mybram_0_wdata,
  input mybram_0_wenable
);

  reg [10-1:0] mybram_0_daddr;
  reg [32-1:0] mem [0:1024-1];

  always @(posedge CLK) begin
    if(mybram_0_wenable) begin
      mem[mybram_0_addr] <= mybram_0_wdata;
    end 
    mybram_0_daddr <= mybram_0_addr;
  end

  assign mybram_0_rdata = mem[mybram_0_daddr];

endmodule
"""


def test():
    veriloggen.reset()
    test_module = types_axi_bram_to_axi.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
