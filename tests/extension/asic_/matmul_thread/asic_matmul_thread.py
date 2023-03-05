from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from typing import Literal


# --- to run without installation ---

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))

# --- to run without installation ---


import numpy as np

from veriloggen import *
from veriloggen.asic import ASICSRAM, make_arr, asic_sim, generate_configs
from veriloggen import thread as vthread
from veriloggen.thread.uart import UartRx, UartTx


rand_seed = 123
rand_range = (-16, 16)


def make_uut(
    pdk: Literal['sky130', 'gf180mcu'],
    matrix_size: int,
    baudrate: int,
    clockfreq: int,
) -> Module:
    m = Module('asic_matmul_thread')
    clk = m.Input('clk')
    rst = m.Input('rst')
    rxd = m.Input('rxd')
    txd = m.Output('txd')

    uart_rx = UartRx(m, 'uart_rx', 'rx_', clk, rst, rxd,
                     baudrate=baudrate, clockfreq=clockfreq)
    uart_tx = UartTx(m, 'uart_tx', 'tx_', clk, rst, txd,
                     baudrate=baudrate, clockfreq=clockfreq)

    addrwidth = (matrix_size*matrix_size - 1).bit_length()
    ram_a = ASICSRAM(m, 'ram_a', clk, rst, 32, addrwidth, pdk=pdk)
    ram_b = ASICSRAM(m, 'ram_b', clk, rst, 32, addrwidth, pdk=pdk)

    def comp():
        while True:
            data = 0  # only to avoid undefined variable error

            # receive matrix A
            for idx in range(matrix_size * matrix_size):
                # big endian
                data[24:32] = uart_rx.recv()
                data[16:24] = uart_rx.recv()
                data[8:16] = uart_rx.recv()
                data[0:8] = uart_rx.recv()
                ram_a.write(idx, data)

            # receive matrix B
            for idx in range(matrix_size * matrix_size):
                # big endian
                data[24:32] = uart_rx.recv()
                data[16:24] = uart_rx.recv()
                data[8:16] = uart_rx.recv()
                data[0:8] = uart_rx.recv()
                ram_b.write(idx, data)

            # multiply matrix A and B, transmitting matrix C
            a_idx = 0
            for i in range(matrix_size):
                b_idx = 0
                for j in range(matrix_size):
                    # calculate inner product
                    w = 0
                    for k in range(matrix_size):
                        x = ram_a.read(a_idx + k)
                        y = ram_b.read(b_idx + k)
                        z = x * y
                        w += z

                    # transmit matrix C
                    # big endian
                    uart_tx.send(w[24:32])
                    uart_tx.send(w[16:24])
                    uart_tx.send(w[8:16])
                    uart_tx.send(w[0:8])

                    b_idx += matrix_size
                a_idx += matrix_size

    thd = vthread.Thread(m, 'thd', clk, rst, comp, datawidth=32)
    thd.start()

    return m


def make_tb(
    pdk: Literal['sky130', 'gf180mcu'],
    matrix_size: int,
    baudrate: int,
    clockfreq: int,
):
    m = Module('tb')

    uut = Submodule(m, make_uut(pdk, matrix_size, baudrate, clockfreq),
                    'uut', as_wire=('rxd', 'txd'))
    clk = uut['clk']
    rst = uut['rst']
    rxd = uut['rxd']
    txd = uut['txd']

    uart_rx = UartRx(m, 'uart_rx', 'rx_', clk, rst, txd,
                     baudrate=baudrate, clockfreq=clockfreq)
    uart_tx = UartTx(m, 'uart_tx', 'tx_', clk, rst, rxd,
                     baudrate=baudrate, clockfreq=clockfreq)

    clockperiod = 1_000_000_000 / clockfreq  # in nanoseconds
    simulation.setup_clock(m, clk, hperiod=clockperiod / 2)
    init = simulation.setup_reset(m, rst, m.make_reset(),
                                  period=clockperiod * 10)

    init.add(
        Delay(10_000_000_000),
        Finish()
    )

    rng = np.random.default_rng(rand_seed)
    mat_a = rng.integers(*rand_range, (matrix_size, matrix_size), endpoint=True)
    mat_b = rng.integers(*rand_range, (matrix_size, matrix_size), endpoint=True)
    mat_c = mat_a @ mat_b

    a = make_arr(m, 'a', mat_a.ravel())
    b = make_arr(m, 'b', mat_b.T.ravel())
    c = make_arr(m, 'c', mat_c.ravel())

    def test():
        ok = True

        # transmit matrix A
        for i in range(matrix_size * matrix_size):
            data = a[i]
            uart_tx.send(data[24:32])
            uart_tx.send(data[16:24])
            uart_tx.send(data[8:16])
            uart_tx.send(data[0:8])

        # transmit matrix B
        for i in range(matrix_size * matrix_size):
            data = b[i]
            uart_tx.send(data[24:32])
            uart_tx.send(data[16:24])
            uart_tx.send(data[8:16])
            uart_tx.send(data[0:8])

        # receive matrix C and check it
        for i in range(matrix_size * matrix_size):
            data[24:32] = uart_rx.recv()
            data[16:24] = uart_rx.recv()
            data[8:16] = uart_rx.recv()
            data[0:8] = uart_rx.recv()
            if data != c[i]:
                ok = False

        if ok:
            print('# verify: PASSED')
        else:
            print('# verify: FAILED')

        vthread.finish()

    thd = vthread.Thread(m, 'thd', clk, rst, test, datawidth=32)
    thd.start()

    return m


def run(
    pdk: Literal['sky130', 'gf180mcu'],
    simulation_model_path: list[str],
    matrix_size: int,
    baudrate: int,
    clockfreq: int,
) -> str:
    """
    Simulate.
    Used for testing (through `pytest`).
    """
    tb = make_tb(pdk, matrix_size, baudrate, clockfreq)
    rslt = asic_sim(tb, macro_model_path=simulation_model_path)
    return rslt


def sim(
    pdk: Literal['sky130', 'gf180mcu'],
    pdk_root: str,
    matrix_size: int,
    baudrate: int,
    clockfreq: int,
) -> str:
    """
    Simulate.
    Used for standalone execution (`if __name__ == '__main__':`).
    """
    tb = make_tb(pdk, matrix_size, baudrate, clockfreq)
    rslt = asic_sim(tb, pdk, pdk_root)
    return rslt


def syn(
    pdk: Literal['sky130', 'gf180mcu'],
    pdk_root: str,
    matrix_size: int,
    baudrate: int,
    clockfreq: int,
    die_shape: tuple[int | float, int | float],
):
    """
    Generate an HDL file and configuration files.
    Used for standalone execution (`if __name__ == '__main__':`).
    """
    clockperiod = 1_000_000_000 / clockfreq
    uut = make_uut(pdk, matrix_size, baudrate, clockfreq)
    uut.to_verilog('asic_matmul_thread.v')
    generate_configs('asic_matmul_thread.v', 'asic_matmul_thread', 'clk',
                     clockperiod, die_shape, pdk, pdk_root)


if __name__ == '__main__':
    pdk = 'sky130'  # sky130 or gf180mcu
    pdk_root = '/Users/mu/research/google/OpenLane/pdks'  # change this path
    matrix_size = 15
    baudrate = 20_000_000
    clockfreq = 200_000_000
    die_shape = (1000, 1000)

    syn(pdk, pdk_root, matrix_size, baudrate, clockfreq, die_shape)
    rslt = sim(pdk, pdk_root, matrix_size, baudrate, clockfreq)
    print(rslt)
