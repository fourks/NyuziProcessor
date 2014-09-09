<img align="right" src="https://github.com/jbush001/GPGPU/wiki/teapot-icon.png">


This project is a multi-processor GPGPU (general purpose graphics processing unit) hardware core, implemented in SystemVerilog. It is licensed under LGPLv2. Documentation is available here: https://github.com/jbush001/GPGPU/wiki.  

## Running in Verilog simulation

### Prerequisites
1. GCC 4.7+ or Clang 4.2+
2. Python 2.7
3. Verilator 3.862 or later (http://www.veripool.org/projects/verilator/wiki/Installing).  
4. libreadline-dev
5. C/C++ cross compiler toolchain targeting this architecture. Download and build from https://github.com/jbush001/LLVM-GPGPU.  Instructions on how to build it are in the README file in that repository.
6. Optional: Emacs v23.2+, for AUTOWIRE/AUTOINST (Note that this doesn't require using Emacs as an editor. Using 'make autos' in the rtl/ directory will run this operation in batch mode if the tools are installed).
7. Optional: Java (J2SE 6+) for visualizer app 
8. Optional: GTKWave (or similar) for analyzing waveform files (http://gtkwave.sourceforge.net/)

Some package managers do have verilator, but the version is pretty old. It is important to have version 862 or later because bug fixes in the most recent version are necessary for this to run correctly.
MacOS should have libreadline-dev by default.

### Building and running

1. Build verilog models and tools. From the top directory of this project, type:

        make

2. To run verification tests (in Verilog simulation). From the top directory: 

        make test

3. To run 3D Engine (output image stored in fb.bmp)

        cd firmware/3D-renderer
        make verirun

## Running on FPGA

### Prerequisites
This runs on Linux only.

1. libusb-1.0
2. USB Blaster JTAG tools (https://github.com/swetland/jtag)
3. Quartus II FPGA design software (http://www.altera.com/products/software/quartus-ii/web-edition/qts-we-index.html)
4. Terasic's DE2-115 evaluation board (http://www.terasic.com.tw/cgi-bin/page/archive.pl?Language=English&No=502)
5. C/C++ cross compiler toolchain described above https://github.com/jbush001/LLVM-GPGPU.

### Building and running
1. Build USB blaster command line tools
 * Update your PATH environment variable to point the directory where you built the tools.  
 * Create a file /etc/udev/rules.d/99-custom.rules and add the line: 

            ATTRS{idVendor}=="09fb" , MODE="0660" , GROUP="plugdev" 

2. Build the bitstream (ensure quartus binary directory is in your PATH, by default installed in ~/altera/[version]/quartus/bin/)

        cd rtl/fpga/de2-115
        make

3. Make sure the FPGA board is in JTAG mode by setting SW19 to 'RUN'
4. Load the bitstream onto the FPGA (note that this will be lost if the FPGA is powered off).

        make program 

5.  Load program into memory and execute it using the runit script as below.   The script assembles the source and uses the jload command to transfer the program over the USB blaster cable that was used to load the bitstream.  jload will automatically reset the processor as a side effect, so the bitstream does not need to be reloaded each time.

        cd ../../../tests/fpga/blinky
        ./runit.sh

