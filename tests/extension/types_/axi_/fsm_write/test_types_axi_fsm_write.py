from __future__ import absolute_import
from __future__ import print_function
import types_axi_fsm_write

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
  localparam waddr_1 = 1;
  localparam waddr_2 = 2;

  always @(posedge CLK) begin
    if(RST) begin
      waddr <= waddr_init;
    end else begin
      case(waddr)
        waddr_init: begin
          myaxi_awready <= 0;
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
          waddr <= waddr_init;
        end
      endcase
    end
  end

  reg [32-1:0] wdata;
  localparam wdata_init = 0;
  localparam wdata_1 = 1;
  localparam wdata_2 = 2;

  always @(posedge CLK) begin
    if(RST) begin
      wdata <= wdata_init;
    end else begin
      case(wdata)
        wdata_init: begin
          myaxi_wready <= 0;
          if(myaxi_wvalid) begin
            wdata <= wdata_1;
          end 
        end
        wdata_1: begin
          if(myaxi_wvalid) begin
            myaxi_wready <= 1;
          end 
          wdata <= wdata_2;
        end
        wdata_2: begin
          myaxi_wready <= 0;
          wdata <= wdata_init;
        end
      endcase
    end
  end

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
    $dumpvars(0, uut, CLK, RST, myaxi_awaddr, myaxi_awlen, myaxi_awvalid, myaxi_awready, myaxi_wdata, myaxi_wstrb, myaxi_wlast, myaxi_wvalid, myaxi_wready, myaxi_araddr, myaxi_arlen, myaxi_arvalid, myaxi_arready, myaxi_rdata, myaxi_rlast, myaxi_rvalid, myaxi_rready, waddr, wdata, _tmp_0, _tmp_1, _tmp_2, _tmp_3);
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
    wdata = wdata_init;
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
  output reg myaxi_rready
);

  reg [32-1:0] fsm;
  localparam fsm_init = 0;
  reg [8-1:0] _tmp_0;
  reg _myaxi_cond_0_1;
  reg [32-1:0] wdata;
  reg _tmp_1;
  reg _myaxi_cond_1_1;
  localparam fsm_1 = 1;
  localparam fsm_2 = 2;

  always @(posedge CLK) begin
    if(RST) begin
      fsm <= fsm_init;
      wdata <= 0;
    end else begin
      case(fsm)
        fsm_init: begin
          if(myaxi_awready || !myaxi_awvalid) begin
            fsm <= fsm_1;
          end 
        end
        fsm_1: begin
          if(myaxi_wready || !myaxi_wvalid) begin
            wdata <= wdata + 1;
          end 
          if((myaxi_wready || !myaxi_wvalid) && _tmp_1) begin
            fsm <= fsm_2;
          end 
        end
      endcase
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      myaxi_araddr <= 0;
      myaxi_arlen <= 0;
      myaxi_arvalid <= 0;
      myaxi_rready <= 0;
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
      myaxi_rready <= 0;
      if((fsm == 0) && (myaxi_awready || !myaxi_awvalid)) begin
        myaxi_awaddr <= 1024;
        myaxi_awlen <= 63;
        myaxi_awvalid <= 1;
        _tmp_0 <= 63;
      end 
      _myaxi_cond_0_1 <= 1;
      if(myaxi_awvalid && !myaxi_awready) begin
        myaxi_awvalid <= myaxi_awvalid;
      end 
      if((fsm == 1) && ((myaxi_wready || !myaxi_wvalid) && !_tmp_1)) begin
        myaxi_wdata <= wdata;
        myaxi_wvalid <= 1;
        myaxi_wlast <= 0;
        myaxi_wstrb <= { 4{ 1'd1 } };
        _tmp_0 <= _tmp_0 - 1;
      end 
      if((fsm == 1) && ((myaxi_wready || !myaxi_wvalid) && !_tmp_1) && (_tmp_0 == 0)) begin
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


endmodule
"""

def test():
    test_module = types_axi_fsm_write.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
