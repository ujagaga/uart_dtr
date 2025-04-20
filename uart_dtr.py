#!/usr/bin/env python3

import serial
import sys


port = "/dev/ttyUSB0"

if len(sys.argv) > 1:
    custom_port = sys.argv[1]
    if custom_port.startswith("tty"):
        port = f"/dev/{custom_port}"

try:
    ser = serial.Serial(port, 9600)
    ser.dtr = True
    print(f"DTR set LOW on port {port}")

    input("\nPress enter to set HIGH")

    ser.dtr = False

    print(f"DTR set HIGH on port {port}\n")
    ser.close()
except serial.SerialException as e:
    print(f"Error opening or setting DTR on port {port}: {e}")