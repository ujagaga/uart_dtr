# Uart DTR

Simple script to controll UART DTR pin. I am using it when programming microcontrollers, 
to set the boot mode pin low and enter programming mode instead of using jumper wires.

## Usage
Befor trying, make sure you have PySerial library installed. On Debian based systems:


	sudo apt instell python3-pyserial


Then you can run 

	
	python3 uart_dtr.py


Or even simpler if you make the script executable and create a shortcut in ~/.local/bin or /usr/bin/

	
	chmod +x /path/to/uart_dtr.py
	ln -s /path/to/uart_dtr.py ~/.local/bin/uart_dtr


Then you can run it symply:


	uart_dtr <optional_uart_port>


If you do not specify the UART port, default is /dev/ttyUSB0


## Windows usage

The script should work in windows too if you provide the correct serial port in the input parameter:


	python uart_dtr.py com3

 
