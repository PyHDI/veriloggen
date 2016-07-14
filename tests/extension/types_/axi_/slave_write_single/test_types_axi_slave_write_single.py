from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import types_axi_slave_write_single

expected_verilog = """
module test;

  reg CLK;
  reg RST;
  reg [32-1:0] myaxi_awaddr;
  reg [8-1:0] myaxi_awlen;
  reg myaxi_awvalid;
  wire myaxi_awready;
  reg [32-1:0] myaxi_wdata;
  reg [4-1:0] myaxi_wstrb;
  reg myaxi_wlast;
  reg myaxi_wvalid;
  wire myaxi_wready;
  reg [32-1:0] myaxi_araddr;
  reg [8-1:0] myaxi_arlen;
  reg myaxi_arvalid;
  wire myaxi_arready;
  wire [32-1:0] myaxi_rdata;
  wire myaxi_rlast;
  wire myaxi_rvalid;
  reg myaxi_rready;
  wire _tmp_0;
  assign _tmp_0 = 1;

  always @(*) begin
    myaxi_awvalid <= _tmp_0;
  end

  wire [32-1:0] _tmp_1;
  assign _tmp_1 = 256;

  always @(*) begin
    myaxi_awaddr <= _tmp_1;
  end

  wire [8-1:0] _tmp_2;
  assign _tmp_2 = 0;

  always @(*) begin
    myaxi_awlen <= _tmp_2;
  end

  wire _tmp_3;
  assign _tmp_3 = 0;

  always @(*) begin
    myaxi_arvalid <= _tmp_3;
  end

  wire [32-1:0] _tmp_4;
  assign _tmp_4 = 0;

  always @(*) begin
    myaxi_araddr <= _tmp_4;
  end

  wire [8-1:0] _tmp_5;
  assign _tmp_5 = 0;

  always @(*) begin
    myaxi_arlen <= _tmp_5;
  end

  wire _tmp_6;
  assign _tmp_6 = 1;

  always @(*) begin
    myaxi_wvalid <= _tmp_6;
  end

  wire [32-1:0] _tmp_7;
  assign _tmp_7 = 512;

  always @(*) begin
    myaxi_wdata <= _tmp_7;
  end

  wire [4-1:0] _tmp_8;
  assign _tmp_8 = { 4{ 1'd1 } };

  always @(*) begin
    myaxi_wstrb <= _tmp_8;
  end

  wire _tmp_9;
  assign _tmp_9 = 1;

  always @(*) begin
    myaxi_wlast <= _tmp_9;
  end

  wire _tmp_10;
  assign _tmp_10 = 0;

  always @(*) begin
    myaxi_rready <= _tmp_10;
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
    $dumpvars(0, uut, CLK, RST, myaxi_awaddr, myaxi_awlen, myaxi_awvalid, myaxi_awready, myaxi_wdata, myaxi_wstrb, myaxi_wlast, myaxi_wvalid, myaxi_wready, myaxi_araddr, myaxi_arlen, myaxi_arvalid, myaxi_arready, myaxi_rdata, myaxi_rlast, myaxi_rvalid, myaxi_rready, _tmp_0, _tmp_1, _tmp_2, _tmp_3, _tmp_4, _tmp_5, _tmp_6, _tmp_7, _tmp_8, _tmp_9, _tmp_10);
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
  input RST,
  input [32-1:0] myaxi_awaddr,
  input [8-1:0] myaxi_awlen,
  input myaxi_awvalid,
  output myaxi_awready,
  input [32-1:0] myaxi_wdata,
  input [4-1:0] myaxi_wstrb,
  input myaxi_wlast,
  input myaxi_wvalid,
  output myaxi_wready,
  input [32-1:0] myaxi_araddr,
  input [8-1:0] myaxi_arlen,
  input myaxi_arvalid,
  output myaxi_arready,
  output reg [32-1:0] myaxi_rdata,
  output reg myaxi_rlast,
  output reg myaxi_rvalid,
  input myaxi_rready
);

  assign myaxi_arready = 0;
  reg [32-1:0] fsm;
  localparam fsm_init = 0;
  reg [8-1:0] _tmp_0;
  reg [32-1:0] _tmp_1;
  reg _tmp_2;
  assign myaxi_awready = (fsm == 0) && !_tmp_2;
  reg [32-1:0] sum;
  assign myaxi_wready = fsm == 1;

  always @(posedge CLK) begin
    if(RST) begin
      myaxi_rvalid <= 0;
      myaxi_rlast <= 0;
      _tmp_1 <= 0;
      _tmp_0 <= 0;
      _tmp_2 <= 0;
    end else begin
      myaxi_rvalid <= 0;
      myaxi_rlast <= 0;
      if(myaxi_awready && myaxi_awvalid) begin
        _tmp_1 <= myaxi_awaddr;
        _tmp_0 <= myaxi_awlen + 1;
      end 
      _tmp_2 <= myaxi_awready && myaxi_awvalid;
      if(myaxi_wready && myaxi_wvalid && (_tmp_0 > 0)) begin
        _tmp_0 <= _tmp_0 - 1;
      end 
    end
  end

  localparam fsm_1 = 1;
  localparam fsm_2 = 2;
  localparam fsm_3 = 3;
  localparam fsm_4 = 4;

  always @(posedge CLK) begin
    if(RST) begin
      fsm <= fsm_init;
      sum <= 0;
    end else begin
      case(fsm)
        fsm_init: begin
          if(_tmp_2) begin
            fsm <= fsm_1;
          end 
        end
        fsm_1: begin
          if(myaxi_wready && myaxi_wvalid) begin
            sum <= sum + myaxi_wdata;
          end 
          if(myaxi_wready && myaxi_wvalid && myaxi_wlast) begin
            fsm <= fsm_2;
          end 
        end
        fsm_2: begin
          if(sum < 4096) begin
            fsm <= fsm_init;
          end 
          if(sum >= 4096) begin
            fsm <= fsm_3;
          end 
        end
        fsm_3: begin
          $display("sum=%d expected_sum=%d", sum, 4096);
          fsm <= fsm_4;
        end
      endcase
    end
  end


endmodule
"""


def test():
    veriloggen.reset()
    test_module = types_axi_slave_write_single.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
