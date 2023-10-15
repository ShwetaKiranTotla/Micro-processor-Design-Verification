SIM ?= icarus
TOPLEVEL_LANG ?= verilog
waves = 1
#VERILOG_INCLUDES += -I$(PWD)/../hdl
VERILOG_INCLUDE_DIRS += $(PWD)/../hdl
#VERILOG_SOURCES += $(PWD)/wrappers/top_wrapper.v
VERILOG_SOURCES += $(PWD)/../hdl/Xilinx/CLKDLL.v
VERILOG_SOURCES += $(PWD)/../hdl/Xilinx/IBUFG.v
VERILOG_SOURCES += $(PWD)/../hdl/Xilinx/STARTUP_VIRTEX4.v
VERILOG_SOURCES += $(PWD)/../hdl/Xilinx/C_DIST_MEM_V4_1.v
VERILOG_SOURCES += $(PWD)/../hdl/Xilinx/SYNC_FIFO_V2_0.v
VERILOG_SOURCES += $(PWD)/../hdl/Xilinx/C_REG_FD_V4_0.v
VERILOG_SOURCES += $(PWD)/../hdl/bufg.v
VERILOG_SOURCES += $(PWD)/../hdl/ACC.v
VERILOG_SOURCES += $(PWD)/../hdl/ALU.v
VERILOG_SOURCES += $(PWD)/../hdl/bus_arbiter.v
VERILOG_SOURCES += $(PWD)/../hdl/cmd_ack.v
VERILOG_SOURCES += $(PWD)/../hdl/cmd_decoder.v
VERILOG_SOURCES += $(PWD)/../hdl/cmd_detector.v
VERILOG_SOURCES += $(PWD)/../hdl/cmd_generator.v
VERILOG_SOURCES += $(PWD)/../hdl/cmd_internal_reg.v
VERILOG_SOURCES += $(PWD)/../hdl/command_if.v
VERILOG_SOURCES += $(PWD)/../hdl/CONTROL.v
VERILOG_SOURCES += $(PWD)/../hdl/data_cache_way0.v
VERILOG_SOURCES += $(PWD)/../hdl/data_cache_way1.v
VERILOG_SOURCES += $(PWD)/../hdl/data_cache_way2.v
VERILOG_SOURCES += $(PWD)/../hdl/data_cache_way3.v
VERILOG_SOURCES += $(PWD)/../hdl/data_in_reg.v
VERILOG_SOURCES += $(PWD)/../hdl/data_port.v
VERILOG_SOURCES += $(PWD)/../hdl/dma_cntrl.v
VERILOG_SOURCES += $(PWD)/../hdl/dma_fifo.v
VERILOG_SOURCES += $(PWD)/../hdl/dma_internal_reg.v
VERILOG_SOURCES += $(PWD)/../hdl/flash_ctrl.v
VERILOG_SOURCES += $(PWD)/../hdl/fsm.v
VERILOG_SOURCES += $(PWD)/../hdl/instruction_cache_way0.v
VERILOG_SOURCES += $(PWD)/../hdl/instruction_cache_way1.v
VERILOG_SOURCES += $(PWD)/../hdl/instruction_cache_way2.v
VERILOG_SOURCES += $(PWD)/../hdl/instruction_cache_way3.v
VERILOG_SOURCES += $(PWD)/../hdl/IR.v
VERILOG_SOURCES += $(PWD)/../hdl/k9f1g08u0m.v
VERILOG_SOURCES += $(PWD)/../hdl/lru_data_cache.v
VERILOG_SOURCES += $(PWD)/../hdl/lru_instruction_cache.v
VERILOG_SOURCES += $(PWD)/../hdl/MEM.v
VERILOG_SOURCES += $(PWD)/../hdl/MUX12.v
VERILOG_SOURCES += $(PWD)/../hdl/MUX16.v
VERILOG_SOURCES += $(PWD)/../hdl/oe_generator.v
VERILOG_SOURCES += $(PWD)/../hdl/PC.v
VERILOG_SOURCES += $(PWD)/../hdl/ras_cas_delay.v
VERILOG_SOURCES += $(PWD)/../hdl/ref_ack.v
VERILOG_SOURCES += $(PWD)/../hdl/ref_timer.v
VERILOG_SOURCES += $(PWD)/../hdl/risc.v
VERILOG_SOURCES += $(PWD)/../hdl/sdram.v
VERILOG_SOURCES += $(PWD)/../hdl/sdram_cntrl.v
VERILOG_SOURCES += $(PWD)/../hdl/sdramctrl_rtl.v
VERILOG_SOURCES += $(PWD)/../hdl/sdram_mux.v
VERILOG_SOURCES += $(PWD)/../hdl/sdram_port.v
VERILOG_SOURCES += $(PWD)/../hdl/timer.v
VERILOG_SOURCES += $(PWD)/../hdl/uart.v
VERILOG_SOURCES += $(PWD)/../hdl/soc.v

sdram:
	rm -rf sim_build
	$(MAKE) sim MODULE=sdram_test TOPLEVEL=soc
	
dummy:
	rm -rf sim_build
	$(MAKE) sim MODULE=dummy_test TOPLEVEL=u_soc
	
uart:
	rm -rf sim_build
	$(MAKE) sim MODULE=uart_test_cocotb TOPLEVEL=u_soc
	
flash:
	rm -rf sim_build
	$(MAKE) sim MODULE=flash_test TOPLEVEL=soc
all: sdram uart flash
include $(shell cocotb-config --makefiles)/Makefile.sim
