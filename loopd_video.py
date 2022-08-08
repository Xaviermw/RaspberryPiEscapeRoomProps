import vlc
import time
import RPi.GPIO as GPIO

#Set GPIO pin format
GPIO.setmode(GPIO.BCM)

#Setup the GPIO buttons
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#Make boolean variables
Tape_Input = GPIO.input(17)
running = True

#creating instance class object
player = vlc.Instance()

#creating a new media list
media_list = player.media_list_new()

#creating media player object
media_player = player.media_list_player_new()

#creating a new media
media = player.media_new("WellBeRightBack_BlueScreen.mp4")

#adding media to the media list 
media_list.add_media(media)

#setting media list to the media player
media_player.set_media_list(media_list)

#setting the loop
player.vlm_set_loop("WellBeRightBack_BlueScreen", True)

#start plsying thed video
while Tape_Input:
    media_player.play()

#
     time.sleep(2)
   

# if (Tape_Input == False):
#     print("pin is false")
#     media_player.stop()