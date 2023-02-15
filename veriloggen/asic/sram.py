from typing import Literal
from functools import partial
from veriloggen.core.module import Module
from veriloggen.core import vtypes
from veriloggen.seq.seq import Seq, make_condition
from veriloggen.types import util
from veriloggen.thread.ram import RAM


def zero(width: int):
    if width <= 0:
        raise ValueError
    return vtypes.Int(0, width)


def pad(data, width):
    if data.get_width() > width:
        raise ValueError
    if data.get_width() == width:
        return data
    else:
        return vtypes.Cat(vtypes.Int(0, width - data.get_width()), data)


def make_mux(
    data,
    select
):
    n = len(data)
    if n <= 1 or n & (n - 1) != 0:
        raise ValueError
    if n == 2:
        return vtypes.Cond(select, data[0], data[1])
    k = n.bit_length() - 1
    if select.get_width() != k:
        raise ValueError
    return vtypes.Cond(select[k - 1],
                       make_mux(data[0:n//2], select[:k - 1]),
                       make_mux(data[n//2:], select[:k - 1]))


def make_decoder(data):
    k = data.get_width()
    n = 2**k
    return vtypes.Cat(*reversed([data == i for i in range(n)]))


def make_sky130_sram(
    name: str,
    datawidth: int,
    addrwidth: int,
) -> Module:
    m = Module(name)

    clk = m.Input('clk')  # clock
    ce0 = m.Input('ce0')  # chip enable for port 0 (active high)
    cen0 = m.Wire('cen0')
    cen0.assign(vtypes.Not(ce0))
    ce1 = m.Input('ce1')  # chip enable for port 1 (active high)
    cen1 = m.Wire('cen1')
    cen1.assign(vtypes.Not(ce1))
    we = m.Input('we')  # write enable for port 0 (active high)
    wen = m.Wire('wen')
    wen.assign(vtypes.Not(we))
    addr0 = m.Input('addr0', addrwidth)  # address for port 0
    addr1 = m.Input('addr1', addrwidth)  # address for port 1
    din = m.Input('din', datawidth)  # input data = written data for port 0
    dout0 = m.Output('dout0', datawidth)  # output data = read data for port 0
    dout1 = m.Output('dout1', datawidth)  # output data = read data for port 1

    if datawidth <= 8:
        if addrwidth <= 11:
            if addrwidth == 11:
                macro_name = 'sky130_sram_2kbyte_1rw1r_32x512_8'
            else:
                macro_name = 'sky130_sram_1kbyte_1rw1r_32x256_8'
            if addrwidth < 2:
                raise ValueError
            mux_sel0 = m.Wire('mux_sel0', 2)
            mux_sel0.assign(addr0[:2])
            mux_sel1 = m.Wire('mux_sel1', 2)
            mux_sel1.assign(addr1[:2])
            sram_addr0 = addr0[2:]
            sram_addr1 = addr1[2:]
            if addrwidth < 10:
                sram_addr0 = vtypes.Cat(zero(10 - addrwidth), sram_addr0)
                sram_addr1 = vtypes.Cat(zero(10 - addrwidth), sram_addr1)
            raw_dout0 = m.Wire('raw_dout0', 32)
            raw_dout1 = m.Wire('raw_dout1', 32)
            dout_list0 = [m.Wire(f'dout0_{i}', datawidth) for i in range(4)]
            dout_list1 = [m.Wire(f'dout1_{i}', datawidth) for i in range(4)]
            for i in range(4):
                dout_list0[i].assign(raw_dout0[8*i:8*(i+1)])
                dout_list1[i].assign(raw_dout1[8*i:8*(i+1)])
            dout0.assign(make_mux(dout_list0, mux_sel0))
            dout1.assign(make_mux(dout_list1, mux_sel1))
            ports = [
                ('clk0', clk), ('clk1', clk), ('csb0', cen0), ('csb1', cen1),
                ('web0', wen), ('wmask0', make_decoder(mux_sel0)),
                ('addr0', sram_addr0), ('addr1', sram_addr1),
                ('din0', pad(din, 8).repeat(4)), ('dout0', raw_dout0),
                ('dout1', raw_dout1)
            ]
            m.Instance(macro_name, 'ram', ports=ports, workaround=True)
        else:
            raise ValueError('not yet implemented')
    elif datawidth <= 16:
        if addrwidth <= 10:
            if addrwidth == 10:
                macro_name = 'sky130_sram_2kbyte_1rw1r_32x512_8'
            else:
                macro_name = 'sky130_sram_1kbyte_1rw1r_32x256_8'
            if addrwidth < 1:
                raise ValueError
            mux_sel0 = m.Wire('mux_sel0')
            mux_sel0.assign(addr0[0])
            mux_sel1 = m.Wire('mux_sel1')
            mux_sel1.assign(addr1[1])
            sram_addr0 = addr0[1:]
            sram_addr1 = addr1[1:]
            if addrwidth < 9:
                sram_addr0 = vtypes.Cat(zero(9 - addrwidth), sram_addr0)
                sram_addr1 = vtypes.Cat(zero(9 - addrwidth), sram_addr1)
            raw_dout0 = m.Wire('raw_dout0', 32)
            raw_dout1 = m.Wire('raw_dout1', 32)
            dout_list0 = [m.Wire(f'dout0_{i}', datawidth) for i in range(2)]
            dout_list1 = [m.Wire(f'dout1_{i}', datawidth) for i in range(2)]
            for i in range(2):
                dout_list0[i].assign(raw_dout0[16*i:16*(i+1)])
                dout_list1[i].assign(raw_dout1[16*i:16*(i+1)])
            dout0.assign(make_mux(dout_list0, mux_sel0))
            dout1.assign(make_mux(dout_list1, mux_sel1))
            byte_write_enable = vtypes.Cat(
                mux_sel0.repeat(2), vtypes.Not(mux_sel0).repeat(2))
            ports = [
                ('clk0', clk), ('clk1', clk), ('csb0', cen0), ('csb1', cen1),
                ('web0', wen), ('wmask0', byte_write_enable),
                ('addr0', sram_addr0), ('addr1', sram_addr1),
                ('din0', pad(din, 16).repeat(2)), ('dout0', raw_dout0),
                ('dout1', raw_dout1)
            ]
            m.Instance(macro_name, 'ram', ports=ports, workaround=True)
        else:
            raise ValueError('not yet implemented')
    elif datawidth <= 32:
        if addrwidth <= 9:
            if addrwidth == 9:
                macro_name = 'sky130_sram_2kbyte_1rw1r_32x512_8'
                pad_addr = partial(pad, width=9)
            else:
                macro_name = 'sky130_sram_1kbyte_1rw1r_32x256_8'
                pad_addr = partial(pad, width=8)
            raw_dout0 = m.Wire('raw_dout0', 32)
            raw_dout1 = m.Wire('raw_dout1', 32)
            dout0.assign(raw_dout0[:datawidth])
            dout1.assign(raw_dout1[:datawidth])
            # NOTE: `wmask0` is really active high?
            ports = [
                ('clk0', clk), ('clk1', clk), ('csb0', cen0), ('csb1', cen1),
                ('web0', wen), ('wmask0', vtypes.Int(1, 1).repeat(4)),
                ('addr0', pad_addr(addr0)), ('addr1', pad_addr(addr1)),
                ('din0', pad(din, 32)), ('dout0', raw_dout0),
                ('dout1', raw_dout1)
            ]
            m.Instance(macro_name, 'ram', ports=ports, workaround=True)
        else:
            raise ValueError('not yet implemented')
    else:
        raise ValueError('not yet implemented')

    return m


def make_gf180mcu_sram(
    name: str,
    datawidth: int,
    addrwidth: int,
) -> Module:
    if datawidth <= 0 or addrwidth <= 0:
        raise ValueError

    m = Module(name)

    clk = m.Input('clk')
    ce = m.Input('ce')  # active high
    cen = m.Wire('cen')  # active low
    cen.assign(vtypes.Not(ce))
    we = m.Input('we')  # active high
    wen = m.Wire('wen')  # active low
    wen.assign(vtypes.Not(we))

    addr = m.Input('addr', addrwidth)
    din = m.Input('din', datawidth)
    dout = m.Output('dout', datawidth)

    if addrwidth <= 9:
        if addrwidth == 9:
            macro_name = 'gf180mcu_fd_ip_sram__sram512x8m8wm1'
        elif addrwidth == 8:
            macro_name = 'gf180mcu_fd_ip_sram__sram256x8m8wm1'
        elif addrwidth == 7:
            macro_name = 'gf180mcu_fd_ip_sram__sram128x8m8wm1'
        else:
            macro_name = 'gf180mcu_fd_ip_sram__sram64x8m8wm1'
        if addrwidth < 6:
            addr = vtypes.Cat(vtypes.Int(0, 6 - addrwidth), addr)
        for j in range(datawidth // 8):
            m.Instance(macro_name, f'ram_{j}',
                       ports=[('CLK', clk), ('CEN', cen), ('GWEN', wen),
                              ('WEN', zero(8)), ('A', addr),
                              ('D', din[8*j:8*(j+1)]),
                              ('Q', dout[8*j:8*(j+1)])],
                       workaround=True)
        if datawidth % 8 != 0:
            tmp_in = m.Wire('tmp_in', 8)
            tmp_in.assign(vtypes.Cat(vtypes.Int(0, 8 - datawidth%8),
                                     din[datawidth // 8 * 8:]))
            tmp_out = m.Wire('tmp_out', 8)
            dout[datawidth // 8 * 8:].assign(tmp_out[:datawidth % 8])
            m.Instance(macro_name, f'ram_{datawidth // 8}',
                       ports=[('CLK', clk), ('CEN', cen), ('GWEN', wen),
                              ('WEN', zero(8)), ('A', addr),
                              ('D', tmp_in), ('Q', tmp_out)],
                       workaround=True)
    else:
        dout_list = [m.Wire(f'dout_{i}', datawidth)
                     for i in range(2**(addrwidth - 9))]
        dout.assign(make_mux(dout_list, addr[9:]))
        if datawidth % 8 != 0:
            tmp_in = m.Wire('tmp_in', 8)
            tmp_in.assign(vtypes.Cat(vtypes.Int(0, 8 - datawidth%8),
                                     din[datawidth // 8 * 8:]))
        for i in range(2**(addrwidth - 9)):
            seln = m.Wire(f'seln_{i}')
            seln.assign(addr[9:] != i)
            for j in range(datawidth // 8):
                m.Instance('gf180mcu_fd_ip_sram__sram512x8m8wm1',
                           f'ram_{i}_{j}',
                           ports=[('CLK', clk), ('CEN', vtypes.Ors(cen, seln)),
                                  ('GWEN', vtypes.Ors(wen, seln)),
                                  ('WEN', zero(8)), ('A', addr[:9]),
                                  ('D', din[8*j:8*(j+1)]),
                                  ('Q', dout_list[i][8*j:8*(j+1)])],
                           workaround=True)
            if datawidth % 8 != 0:
                tmp_out = m.Wire(f'tmp_out_{i}', 8)
                dout_list[i][datawidth // 8 * 8:].assign(tmp_out[:datawidth % 8])
                m.Instance('gf180mcu_fd_ip_sram__sram512x8m8wm1',
                           f'ram_{i}_{datawidth // 8}',
                           ports=[('CLK', clk), ('CEN', vtypes.Ors(cen, seln)),
                                  ('GWEN', vtypes.Ors(wen, seln)),
                                  ('WEN', zero(8)), ('A', addr[:9]),
                                  ('D', tmp_in), ('Q', tmp_out)],
                           workaround=True)

    return m


class ASICSRAM(RAM):
    def __init__(
        self,
        m: Module,
        name: str,
        clk: vtypes._Variable,
        rst: vtypes._Variable,
        datawidth: int,
        addrwidth: int,
        pdk: Literal['sky130', 'gf180mcu'] = 'sky130',
    ):
        self.m = m
        self.name = name
        self.clk = clk
        self.rst = rst
        self.datawidth = datawidth
        self.addrwidth = addrwidth
        self.pdk = pdk

        self.interfaces: list[dict[str, vtypes.Wire]] = []
        rw_if: dict[str, vtypes.Wire] = {}
        rw_if['ce'] = m.Wire(f'{name}_ce0')
        rw_if['we'] = m.Wire(f'{name}_we0')
        rw_if['addr'] = m.Wire(f'{name}_addr0', addrwidth)
        rw_if['din'] = m.Wire(f'{name}_din0', datawidth)
        rw_if['dout'] = m.Wire(f'{name}_dout0', datawidth)
        self.interfaces.append(rw_if)
        if pdk == 'sky130':
            r_if: dict[str, vtypes.Wire] = {}
            r_if['ce'] = m.Wire(f'{name}_ce1')
            r_if['addr'] = m.Wire(f'{name}_addr1', addrwidth)
            r_if['dout'] = m.Wire(f'{name}_dout1', datawidth)
            self.interfaces.append(r_if)

        if pdk == 'sky130':
            mod = make_sky130_sram(f'{name}_mod', datawidth, addrwidth)
            ports = [
                ('clk', clk), ('ce0', rw_if['ce']), ('ce1', r_if['ce']),
                ('we', rw_if['we']), ('addr0', rw_if['addr']),
                ('addr1', r_if['addr']), ('din', rw_if['din']),
                ('dout0', rw_if['dout']), ('dout1', r_if['dout'])
            ]
        elif pdk == 'gf180mcu':
            mod = make_gf180mcu_sram(f'{name}_mod', datawidth, addrwidth)
            ports = [
                ('clk', clk), ('ce', rw_if['ce']), ('we', rw_if['we']),
                ('addr', rw_if['addr']), ('din', rw_if['din']),
                ('dout', rw_if['dout'])
            ]
        else:
            raise ValueError(f'invalid PDK: {pdk}')
        m.Instance(mod, name + '_inst', ports=ports)

        self.seq = Seq(m, name + '_seq', clk, rst)

        self.mutex = None

    def read_rtl(self, addr, port=0, cond=None):
        """
        @return data, valid
        """

        cond = make_condition(cond)

        if cond is not None:
            enable = cond
        else:
            enable = vtypes.Int(1, 1)

        util.add_mux(self.interfaces[port]['addr'], enable, addr)
        util.add_enable_cond(self.interfaces[port]['ce'], enable, vtypes.Int(1, 1))

        rdata = self.interfaces[port]['dout']
        rvalid = self.seq.Prev(enable, 1)

        return rdata, rvalid

    def write_rtl(self, addr, wdata, port=0, cond=None):
        """
        @return None
        """
        cond = make_condition(cond)

        if cond is not None:
            enable = cond
        else:
            enable = vtypes.Int(1, 1)

        util.add_mux(self.interfaces[port]['addr'], enable, addr)
        util.add_mux(self.interfaces[port]['din'], enable, wdata)
        util.add_enable_cond(self.interfaces[port]['we'], enable, vtypes.Int(1, 1))
        util.add_enable_cond(self.interfaces[port]['ce'], enable, vtypes.Int(1, 1))
