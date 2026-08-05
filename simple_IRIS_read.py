import serial # installed using pip install pyserial. 
import time

# connect to the device using the defined baud rate, on my computer, the com port is COM6
device = serial.Serial("COM6", 9600, 8, "N", 1, timeout=1)

# issue the XY-OFF command to ensure the device is in quarry mode and not in stream mode. 
# it just makes reading data that we asked for easier. 
device.write("*9900XYC-OFF\r\n".encode("utf-8"))
# read the echo on the serial port.
data = device.readline().decode("utf-8")
# print the data
print(data)

# issue the XY command to trigger a single shot tilt measurement.
device.write("*9900XY\r\n".encode("utf-8"))
# wait for the command to process. Not really needed but recommended.
time.sleep(0.1)
# read the data into a data variable for the string.
data = device.readline().decode("utf-8")
# print the data
print(data)

# send the dump settings command.
device.write("*9900XY-DUMP-SETTINGS\r\n".encode("utf-8"))

# wait for the device to process the request and send data back.
time.sleep(0.1)
# read the serial port until the device is done transmitting data.
while True:
    data = device.readline().decode("utf-8")

    print(data)
    if data == "":
        break
# send the dump2 command to dump the second part of the settings information.
device.write("*9900XY-DUMP2\r\n".encode("utf-8"))

time.sleep(0.1)
while True:
    # read the serial port until the device is done transmitting data.
    data = device.readline().decode("utf-8")

    print(data)
    if data == "":
        break

# send the lut dump command, this will show the ADC counts mapped to an angle for the X and Y axes.
device.write("*9900LUT-OUTPUT\r\n".encode("utf-8"))

time.sleep(0.1)
while True:
    # read the serial port until the device is done transmitting data.
    data = device.readline().decode("utf-8")

    print(data)
    if data == "":
        break

# send the stream data command to see what the output looks like.
device.write("*9900XYC1\r\n".encode("utf-8"))
while True:
    # read the serial port until the device is done transmitting data.
    try:
        time.sleep(0.1)
        data = device.readline().decode("utf-8")

        print(data)
        if data == "":
            break
    except KeyboardInterrupt:
        break
