# Testplan

## Design Specification
* DUT : Embedded 32 bit RISC microprocessor with SDRAM controller
* Sub Modules:  
	* SDRAM Controller
	* UART
	* Flash Controller

## Logistics

* Machine: Laptop
* Repository: Github (https://github.com/learn-cocotb/capstone-ShwetaKiranTotla)
* Regression: Github actions
* Issue Tracking: Github issues
* Software: Python 3.10 (or any Python>3.6), iverilog, cocotb, cocotb-bus, cocotb-coverage, xcelium/vcs/questasim (for code coverage)
* Licenses: Simulator License for code coverage
### Bus Functional Model

* SDRAM Controller:  
	* This BFM emulates the behavior of the SDRAM (Synchronous Dynamic Random-Access Memory) module.
	* It provides methods to simulate read and write operations to the SDRAM.

* UART:  
	* This BFM emulates the behavior of the Universal Asynchronous Receiver-Transmitter module.
	* It provides methods to simulate data transmission and reception.

* Flash Controller:  
	* This BFM emulates the behavior of the flash memory module.
	* It provides methods to simulate flash memory read and write operations.

* Testbench:  
	* This BFM handles the configuration and connectivity of the testbench components.
	* It sets up the necessary connections between the SDRAM controller, UART, Flash controller, and other verification components.

* Scoreboard:  
	* This BFM compares the actual outputs from the DUT with the expected results and raises assertions if any discrepancies are found.
	* The scoreboard can be used as a monitor for the behavior of the SDRAM controller, UART, and Flash controller, and verify the correctness of their operations.

## Environment
Unit Level:  
Microprocessor which has IRQ and clock signal as input and Halted signal as output


## Test cases

### Test case 1: SDRAM Controller Datapath test
* Feature: SDRAM Controller
* Description: Perform read/write operations to the SDRAM and verify the data correctness.
* Scenario: Write a pattern of data to a specific address in the SDRAM, read it back, and compare it with the expected values.

### Test case 2: UART Communication test
* Feature: UART
* Description: Verify the communication functionality of the UART module by transmitting and receiving data.
* Scenario: Configure the UART module to transmit data, receive the transmitted data, and compare it with the expected values.

### Test case 3: Flash Controller Datapath test
* Feature: Flash Controller
* Description: Read/ Write data to/from flash and check whether the data is transmitted/ received correctly.

## Goals: Code Coverage and Functional Coverage

* Branch and Toggle Coverage
* 100% Functional Coverage

### SDRAM Coverage Cross
* Transaction * Address Range * Data Patterns

#### Coverage Bins
* Transaction = ['Read', 'Write']
* Address Range = [0, 4095]
* Data Patterns: 12'h000, 12'h111, 12'hAAA, 12'h555 and random cases.

### UART Coverage Cross
* Transaction * Address Range * Data Patterns

#### Coverage Bins
* Transaction = ['Transmit data', 'Receive data']
* Address Range = [0, 255]
* Data Patterns: 8'h00, 8'h11, 8'hAA, 8'h55 and random cases.

### Flash Coverage Cross
* Transaction * Address Range * Data Patterns

#### Coverage Bins
* Address Range = [0, 255]
* Transaction = ['Flash Data In', 'Flash Data Out']
* Data Patterns: 8'h00, 8'h11, 8'hAA, 8'h55 and random cases.

## Protocol
### RISC Processor Signals :traffic_light:

| name   | direction | description                                                 |
| ---    | ---       | ---                                                         |
| reset  | input     | resets the SDRAM controller when asserted                   |
| clk    | input     | clock                                                       |
| addr   | input     | address bus                                                 |
| q      | output    | output data bus                                             |



## Diagram showing the verification components(SB, Driver, Monitor) and their connection to each Interface
```
+---------------------------------------------+
|                  Scoreboard                 |
+-------^-------------------------------------+
        |                    +---------------------------------------------+
        |                    |            Testcase/ Sequencer              |
        |                    +---------------------------------------------+
        |                           |              |               |
        |                           |              |               |
        |                           |              |               |
+----------------+      +-----------v----+  +------v-----------+  +v------------+
|    Monitor     |      |    Driver      |  |     Driver       |  |   Driver    |
+------^---------+      +----------------+  +------------------+  +-------------+
       |                             |              |               |
       |-----------------------------|              |               |
                                     |              |               |
                      +--------------v--+  +--------v-------+  +----v-------------+
                      | SDRAM Controller|  |       UART     |  | Flash Controller |
                      +-----------------+  +----------------+  +------------------+
                                   |              |               |
                                   |              |               |
                                   |              |               |
                       +-----------v--------------v---------------v--+
                       |                  Bus Arbiter                |
                       +---------------------------------------------+


```

## File Descriptions
* sdram_cvr.py: Directed and random test cases for sdram controller module with coverage report.
* flash_test.py: Testbench for directed test case for sample values of receieve and transmit in flash.
* sdram_test.py: Directed and random test cases for sdram controller module with scoreboard and monitor.
* sdram_directed.py: Basic directed test cases for sdram controller module.
* uart_test.py: Directed and random test cases for uart.
* uart_hello: Testing uart receive and transmit by a hello string.
* dummy_test.py: A sample cocotb test file, upon running this, there is always a test pass.
* print.py: Snippet to print a random value from an array.
* uart_cocotb.py: Trial of the uart functionality using the exeternal uart module in cocotb.


