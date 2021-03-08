#!/usr/bin/python3
from tkinter import *
import serial
import time
from TFmini_I2C import *

root = Tk()
root.geometry("450x300")


def readSerial():
    Sensor0 = TFminiI2C(1, 0x10)

    counter = 0
    while(counter <= 1):
    #print( Sensor0.readAll(), "\t")
        if (Sensor0.readDistance() >= 4 and Sensor0.readDistance() <= 110):
            v.set(Sensor0.readDistance())
            print("Dist:", Sensor0.readDistance())
        else:
            print("Dist:",0)
            v.set(0)
        counter += 1
    root.after(1, readSerial)


v = StringVar()
Label(root, anchor='center', bg='white', textvariable=v,font=("Helvetica", 40), height='125', width='125').pack()
v.set('--.-')
root.after(100, readSerial)
root.mainloop()   

