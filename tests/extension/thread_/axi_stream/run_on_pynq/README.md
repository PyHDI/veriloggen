Run on PYNQ
====================

Environment
--------------------

- Design tool: Vivado 2021.2
- FPGA board: Ultra96-V2
- Framework: PYNQ v2.5 for Ultra96-V2 (https://github.com/Avnet/Ultra96-PYNQ/releases/tag/v2.5.0, http://avnet.me/ultra96v2-pynq-image-v2.5)

To run
--------------------

Copy `run_on_pynq.ipynb`, `axi_stream.bit`, and `axi_stream.hwh` to the PYNQ environment via Jupyter notebook. Run then `run_on_pynq.ipynb`.


To synthesize
--------------------

Use `axi_stream.v` and `design_1.tcl`.

Note that the reset polarity of `RST` of `axi_stream.v` is recognized as `ACTIVE_LOW` when it is imported into the block design in Vivado.
Please change the the reset polarity to `ACTIVE_HIGH` in the block pin property setting.
