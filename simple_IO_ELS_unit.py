"""
Author: Lucas Jameson
Date: 3 September 2026
This app was made for the folks who need to interact with a digital ELS unit but dont want to or cant use Realterm.
Feel free to mess with this app and test it out and try things. note that if it breaks, Jewell is happy to help you get it working again...To an extent.
"""

import sys
import time

import keyboard  # install using pip install keyboard
import serial  # installed using pip install pyserial.
import serial.tools.list_ports


def send(device: serial.Serial, text: str) -> None:
    device.write(f"{text}\r\n".encode("utf-8"))  # noqa: UP012


def read(device: serial.Serial) -> str:
    # read the echo on the serial port.
    return device.readline().decode("utf-8")


# Fetch all available serial ports
port_list = [port.device for port in serial.tools.list_ports.comports()]
print(f"Available ports: {port_list}")

baud_list = [9600, 19200, 28800, 57600, 115200, 230400]

# connect to the device using the defined baud rate, on my computer, the com port is COM6
while True:
    try:
        port: str = input("Enter the serial port[/dev/ttyUSBx or COMx]: ")
        # check if port is actually available...
        if port in port_list:
            break
        else:
            print("The port you entered does not exist..")
    except KeyboardInterrupt:  # use CTRL + C to abort.
        sys.exit()
    except Exception as e:  # noqa: BLE001
        print(e)

while True:
    try:
        baud_str: str = input("Enter the buad rate: ")
        # check if port is actually available...
        baud: int = int(baud_str)
        if baud in baud_list:
            break
        else:
            print("The baudrate you entered does not exist..")
    except KeyboardInterrupt:  # use CTRL + C to abort.
        sys.exit()
    except Exception as e:  # noqa: BLE001
        print(e)

# this assumes the 8 bytes, No parity, and 1 stopbits.
device = serial.Serial(port, baud, 8, "N", 1, timeout=1)

print("if you start it streaming, use the ESC key to breakout and send a new command. ")
while True:
    # read the serial port until the device is done transmitting data.
    command: str = input("Enter a command to send: ")
    try:
        send(device, command)
        time.sleep(0.1)
        while True:
            if keyboard.is_pressed("esc"):
                break
            data = read(device)
            print(data)
            if data == "":
                break

    except KeyboardInterrupt:
        break
