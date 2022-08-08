import RPi.GPIO as GPIO
import gpiozero as gpz
import time

#Set GPIO Pin Format
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#Setup the Hand Sensor inputs
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#Setup the Vent Magnet
GPIO.setup(24,GPIO.OUT)


#Magnet Initially On
GPIO.output(24,GPIO.HIGH)
magnet_on = GPIO.input(24)

while magnet_on: 
    cell_one_pressed = GPIO.input(17)
    cell_two_pressed = GPIO.input(27)
    
    # Both sensors "blocked" turn magent off
    if  (cell_one_pressed == False and cell_two_pressed == False):
        GPIO.output(24,GPIO.LOW)
        magnet_on = GPIO.input(24)
        
    


print("Exited")



            
            