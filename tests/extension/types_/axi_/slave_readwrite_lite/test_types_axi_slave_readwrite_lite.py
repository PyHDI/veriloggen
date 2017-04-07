from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import types_axi_slave_readwrite_lite

expected_verilog = """
module test;

  reg CLK;
  reg RST;
  wire [32-1:0] sum;
  reg [32-1:0] myaxi_awaddr;
  reg myaxi_awvalid;
  wire myaxi_awready;
  reg [32-1:0] myaxi_wdata;
  reg [4-1:0] myaxi_wstrb;
  reg myaxi_wvalid;
  wire myaxi_wready;
  reg [32-1:0] myaxi_araddr;
  reg myaxi_arvalid;
  wire myaxi_arready;
  wire [32-1:0] myaxi_rdata;
  wire myaxi_rvalid;
  reg myaxi_rready;
  reg [32-1:0] _axi_awaddr;
  reg _axi_awvalid;
  wire _axi_awready;
  reg [32-1:0] _axi_wdata;
  reg [4-1:0] _axi_wstrb;
  reg _axi_wvalid;
  wire _axi_wready;
  reg [32-1:0] _axi_araddr;
  reg _axi_arvalid;
  wire _axi_arready;
  wire [32-1:0] _axi_rdata;
  wire _axi_rvalid;
  wire _axi_rready;
  wire [32-1:0] _tmp_0;
  assign _tmp_0 = _axi_awaddr;

  always @(*) begin
    myaxi_awaddr = _tmp_0;
  end

  wire _tmp_1;
  assign _tmp_1 = _axi_awvalid;

  always @(*) begin
    myaxi_awvalid = _tmp_1;
  end

  assign _axi_awready = myaxi_awready;
  wire [32-1:0] _tmp_2;
  assign _tmp_2 = _axi_wdata;

  always @(*) begin
    myaxi_wdata = _tmp_2;
  end

  wire [4-1:0] _tmp_3;
  assign _tmp_3 = _axi_wstrb;

  always @(*) begin
    myaxi_wstrb = _tmp_3;
  end

  wire _tmp_4;
  assign _tmp_4 = _axi_wvalid;

  always @(*) begin
    myaxi_wvalid = _tmp_4;
  end

  assign _axi_wready = myaxi_wready;
  wire [32-1:0] _tmp_5;
  assign _tmp_5 = _axi_araddr;

  always @(*) begin
    myaxi_araddr = _tmp_5;
  end

  wire _tmp_6;
  assign _tmp_6 = _axi_arvalid;

  always @(*) begin
    myaxi_arvalid = _tmp_6;
  end

  assign _axi_arready = myaxi_arready;
  assign _axi_rdata = myaxi_rdata;
  assign _axi_rvalid = myaxi_rvalid;
  wire _tmp_7;
  assign _tmp_7 = _axi_rready;

  always @(*) begin
    myaxi_rready = _tmp_7;
  end

  reg [32-1:0] fsm;
  localparam fsm_init = 0;
  reg [32-1:0] rsum;
  reg __axi_cond_0_1;
  reg __axi_cond_1_1;
  assign _axi_rready = (fsm == 1) || (fsm == 3);
  reg __axi_cond_2_1;
  reg [32-1:0] wdata;
  reg __axi_cond_3_1;
  reg __axi_cond_4_1;
  reg __axi_cond_5_1;

  main
  uut
  (
    .CLK(CLK),
    .RST(RST),
    .sum(sum),
    .myaxi_awaddr(myaxi_awaddr),
    .myaxi_awvalid(myaxi_awvalid),
    .myaxi_awready(myaxi_awready),
    .myaxi_wdata(myaxi_wdata),
    .myaxi_wstrb(myaxi_wstrb),
    .myaxi_wvalid(myaxi_wvalid),
    .myaxi_wready(myaxi_wready),
    .myaxi_araddr(myaxi_araddr),
    .myaxi_arvalid(myaxi_arvalid),
    .myaxi_arready(myaxi_arready),
    .myaxi_rdata(myaxi_rdata),
    .myaxi_rvalid(myaxi_rvalid),
    .myaxi_rready(myaxi_rready)
  );


  initial begin
    $dumpfile("uut.vcd");
    $dumpvars(0, uut, CLK, RST, sum, myaxi_awaddr, myaxi_awvalid, myaxi_awready, myaxi_wdata, myaxi_wstrb, myaxi_wvalid, myaxi_wready, myaxi_araddr, myaxi_arvalid, myaxi_arready, myaxi_rdata, myaxi_rvalid, myaxi_rready, _axi_awaddr, _axi_awvalid, _axi_awready, _axi_wdata, _axi_wstrb, _axi_wvalid, _axi_wready, _axi_araddr, _axi_arvalid, _axi_arready, _axi_rdata, _axi_rvalid, _axi_rready, _tmp_0, _tmp_1, _tmp_2, _tmp_3, _tmp_4, _tmp_5, _tmp_6, _tmp_7, fsm, rsum, __axi_cond_0_1, __axi_cond_1_1, __axi_cond_2_1, wdata, __axi_cond_3_1, __axi_cond_4_1, __axi_cond_5_1);
  end


  initial begin
    CLK = 0;
    forever begin
      #5 CLK = !CLK;
    end
  end


  initial begin
    RST = 0;
    _axi_awaddr = 0;
    _axi_awvalid = 0;
    _axi_wdata = 0;
    _axi_wstrb = 0;
    _axi_wvalid = 0;
    _axi_araddr = 0;
    _axi_arvalid = 0;
    fsm = fsm_init;
    rsum = 0;
    __axi_cond_0_1 = 0;
    __axi_cond_1_1 = 0;
    __axi_cond_2_1 = 0;
    wdata = 100;
    __axi_cond_3_1 = 0;
    __axi_cond_4_1 = 0;
    __axi_cond_5_1 = 0;
    #100;
    RST = 1;
    #100;
    RST = 0;
    #100000;
    $finish;
  end


  always @(posedge CLK) begin
    if(RST) begin
      _axi_araddr <= 0;
      _axi_arvalid <= 0;
      __axi_cond_0_1 <= 0;
      __axi_cond_1_1 <= 0;
      _axi_awaddr <= 0;
      _axi_awvalid <= 0;
      __axi_cond_2_1 <= 0;
      _axi_wdata <= 0;
      _axi_wvalid <= 0;
      _axi_wstrb <= 0;
      __axi_cond_3_1 <= 0;
      __axi_cond_4_1 <= 0;
      __axi_cond_5_1 <= 0;
    end else begin
      if(__axi_cond_0_1) begin
        _axi_arvalid <= 0;
      end 
      if(__axi_cond_1_1) begin
        _axi_arvalid <= 0;
      end 
      if(__axi_cond_2_1) begin
        _axi_awvalid <= 0;
      end 
      if(__axi_cond_3_1) begin
        _axi_wvalid <= 0;
      end 
      if(__axi_cond_4_1) begin
        _axi_awvalid <= 0;
      end 
      if(__axi_cond_5_1) begin
        _axi_wvalid <= 0;
      end 
      if((fsm == 0) && (_axi_arready || !_axi_arvalid)) begin
        _axi_araddr <= 1024;
        _axi_arvalid <= 1;
      end 
      __axi_cond_0_1 <= 1;
      if(_axi_arvalid && !_axi_arready) begin
        _axi_arvalid <= _axi_arvalid;
      end 
      if((fsm == 2) && (_axi_arready || !_axi_arvalid)) begin
        _axi_araddr <= 2048;
        _axi_arvalid <= 1;
      end 
      __axi_cond_1_1 <= 1;
      if(_axi_arvalid && !_axi_arready) begin
        _axi_arvalid <= _axi_arvalid;
      end 
      if((fsm == 5) && (_axi_awready || !_axi_awvalid)) begin
        _axi_awaddr <= 1024;
        _axi_awvalid <= 1;
      end 
      __axi_cond_2_1 <= 1;
      if(_axi_awvalid && !_axi_awready) begin
        _axi_awvalid <= _axi_awvalid;
      end 
      if((fsm == 6) && (_axi_wready || !_axi_wvalid)) begin
        _axi_wdata <= wdata;
        _axi_wvalid <= 1;
        _axi_wstrb <= { 4{ 1'd1 } };
      end 
      __axi_cond_3_1 <= 1;
      if(_axi_wvalid && !_axi_wready) begin
        _axi_wvalid <= _axi_wvalid;
      end 
      if((fsm == 7) && (_axi_awready || !_axi_awvalid)) begin
        _axi_awaddr <= 1024;
        _axi_awvalid <= 1;
      end 
      __axi_cond_4_1 <= 1;
      if(_axi_awvalid && !_axi_awready) begin
        _axi_awvalid <= _axi_awvalid;
      end 
      if((fsm == 8) && (_axi_wready || !_axi_wvalid)) begin
        _axi_wdata <= wdata;
        _axi_wvalid <= 1;
        _axi_wstrb <= { 4{ 1'd1 } };
      end 
      __axi_cond_5_1 <= 1;
      if(_axi_wvalid && !_axi_wready) begin
        _axi_wvalid <= _axi_wvalid;
      end 
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
  localparam fsm_9 = 9;
  localparam fsm_10 = 10;
  localparam fsm_11 = 11;
  localparam fsm_12 = 12;
  localparam fsm_13 = 13;
  localparam fsm_14 = 14;
  localparam fsm_15 = 15;
  localparam fsm_16 = 16;
  localparam fsm_17 = 17;
  localparam fsm_18 = 18;
  localparam fsm_19 = 19;
  localparam fsm_20 = 20;

  always @(posedge CLK) begin
    if(RST) begin
      fsm <= fsm_init;
      rsum <= 0;
      wdata <= 100;
    end else begin
      case(fsm)
        fsm_init: begin
          if(_axi_arready || !_axi_arvalid) begin
            fsm <= fsm_1;
          end 
        end
        fsm_1: begin
          if(_axi_rready && _axi_rvalid) begin
            rsum <= rsum + _axi_rdata;
          end 
          if(_axi_rready && _axi_rvalid) begin
            fsm <= fsm_2;
          end 
        end
        fsm_2: begin
          if(_axi_arready || !_axi_arvalid) begin
            fsm <= fsm_3;
          end 
        end
        fsm_3: begin
          if(_axi_rready && _axi_rvalid) begin
            rsum <= rsum + _axi_rdata;
          end 
          if(_axi_rready && _axi_rvalid) begin
            fsm <= fsm_4;
          end 
        end
        fsm_4: begin
          $display("rsum=%d expected_rsum=%d", rsum, 768);
          fsm <= fsm_5;
        end
        fsm_5: begin
          wdata <= 100;
          if(_axi_awready || !_axi_awvalid) begin
            fsm <= fsm_6;
          end 
        end
        fsm_6: begin
          if(_axi_wready || !_axi_wvalid) begin
            fsm <= fsm_7;
          end 
        end
        fsm_7: begin
          wdata <= 200;
          if(_axi_awready || !_axi_awvalid) begin
            fsm <= fsm_8;
          end 
        end
        fsm_8: begin
          if(_axi_wready || !_axi_wvalid) begin
            fsm <= fsm_9;
          end 
        end
        fsm_9: begin
          fsm <= fsm_10;
        end
        fsm_10: begin
          fsm <= fsm_11;
        end
        fsm_11: begin
          fsm <= fsm_12;
        end
        fsm_12: begin
          fsm <= fsm_13;
        end
        fsm_13: begin
          fsm <= fsm_14;
        end
        fsm_14: begin
          fsm <= fsm_15;
        end
        fsm_15: begin
          fsm <= fsm_16;
        end
        fsm_16: begin
          fsm <= fsm_17;
        end
        fsm_17: begin
          fsm <= fsm_18;
        end
        fsm_18: begin
          fsm <= fsm_19;
        end
        fsm_19: begin
          $display("sum=%d expected_sum=%d", sum, 300);
          fsm <= fsm_20;
        end
      endcase
    end
  end


endmodule



module main
(
  input CLK,
  input RST,
  output reg [32-1:0] sum,
  input [32-1:0] myaxi_awaddr,
  input myaxi_awvalid,
  output myaxi_awready,
  input [32-1:0] myaxi_wdata,
  input [4-1:0] myaxi_wstrb,
  input myaxi_wvalid,
  output myaxi_wready,
  input [32-1:0] myaxi_araddr,
  input myaxi_arvalid,
  output myaxi_arready,
  output reg [32-1:0] myaxi_rdata,
  output reg myaxi_rvalid,
  input myaxi_rready
);

  reg [32-1:0] fsm;
  localparam fsm_init = 0;
  reg [32-1:0] _tmp_0;
  reg _tmp_1;
  reg _tmp_2;
  reg _tmp_3;
  reg _tmp_4;
  assign myaxi_awready = (fsm == 0) && !_tmp_1 && !_tmp_2 && _tmp_3;
  assign myaxi_arready = (fsm == 0) && !_tmp_2 && !_tmp_1 && _tmp_4;
  reg [32-1:0] rdata;
  reg _myaxi_cond_0_1;
  assign myaxi_wready = fsm == 100;

  always @(posedge CLK) begin
    if(RST) begin
      _tmp_3 <= 0;
      _tmp_4 <= 0;
      _tmp_1 <= 0;
      _tmp_2 <= 0;
      _tmp_0 <= 0;
      myaxi_rdata <= 0;
      myaxi_rvalid <= 0;
      _myaxi_cond_0_1 <= 0;
    end else begin
      if(_myaxi_cond_0_1) begin
        myaxi_rvalid <= 0;
      end 
      _tmp_3 <= myaxi_awvalid;
      _tmp_4 <= myaxi_arvalid;
      _tmp_1 <= 0;
      _tmp_2 <= 0;
      if(myaxi_awready && myaxi_awvalid) begin
        _tmp_0 <= myaxi_awaddr;
        _tmp_1 <= 1;
      end else if(myaxi_arready && myaxi_arvalid) begin
        _tmp_0 <= myaxi_araddr;
        _tmp_2 <= 1;
      end 
      if((fsm == 1) && (myaxi_rready || !myaxi_rvalid)) begin
        myaxi_rdata <= rdata;
        myaxi_rvalid <= 1;
      end 
      _myaxi_cond_0_1 <= 1;
      if(myaxi_rvalid && !myaxi_rready) begin
        myaxi_rvalid <= myaxi_rvalid;
      end 
    end
  end

  localparam fsm_1 = 1;
  localparam fsm_2 = 2;
  localparam fsm_100 = 100;
  localparam fsm_101 = 101;

  always @(posedge CLK) begin
    if(RST) begin
      fsm <= fsm_init;
      rdata <= 0;
      sum <= 0;
    end else begin
      case(fsm)
        fsm_init: begin
          if(_tmp_2) begin
            rdata <= _tmp_0 >> 2;
          end 
          if(_tmp_1) begin
            fsm <= fsm_100;
          end 
          if(_tmp_2) begin
            fsm <= fsm_1;
          end 
        end
        fsm_1: begin
          if(myaxi_rready || !myaxi_rvalid) begin
            rdata <= rdata + 1;
          end 
          if(myaxi_rready || !myaxi_rvalid) begin
            fsm <= fsm_2;
          end 
        end
        fsm_2: begin
          fsm <= fsm_init;
        end
        fsm_100: begin
          if(myaxi_wready && myaxi_wvalid) begin
            sum <= sum + myaxi_wdata;
          end 
          if(myaxi_wready && myaxi_wvalid) begin
            fsm <= fsm_101;
          end 
        end
        fsm_101: begin
          fsm <= fsm_init;
        end
      endcase
    end
  end


endmodule
"""


def test():
    veriloggen.reset()
    test_module = types_axi_slave_readwrite_lite.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
