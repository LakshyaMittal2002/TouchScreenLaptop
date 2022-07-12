import pyautogui
import serial
import math

# make sure the 'COM#' is set according the Windows Device Manager
#This is used to transfer the coordinates from arduino to python serially
ser = serial.Serial('COM9', 115200, timeout=1)
# l is half the longest dimension of the screen
l=11

i=0
#Making a loop for now of values it should transfer
while i<50:
    line = ser.readline()   # read a byte
    if line:
        string = line.decode()  # convert the byte string to a unicode string
        # num = int(string)  # convert the unicode string to an int
        r,Q=(string.split(","))
        #r1 is the disantce obtained from TOF sensor
        r1=float(r)
        # q1 is the angle which sensor makes with the x axis as the servo motor changes its angle
        Q1=float(Q.strip())
        # Printing distnace and angle values
        print("r : " +str(r1)+" | " + "Q : "+ str(Q1))  
        
        # x=l-r1*(math.cos(Q1*0.0174532925))+3
        # y=r1*(math.sin(Q1*0.0174532925))+2
        #Converting the obtained x and y values from distance sensor to final coordinates according the laptop
        # origin is at top left corner of the laptop or any computer screen
        x=l-r1*(math.sin(Q1*0.0174532925))+3
        y=r1*(math.cos(Q1*0.0174532925))+2
        #+3 and +2 are added to improve the error correction due to faulty servos
        # if (0<Q<=90):
        #     x=l-r1*(math.sin(Q1*0.0174532925))+3
        # elif (90<Q<180):
        #     x=l+r1*(math.sin(Q1*0.0174532925))+3
        # else


        print("x: "+ str(x) + " | "+ " y: " +str(y))
        # if x or y <0 then the cursor will hide inside which we do not want so everytime we make it to 1,1 so that cursor is visible.
        if x<=0.1 or y<=0.1:
            x=1
            y=1
     # Moving the cursor according to our hand movements   
        pyautogui.moveTo( (x*60) , (x*61), duration = 1)
     #duration high so chances of delay
        i=i+1


ser.close()