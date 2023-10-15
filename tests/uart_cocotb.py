from cocotbext.uart import UartSource, UartSink

uart_source = UartSource(dut.ser_txd, baud=115200, bits=8)
uart_sink = UartSink(dut.ser_rxd, baud=115200, bits=8)

@cocotb.test
async def UartTx():
	await uart_source.send(b'test data')
	await uart_source.wait()
