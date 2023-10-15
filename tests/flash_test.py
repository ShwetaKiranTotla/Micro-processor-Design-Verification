import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge, Timer
from cocotb.result import TestFailure
from cocotb.binary import BinaryValue


@cocotb.coroutine
def uart_tx(dut, data):
    dut.uart_tx_data <= data
    dut.uart_tx_valid <= 1
    yield RisingEdge(dut.clk)
    dut.uart_tx_valid <= 0


@cocotb.coroutine
def uart_rx(dut):
    yield RisingEdge(dut.clk)
    while dut.uart_rx_valid != 1:
        yield RisingEdge(dut.clk)
    data = dut.uart_rx_data.value
    yield FallingEdge(dut.clk)
    return data


@cocotb.coroutine
def reset_dut(dut):
    dut.rst <= 1
    yield Timer(2, units='us')
    dut.rst <= 0
    yield Timer(1, units='us')


@cocotb.test()
def uart_test(dut):
    clock = Clock(dut.clk, 10, units='ns')
    cocotb.fork(clock.start())

    yield reset_dut(dut)

    # Test data to be transmitted
    test_data = [0x12, 0x34, 0x56, 0x78]

    # Transmit test data
    for data in test_data:
        yield uart_tx(dut, BinaryValue(data, n_bits=8, bigEndian=False))

    # Receive and verify transmitted data
    for data in test_data:
        received_data = yield uart_rx(dut)
        if received_data != data:
            raise TestFailure(f"Received data {received_data} does not match transmitted data {data}")

