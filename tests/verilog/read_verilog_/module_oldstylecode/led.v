module blinkled 
 (
  CLK,
  RST,
  LED
 );

  output [7:0] LED;
  input RST;
  input CLK;

  reg [31:0] count;
  reg [7:0] led_count;

  always @(posedge CLK) begin
    if(RST) begin
      count <= 0;
    end else begin
      if(count == 1023) begin
        count <= 0;
      end else begin
        count <= count + 1;
      end
    end
  end

  always @(posedge CLK) begin
    if(RST) begin
      led_count <= 0;
    end else begin
      if(count == 1023) begin
        led_count <= led_count + 1;
      end
    end
  end

  assign LED = led_count;

endmodule
