import bram
from veriloggen import *

expected_verilog = """
module test #
(
  parameter ADDR_WIDTH = 10,
  parameter DATA_WIDTH = 32
);

  reg CLK;
  reg RST;

  TOP
  #(
    .ADDR_WIDTH(ADDR_WIDTH),
    .DATA_WIDTH(DATA_WIDTH)
  )
  uut
  (
    .CLK(CLK),
    .RST(RST)
  );

  initial begin
    CLK = 0;
    forever begin
      #5 CLK = (!CLK);
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

module TOP #
  (
   parameter ADDR_WIDTH = 10, 
   parameter DATA_WIDTH = 32
   )
  (
   input CLK, 
   input RST
   );
  reg [ADDR_WIDTH-1:0] addr;
  reg [DATA_WIDTH-1:0] datain;
  reg [1-1:0] write;
  wire [DATA_WIDTH-1:0] dataout;

  my_bram
    #(
      .ADDR_WIDTH(ADDR_WIDTH),
      .DATA_WIDTH(DATA_WIDTH)
      )
  inst_bram
    (
     .CLK(CLK),
     .addr(addr),
     .datain(datain),
     .write(write),
     .dataout(dataout)
     );
  
  reg [32-1:0] fsm;
  localparam fsm_init = 0;

  reg [32-1:0] _d1_fsm;
  reg _fsm_cond_1_0_1;
  reg [ADDR_WIDTH-1:0] _tmp_0;
  reg [32-1:0] _d2_fsm;
  reg _fsm_cond_2_1_1;
  reg _fsm_cond_2_1_2;

  localparam fsm_1 = 1;
  localparam fsm_2 = 2;
  localparam fsm_3 = 3;

  always @(posedge CLK) begin
    if(RST) begin        
      addr <= 0;        
      datain <= 0;        
      write <= 0;        
      fsm <= fsm_init;
      _d1_fsm <= fsm_init;
      _d2_fsm <= fsm_init;
      _fsm_cond_1_0_1 <= 0;
      _tmp_0 <= 0;
      _fsm_cond_2_1_1 <= 0;
      _fsm_cond_2_1_2 <= 0;
    end else begin
      _d1_fsm <= fsm;
      _d2_fsm <= _d1_fsm;
      case(_d2_fsm)
        fsm_2: begin
          if(_fsm_cond_2_1_2) begin
            $display("addr:%x read : %x", _tmp_0-1, dataout);
          end 
        end
      endcase
      case(_d1_fsm)
        fsm_1: begin
          if(_fsm_cond_1_0_1) begin
            $display("addr:%x write: %x", (addr - 1), datain);
          end 
        end
        fsm_2: begin
          _tmp_0 <= addr;
          _fsm_cond_2_1_2 <= _fsm_cond_2_1_1;
        end
      endcase
      case(fsm)
        fsm_init: begin
          addr <= 0;
          datain <= 0;
          write <= 0;
          datain <= -4;
          fsm <= fsm_1;
        end
        fsm_1: begin
          if(addr < 128) begin
            addr <= addr + 1;
            write <= 1;
            datain <= datain + 4;
          end 
          _fsm_cond_1_0_1 <= (addr < 128);
          if(!(addr < 128)) begin
            addr <= 0;
            datain <= 0;
            write <= 0;
          end 
          if(!(addr < 128)) begin
            fsm <= fsm_2;
          end 
        end
        fsm_2: begin
          if(addr < 128) begin
            addr <= addr + 1;
          end 
          _fsm_cond_2_1_1 <= (addr < 128);
          if(!(addr < 128)) begin
            addr <= 0;
            datain <= 0;
            write <= 0;
          end 
          if(!(addr < 128)) begin
            fsm <= fsm_3;
          end 
        end
      endcase
    end 
  end
  
endmodule

module my_bram #
  (
   parameter ADDR_WIDTH = 10, 
   parameter DATA_WIDTH = 32
   )
  (
   input CLK, 
   input [ADDR_WIDTH-1:0] addr, 
   input [DATA_WIDTH-1:0] datain, 
   input [1-1:0] write, 
   output [DATA_WIDTH-1:0] dataout
   );

  reg [DATA_WIDTH-1:0] d_addr;
  reg [DATA_WIDTH-1:0] mem [0:2**ADDR_WIDTH-1];

  always @(posedge CLK) begin
    if(write) begin        
      mem[addr] <= datain;
    end  
    d_addr <= addr;
  end 

  assign dataout = mem[d_addr];
endmodule
"""

expected_rslt = """\
addr:00000000 write: 00000000
addr:00000001 write: 00000004
addr:00000002 write: 00000008
addr:00000003 write: 0000000c
addr:00000004 write: 00000010
addr:00000005 write: 00000014
addr:00000006 write: 00000018
addr:00000007 write: 0000001c
addr:00000008 write: 00000020
addr:00000009 write: 00000024
addr:0000000a write: 00000028
addr:0000000b write: 0000002c
addr:0000000c write: 00000030
addr:0000000d write: 00000034
addr:0000000e write: 00000038
addr:0000000f write: 0000003c
addr:00000010 write: 00000040
addr:00000011 write: 00000044
addr:00000012 write: 00000048
addr:00000013 write: 0000004c
addr:00000014 write: 00000050
addr:00000015 write: 00000054
addr:00000016 write: 00000058
addr:00000017 write: 0000005c
addr:00000018 write: 00000060
addr:00000019 write: 00000064
addr:0000001a write: 00000068
addr:0000001b write: 0000006c
addr:0000001c write: 00000070
addr:0000001d write: 00000074
addr:0000001e write: 00000078
addr:0000001f write: 0000007c
addr:00000020 write: 00000080
addr:00000021 write: 00000084
addr:00000022 write: 00000088
addr:00000023 write: 0000008c
addr:00000024 write: 00000090
addr:00000025 write: 00000094
addr:00000026 write: 00000098
addr:00000027 write: 0000009c
addr:00000028 write: 000000a0
addr:00000029 write: 000000a4
addr:0000002a write: 000000a8
addr:0000002b write: 000000ac
addr:0000002c write: 000000b0
addr:0000002d write: 000000b4
addr:0000002e write: 000000b8
addr:0000002f write: 000000bc
addr:00000030 write: 000000c0
addr:00000031 write: 000000c4
addr:00000032 write: 000000c8
addr:00000033 write: 000000cc
addr:00000034 write: 000000d0
addr:00000035 write: 000000d4
addr:00000036 write: 000000d8
addr:00000037 write: 000000dc
addr:00000038 write: 000000e0
addr:00000039 write: 000000e4
addr:0000003a write: 000000e8
addr:0000003b write: 000000ec
addr:0000003c write: 000000f0
addr:0000003d write: 000000f4
addr:0000003e write: 000000f8
addr:0000003f write: 000000fc
addr:00000040 write: 00000100
addr:00000041 write: 00000104
addr:00000042 write: 00000108
addr:00000043 write: 0000010c
addr:00000044 write: 00000110
addr:00000045 write: 00000114
addr:00000046 write: 00000118
addr:00000047 write: 0000011c
addr:00000048 write: 00000120
addr:00000049 write: 00000124
addr:0000004a write: 00000128
addr:0000004b write: 0000012c
addr:0000004c write: 00000130
addr:0000004d write: 00000134
addr:0000004e write: 00000138
addr:0000004f write: 0000013c
addr:00000050 write: 00000140
addr:00000051 write: 00000144
addr:00000052 write: 00000148
addr:00000053 write: 0000014c
addr:00000054 write: 00000150
addr:00000055 write: 00000154
addr:00000056 write: 00000158
addr:00000057 write: 0000015c
addr:00000058 write: 00000160
addr:00000059 write: 00000164
addr:0000005a write: 00000168
addr:0000005b write: 0000016c
addr:0000005c write: 00000170
addr:0000005d write: 00000174
addr:0000005e write: 00000178
addr:0000005f write: 0000017c
addr:00000060 write: 00000180
addr:00000061 write: 00000184
addr:00000062 write: 00000188
addr:00000063 write: 0000018c
addr:00000064 write: 00000190
addr:00000065 write: 00000194
addr:00000066 write: 00000198
addr:00000067 write: 0000019c
addr:00000068 write: 000001a0
addr:00000069 write: 000001a4
addr:0000006a write: 000001a8
addr:0000006b write: 000001ac
addr:0000006c write: 000001b0
addr:0000006d write: 000001b4
addr:0000006e write: 000001b8
addr:0000006f write: 000001bc
addr:00000070 write: 000001c0
addr:00000071 write: 000001c4
addr:00000072 write: 000001c8
addr:00000073 write: 000001cc
addr:00000074 write: 000001d0
addr:00000075 write: 000001d4
addr:00000076 write: 000001d8
addr:00000077 write: 000001dc
addr:00000078 write: 000001e0
addr:00000079 write: 000001e4
addr:0000007a write: 000001e8
addr:0000007b write: 000001ec
addr:0000007c write: 000001f0
addr:0000007d write: 000001f4
addr:0000007e write: 000001f8
addr:0000007f write: 000001fc
addr:00000000 read : 00000000
addr:00000001 read : 00000004
addr:00000002 read : 00000008
addr:00000003 read : 0000000c
addr:00000004 read : 00000010
addr:00000005 read : 00000014
addr:00000006 read : 00000018
addr:00000007 read : 0000001c
addr:00000008 read : 00000020
addr:00000009 read : 00000024
addr:0000000a read : 00000028
addr:0000000b read : 0000002c
addr:0000000c read : 00000030
addr:0000000d read : 00000034
addr:0000000e read : 00000038
addr:0000000f read : 0000003c
addr:00000010 read : 00000040
addr:00000011 read : 00000044
addr:00000012 read : 00000048
addr:00000013 read : 0000004c
addr:00000014 read : 00000050
addr:00000015 read : 00000054
addr:00000016 read : 00000058
addr:00000017 read : 0000005c
addr:00000018 read : 00000060
addr:00000019 read : 00000064
addr:0000001a read : 00000068
addr:0000001b read : 0000006c
addr:0000001c read : 00000070
addr:0000001d read : 00000074
addr:0000001e read : 00000078
addr:0000001f read : 0000007c
addr:00000020 read : 00000080
addr:00000021 read : 00000084
addr:00000022 read : 00000088
addr:00000023 read : 0000008c
addr:00000024 read : 00000090
addr:00000025 read : 00000094
addr:00000026 read : 00000098
addr:00000027 read : 0000009c
addr:00000028 read : 000000a0
addr:00000029 read : 000000a4
addr:0000002a read : 000000a8
addr:0000002b read : 000000ac
addr:0000002c read : 000000b0
addr:0000002d read : 000000b4
addr:0000002e read : 000000b8
addr:0000002f read : 000000bc
addr:00000030 read : 000000c0
addr:00000031 read : 000000c4
addr:00000032 read : 000000c8
addr:00000033 read : 000000cc
addr:00000034 read : 000000d0
addr:00000035 read : 000000d4
addr:00000036 read : 000000d8
addr:00000037 read : 000000dc
addr:00000038 read : 000000e0
addr:00000039 read : 000000e4
addr:0000003a read : 000000e8
addr:0000003b read : 000000ec
addr:0000003c read : 000000f0
addr:0000003d read : 000000f4
addr:0000003e read : 000000f8
addr:0000003f read : 000000fc
addr:00000040 read : 00000100
addr:00000041 read : 00000104
addr:00000042 read : 00000108
addr:00000043 read : 0000010c
addr:00000044 read : 00000110
addr:00000045 read : 00000114
addr:00000046 read : 00000118
addr:00000047 read : 0000011c
addr:00000048 read : 00000120
addr:00000049 read : 00000124
addr:0000004a read : 00000128
addr:0000004b read : 0000012c
addr:0000004c read : 00000130
addr:0000004d read : 00000134
addr:0000004e read : 00000138
addr:0000004f read : 0000013c
addr:00000050 read : 00000140
addr:00000051 read : 00000144
addr:00000052 read : 00000148
addr:00000053 read : 0000014c
addr:00000054 read : 00000150
addr:00000055 read : 00000154
addr:00000056 read : 00000158
addr:00000057 read : 0000015c
addr:00000058 read : 00000160
addr:00000059 read : 00000164
addr:0000005a read : 00000168
addr:0000005b read : 0000016c
addr:0000005c read : 00000170
addr:0000005d read : 00000174
addr:0000005e read : 00000178
addr:0000005f read : 0000017c
addr:00000060 read : 00000180
addr:00000061 read : 00000184
addr:00000062 read : 00000188
addr:00000063 read : 0000018c
addr:00000064 read : 00000190
addr:00000065 read : 00000194
addr:00000066 read : 00000198
addr:00000067 read : 0000019c
addr:00000068 read : 000001a0
addr:00000069 read : 000001a4
addr:0000006a read : 000001a8
addr:0000006b read : 000001ac
addr:0000006c read : 000001b0
addr:0000006d read : 000001b4
addr:0000006e read : 000001b8
addr:0000006f read : 000001bc
addr:00000070 read : 000001c0
addr:00000071 read : 000001c4
addr:00000072 read : 000001c8
addr:00000073 read : 000001cc
addr:00000074 read : 000001d0
addr:00000075 read : 000001d4
addr:00000076 read : 000001d8
addr:00000077 read : 000001dc
addr:00000078 read : 000001e0
addr:00000079 read : 000001e4
addr:0000007a read : 000001e8
addr:0000007b read : 000001ec
addr:0000007c read : 000001f0
addr:0000007d read : 000001f4
addr:0000007e read : 000001f8
addr:0000007f read : 000001fc
"""

def test():
    test_module = bram.mkTest()
    test_code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == test_code)

    sim = lib.simulation.Simulator(test_module)
    rslt = sim.run()

    assert(expected_rslt == rslt)
