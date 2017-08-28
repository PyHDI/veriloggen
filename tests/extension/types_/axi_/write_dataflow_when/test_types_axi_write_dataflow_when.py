from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import types_axi_write_dataflow_when

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
  wire _tmp_0;
  assign _tmp_0 = 0;

  always @(*) begin
    myaxi_arready <= _tmp_0;
  end

  wire _tmp_1;
  assign _tmp_1 = 0;

  always @(*) begin
    myaxi_rvalid <= _tmp_1;
  end

  wire [32-1:0] _tmp_2;
  assign _tmp_2 = 0;

  always @(*) begin
    myaxi_rdata <= _tmp_2;
  end

  wire _tmp_3;
  assign _tmp_3 = 0;

  always @(*) begin
    myaxi_rlast <= _tmp_3;
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
    $dumpvars(0, uut, CLK, RST, myaxi_awaddr, myaxi_awlen, myaxi_awvalid, myaxi_awready, myaxi_wdata, myaxi_wstrb, myaxi_wlast, myaxi_wvalid, myaxi_wready, myaxi_araddr, myaxi_arlen, myaxi_arvalid, myaxi_arready, myaxi_rdata, myaxi_rlast, myaxi_rvalid, myaxi_rready, waddr, _awlen, _tmp_0, _tmp_1, _tmp_2, _tmp_3);
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

  assign myaxi_rready = 0;
  reg [32-1:0] fsm;
  localparam fsm_init = 0;
  reg [9-1:0] _tmp_0;
  reg _myaxi_cond_0_1;
  reg _tmp_1;
  wire _tmp_all_valid_2;
  wire [32-1:0] _tmp_data_3;
  wire _tmp_valid_3;
  wire _tmp_ready_3;
  assign _tmp_ready_3 = (_tmp_0 > 0) && (myaxi_wready || !myaxi_wvalid) && _tmp_all_valid_2;
  wire [1-1:0] _tmp_data_4;
  wire _tmp_valid_4;
  wire _tmp_ready_4;
  assign _tmp_ready_4 = (_tmp_0 > 0) && (myaxi_wready || !myaxi_wvalid) && _tmp_all_valid_2;
  assign _tmp_all_valid_2 = _tmp_valid_3 && _tmp_valid_4;
  reg _myaxi_cond_1_1;
  reg [32-1:0] sum;
  reg _seq_cond_0_1;

  always @(posedge CLK) begin
    if(RST) begin
      myaxi_araddr <= 0;
      myaxi_arlen <= 0;
      myaxi_arvalid <= 0;
      myaxi_awaddr <= 0;
      myaxi_awlen <= 0;
      myaxi_awvalid <= 0;
      _tmp_0 <= 0;
      _myaxi_cond_0_1 <= 0;
      myaxi_wdata <= 0;
      myaxi_wvalid <= 0;
      myaxi_wlast <= 0;
      myaxi_wstrb <= 0;
      _tmp_1 <= 0;
      _myaxi_cond_1_1 <= 0;
    end else begin
      if(_myaxi_cond_0_1) begin
        myaxi_awvalid <= 0;
      end 
      if(_myaxi_cond_1_1) begin
        myaxi_wvalid <= 0;
        myaxi_wlast <= 0;
        _tmp_1 <= 0;
      end 
      myaxi_araddr <= 0;
      myaxi_arlen <= 0;
      myaxi_arvalid <= 0;
      if((fsm == 0) && ((myaxi_awready || !myaxi_awvalid) && (_tmp_0 == 0))) begin
        myaxi_awaddr <= 1024;
        myaxi_awlen <= 63;
        myaxi_awvalid <= 1;
        _tmp_0 <= 64;
      end 
      if((fsm == 0) && ((myaxi_awready || !myaxi_awvalid) && (_tmp_0 == 0)) && 0) begin
        myaxi_awvalid <= 0;
      end 
      _myaxi_cond_0_1 <= 1;
      if(myaxi_awvalid && !myaxi_awready) begin
        myaxi_awvalid <= myaxi_awvalid;
      end 
      if(_tmp_data_4 && (_tmp_valid_3 && ((_tmp_0 > 0) && (myaxi_wready || !myaxi_wvalid) && _tmp_all_valid_2)) && ((_tmp_0 > 0) && (myaxi_wready || !myaxi_wvalid) && (_tmp_0 > 0))) begin
        myaxi_wdata <= _tmp_data_3;
        myaxi_wvalid <= 1;
        myaxi_wlast <= 0;
        myaxi_wstrb <= { 4{ 1'd1 } };
        _tmp_0 <= _tmp_0 - 1;
      end 
      if(_tmp_data_4 && (_tmp_valid_3 && ((_tmp_0 > 0) && (myaxi_wready || !myaxi_wvalid) && _tmp_all_valid_2)) && ((_tmp_0 > 0) && (myaxi_wready || !myaxi_wvalid) && (_tmp_0 > 0)) && (_tmp_0 == 1)) begin
        myaxi_wlast <= 1;
        _tmp_1 <= 1;
      end 
      _myaxi_cond_1_1 <= 1;
      if(myaxi_wvalid && !myaxi_wready) begin
        myaxi_wvalid <= myaxi_wvalid;
        myaxi_wlast <= myaxi_wlast;
        _tmp_1 <= _tmp_1;
      end 
    end
  end

  reg [32-1:0] _tmp_data_5;
  reg _tmp_valid_5;
  wire _tmp_ready_5;
  reg [32-1:0] _tmp_data_6;
  reg _tmp_valid_6;
  wire _tmp_ready_6;
  reg [32-1:0] _tmp_data_7;
  reg _tmp_valid_7;
  wire _tmp_ready_7;
  assign _tmp_ready_5 = (_tmp_ready_7 || !_tmp_valid_7) && _tmp_valid_5;
  reg [32-1:0] _tmp_data_8;
  reg [1-1:0] _tmp_data_9;
  reg _tmp_valid_9;
  wire _tmp_ready_9;
  assign _tmp_ready_6 = (_tmp_ready_9 || !_tmp_valid_9) && _tmp_valid_6;
  assign _tmp_data_3 = _tmp_data_7;
  assign _tmp_valid_3 = _tmp_valid_7;
  assign _tmp_ready_7 = _tmp_ready_3;
  assign _tmp_data_4 = _tmp_data_9;
  assign _tmp_valid_4 = _tmp_valid_9;
  assign _tmp_ready_9 = _tmp_ready_4;

  always @(posedge CLK) begin
    if(RST) begin
      _tmp_data_5 <= 1'sd0;
      _tmp_valid_5 <= 0;
      _tmp_data_6 <= 1'sd0;
      _tmp_valid_6 <= 0;
      _tmp_data_7 <= 0;
      _tmp_valid_7 <= 0;
      _tmp_data_8 <= 0;
      _tmp_data_9 <= 0;
      _tmp_valid_9 <= 0;
    end else begin
      if((_tmp_ready_5 || !_tmp_valid_5) && 1 && 1) begin
        _tmp_data_5 <= _tmp_data_5 + 2'sd1;
      end 
      if(_tmp_valid_5 && _tmp_ready_5) begin
        _tmp_valid_5 <= 0;
      end 
      if((_tmp_ready_5 || !_tmp_valid_5) && 1) begin
        _tmp_valid_5 <= 1;
      end 
      if((_tmp_ready_6 || !_tmp_valid_6) && 1 && 1) begin
        _tmp_data_6 <= (_tmp_data_6 >= 7)? 0 : _tmp_data_6 + 2'sd1;
      end 
      if(_tmp_valid_6 && _tmp_ready_6) begin
        _tmp_valid_6 <= 0;
      end 
      if((_tmp_ready_6 || !_tmp_valid_6) && 1) begin
        _tmp_valid_6 <= 1;
      end 
      if((_tmp_ready_7 || !_tmp_valid_7) && _tmp_ready_5 && _tmp_valid_5) begin
        _tmp_data_7 <= _tmp_data_5 - 2'sd1;
      end 
      if(_tmp_valid_7 && _tmp_ready_7) begin
        _tmp_valid_7 <= 0;
      end 
      if((_tmp_ready_7 || !_tmp_valid_7) && _tmp_ready_5) begin
        _tmp_valid_7 <= _tmp_valid_5;
      end 
      if(_tmp_valid_6 && _tmp_ready_6) begin
        _tmp_data_8 <= _tmp_data_6;
      end 
      if((_tmp_ready_9 || !_tmp_valid_9) && _tmp_ready_6 && _tmp_valid_6) begin
        _tmp_data_9 <= _tmp_data_8 == 1'sd0;
      end 
      if(_tmp_valid_9 && _tmp_ready_9) begin
        _tmp_valid_9 <= 0;
      end 
      if((_tmp_ready_9 || !_tmp_valid_9) && _tmp_ready_6) begin
        _tmp_valid_9 <= _tmp_valid_6;
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
          if(myaxi_awready || !myaxi_awvalid) begin
            fsm <= fsm_1;
          end 
        end
        fsm_1: begin
          if(_tmp_1 && myaxi_wvalid && myaxi_wready) begin
            fsm <= fsm_2;
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
        $display("sum=%d expected_sum=%d", sum, 16128);
      end 
      if(myaxi_wvalid && myaxi_wready) begin
        sum <= sum + myaxi_wdata;
      end 
      _seq_cond_0_1 <= myaxi_wvalid && myaxi_wready && myaxi_wlast;
    end
  end


endmodule
"""


def test():
    veriloggen.reset()
    test_module = types_axi_write_dataflow_when.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
