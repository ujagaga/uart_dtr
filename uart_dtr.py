#!/usr/bin/env python3

import serial
import sys
import time
import errno


port = "/dev/ttyUSB0"

if len(sys.argv) > 1:
    custom_port = sys.argv[1]
    if custom_port.startswith("tty"):
        port = f"/dev/{custom_port}"
    else:
        port = custom_port

try:
    ser = serial.Serial(port, 9600)
    # Often it does not work correctly the first time, so you need to try again
    ser.close()
    time.sleep(0.1)
    ser = serial.Serial(port, 9600)

    ser.dtr = True
    print(f"DTR set LOW on port {port}")
    input("\nPress enter to set HIGH")

    ser.dtr = False
    print(f"DTR set HIGH on port {port}\n")
    ser.close()

except serial.SerialException as e:
    if hasattr(e, 'errno'):
        err = e.errno
    else:
        # On some systems, errno might not be directly available.
        # Parse the string instead:
        err = None
        if "Device or resource busy" in str(e):
            err = errno.EBUSY

    if err == errno.EBUSY:
        print(f"Port {port} is busy (Device is open by another process).")
    else:
        print(f"SerialException: {e}")

except Exception as e:
    print(f"Error opening or setting DTR on port {port}: {e}")
    print("Please specify a valid serial port")