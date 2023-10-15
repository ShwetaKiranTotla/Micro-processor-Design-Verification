import cocotb
from cocotb.triggers import RisingEdge
from cocotb.clock import Clock
import random

@cocotb.test()
async def uart_controller_test(dut):
    # Start Clock
    clock = Clock(dut.clk0, 10, units="ns")
    cocotb.fork(clock.start())

    # Reset the controller
    dut.reset = 1
    await RisingEdge(dut.clk0)
    dut.reset = 0
    
    # Data values for write and read
    data_values = [0x0000_0000, 0x1111_1111, 0x5555_5555, 0xAAAA_AAAA]
    
    # Directed Test case
    for data in data_values:
        # Write data to UART
        dut.uart_wr = 1
        dut.uart_data = data
        await RisingEdge(dut.clk0)
        dut.uart_wr = 0
        
        # Wait for data to be transmitted
        #while dut.uart_busy:
         #   await RisingEdge(dut.clk0)
        
        # Read data from UART
        dut.uart_rd = 1
        await RisingEdge(dut.clk0)
        assert dut.uart_data_out == data, f"UART data mismatch for {hex(data)}"
        dut.uart_rd = 0
    
    # Randomized Test Case
    random_data_values = random.sample(range(0x00000000, 0xFFFFFFFF), 5)

    for data in random_data_values:
        # Write data to UART
        dut.uart_wr = 1
        dut.uart_data = data
        await RisingEdge(dut.clk0)
        dut.uart_wr = 0
        
        # Wait for data to be transmitted
        
        # Read data from UART
        dut.uart_rd = 1
        await RisingEdge(dut.clk0)
        assert dut.uart_data_out == data, f"UART data mismatch for {hex(data)}"
        dut.uart_rd = 0

