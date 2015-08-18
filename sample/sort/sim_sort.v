
module test;
  initial begin
    $dumpfile("uut.vcd");
    $dumpvars(0, uut);
  end

  parameter WIDTH = 32;
  
  reg CLK;
  reg RST;
  reg [(WIDTH - 1):0] input_0;
  reg [(WIDTH - 1):0] input_1;
  reg [(WIDTH - 1):0] input_2;
  reg [(WIDTH - 1):0] input_3;
  wire [(WIDTH - 1):0] output_0;
  wire [(WIDTH - 1):0] output_1;
  wire [(WIDTH - 1):0] output_2;
  wire [(WIDTH - 1):0] output_3;
  reg kick;
  wire busy;
      
  sort uut(
           CLK,
           RST,
           input_0,
           input_1,
           input_2,
           input_3,
           output_0,
           output_1,
           output_2,
           output_3,
           kick,
           busy
           );

  initial begin
    CLK = 0;
    forever #5 CLK = ~CLK;
  end

  initial begin
    RST = 0;
    kick = 0;
    input_0 = 4;
    input_1 = 3;
    input_2 = 2;
    input_3 = 1;
    #100;
    RST = 1;
    #100;
    RST = 0;
    
    @(posedge CLK);
    #1;
    
    @(posedge CLK);
    #1;
    
    @(posedge CLK);
    #1;

    kick = 1;

    @(posedge CLK);
    #1;

    kick = 0;

    #500;
    $finish;
  end
  
endmodule
