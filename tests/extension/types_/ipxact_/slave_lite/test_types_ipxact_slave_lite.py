from __future__ import absolute_import
from __future__ import print_function

import veriloggen
import types_ipxact_slave_lite

expected_verilog = """
module test;

  reg CLK;
  reg RST;
  wire [32-1:0] LED;
  reg [32-1:0] myaxi_awaddr;
  reg [4-1:0] myaxi_awcache;
  reg [3-1:0] myaxi_awprot;
  reg myaxi_awvalid;
  wire myaxi_awready;
  reg [32-1:0] myaxi_wdata;
  reg [4-1:0] myaxi_wstrb;
  reg myaxi_wvalid;
  wire myaxi_wready;
  wire [2-1:0] myaxi_bresp;
  wire myaxi_bvalid;
  reg myaxi_bready;
  reg [32-1:0] myaxi_araddr;
  reg [4-1:0] myaxi_arcache;
  reg [3-1:0] myaxi_arprot;
  reg myaxi_arvalid;
  wire myaxi_arready;
  wire [32-1:0] myaxi_rdata;
  wire [2-1:0] myaxi_rresp;
  wire myaxi_rvalid;
  reg myaxi_rready;
  reg [32-1:0] _axi_awaddr;
  wire [4-1:0] _axi_awcache;
  wire [3-1:0] _axi_awprot;
  reg _axi_awvalid;
  wire _axi_awready;
  assign _axi_awcache = 3;
  assign _axi_awprot = 0;
  wire [32-1:0] _axi_wdata;
  wire [4-1:0] _axi_wstrb;
  wire _axi_wvalid;
  wire _axi_wready;
  reg [32-1:0] __axi_wdata_sb_0;
  reg [4-1:0] __axi_wstrb_sb_0;
  reg __axi_wvalid_sb_0;
  wire __axi_wready_sb_0;
  wire [4-1:0] _sb__axi_writedata_s_value_0;
  assign _sb__axi_writedata_s_value_0 = __axi_wstrb_sb_0;
  wire [32-1:0] _sb__axi_writedata_s_value_1;
  assign _sb__axi_writedata_s_value_1 = __axi_wdata_sb_0;
  wire [36-1:0] _sb__axi_writedata_s_data_2;
  assign _sb__axi_writedata_s_data_2 = { _sb__axi_writedata_s_value_0, _sb__axi_writedata_s_value_1 };
  wire _sb__axi_writedata_s_valid_3;
  assign _sb__axi_writedata_s_valid_3 = __axi_wvalid_sb_0;
  wire _sb__axi_writedata_m_ready_4;
  assign _sb__axi_writedata_m_ready_4 = _axi_wready;
  reg [36-1:0] _sb__axi_writedata_data_5;
  reg _sb__axi_writedata_valid_6;
  wire _sb__axi_writedata_ready_7;
  reg [36-1:0] _sb__axi_writedata_tmp_data_8;
  reg _sb__axi_writedata_tmp_valid_9;
  wire [36-1:0] _sb__axi_writedata_next_data_10;
  wire _sb__axi_writedata_next_valid_11;
  assign _sb__axi_writedata_ready_7 = !_sb__axi_writedata_tmp_valid_9;
  assign _sb__axi_writedata_next_data_10 = (_sb__axi_writedata_tmp_valid_9)? _sb__axi_writedata_tmp_data_8 : _sb__axi_writedata_s_data_2;
  assign _sb__axi_writedata_next_valid_11 = _sb__axi_writedata_tmp_valid_9 || _sb__axi_writedata_s_valid_3;
  wire [4-1:0] _sb__axi_writedata_m_value_12;
  assign _sb__axi_writedata_m_value_12 = _sb__axi_writedata_data_5[35:32];
  wire [32-1:0] _sb__axi_writedata_m_value_13;
  assign _sb__axi_writedata_m_value_13 = _sb__axi_writedata_data_5[31:0];
  assign __axi_wready_sb_0 = _sb__axi_writedata_ready_7;
  assign _axi_wdata = _sb__axi_writedata_m_value_13;
  assign _axi_wstrb = _sb__axi_writedata_m_value_12;
  assign _axi_wvalid = _sb__axi_writedata_valid_6;
  wire [2-1:0] _axi_bresp;
  wire _axi_bvalid;
  wire _axi_bready;
  assign _axi_bready = 1;
  reg [32-1:0] _axi_araddr;
  wire [4-1:0] _axi_arcache;
  wire [3-1:0] _axi_arprot;
  reg _axi_arvalid;
  wire _axi_arready;
  assign _axi_arcache = 3;
  assign _axi_arprot = 0;
  wire [32-1:0] _axi_rdata;
  wire [2-1:0] _axi_rresp;
  wire _axi_rvalid;
  wire _axi_rready;
  wire [32-1:0] __axi_rdata_sb_0;
  wire __axi_rvalid_sb_0;
  wire __axi_rready_sb_0;
  wire [32-1:0] _sb__axi_readdata_s_value_14;
  assign _sb__axi_readdata_s_value_14 = _axi_rdata;
  wire [32-1:0] _sb__axi_readdata_s_data_15;
  assign _sb__axi_readdata_s_data_15 = { _sb__axi_readdata_s_value_14 };
  wire _sb__axi_readdata_s_valid_16;
  assign _sb__axi_readdata_s_valid_16 = _axi_rvalid;
  wire _sb__axi_readdata_m_ready_17;
  assign _sb__axi_readdata_m_ready_17 = __axi_rready_sb_0;
  reg [32-1:0] _sb__axi_readdata_data_18;
  reg _sb__axi_readdata_valid_19;
  wire _sb__axi_readdata_ready_20;
  reg [32-1:0] _sb__axi_readdata_tmp_data_21;
  reg _sb__axi_readdata_tmp_valid_22;
  wire [32-1:0] _sb__axi_readdata_next_data_23;
  wire _sb__axi_readdata_next_valid_24;
  assign _sb__axi_readdata_ready_20 = !_sb__axi_readdata_tmp_valid_22;
  assign _sb__axi_readdata_next_data_23 = (_sb__axi_readdata_tmp_valid_22)? _sb__axi_readdata_tmp_data_21 : _sb__axi_readdata_s_data_15;
  assign _sb__axi_readdata_next_valid_24 = _sb__axi_readdata_tmp_valid_22 || _sb__axi_readdata_s_valid_16;
  wire [32-1:0] _sb__axi_readdata_m_value_25;
  assign _sb__axi_readdata_m_value_25 = _sb__axi_readdata_data_18[31:0];
  assign __axi_rdata_sb_0 = _sb__axi_readdata_m_value_25;
  assign __axi_rvalid_sb_0 = _sb__axi_readdata_valid_19;
  assign _axi_rready = _sb__axi_readdata_ready_20;
  reg [3-1:0] __axi_outstanding_wcount;
  wire __axi_has_outstanding_write;
  assign __axi_has_outstanding_write = (__axi_outstanding_wcount > 0) || _axi_awvalid;
  wire [32-1:0] _tmp_26;
  assign _tmp_26 = _axi_awaddr;

  always @(*) begin
    myaxi_awaddr = _tmp_26;
  end

  wire [4-1:0] _tmp_27;
  assign _tmp_27 = _axi_awcache;

  always @(*) begin
    myaxi_awcache = _tmp_27;
  end

  wire [3-1:0] _tmp_28;
  assign _tmp_28 = _axi_awprot;

  always @(*) begin
    myaxi_awprot = _tmp_28;
  end

  wire _tmp_29;
  assign _tmp_29 = _axi_awvalid;

  always @(*) begin
    myaxi_awvalid = _tmp_29;
  end

  assign _axi_awready = myaxi_awready;
  wire [32-1:0] _tmp_30;
  assign _tmp_30 = _axi_wdata;

  always @(*) begin
    myaxi_wdata = _tmp_30;
  end

  wire [4-1:0] _tmp_31;
  assign _tmp_31 = _axi_wstrb;

  always @(*) begin
    myaxi_wstrb = _tmp_31;
  end

  wire _tmp_32;
  assign _tmp_32 = _axi_wvalid;

  always @(*) begin
    myaxi_wvalid = _tmp_32;
  end

  assign _axi_wready = myaxi_wready;
  assign _axi_bresp = myaxi_bresp;
  assign _axi_bvalid = myaxi_bvalid;
  wire _tmp_33;
  assign _tmp_33 = _axi_bready;

  always @(*) begin
    myaxi_bready = _tmp_33;
  end

  wire [32-1:0] _tmp_34;
  assign _tmp_34 = _axi_araddr;

  always @(*) begin
    myaxi_araddr = _tmp_34;
  end

  wire [4-1:0] _tmp_35;
  assign _tmp_35 = _axi_arcache;

  always @(*) begin
    myaxi_arcache = _tmp_35;
  end

  wire [3-1:0] _tmp_36;
  assign _tmp_36 = _axi_arprot;

  always @(*) begin
    myaxi_arprot = _tmp_36;
  end

  wire _tmp_37;
  assign _tmp_37 = _axi_arvalid;

  always @(*) begin
    myaxi_arvalid = _tmp_37;
  end

  assign _axi_arready = myaxi_arready;
  assign _axi_rdata = myaxi_rdata;
  assign _axi_rresp = myaxi_rresp;
  assign _axi_rvalid = myaxi_rvalid;
  wire _tmp_38;
  assign _tmp_38 = _axi_rready;

  always @(*) begin
    myaxi_rready = _tmp_38;
  end

  reg [32-1:0] fsm;
  localparam fsm_init = 0;
  reg __axi_raddr_cond_0_1;
  reg [32-1:0] sum;
  reg __axi_raddr_cond_1_1;
  assign __axi_rready_sb_0 = (fsm == 1) || (fsm == 3);

  main
  uut
  (
    .CLK(CLK),
    .RST(RST),
    .LED(LED),
    .myaxi_awaddr(myaxi_awaddr),
    .myaxi_awcache(myaxi_awcache),
    .myaxi_awprot(myaxi_awprot),
    .myaxi_awvalid(myaxi_awvalid),
    .myaxi_awready(myaxi_awready),
    .myaxi_wdata(myaxi_wdata),
    .myaxi_wstrb(myaxi_wstrb),
    .myaxi_wvalid(myaxi_wvalid),
    .myaxi_wready(myaxi_wready),
    .myaxi_bresp(myaxi_bresp),
    .myaxi_bvalid(myaxi_bvalid),
    .myaxi_bready(myaxi_bready),
    .myaxi_araddr(myaxi_araddr),
    .myaxi_arcache(myaxi_arcache),
    .myaxi_arprot(myaxi_arprot),
    .myaxi_arvalid(myaxi_arvalid),
    .myaxi_arready(myaxi_arready),
    .myaxi_rdata(myaxi_rdata),
    .myaxi_rresp(myaxi_rresp),
    .myaxi_rvalid(myaxi_rvalid),
    .myaxi_rready(myaxi_rready)
  );


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
    __axi_wdata_sb_0 = 0;
    __axi_wstrb_sb_0 = 0;
    __axi_wvalid_sb_0 = 0;
    _sb__axi_writedata_data_5 = 0;
    _sb__axi_writedata_valid_6 = 0;
    _sb__axi_writedata_tmp_data_8 = 0;
    _sb__axi_writedata_tmp_valid_9 = 0;
    _axi_araddr = 0;
    _axi_arvalid = 0;
    _sb__axi_readdata_data_18 = 0;
    _sb__axi_readdata_valid_19 = 0;
    _sb__axi_readdata_tmp_data_21 = 0;
    _sb__axi_readdata_tmp_valid_22 = 0;
    __axi_outstanding_wcount = 0;
    fsm = fsm_init;
    __axi_raddr_cond_0_1 = 0;
    sum = 0;
    __axi_raddr_cond_1_1 = 0;
    #100;
    RST = 1;
    #100;
    RST = 0;
    #100000;
    $finish;
  end


  always @(posedge CLK) begin
    if(RST) begin
      _axi_awaddr <= 0;
      _axi_awvalid <= 0;
    end else begin
      _axi_awaddr <= 0;
      _axi_awvalid <= 0;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      __axi_wdata_sb_0 <= 0;
      __axi_wstrb_sb_0 <= 0;
      __axi_wvalid_sb_0 <= 0;
    end else begin
      __axi_wdata_sb_0 <= 0;
      __axi_wstrb_sb_0 <= 0;
      __axi_wvalid_sb_0 <= 0;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      _sb__axi_writedata_data_5 <= 0;
      _sb__axi_writedata_valid_6 <= 0;
      _sb__axi_writedata_tmp_data_8 <= 0;
      _sb__axi_writedata_tmp_valid_9 <= 0;
    end else begin
      if(_sb__axi_writedata_m_ready_4 || !_sb__axi_writedata_valid_6) begin
        _sb__axi_writedata_data_5 <= _sb__axi_writedata_next_data_10;
        _sb__axi_writedata_valid_6 <= _sb__axi_writedata_next_valid_11;
      end 
      if(!_sb__axi_writedata_tmp_valid_9 && _sb__axi_writedata_valid_6 && !_sb__axi_writedata_m_ready_4) begin
        _sb__axi_writedata_tmp_data_8 <= _sb__axi_writedata_s_data_2;
        _sb__axi_writedata_tmp_valid_9 <= _sb__axi_writedata_s_valid_3;
      end 
      if(_sb__axi_writedata_tmp_valid_9 && _sb__axi_writedata_m_ready_4) begin
        _sb__axi_writedata_tmp_valid_9 <= 0;
      end 
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      _axi_araddr <= 0;
      _axi_arvalid <= 0;
      __axi_raddr_cond_0_1 <= 0;
      __axi_raddr_cond_1_1 <= 0;
    end else begin
      if(__axi_raddr_cond_0_1) begin
        _axi_arvalid <= 0;
      end 
      if(__axi_raddr_cond_1_1) begin
        _axi_arvalid <= 0;
      end 
      if((fsm == 0) && (_axi_arready || !_axi_arvalid)) begin
        _axi_araddr <= 1024;
        _axi_arvalid <= 1;
      end 
      __axi_raddr_cond_0_1 <= 1;
      if(_axi_arvalid && !_axi_arready) begin
        _axi_arvalid <= _axi_arvalid;
      end 
      if((fsm == 2) && (_axi_arready || !_axi_arvalid)) begin
        _axi_araddr <= 2048;
        _axi_arvalid <= 1;
      end 
      __axi_raddr_cond_1_1 <= 1;
      if(_axi_arvalid && !_axi_arready) begin
        _axi_arvalid <= _axi_arvalid;
      end 
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      _sb__axi_readdata_data_18 <= 0;
      _sb__axi_readdata_valid_19 <= 0;
      _sb__axi_readdata_tmp_data_21 <= 0;
      _sb__axi_readdata_tmp_valid_22 <= 0;
    end else begin
      if(_sb__axi_readdata_m_ready_17 || !_sb__axi_readdata_valid_19) begin
        _sb__axi_readdata_data_18 <= _sb__axi_readdata_next_data_23;
        _sb__axi_readdata_valid_19 <= _sb__axi_readdata_next_valid_24;
      end 
      if(!_sb__axi_readdata_tmp_valid_22 && _sb__axi_readdata_valid_19 && !_sb__axi_readdata_m_ready_17) begin
        _sb__axi_readdata_tmp_data_21 <= _sb__axi_readdata_s_data_15;
        _sb__axi_readdata_tmp_valid_22 <= _sb__axi_readdata_s_valid_16;
      end 
      if(_sb__axi_readdata_tmp_valid_22 && _sb__axi_readdata_m_ready_17) begin
        _sb__axi_readdata_tmp_valid_22 <= 0;
      end 
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      __axi_outstanding_wcount <= 0;
    end else begin
      if(_axi_awvalid && _axi_awready && !(_axi_bvalid && _axi_bready) && (__axi_outstanding_wcount < 7)) begin
        __axi_outstanding_wcount <= __axi_outstanding_wcount + 1;
      end 
      if(!(_axi_awvalid && _axi_awready) && (_axi_bvalid && _axi_bready) && (__axi_outstanding_wcount > 0)) begin
        __axi_outstanding_wcount <= __axi_outstanding_wcount - 1;
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
      sum <= 0;
    end else begin
      case(fsm)
        fsm_init: begin
          if(_axi_arready || !_axi_arvalid) begin
            fsm <= fsm_1;
          end 
        end
        fsm_1: begin
          if(__axi_rready_sb_0 && __axi_rvalid_sb_0) begin
            sum <= sum + __axi_rdata_sb_0;
          end 
          if(__axi_rready_sb_0 && __axi_rvalid_sb_0) begin
            fsm <= fsm_2;
          end 
        end
        fsm_2: begin
          if(_axi_arready || !_axi_arvalid) begin
            fsm <= fsm_3;
          end 
        end
        fsm_3: begin
          if(__axi_rready_sb_0 && __axi_rvalid_sb_0) begin
            sum <= sum + __axi_rdata_sb_0;
          end 
          if(__axi_rready_sb_0 && __axi_rvalid_sb_0) begin
            fsm <= fsm_4;
          end 
        end
        fsm_4: begin
          $display("sum=%d expected_sum=%d", sum, 768);
          if(sum == 768) begin
            $display("# verify: PASSED");
          end else begin
            $display("# verify: FAILED");
          end
          fsm <= fsm_5;
        end
      endcase
    end
  end


endmodule



module main
(
  input CLK,
  input RST,
  output [32-1:0] LED,
  input [32-1:0] myaxi_awaddr,
  input [4-1:0] myaxi_awcache,
  input [3-1:0] myaxi_awprot,
  input myaxi_awvalid,
  output myaxi_awready,
  input [32-1:0] myaxi_wdata,
  input [4-1:0] myaxi_wstrb,
  input myaxi_wvalid,
  output myaxi_wready,
  output [2-1:0] myaxi_bresp,
  output reg myaxi_bvalid,
  input myaxi_bready,
  input [32-1:0] myaxi_araddr,
  input [4-1:0] myaxi_arcache,
  input [3-1:0] myaxi_arprot,
  input myaxi_arvalid,
  output myaxi_arready,
  output reg [32-1:0] myaxi_rdata,
  output [2-1:0] myaxi_rresp,
  output reg myaxi_rvalid,
  input myaxi_rready
);

  assign myaxi_bresp = 0;
  assign myaxi_rresp = 0;
  assign myaxi_awready = 0;
  assign myaxi_wready = 0;
  reg [32-1:0] fsm;
  localparam fsm_init = 0;
  reg [32-1:0] addr_0;
  reg valid_1;
  reg prev_arvalid_2;
  assign myaxi_arready = (fsm == 0) && !valid_1 && prev_arvalid_2;
  reg [32-1:0] rdata;
  reg _myaxi_rdata_cond_0_1;

  always @(posedge CLK) begin
    if(RST) begin
      myaxi_rdata <= 0;
      myaxi_rvalid <= 0;
      _myaxi_rdata_cond_0_1 <= 0;
    end else begin
      if(_myaxi_rdata_cond_0_1) begin
        myaxi_rvalid <= 0;
      end 
      if((fsm == 1) && (myaxi_rready || !myaxi_rvalid)) begin
        myaxi_rdata <= rdata;
        myaxi_rvalid <= 1;
      end 
      _myaxi_rdata_cond_0_1 <= 1;
      if(myaxi_rvalid && !myaxi_rready) begin
        myaxi_rvalid <= myaxi_rvalid;
      end 
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      myaxi_bvalid <= 0;
      prev_arvalid_2 <= 0;
      valid_1 <= 0;
      addr_0 <= 0;
    end else begin
      if(myaxi_bvalid && myaxi_bready) begin
        myaxi_bvalid <= 0;
      end 
      if(myaxi_wvalid && myaxi_wready) begin
        myaxi_bvalid <= 1;
      end 
      prev_arvalid_2 <= myaxi_arvalid;
      valid_1 <= 0;
      if(myaxi_arready && myaxi_arvalid) begin
        addr_0 <= myaxi_araddr;
        valid_1 <= 1;
      end 
    end
  end

  localparam fsm_1 = 1;
  localparam fsm_2 = 2;

  always @(posedge CLK) begin
    if(RST) begin
      fsm <= fsm_init;
      rdata <= 0;
    end else begin
      case(fsm)
        fsm_init: begin
          if(valid_1) begin
            rdata <= addr_0 >> 2;
          end 
          if(valid_1) begin
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
      endcase
    end
  end


endmodule
"""


def test():
    veriloggen.reset()
    test_module = types_ipxact_slave_lite.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
