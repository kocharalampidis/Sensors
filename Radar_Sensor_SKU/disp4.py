#!/usr/bin/python3
from tkinter import *
import serial
import time

DEVICE = '/dev/ttyS0'
BAUD = 57600

root = Tk()
root.geometry("450x300")

def readSerial() :
    ser = serial.Serial(DEVICE, BAUD)
    counter = 0
    array=[]
    while counter < 8:
#         c = ser.read() # attempt to read a character from Serial
#         c = ord(serial.read())
          for i in range(0, 8):
            array.append(ord(ser.read()))
        
          YCTa = array[3]
          
          YCTb = array[4]
          YCT1 = (YCTa << 8) + YCTb
          if (YCT1 >= 60 and YCT1 <= 190):
              serBuffer = str(YCT1)
          else:
              serBuffer = 0
          print(YCT1, '\t', array[4])
          array.clear()
          counter = 1 + counter
          #log.insert('0.0', serBuffer)
          v.set(serBuffer)
    root.after(1, readSerial)



v = StringVar()
Label(root, anchor='center', bg='white', textvariable=v,font=("Helvetica", 40), height='125', width='125').pack()
v.set('--.-')

root.after(10, readSerial)
root.mainloop()
