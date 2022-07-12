import pyautogui
import serial
import math
import time

# make sure the 'COM#' is set according the Windows Device Manager
ser = serial.Serial('COM9', 115200, timeout=1)

l=11

i=0
while i<150:
    line = ser.readline()   # read a byte
    if line:
        string = line.decode()  # convert the byte string to a unicode string
        # num = int(string)  # convert the unicode string to an int
        r,Q=(string.split(","))

        r1=float(r)
        Q1=float(Q.strip())

        print("r : " +str(r1)+" | " + "Q : "+ str(Q1))  
        
        
        


       
        if (r1<=0.1 or Q1<=0.1):
            r1=1
            Q1=1
        # Duration should be low to avoid delay
        pyautogui.moveTo( (r1*60) , (Q1*61), duration=0.001)

        i=i+1
        time.sleep(0.01)

ser.close()