import vlc
import RPi.GPIO as GPIO
import time
import os
import numpy as np


#Set GPIO pin format
GPIO.setmode(GPIO.BCM)

#Setup the GPIO buttons
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)


VIDEO_DIRECTORY = "/home/pi/Videos/"
STATIC_VIDEO = VIDEO_DIRECTORY + "tv static 1080hd 60fps.mp4"
BLUE_SCREEN_VIDEO = VIDEO_DIRECTORY + "WellBeRightBack_BlueScreen.mp4"


#Setup video destination variable
video_static = vlc.MediaPlayer(STATIC_VIDEO)
video_blue_screen = vlc.MediaPlayer(BLUE_SCREEN_VIDEO)

#Make boolean variables
Running = True

while Running:


    Tape_Input = GPIO.input(17)
    
    if  ( Tape_Input == True):
        video_blue_screen.stop()
        video_static.play()
        
        if (video_static.is_playing() == False) :
            video_static.stop()
            video_static.play()
            time.sleep(5)
        
    else:
        video_static.stop()
        video_blue_screen.play()
        
        if (video_blue_screen.is_playing() == False) :
            video_blue_screen.stop()
            video_blue_screen.play()
            time.sleep(5)
            
            