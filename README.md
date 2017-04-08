Veriloggen
==============================

[![Build Status](https://travis-ci.org/PyHDI/veriloggen.svg)](https://travis-ci.org/PyHDI/veriloggen)

A library for constructing a Verilog HDL source code in Python

Copyright (C) 2015, Shinya Takamaeda-Yamazaki

E-mail: takamaeda\_at\_ist.hokudai.ac.jp


License
==============================

Apache License 2.0
(http://www.apache.org/licenses/LICENSE-2.0)


Publication
==============================

If you use Veriloggen for your research, please cite our paper:

- Minoru Watanabe, Kentaro Sano, Shinya Takamaeda, Takefumi Miyoshi, and Hironori Nakajo: Japanese High-level Synthesis Tools for FPGA Hardware Acceleration, IEICE Transactions on Communications, Vol. J100-B, No. 1, pp.1-10, January 2017.
[Paper](https://search.ieice.org/bin/summary.php?id=j100-b_1_1)

Or, please cite the project URL:

```
@misc{veriloggen:github,
author = {Shinya Takamaeda-Yamazaki},
title = {Veriloggen: A library for constructing a Verilog HDL source code in Python},
howpublished = {\url{https://github.com/PyHDI/veriloggen}},
}
```


What's Veriloggen?
==============================

Veriloggen is an open-sourced library for constructing a Verilog HDL source code in Python.

Veriloggen is not a behavior synthesis (or high level synthesis). Veriloggen provides a lightweight abstraction of Verilog HDL AST. You can build up a hardware design written in Verilog HDL very easily by using the AST abstraction and the entire functionality of Python.
 
Veriloggen is not designed for designing a hardware by programmer directly, but is for providing an efficient abstraction to develop a more efficient domain specific language and tools.


Installation
==============================

Requirements
--------------------

- Python: 2.7, 3.5 or later

Python3 is recommended.

- Icarus Verilog: 0.9.7 or later (but 10.0 is not recommended)

Install on your platform. For exmple, on Ubuntu:

    sudo apt-get install iverilog

- Jinja2: 2.8 or later

Install on your python environment by using pip:

    pip install jinja2

- Pyverilog: 1.0.7 or later

Install from pip (or download and install from GitHub):

    pip install pyverilog

- IPgen: 0.2.1 or later

Install from pip (or download and install from GitHub):

    pip install ipgen

Options
--------------------

- pytest: 2.8.2 or later
- pytest-pythonpath: 0.7 or later

These softwares are required for running the tests in tests and examples:

    pip install pytest pytest-pythonpath

- Graphviz: 2.38.0 or later
- Pygraphviz: 1.3.1 or later

These softwares are required for graph visualization by lib.dataflow:

    sudo apt-get install graphviz
    pip install pygraphviz

Install
--------------------

Install Veriloggen:

    python setup.py install

On Docker
--------------------

Dockerfile is available, so that you can try Veriloggen on Docker without any installation on your host platform.

```
cd docker
sudo docker build -t user/veriloggen .
sudo docker run --name veriloggen -i -t user/veriloggen /bin/bash
cd veriloggen/examples/led/
make
```


Getting Started
==============================

You can find some examples in 'veriloggen/examples/' and 'veriloggen/tests'.

Let's begin veriloggen by an example. Create a example Python script in Python as below. A blinking LED hardware is modeled in Python.
Open 'hello_led.py' in the root directory.

```python
from __future__ import absolute_import
from __future__ import print_function
import sys
import os
from veriloggen import *


def mkLed():
    m = Module('blinkled')
    width = m.Parameter('WIDTH', 8)
    clk = m.Input('CLK')
    rst = m.Input('RST')
    led = m.OutputReg('LED', width)
    count = m.Reg('count', 32)

    m.Always(Posedge(clk))(
        If(rst)(
            count(0)
        ).Else(
            If(count == 1023)(
                count(0)
            ).Else(
                count(count + 1)
            )
        ))

    m.Always(Posedge(clk))(
        If(rst)(
            led(0)
        ).Else(
            If(count == 1024 - 1)(
                led(led + 1)
            )
        ))

    m.Always(Posedge(clk))(
        If(rst)(
        ).Else(
            Systask('display', "LED:%d count:%d", led, count)
        ))

    return m


def mkTest():
    m = Module('test')

    # target instance
    led = mkLed()

    uut = Submodule(m, led, name='uut')
    clk = uut['CLK']
    rst = uut['RST']

    simulation.setup_waveform(m, uut, m.get_vars())
    simulation.setup_clock(m, clk, hperiod=5)
    init = simulation.setup_reset(m, rst, m.make_reset(), period=100)

    init.add(
        Delay(1000 * 100),
        Systask('finish'),
    )

    return m

if __name__ == '__main__':
    test = mkTest()
    verilog = test.to_verilog(filename='tmp.v')
    #verilog = test.to_verilog()
    print(verilog)

    sim = simulation.Simulator(test)
    rslt = sim.run()
    print(rslt)

    # sim.view_waveform()
```

Run the script.

```
python hello_led.py
```

You will have a complete Verilog HDL source code named 'tmp.v' as below, which is generated by the source code generator.

```verilog
module test #
(
  parameter WIDTH = 8
)
(

);

  reg CLK;
  reg RST;
  wire [WIDTH-1:0] LED;

  blinkled
  #(
    .WIDTH(WIDTH)
  )
  uut
  (
    .CLK(CLK),
    .RST(RST),
    .LED(LED)
  );


  initial begin
    $dumpfile("uut.vcd");
    $dumpvars(0, uut, CLK, RST, LED);
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



module blinkled #
(
  parameter WIDTH = 8
)
(
  input CLK,
  input RST,
  output reg [WIDTH-1:0] LED
);

  reg [32-1:0] count;

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
      LED <= 0;
    end else begin
      if(count == 1023) begin
        LED <= LED + 1;
      end 
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
    end else begin
      $display("LED:%d count:%d", LED, count);
    end
  end


endmodule
```

You will also see the simulation result of the generated Verilog code on Icarus Verilog.

```
VCD info: dumpfile uut.vcd opened for output.
LED:  x count:         x
LED:  x count:         x
LED:  x count:         x
LED:  x count:         x
LED:  x count:         x
LED:  x count:         x
LED:  x count:         x
LED:  x count:         x
LED:  x count:         x
LED:  x count:         x
LED:  0 count:         0
LED:  0 count:         1
LED:  0 count:         2
LED:  0 count:         3
LED:  0 count:         4
...
LED:  9 count:       777
LED:  9 count:       778
LED:  9 count:       779
LED:  9 count:       780
LED:  9 count:       781
LED:  9 count:       782
LED:  9 count:       783
```

If you installed GTKwave and enable 'sim.view_waveform()' in 'hello_led.py', you can see the waveform the simulation result.

![waveform.png](img/waveform.png)


Veriloggen Extension Libraries
==============================

- veriloggen.verilog: Verilog HDL source code synthesis and import APIs
- veriloggen.simulation: Simulation APIs via Verilog simulators
- veriloggen.seq: Synchronous circuit builder (Seq)
- veriloggen.fsm: Finite state machine builder (FSM)
- veriloggen.types: Library of frequently-used structure, such as memory, fixed-point, AXI bus, etc.
- veriloggen.pipeline: Explicit pipeline builder
- veriloggen.dataflow: Dataflow-based stream processing hardware builder
- veriloggen.thread: Tightly-coupled high-level synthesis compiler emedded within Veriloggen HDL


Related Project
==============================

[Pyverilog](https://github.com/PyHDI/Pyverilog)
- Python-based Hardware Design Processing Toolkit for Verilog HDL

[IPgen](https://github.com/PyHDI/ipgen)
- IP-core package generator for AXI4/Avalon
