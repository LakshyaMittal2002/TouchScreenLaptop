#Importing various Modules
import pygame
import random
import serial
import time

#This is used to transfer the coordinates from arduino to python serially
ser = serial.Serial('COM9', 115200, timeout=1)
# time.sleep(1)


pygame.init()
#Fixing game screen size
win_x=800
win_y=600
screen=pygame.display.set_mode((win_x,win_y))
#obtaining images to be used in the game
pygame.display.set_caption("flappy birdy")
icon = pygame.image.load("space-invaders.png")  # change
pygame.display.set_icon(icon)

#player
birdImg = pygame.image.load("space-invaders.png")  # change
birdX=300
birdY=100
birdYchange=0
birdYspeed = .3

def bird(x,y):
    screen.blit(birdImg,(x,y))


running = True
while running:
    screen.fill((0,0,0))
#Reading coordinates which are obtained from arduino and changing the x and y values
    line = ser.readline()

    if line:
        string = line.decode()
        birdY=float(string)
#Setting commands for the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                birdYchange = -birdYspeed
            if event.key == pygame.K_DOWN:
                birdYchange = birdYspeed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                birdYchange = 0

    # birdY += birdYchange

    # if birdY >= win_y:
    #     birdY = win_y
    # elif birdY <= 0:
    #     birdY = 0
#Mapping the finger coordinates to respective bird movements
    bird(birdX, birdY*28)

    pygame.display.update()
