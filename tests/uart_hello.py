import cocotb
from cocotb.triggers import RisingEdge, FallingEdge
from cocotb.clock import Clock

@cocotb.test()
async def uart_test(dut):
    # Start Clock
    clock = Clock(dut.clk, 10, units="ns")
    cocotb.fork(clock.start())

    # Reset the UART
    dut.reset = 1
    await RisingEdge(dut.clk0)
    dut.reset = 0

    # Test data to be transmitted
    test_data = b"Hello, UART!"

    # Transmit test data
    cocotb.fork(transmit_data(dut, test_data))

    # Receive and verify test data
    received_data = await receive_data(dut, len(test_data))
    assert received_data == test_data, "Received data does not match transmitted data"

async def transmit_data(dut, data):
    # Transmit data byte by byte
    dut.uart_wr = 1
    for byte in data:
        dut.tx_data = byte
        await RisingEdge(dut.clk)
    dut.uart_wr = 0

async def receive_data(dut, length):
    received_data = bytearray()
    rx_active = False

    # Receive data byte by byte
    while len(received_data) < length:
        if dut.rx_active and not rx_active:
            rx_active = True
            await RisingEdge(dut.clk)
        elif rx_active and not dut.rx_active:
            received_data.append(dut.rx_data.value.integer)
            rx_active = False
            await RisingEdge(dut.clk)
        else:
            await RisingEdge(dut.clk)
    return received_data

