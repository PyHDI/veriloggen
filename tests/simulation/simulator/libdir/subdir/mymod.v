module mymod
  (
   input CLK,
   input RST,
   output reg [7:0] LED
   );

  reg [24:0] count;

  always @(posedge CLK) begin
    if(RST) begin
      count <= 0;
      LED <= 0;
    end else begin
      count <= count + 1;
      if(count == 1024 - 1) begin
        count <= 0;
        LED <= LED + 1;
      end
    end
  end

endmodule
