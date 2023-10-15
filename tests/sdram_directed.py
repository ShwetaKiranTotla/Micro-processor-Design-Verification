import cocotb
from cocotb.triggers import RisingEdge, FallingEdge, Timer
from cocotb.clock import Clock


@cocotb.test()
async def sdram_controller_test(dut):
	#Start Clock
	clock = Clock(dut.clk0, 10, units="ns")
	cocotb.fork(clock.start())
	
	#Reset the controller
	dut.reset = 1
	await RisingEdge(dut.clk0)
	dut.reset = 0
	
	#Write data to SDRAM
	dut.wwe = 1
	dut.wsadd = 0x001
	dut.sdram_in = 0x0000_0000
	await RisingEdge(dut.clk0)
	dut.wwe = 0
	
	#Read data from SDRAM
	dut.wsadd = 0x001
	await RisingEdge(dut.clk0)
	assert dut.sdram_data == 0x0000_0000, "SDRAM data mismatch"  # Check if the read data is correct
	
	#Write data to SDRAM
	dut.wwe = 1
	dut.wsadd = 0x022
	dut.sdram_in = 0x1111_1111
	await RisingEdge(dut.clk0)
	dut.wwe = 0
	
	#Read data from SDRAM
	dut.wsadd = 0x022
	await RisingEdge(dut.clk0)
	assert dut.sdram_data == 0x1111_1111, "SDRAM data mismatch"  # Check if the read data is correct
	
	#Write data to SDRAM
	dut.wwe = 1
	dut.wsadd = 0x033
	dut.sdram_in = 0x5555_5555
	await RisingEdge(dut.clk0)
	dut.wwe = 0
	
	#Read data from SDRAM
	dut.wsadd = 0x033
	await RisingEdge(dut.clk0)
	assert dut.sdram_data == 0x5555_5555, "SDRAM data mismatch"  # Check if the read data is correct
	
	#Write data to SDRAM
	dut.wwe = 1
	dut.wsadd = 0x044
	dut.sdram_in = 0xAAAA_AAAA
	await RisingEdge(dut.clk0)
	dut.wwe = 0
	
	#Read data from SDRAM
	dut.wsadd = 0x044
	await RisingEdge(dut.clk0)
	assert dut.sdram_data == 0xAAAA_AAAA, "SDRAM data mismatch"  # Check if the read data is correct
