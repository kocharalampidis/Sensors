from pyfiglet import *
import serial
import os
import time

ser = serial.Serial('/dev/ttyS0', 57600)
array = []

while True:
    for i in range(0, 8):
        array.append(ord(ser.read()))
        
    YCTa = array[3]
    YCTb = array[4]
    YCT1 = (YCTa << 8) + YCTb
    print(YCT1, '\t', array[4])
    array.clear()

# for i in range(0, len(array)):
#     print(array[i])


