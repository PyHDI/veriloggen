from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import types_axi_read_dataflow

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
  wire _tmp_0;
  assign _tmp_0 = 1;

  always @(*) begin
    myaxi_awready <= _tmp_0;
  end

  wire _tmp_1;
  assign _tmp_1 = 1;

  always @(*) begin
    myaxi_wready <= _tmp_1;
  end

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
          if(myaxi_rvalid && !myaxi_rready) begin
            myaxi_rvalid <= myaxi_rvalid;
            myaxi_rlast <= myaxi_rlast;
          end 
          if(myaxi_rvalid && myaxi_rready && myaxi_rlast) begin
            raddr <= raddr_4;
          end 
        end
        raddr_4: begin
          raddr <= raddr_5;
        end
        raddr_5: begin
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
    $dumpvars(0, uut, CLK, RST, myaxi_awaddr, myaxi_awlen, myaxi_awvalid, myaxi_awready, myaxi_wdata, myaxi_wstrb, myaxi_wlast, myaxi_wvalid, myaxi_wready, myaxi_araddr, myaxi_arlen, myaxi_arvalid, myaxi_arready, myaxi_rdata, myaxi_rlast, myaxi_rvalid, myaxi_rready, _tmp_0, _tmp_1, raddr, _arlen, _d1_raddr, _raddr_cond_3_0_1);
  end


  initial begin
    CLK = 0;
    forever begin
      #5 CLK = !CLK;
    end
  end


  initial begin
    RST = 0;
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

  reg [32-1:0] req_fsm;
  localparam req_fsm_init = 0;
  reg [9-1:0] _tmp_0;
  reg _myaxi_cond_0_1;
  wire _tmp_1;
  wire _tmp_2;
  assign myaxi_rready = _tmp_1 && _tmp_2;
  wire signed [32-1:0] _reduceadd_data_3;
  wire _reduceadd_valid_3;
  wire _reduceadd_ready_3;
  assign _reduceadd_ready_3 = 1;
  wire [1-1:0] __variable_data_4;
  wire __variable_valid_4;
  wire __variable_ready_4;
  assign __variable_ready_4 = 1;
  reg _data_seq_cond_0_1;

  always @(posedge CLK) begin
    if(RST) begin
      myaxi_awaddr <= 0;
      myaxi_awlen <= 0;
      myaxi_awvalid <= 0;
      myaxi_wdata <= 0;
      myaxi_wstrb <= 0;
      myaxi_wvalid <= 0;
      myaxi_wlast <= 0;
      myaxi_araddr <= 0;
      myaxi_arlen <= 0;
      myaxi_arvalid <= 0;
      _tmp_0 <= 0;
      _myaxi_cond_0_1 <= 0;
    end else begin
      if(_myaxi_cond_0_1) begin
        myaxi_arvalid <= 0;
      end 
      myaxi_awaddr <= 0;
      myaxi_awlen <= 0;
      myaxi_awvalid <= 0;
      myaxi_wdata <= 0;
      myaxi_wstrb <= 0;
      myaxi_wvalid <= 0;
      myaxi_wlast <= 0;
      if((req_fsm == 0) && ((myaxi_arready || !myaxi_arvalid) && (_tmp_0 == 0))) begin
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
    end
  end

  assign __variable_data_4 = myaxi_rlast;
  assign __variable_valid_4 = myaxi_rvalid;
  reg [1-1:0] __prev_data_5;
  reg signed [32-1:0] _reduceadd_data_6;
  reg _reduceadd_valid_6;
  wire _reduceadd_ready_6;
  assign _tmp_1 = 1 && ((_reduceadd_ready_6 || !_reduceadd_valid_6) && (myaxi_rvalid && myaxi_rvalid));
  assign _tmp_2 = 1 && __variable_ready_4 && ((_reduceadd_ready_6 || !_reduceadd_valid_6) && (myaxi_rvalid && myaxi_rvalid));
  assign _reduceadd_data_3 = _reduceadd_data_6;
  assign _reduceadd_valid_3 = _reduceadd_valid_6;
  assign _reduceadd_ready_6 = _reduceadd_ready_3;

  always @(posedge CLK) begin
    if(RST) begin
      __prev_data_5 <= 0;
      _reduceadd_data_6 <= 1'sd0;
      _reduceadd_valid_6 <= 0;
    end else begin
      if(myaxi_rvalid && _tmp_2) begin
        __prev_data_5 <= myaxi_rlast;
      end 
      if((_reduceadd_ready_6 || !_reduceadd_valid_6) && (_tmp_1 && _tmp_2) && (myaxi_rvalid && myaxi_rvalid)) begin
        _reduceadd_data_6 <= _reduceadd_data_6 + myaxi_rdata;
      end 
      if(_reduceadd_valid_6 && _reduceadd_ready_6) begin
        _reduceadd_valid_6 <= 0;
      end 
      if((_reduceadd_ready_6 || !_reduceadd_valid_6) && (_tmp_1 && _tmp_2)) begin
        _reduceadd_valid_6 <= myaxi_rvalid && myaxi_rvalid;
      end 
      if((_reduceadd_ready_6 || !_reduceadd_valid_6) && (_tmp_1 && _tmp_2) && (myaxi_rvalid && myaxi_rvalid) && __prev_data_5) begin
        _reduceadd_data_6 <= 1'sd0 + myaxi_rdata;
      end 
    end
  end

  localparam req_fsm_1 = 1;

  always @(posedge CLK) begin
    if(RST) begin
      req_fsm <= req_fsm_init;
    end else begin
      case(req_fsm)
        req_fsm_init: begin
          if(myaxi_arready || !myaxi_arvalid) begin
            req_fsm <= req_fsm_1;
          end 
        end
      endcase
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      _data_seq_cond_0_1 <= 0;
    end else begin
      if(_data_seq_cond_0_1) begin
        $display("sum=%d expected_sum=%d", _reduceadd_data_3, 67552);
      end 
      _data_seq_cond_0_1 <= _reduceadd_valid_3 && __variable_valid_4 && (__variable_data_4 == 1);
    end
  end


endmodule
"""


def test():
    veriloggen.reset()
    test_module = types_axi_read_dataflow.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
