// Parameters

/****** RISC Processor ******/
parameter add_size	  = 12;
parameter padd_size    = 24;
parameter cmd_size     = 3;
parameter cs_size      = 2;
parameter dqm_size     = 4;
parameter ba_size      = 2;
parameter data_size    = 32;
parameter timing_size  = 12;

parameter DataWidth = 32;
parameter AddrWidth = 24;
parameter OpcodeWidth = 8;
parameter StateSize = 2;

parameter Byte_size = 8;
parameter uart_add  = 3;

/****** SDRAM CNTRL ******/
parameter burst 		=	  3;
parameter HiZ       =  32'hz;
parameter cas_size     = 2;
parameter rc_size      = 2;
parameter ref_dur_size = 4;
parameter burst_size   = 4;
parameter byte_size    = 8;
parameter row_size     = 12;
parameter col_size     = 10;
parameter bank_size    = 2;
parameter rowstart     = 10;
parameter colstart     = 0;
parameter bankstart    = 22;

/****** Bus Arbiter ******/
parameter arbiter_bus_size = 3;
parameter irq_size		 	= 3;

/****** DMA CNTRL ******/
parameter dma_reg_addr  = 3;
parameter dma_reg_depth = 8;
parameter dma_reg_width = 32;
parameter dma_fifo_width = 8;
parameter dma_fifo_depth = 32;
parameter dma_counter_size = 5;
parameter fifo_size = 8;

/****** UART ******/
parameter uart_reg_depth = 8;
parameter uart_reg_width = 32;
parameter uart_cnt_size = 3;
parameter ser_in_cnt = 3;
parameter ser_out_cnt = 3;

/****** LRU Cache ******/
parameter cache_reg_depth = 8;
parameter cache_reg_width = 32;
parameter cache_line_size = 53;
parameter cache_valid = 2;
parameter cache_tag = 19;

/****** Timer ******/
parameter timer_reg_depth = 4;
parameter timer_reg_width = 32;
parameter timer_addr_size = 2;
parameter timer_size = 32;

/****** Flash CNTRL ******/
parameter flash_size = 8;
parameter flash_reg_width = 32;
parameter flash_reg_depth = 8;

module u_soc(// Inputs
	clk,
	reset,
	irq,
	ser_rxd,
	flash_datain,
	mem_datain,
	// Outputs
	pll_lock,
	addr,
	cs,
	ras,
	cas,
	we,
	dqm,
	cke,
	ba,
	pllclk,
	halted,
	ser_txd,
	flash_cle,
	flash_ale,
	flash_ce,
	flash_re,
	flash_we,
	flash_wp,
	flash_rb,
	flash_irq,
	flash_dataout,
	mem_dataout,
	mem_addr,
	mem_req,
	mem_rdwr,
	// Inouts
	dq
	);
						
	// Inputs
	output reg clk;
	input reset;
	input irq;
	input ser_rxd;
	input [flash_size - 1 : 0]flash_datain;
	input [data_size - 1 : 0]mem_datain;

	// Outputs
	output pll_lock;
	output [add_size - 1 : 0]addr;
	output [cs_size  - 1 : 0]cs;
	output ras;
	output cas;
	output we;
	output [dqm_size - 1 : 0]dqm;
	output cke;
	output [ba_size - 1 : 0]ba;
	output pllclk;
	output halted;
	output ser_txd;
	output flash_cle;
	output flash_ale;
	output flash_ce;
	output flash_re;
	output flash_we;
	output flash_wp;
	output flash_rb;
	output flash_irq;
	output [flash_size - 1 : 0]flash_dataout;
	output [data_size -1 : 0]mem_dataout;
	output [padd_size - 1 : 0]mem_addr;
	output mem_req;
	output mem_rdwr;

	// Inouts
	inout [data_size - 1 : 0]dq;

	// Signal Declarations
	// wire clk;
	wire reset;
	wire irq;
	wire [add_size - 1 : 0]addr;
	wire [cs_size - 1 : 0]cs;
	wire ras;
	wire cas;
	wire we;
	wire [dqm_size - 1 : 0]dqm;
	wire cke;
	wire [ba_size - 1 : 0]ba;
	wire pllclk;
	wire halted;
	wire [data_size - 1 : 0]dq;

	/****************************** Top Level Block Instantiation ****************************/
	// Could not find instantiation of pllclk and mem_addr in sub level of soc.v
	soc dut(	// Inputs
		.clk(clk0),
		.reset(reset),
		.irq(irq),
		.ser_rxd(ser_rxd),
		.flash_datain(flash_datain),
		.mem_datain(mem_datain),
		// Outputs
		.pll_lock(pll_lock),
		.addr(addr),
		.cs(cs),
		.ras(ras),
		.cas(cas),
		.we(we),
		.dqm(dqm),
		.cke(cke),
		.ba(ba),
		.pllclk(pllclk),
		.halted(halted),
		.ser_txd(ser_txd),
		.flash_cle(flash_cle),
		.flash_ale(flash_ale),
		.flash_ce(flash_ce),
		.flash_re(flash_re),
		.flash_we(flash_we),
		.flash_wp(flash_wp),
		.flash_rb(flash_rb),
		.flash_irq(flash_irq),
		.flash_dataout(flash_dataout),
		.mem_dataout(mem_dataout),
		.mem_addr(mem_addr),
		.mem_req(mem_req),
		.mem_rdwr(mem_rdwr),
		// Inouts
		.dq(dq)
		);



	initial begin
		$dumpfile("up.vcd");
		$dumpvars;
		clk=0;
		forever begin
			#5 clk=~clk;
		end
	end
	endmodule

