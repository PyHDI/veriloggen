

module blinkled
(
  input CLK,
  input RST,
  input [32-1:0] axi_a_tdata,
  input axi_a_tvalid,
  output axi_a_tready,
  input axi_a_tlast,
  output reg [32-1:0] axi_b_tdata,
  output reg axi_b_tvalid,
  input axi_b_tready,
  output reg axi_b_tlast,
  input [32-1:0] saxi_awaddr,
  input [4-1:0] saxi_awcache,
  input [3-1:0] saxi_awprot,
  input saxi_awvalid,
  output saxi_awready,
  input [32-1:0] saxi_wdata,
  input [4-1:0] saxi_wstrb,
  input saxi_wvalid,
  output saxi_wready,
  output [2-1:0] saxi_bresp,
  output reg saxi_bvalid,
  input saxi_bready,
  input [32-1:0] saxi_araddr,
  input [4-1:0] saxi_arcache,
  input [3-1:0] saxi_arprot,
  input saxi_arvalid,
  output saxi_arready,
  output reg [32-1:0] saxi_rdata,
  output [2-1:0] saxi_rresp,
  output reg saxi_rvalid,
  input saxi_rready
);

  wire _axi_a_read_req_fifo_enq;
  wire [105-1:0] _axi_a_read_req_fifo_wdata;
  wire _axi_a_read_req_fifo_full;
  wire _axi_a_read_req_fifo_almost_full;
  wire _axi_a_read_req_fifo_deq;
  wire [105-1:0] _axi_a_read_req_fifo_rdata;
  wire _axi_a_read_req_fifo_empty;
  wire _axi_a_read_req_fifo_almost_empty;
  assign _axi_a_read_req_fifo_enq = 0;
  assign _axi_a_read_req_fifo_wdata = 'hx;
  assign _axi_a_read_req_fifo_deq = 0;

  _axi_a_read_req_fifo
  inst__axi_a_read_req_fifo
  (
    .CLK(CLK),
    .RST(RST),
    ._axi_a_read_req_fifo_enq(_axi_a_read_req_fifo_enq),
    ._axi_a_read_req_fifo_wdata(_axi_a_read_req_fifo_wdata),
    ._axi_a_read_req_fifo_full(_axi_a_read_req_fifo_full),
    ._axi_a_read_req_fifo_almost_full(_axi_a_read_req_fifo_almost_full),
    ._axi_a_read_req_fifo_deq(_axi_a_read_req_fifo_deq),
    ._axi_a_read_req_fifo_rdata(_axi_a_read_req_fifo_rdata),
    ._axi_a_read_req_fifo_empty(_axi_a_read_req_fifo_empty),
    ._axi_a_read_req_fifo_almost_empty(_axi_a_read_req_fifo_almost_empty)
  );

  reg [4-1:0] count__axi_a_read_req_fifo;
  wire [8-1:0] _axi_a_read_op_sel_fifo;
  wire [32-1:0] _axi_a_read_local_addr_fifo;
  wire [32-1:0] _axi_a_read_local_stride_fifo;
  wire [33-1:0] _axi_a_read_local_size_fifo;
  wire [8-1:0] unpack_read_req_op_sel_0;
  wire [32-1:0] unpack_read_req_local_addr_1;
  wire [32-1:0] unpack_read_req_local_stride_2;
  wire [33-1:0] unpack_read_req_local_size_3;
  assign unpack_read_req_op_sel_0 = _axi_a_read_req_fifo_rdata[104:97];
  assign unpack_read_req_local_addr_1 = _axi_a_read_req_fifo_rdata[96:65];
  assign unpack_read_req_local_stride_2 = _axi_a_read_req_fifo_rdata[64:33];
  assign unpack_read_req_local_size_3 = _axi_a_read_req_fifo_rdata[32:0];
  assign _axi_a_read_op_sel_fifo = unpack_read_req_op_sel_0;
  assign _axi_a_read_local_addr_fifo = unpack_read_req_local_addr_1;
  assign _axi_a_read_local_stride_fifo = unpack_read_req_local_stride_2;
  assign _axi_a_read_local_size_fifo = unpack_read_req_local_size_3;
  reg [8-1:0] _axi_a_read_op_sel_buf;
  reg [32-1:0] _axi_a_read_local_addr_buf;
  reg [32-1:0] _axi_a_read_local_stride_buf;
  reg [33-1:0] _axi_a_read_local_size_buf;
  reg _axi_a_read_data_idle;
  wire _axi_a_read_idle;
  assign _axi_a_read_idle = _axi_a_read_req_fifo_empty && _axi_a_read_data_idle;
  wire _axi_b_write_req_fifo_enq;
  wire [105-1:0] _axi_b_write_req_fifo_wdata;
  wire _axi_b_write_req_fifo_full;
  wire _axi_b_write_req_fifo_almost_full;
  wire _axi_b_write_req_fifo_deq;
  wire [105-1:0] _axi_b_write_req_fifo_rdata;
  wire _axi_b_write_req_fifo_empty;
  wire _axi_b_write_req_fifo_almost_empty;
  assign _axi_b_write_req_fifo_enq = 0;
  assign _axi_b_write_req_fifo_wdata = 'hx;
  assign _axi_b_write_req_fifo_deq = 0;

  _axi_b_write_req_fifo
  inst__axi_b_write_req_fifo
  (
    .CLK(CLK),
    .RST(RST),
    ._axi_b_write_req_fifo_enq(_axi_b_write_req_fifo_enq),
    ._axi_b_write_req_fifo_wdata(_axi_b_write_req_fifo_wdata),
    ._axi_b_write_req_fifo_full(_axi_b_write_req_fifo_full),
    ._axi_b_write_req_fifo_almost_full(_axi_b_write_req_fifo_almost_full),
    ._axi_b_write_req_fifo_deq(_axi_b_write_req_fifo_deq),
    ._axi_b_write_req_fifo_rdata(_axi_b_write_req_fifo_rdata),
    ._axi_b_write_req_fifo_empty(_axi_b_write_req_fifo_empty),
    ._axi_b_write_req_fifo_almost_empty(_axi_b_write_req_fifo_almost_empty)
  );

  reg [4-1:0] count__axi_b_write_req_fifo;
  wire [8-1:0] _axi_b_write_op_sel_fifo;
  wire [32-1:0] _axi_b_write_local_addr_fifo;
  wire [32-1:0] _axi_b_write_local_stride_fifo;
  wire [33-1:0] _axi_b_write_size_fifo;
  wire [8-1:0] unpack_write_req_op_sel_4;
  wire [32-1:0] unpack_write_req_local_addr_5;
  wire [32-1:0] unpack_write_req_local_stride_6;
  wire [33-1:0] unpack_write_req_local_size_7;
  assign unpack_write_req_op_sel_4 = _axi_b_write_req_fifo_rdata[104:97];
  assign unpack_write_req_local_addr_5 = _axi_b_write_req_fifo_rdata[96:65];
  assign unpack_write_req_local_stride_6 = _axi_b_write_req_fifo_rdata[64:33];
  assign unpack_write_req_local_size_7 = _axi_b_write_req_fifo_rdata[32:0];
  assign _axi_b_write_op_sel_fifo = unpack_write_req_op_sel_4;
  assign _axi_b_write_local_addr_fifo = unpack_write_req_local_addr_5;
  assign _axi_b_write_local_stride_fifo = unpack_write_req_local_stride_6;
  assign _axi_b_write_size_fifo = unpack_write_req_local_size_7;
  reg [8-1:0] _axi_b_write_op_sel_buf;
  reg [32-1:0] _axi_b_write_local_addr_buf;
  reg [32-1:0] _axi_b_write_local_stride_buf;
  reg [33-1:0] _axi_b_write_size_buf;
  reg _axi_b_write_data_idle;
  wire _axi_b_write_idle;
  assign _axi_b_write_idle = _axi_b_write_req_fifo_empty && _axi_b_write_data_idle;
  assign saxi_bresp = 0;
  assign saxi_rresp = 0;
  reg signed [32-1:0] _saxi_register_0;
  reg signed [32-1:0] _saxi_register_1;
  reg signed [32-1:0] _saxi_register_2;
  reg signed [32-1:0] _saxi_register_3;
  reg _saxi_flag_0;
  reg _saxi_flag_1;
  reg _saxi_flag_2;
  reg _saxi_flag_3;
  reg signed [32-1:0] _saxi_resetval_0;
  reg signed [32-1:0] _saxi_resetval_1;
  reg signed [32-1:0] _saxi_resetval_2;
  reg signed [32-1:0] _saxi_resetval_3;
  localparam _saxi_maskwidth = 2;
  localparam _saxi_mask = { _saxi_maskwidth{ 1'd1 } };
  localparam _saxi_shift = 2;
  reg [32-1:0] _saxi_register_fsm;
  localparam _saxi_register_fsm_init = 0;
  reg [32-1:0] addr_8;
  reg writevalid_9;
  reg readvalid_10;
  reg prev_awvalid_11;
  reg prev_arvalid_12;
  assign saxi_awready = (_saxi_register_fsm == 0) && (!writevalid_9 && !readvalid_10 && !saxi_bvalid && prev_awvalid_11);
  assign saxi_arready = (_saxi_register_fsm == 0) && (!readvalid_10 && !writevalid_9 && prev_arvalid_12 && !prev_awvalid_11);
  reg [_saxi_maskwidth-1:0] axis_maskaddr_13;
  wire signed [32-1:0] axislite_rdata_14;
  assign axislite_rdata_14 = (axis_maskaddr_13 == 0)? _saxi_register_0 : 
                             (axis_maskaddr_13 == 1)? _saxi_register_1 : 
                             (axis_maskaddr_13 == 2)? _saxi_register_2 : 
                             (axis_maskaddr_13 == 3)? _saxi_register_3 : 'hx;
  wire axislite_flag_15;
  assign axislite_flag_15 = (axis_maskaddr_13 == 0)? _saxi_flag_0 : 
                            (axis_maskaddr_13 == 1)? _saxi_flag_1 : 
                            (axis_maskaddr_13 == 2)? _saxi_flag_2 : 
                            (axis_maskaddr_13 == 3)? _saxi_flag_3 : 'hx;
  wire signed [32-1:0] axislite_resetval_16;
  assign axislite_resetval_16 = (axis_maskaddr_13 == 0)? _saxi_resetval_0 : 
                                (axis_maskaddr_13 == 1)? _saxi_resetval_1 : 
                                (axis_maskaddr_13 == 2)? _saxi_resetval_2 : 
                                (axis_maskaddr_13 == 3)? _saxi_resetval_3 : 'hx;
  reg _saxi_cond_0_1;
  assign saxi_wready = _saxi_register_fsm == 2;
  reg [32-1:0] th_comp;
  localparam th_comp_init = 0;
  reg signed [32-1:0] _th_comp_size_0;
  reg signed [32-1:0] _th_comp_i_1;
  reg signed [32-1:0] axistreamin_tdata_17;
  reg axistreamin_tlast_18;
  assign axi_a_tready = th_comp == 8;
  reg signed [32-1:0] _th_comp_a_2;
  reg signed [32-1:0] _th_comp_a_last_3;
  reg signed [32-1:0] _th_comp_b_4;
  reg signed [32-1:0] _th_comp_b_last_5;
  reg _axi_b_cond_0_1;

  always @(posedge CLK) begin
    if(RST) begin
      _axi_a_read_data_idle <= 1;
    end else begin
      if((th_comp == 7) && _axi_a_read_data_idle) begin
        _axi_a_read_data_idle <= 0;
      end 
      if((th_comp == 8) && axi_a_tvalid) begin
        _axi_a_read_data_idle <= 1;
      end 
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      count__axi_a_read_req_fifo <= 0;
    end else begin
      if(_axi_a_read_req_fifo_enq && !_axi_a_read_req_fifo_full && (_axi_a_read_req_fifo_deq && !_axi_a_read_req_fifo_empty)) begin
        count__axi_a_read_req_fifo <= count__axi_a_read_req_fifo;
      end else if(_axi_a_read_req_fifo_enq && !_axi_a_read_req_fifo_full) begin
        count__axi_a_read_req_fifo <= count__axi_a_read_req_fifo + 1;
      end else if(_axi_a_read_req_fifo_deq && !_axi_a_read_req_fifo_empty) begin
        count__axi_a_read_req_fifo <= count__axi_a_read_req_fifo - 1;
      end 
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      _axi_b_write_data_idle <= 1;
      axi_b_tdata <= 0;
      axi_b_tvalid <= 0;
      axi_b_tlast <= 0;
      _axi_b_cond_0_1 <= 0;
    end else begin
      if(_axi_b_cond_0_1) begin
        axi_b_tvalid <= 0;
        axi_b_tlast <= 0;
      end 
      if((th_comp == 12) && _axi_b_write_data_idle) begin
        _axi_b_write_data_idle <= 0;
      end 
      if((th_comp == 13) && (axi_b_tready || !axi_b_tvalid)) begin
        axi_b_tdata <= _th_comp_b_4;
        axi_b_tvalid <= 1;
        axi_b_tlast <= _th_comp_b_last_5;
      end 
      _axi_b_cond_0_1 <= 1;
      if(axi_b_tvalid && !axi_b_tready) begin
        axi_b_tvalid <= axi_b_tvalid;
        axi_b_tlast <= axi_b_tlast;
      end 
      if((th_comp == 13) && (axi_b_tready || !axi_b_tvalid)) begin
        _axi_b_write_data_idle <= 1;
      end 
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      count__axi_b_write_req_fifo <= 0;
    end else begin
      if(_axi_b_write_req_fifo_enq && !_axi_b_write_req_fifo_full && (_axi_b_write_req_fifo_deq && !_axi_b_write_req_fifo_empty)) begin
        count__axi_b_write_req_fifo <= count__axi_b_write_req_fifo;
      end else if(_axi_b_write_req_fifo_enq && !_axi_b_write_req_fifo_full) begin
        count__axi_b_write_req_fifo <= count__axi_b_write_req_fifo + 1;
      end else if(_axi_b_write_req_fifo_deq && !_axi_b_write_req_fifo_empty) begin
        count__axi_b_write_req_fifo <= count__axi_b_write_req_fifo - 1;
      end 
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      saxi_bvalid <= 0;
      prev_awvalid_11 <= 0;
      prev_arvalid_12 <= 0;
      writevalid_9 <= 0;
      readvalid_10 <= 0;
      addr_8 <= 0;
      saxi_rdata <= 0;
      saxi_rvalid <= 0;
      _saxi_cond_0_1 <= 0;
      _saxi_register_0 <= 0;
      _saxi_flag_0 <= 0;
      _saxi_register_1 <= 0;
      _saxi_flag_1 <= 0;
      _saxi_register_2 <= 0;
      _saxi_flag_2 <= 0;
      _saxi_register_3 <= 0;
      _saxi_flag_3 <= 0;
    end else begin
      if(_saxi_cond_0_1) begin
        saxi_rvalid <= 0;
      end 
      if(saxi_bvalid && saxi_bready) begin
        saxi_bvalid <= 0;
      end 
      if(saxi_wvalid && saxi_wready) begin
        saxi_bvalid <= 1;
      end 
      prev_awvalid_11 <= saxi_awvalid;
      prev_arvalid_12 <= saxi_arvalid;
      writevalid_9 <= 0;
      readvalid_10 <= 0;
      if(saxi_awready && saxi_awvalid && !saxi_bvalid) begin
        addr_8 <= saxi_awaddr;
        writevalid_9 <= 1;
      end else if(saxi_arready && saxi_arvalid) begin
        addr_8 <= saxi_araddr;
        readvalid_10 <= 1;
      end 
      if((_saxi_register_fsm == 1) && (saxi_rready || !saxi_rvalid)) begin
        saxi_rdata <= axislite_rdata_14;
        saxi_rvalid <= 1;
      end 
      _saxi_cond_0_1 <= 1;
      if(saxi_rvalid && !saxi_rready) begin
        saxi_rvalid <= saxi_rvalid;
      end 
      if((_saxi_register_fsm == 1) && (saxi_rready || !saxi_rvalid) && axislite_flag_15 && (axis_maskaddr_13 == 0)) begin
        _saxi_register_0 <= axislite_resetval_16;
        _saxi_flag_0 <= 0;
      end 
      if((_saxi_register_fsm == 1) && (saxi_rready || !saxi_rvalid) && axislite_flag_15 && (axis_maskaddr_13 == 1)) begin
        _saxi_register_1 <= axislite_resetval_16;
        _saxi_flag_1 <= 0;
      end 
      if((_saxi_register_fsm == 1) && (saxi_rready || !saxi_rvalid) && axislite_flag_15 && (axis_maskaddr_13 == 2)) begin
        _saxi_register_2 <= axislite_resetval_16;
        _saxi_flag_2 <= 0;
      end 
      if((_saxi_register_fsm == 1) && (saxi_rready || !saxi_rvalid) && axislite_flag_15 && (axis_maskaddr_13 == 3)) begin
        _saxi_register_3 <= axislite_resetval_16;
        _saxi_flag_3 <= 0;
      end 
      if((_saxi_register_fsm == 2) && saxi_wvalid && (axis_maskaddr_13 == 0)) begin
        _saxi_register_0 <= saxi_wdata;
      end 
      if((_saxi_register_fsm == 2) && saxi_wvalid && (axis_maskaddr_13 == 1)) begin
        _saxi_register_1 <= saxi_wdata;
      end 
      if((_saxi_register_fsm == 2) && saxi_wvalid && (axis_maskaddr_13 == 2)) begin
        _saxi_register_2 <= saxi_wdata;
      end 
      if((_saxi_register_fsm == 2) && saxi_wvalid && (axis_maskaddr_13 == 3)) begin
        _saxi_register_3 <= saxi_wdata;
      end 
      if((_saxi_register_0 == 1) && (th_comp == 2) && 1) begin
        _saxi_register_0 <= 0;
      end 
      if((_saxi_register_0 == 1) && (th_comp == 2) && 0) begin
        _saxi_register_1 <= 0;
      end 
      if((_saxi_register_0 == 1) && (th_comp == 2) && 0) begin
        _saxi_register_2 <= 0;
      end 
      if((_saxi_register_0 == 1) && (th_comp == 2) && 0) begin
        _saxi_register_3 <= 0;
      end 
      if((th_comp == 3) && 0) begin
        _saxi_register_0 <= 1;
        _saxi_flag_0 <= 0;
      end 
      if((th_comp == 3) && 1) begin
        _saxi_register_1 <= 1;
        _saxi_flag_1 <= 0;
      end 
      if((th_comp == 3) && 0) begin
        _saxi_register_2 <= 1;
        _saxi_flag_2 <= 0;
      end 
      if((th_comp == 3) && 0) begin
        _saxi_register_3 <= 1;
        _saxi_flag_3 <= 0;
      end 
      if((th_comp == 15) && 0) begin
        _saxi_register_0 <= 0;
        _saxi_flag_0 <= 0;
      end 
      if((th_comp == 15) && 1) begin
        _saxi_register_1 <= 0;
        _saxi_flag_1 <= 0;
      end 
      if((th_comp == 15) && 0) begin
        _saxi_register_2 <= 0;
        _saxi_flag_2 <= 0;
      end 
      if((th_comp == 15) && 0) begin
        _saxi_register_3 <= 0;
        _saxi_flag_3 <= 0;
      end 
    end
  end

  localparam _saxi_register_fsm_1 = 1;
  localparam _saxi_register_fsm_2 = 2;

  always @(posedge CLK) begin
    if(RST) begin
      _saxi_register_fsm <= _saxi_register_fsm_init;
      axis_maskaddr_13 <= 0;
    end else begin
      case(_saxi_register_fsm)
        _saxi_register_fsm_init: begin
          if(readvalid_10 || writevalid_9) begin
            axis_maskaddr_13 <= (addr_8 >> _saxi_shift) & _saxi_mask;
          end 
          if(readvalid_10) begin
            _saxi_register_fsm <= _saxi_register_fsm_1;
          end 
          if(writevalid_9) begin
            _saxi_register_fsm <= _saxi_register_fsm_2;
          end 
        end
        _saxi_register_fsm_1: begin
          if(saxi_rready || !saxi_rvalid) begin
            _saxi_register_fsm <= _saxi_register_fsm_init;
          end 
        end
        _saxi_register_fsm_2: begin
          if(saxi_wvalid) begin
            _saxi_register_fsm <= _saxi_register_fsm_init;
          end 
        end
      endcase
    end
  end

  localparam th_comp_1 = 1;
  localparam th_comp_2 = 2;
  localparam th_comp_3 = 3;
  localparam th_comp_4 = 4;
  localparam th_comp_5 = 5;
  localparam th_comp_6 = 6;
  localparam th_comp_7 = 7;
  localparam th_comp_8 = 8;
  localparam th_comp_9 = 9;
  localparam th_comp_10 = 10;
  localparam th_comp_11 = 11;
  localparam th_comp_12 = 12;
  localparam th_comp_13 = 13;
  localparam th_comp_14 = 14;
  localparam th_comp_15 = 15;
  localparam th_comp_16 = 16;
  localparam th_comp_17 = 17;
  localparam th_comp_18 = 18;

  always @(posedge CLK) begin
    if(RST) begin
      th_comp <= th_comp_init;
      _th_comp_size_0 <= 0;
      _th_comp_i_1 <= 0;
      axistreamin_tdata_17 <= 0;
      axistreamin_tlast_18 <= 0;
      _th_comp_a_2 <= 0;
      _th_comp_a_last_3 <= 0;
      _th_comp_b_4 <= 0;
      _th_comp_b_last_5 <= 0;
    end else begin
      case(th_comp)
        th_comp_init: begin
          th_comp <= th_comp_1;
        end
        th_comp_1: begin
          if(1) begin
            th_comp <= th_comp_2;
          end else begin
            th_comp <= th_comp_17;
          end
        end
        th_comp_2: begin
          if(_saxi_register_0 == 1) begin
            th_comp <= th_comp_3;
          end 
        end
        th_comp_3: begin
          th_comp <= th_comp_4;
        end
        th_comp_4: begin
          _th_comp_size_0 <= _saxi_register_2;
          th_comp <= th_comp_5;
        end
        th_comp_5: begin
          _th_comp_i_1 <= 0;
          th_comp <= th_comp_6;
        end
        th_comp_6: begin
          if(_th_comp_i_1 < _th_comp_size_0) begin
            th_comp <= th_comp_7;
          end else begin
            th_comp <= th_comp_15;
          end
        end
        th_comp_7: begin
          if(_axi_a_read_data_idle) begin
            th_comp <= th_comp_8;
          end 
        end
        th_comp_8: begin
          if(axi_a_tvalid) begin
            axistreamin_tdata_17 <= axi_a_tdata;
          end 
          if(axi_a_tvalid) begin
            axistreamin_tlast_18 <= axi_a_tlast;
          end 
          if(axi_a_tvalid) begin
            th_comp <= th_comp_9;
          end 
        end
        th_comp_9: begin
          _th_comp_a_2 <= axistreamin_tdata_17;
          _th_comp_a_last_3 <= axistreamin_tlast_18;
          th_comp <= th_comp_10;
        end
        th_comp_10: begin
          _th_comp_b_4 <= _th_comp_a_2 + 1;
          th_comp <= th_comp_11;
        end
        th_comp_11: begin
          _th_comp_b_last_5 <= _th_comp_a_last_3;
          th_comp <= th_comp_12;
        end
        th_comp_12: begin
          if(_axi_b_write_data_idle) begin
            th_comp <= th_comp_13;
          end 
        end
        th_comp_13: begin
          if(axi_b_tready || !axi_b_tvalid) begin
            th_comp <= th_comp_14;
          end 
        end
        th_comp_14: begin
          _th_comp_i_1 <= _th_comp_i_1 + 1;
          th_comp <= th_comp_6;
        end
        th_comp_15: begin
          th_comp <= th_comp_16;
        end
        th_comp_16: begin
          th_comp <= th_comp_1;
        end
        th_comp_17: begin
          $finish;
          th_comp <= th_comp_18;
        end
      endcase
    end
  end


endmodule



module _axi_a_read_req_fifo
(
  input CLK,
  input RST,
  input _axi_a_read_req_fifo_enq,
  input [105-1:0] _axi_a_read_req_fifo_wdata,
  output _axi_a_read_req_fifo_full,
  output _axi_a_read_req_fifo_almost_full,
  input _axi_a_read_req_fifo_deq,
  output [105-1:0] _axi_a_read_req_fifo_rdata,
  output _axi_a_read_req_fifo_empty,
  output _axi_a_read_req_fifo_almost_empty
);

  reg [105-1:0] mem [0:8-1];
  reg [3-1:0] head;
  reg [3-1:0] tail;
  wire is_empty;
  wire is_almost_empty;
  wire is_full;
  wire is_almost_full;
  assign is_empty = head == tail;
  assign is_almost_empty = head == (tail + 1 & 7);
  assign is_full = (head + 1 & 7) == tail;
  assign is_almost_full = (head + 2 & 7) == tail;
  wire [105-1:0] rdata;
  assign _axi_a_read_req_fifo_full = is_full;
  assign _axi_a_read_req_fifo_almost_full = is_almost_full || is_full;
  assign _axi_a_read_req_fifo_empty = is_empty;
  assign _axi_a_read_req_fifo_almost_empty = is_almost_empty || is_empty;
  assign rdata = mem[tail];
  assign _axi_a_read_req_fifo_rdata = rdata;

  always @(posedge CLK) begin
    if(RST) begin
      head <= 0;
      tail <= 0;
    end else begin
      if(_axi_a_read_req_fifo_enq && !is_full) begin
        mem[head] <= _axi_a_read_req_fifo_wdata;
        head <= head + 1;
      end 
      if(_axi_a_read_req_fifo_deq && !is_empty) begin
        tail <= tail + 1;
      end 
    end
  end


endmodule



module _axi_b_write_req_fifo
(
  input CLK,
  input RST,
  input _axi_b_write_req_fifo_enq,
  input [105-1:0] _axi_b_write_req_fifo_wdata,
  output _axi_b_write_req_fifo_full,
  output _axi_b_write_req_fifo_almost_full,
  input _axi_b_write_req_fifo_deq,
  output [105-1:0] _axi_b_write_req_fifo_rdata,
  output _axi_b_write_req_fifo_empty,
  output _axi_b_write_req_fifo_almost_empty
);

  reg [105-1:0] mem [0:8-1];
  reg [3-1:0] head;
  reg [3-1:0] tail;
  wire is_empty;
  wire is_almost_empty;
  wire is_full;
  wire is_almost_full;
  assign is_empty = head == tail;
  assign is_almost_empty = head == (tail + 1 & 7);
  assign is_full = (head + 1 & 7) == tail;
  assign is_almost_full = (head + 2 & 7) == tail;
  wire [105-1:0] rdata;
  assign _axi_b_write_req_fifo_full = is_full;
  assign _axi_b_write_req_fifo_almost_full = is_almost_full || is_full;
  assign _axi_b_write_req_fifo_empty = is_empty;
  assign _axi_b_write_req_fifo_almost_empty = is_almost_empty || is_empty;
  assign rdata = mem[tail];
  assign _axi_b_write_req_fifo_rdata = rdata;

  always @(posedge CLK) begin
    if(RST) begin
      head <= 0;
      tail <= 0;
    end else begin
      if(_axi_b_write_req_fifo_enq && !is_full) begin
        mem[head] <= _axi_b_write_req_fifo_wdata;
        head <= head + 1;
      end 
      if(_axi_b_write_req_fifo_deq && !is_empty) begin
        tail <= tail + 1;
      end 
    end
  end


endmodule

