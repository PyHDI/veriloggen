Run on PYNQ
====================

Environment
--------------------

- Design tool: Vivado 2021.2
- FPGA board: Ultra96-V2
- Framework: PYNQ v2.5 for Ultra96-V2 (https://github.com/Avnet/Ultra96-PYNQ/releases/tag/v2.5.0, http://avnet.me/ultra96v2-pynq-image-v2.5)

To run
--------------------

Copy `run_on_pynq.ipynb`, `stream_axi_stream_fifo_ipxact.bit`, and `stream_axi_stream_fifo_ipxact.hwh` to the PYNQ environment via Jupyter notebook. Run then `run_on_pynq.ipynb`.


To synthesize
--------------------

Use `blinkled_v1_0` and `design_1.tcl`.
Import `blinkled_v1_0` into the IP repository, and create a module in the block design.
