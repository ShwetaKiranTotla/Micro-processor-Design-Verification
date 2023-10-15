import random
import cocotb
from cocotb.triggers import Timer, RisingEdge, ReadOnly, NextTimeStep, FallingEdge
from cocotb_bus.drivers import BusDriver
from cocotb_bus.scoreboard import Scoreboard
#from cocotb_coverage.coverage import CoverCross, CoverPoint, coverage_db
#from cocotb_bus.monitors import BusMonitor
from cocotb.clock import Clock

class InputDriver(BusDriver):
    _signals = ["wwe", "wsadd", "sdram_in"]

    async def write_data(self, addr, data):
        self.bus.wwe = 1
        self.bus.wsadd = addr
        self.bus.sdram_in = data
        await RisingEdge(dut.clk0)
        self.bus.wwe = 0

@cocotb.test()
async def sdram_controller_test(dut):
    # Start Clock
    clock = Clock(dut.clk0, 10, units="ns")
    cocotb.fork(clock.start())
    
    scoreboard = Scoreboard(dut)

    # Create and start the input driver
    driver = InputDriver(dut, None, None)
    
    # Reset the controller
    dut.reset = 1
    for i in range(5):
    	await RisingEdge(dut.clk0)
    
    dut.reset = 0
    for i in range(5):
    	await RisingEdge(dut.clk0)
    	
    data_addresses = [0x001, 0x022, 0x033, 0x044]
    data_values = [0x0000_0000, 0x1111_1111, 0x5555_5555, 0xAAAA_AAAA]

    if dut.we == 0:
        # Read and compare directed test case data from the SDRAM
        for addr, data in zip(data_addresses, data_values):
            # Read data from SDRAM
            for i in range(5):
            	await RisingEdge(dut.clk0)
            dut.wsadd = addr
            await RisingEdge(dut.clk0)
            #scoreboard.add_expected_results(addr, data)
            #scoreboard.add_actual_results(addr, dut.sdram_data)
            scoreboard.append(await scoreboard.read(dut.sdram_data, data, "Read data mismatch"))

    random_data_addresses = random.sample(range(0x000, 0xFFF), 5)
    random_data_values = random.sample(range(0x00000000, 0xFFFFFFFF), 5)

    if dut.we == 0:
        # Read and compare randomized test case data from the SDRAM
        for addr, data in zip(random_data_addresses, random_data_values):
            # Read data from SDRAM
            dut.wsadd = addr
            await RisingEdge(dut.clk0)
            scoreboard.append(await scoreboard.read(dut.sdram_data, data, "Read data mismatch"))
