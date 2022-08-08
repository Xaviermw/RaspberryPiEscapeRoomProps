import vlc
import RPi.GPIO as GPIO

#Set GPIO pin format
GPIO.setmode(GPIO.BCM)

#Setup the GPIO buttons
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#Make boolean variables
Tape_Input = GPIO.input(17)
Running = True

#Video Play Function*************************************************************
def video(source):
    
    #Create a VLC instance
    vlc_instance = vlc.Instance()
    
    #Create the media player
    player = vlc_instance.media_player_new()
    
    #Create the media
    media = vlc_instance.media_new(source)
    
    #Set media to the player
    player.set_media(media)
    
    #Play the video
    player.play()
#********************************************************************************
while (Tape_Input == True):
    print("Pin is True")
    #video("/home/pi/Videos/tv static 1080hd 60fps.mp4")
    # video("/home/pi/Videos/WellBeRightBack_BlueScreen.mp4")
# else:
#     print("Pin is False")
#     video("/home/pi/Videos/WellBeRightBack_BlueScreen.mp4")