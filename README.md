# ELS_Quick_Setup
A quick start app for the digital electrolytic sensors line (D801, D711, MD900, D500).

## About
Author: Lucas Jameson
Date: 8th March 2024

## Installation
+ Clone the repository from Github to one's local machine.
+ Create a virtual environment (venv) using command "python -m venv .venv"
+ Activate the venv using the command "source /.venv/bin/activate" (Linux) or "\.venv\Scripts\acitvate"
+ Load all modules for the app using the command "pip install -r requirements.txt"

## Usage
Select the serial port, baud rate, and parity from the dropdown menus. Press the "Connect" button to establish a serial connection to one's sensor.
At this point, one can use the "Command" box to send command to the sensor. The output will be displayed in the "Message Prompt" box. One could alterna


## Commands
+ XY - Outputs a single tilt and temperature measurement. The format of the output depends on the setting of the SO command.
+ SO-xxx -  Selects the output format for the XY command. “xxx” selects format as follows:
    - ASH: Ashtech compatible NMEA format
    - SIM: Simple x,y,t,sn output string (default)
    - XDR: NMEA XDR format
    - TCM: Trimble Navigation proprietary pitch (Y) and roll (X) string
    - BAE: BAE Systems encoded 11-byte string containing a sync packet, x, y, t,
    - SN, and checksum information. Advanced users only—typically for embedded system integration.
+ XY-MEMS - Stores tiltmeter readings at selected output rate in nonvolatile memory. (Versions 5.1 and higher)
+ XY-MEMD - Downloads data from nonvolatile memory. (Versions 5.1 and higher)
+ XY-M1 - Sets the tiltmeter to Mode-1 operation.
+ XYVR - Displays the sign-on string.
+ ID - Sets the ID of units in the daisy chain (not currently implemented).
+ XY-TR-PASH-ON - Translates the Paros provided $PASHS,XDR,P sentences to standard NMEA XDR format.
+ XY-TR-PASH-OFF - Turns off translation of $PASHS,XDR,P sentences.
+ XY-EP - Enables power on message.
+ XY-SP - Disables power on message.
+ XY-EE - Enables echoing of global 99 commands.
+ XY-SE - Disables echoing of global 99 commands.
+ XY-SET-BAUDRATE,x - Sets baud rate to value of x in bits per second. Selectable values include 9600, 19200, 28800, 57600, 115200 and 230400 baud.
+ XY-SET-N-SAMP,x - Sets number of samples that are averaged before a reading is transmitted; x may have any value from 1 to 1000. Changing this value may also change the output rate.
+ XY-SET-RSMODE,x - Selects serial output mode:
  - x = 0 RS232
  - x = 1 RS485 (RS422)
+ XY-AUTOZ - Turns on auto zero function.
+ XY-AUTOZOFF - Turns off auto zero function.
+ XYCx - Continuously sends XY data where x determines output rate as follows:
  - x = 0: 8-10 outputs per second
  - x = 1: 4 outputs per second
  - x = 2: 1 output per second (default)
  - x = 3: 1 output every 10 seconds
  - x = 4: 1 output every 60 seconds
  - x = 5: 1 output every hour
  - x = 6: 1 output every 12 hours
  - x = 7: 1 output every 24 hours
  - x = 0A: Averaging of the 8-10 outputs per second data
  - x = 1A: Averaging of the 4 outputs per second data
  - x = 2A or x = A: Averaging of the 1 output per second data
  Once initiated, continuous output remains in effect until turned off with the
+ XYC-OFF - Turns off XYC mode.
+ XY-SET-CTRL-ON - Enables control feature.
+ XY-SET-CTRL-OFF - Disables control feature.
+ XY-SET-CTRLTEST-ON - Sets the control pin high (+5 VDC).
+ XY-SET-CTRLTEST-OFF - Sets the control pin low (0 VDC).
+ XY-SET-THRESHOLD,x+,x-,y+,y- - Sets the control thresholds.
+ XY-SET-HYST,k - Sets the control hysteresis.
+ XY-DUMP-SETTINGS - Dumps settings of device.
+ XY-DUMP2 - Dumps extended settings of device